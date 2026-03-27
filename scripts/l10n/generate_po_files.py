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

sys.path.insert(0, str(Path.cwd()))
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
                "#" if not line.rstrip() else f"# {line.rstrip()}" for line in content.splitlines()
            )
            + "\n#"
        )

    @staticmethod
    def _get_standard_metadata(default_language: str = "en_US") -> dict:
        """Returns the standard metadata required for gettext."""
        return {
            "Report-Msgid-Bugs-To": "l10n@vacanza.dev",
            "Language-Team": "Holidays Localization Team",
            "X-Source-Language": default_language,
        }

    @classmethod
    def _init_worker(cls, po_index: dict[str, list[Path]]) -> None:
        """Initialize worker with shared PO index for multiprocessing."""
        cls._po_index = po_index

    @staticmethod
    def _strip_gettext_boilerplate(content: str) -> str:
        if content.startswith("# SOME DESCRIPTIVE TITLE"):
            return content.split("#, fuzzy", 1)[1].lstrip()
        return content.lstrip()

    @staticmethod
    def _process_entity_worker(
        entity_code_info: tuple[str, tuple[str, Path, str]],
    ) -> list[tuple[Path, Path, str, str]]:
        """Process a single entity: create .pot, default .po, and return update tasks."""
        entity_code, (default_language, class_file_path, class_docstring) = entity_code_info

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
        pot_file.metadata.update(POGenerator._get_standard_metadata(default_language))
        pot_file.metadata["Project-Id-Version"] = f"Holidays {package_version}"
        pot_file.save(newline="\n")

        po_directory = POGenerator._locale_path / default_language / "LC_MESSAGES"
        po_directory.mkdir(parents=True, exist_ok=True)
        default_po_path = po_directory / f"{entity_code}.po"

        if not default_po_path.exists():
            pot_file.metadata["PO-Revision-Date"] = pot_file.metadata["POT-Creation-Date"]
            pot_file.metadata["Language"] = default_language
            pot_file.save(str(default_po_path), newline="\n")

        if POGenerator._po_index is None:
            raise RuntimeError("PO index not initialized in worker")

        return [
            (po_file_path, pot_file_path, class_docstring, default_language)
            for po_file_path in POGenerator._po_index.get(entity_code, [])
        ]

    @staticmethod
    def _update_po_file(args: tuple[Path, Path, str, str]) -> None:
        """Merge .po file with .pot using strict no-change policies."""
        po_path, pot_path, entity_docstring, default_language = args
        po_path = po_path.resolve()
        pot_path = pot_path.resolve()
        entity_code = po_path.stem.upper()

        po_file = pofile(str(po_path), wrapwidth=WRAP_WIDTH)
        po_file_initial = po_file.copy()

        pot_file = pofile(str(pot_path), wrapwidth=WRAP_WIDTH)

        po_file.merge(pot_file)
        po_file.sort(key=_location_sort_key)
        for entry in po_file:
            entry.occurrences.clear()

        has_content_changed = po_file != po_file_initial

        license_header = POGenerator._get_license_header()
        current_lang = po_path.parent.parent.name
        is_default_lang = current_lang == default_language

        clean_name = ""
        if entity_docstring:
            first_line = entity_docstring.strip().split("\n")[0].strip().rstrip(".")
            if first_line.endswith(" holidays"):
                clean_name = first_line[:-9].strip()
            else:
                clean_name = first_line

        display_name = LEGACY_NAME_MAP.get(entity_code, clean_name)
        desc_line = ""
        if not is_default_lang and clean_name:
            desc_line = f"# {display_name} holidays {current_lang} localization."
        elif clean_name:
            desc_line = f"# {display_name} holidays."

        if not has_content_changed:
            if po_path.exists():
                content = po_path.read_text(encoding="utf-8")
                content = POGenerator._strip_gettext_boilerplate(content)
                if not content.startswith("#  holidays\n#  --------"):
                    new_parts = []
                    if license_header:
                        new_parts.append(license_header)
                    if desc_line and desc_line not in content.splitlines():
                        new_parts.append(desc_line)

                    if new_parts:
                        new_parts.append("#")
                        final_content = "\n".join(new_parts) + "\n" + content
                        if final_content.strip() != content.strip():
                            po_path.write_text(final_content, encoding="utf-8")
            return

        timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M%z")
        po_file.metadata["Project-Id-Version"] = f"Holidays {package_version}"
        po_file.metadata["PO-Revision-Date"] = timestamp

        std_meta = POGenerator._get_standard_metadata(default_language)
        std_meta["Language"] = current_lang

        for k, v in std_meta.items():
            po_file.metadata[k] = v

        po_file.save(str(po_path), newline="\n")

        content = po_path.read_text(encoding="utf-8")
        new_parts = []

        if license_header and not content.startswith("#  holidays\n#  --------"):
            new_parts.append(license_header)

        if desc_line and desc_line not in content:
            new_parts.append(desc_line)

        if new_parts:
            new_parts.append("#")

            final_content = "\n".join(new_parts) + "\n" + content
            po_path.write_text(final_content, encoding="utf-8")

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
                        and getattr(cls, "default_language") is not None
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
