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

"""Generate the code reference pages inside docs/auto_gen_files/"""

from pathlib import Path

import mkdocs_gen_files

root = Path(__file__).parent.parent  # project folder
countries_src = root / "holidays/countries"  # proj_folder/holidays/countries
financial_src = root / "holidays/financial"  # proj_folder/holidays/financial

# Generating the countries documentation files
for path in sorted(countries_src.rglob("*py")):
    py_file_path = path.relative_to(countries_src).with_suffix("")  # india
    md_file_path = path.relative_to(countries_src).with_suffix(".md")  # india.md
    doc_path = Path(
        "auto_gen_docs", md_file_path
    )  # where to generate files relative to mkdocs root folder

    py_file_path_parts = tuple(py_file_path.parts)  # ("submodule", "fileName")

    # Skip __init__.py and __main__.py files
    if py_file_path_parts[-1] in ("__init__", "__main__"):
        continue

    # Write the content
    with mkdocs_gen_files.open(doc_path, "w") as fd:
        identifier = ".".join(py_file_path_parts)
        print(f"::: holidays.countries.{identifier}", file=fd)

    mkdocs_gen_files.set_edit_path(doc_path, path.relative_to(root))

# Generating the financial documentation files
for path in sorted(financial_src.rglob("*py")):
    py_file_path = path.relative_to(financial_src).with_suffix("")  # brasil_bolsa_balcao
    md_file_path = path.relative_to(financial_src).with_suffix(".md")  # brasil_bolsa_balcao.md
    doc_path = Path(
        "auto_gen_docs", md_file_path
    )  # where to generate files relative to mkdocs root folder

    py_file_path_parts = tuple(py_file_path.parts)  # ("submodule", "fileName")

    # Skip __init__.py and __main__.py files
    if py_file_path_parts[-1] in ("__init__", "__main__"):
        continue

    # Write the content
    with mkdocs_gen_files.open(doc_path, "w") as fd:
        identifier = ".".join(py_file_path_parts)
        print(f"::: holidays.financial.{identifier}", file=fd)

    mkdocs_gen_files.set_edit_path(doc_path, path.relative_to(root))
