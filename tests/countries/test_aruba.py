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

import os
import sys
import unittest
import warnings
from glob import glob
from itertools import product

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta, MO
from flake8.api import legacy as flake8

import holidays


class TestAruba(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.AW()

    def test_2017(self):
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 1, 25), self.holidays)
        self.assertIn(date(2017, 3, 18), self.holidays)
        self.assertIn(date(2017, 2, 27), self.holidays)
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 4, 27), self.holidays)
        self.assertIn(date(2017, 5, 1), self.holidays)
        self.assertIn(date(2017, 5, 25), self.holidays)
        self.assertIn(date(2017, 12, 25), self.holidays)
        self.assertIn(date(2017, 12, 26), self.holidays)

    def test_new_years(self):
        self.assertIn(date(2017, 1, 1), self.holidays)

    def test_betico_day(self):
        self.assertIn(date(2017, 1, 25), self.holidays)

    def test_carnaval_monday(self):
        self.assertIn(date(2017, 2, 27), self.holidays)

    def test_anthem_and_flag_day(self):
        self.assertIn(date(2017, 3, 18), self.holidays)

    def test_good_friday(self):
        self.assertIn(date(2017, 4, 14), self.holidays)

    def test_easter_monday(self):
        self.assertIn(date(2017, 4, 17), self.holidays)

    def test_labour_day(self):
        self.assertIn(date(2017, 5, 1), self.holidays)

    def test_queens_day_between_1891_and_1948(self):
        # Between 1891 and 1948 Queens Day was celebrated on 8-31
        self.holidays = holidays.AW(years=[1901])
        self.assertIn(date(1901, 8, 31), self.holidays)

    def test_queens_day_between_1891_and_1948_substituted_later(self):
        # Between 1891 and 1948 Queens Day was celebrated on 9-1
        #  (one day later) when Queens Day falls on a Sunday
        self.holidays = holidays.AW(years=[1947])
        self.assertIn(date(1947, 9, 1), self.holidays)

    def test_queens_day_between_1949_and_2013(self):
        self.holidays = holidays.AW(years=[1965])
        self.assertIn(date(1965, 4, 30), self.holidays)

    def test_queens_day_between_1949_and_1980_substituted_later(self):
        self.holidays = holidays.AW(years=[1967])
        self.assertIn(date(1967, 5, 1), self.holidays)

    def test_queens_day_between_1980_and_2013_substituted_earlier(self):
        self.holidays = holidays.AW(years=[2006])
        self.assertIn(date(2006, 4, 29), self.holidays)

    def test_kings_day_after_2014(self):
        self.holidays = holidays.AW(years=[2013])
        self.assertNotIn(date(2013, 4, 27), self.holidays)

        self.holidays = holidays.AW(years=[2017])
        self.assertIn(date(2017, 4, 27), self.holidays)

    def test_kings_day_after_2014_substituted_earlier(self):
        self.holidays = holidays.AW(years=[2188])
        self.assertIn(date(2188, 4, 26), self.holidays)

    def test_ascension_day(self):
        self.holidays = holidays.AW(years=2017)
        self.assertIn(date(2017, 5, 25), self.holidays)

    def test_christmas(self):
        self.holidays = holidays.AW(years=2017)
        self.assertIn(date(2017, 12, 25), self.holidays)

    def test_second_christmas(self):
        self.holidays = holidays.AW(years=2017)
        self.assertIn(date(2017, 12, 26), self.holidays)
