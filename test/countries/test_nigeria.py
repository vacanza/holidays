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


class TestNigeria(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Nigeria()

    def test_not_holiday(self):
        self.assertNotIn(date(1966, 1, 1), self.holidays)

    def test_fixed_holidays(self):
        self.assertIn(date(2015, 5, 29), self.holidays)
        self.assertIn(date(2019, 1, 1), self.holidays)
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 6, 12), self.holidays)
        self.assertIn(date(2019, 10, 1), self.holidays)
        self.assertIn(date(2019, 12, 25), self.holidays)
        self.assertIn(date(2019, 12, 26), self.holidays)
        self.assertIn(date(2020, 6, 12), self.holidays)
        self.assertIn(date(2021, 6, 14), self.holidays)
