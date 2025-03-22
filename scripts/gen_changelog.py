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

"""Generate docs/changelog.md from CHANGES.md"""

from pathlib import Path

import mkdocs_gen_files


def main():
    with mkdocs_gen_files.open("changelog.md", "w", newline="\n") as f:
        changes_file = Path(__file__).parent.parent / "CHANGES.md"
        changes_lines = changes_file.read_text(encoding="utf-8").split("\n")
        header = ["# Changelog", ""]
        changelog = [
            f"#{line}" if line.startswith("# Version") else line for line in changes_lines
        ]
        f.write("\n".join(header + changelog))


if __name__ in {"__main__", "<run_path>"}:
    main()
