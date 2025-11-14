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

from pathlib import Path
from time import perf_counter

from polib import pofile


class MOGenerator:
    """Creates .mo files for supported country/market entities."""

    @staticmethod
    def run():
        """Runs the .mo files generation process."""
        locale_path = Path("holidays/locale")

        for mo_path in locale_path.rglob("*.mo"):
            mo_path.unlink()
        for po_path in locale_path.rglob("*.po"):
            pofile(po_path).save_as_mofile(po_path.with_suffix(".mo"))


if __name__ == "__main__":
    mo_time_start = perf_counter()
    MOGenerator.run()
    mo_time_end = perf_counter()
    print(f"[TIMER] Total generate mo files runtime: {mo_time_end - mo_time_start:.2f} seconds")
