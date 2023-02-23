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


from datetime import date
from datetime import timedelta as td

from holidays.countries.bulgaria import Bulgaria, BG, BLG
from tests.common import TestCase


class TestBulgaria(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Bulgaria)

    def test_country_aliases(self):
        self.assertCountryAliases(Bulgaria, BG, BLG)

    def test_before_1990(self):
        self.assertEqual(len(Bulgaria(years=[1989])), 0)

    def test_new_years_day(self):
        for year in range(1990, 2020):
            self.assertIn(date(year, 1, 1), self.holidays)

    def test_liberation_day(self):
        for year in range(1990, 2020):
            self.assertIn(date(year, 3, 3), self.holidays)

    def test_labour_day(self):
        for year in range(1990, 2020):
            self.assertIn(date(year, 5, 1), self.holidays)

    def test_saint_georges_day(self):
        for year in range(1990, 2020):
            self.assertIn(date(year, 5, 6), self.holidays)

    def test_twenty_fourth_of_may(self):
        for year in range(1990, 2020):
            self.assertIn(date(year, 5, 24), self.holidays)

    def test_unification_day(self):
        for year in range(1990, 2020):
            self.assertIn(date(year, 9, 6), self.holidays)

    def test_independence_day(self):
        for year in range(1990, 2020):
            self.assertIn(date(year, 9, 22), self.holidays)

    def test_national_awakening_day(self):
        for year in range(1990, 2020):
            self.assertIn(date(year, 11, 1), self.holidays)

    def test_christmas(self):
        for year in range(1990, 2020):
            self.assertIn(date(year, 12, 24), self.holidays)
            self.assertIn(date(year, 12, 25), self.holidays)
            self.assertIn(date(year, 12, 26), self.holidays)

    def test_easter(self):
        for year, month, day in [
            (2000, 4, 30),
            (2001, 4, 15),
            (2002, 5, 5),
            (2003, 4, 27),
            (2004, 4, 11),
            (2005, 5, 1),
            (2006, 4, 23),
            (2007, 4, 8),
            (2008, 4, 27),
            (2009, 4, 19),
            (2010, 4, 4),
            (2011, 4, 24),
            (2012, 4, 15),
            (2013, 5, 5),
            (2014, 4, 20),
            (2015, 4, 12),
            (2016, 5, 1),
            (2017, 4, 16),
            (2018, 4, 8),
            (2019, 4, 28),
            (2020, 4, 19),
            (2021, 5, 2),
            (2022, 4, 24),
        ]:
            easter = date(year, month, day)
            easter_friday = easter + td(days=-2)
            easter_saturday = easter + td(days=-1)
            easter_monday = easter + td(days=+1)
            for holiday in [
                easter_friday,
                easter_saturday,
                easter,
                easter_monday,
            ]:
                self.assertIn(holiday, self.holidays)

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                bg = Bulgaria(language=language)
                self.assertEqual(bg["2022-01-01"], "Нова година")
                self.assertEqual(bg["2022-12-25"], "Рождество Христово")

        run_tests((Bulgaria.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Bulgaria.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        bg = Bulgaria(language=en_us)
        self.assertEqual(bg["2018-01-01"], "New Year's Day")
        self.assertEqual(bg["2022-12-25"], "Christmas Day")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            bg = Bulgaria(language=language)
            self.assertEqual(bg["2018-01-01"], "New Year's Day")
            self.assertEqual(bg["2022-12-25"], "Christmas Day")
