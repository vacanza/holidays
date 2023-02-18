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

import importlib.util
from datetime import date

from holidays.countries.ethiopia import Ethiopia, ET, ETH
from tests.common import TestCase


class TestEthiopia(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Ethiopia)

    def test_country_aliases(self):
        self.assertCountryAliases(Ethiopia, ET, ETH)

    # Check isleap loops
    def test_not_holiday(self):
        self.assertNotIn(date(2019, 9, 11), self.holidays)
        self.assertNotIn(date(2019, 9, 27), self.holidays)
        self.assertNotIn(date(2019, 9, 13), self.holidays)
        self.assertNotIn(date(1940, 5, 5), self.holidays)
        self.assertNotIn(date(1990, 5, 28), self.holidays)
        self.assertNotIn(date(1971, 9, 13), self.holidays)
        self.assertNotIn(date(1970, 9, 12), self.holidays)
        self.assertNotIn(date(1993, 9, 13), self.holidays)
        self.assertNotIn(date(1994, 9, 12), self.holidays)

    def test_2019(self):
        self.assertIn(date(2019, 1, 7), self.holidays)
        self.assertIn(date(2019, 1, 19), self.holidays)
        self.assertIn(date(2019, 3, 2), self.holidays)
        self.assertIn(date(2019, 4, 28), self.holidays)
        self.assertIn(date(2019, 4, 26), self.holidays)
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 5, 5), self.holidays)
        self.assertIn(date(2019, 5, 28), self.holidays)
        self.assertIn(date(2019, 9, 12), self.holidays)
        self.assertIn(date(2019, 9, 28), self.holidays)
        self.assertIn(date(2019, 11, 10), self.holidays)
        self.assertIn(date(1975, 9, 13), self.holidays)
        self.assertIn(date(1976, 9, 12), self.holidays)

    def test_2020(self):
        self.assertIn(date(2020, 9, 11), self.holidays)
        self.assertIn(date(2020, 9, 27), self.holidays)

    def test_ethiopian_christmas(self):
        self.assertIn(date(2019, 1, 7), self.holidays)

    def test_ethiopian_ephiphany(self):
        self.assertIn(date(2019, 1, 19), self.holidays)

    def test_adwa_victory(self):
        self.assertIn(date(2019, 3, 2), self.holidays)

    def test_easter_good_friday(self):
        self.assertIn(date(2019, 4, 26), self.holidays)

    def test_easter(self):
        self.assertIn(date(2019, 4, 28), self.holidays)

    def test_labour_day(self):
        self.assertIn(date(2019, 5, 1), self.holidays)

    def test_patriots_day(self):
        self.assertNotIn(date(1940, 5, 5), self.holidays)
        self.assertIn(date(2019, 5, 5), self.holidays)

    def test_downfall_of_dergue(self):
        self.assertIn(date(2019, 5, 28), self.holidays)

    def test_formation_of_dergue(self):
        self.assertIn(date(1982, 9, 12), self.holidays)
        self.assertIn(date(1983, 9, 13), self.holidays)

    def test_hijri_based(self):
        if not importlib.util.find_spec("hijri_converter"):
            return None

        self.holidays = Ethiopia(years=[2019])
        # eid_alfitr
        self.assertIn(date(2019, 6, 4), self.holidays)
        # eid_aladha
        self.assertIn(date(2019, 8, 11), self.holidays)
        # muhammad's birthday
        self.assertIn(date(2019, 11, 10), self.holidays)

    def test_pre_1897(self):
        self.assertNotIn(date(1896, 3, 2), self.holidays)

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                et = Ethiopia(language=language)
                self.assertEqual(et["2022-01-07"], "ገና")
                self.assertEqual(et["2022-09-11"], "አዲስ ዓመት እንቁጣጣሽ")

        run_tests((Ethiopia.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Ethiopia.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        et = Ethiopia(language=en_us)
        self.assertEqual(et["2022-01-07"], "Orthodox Christmas Day")
        self.assertEqual(et["2022-09-11"], "Ethiopian New Year's Day")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            et = Ethiopia(language=language)
            self.assertEqual(et["2022-01-07"], "Orthodox Christmas Day")
            self.assertEqual(et["2022-09-11"], "Ethiopian New Year's Day")
