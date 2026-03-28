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
import sys
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from pathlib import Path
from time import perf_counter

from lingva.extract import extract as create_pot_file
from lingva.extract import _location_sort_key
from polib import pofile

sys.path.insert(0, str(Path.cwd()))  # Make holidays visible.
from holidays import __version__ as package_version
from holidays.holiday_base import HolidayBase

LEGACY_NAME_MAP = {
    "IM": "Isle of Man",
    "MP": "Northern Mariana Islands",
    "TL": "Timor-Leste",
    "US": "United States of America",
    "VI": "United States Virgin Islands",
    "XNSE": "National Stock Exchange of India",
}
WRAP_WIDTH = 99
HEADER_PATH = Path("docs/file_header.txt")


class POGenerator:
    """Generates .po files for supported country/market entities."""

    _locale_path: Path = Path("holidays/locale")
    _po_index: dict[str, list[Path]] | None = None

    @staticmethod
    def _get_license_header() -> str:
        """Reads and formats the license header from docs/file_header.txt."""
        if not HEADER_PATH.exists():
            return ""

        content = HEADER_PATH.read_text(encoding="utf-8").lstrip("\n")
        if not content:
            return ""

        return (
            "\n".join(
                f"# {stripped}" if (stripped := line.rstrip()) else "#"
                for line in content.splitlines()
            )
            + "\n#"
        )

    @classmethod
    def _init_worker(cls, po_index: dict[str, list[Path]]) -> None:
        """Initialize worker with shared PO index for multiprocessing."""
        cls._po_index = po_index

    @staticmethod
    def _build_desc_line(
        entity_code: str, docstring: str, current_language: str, default_language: str
    ) -> str:
        """Builds the descriptive comment line for a .po file header."""
        clean_name = ""
        if docstring:
            first_line = docstring.strip().split("\n")[0].strip().rstrip(".")
            if first_line.endswith(" holidays"):
                clean_name = first_line[:-9].strip()
            else:
                clean_name = first_line

        display_name = LEGACY_NAME_MAP.get(entity_code, clean_name)
        if not display_name:
            return ""
        if current_language != default_language:
            return f"# {display_name} holidays {current_language} localization."
        return f"# {display_name} holidays."

    @staticmethod
    def _write_po_header(po_path: Path, desc_line: str) -> None:
        """Strips gettext boilerplate and prepends the license header + desc line."""
        content = po_path.read_text(encoding="utf-8")
        content = (
            content.split("#, fuzzy", 1)[1].lstrip()
            if content.startswith("# SOME DESCRIPTIVE TITLE")
            else content.lstrip()
        )

        if content.startswith("#  holidays\n#  --------"):
            return

        license_header = POGenerator._get_license_header()
        parts = []
        if license_header:
            parts.append(license_header)
        if desc_line and desc_line not in content:
            parts.append(desc_line)
        if parts:
            parts.append("#")
            po_path.write_text("\n".join(parts) + "\n" + content, encoding="utf-8")  # NOSONAR

    @staticmethod
    def _process_entity_worker(
        entity_code_info: tuple[str, tuple[str, Path, str, tuple[str, ...]]],
    ) -> list[tuple[Path, Path, str, str]]:
        """Process a single entity: create .pot, default .po, and return update tasks."""
        entity_code, (default_language, class_file_path, class_docstring, supported_languages) = (
            entity_code_info
        )

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
            location=False,
            allow_empty=True,
            msgid_bugs_address="l10n@vacanza.dev",
        )

        pot_file = pofile(str(pot_file_path), wrapwidth=WRAP_WIDTH)
        pot_file.metadata["Project-Id-Version"] = f"Holidays {package_version}"
        pot_file.metadata["Report-Msgid-Bugs-To"] = "l10n@vacanza.dev"
        pot_file.metadata["PO-Revision-Date"] = pot_file.metadata["POT-Creation-Date"]
        pot_file.metadata["Language-Team"] = "Holidays Localization Team"
        pot_file.metadata["X-Source-Language"] = default_language
        pot_file.save(newline="\n")

        if POGenerator._po_index is None:
            raise RuntimeError("PO index not initialized in worker")

        update_tasks = [
            (po_file_path, pot_file_path, class_docstring, default_language)
            for po_file_path in POGenerator._po_index.get(entity_code, [])
        ]

        for lang in supported_languages:
            lang_directory = POGenerator._locale_path / lang / "LC_MESSAGES"
            lang_directory.mkdir(parents=True, exist_ok=True)
            lang_po_path = lang_directory / f"{entity_code}.po"

            if not lang_po_path.exists():
                pot_file.metadata["Language"] = lang
                pot_file.save(str(lang_po_path), newline="\n")

                desc_line = POGenerator._build_desc_line(
                    entity_code, class_docstring, lang, default_language
                )
                POGenerator._write_po_header(lang_po_path, desc_line)

        return update_tasks

    @staticmethod
    def _update_po_file(args: tuple[Path, Path, str, str]) -> None:
        """Merge .po file with .pot using strict no-change policies."""
        po_path, pot_path, entity_docstring, default_language = args
        po_path = po_path.resolve()
        pot_path = pot_path.resolve()
        entity_code = po_path.stem.upper()
        current_lang = po_path.parent.parent.name

        desc_line = POGenerator._build_desc_line(
            entity_code, entity_docstring, current_lang, default_language
        )

        po_file = pofile(str(po_path), wrapwidth=WRAP_WIDTH)
        po_file_initial = po_file.copy()

        pot_file = pofile(str(pot_path), wrapwidth=WRAP_WIDTH)

        po_file.merge(pot_file)
        po_file.sort(key=_location_sort_key)
        for entry in po_file:
            entry.occurrences.clear()

        has_content_changed = po_file != po_file_initial

        if not has_content_changed:
            POGenerator._write_po_header(po_path, desc_line)
            return

        timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M%z")
        po_file.metadata["Project-Id-Version"] = f"Holidays {package_version}"
        po_file.metadata["Report-Msgid-Bugs-To"] = "l10n@vacanza.dev"
        po_file.metadata["PO-Revision-Date"] = timestamp
        po_file.metadata["Language-Team"] = "Holidays Localization Team"
        po_file.metadata["Language"] = current_lang
        po_file.metadata["X-Source-Language"] = default_language
        po_file.save(str(po_path), newline="\n")

        POGenerator._write_po_header(po_path, desc_line)

    def process_entities(self):
        """Processes entities in specified directory."""
        entity_code_info_mapping = {}
        for entity_type in ("countries", "financial"):
            for path in Path(f"holidays/{entity_type}").glob("*.py"):
                if path.stem == "__init__":
                    continue
                module = f"holidays.{entity_type}.{path.stem}"

                try:
                    mod = importlib.import_module(module)
                except ImportError:
                    continue

                candidates = []
                for _, cls in inspect.getmembers(mod, inspect.isclass):
                    if (
                        issubclass(cls, HolidayBase)
                        and cls.__module__ == module
                        and cls.default_language is not None
                    ):
                        candidates.append(cls)

                if not candidates:
                    continue

                chosen_cls = None
                target_name = path.stem.replace("_", "").lower()

                for cls in candidates:
                    if cls.__name__.lower() == target_name:
                        chosen_cls = cls
                        break

                if not chosen_cls:
                    candidates.sort(key=lambda c: len(c.__doc__ or ""), reverse=True)
                    chosen_cls = candidates[0]

                name = getattr(chosen_cls, "country", None) or getattr(chosen_cls, "market", None)
                if not name:
                    continue

                entity_code_info_mapping[name.upper()] = (
                    chosen_cls.default_language,
                    path,
                    chosen_cls.__doc__ or "",
                    chosen_cls.supported_languages or (),
                )

        po_index: dict[str, list[Path]] = {}
        for path in self._locale_path.rglob("*.po"):
            po_index.setdefault(path.stem.upper(), []).append(path)

        all_po_update_tasks: list[tuple[Path, Path, str, str]] = []
        with ProcessPoolExecutor(
            initializer=POGenerator._init_worker,
            initargs=(po_index,),
        ) as executor:
            for po_tasks in executor.map(
                POGenerator._process_entity_worker,
                entity_code_info_mapping.items(),
            ):
                all_po_update_tasks.extend(po_tasks)

            list(executor.map(POGenerator._update_po_file, all_po_update_tasks))

    @staticmethod
    def run():
        """Runs the .po files generation process."""
        POGenerator().process_entities()


if __name__ == "__main__":
    po_time_start = perf_counter()
    POGenerator.run()
    po_time_end = perf_counter()
    print(f"[TIMER] Total generate po files runtime: {po_time_end - po_time_start:.2f} seconds")
