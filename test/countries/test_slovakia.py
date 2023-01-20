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


class TestSK(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.SK()

    def test_2018(self):
        # https://www.officeholidays.com/countries/slovakia/2018.php
        self.assertIn(date(2018, 1, 1), self.holidays)
        self.assertIn(date(2018, 1, 6), self.holidays)
        self.assertIn(date(2018, 3, 30), self.holidays)
        self.assertIn(date(2018, 5, 1), self.holidays)
        self.assertIn(date(2018, 5, 8), self.holidays)
        self.assertIn(date(2018, 4, 2), self.holidays)
        self.assertIn(date(2018, 7, 5), self.holidays)
        self.assertIn(date(2018, 8, 29), self.holidays)
        self.assertIn(date(2018, 9, 1), self.holidays)
        self.assertIn(date(2018, 9, 15), self.holidays)
        self.assertIn(date(2018, 10, 30), self.holidays)
        self.assertIn(date(2018, 11, 1), self.holidays)
        self.assertIn(date(2018, 11, 17), self.holidays)
        self.assertIn(date(2018, 12, 24), self.holidays)
        self.assertIn(date(2018, 12, 25), self.holidays)
        self.assertIn(date(2018, 12, 26), self.holidays)

    def test_special_dates(self):
        self.assertNotIn(date(1996, 5, 8), self.holidays)
        self.assertIn(date(1997, 5, 8), self.holidays)

        self.assertNotIn(date(2000, 11, 17), self.holidays)
        self.assertIn(date(2001, 11, 17), self.holidays)

    def test_special_holidays(self):
        self.assertIn(date(2018, 10, 30), self.holidays)

        self.assertNotIn(date(2017, 10, 30), self.holidays)
        self.assertNotIn(date(2019, 10, 30), self.holidays)
