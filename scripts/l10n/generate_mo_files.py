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

from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from time import perf_counter

from polib import pofile


class MOGenerator:
    """Creates .mo files for supported country/market entities."""

    @staticmethod
    def _convert_po_to_mo(po_path: Path) -> None:
        """Convert a single .po file to .mo file."""
        pofile(po_path).save_as_mofile(str(po_path.with_suffix(".mo")))

    @staticmethod
    def _unlink_file(path: Path) -> None:
        """Unlink old .mo file"""
        path.unlink(missing_ok=True)

    @staticmethod
    def run() -> None:
        """Runs the .mo files generation process."""
        locale_path = Path("holidays/locale")
        with ProcessPoolExecutor() as executor:
            executor.map(MOGenerator._unlink_file, locale_path.rglob("*.mo"))
            executor.map(MOGenerator._convert_po_to_mo, locale_path.rglob("*.po"))


if __name__ == "__main__":
    mo_time_start = perf_counter()
    MOGenerator.run()
    mo_time_end = perf_counter()
    print(f"[TIMER] Total generate mo files runtime: {mo_time_end - mo_time_start:.2f} seconds")
