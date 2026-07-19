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

"""Generate per-locale .pot and .po files from the JSON file.

Run with:
    python scripts/l10n/generate_locale_po_files.py

This generates:
    * scripts/l10n/holidays.pot  - master template with all msgids
    * holidays/locale/{lang}/LC_MESSAGES/holidays.po  - one per language
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

from git import Repo, exc
from polib import POEntry, POFile

from holidays import __version__ as package_version

sys.path.insert(0, str(Path.cwd()))


_JSON_PATH = Path("scripts/l10n/holidays_l10n.json")
_LOCALE_PATH = Path("holidays/locale")
_HEADER_PATH = Path("docs/file_header.txt")
_POT_PATH = Path("scripts/l10n/holidays.pot")
_PO_FILENAME = "holidays.po"
WRAP_WIDTH = 99
MSGID_BUGS_ADDRESS = "l10n@vacanza.dev"
TRANSLATOR_PATTERN = re.compile(r"[^\s<]+(?:\s+[^\s<]+)*\s+<[^@\s<]+@[^@\s<.]+(?:\.[^@\s<.]+)+>")


class LocalePOGenerator:
    """Generates per-locale .pot and .po files from the JSON."""

    def __init__(self) -> None:
        if not _JSON_PATH.exists():
            raise FileNotFoundError(f"{_JSON_PATH} not found. Run json_builder.py first.")
        with _JSON_PATH.open(encoding="utf-8") as f:
            self.data: list[dict] = json.load(f)

        self.data_by_msgid = {(e.get("msgid") or e.get("id", "")): e for e in self.data}
        self.timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M%z")
        self.author_identity = self._get_author_identity()
        self.license_header = self._get_license_header()

    def _get_author_identity(self) -> str:
        """Read author name and email from git config."""
        result = "FULL NAME <EMAIL@EXAMPLE.COM>"
        try:
            repo = Repo(Path(__file__).parents[2])
            config = repo.config_reader()
            name = config.get_value("user", "name", "")
            email = config.get_value("user", "email", "")
            if name and email and TRANSLATOR_PATTERN.fullmatch(identity := f"{name} <{email}>"):
                result = identity
        except exc.GitError:
            pass
        return result

    @staticmethod
    def _get_license_header() -> str:
        """Read and format the license header from docs/file_header.txt."""
        if not _HEADER_PATH.exists():
            return ""
        if not (content := _HEADER_PATH.read_text(encoding="utf-8").lstrip("\n")):
            return ""
        return (
            "\n".join(
                f"# {stripped}" if (stripped := line.rstrip()) else "#"
                for line in content.splitlines()
            )
            + "\n#"
        )

    def _make_comment(self, entry: dict) -> str:
        """Use new_comment if set, otherwise fall back to comment."""
        return entry.get("new_comment") or entry.get("comment", "")

    def _make_metadata(self, lang: str | None = None) -> dict:
        """Build standard Gettext metadata for a .po or .pot file."""
        last_translator = "FULL NAME <EMAIL@EXAMPLE.COM>" if lang is None else self.author_identity
        return {
            "Project-Id-Version": f"Holidays {package_version}",
            "Report-Msgid-Bugs-To": MSGID_BUGS_ADDRESS,
            "POT-Creation-Date": self.timestamp,
            "PO-Revision-Date": self.timestamp,
            "Last-Translator": last_translator,
            "Language-Team": "Holidays Localization Team",
            "Language": lang or "",
            "MIME-Version": "1.0",
            "Content-Type": "text/plain; charset=UTF-8",
            "Content-Transfer-Encoding": "8bit",
            "X-Source-Language": "en_US",
        }

    def _get_translation(self, messages: dict, lang: str) -> str | None:
        """Extract a flat translation string for a language from messages.

        Returns None if the language is not present. For nested dicts
        the translation is skipped - per-country variants are handled
        by the existing per-entity .po files.
        """
        val = messages.get(lang)
        if val is None:
            return None
        if isinstance(val, str):
            return val
        return None

    def _write_po_header(self, po_path: Path, lang: str) -> None:
        """Prepend the license header to a written .po file."""
        if not self.license_header:
            return
        content = po_path.read_text(encoding="utf-8")
        if content.startswith("#  holidays\n#  --------"):
            return
        desc_line = f"# Holidays {lang} localization."
        po_path.write_text(
            self.license_header + "\n" + desc_line + "\n#\n" + content,
            encoding="utf-8",
            newline="\n",
        )

    def _build_pot(self) -> POFile:
        """Build the master .pot template from all entries."""
        pot = POFile(wrapwidth=WRAP_WIDTH)
        pot.metadata = self._make_metadata()

        for entry in self.data:
            msgid = entry.get("msgid") or entry.get("id", "")
            if not msgid:
                continue
            pot.append(
                POEntry(
                    msgid=msgid,
                    msgstr="",
                    comment=self._make_comment(entry),
                )
            )

        return pot

    def _build_po(self, lang: str, pot: POFile) -> POFile:
        """Build a per-locale .po file for a given language."""
        po = POFile(wrapwidth=WRAP_WIDTH)
        po.metadata = self._make_metadata(lang)

        for pot_entry in pot:
            data_entry = self.data_by_msgid.get(pot_entry.msgid)
            if data_entry is None:
                continue
            translation = self._get_translation(data_entry["messages"], lang)
            if translation is None:
                continue
            po.append(
                POEntry(
                    msgid=pot_entry.msgid,
                    msgstr=translation,
                    comment=pot_entry.comment,
                )
            )

        return po

    def _collect_languages(self) -> set[str]:
        """Collect all language codes present across all entries."""
        langs: set[str] = set()
        for entry in self.data:
            for lang, val in entry.get("messages", {}).items():
                if isinstance(val, str):
                    langs.add(lang)
        return langs

    def _write_pot(self, pot: POFile) -> None:
        """Write the master .pot file."""
        _POT_PATH.parent.mkdir(parents=True, exist_ok=True)
        pot.save(str(_POT_PATH), newline="\n")
        print(f"Saved .pot: {_POT_PATH} ({len(pot)} entries)")

    def _write_po(self, lang: str, po: POFile) -> None:
        """Write a per-locale .po file."""
        if not len(po):
            return
        po_dir = _LOCALE_PATH / lang / "LC_MESSAGES"
        po_dir.mkdir(parents=True, exist_ok=True)
        po_path = po_dir / _PO_FILENAME
        po.save(str(po_path), newline="\n")
        self._write_po_header(po_path, lang)
        print(f"Saved .po: {po_path} ({len(po)} entries)")

    def run(self) -> None:
        """Generate the .pot and all per-locale .po files."""
        pot = self._build_pot()
        self._write_pot(pot)

        langs = self._collect_languages()
        print(f"Generating .po files for {len(langs)} languages...")

        for lang in sorted(langs):
            po = self._build_po(lang, pot)
            self._write_po(lang, po)

        print("Done.")


if __name__ == "__main__":
    LocalePOGenerator().run()
