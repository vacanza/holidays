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

import os
import subprocess
import sys
from pathlib import Path


class MOGenerator:
    """Creates .mo files for supported country/market entities."""

    def run(self):
        """Runs the .mo files generation process."""
        # Delete old files.
        for mo_file in Path(os.path.join("holidays", "locale")).rglob("*.mo"):
            os.unlink(str(mo_file))

        # Create new files.
        for po_path in Path(os.path.join("holidays", "locale")).rglob("*.po"):
            po_file = str(po_path)
            mo_file = po_file.replace(".po", ".mo")
            subprocess.run(
                (
                    sys.executable,
                    os.path.join("scripts", "l10n", "msgfmt.py"),
                    "-o",
                    mo_file,
                    po_file,
                ),
                check=True,
            )


if __name__ == "__main__":
    MOGenerator().run()
