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

import unittest
from datetime import date

import holidays


class TestLU(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.LU()

    def test_2018(self):
        year = 2018
        # https://www.officeholidays.com/countries/luxembourg/2018
        self.assertIn(date(year, 1, 1), self.holidays)
        self.assertIn(date(year, 4, 2), self.holidays)
        self.assertIn(date(year, 5, 1), self.holidays)
        self.assertIn(date(year, 5, 10), self.holidays)
        self.assertIn(date(year, 5, 21), self.holidays)
        self.assertIn(date(year, 6, 23), self.holidays)
        self.assertIn(date(year, 8, 15), self.holidays)
        self.assertIn(date(year, 11, 1), self.holidays)
        self.assertIn(date(year, 12, 25), self.holidays)
        self.assertIn(date(year, 12, 26), self.holidays)

    def test_2019(self):
        # https://www.officeholidays.com/countries/luxembourg/2019
        self.assertIn(date(2019, 1, 1), self.holidays)
        self.assertIn(date(2019, 4, 22), self.holidays)
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 5, 9), self.holidays)
        self.assertIn(date(2019, 5, 30), self.holidays)
        self.assertIn(date(2019, 6, 10), self.holidays)
        self.assertIn(date(2019, 6, 23), self.holidays)
        self.assertIn(date(2019, 8, 15), self.holidays)
        self.assertIn(date(2019, 11, 1), self.holidays)
        self.assertIn(date(2019, 12, 25), self.holidays)
        self.assertIn(date(2019, 12, 26), self.holidays)
