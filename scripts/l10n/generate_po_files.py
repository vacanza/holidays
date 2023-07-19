#!/usr/bin/env python3

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import importlib
import inspect
import sys
from pathlib import Path

from lingua.extract import main as create_pot_file
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
        if po_file != po_file_initial:
            po_file.metadata["Project-Id-Version"] = f"Python Holidays {package_version}"
            po_file.save(po_path)

    def process_countries(self):
        """Processes entities in specified directory."""
        country_code_info_mapping = {}
        modules = (
            (path.stem, path)
            for path in Path("holidays/countries").glob("*.py")
            if path.stem != "__init__"
        )

        sys.path.append(f"{Path.cwd()}")  # Make holidays visible.
        from holidays import __version__ as package_version
        from holidays.holiday_base import HolidayBase

        for module_name, module_path in modules:
            module = f"holidays.countries.{module_name}"
            country_code_info_mapping.update(
                {
                    name.upper(): (cls.default_language, module_path)
                    for name, cls in inspect.getmembers(
                        importlib.import_module(module), inspect.isclass
                    )
                    if issubclass(cls, HolidayBase)
                    and len(name) == 2
                    and cls.__module__ == module
                    and getattr(cls, "default_language") is not None
                }
            )

        locale_path = Path("holidays/locale")
        pot_path = locale_path / "pot"
        pot_path.mkdir(exist_ok=True)
        for country_code in sorted(country_code_info_mapping.keys()):
            default_language, class_file_path = country_code_info_mapping[country_code]
            pot_file_path = pot_path / f"{country_code}.pot"
            # Create .pot file.
            create_pot_file(
                (
                    f"{class_file_path}",
                    "-k",
                    "tr",
                    "-o",
                    f"{pot_file_path}",
                    "--package-name",
                    "Python Holidays",
                    "--package-version",
                    package_version,
                    "--width",
                    "100",
                    "--no-location",
                ),
                standalone_mode=False,
            )

            # Create country default .po file from the .pot file.
            po_directory = locale_path / default_language / "LC_MESSAGES"
            po_directory.mkdir(parents=True, exist_ok=True)
            po_file_path = po_directory / f"{country_code}.po"
            if not po_file_path.exists():
                po_file = pofile(pot_file_path)
                po_file.metadata["Language"] = default_language
                po_file.save(po_file_path)

            # Update all .po files.
            for po_file_path in locale_path.rglob(f"{country_code}.po"):
                self.update_po_file(po_file_path, pot_file_path, package_version)

    @staticmethod
    def run():
        """Runs the .po files generation process."""
        POGenerator().process_countries()


if __name__ == "__main__":
    POGenerator.run()
