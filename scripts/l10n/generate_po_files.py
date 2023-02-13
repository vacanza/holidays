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
    """
    Generates .pot files for supported country/market entities.
    """

    def process_countries(self):
        """Processes entities in specified directory."""
        country_code_path_mapping = {}
        module_name_path_mapping = {
            str(path).split("/")[-1].replace(".py", ""): str(path)
            for path in Path("holidays/countries").glob("*.py")
            if not str(path).endswith("__init__.py")
        }

        # Make holidays visible.
        sys.path.insert(0, os.getcwd())
        from holidays.holiday_base import HolidayBase

        for module_name, module_path in module_name_path_mapping.items():
            module = f"holidays.countries.{module_name}"
            country_code_path_mapping.update(
                {
                    name.upper(): module_path
                    for name, cls in inspect.getmembers(
                        importlib.import_module(module), inspect.isclass
                    )
                    if issubclass(cls, HolidayBase)
                    and len(name) == 2
                    and cls.__module__ == module
                    and hasattr(cls, "default_language")
                }
            )

        for country_code, class_file_path in country_code_path_mapping.items():
            pot_file_path = f"holidays/locale/pot/{country_code}.pot"
            # Create .pot files.
            subprocess.run(
                (
                    "pot-create",
                    class_file_path,
                    "-k",
                    "tr",
                    "-o",
                    pot_file_path,
                ),
                check=True,
            )

            # Update .po files.
            for po_file_path in Path("holidays/locale").rglob(
                f"{country_code}.po"
            ):
                subprocess.run(
                    (
                        "msgmerge",
                        po_file_path,
                        pot_file_path,
                        "-o",
                        po_file_path,
                        "--force-po",
                    ),
                    check=True,
                )

    def run(self):
        """Runs the POT files generation process."""
        self.process_countries()


if __name__ == "__main__":
    pot_generator = POTGenerator()
    pot_generator.run()
