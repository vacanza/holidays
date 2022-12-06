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


class TestZimbabwe(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.ZW()

    def test_new_years(self):
        self.assertIn(date(2010, 1, 1), self.holidays)
        self.assertIn(date(2020, 1, 1), self.holidays)
        self.assertNotIn(date(1986, 1, 2), self.holidays)  # sunday

    def test_observed(self):
        self.assertIn(date(2017, 1, 2), self.holidays)  # sunday

    def test_easter(self):
        self.assertIn(date(2017, 4, 14), self.holidays)  # Good friday
        self.assertIn(date(2017, 4, 15), self.holidays)  # Easter Saturday
        self.assertIn(date(2017, 4, 17), self.holidays)  # Easter Monday

    def test_heroes_day(self):
        self.assertIn(date(1988, 8, 8), self.holidays)
        self.assertIn(date(1988, 8, 9), self.holidays)
        self.assertIn(date(1996, 8, 12), self.holidays)
        self.assertIn(date(1996, 8, 13), self.holidays)
        self.assertIn(date(2000, 8, 14), self.holidays)
        self.assertIn(date(2000, 8, 15), self.holidays)
        self.assertIn(date(2020, 8, 10), self.holidays)
        self.assertIn(date(2020, 8, 11), self.holidays)
        self.assertIn(date(2021, 8, 9), self.holidays)
        self.assertIn(date(2021, 8, 10), self.holidays)
        self.assertIn(date(2022, 8, 8), self.holidays)
        self.assertIn(date(2022, 8, 9), self.holidays)

    def test_not_holiday(self):
        self.assertNotIn(date(2016, 1, 12), self.holidays)
        self.assertNotIn(date(1999, 2, 3), self.holidays)

    def test_youth_day(self):
        self.assertIn(date(2019, 2, 21), self.holidays)
        self.assertNotIn(date(2015, 2, 21), self.holidays)

    def test_not_observed(self):
        self.holidays = holidays.ZW(observed=False)
        self.assertNotIn(date(2017, 1, 2), self.holidays)
        self.assertNotIn(date(2019, 12, 23), self.holidays)
        self.assertNotIn(date(2021, 2, 22), self.holidays)
        self.assertNotIn(date(2022, 5, 2), self.holidays)
        self.assertNotIn(date(2022, 12, 27), self.holidays)
