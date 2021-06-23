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


class TestBotswana(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.BW()

    def test_new_years(self):
        self.assertIn(date(1966, 1, 1), self.holidays)
        self.assertIn(date(2018, 1, 1), self.holidays)
        self.assertIn(date(2999, 1, 1), self.holidays)
        self.assertIn(date(2017, 1, 2), self.holidays)  # sunday

    def test_easter(self):
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(1994, 4, 1), self.holidays)

    def test_static(self):
        self.assertIn(date(2004, 7, 1), self.holidays)
        self.assertIn(date(2022, 12, 26), self.holidays)  # Christmas

    def test_not_holiday(self):
        self.assertNotIn(date(2016, 12, 28), self.holidays)
        self.assertNotIn(date(2015, 3, 2), self.holidays)
        self.assertNotIn(date(1964, 4, 16), self.holidays)

    def test_onceoff(self):
        self.assertIn(date(2019, 7, 2), self.holidays)

    def test_saturday_and_monday(self):
        self.assertIn(date(2020, 12, 26), self.holidays)
