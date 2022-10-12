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


class TestGeorgia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.GE()

    def test_easter(self):
        self.assertIn(date(2020, 4, 19), self.holidays)
        self.assertIn(date(2019, 4, 28), self.holidays)
        self.assertIn(date(2018, 4, 8), self.holidays)

    def test_2020(self):
        # https://en.wikipedia.org/wiki/Public_holidays_in_Georgia_(country)
        self.assertIn(date(2020, 1, 1), self.holidays)
        self.assertIn(date(2020, 1, 2), self.holidays)
        self.assertIn(date(2020, 1, 7), self.holidays)
        self.assertIn(date(2020, 1, 19), self.holidays)
        self.assertIn(date(2020, 3, 3), self.holidays)
        self.assertIn(date(2020, 3, 8), self.holidays)
        self.assertIn(date(2020, 4, 9), self.holidays)
        self.assertIn(date(2020, 5, 9), self.holidays)
        self.assertIn(date(2020, 5, 12), self.holidays)
        self.assertIn(date(2020, 5, 26), self.holidays)
        self.assertIn(date(2020, 8, 28), self.holidays)
        self.assertIn(date(2020, 10, 14), self.holidays)
        self.assertIn(date(2020, 11, 23), self.holidays)

    def test_not_holiday(self):
        self.assertNotIn("2020-08-16", self.holidays)
        self.assertNotIn("2008-08-05", self.holidays)
