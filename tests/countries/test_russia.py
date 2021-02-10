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


class TestRussia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.RU()

    def test_before_2005(self):
        self.assertIn(date(2004, 11, 7), self.holidays)
        self.assertNotIn(date(2004, 11, 4), self.holidays)

    def test_2018(self):
        # https://en.wikipedia.org/wiki/Public_holidays_in_Russia
        self.assertIn(date(2018, 1, 1), self.holidays)
        self.assertIn(date(2018, 1, 2), self.holidays)
        self.assertIn(date(2018, 1, 3), self.holidays)
        self.assertIn(date(2018, 1, 4), self.holidays)
        self.assertIn(date(2018, 1, 5), self.holidays)
        self.assertIn(date(2018, 1, 6), self.holidays)
        self.assertIn(date(2018, 1, 7), self.holidays)
        self.assertIn(date(2018, 1, 8), self.holidays)
        self.assertIn(date(2018, 2, 23), self.holidays)
        self.assertIn(date(2018, 3, 8), self.holidays)
        self.assertIn(date(2018, 5, 1), self.holidays)
        self.assertIn(date(2018, 5, 9), self.holidays)
        self.assertIn(date(2018, 6, 12), self.holidays)
        self.assertIn(date(2018, 11, 4), self.holidays)
        self.assertNotIn(date(2018, 11, 7), self.holidays)
