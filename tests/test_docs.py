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

import re
import unicodedata
from pathlib import Path
from unittest import TestCase

from holidays import (
    country_holidays,
    financial_holidays,
    list_localized_countries,
    list_localized_financial,
    list_supported_countries,
    list_supported_financial,
)
from holidays.constants import PUBLIC


class TestAuthors(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = Path("CONTRIBUTORS").read_text(encoding="UTF-8").strip().split("\n")
        super().setUpClass()

    def test_authors_list(self):
        authors = self.content[1:]
        self.assertEqual(
            authors,
            sorted(authors),
            "Contributors list should be sorted alphabetically.\n"
            + "\n".join((f"{c} != {s}" for c, s in zip(authors, sorted(authors)) if c != s)),
        )


class TestReadme(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.readme_content = Path("README.md").read_text(encoding="UTF-8")

        super().setUpClass()

    def _parse_table(self, table_index: int):
        """Parse HTML table at given index from README.md content."""

        table_cell_re = re.compile(r"<td>(.*?)</td>")
        tables = re.findall(r"<table style.*?</table>", self.readme_content, re.DOTALL)  # type: ignore[attr-defined]
        table = tables[table_index]
        rows = re.findall(r"<tr>(.*?)</tr>", table, re.DOTALL)
        return [table_cell_re.findall(line) for line in rows[1:]]

    def test_supported_countries_count(self):
        actual_country_count = len(list_supported_countries(include_aliases=False))
        readme_country_count = int(
            re.findall(r"We currently support (\d+) country codes.", self.readme_content)[0]
        )
        self.assertEqual(
            readme_country_count,
            actual_country_count,
            "README.md supported countries statement is out of date: "
            f"'We currently support {readme_country_count} countries'. "
            f"Actual supported countries count: {actual_country_count}",
        )

    def test_supported_countries_table(self):
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
        default_value_re = re.compile(r"<strong>(.*?)</strong>")

        # Parse 1st table.
        table_content = self._parse_table(0)

        for row in table_content:
            # Country: 1st column.
            country_names.append(
                re.sub(
                    r"[-,\s]",
                    "",
                    unicodedata.normalize("NFKD", row[0])
                    .encode("ascii", "ignore")
                    .decode("ascii"),
                ).lower()
            )

            # Code: 2nd column.
            country_code = row[1]
            if country_code:
                country_alpha_2_codes.add(country_code)

            # Subdivisions and their aliases: 3rd column.
            country_subdivisions[country_code] = []
            country_subdivisions_aliases[country_code] = {}
            subdivision_str = row[2]
            if subdivision_str:
                for subdivision_aliases_group in subdivision_str.split(";"):
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
                            # "Virgin Islands, U.S." special case.
                            if len(aliases) == 2 and aliases[1] == "U.S.":
                                aliases = [subdivision_aliases.group(2)]
                        else:
                            aliases = []
                            subdivision = subdivision_aliases
                        subdivision = subdivision.strip()

                        country_subdivisions[country_code].append(subdivision)
                        country_subdivisions_aliases[country_code][subdivision] = aliases

            # Supported Languages: 4th column.
            supported_languages = row[3]
            if supported_languages:
                languages = []
                for supported_language in supported_languages.split(","):
                    supported_language = supported_language.strip()

                    if "<strong>" in supported_language:
                        supported_language = default_value_re.search(supported_language).group(1)
                        country_default_languages[country_code] = supported_language
                    languages.append(supported_language)

                country_supported_languages[country_code] = languages

            # Supported Categories: 5th column.
            supported_categories = row[4]
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

        country_names = {c.split("(the)")[0] for c in country_names}
        supported_countries = list_supported_countries(include_aliases=False)
        localized_countries = list_localized_countries(include_aliases=False)
        for country_code in supported_countries:
            instance = country_holidays(country_code)
            country_name = instance.__class__.__base__.__name__

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
                            supported_countries[country_code], country_subdivisions[country_code]
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
                    "correctly in the table. Use <strong>language</strong> format "
                    "to specify the country default language: "
                    f"<strong>{instance.default_language}</strong>.",
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

    def test_supported_markets_table(self):
        market_mic_codes = set()
        market_default_languages = {}
        market_names = []
        market_supported_languages = {}
        default_value_re = re.compile(r"<strong>(.*?)</strong>")

        # Parse 2nd table.
        table_content = self._parse_table(1)
        replace_chars = str.maketrans(
            {
                " ": "",
                ",": "",
                "ã": "a",
            }
        )

        for row in table_content:
            # Market: 1st column.
            name = row[0].translate(replace_chars).lower()
            market_names.append(name)

            # Code: 2nd column.
            market_code = row[1]
            if market_code:
                market_mic_codes.add(market_code)

            # Supported Languages: 4th column.
            supported_languages = row[3]
            if supported_languages:
                languages = []
                for supported_language in supported_languages.split(","):
                    supported_language = supported_language.strip()

                    if "<strong>" in supported_language:
                        supported_language = default_value_re.search(supported_language).group(1)
                        market_default_languages[market_code] = supported_language
                    languages.append(supported_language)

                market_supported_languages[market_code] = languages

        # Check the data.
        self.assertEqual(
            market_names,
            sorted(market_names),
            "The supported markets table must be sorted alphabetically by market name.\n"
            + "\n".join(
                (f"{c} != {s}" for c, s in zip(market_names, sorted(market_names)) if c != s)
            ),
        )

        supported_markets = list_supported_financial(include_aliases=False)
        localized_markets = list_localized_financial(include_aliases=False)
        for market_code in supported_markets:
            instance = financial_holidays(market_code)
            market_name = instance.__class__.__base__.__name__

            # Make sure market name is shown correctly.
            self.assertIn(
                market_name.lower(),
                market_names,
                f"Market '{market_name}' name is not shown correctly in the table.",
            )

            # Make sure market MIC code is shown correctly.
            self.assertIn(
                instance.market,
                market_mic_codes,
                f"Market '{market_name}' MIC code is not shown correctly in the table.",
            )

            # Make sure supported languages are shown correctly.
            if market_code in localized_markets:
                supported_languages = localized_markets[market_code]
                self.assertEqual(
                    supported_languages,
                    market_supported_languages.get(market_code),
                    f"Market {market_name} supported languages are not "
                    "shown correctly in the table. The column must contain "
                    "all supported languages: "
                    f"{', '.join(instance.supported_languages)}",
                )

                self.assertEqual(
                    market_default_languages.get(market_code),
                    instance.default_language,
                    f"Market {market_name} default language is not shown "
                    "correctly in the table. Use <strong>language</strong> format "
                    "to specify the market default language: "
                    f"<strong>{instance.default_language}</strong>.",
                )
