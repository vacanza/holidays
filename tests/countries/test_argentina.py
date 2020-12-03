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


class TestAR(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.AR(observed=True)

    def test_new_years(self):
        self.holidays.observed = False
        self.assertNotIn(date(2010, 12, 31), self.holidays)
        self.assertNotIn(date(2017, 1, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2017, 1, 1), self.holidays)
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_carnival_day(self):
        for dt in [
            date(2018, 2, 12),
            date(2018, 2, 13),
            date(2017, 2, 27),
            date(2017, 2, 28),
            date(2016, 2, 8),
            date(2016, 2, 9),
        ]:
            self.assertIn(dt, self.holidays)

    def test_memory_national_day(self):
        self.holidays.observed = False
        self.assertNotIn(date(1907, 3, 24), self.holidays)
        self.assertNotIn(date(2002, 3, 24), self.holidays)
        self.holidays.observed = True
        for dt in [date(2018, 3, 24), date(2017, 3, 24), date(2016, 3, 24)]:
            self.assertIn(dt, self.holidays)

    def test_holy_week_day(self):
        for dt in [
            date(2018, 3, 29),
            date(2018, 3, 30),
            date(2017, 4, 13),
            date(2017, 4, 14),
            date(2016, 3, 24),
            date(2016, 3, 25),
        ]:
            self.assertIn(dt, self.holidays)

    def test_malvinas_war_day(self):
        for year in range(1900, 2100):
            dt = date(year, 4, 2)
            self.assertIn(dt, self.holidays)

    def test_labor_day(self):
        self.holidays.observed = False
        self.assertNotIn(date(2010, 4, 30), self.holidays)
        self.assertNotIn(date(2011, 5, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(1922, 5, 1), self.holidays)
        for year in range(1900, 2100):
            dt = date(year, 5, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_may_revolution_day(self):
        self.holidays.observed = False
        self.assertNotIn(date(1930, 5, 25), self.holidays)
        self.assertNotIn(date(2014, 5, 25), self.holidays)
        self.holidays.observed = True
        for year in range(1900, 2100):
            dt = date(year, 5, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_guemes_day(self):
        for year in range(1900, 2100):
            dt = date(year, 6, 17)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_belgrano_day(self):
        for year in range(1900, 2100):
            dt = date(year, 6, 20)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_independence_day(self):
        self.holidays.observed = False
        self.assertNotIn(date(2017, 7, 9), self.holidays)
        self.assertNotIn(date(2011, 7, 9), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2017, 7, 9), self.holidays)
        self.assertIn(date(2011, 7, 9), self.holidays)
        for year in range(1900, 2100):
            dt = date(year, 7, 9)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_san_martin_day(self):
        self.holidays.observed = False
        self.assertNotIn(date(1930, 8, 10), self.holidays)
        self.assertNotIn(date(2008, 8, 10), self.holidays)
        self.holidays.observed = True
        for year in range(1900, 2100):
            dt = date(year, 8, 17)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_cultural_day(self):
        self.holidays.observed = False
        self.assertNotIn(date(2014, 10, 12), self.holidays)
        self.assertNotIn(date(1913, 10, 12), self.holidays)
        self.holidays.observed = True
        for year in range(1900, 2100):
            dt = date(year, 10, 12)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_national_sovereignty_day(self):
        for year in range(1900, 2100):
            dt = date(year, 11, 20)
            if year < 2010:
                self.assertNotIn(dt, self.holidays)
            else:
                self.assertIn(dt, self.holidays)
                self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
                self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_inmaculate_conception_day(self):
        self.holidays.observed = False
        self.assertNotIn(date(1940, 12, 8), self.holidays)
        self.assertNotIn(date(2013, 12, 8), self.holidays)
        self.holidays.observed = True
        for year in range(1900, 2100):
            dt = date(year, 12, 8)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_christmas(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

