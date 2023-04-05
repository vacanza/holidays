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

from lingua.extract import main as pot_create
from polib import pofile


class POGenerator:
    """Generates .po files for supported country/market entities."""

    def update_po_file(self, po_path: str, pot_path: str) -> None:
        """Merge .po file with .pot"""
        po_file = pofile(po_path)
        pot_file = pofile(pot_path)
        po_file.merge(pot_file)
        po_file.save(po_path)

    def process_countries(self):
        """Processes entities in specified directory."""
        country_code_info_mapping = {}
        modules = (
            (path.stem, path)
            for path in (Path() / "holidays" / "countries").glob("*.py")
            if path.stem != "__init__"
        )

        sys.path.append(str(Path.cwd()))  # Make holidays visible.
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
                    and hasattr(cls, "default_language")
                }
            )

        locale_path = Path() / "holidays" / "locale"
        for country_code in sorted(country_code_info_mapping.keys()):
            default_language, class_file_path = country_code_info_mapping[
                country_code
            ]
            pot_file_path = str(locale_path / "pot" / f"{country_code}.pot")
            # Create .pot files.
            pot_create(
                (
                    str(class_file_path),
                    "-k",
                    "tr",
                    "-o",
                    pot_file_path,
                    "--package-name",
                    "Python Holidays",
                    "--package-version",
                    package_version,
                    "--width",
                    "80",
                ),
                standalone_mode=False,
            )

            # Update default country .po file.
            po_directory = locale_path / default_language / "LC_MESSAGES"
            po_directory.mkdir(parents=True, exist_ok=True)
            po_file_path = po_directory / f"{country_code}.po"
            if po_file_path.exists():
                self.update_po_file(str(po_file_path), pot_file_path)

            # Update .po files.
            for po_file_path in locale_path.rglob(f"{country_code}.po"):
                self.update_po_file(str(po_file_path), pot_file_path)

    def run(self):
        """Runs the .po files generation process."""
        self.process_countries()


if __name__ == "__main__":
    POGenerator().run()
