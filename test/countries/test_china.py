# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest

from datetime import date

import holidays

date(1950, 6, 19)


class TestChina(unittest.TestCase):
    # https: // en.wikipedia.org / wiki / Public_holidays_in_China
    def setUp(self):
        self.holidays = holidays.CN()

    def test_between_1949_and_1999(self):
        self.assertIn(date(1950, 1, 1), self.holidays)  # New Year's Day
        self.assertIn(
            date(1950, 2, 17), self.holidays
        )  # Chinese New Year day 1
        self.assertIn(
            date(1950, 2, 18), self.holidays
        )  # Chinese New Year day 2
        self.assertIn(
            date(1950, 2, 19), self.holidays
        )  # Chinese New Year day 3
        self.assertIn(date(1950, 5, 1), self.holidays)  # Labour Day day 1
        self.assertNotIn(
            date(1950, 5, 2), self.holidays
        )  # NO Labour Day day 2
        self.assertNotIn(
            date(1950, 5, 3), self.holidays
        )  # NO Labour Day day 3
        self.assertNotIn(
            date(1950, 6, 19), self.holidays
        )  # NO Dragon Boat Festival
        self.assertNotIn(
            date(1950, 9, 26), self.holidays
        )  # NO Mid-Autumn Festival
        self.assertIn(date(1950, 10, 1), self.holidays)  # National Day day 1
        self.assertIn(date(1950, 10, 2), self.holidays)  # National Day day 2
        self.assertNotIn(
            date(1950, 10, 3), self.holidays
        )  # NO National Day day 3

    def test_between_1999_and_2007(self):
        self.assertIn(date(2005, 1, 1), self.holidays)  # New Year's Day
        self.assertIn(
            date(2005, 2, 9), self.holidays
        )  # Chinese New Year day 1
        self.assertIn(
            date(2005, 2, 10), self.holidays
        )  # Chinese New Year day 2
        self.assertIn(
            date(2005, 2, 11), self.holidays
        )  # Chinese New Year day 3
        self.assertNotIn(
            date(2005, 4, 5), self.holidays
        )  # NO Tomb-Sweeping Day
        self.assertIn(date(2005, 5, 1), self.holidays)  # Labour Day day 1
        self.assertIn(date(2005, 5, 2), self.holidays)  # Labour Day day 2
        self.assertIn(date(2005, 5, 3), self.holidays)  # Labour Day day 3
        self.assertNotIn(
            date(2005, 6, 11), self.holidays
        )  # NO Dragon Boat Festival
        self.assertNotIn(
            date(2005, 9, 18), self.holidays
        )  # NO Mid-Autumn Festival
        self.assertIn(date(2005, 10, 1), self.holidays)  # National Day day 1
        self.assertIn(date(2005, 10, 2), self.holidays)  # National Day day 2
        self.assertIn(date(2005, 10, 3), self.holidays)  # National Day day 3

    def test_after_2007(self):
        self.assertIn(date(2015, 1, 1), self.holidays)  # New Year's Day
        self.assertIn(
            date(2015, 2, 19), self.holidays
        )  # Chinese New Year day 1
        self.assertIn(
            date(2015, 2, 20), self.holidays
        )  # Chinese New Year day 2
        self.assertIn(
            date(2015, 2, 21), self.holidays
        )  # Chinese New Year day 3
        self.assertIn(date(2015, 4, 5), self.holidays)  # Tomb-Sweeping Day
        self.assertIn(date(2015, 5, 1), self.holidays)  # Labour Day
        self.assertNotIn(
            date(2015, 5, 2), self.holidays
        )  # NO Labour Day day 2
        self.assertNotIn(
            date(2015, 5, 3), self.holidays
        )  # NO Labour Day day 3
        self.assertIn(date(2015, 6, 20), self.holidays)  # Dragon Boat Festival
        self.assertIn(date(2015, 9, 27), self.holidays)  # Mid-Autumn Festival
        self.assertIn(date(2015, 10, 1), self.holidays)  # National Day day 1
        self.assertIn(date(2015, 10, 2), self.holidays)  # National Day day 2
        self.assertIn(date(2015, 10, 3), self.holidays)  # National Day day 3
