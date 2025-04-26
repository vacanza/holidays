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

"""Generate index.md and contributing.md with proper link."""

from pathlib import Path

import mkdocs_gen_files


def write_file(file_path: Path, content: str):
    """Write content to a file with proper encoding and newline."""
    with mkdocs_gen_files.open(file_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def main():
    project_root = Path(__file__).parents[2]

    contributing_file = project_root / "CONTRIBUTING.md"
    write_file("contributing.md", contributing_file.read_text(encoding="utf-8"))

    readme_file = project_root / "README.md"
    write_file(
        "index.md",
        readme_file.read_text(encoding="utf-8").replace(
            "[here](https://github.com/vacanza/holidays/blob/dev/CONTRIBUTING.md)",
            "[here](contributing.md)",
        ),
    )


if __name__ in {"__main__", "<run_path>"}:
    main()
