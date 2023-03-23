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

import re
from pathlib import Path
from unittest import TestCase

from holidays.utils import country_holidays, country_to_module
from holidays.utils import list_supported_countries


class TestReadme(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.readme_content = (
            Path(__file__)
            .parent.parent.joinpath("README.rst")
            .read_text(encoding="utf-8")
        )
        # with open("README.rst", encoding="utf-8") as readme_file:
        #     cls.readme_content = "".join(readme_file.readlines())

        super().setUpClass()

    def test_supported_countries_count(self):
        actual_country_count = len(list_supported_countries())
        readme_country_count = int(
            re.findall(
                r"We currently support (\d+) country codes.",
                self.readme_content,
            )[0]
        )
        self.assertEqual(
            readme_country_count,
            actual_country_count,
            "README.rst supported countries statement is out of date: "
            f"'We currently support {readme_country_count} countries'. "
            f"Actual supported countries count: {actual_country_count}",
        )

    def test_supported_countries_table(self):
        # Parse table data.
        table_content = [
            line.strip()
            for line in re.findall(
                r"Subdivisions Available(.*)Available Financial Markets",
                self.readme_content,
                re.DOTALL,
            )[0].split("\n")
            if line
        ]
        country_names = []
        country_alpha_2_codes = []
        country_subdivisions = {}
        subdivisions_re = re.compile(".*: (.*)")
        for idx in range(0, len(table_content), 3):  # 3 column table.
            # 1st column.
            name = table_content[idx].strip(" *-").replace(" ", "").lower()
            country_names.append(name)

            # 2nd column.
            alpha_2_code = table_content[idx + 1].strip(" -")
            if alpha_2_code:
                country_alpha_2_codes.append(alpha_2_code)

            # 3rd column.
            country_subdivisions[alpha_2_code] = []
            subdivisions = table_content[idx + 2].split(".")
            for subdivision in subdivisions:
                subdivision_group = subdivision.split(";")[0].strip(" -")
                # Exclude empty subdivisions.
                if subdivision_group.startswith("None") or alpha_2_code == "":
                    country_subdivisions[alpha_2_code] = []
                    continue

                # Combine all subdivision codes.
                country_subdivisions[alpha_2_code].extend(
                    [
                        subdivision_code.replace("(default)", "").strip("* ")
                        for subdivision_code in subdivisions_re.findall(
                            subdivision_group
                        )[0].split(",")
                    ]
                )

        # Check no duplicate countries, alpha-2 codes, and sudviv.
        self.assertEqual(
            len(country_names),
            len(set(country_names)),
            "Duplicate country name in README.rst",
        )
        self.assertEqual(
            len(country_alpha_2_codes),
            len(set(country_alpha_2_codes)),
            "Duplicate alpha-2 codes in README.rst",
        )
        for country in country_subdivisions:
            self.assertEqual(
                len(country_subdivisions[country]),
                len(set(country_subdivisions[country])),
                f"Duplicate subdivision(s) in {country} in README.rst",
            )

        # Check all countries are in README.rst
        self.assertEqual(
            set(country_alpha_2_codes) - set(country_to_module),
            set(),
            f"Non-matching countries in README.rst: "
            f"{set(country_alpha_2_codes) - set(country_to_module)}",
        )

        # Check sorting of README.rst.
        self.assertEqual(
            country_names,
            sorted(country_names),
            "The supported countries table inREADME.rst must be sorted "
            "alphabetically by country name.\n"
            + "\n".join(
                (
                    f"{c} != {s}"
                    for c, s in zip(country_names, sorted(country_names))
                    if c != s
                )
            ),
        )

        supported_countries = list_supported_countries()
        for country_alpha_2_code in supported_countries:
            country = country_holidays(country_alpha_2_code)

            # Make sure country alpha-2 code is shown correctly.
            self.assertIn(
                country.country,
                country_alpha_2_codes,
                f"Country alpha-2 code '{country_alpha_2_code}' is not "
                "shown correctly in the table.",
            )

            # Make sure country subdivisions are shown correctly.
            self.assertEqual(
                supported_countries[country_alpha_2_code],
                country_subdivisions[country_alpha_2_code],
                f"Country '{country_alpha_2_code}' subdivisions are not "
                "shown correctly in the table.\n"
                + "\n".join(
                    (
                        f"{c} != {s}"
                        for c, s in zip(
                            supported_countries[country_alpha_2_code],
                            country_subdivisions[country_alpha_2_code],
                        )
                        if c != s
                    )
                ),
            )
