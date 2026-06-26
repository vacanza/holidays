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
import copy
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

    def _deduplicate_ids(self, grouped: dict) -> None:
        """Ensure all IDs are unique by appending a counter to duplicates."""
        counts = Counter(entry["id"] for entry in grouped.values())
        seen: defaultdict[str, int] = defaultdict(int)
        for entry in sorted(grouped.values(), key=lambda x: x["comment"]):
            if counts[base_id := entry["id"]] > 1:
                seen[base_id] += 1
                entry["id"] = f"{base_id}_{seen[base_id]}"

    def _flatten_messages(self, messages: dict) -> dict:
        """Flatten per-country messages to a single string where all countries agree."""
        flattened = {}
        for lang, translations in messages.items():
            values = iter(translations.values())
            first = next(values)
            if all(v == first for v in values):
                flattened[lang] = first
            else:
                flattened[lang] = dict(sorted(translations.items()))
        return dict(sorted(flattened.items()))

    def _get_msgid(self, messages: dict, override: str | None = None) -> str:
        """Derive msgid from en_US translation or use explicit override."""
        if override:
            return override
        en_us = messages.get("en_US", "")
        if isinstance(en_us, dict):
            en_us = next(iter(en_us.values()), "")
        return en_us.removesuffix(".")

    def _build_lang_country_map(self) -> None:
        """Populate lang_countries map from locale .po file structure."""
        for po_path in self.locale_path.rglob("*.po"):
            self.lang_countries.setdefault(po_path.parents[1].name, set()).add(po_path.stem)

    def _remove_countries_from_messages(
        self,
        messages: dict,
        countries: set,
        lang_countries: dict[str, set[str]] | None = None,
    ) -> dict:
        """Remove countries from nested language dicts, reflattening where possible."""
        cleaned = {}
        for lang, val in messages.items():
            if isinstance(val, dict):
                remaining = {k: v for k, v in val.items() if k not in countries}
                if not remaining:
                    continue
                unique = set(remaining.values())
                cleaned[lang] = next(iter(unique)) if len(unique) == 1 else remaining
            else:
                if lang_countries:
                    lang_owners = lang_countries.get(lang, set())
                    if lang_owners and lang_owners <= countries:
                        continue
                cleaned[lang] = val
        return cleaned

    def _extract_group_messages(
        self,
        messages: dict,
        country_codes: set[str],
        lang_countries: dict[str, set[str]],
    ) -> dict:
        """Extract translations relevant to a group of countries."""
        extracted = {}
        for lang, val in messages.items():
            if isinstance(val, dict):
                group_translations = {k: v for k, v in val.items() if k in country_codes}
                if not group_translations:
                    continue
                unique = set(group_translations.values())
                extracted[lang] = next(iter(unique)) if len(unique) == 1 else group_translations
            else:
                if lang_countries.get(lang, set()) & country_codes:
                    extracted[lang] = val
        return extracted

    def _sort_entries(self, entries: list) -> list:
        """Sort holiday entries by ID."""
        return sorted(entries, key=lambda x: x["id"])

    def _backup(self) -> None:
        """Save a backup of the existing JSON before overwriting."""
        if self.output_path.exists():
            shutil.copy2(self.output_path, self.backup_path)
            print(f"Backup saved to: {self.backup_path}")
            print("Note: if you have split entries, compare with the backup.")

    def _merge_with_existing(self, fresh: list) -> list:
        """Merge fresh build with existing JSON, preserving manual edits and split entries."""
        if not self.output_path.exists():
            return self._sort_entries(fresh)

        with self.output_path.open(encoding="utf-8") as f:
            existing = json.load(f)

        fresh_comments = {entry["comment"] for entry in fresh}
        fresh_ids = {entry["id"] for entry in fresh}

        existing_by_comment = {
            entry["comment"]: entry
            for entry in existing
            if entry["id"] == _ID_RE.sub("_", entry["comment"].lower()).strip("_")
        }

        for entry in fresh:
            if existing_entry := existing_by_comment.get(entry["comment"]):
                entry["id"] = existing_entry["id"]

        split_entries = [
            copy.deepcopy(e)
            for e in existing
            if e["comment"] in fresh_comments and e["id"] not in fresh_ids
        ]

        fresh_by_comment = {e["comment"]: e for e in fresh}
        split_countries: dict[str, set] = defaultdict(set)
        for split_entry in split_entries:
            split_countries[split_entry["comment"]].update(split_entry["countries"])

        for comment, countries in split_countries.items():
            if comment not in fresh_by_comment:
                continue
            source = fresh_by_comment[comment]
            source["countries"] = sorted(set(source["countries"]) - countries)
            source["messages"] = self._remove_countries_from_messages(
                source["messages"], countries, self.lang_countries
            )

        fresh.extend(split_entries)
        return self._sort_entries(fresh)

    def _build(self) -> None:
        """Build or update the JSON file."""
        grouped: dict[str, dict] = {}

        for po_file_path in self.locale_path.rglob("*.po"):
            lang = po_file_path.parents[1].name
            country_code = po_file_path.stem
            self.lang_countries.setdefault(lang, set()).add(country_code)
            po = pofile(str(po_file_path))

            for po_entry in po:
                translation = po_entry.msgstr or po_entry.msgid
                comment = po_entry.comment
                entry = grouped.setdefault(
                    comment,
                    {
                        "id": _ID_RE.sub("_", comment.lower()).strip("_"),
                        "msgid": "",
                        "comment": comment,
                        "messages": {},
                        "countries": set(),
                    },
                )
                entry["messages"].setdefault(lang, {})[country_code] = translation
                entry["countries"].add(country_code)

        self._deduplicate_ids(grouped)

        output = self._sort_entries(list(grouped.values()))
        for entry in output:
            entry["messages"] = self._flatten_messages(entry["messages"])
            entry["countries"] = sorted(entry["countries"])
            entry["msgid"] = self._get_msgid(entry["messages"])

        self._backup()

        if not self.args.refresh:
            output = self._merge_with_existing(output)

        self.output_path.write_text(
            json.dumps(output, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )

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

        self._build_lang_country_map()
        entry_id = self.args.new_id or _ID_RE.sub(
            "_",
            f"{comment} {' '.join(sorted(country_codes))}".lower(),
        ).strip("_")

        new_messages = self._extract_group_messages(
            source["messages"], country_codes, self.lang_countries
        )

        new_entry = {
            "id": entry_id,
            "msgid": self._get_msgid(new_messages, self.args.msgid),
            "comment": comment,
            "messages": new_messages,
            "countries": sorted(country_codes),
        }

        source["messages"] = self._remove_countries_from_messages(
            source["messages"], country_codes, self.lang_countries
        )
        source["countries"] = sorted(set(source["countries"]) - country_codes)

        data.append(new_entry)
        data = self._sort_entries(data)

        self.output_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )

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
