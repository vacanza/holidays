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

"""Build a JSON file mapping holiday strings across all locales.

Run with:
    python scripts/l10n/json_builder.py

To rebuild from scratch, replacing the existing file:
    python scripts/l10n/json_builder.py --refresh

To split a holiday entry into a country-specific dedicated msgid:
    python scripts/l10n/json_builder.py --split <comment> <country_code> [<country_code> ...]
        --new-id <new_id> --msgid <msgid>

Examples:
    python scripts/l10n/json_builder.py --split "Epiphany." SK --new-id epiphany_sk
    python scripts/l10n/json_builder.py --split "New Year's Day." CN KR LA VN
        --new-id international_new_year --msgid "International New Year"

This generates the file:
    * scripts/l10n/holidays_l10n.json

A backup of the previous file is saved to:
    * scripts/l10n/holidays_l10n.json.bak
"""

import argparse
import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

from polib import pofile

_ID_RE = re.compile(r"[^a-z0-9]+")


class IntermediateJsonBuilder:
    """Builds and manages the JSON file mapping holiday strings across all locales."""

    def __init__(self) -> None:
        arg_parser = argparse.ArgumentParser(description="Build JSON from .po translation files.")
        mode = arg_parser.add_mutually_exclusive_group()
        mode.add_argument(
            "--refresh",
            action="store_true",
            help="Rebuild from scratch, replacing the existing file after backup.",
        )
        mode.add_argument(
            "--split",
            nargs="+",
            metavar="ARG",
            help="Split a holiday entry: <comment> <country_code> [<country_code> ...]",
        )
        arg_parser.add_argument(
            "--new-id",
            help="New ID for the split entry (auto-generated if not provided)",
            type=str,
        )
        arg_parser.add_argument(
            "--msgid",
            help="Explicit msgid for the split entry (derived from en_US if not provided)",
            type=str,
        )
        self.args = arg_parser.parse_args()

        self.locale_path = Path("holidays/locale")
        self.output_path = Path("scripts/l10n/holidays_l10n.json")
        self.backup_path = Path("scripts/l10n/holidays_l10n.json.bak")
        self.lang_countries: dict[str, set[str]] = {}
        for po_path in self.locale_path.rglob("*.po"):
            self.lang_countries.setdefault(po_path.parents[1].name, set()).add(po_path.stem)

    def _make_id(self, text: str) -> str:
        return _ID_RE.sub("_", text.lower()).strip("_")

    def _deduplicate_ids(self, grouped: dict) -> None:
        """Ensure all IDs are unique by appending a counter to duplicates."""
        counts = Counter(entry["id"] for entry in grouped.values())
        seen: defaultdict[str, int] = defaultdict(int)
        for entry in sorted(grouped.values(), key=lambda x: x["comment"]):
            if counts[base_id := entry["id"]] > 1:
                seen[base_id] += 1
                entry["id"] = f"{base_id}_{seen[base_id]}"

    def _get_msgid(self, messages: dict) -> str:
        """Derive msgid from en_US translation or use explicit override."""
        en_us = messages.get("en_US", "")
        if isinstance(en_us, dict):
            en_us = next(iter(en_us.values()), "")
        return en_us.removesuffix(".")

    def _flatten_translation_dict(self, translations: dict[str, str]) -> str | dict[str, str]:
        values = iter(translations.values())
        first = next(values)
        return first if all(v == first for v in values) else translations

    def _filter_messages(self, messages: dict, countries: set[str], *, include: bool) -> dict:
        """Keep or remove translations for the specified countries."""
        result = {}
        for lang, value in messages.items():
            if isinstance(value, dict):
                filtered = {
                    country: translation
                    for country, translation in value.items()
                    if (country in countries) == include
                }
                if filtered:
                    result[lang] = self._flatten_translation_dict(filtered)
            else:
                filtered_countries = (
                    self.lang_countries[lang] & countries
                    if include
                    else self.lang_countries[lang] - countries
                )
                if filtered_countries:
                    result[lang] = value

        return result

    def _flatten_messages(self, messages: dict) -> dict:
        """Flatten per-country messages to a single string where all countries agree."""
        return {
            lang: self._flatten_translation_dict(dict(sorted(translations.items())))
            for lang, translations in sorted(messages.items())
        }

    def _remove_countries_from_messages(self, messages: dict, countries: set[str]) -> dict:
        """Remove countries from nested language dicts, reflattening where possible."""
        return self._filter_messages(messages, countries, include=False)

    def _extract_group_messages(self, messages: dict, countries: set[str]) -> dict:
        """Extract translations relevant to a group of countries."""
        return self._filter_messages(messages, countries, include=True)

    def _merge_with_existing(self, fresh: list) -> list:
        """Merge fresh build with existing JSON, preserving manual edits and split entries."""
        if not self.output_path.exists():
            return fresh

        with self.output_path.open(encoding="utf-8") as f:
            existing = json.load(f)

        existing_by_comment = {
            entry["comment"]: entry
            for entry in existing
            if entry["id"] == self._make_id(entry["comment"])
        }

        for entry in fresh:
            if existing_entry := existing_by_comment.get(entry["comment"]):
                entry["id"] = existing_entry["id"]
                entry["new_comment"] = existing_entry["new_comment"]

        fresh_comments = {entry["comment"] for entry in fresh}
        fresh_ids = {entry["id"] for entry in fresh}

        split_entries = [
            e for e in existing if e["comment"] in fresh_comments and e["id"] not in fresh_ids
        ]

        fresh_by_comment = {e["comment"]: e for e in fresh}
        split_countries: dict[str, set] = defaultdict(set)
        for split_entry in split_entries:
            split_countries[split_entry["comment"]].update(split_entry["countries"])

        for comment, countries in split_countries.items():
            if comment not in fresh_by_comment:
                continue
            source = fresh_by_comment[comment]
            source["countries"] -= countries
            source["messages"] = self._remove_countries_from_messages(
                source["messages"], countries
            )

        return fresh + split_entries

    def out_to_file(self, output: list) -> None:
        for entry in output:
            entry["countries"] = sorted(entry["countries"])
        output.sort(key=lambda x: x["id"])
        self.output_path.write_text(  # NOSONAR
            json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
        )

    def _build(self) -> None:
        """Build or update the JSON file."""
        grouped: dict[str, dict] = {}
        for lang, countries in self.lang_countries.items():
            for country_code in countries:
                po_file_path = self.locale_path / lang / "LC_MESSAGES" / f"{country_code}.po"
                for po_entry in pofile(str(po_file_path)):
                    translation = po_entry.msgstr or po_entry.msgid
                    comment = po_entry.comment
                    entry = grouped.setdefault(
                        comment,
                        {
                            "id": self._make_id(comment),
                            "msgid": "",
                            "new_comment": "",
                            "comment": comment,
                            "messages": {},
                            "countries": set(),
                        },
                    )
                    entry["messages"].setdefault(lang, {})[country_code] = translation
                    entry["countries"].add(country_code)

        self._deduplicate_ids(grouped)

        output = list(grouped.values())
        for entry in output:
            entry["messages"] = self._flatten_messages(entry["messages"])
            entry["msgid"] = self._get_msgid(entry["messages"])

        if self.output_path.exists():
            shutil.copy(self.output_path, self.backup_path)
            print(f"Backup saved to: {self.backup_path}")
            print("Note: if you have split entries, compare with the backup.")

        if not self.args.refresh:
            output = self._merge_with_existing(output)

        self.out_to_file(output)
        print(f"Total unique holidays: {len(output)}")
        print(f"Saved to: {self.output_path}")

    def _split(self) -> None:
        """Split a holiday entry into a country-specific dedicated msgid."""
        if not self.output_path.exists():
            print(f"Error: {self.output_path} not found. Run json_builder.py first.")
            sys.exit(1)

        with self.output_path.open(encoding="utf-8") as f:
            data = json.load(f)

        comment = self.args.split[0]
        country_codes = set(self.args.split[1:])

        source = next(
            (e for e in data if e["comment"] == comment and country_codes <= set(e["countries"])),
            None,
        )
        if not source:
            print(f"Error: no entry found with comment {comment!r} containing {country_codes}")
            sys.exit(1)

        entry_id = self.args.new_id or self._make_id(
            f"{comment} {' '.join(sorted(country_codes))}"
        )
        new_messages = self._extract_group_messages(source["messages"], country_codes)
        new_entry = {
            "id": entry_id,
            "msgid": self.args.msgid or self._get_msgid(new_messages),
            "new_comment": f"??? {source['new_comment']}" if source["new_comment"] else "",
            "comment": comment,
            "messages": new_messages,
            "countries": country_codes,
        }

        source["messages"] = self._remove_countries_from_messages(
            source["messages"], country_codes
        )
        source["countries"] = set(source["countries"]) - country_codes

        data.append(new_entry)
        self.out_to_file(data)

        print(f"Split {sorted(country_codes)} from {comment!r}")
        print(f"New entry ID: {entry_id}")
        print(f"New entry msgid: {new_entry['msgid']}")
        print(f"Remaining countries in source: {len(source['countries'])}")
        print(f"Countries in new entry: {len(new_entry['countries'])}")
        print(f"Languages in new entry: {len(new_entry['messages'])}")

    def run(self) -> None:
        """Parse arguments and run the build or split process."""
        if self.args.split:
            if len(self.args.split) < 2:
                print("Error: --split requires a comment and at least one country code")
                sys.exit(1)
            self._split()
        else:
            self._build()


if __name__ == "__main__":
    IntermediateJsonBuilder().run()
