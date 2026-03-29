#!/usr/bin/env python3


#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import argparse
import csv
import importlib
import sys
from collections import defaultdict
from pathlib import Path

from polib import pofile

WRAP_WIDTH = 99


class LocalizationHelper:
    def __init__(self) -> None:
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument("country_code", help="Country code", type=str)
        arg_parser.add_argument("--create-po", action="store_true", help="Create .po files")
        arg_parser.add_argument("--export-csv", action="store_true", help="Export to .csv")
        arg_parser.add_argument("--import-csv", action="store_true", help="Import from .csv")
        arg_parser.add_argument(
            "--fill-missing",
            action="store_true",
            help="Fill missing translations from other countries",
        )
        arg_parser.add_argument(
            "--bom",
            action=argparse.BooleanOptionalAction,
            default=False,
            help="Use files with BOM on export/import",
        )
        arg_parser.add_argument(
            "--overwrite",
            action=argparse.BooleanOptionalAction,
            default=False,
            help="Overwrite existing files",
        )
        arg_parser.add_argument(
            "--strict-locale",
            action=argparse.BooleanOptionalAction,
            default=True,
            help="Use strict locale when searching for suitable translations",
        )
        self.args = arg_parser.parse_args()
        if not any(
            getattr(self.args, action.dest)
            for action in arg_parser._actions
            if isinstance(action, argparse._StoreTrueAction)
        ):
            print("No action specified.\n")
            arg_parser.print_help()
            sys.exit(1)

        self.country_code = self.args.country_code
        self.encoding = "utf-8-sig" if self.args.bom else "utf-8"
        self.csv_file_path = Path(f"holidays/locale/csv/{self.country_code}.csv")

    def create_po_files(self):
        sys.path.append(str(Path.cwd()))  # Make holidays visible.
        from holidays.registry import COUNTRIES

        class_name = None
        for module_name, entity_data in COUNTRIES.items():
            if entity_data[1] == self.country_code:
                class_name = entity_data[0]
                break
        if not class_name:
            print(f"Class for country code {self.country_code} not found!")
            sys.exit(1)

        cls = getattr(importlib.import_module(f"holidays.countries.{module_name}"), class_name)
        docstring = cls.__doc__

        header = [
            f"# {line}" if line else "#"
            for line in Path("docs/file_header.txt").read_text(encoding="utf-8").split("\n")
        ]
        country_name = "COUNTRY"
        if (title := docstring.split("\n")[0]) and title.endswith(" holidays."):
            country_name = title.split("holidays")[0].strip()

        locale_directory = Path("holidays/locale")
        pot_file_path = locale_directory / "pot" / f"{self.country_code}.pot"
        pot_file = pofile(pot_file_path, wrapwidth=WRAP_WIDTH)
        for entry in pot_file:
            entry.occurrences.clear()

        for language in cls.supported_languages:
            po_directory = locale_directory / language / "LC_MESSAGES"
            po_directory.mkdir(parents=True, exist_ok=True)
            po_file_path = po_directory / f"{self.country_code}.po"
            if not self.args.overwrite and po_file_path.exists():
                continue
            pot_file.metadata["Language"] = language
            pot_file.save(po_file_path, newline="\n")

            file_content = po_file_path.read_text(encoding="utf-8").split("\n")
            if file_content[0] != "# SOME DESCRIPTIVE TITLE":
                continue
            l10n_suffix = f" {language} localization" if language != cls.default_language else ""
            title = f"# {country_name} holidays{l10n_suffix}."
            file_content = header + [title, "#"] + file_content[4:]
            po_file_path.write_text("\n".join(file_content), encoding="utf-8", newline="\n")

        if cls.default_language == "en_US":
            return None

        en_us_po_path = locale_directory / "en_us/LC_MESSAGES" / f"{self.country_code}.po"
        po_file = pofile(en_us_po_path, wrapwidth=WRAP_WIDTH)
        for po_entry in po_file:
            if po_entry.comment:
                po_entry.msgstr = po_entry.comment.removesuffix(".")
        po_file.save(en_us_po_path, newline="\n")

    def export_to_csv(self):
        if not self.args.overwrite and self.csv_file_path.exists():
            print(f"File {self.csv_file_path} exists and no --overwrite option!")
            sys.exit(1)

        comments = {}
        languages = []
        po_data = defaultdict(dict)
        for po_path in Path("holidays/locale").rglob(f"{self.country_code}.po"):
            po_file = pofile(po_path, wrapwidth=WRAP_WIDTH)
            language = po_file.metadata["Language"]
            default_language = po_file.metadata["X-Source-Language"]
            if language != default_language:
                languages.append(language)
                for po_entry in po_file:
                    po_data[po_entry.msgid][language] = po_entry.msgstr
            else:
                for po_entry in po_file:
                    comments[po_entry.msgid] = po_entry.comment

        languages = sorted(languages)
        headers = ["msgid", "msgcomment", *languages]
        rows = [
            [msgid, comments[msgid]] + [po_data[msgid][language] for language in languages]
            for msgid in po_data
        ]
        self.write_csv(headers, rows)

    def read_csv(self) -> tuple[list[str], list[list[str]]]:
        if not self.csv_file_path.exists():
            print(f"File {self.csv_file_path} not found!")
            sys.exit(1)

        with self.csv_file_path.open("r", encoding=self.encoding) as f:
            reader = csv.reader(f, delimiter=";")
            headers, *rows = reader
        return headers, rows

    def write_csv(self, headers: list[str], rows: list[list[str]]):
        self.csv_file_path.parent.mkdir(parents=True, exist_ok=True)
        with self.csv_file_path.open("w", newline="", encoding=self.encoding) as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(headers)
            writer.writerows(rows)

    def import_from_csv(self):
        headers, rows = self.read_csv()
        languages = headers[2:]
        entries = [(msgid, dict(zip(languages, msgstrs))) for msgid, _, *msgstrs in rows]

        for language in languages:
            po_path = Path(f"holidays/locale/{language}/LC_MESSAGES/{self.country_code}.po")
            po_file = pofile(po_path, wrapwidth=WRAP_WIDTH)

            changed = False
            for msgid, msg_mapping in entries:
                entry = po_file.find(msgid)
                if not entry:
                    continue
                msgstr = msg_mapping[language]
                if entry.msgstr != msgstr:
                    entry.msgstr = msgstr
                    if "|" in msgstr:
                        entry.flags.append("fuzzy")
                    changed = True

            if changed:
                po_file.save(po_path, newline="\n")

    def fill_missing_translations(self):
        headers, rows = self.read_csv()
        languages = headers[2:]

        untranslated_languages = set()
        for row in rows:
            msgstrs = row[2:]
            for lang, msgstr in zip(languages, msgstrs):
                if not msgstr.strip():
                    untranslated_languages.add(lang)

        locale_path = Path("holidays/locale")
        translations = {language: defaultdict(set) for language in untranslated_languages}
        for language in untranslated_languages:
            language_prefix = language if self.args.strict_locale else language.split("_")[0]
            for po_path in locale_path.rglob("LC_MESSAGES/*.po"):
                if po_path.stem == self.country_code:
                    continue
                language_dir = po_path.parent.parent.name
                if not (
                    language_dir == language_prefix
                    if self.args.strict_locale
                    else language_dir.startswith(language_prefix)
                ):
                    continue
                po_file = pofile(po_path, wrapwidth=WRAP_WIDTH)
                for entry in po_file:
                    if entry.comment:
                        translations[language][entry.comment].add(entry.msgstr or entry.msgid)

        updated_rows = []
        for msgid, msgcomment, *msgstrs in rows:
            new_msgstrs = []
            for lang, msgstr in zip(languages, msgstrs):
                if msgstr.strip():
                    new_msgstrs.append(msgstr)
                elif msgcomment in translations[lang]:
                    new_msgstrs.append(" | ".join(sorted(translations[lang][msgcomment])))
                else:
                    new_msgstrs.append("")

            updated_rows.append([msgid, msgcomment, *new_msgstrs])

        self.write_csv(headers, updated_rows)

    def run(self):
        if self.args.create_po:
            self.create_po_files()
        elif self.args.export_csv:
            self.export_to_csv()
        elif self.args.import_csv:
            self.import_from_csv()
        elif self.args.fill_missing:
            self.fill_missing_translations()


if __name__ == "__main__":
    LocalizationHelper().run()
