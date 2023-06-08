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


class TestChina(unittest.TestCase):
    # https: // en.wikipedia.org / wiki / Public_holidays_in_China
    def setUp(self):
        self.holidays = holidays.CN()

    def test_1950(self):
        self.assertIn(date(1950, 1, 1), self.holidays)  # New Year's Day
        # Chinese New Year day 1
        self.assertIn(date(1950, 2, 17), self.holidays)
        # Chinese New Year day 2
        self.assertIn(date(1950, 2, 18), self.holidays)
        # Chinese New Year day 3
        self.assertIn(date(1950, 2, 19), self.holidays)
        # Labour Day day 1
        self.assertIn(date(1950, 5, 1), self.holidays)
        # NO Labour Day day 2
        self.assertNotIn(date(1950, 5, 2), self.holidays)
        # NO Labour Day day 3
        self.assertNotIn(date(1950, 5, 3), self.holidays)
        # NO Dragon Boat Festival
        self.assertNotIn(date(1950, 6, 19), self.holidays)
        # NO Mid-Autumn Festival
        self.assertNotIn(date(1950, 9, 26), self.holidays)
        self.assertIn(date(1950, 10, 1), self.holidays)  # National Day day 1
        self.assertIn(date(1950, 10, 2), self.holidays)  # National Day day 2
        # NO National Day day 3
        self.assertNotIn(date(1950, 10, 3), self.holidays)

    def test_2005(self):
        # New Year's Day
        self.assertIn(date(2005, 1, 1), self.holidays)
        # Chinese New Year day 1
        self.assertIn(date(2005, 2, 9), self.holidays)
        # Chinese New Year day 2
        self.assertIn(date(2005, 2, 10), self.holidays)
        # Chinese New Year day 3
        self.assertIn(date(2005, 2, 11), self.holidays)
        # NO Tomb-Sweeping Day
        self.assertNotIn(date(2005, 4, 5), self.holidays)
        # Labour Day day 1
        self.assertIn(date(2005, 5, 1), self.holidays)
        # Labour Day day 2
        self.assertIn(date(2005, 5, 2), self.holidays)
        # Labour Day day 3
        self.assertIn(date(2005, 5, 3), self.holidays)
        self.assertNotIn(date(2005, 6, 11), self.holidays)  # NO Dragon Boat Festival
        # NO Mid-Autumn Festival
        self.assertNotIn(date(2005, 9, 18), self.holidays)
        # National Day day 1
        self.assertIn(date(2005, 10, 1), self.holidays)
        # National Day day 2
        self.assertIn(date(2005, 10, 2), self.holidays)
        # National Day day 3
        self.assertIn(date(2005, 10, 3), self.holidays)

    def test_chinese_new_year_2010(self):
        self.assertIn(date(2010, 2, 13), self.holidays)
        self.assertIn(date(2010, 2, 14), self.holidays)
        self.assertIn(date(2010, 2, 15), self.holidays)

    def test_2015(self):
        # New Year's Day
        self.assertIn(date(2015, 1, 1), self.holidays)
        # Chinese New Year day 1
        self.assertIn(date(2015, 2, 19), self.holidays)  # Chinese New Year day 2
        self.assertIn(date(2015, 2, 20), self.holidays)
        # Chinese New Year day 3
        self.assertIn(date(2015, 2, 21), self.holidays)
        # Tomb-Sweeping Day
        self.assertIn(date(2015, 4, 5), self.holidays)
        # Labour Day
        self.assertIn(date(2015, 5, 1), self.holidays)
        # NO Labour Day day 2
        self.assertNotIn(date(2015, 5, 2), self.holidays)
        # NO Labour Day day 3
        self.assertNotIn(date(2015, 5, 3), self.holidays)
        self.assertIn(date(2015, 6, 20), self.holidays)  # Dragon Boat Festival
        self.assertIn(date(2015, 9, 27), self.holidays)  # Mid-Autumn Festival
        self.assertIn(date(2015, 10, 1), self.holidays)  # National Day day 1
        self.assertIn(date(2015, 10, 2), self.holidays)  # National Day day 2
        self.assertIn(date(2015, 10, 3), self.holidays)  # National Day day 3

    def test_pre_1950(self):
        self.assertNotIn(date(1949, 1, 1), self.holidays)
