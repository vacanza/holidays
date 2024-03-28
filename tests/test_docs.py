#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

import re
from pathlib import Path
from unittest import TestCase

from holidays import country_holidays, list_supported_countries, list_localized_countries
from holidays.constants import PUBLIC


class TestReadme(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.readme_content = Path("README.rst").read_text(encoding="UTF-8")

        super().setUpClass()

    def test_supported_countries_count(self):
        actual_country_count = len(list_supported_countries(include_aliases=False))
        readme_country_count = int(
            re.findall(r"We currently support (\d+) country codes.", self.readme_content)[0]
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
        columns_number = 5
        country_alpha_2_codes = set()
        country_default_languages = {}
        country_names = []
        country_subdivisions = {}
        country_subdivisions_aliases = {}
        country_supported_languages = {}
        country_supported_categories = {}
        subdivision_group_re = re.compile(r"\w+:\s*([^\n:]+)")
        subdivision_and_aliases_re = re.compile(r",(?![^()]*\))")
        subdivision_aliases_re = re.compile(r"(.*?)\s\(([^()]*)\)")

        table_content = [
            line.strip()
            for line in re.findall(
                r"Supported Categories(.*)Available Financial Markets",
                self.readme_content,
                re.DOTALL,
            )[0].split("\n")
            if line
        ]

        for idx in range(0, len(table_content), columns_number):
            # Country: 1st column.
            name = table_content[idx].strip(" *-").replace(" ", "").lower()
            country_names.append(name)

            # Code: 2nd column.
            country_code = table_content[idx + 1].strip(" -")
            if country_code:
                country_alpha_2_codes.add(country_code)

            # Subdivisions and their aliases: 3rd column.
            country_subdivisions[country_code] = []
            country_subdivisions_aliases[country_code] = {}
            subdivision_str = table_content[idx + 2].strip(" -")
            if subdivision_str:
                for subdivision_groups in subdivision_str.split("."):
                    subdivision_aliases_group = subdivision_groups.split(";")[0].strip()
                    # Exclude empty subdivisions.
                    if ":" not in subdivision_aliases_group:
                        country_subdivisions[country_code] = []
                        continue

                    # Combine all subdivision and their aliases.
                    subdivision_aliases_group = subdivision_group_re.findall(
                        subdivision_aliases_group
                    )[0]
                    for subdivision_aliases in subdivision_and_aliases_re.split(
                        subdivision_aliases_group
                    ):
                        if "(" in subdivision_aliases:  # Subdivision with aliases.
                            subdivision_aliases = subdivision_aliases_re.match(subdivision_aliases)
                            subdivision = subdivision_aliases.group(1)
                            aliases = subdivision_aliases.group(2).split(", ")
                        else:
                            aliases = []
                            subdivision = subdivision_aliases
                        subdivision = subdivision.strip(" *")

                        country_subdivisions[country_code].append(subdivision)
                        country_subdivisions_aliases[country_code][subdivision] = aliases

            # Supported Languages: 4th column.
            supported_languages = table_content[idx + 3].strip(" -")
            if supported_languages:
                languages = []
                for supported_language in supported_languages.split(","):
                    supported_language = supported_language.strip()

                    if "*" in supported_language:
                        supported_language = supported_language.strip("*")
                        country_default_languages[country_code] = supported_language
                    languages.append(supported_language)

                country_supported_languages[country_code] = languages

            # Supported Categories: 5th column.
            supported_categories = table_content[idx + 4].strip(" -")
            if supported_categories:
                categories = [PUBLIC]
                for supported_category in supported_categories.split(","):
                    categories.append(supported_category.strip().lower())
                country_supported_categories[country_code] = sorted(categories)

        # Check the data.
        self.assertEqual(
            country_names,
            sorted(country_names),
            "The supported countries table must be sorted alphabetically by "
            "country name.\n"
            + "\n".join(
                (f"{c} != {s}" for c, s in zip(country_names, sorted(country_names)) if c != s)
            ),
        )

        country_names = set(c.split("(the)")[0] for c in country_names)
        supported_countries = list_supported_countries(include_aliases=False)
        localized_countries = list_localized_countries(include_aliases=False)
        for country_code in supported_countries:
            instance = country_holidays(country_code)
            country_name = instance.__class__.__base__.__name__

            # Make sure country name is shown correctly.
            if country_name.startswith("Holiday"):
                self.assertIn(
                    country_name[8:],
                    country_alpha_2_codes,
                    f"Country '{country_name}' name is not shown correctly in the table.",
                )
            else:
                self.assertIn(
                    country_name.lower().replace("unitedstates", "unitedstatesofamerica"),
                    country_names,
                    f"Country '{country_name}' name is not shown correctly in the table.",
                )

            # Make sure country alpha-2 code is shown correctly.
            self.assertIn(
                instance.country,
                country_alpha_2_codes,
                f"Country '{country_name}' alpha-2 code is not shown correctly in the table.",
            )

            # Make sure country subdivisions are shown correctly.
            self.assertEqual(
                supported_countries[country_code],
                country_subdivisions[country_code],
                f"Country '{country_name}' subdivisions are not shown "
                "correctly in the table.\n"
                + "\n".join(
                    (
                        f"{c} != {s}"
                        for c, s in zip(
                            supported_countries[country_code],
                            country_subdivisions[country_code],
                        )
                        if c != s
                    )
                ),
            )

            # Make sure country subdivisions aliases are shown correctly.
            subdivision_aliases = instance.get_subdivision_aliases()
            for subdivision in instance.subdivisions:
                self.assertEqual(
                    subdivision_aliases.get(subdivision, []),
                    country_subdivisions_aliases[country_code][subdivision],
                    f"Country '{country_name}' subdivisions '{subdivision}' aliases are not shown "
                    "correctly in the table.\n",
                )

            # Make sure supported languages are shown correctly.
            if country_code in localized_countries:
                supported_languages = localized_countries[country_code]
                self.assertEqual(
                    supported_languages,
                    country_supported_languages.get(country_code),
                    f"Country {country_name} supported languages are not "
                    "shown correctly in the table. The column must contain "
                    "all supported languages: "
                    f"{', '.join(instance.supported_languages)}",
                )

                self.assertEqual(
                    country_default_languages.get(country_code),
                    instance.default_language,
                    f"Country {country_name} default language is not shown "
                    "correctly in the table. Use **language** format "
                    "to specify the country default language: "
                    f"**{instance.default_language}**.",
                )

            # Make sure supported categories are shown correctly.
            supported_categories = sorted(instance.supported_categories)
            self.assertEqual(
                supported_categories,
                country_supported_categories.get(country_code, [PUBLIC]),
                f"Country {country_name} supported categories are not "
                "shown correctly in the table. The column must contain "
                "all supported categories: "
                f"{', '.join(instance.supported_categories)}",
            )
