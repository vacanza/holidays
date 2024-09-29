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

from pathlib import Path

from polib import pofile


class MOGenerator:
    """Creates .mo files for supported country/market entities."""

    @staticmethod
    def run():
        """Runs the .mo files generation process."""
        for po_path in Path("holidays/locale").rglob("*.po"):
            mo_path = po_path.with_suffix(".mo")
            if mo_path.exists():
                mo_path.unlink()
            pofile(po_path).save_as_mofile(mo_path)


if __name__ == "__main__":
    MOGenerator.run()
