#!/usr/bin/env python3

#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import importlib
import inspect
import sys
from pathlib import Path

from lingva.extract import main as create_pot_file
from polib import pofile


class POGenerator:
    """Generates .po files for supported country/market entities."""

    @staticmethod
    def update_po_file(po_path: str, pot_path: str, package_version: str) -> None:
        """Merge .po file with .pot"""
        po_file = pofile(po_path)
        po_file_initial = po_file.copy()
        pot_file = pofile(pot_path)

        po_file.merge(pot_file)

        # Update the project version if po file entries translation has changed only.
        if po_file != po_file_initial:
            po_file.metadata["Project-Id-Version"] = f"Holidays {package_version}"

        # Save the file each time in order to capture all other changes properly.
        po_file.save(po_path)

    def process_entities(self):
        """Processes entities in specified directory."""
        sys.path.append(f"{Path.cwd()}")  # Make holidays visible.
        from holidays import __version__ as package_version
        from holidays.holiday_base import HolidayBase

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

        locale_path = Path("holidays/locale")
        pot_path = locale_path / "pot"
        pot_path.mkdir(exist_ok=True)
        for entity_code in sorted(entity_code_info_mapping.keys()):
            default_language, class_file_path = entity_code_info_mapping[entity_code]
            pot_file_path = pot_path / f"{entity_code}.pot"
            # Create .pot file.
            create_pot_file(
                (
                    f"{class_file_path}",
                    "-k",
                    "tr",
                    "-o",
                    f"{pot_file_path}",
                    "--package-name",
                    "Holidays",
                    "--package-version",
                    package_version,
                    "--width",
                    "100",
                    "--no-location",
                ),
                standalone_mode=False,
            )

            # Update .pot file metadata.
            pot_file = pofile(pot_file_path)
            pot_file.metadata.update(
                {
                    "Language-Team": "Holidays Localization Team",
                    "PO-Revision-Date": pot_file.metadata["POT-Creation-Date"],
                }
            )
            pot_file.save()

            # Create entity default .po file from the .pot file.
            po_directory = locale_path / default_language / "LC_MESSAGES"
            po_directory.mkdir(parents=True, exist_ok=True)
            po_file_path = po_directory / f"{entity_code}.po"
            if not po_file_path.exists():
                po_file = pofile(pot_file_path)
                po_file.metadata["Language"] = default_language
                po_file.save(po_file_path)

            # Update all .po files.
            for po_file_path in locale_path.rglob(f"{entity_code}.po"):
                self.update_po_file(po_file_path, pot_file_path, package_version)

    @staticmethod
    def run():
        """Runs the .po files generation process."""
        POGenerator().process_entities()


if __name__ == "__main__":
    POGenerator.run()
