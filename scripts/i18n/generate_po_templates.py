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

    def process_directory(self, directory):
        """Runs the POT files generation process."""

        country_code_path_mapping = {}
        module_name_path_mapping = {
            str(path).split("/")[-1].replace(".py", ""): str(path)
            for path in Path(f"holidays/{directory}").glob("*.py")
            if not str(path).endswith("__init__.py")
        }

        sys.path.insert(0, os.getcwd())
        from holidays.holiday_base import HolidayBase

        for module_name, module_path in module_name_path_mapping.items():
            module = f"holidays.{directory}.{module_name}"
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

        for country_code, file_path in country_code_path_mapping.items():
            subprocess.run(
                (
                    "pot-create",
                    file_path,
                    "-k",
                    "tr",
                    "-o",
                    f"holidays/locale/pot/{country_code}.pot",
                ),
                check=True,
            )

    def run(self):
        self.process_directory("countries")
        self.process_directory("markets")


if __name__ == "__main__":
    pot_generator = POTGenerator()
    pot_generator.run()
