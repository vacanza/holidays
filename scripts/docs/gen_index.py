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


def main():
    readme_file = Path(__file__).parents[2] / "README.md"
    readme_content = readme_file.read_text(encoding="utf-8")
    readme_content = readme_content.replace(
        "[here](https://github.com/vacanza/holidays/blob/dev/CONTRIBUTING.md)",
        "[here](contributing.md)",
    )
    with mkdocs_gen_files.open("index.md", "w", encoding="utf-8", newline="\n") as f:
        f.write(readme_content)

    contributing_file = Path(__file__).parents[2] / "CONTRIBUTING.md"
    contributing_content = contributing_file.read_text(encoding="utf-8")
    with mkdocs_gen_files.open("contributing.md", "w", encoding="utf-8", newline="\n") as f:
        f.write(contributing_content)


if __name__ in {"__main__", "<run_path>"}:
    main()
