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

"""Generate SUMMARY.md for literate-nav with list of the countries and markets files."""

from pathlib import Path

import mkdocs_gen_files


def main():
    root = Path(__file__).parents[2]  # project folder
    holidays_path = root / "holidays"

    entities_data = [
        "* [Overview](index.md)",
        "* [Additional Examples](examples.md)",
        "* [Changelog](changelog.md)",
        "* [Contributing](contributing.md)",
        "* [API Reference](api.md)",
        "* Supported Entities",
    ]

    for entity_type in ("countries", "financial"):
        entities_data.append(f"    * holidays.{entity_type}")
        for path in sorted((holidays_path / entity_type).rglob("*.py")):
            file_name = path.stem
            if file_name == "__init__":
                continue
            entities_data.append(f"        * [{file_name}](auto_gen_docs/{file_name}.md)")

    with mkdocs_gen_files.open("SUMMARY.md", "w") as f:
        f.write("\n".join(entities_data))


if __name__ in {"__main__", "<run_path>"}:
    main()
