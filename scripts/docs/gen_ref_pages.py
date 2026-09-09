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

"""Generate reference pages for countries and markets inside docs/auto_gen_docs."""

from pathlib import Path

import mkdocs_gen_files


def main():
    root = Path(__file__).parents[2]  # project folder
    holidays_path = root / "holidays"

    for entity_type in ("countries", "financial"):
        for path in sorted((holidays_path / entity_type).rglob("*.py")):
            file_name = path.stem
            if file_name == "__init__":
                continue
            doc_path = Path("auto_gen_docs", f"{file_name}.md")

            with mkdocs_gen_files.open(doc_path, "w") as f:
                f.write(f"::: holidays.{entity_type}.{file_name}")
            mkdocs_gen_files.set_edit_path(doc_path, path.relative_to(root))


if __name__ in {"__main__", "<run_path>"}:
    main()
