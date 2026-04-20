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

from unittest import TestCase

from holidays.utils import list_localized_countries, list_localized_financial
from scripts.generate_site_assets import LANGUAGES


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
