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

import importlib
import inspect
import re
import sys
from concurrent.futures import ProcessPoolExecutor
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from time import perf_counter

from lingva.extract import extract as create_pot_file
from lingva.extract import _location_sort_key
from polib import POFile, pofile

sys.path.insert(0, str(Path.cwd()))  # Make holidays visible.
from holidays import __version__ as package_version
from holidays.registry import COUNTRIES, FINANCIAL

WRAP_WIDTH = 99
HEADER_PATH = Path("docs/file_header.txt")
MSGID_BUGS_ADDRESS = "l10n@vacanza.dev"
REQUIRED_METADATA_KEYS = frozenset(
    {
        "Project-Id-Version",
        "Report-Msgid-Bugs-To",
        "POT-Creation-Date",
        "PO-Revision-Date",
        "Last-Translator",
        "Language-Team",
        "Language",
        "MIME-Version",
        "Content-Type",
        "Content-Transfer-Encoding",
        "X-Source-Language",
    }
)

DATE_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}[+-]\d{4}")
TRANSLATOR_PATTERN = re.compile(r"[^\s<]+(?:\s+[^\s<]+)*\s+<[^@\s<]+@[^@\s<.]+(?:\.[^@\s<.]+)+>")


class POGenerator:
    """Generates .po files for supported country/market entities."""

    _license_header: str = ""
    _locale_path: Path = Path("holidays/locale")

    @staticmethod
    def _get_license_header() -> str:
        """Reads and formats the license header from docs/file_header.txt."""
        if not HEADER_PATH.exists():
            return ""

        if not (content := HEADER_PATH.read_text(encoding="utf-8").lstrip("\n")):
            return ""

        return (
            "\n".join(
                f"# {stripped}" if (stripped := line.rstrip()) else "#"
                for line in content.splitlines()
            )
            + "\n#"
        )

    @classmethod
    def _init_worker(cls, license_header: str) -> None:
        """Initialize worker with shared license header for multiprocessing."""
        cls._license_header = license_header

    @staticmethod
    def _apply_metadata(
        po_file: POFile, current_lang: str, default_language: str, timestamp: str
    ) -> None:
        """Applies metadata to a .po file."""
        forced_metadata = {
            "Project-Id-Version": f"Holidays {package_version}",
            "Report-Msgid-Bugs-To": MSGID_BUGS_ADDRESS,
            "PO-Revision-Date": timestamp,
            "Language-Team": "Holidays Localization Team",
            "Language": current_lang,
            "MIME-Version": "1.0",
            "Content-Type": "text/plain; charset=UTF-8",
            "Content-Transfer-Encoding": "8bit",
            "X-Source-Language": default_language,
        }
        default_metadata = {
            "POT-Creation-Date": timestamp,
            "Last-Translator": "FULL NAME <EMAIL@EXAMPLE.COM>",
        }
        po_file.metadata = default_metadata | po_file.metadata | forced_metadata

    @classmethod
    def _write_po_header(
        cls, po_path: Path, docstring: str, current_language: str, default_language: str
    ) -> None:
        """Strips gettext boilerplate and prepends the license header + desc line."""
        content = po_path.read_text(encoding="utf-8")
        content = (
            content.split("#, fuzzy", 1)[1].lstrip()
            if content.startswith("# SOME DESCRIPTIVE TITLE")
            else content.lstrip()
        )
        if content.startswith("#  holidays\n#  --------"):
            return

        desc_line = None
        if docstring:
            if display_name := docstring.split("\n", maxsplit=1)[0].removesuffix(" holidays."):
                lang_tag = (
                    f" {current_language} localization"
                    if current_language != default_language
                    else ""
                )
                desc_line = f"# {display_name} holidays{lang_tag}."

        parts = []
        if cls._license_header:
            parts.append(cls._license_header)
        if desc_line and desc_line not in content:
            parts.append(desc_line)
        if parts:
            parts.append("#\n")
            po_path.write_text(  # NOSONAR
                "\n".join(parts) + content, encoding="utf-8", newline="\n"
            )

    @staticmethod
    def _process_entity_worker(args: tuple[str, Path, tuple[str, ...]]) -> tuple[str, POFile]:
        """Process a single entity: create .pot, default .po, and return update tasks."""
        entity_code, class_file_path, supported_languages = args

        pot_path = POGenerator._locale_path / "pot"
        pot_path.mkdir(parents=True, exist_ok=True)
        pot_file_path = pot_path / f"{entity_code}.pot"

        create_pot_file(
            sources=[class_file_path],
            keywords=["tr"],
            output=pot_file_path,
            package_name="Holidays",
            package_version=package_version,
            width=WRAP_WIDTH,
            allow_empty=True,
            msgid_bugs_address=MSGID_BUGS_ADDRESS,
        )

        pot_file = pofile(str(pot_file_path), wrapwidth=WRAP_WIDTH)

        for lang in supported_languages:
            lang_directory = POGenerator._locale_path / lang / "LC_MESSAGES"
            lang_directory.mkdir(parents=True, exist_ok=True)
            lang_po_path = lang_directory / f"{entity_code}.po"

            if not lang_po_path.exists():
                pot_file.save(str(lang_po_path), newline="\n")

        return entity_code, pot_file

    @staticmethod
    def _update_po_file(args: tuple[Path, POFile, str, str]) -> None:
        """Merge .po file with .pot using strict no-change policies."""
        po_path, pot_file, default_language, entity_docstring = args
        po_path = po_path.resolve()
        current_lang = po_path.parent.parent.name

        po_file = pofile(str(po_path), wrapwidth=WRAP_WIDTH)
        po_file_initial = deepcopy(po_file)

        po_file.merge(pot_file)
        po_file.sort(key=_location_sort_key)
        for entry in po_file:
            entry.occurrences.clear()

        metadata = po_file.metadata
        for field_name in ("POT-Creation-Date", "PO-Revision-Date"):
            if not DATE_PATTERN.fullmatch(metadata.get(field_name, "")):
                metadata.pop(field_name, None)
        if not TRANSLATOR_PATTERN.fullmatch(metadata.get("Last-Translator", "")):
            metadata.pop("Last-Translator", None)

        if po_file != po_file_initial or not REQUIRED_METADATA_KEYS.issubset(metadata):
            POGenerator._apply_metadata(
                po_file,
                current_lang,
                default_language,
                datetime.now().astimezone().strftime("%Y-%m-%d %H:%M%z"),
            )
            po_file.save(str(po_path), newline="\n")

        POGenerator._write_po_header(po_path, entity_docstring, current_lang, default_language)

    @staticmethod
    def process_entities() -> None:
        """Processes entities in specified directory."""
        entities_data = {}
        entity_worker_data = []

        for entity_type, entity_mapping in (("countries", COUNTRIES), ("financial", FINANCIAL)):
            for path in Path(f"holidays/{entity_type}").glob("*.py"):
                if (mod_name := path.stem) == "__init__":
                    continue

                class_name, entity_code = entity_mapping[mod_name][0:2]
                mod = importlib.import_module(f"holidays.{entity_type}.{mod_name}")

                entity_cls = None
                for cls_name, cls in inspect.getmembers(mod, inspect.isclass):
                    if cls_name == class_name and cls.default_language is not None:
                        entity_cls = cls
                        break

                if not entity_cls:
                    continue

                entity_worker_data.append((entity_code, path, entity_cls.supported_languages))
                entities_data[entity_code] = (
                    entity_cls.default_language,
                    entity_cls.__doc__ or "",
                )

        with ProcessPoolExecutor() as executor:
            entity_pot_mapping = dict(
                executor.map(POGenerator._process_entity_worker, entity_worker_data)
            )

        with ProcessPoolExecutor(
            initializer=POGenerator._init_worker, initargs=(POGenerator._get_license_header(),)
        ) as executor:
            list(
                executor.map(
                    POGenerator._update_po_file,
                    (
                        (path, entity_pot_mapping[path.stem], *entities_data[path.stem])
                        for path in POGenerator._locale_path.rglob("*.po")
                    ),
                )
            )


if __name__ == "__main__":
    po_time_start = perf_counter()
    POGenerator.process_entities()
    po_time_end = perf_counter()
    print(f"[TIMER] Total generate po files runtime: {po_time_end - po_time_start:.2f} seconds")
