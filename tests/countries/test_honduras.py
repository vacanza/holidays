# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2020
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest

from datetime import date

import holidays


class TestHonduras(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.HND()

    def test_2014(self):
        self.assertIn(date(2014, 10, 3), self.holidays)  # Morazan's Day
        self.assertIn(date(2014, 10, 12), self.holidays)  # Columbus Day
        self.assertIn(date(2014, 10, 21), self.holidays)  # Army Day

    def test_2018(self):
        self.assertIn(date(2018, 1, 1), self.holidays)  # New Year
        self.assertIn(date(2018, 4, 14), self.holidays)  # America's Day
        self.assertIn(date(2018, 5, 1), self.holidays)  # Workers' Day
        self.assertNotIn(date(2018, 5, 6), self.holidays)  # Mother's Day
        self.assertIn(date(2018, 5, 13), self.holidays)  # Mother's Day
        self.assertIn(date(2018, 9, 10), self.holidays)  # Children weekend
        self.assertIn(date(2018, 9, 15), self.holidays)  # Independence Day
        self.assertIn(date(2018, 9, 17), self.holidays)  # Teacher's Day
        self.assertIn(date(2018, 10, 3), self.holidays)  # Morazan's weekend
        self.assertIn(date(2018, 12, 25), self.holidays)  # Christmas
