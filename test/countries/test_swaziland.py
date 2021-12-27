# -*- coding: utf-8 -*-

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


class TestSwaziland(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.SZ()

    def test_out_of_range(self):
        self.assertNotIn(date(1920, 1, 1), self.holidays)
        self.assertNotIn(date(1938, 1, 1), self.holidays)

    def test_new_years(self):
        self.assertIn(date(1996, 1, 1), self.holidays)
        self.assertIn(date(2000, 1, 1), self.holidays)
        self.assertIn(date(2001, 1, 1), self.holidays)

    def test_easter(self):
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 5, 25), self.holidays)
        self.assertNotIn(date(2017, 5, 26), self.holidays)

    def test_once_off(self):
        self.assertIn(date(1999, 12, 31), self.holidays)  # y2k
        self.assertIn(date(2000, 1, 3), self.holidays)  # y2k

    def test_national_flag_day(self):
        self.assertNotIn(date(1968, 4, 25), self.holidays)
        self.assertIn(date(2006, 4, 25), self.holidays)

    def test_kings_birthday(self):
        self.assertNotIn(date(1982, 7, 22), self.holidays)
        self.assertIn(date(1983, 7, 22), self.holidays)
        self.assertIn(date(1987, 4, 19), self.holidays)
        self.assertNotIn(date(1986, 4, 19), self.holidays)
        self.assertNotIn(date(1985, 4, 19), self.holidays)

    def test_holidays(self):
        self.assertIn(date(2020, 5, 1), self.holidays)
        self.assertIn(date(2020, 9, 6), self.holidays)
        self.assertIn(date(2020, 12, 25), self.holidays)
        self.assertIn(date(2020, 12, 26), self.holidays)

    def test_observed(self):
        self.assertIn(date(2021, 4, 26), self.holidays)
        self.assertIn(date(2021, 12, 27), self.holidays)
        self.assertIn(date(2023, 1, 2), self.holidays)
