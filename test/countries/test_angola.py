#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date

import holidays


class TestAngola(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.AO()

    def test_new_years(self):
        self.assertIn("1975-01-01", self.holidays)
        self.assertIn("2017-01-01", self.holidays)
        self.assertIn("2999-01-01", self.holidays)
        self.assertIn("2017-01-02", self.holidays)  # sunday

    def test_carnival(self):
        self.assertIn("1994-02-15", self.holidays)
        self.assertIn("2002-02-12", self.holidays)
        self.assertIn("2010-02-16", self.holidays)
        self.assertIn("2017-02-28", self.holidays)
        self.assertIn("2018-02-13", self.holidays)
        self.assertIn("2019-03-05", self.holidays)
        self.assertIn("2020-02-25", self.holidays)
        self.assertIn("2021-02-16", self.holidays)
        self.assertIn("2022-03-01", self.holidays)

    def test_easter(self):
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2020, 4, 10), self.holidays)
        self.assertIn(date(1994, 4, 1), self.holidays)

    def test_static(self):
        self.assertIn("2004-03-08", self.holidays)
        self.assertIn("2020-03-23", self.holidays)

    def test_long_weekend(self):
        self.assertIn("2020-02-03", self.holidays)
        self.assertIn("2019-04-05", self.holidays)
        self.assertIn("2050-03-07", self.holidays)

    def test_not_holiday(self):
        self.assertNotIn("2016-12-28", self.holidays)
        self.assertNotIn("2015-03-02", self.holidays)
        self.assertNotIn("2018-03-23", self.holidays)

    def test_national_hero_day(self):
        for year in range(1980, 1979):
            self.assertNotIn(date(year, 9, 17), self.holidays)
        for year in range(1980, 2030):
            self.assertIn(date(year, 9, 17), self.holidays)

    def test_national_liberation_day(self):
        for year in range(1990, 2018):
            self.assertNotIn(date(year, 3, 23), self.holidays)
        for year in range(2019, 2030):
            self.assertIn(date(year, 3, 23), self.holidays)

    def test_pre_1975(self):
        # Holidays are defined since 1975.
        self.assertNotIn("1974-01-01", self.holidays)
        self.assertEqual(0, len(holidays.AO(years=1974)))

    def test_observed(self):
        for _, name in holidays.AO(observed=False, years=2020).items():
            self.assertNotIn("Observed", name)
