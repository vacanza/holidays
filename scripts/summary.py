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

"""Lists the countries files and financial files in SUMMARY.md  for literate-nav"""

from pathlib import Path

import mkdocs_gen_files

root = Path(__file__).parent.parent  # project folder
countries_src = root / "holidays/countries"
financial_src = root / "holidays/financial"
summary_file = "SUMMARY.md"

with mkdocs_gen_files.open(summary_file, "w") as f:
    f.write("* [Overview](index.md)\n")
    f.write("* [Additional Examples](examples.md)\n")
    f.write("* [Contributing](CONTRIBUTING.md)\n")
    f.write("* [API Reference](api.md)\n")
    f.write("* [Mixins](mixins.md)\n")
    f.write("* Supported Entities\n")
    f.write("    * holidays.countries\n")

    for path in sorted(countries_src.rglob("*.py")):
        file_name = path.stem  # india
        if file_name in ["__init__", "__main__"]:
            continue
        f.write(f"        * [{file_name}](auto_gen_docs/{file_name}.md)\n")

    f.write("    * holidays.financial\n")

    for path in sorted(financial_src.rglob("*.py")):
        file_name = path.stem  # brasil_bolsa_balcao
        if file_name in ["__init__", "__main__"]:
            continue
        f.write(f"        * [{file_name}](auto_gen_docs/{file_name}.md)\n")

    f.write("* [Changelog](changelog.md)")
