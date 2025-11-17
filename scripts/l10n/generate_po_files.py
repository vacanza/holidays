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
from pathlib import Path
from time import perf_counter

from lingva.extract import extract as create_pot_file
from lingva.extract import _location_sort_key
from polib import pofile

sys.path.append(f"{Path.cwd()}")  # Make holidays visible.
from holidays import __version__ as package_version
from holidays.holiday_base import HolidayBase

WRAP_WIDTH = 99


class POGenerator:
    """Generates .po files for supported country/market entities."""

    @staticmethod
    def _process_entity_worker(
        entity_code_info: tuple[str, tuple[str, Path]],
    ) -> list[tuple[str, str, str]]:
        """Process a single entity: create .pot, default .po, and return update tasks."""
        entity_code, (default_language, class_file_path) = entity_code_info

        locale_path = Path("holidays/locale")
        pot_path = locale_path / "pot"
        pot_path.mkdir(exist_ok=True)

        pot_file_path = pot_path / f"{entity_code}.pot"

        # Create .pot file.
        create_pot_file(
            sources=[class_file_path],
            keywords=["tr"],
            output=pot_file_path,
            package_name="Holidays",
            package_version=package_version,
            width=WRAP_WIDTH,
            allow_empty=True,
        )

        # Update .pot file metadata.
        pot_file = pofile(pot_file_path, wrapwidth=WRAP_WIDTH)
        pot_file.metadata.update(
            {
                "Language": default_language,
                "Language-Team": "Holidays Localization Team",
                "X-Source-Language": default_language,
            }
        )
        pot_file.save(newline="\n")

        # Create entity default .po file from the .pot file.
        po_directory = locale_path / default_language / "LC_MESSAGES"
        po_directory.mkdir(parents=True, exist_ok=True)
        default_po_path = po_directory / f"{entity_code}.po"
        if not default_po_path.exists():
            pot_file.save(str(default_po_path), newline="\n")

        # Collect .po update tasks.
        po_update_tasks: list[tuple[str, str, str]] = [
            (str(po_file_path), str(pot_file_path), package_version)
            for po_file_path in locale_path.rglob(f"{entity_code}.po")
        ]

        return po_update_tasks

    @staticmethod
    def _update_po_file(args: tuple[str, str, str]) -> None:
        """Merge .po file with .pot"""
        po_path, pot_path, package_version = args
        po_file = pofile(po_path, wrapwidth=WRAP_WIDTH)
        po_file_initial = po_file.copy()

        po_file.merge(pofile(pot_path))
        po_file.sort(key=_location_sort_key)
        for entry in po_file:
            entry.occurrences.clear()

        # Only update the project version if po file translation entriesv has changed.
        if po_file != po_file_initial:
            po_file.metadata["Project-Id-Version"] = f"Holidays {package_version}"

        # Save the file each time in order to capture all other changes properly.
        po_file.save(po_path, newline="\n")

    def process_entities(self):
        """Processes entities in specified directory."""
        entity_code_info_mapping = {}
        for entity_type in ("countries", "financial"):
            for path in Path(f"holidays/{entity_type}").glob("*.py"):
                if path.stem == "__init__":
                    continue
                module = f"holidays.{entity_type}.{path.stem}"
                for _, cls in inspect.getmembers(importlib.import_module(module), inspect.isclass):
                    if (
                        issubclass(cls, HolidayBase)
                        and cls.__module__ == module
                        and getattr(cls, "default_language") is not None
                    ):
                        name = getattr(cls, "country", getattr(cls, "market", None))
                        entity_code_info_mapping[name.upper()] = (cls.default_language, path)
                        break

        all_po_update_tasks: list[tuple[str, str, str]] = []
        with ProcessPoolExecutor() as executor:
            for po_tasks in executor.map(
                self._process_entity_worker, entity_code_info_mapping.items()
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
