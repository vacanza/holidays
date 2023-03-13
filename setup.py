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

from setuptools import setup


def generate_mo_files():
    """Looks up for .po files and generates respective .mo files."""
    for po_path in Path(os.path.join("holidays", "locale")).rglob("*.po"):
        po_file = str(po_path)
        mo_file = po_file.replace(".po", ".mo")

        if os.path.exists(mo_file):
            os.unlink(mo_file)
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
    generate_mo_files()
    setup()
