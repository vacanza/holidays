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


class TestCZ(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.CZ()

    def test_2017(self):
        # http://www.officeholidays.com/countries/czech_republic/2017.php
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 5, 1), self.holidays)
        self.assertIn(date(2017, 5, 8), self.holidays)
        self.assertIn(date(2017, 7, 5), self.holidays)
        self.assertIn(date(2017, 7, 6), self.holidays)
        self.assertIn(date(2017, 9, 28), self.holidays)
        self.assertIn(date(2017, 10, 28), self.holidays)
        self.assertIn(date(2017, 11, 17), self.holidays)
        self.assertIn(date(2017, 12, 24), self.holidays)
        self.assertIn(date(2017, 12, 25), self.holidays)
        self.assertIn(date(2017, 12, 26), self.holidays)

    def test_others(self):
        self.assertIn(date(1991, 5, 9), self.holidays)

    def test_older_years(self):
        self.assertNotIn(date(1950, 5, 1), self.holidays)
        self.assertNotIn(date(1991, 5, 8), self.holidays)
        self.assertIn(date(1990, 5, 9), self.holidays)
        self.assertNotIn(date(1946, 5, 9), self.holidays)
        self.assertNotIn(date(1950, 7, 5), self.holidays)
        self.assertNotIn(date(1950, 10, 28), self.holidays)
        self.assertNotIn(date(1989, 11, 17), self.holidays)
        self.assertNotIn(date(1989, 12, 24), self.holidays)
        self.assertNotIn(date(1950, 12, 25), self.holidays)
        self.assertNotIn(date(1950, 12, 26), self.holidays)
