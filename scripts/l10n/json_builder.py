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
"""Build an intermediate JSON file mapping holiday strings across all locales.

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
    * scripts/l10n/holidays_intermediate.json
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
    """Builds and manages the intermediate JSON file mapping holiday strings across all locales."""

    _locale_path: Path = Path("holidays/locale")
    _output_path: Path = Path("scripts/l10n/holidays_intermediate.json")
    _backup_path: Path = Path("scripts/l10n/holidays_intermediate.json.bak")

    @staticmethod
    def _deduplicate_ids(grouped: dict) -> None:
        """Ensure all IDs are unique by appending a counter to duplicates."""
        counts = Counter(entry["id"] for entry in grouped.values())
        seen: defaultdict[str, int] = defaultdict(int)
        for entry in sorted(grouped.values(), key=lambda x: x["comment"]):
            if counts[base_id := entry["id"]] > 1:
                seen[base_id] += 1
                entry["id"] = f"{base_id}_{seen[base_id]}"

    @staticmethod
    def _flatten_messages(messages: dict) -> dict:
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

    @staticmethod
    def _get_msgid(messages: dict, override: str | None = None) -> str:
        """Derive msgid from en_US translation or use explicit override."""
        if override:
            return override
        en_us = messages.get("en_US", "")
        if isinstance(en_us, dict):
            en_us = next(iter(en_us.values()), "")
        return en_us.removesuffix(".")

    @staticmethod
    def _remove_countries_from_messages(messages: dict, countries: set) -> dict:
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
                cleaned[lang] = val
        return cleaned

    @staticmethod
    def _extract_group_messages(
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

    @staticmethod
    def _build_lang_country_map() -> dict[str, set[str]]:
        """Map each language code to the set of countries that use it."""
        lang_countries: dict[str, set[str]] = defaultdict(set)
        for po_path in IntermediateJsonBuilder._locale_path.rglob("*.po"):
            lang_countries[po_path.parents[1].name].add(po_path.stem)
        return lang_countries

    @staticmethod
    def _backup() -> None:
        """Save a backup of the existing JSON before overwriting."""
        if IntermediateJsonBuilder._output_path.exists():
            shutil.copy2(
                IntermediateJsonBuilder._output_path,
                IntermediateJsonBuilder._backup_path,
            )
            print(f"Backup saved to: {IntermediateJsonBuilder._backup_path}")

    @staticmethod
    def _merge_with_existing(fresh: list, existing_path: Path) -> list:
        """Merge fresh build with existing JSON, preserving manual edits and split entries."""
        if not existing_path.exists():
            return fresh

        with existing_path.open(encoding="utf-8") as f:
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
            source["messages"] = IntermediateJsonBuilder._remove_countries_from_messages(
                source["messages"], countries
            )

        fresh.extend(split_entries)
        return sorted(fresh, key=lambda x: x["id"])

    @staticmethod
    def _build(*, refresh: bool = False) -> None:
        """Build or update the intermediate JSON file."""
        grouped: dict[str, dict] = {}

        for po_file_path in IntermediateJsonBuilder._locale_path.rglob("*.po"):
            lang = po_file_path.parents[1].name
            country_code = po_file_path.stem
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

        IntermediateJsonBuilder._deduplicate_ids(grouped)

        output = sorted(grouped.values(), key=lambda x: x["id"])
        for entry in output:
            entry["messages"] = IntermediateJsonBuilder._flatten_messages(entry["messages"])
            entry["countries"] = sorted(entry["countries"])
            entry["msgid"] = IntermediateJsonBuilder._get_msgid(entry["messages"])

        IntermediateJsonBuilder._backup()

        if not refresh:
            output = IntermediateJsonBuilder._merge_with_existing(
                output, IntermediateJsonBuilder._output_path
            )

        IntermediateJsonBuilder._output_path.resolve().write_text(
            json.dumps(output, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )

        print(f"Total unique holidays: {len(output)}")
        print(f"Saved to: {IntermediateJsonBuilder._output_path}")

    @staticmethod
    def _split(
        comment: str,
        country_codes: set[str],
        new_id: str | None = None,
        msgid: str | None = None,
    ) -> None:
        """Split a holiday entry into a country-specific dedicated msgid."""
        if not IntermediateJsonBuilder._output_path.exists():
            print(
                f"Error: {IntermediateJsonBuilder._output_path} not found."
                " Run json_builder.py first."
            )
            sys.exit(1)

        with IntermediateJsonBuilder._output_path.open(encoding="utf-8") as f:
            data = json.load(f)

        source = next(
            (e for e in data if e["comment"] == comment and country_codes <= set(e["countries"])),
            None,
        )

        if not source:
            print(f"Error: no entry found with comment {comment!r} containing {country_codes}")
            sys.exit(1)

        lang_countries = IntermediateJsonBuilder._build_lang_country_map()
        entry_id = new_id or _ID_RE.sub(
            "_",
            f"{comment} {' '.join(sorted(country_codes))}".lower(),
        ).strip("_")

        new_messages = IntermediateJsonBuilder._extract_group_messages(
            source["messages"], country_codes, lang_countries
        )

        new_entry = {
            "id": entry_id,
            "msgid": IntermediateJsonBuilder._get_msgid(new_messages, msgid),
            "comment": comment,
            "messages": new_messages,
            "countries": sorted(country_codes),
        }

        source["messages"] = IntermediateJsonBuilder._remove_countries_from_messages(
            source["messages"], country_codes
        )
        source["countries"] = sorted(set(source["countries"]) - country_codes)

        data.append(new_entry)
        data.sort(key=lambda x: x["id"])

        IntermediateJsonBuilder._output_path.resolve().write_text(
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

    @staticmethod
    def run() -> None:
        """Parse arguments and run the build or split process."""
        arg_parser = argparse.ArgumentParser(
            description="Build intermediate JSON from .po translation files."
        )
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
        args = arg_parser.parse_args()

        if args.split:
            if len(args.split) < 2:
                arg_parser.error("--split requires a comment and at least one country code")
            IntermediateJsonBuilder._split(
                comment=args.split[0],
                country_codes=set(args.split[1:]),
                new_id=args.new_id,
                msgid=args.msgid,
            )
        else:
            IntermediateJsonBuilder._build(refresh=args.refresh)


if __name__ == "__main__":
    IntermediateJsonBuilder.run()
