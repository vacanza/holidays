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
import os
import subprocess
import sys
from pathlib import Path


class POTGenerator:
    """Generates .pot files for supported country/market entities."""

    def process_countries(self):
        """Processes entities in specified directory."""
        country_code_info_mapping = {}
        module_name_path_mapping = {
            str(path).split(os.sep)[-1].replace(".py", ""): str(path)
            for path in Path(os.path.join("holidays", "countries")).glob(
                "*.py"
            )
            if not str(path).endswith("__init__.py")
        }

        sys.path.append(os.getcwd())  # Make holidays visible.
        from holidays import __version__ as package_version
        from holidays.holiday_base import HolidayBase

        for module_name, module_path in module_name_path_mapping.items():
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

        for country_code in sorted(country_code_info_mapping.keys()):
            default_language, class_file_path = country_code_info_mapping[
                country_code
            ]
            pot_file_path = os.path.join(
                "holidays", "locale", "pot", f"{country_code}.pot"
            )
            # Create .pot files.
            subprocess.run(
                (
                    "pot-create",
                    class_file_path,
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
                    # "--add-location",
                    # "--linenumbers",
                ),
                check=True,
            )

            # Update default country .po file.
            po_directory = os.path.join(
                "holidays", "locale", default_language, "LC_MESSAGES"
            )
            os.makedirs(po_directory, exist_ok=True)
            po_file_path = os.path.join(po_directory, f"{country_code}.po")
            subprocess.run(
                (
                    "msgmerge",
                    po_file_path,
                    pot_file_path,
                    "-o",
                    po_file_path,
                ),
                check=True,
            )

            # Update .po files.
            for po_file_path in Path(os.path.join("holidays", "locale")).rglob(
                f"{country_code}.po"
            ):
                subprocess.run(
                    (
                        "msgmerge",
                        po_file_path,
                        pot_file_path,
                        "-o",
                        po_file_path,
                    ),
                    check=True,
                )

    def run(self):
        """Runs the POT files generation process."""
        self.process_countries()


if __name__ == "__main__":
    pot_generator = POTGenerator()
    pot_generator.run()
