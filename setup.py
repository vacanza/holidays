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
from pathlib import Path

from setuptools import setup


def generate_mo_files():
    """Looks up for .po files and generates respective .mo files."""
    for po_path in Path("locale").rglob("*.po"):
        mo_path = str(po_path).replace(".po", ".mo")
        subprocess.run(
            (
                os.path.join("scripts", "build", "msgfmt.py"),
                "-o",
                mo_path,
                po_path,
            ),
            check=True,
        )


def main():
    """Setup entry point."""
    generate_mo_files()
    setup()


if __name__ == "__main__":
    main()
