#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
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
    for po_path in Path("locale").rglob("*.po"):
        po_file = str(po_path)
        mo_file = po_file.replace(".po", ".mo")
        subprocess.run(
            (
                sys.executable,
                os.path.join("scripts", "build", "msgfmt.py"),
                "-o",
                mo_file,
                po_file,
            ),
            check=True,
        )


def main():
    """Setup entry point."""
    generate_mo_files()
    setup()


if __name__ == "__main__":
    main()
