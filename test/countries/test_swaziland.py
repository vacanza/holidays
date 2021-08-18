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


class TestSwaziland(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.SZ()

    def test_new_years(self):
        self.assertIn(date(1996, 1, 1), self.holidays)
        self.assertIn(date(2000, 1, 1), self.holidays)
        self.assertIn(date(2001, 1, 1), self.holidays)
        self.assertNotIn(date(2021, 1, 5), self.holidays)

    def test_easter(self):
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2017, 4, 16), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2021, 5, 13), self, holidays)  # ascension day

    def test_once_off(self):
        self.assertIn(date(1999, 12, 31), self.holidays)  # y2k
        self.assertIn(date(2000, 1, 3), self.holidays)  # y2k

    def test_national_flag_day(self):
        self.assertIn(date(2004, 3, 26), self.holidays)
        self.assertIn(date(2005, 3, 25), self.holidays)
        self.assertNotIn(date(2005, 3, 26), self.holidays)

    def test_kings_birthday(self):
        self.assertIn(date(1983, 7, 22), self.holidays)
        self.assertIn(date(1987, 4, 19), self.holidays)
        self.assertNotIn(date(1985, 4, 19), self.holidays)

    def test_normal_days(self):
        self.assertIn(date(2020, 5, 1), self.holidays)
        self.assertIn(date(2020, 9, 6), self.holidays)
        self.assertIn(date(2020, 12, 25), self.holidays)
        self.assertIn(date(2020, 12, 26), self.holidays)

    def test_observed(self):
        self.assertIn(date(2021, 5, 3), self.holidays)
        self.assertIn(date(2021, 12, 27), self.holidays)
        self.assertNotIn(
            date(2021, 12, 28), self.holidays
        )  # exception with christmas day and boxing day
