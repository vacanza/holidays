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



class TestNetherlands(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.NL()

    def test_2017(self):
        # http://www.iamsterdam.com/en/plan-your-trip/practical-info/public-holidays
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 4, 16), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 4, 27), self.holidays)
        self.assertIn(date(2017, 5, 25), self.holidays)
        self.assertIn(date(2017, 6, 4), self.holidays)
        self.assertIn(date(2017, 6, 5), self.holidays)
        self.assertIn(date(2017, 12, 25), self.holidays)
        self.assertIn(date(2017, 12, 26), self.holidays)

    def test_new_years(self):
        self.assertIn(date(2017, 1, 1), self.holidays)

    def test_easter(self):
        self.assertIn(date(2017, 4, 16), self.holidays)

    def test_easter_monday(self):
        self.assertIn(date(2017, 4, 17), self.holidays)

    def test_queens_day_between_1891_and_1948(self):
        # Between 1891 and 1948 Queens Day was celebrated on 8-31
        self.holidays = holidays.NL(years=[1901])
        self.assertIn(date(1901, 8, 31), self.holidays)

    def test_queens_day_between_1891_and_1948_substituted_later(self):
        # Between 1891 and 1948 Queens Day was celebrated on 9-1
        #  (one day later) when Queens Day falls on a Sunday
        self.holidays = holidays.NL(years=[1947])
        self.assertIn(date(1947, 9, 1), self.holidays)

    def test_queens_day_between_1949_and_2013(self):
        self.holidays = holidays.NL(years=[1965])
        self.assertIn(date(1965, 4, 30), self.holidays)

    def test_queens_day_between_1949_and_1980_substituted_later(self):
        self.holidays = holidays.NL(years=[1967])
        self.assertIn(date(1967, 5, 1), self.holidays)

    def test_queens_day_between_1980_and_2013_substituted_earlier(self):
        self.holidays = holidays.NL(years=[2006])
        self.assertIn(date(2006, 4, 29), self.holidays)

    def test_kings_day_after_2014(self):
        self.holidays = holidays.NL(years=[2013])
        self.assertNotIn(date(2013, 4, 27), self.holidays)

        self.holidays = holidays.NL(years=[2017])
        self.assertIn(date(2017, 4, 27), self.holidays)

    def test_kings_day_after_2014_substituted_earlier(self):
        self.holidays = holidays.NL(years=[2188])
        self.assertIn(date(2188, 4, 26), self.holidays)

    def test_liberation_day(self):
        self.holidays = holidays.NL(years=1900)
        self.assertNotIn(date(1900, 5, 5), self.holidays)

    def test_liberation_day_after_1990_non_lustrum_year(self):
        self.holidays = holidays.NL(years=2017)
        self.assertNotIn(date(2017, 5, 5), self.holidays)

    def test_liberation_day_after_1990_in_lustrum_year(self):
        self.holidays = holidays.NL(years=2020)
        self.assertIn(date(2020, 5, 5), self.holidays)

    def test_ascension_day(self):
        self.holidays = holidays.NL(years=2017)
        self.assertIn(date(2017, 5, 25), self.holidays)

    def test_whit_sunday(self):
        self.holidays = holidays.NL(years=2017)
        self.assertIn(date(2017, 6, 4), self.holidays)

    def test_whit_monday(self):
        self.holidays = holidays.NL(years=2017)
        self.assertIn(date(2017, 6, 5), self.holidays)

    def test_first_christmas(self):
        self.holidays = holidays.NL(years=2017)
        self.assertIn(date(2017, 12, 25), self.holidays)

    def test_second_christmas(self):
        self.holidays = holidays.NL(years=2017)
        self.assertIn(date(2017, 12, 26), self.holidays)
