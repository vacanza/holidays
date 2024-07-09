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

from holidays import iso_3166_holidays, list_iso_3166_entities, list_localized_iso_3166_entities
from holidays.constants import PUBLIC


class TestReadme(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.readme_content = Path("README.rst").read_text(encoding="UTF-8")

        super().setUpClass()

    def test_supported_countries_count(self):
        actual_country_count = len(list_iso_3166_entities(include_aliases=False))
        readme_country_count = int(
            re.findall(
                r"We currently support (\d+) ISO 3166 entity codes.",
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
        columns_number = 5
        entity_codes = []
        entity_default_languages = {}
        entity_names = []
        entity_subdivisions = {}
        entity_subdivisions_aliases = {}
        entity_supported_languages = {}
        entity_supported_categories = {}

        subdivision_group_re = re.compile(r"([^\n:]+)")
        subdivision_and_aliases_re = re.compile(r",(?![^()]*\))")
        subdivision_aliases_re = re.compile(r"(.*?)\s\(([^()]*)\)")

        table_content = [
            line.strip()
            for line in re.findall(
                r"Categories(.*)Available ISO 10383 Entities",
                self.readme_content,
                re.DOTALL,
            )[0].split("\n")
            if line
        ]

        iso_3166_entities = set(list_iso_3166_entities())
        iso_3166_localized_entities = set(list_localized_iso_3166_entities())

        for idx in range(0, len(table_content), columns_number):
            # Code: 1st column.
            entity_code = table_content[idx].strip(" *-")
            self.assertIn(entity_code, iso_3166_entities)
            entity_codes.append(entity_code)

            # Entity name: 2nd column.
            entity_name = table_content[idx + 1].strip(" -")
            entity_names.append(entity_name)

            # Subdivisions and their aliases: 3rd column.
            entity_subdivisions[entity_code] = []
            entity_subdivisions_aliases[entity_code] = {}
            subdivision_str = table_content[idx + 2].strip(" -")
            if subdivision_str:
                for subdivision_groups in subdivision_str.split("."):
                    subdivision_aliases_group = subdivision_groups.split(";")[0].strip()

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

                        entity_subdivisions[entity_code].append(subdivision)
                        entity_subdivisions_aliases[entity_code][subdivision] = aliases

            # Supported Languages: 4th column.
            supported_languages = table_content[idx + 3].strip(" -")
            if supported_languages:
                self.assertIn(
                    entity_code,
                    iso_3166_localized_entities,
                    f"Entity {entity_code} hasn't been localized but its supported "
                    "languages column is not empty.",
                )
                languages = []
                for supported_language in supported_languages.split(","):
                    supported_language = supported_language.strip()

                    if "*" in supported_language:
                        supported_language = supported_language.strip("*")
                        self.assertIsNone(
                            entity_default_languages.get(entity_code),
                            f"Entity {entity_code} should have the default language specified "
                            "only once.",
                        )
                        entity_default_languages[entity_code] = supported_language
                    languages.append(supported_language)

                entity_supported_languages[entity_code] = languages

            # Supported Categories: 5th column.
            supported_categories = table_content[idx + 4].strip("-")
            if supported_categories:
                categories = [PUBLIC]
                for supported_category in supported_categories.split(","):
                    categories.append(supported_category.strip().lower())
                entity_supported_categories[entity_code] = sorted(categories)

        # Check the data.
        self.assertEqual(
            entity_codes,
            sorted(entity_codes),
            "The supported countries table must be sorted alphabetically by "
            "country name.\n"
            + "\n".join(
                (f"{c} != {s}" for c, s in zip(entity_names, sorted(entity_names)) if c != s)
            ),
        )

        supported_countries = list_iso_3166_entities()
        localized_countries = list_localized_iso_3166_entities()
        for entity_code in supported_countries:
            instance = iso_3166_holidays(entity_code)
            country_name = instance.name
            self.assertIn(
                instance.name,
                entity_names,
                f"Country '{country_name}' name is not shown correctly in the table.",
            )

            # Make sure country alpha-2 code is shown correctly.
            self.assertIn(
                instance.country,
                entity_codes,
                f"Country '{country_name}' alpha-2 code is not shown correctly in the table.",
            )

            # Make sure country subdivisions are shown correctly.
            self.assertEqual(
                supported_countries[entity_code],
                tuple(entity_subdivisions[entity_code]),
                f"Country '{country_name}' subdivisions are not shown "
                "correctly in the table.\n"
                + "\n".join(
                    (
                        f"{c} != {s}"
                        for c, s in zip(
                            supported_countries[entity_code],
                            entity_subdivisions[entity_code],
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
                    entity_subdivisions_aliases[entity_code][subdivision],
                    f"Country '{country_name}' subdivisions '{subdivision}' aliases are not shown "
                    "correctly in the table.\n",
                )

            # Make sure supported languages are shown correctly.
            if entity_code in localized_countries:
                supported_languages = localized_countries[entity_code]
                self.assertEqual(
                    supported_languages,
                    entity_supported_languages.get(entity_code),
                    f"Country {country_name} supported languages are not "
                    "shown correctly in the table. The column must contain "
                    "all supported languages: "
                    f"{', '.join(instance.supported_languages)}",
                )

                self.assertEqual(
                    entity_default_languages.get(entity_code),
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
                entity_supported_categories.get(entity_code, [PUBLIC]),
                f"Country {country_name} supported categories are not "
                "shown correctly in the table. The column must contain "
                "all supported categories: "
                f"{', '.join(instance.supported_categories)}",
            )
