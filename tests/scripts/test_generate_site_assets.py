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

import tempfile
from pathlib import Path
from unittest import TestCase

from holidays.utils import list_localized_countries, list_localized_financial
from scripts.generate_site_assets import generate_html_index, LANGUAGES


class TestGenerateSiteAssets(TestCase):
    def test_languages_mapping(self):
        languages = set(LANGUAGES)
        supported_languages = set().union(
            *list_localized_countries(include_aliases=False).values(),
            *list_localized_financial(include_aliases=False).values(),
        )
        self.assertEqual(
            languages,
            supported_languages,
            "LANGUAGES in `generate_site_assets.py` does not match supported languages list; "
            f"missing: {supported_languages - languages or 'no'}, "
            f"extra: {languages - supported_languages or 'no'}",
        )

    def test_generate_html_index(self):
        manifest = {
            "countries": {
                "DK": {
                    "name": "Denmark",
                    "subdivisions": {},
                    "languages": {"da": "Danish"},
                    "categories": ["public"],
                }
            },
            "financial": {},
        }

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp)
            country_dir = output_dir / "countries" / "DK"
            country_dir.mkdir(parents=True)
            (country_dir / "ALL_da_public.ics").write_text(
                "BEGIN:VCALENDAR\nEND:VCALENDAR\n", encoding="utf-8"
            )
            (country_dir / "ALL_da_public.json").write_text("[]", encoding="utf-8")
            (country_dir / "ALL_da_optional.ics").write_text(
                "BEGIN:VCALENDAR\nEND:VCALENDAR\n", encoding="utf-8"
            )

            generate_html_index(manifest, output_dir)
            document = (output_dir / "index.html").read_text(encoding="utf-8")

        self.assertIn("Denmark (DK)", document)
        self.assertIn("Danish (da)", document)
        self.assertIn('href="countries/DK/ALL_da_public.ics"', document)
        self.assertIn('href="countries/DK/ALL_da_public.json"', document)
        self.assertIn(
            "webcal://vacanza.github.io/holidays/downloads/ics/countries/DK/ALL_da_public.ics",
            document,
        )
        self.assertNotIn("ALL_da_optional.ics", document)
        self.assertIn('id="calendars"', document)

    def test_generate_html_index_escapes_metadata(self):
        manifest = {
            "countries": {
                "XX&YY": {
                    "name": '<script>alert("x")</script>',
                    "subdivisions": {},
                    "languages": {"en": "English"},
                    "categories": ["public"],
                }
            },
            "financial": {},
        }

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp)
            country_dir = output_dir / "countries" / "XX&YY"
            country_dir.mkdir(parents=True)
            (country_dir / "ALL_en_public.ics").write_text("BEGIN:VCALENDAR\nEND:VCALENDAR\n", encoding="utf-8")

            generate_html_index(manifest, output_dir)
            document = (output_dir / "index.html").read_text(encoding="utf-8")

        self.assertIn(
            'href="countries/XX&amp;YY/ALL_en_public.ics"',
            document,
        )
        self.assertIn(
            "webcal://vacanza.github.io/holidays/downloads/ics/"
            "countries/XX&amp;YY/ALL_en_public.ics",
            document,
        )
