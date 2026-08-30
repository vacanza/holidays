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
    * holidays/locale/holidays.pot  - master template with all msgids
    * holidays/locale/{lang}.po  - one per language
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

from polib import POEntry, POFile

sys.path.insert(0, str(Path.cwd()))
from holidays import __version__ as package_version

JSON_PATH = Path("scripts/l10n/holidays_l10n.json")
LOCALE_PATH = Path("holidays/locale")
HEADER_PATH = Path("docs/file_header.txt")
POT_FILENAME = "holidays.pot"
WRAP_WIDTH = 99
MSGID_BUGS_ADDRESS = "l10n@vacanza.dev"
TRANSLATOR_PATTERN = re.compile(r"[^\s<]+(?:\s+[^\s<]+)*\s+<[^@\s<]+@[^@\s<.]+(?:\.[^@\s<.]+)+>")


class LocalePOGenerator:
    """Generates per-locale .pot and .po files from the JSON."""

    def __init__(self) -> None:
        if not JSON_PATH.exists():
            raise FileNotFoundError(f"{JSON_PATH} not found!")
        with JSON_PATH.open(encoding="utf-8") as f:
            self.data: list[dict] = json.load(f)

        self.timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M%z")
        self.license_header = self._get_license_header()

    @staticmethod
    def _get_license_header() -> str:
        """Read and format the license header from docs/file_header.txt."""
        content = HEADER_PATH.read_text(encoding="utf-8").lstrip("\n")
        return (
            "\n".join(
                f"# {stripped}" if (stripped := line.rstrip()) else "#"
                for line in content.splitlines()
            )
            + "\n#"
        )

    def _make_metadata(self, lang: str | None = None) -> dict:
        """Build standard Gettext metadata for a .po or .pot file."""
        return {
            "Project-Id-Version": f"Holidays {package_version}",
            "Report-Msgid-Bugs-To": MSGID_BUGS_ADDRESS,
            "POT-Creation-Date": self.timestamp,
            "PO-Revision-Date": self.timestamp,
            "Last-Translator": f"Holidays Localization Team <{MSGID_BUGS_ADDRESS}>",
            "Language-Team": "Holidays Localization Team",
            "Language": lang or "en",
            "MIME-Version": "1.0",
            "Content-Type": "text/plain; charset=UTF-8",
            "Content-Transfer-Encoding": "8bit",
            "X-Source-Language": "en",
        }

    def _write_po_header(self, po_path: Path, lang: str | None) -> None:
        """Prepend the license header to a written .po file."""
        output = [
            self.license_header,
            f"# Holidays {lang} localization." if lang else "# Holidays localization.",
            "#",
            po_path.read_text(encoding="utf-8"),
        ]
        po_path.write_text("\n".join(output), encoding="utf-8", newline="\n")

    def _build_po(self, lang: str | None = None) -> None:
        """Build a per-locale .po file for a given language."""
        po = POFile(wrapwidth=WRAP_WIDTH)
        po.metadata = self._make_metadata(lang)

        for entry in self.data:
            po.append(
                POEntry(
                    msgid=entry["msgid"],
                    msgstr=entry["messages"].get(lang) or "",
                    comment=entry.get("new_comment"),
                    flags=["c-format"] if "%" in entry["msgid"] else [],
                )
            )

        po_path = LOCALE_PATH / (f"{lang}.po" if lang else POT_FILENAME)
        po.save(str(po_path), newline="\n")
        self._write_po_header(po_path, lang)
        print(f"Saved {po_path} ({len(po)} entries)")

    def _collect_languages(self) -> set[str]:
        """Collect all language codes present across all entries."""
        langs: set[str] = set()
        for entry in self.data:
            for lang, val in entry["messages"].items():
                if isinstance(val, str):
                    langs.add(lang)
                else:
                    raise ValueError(
                        f"Msgid `{entry['msgid']}` contains multiple translation for lang `{lang}`"
                    )

        return langs

    def run(self) -> None:
        """Generate the .pot and all per-locale .po files."""
        langs = self._collect_languages()
        # build .pot file.
        self._build_po()

        print(f"Generating .po files for {len(langs)} languages...")
        for lang in sorted(langs):
            self._build_po(lang)

        print("Done.")


if __name__ == "__main__":
    LocalePOGenerator().run()
