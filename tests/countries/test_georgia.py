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

from holidays.countries.georgia import Georgia, GE, GEO
from tests.common import TestCase


class TestGeorgia(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Georgia)

    def test_country_aliases(self):
        self.assertCountryAliases(Georgia, GE, GEO)

    def test_easter(self):
        self.assertHoliday(
            "2020-04-19",
            "2019-04-28",
            "2018-04-08",
        )

    def test_2020(self):
        # https://en.wikipedia.org/wiki/Public_holidays_in_Georgia_(country)
        self.assertHoliday(
            "2020-01-01",
            "2020-01-02",
            "2020-01-07",
            "2020-01-19",
            "2020-03-03",
            "2020-03-08",
            "2020-04-09",
            "2020-05-09",
            "2020-05-12",
            "2020-05-26",
            "2020-08-28",
            "2020-10-14",
            "2020-11,-23",
        )

    def test_not_holiday(self):
        self.assertNoHoliday(
            "2020-08-16",
            "2008-08-05",
        )

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                ge = Georgia(language=language)
                self.assertEqual(ge["2022-01-01"], "ახალი წელი")
                self.assertEqual(ge["2022-01-07"], "ქრისტეშობა")

        run_tests((Georgia.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Georgia.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        ge = Georgia(language=en_us)
        self.assertEqual(ge["2022-01-01"], "New Year's Day")
        self.assertEqual(ge["2022-01-07"], "Orthodox Christmas Day")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            ge = Georgia(language=language)
            self.assertEqual(ge["2022-01-01"], "New Year's Day")
            self.assertEqual(ge["2022-01-07"], "Orthodox Christmas Day")
