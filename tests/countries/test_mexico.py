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




class TestMX(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.MX(observed=False)

    def test_new_years(self):
        self.assertNotIn(date(2010, 12, 31), self.holidays)
        self.assertNotIn(date(2017, 1, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2010, 12, 31), self.holidays)
        self.assertIn(date(2017, 1, 2), self.holidays)
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_constitution_day(self):
        for dt in [
            date(2005, 2, 5),
            date(2006, 2, 5),
            date(2007, 2, 5),
            date(2009, 2, 5),
            date(2010, 2, 5),
            date(2015, 2, 5),
            date(2016, 2, 5),
            date(2020, 2, 5),
            date(2021, 2, 5),
            date(2022, 2, 5),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.holidays.observed = True
        for dt in [
            date(2005, 2, 5),
            date(2006, 2, 5),
            date(2007, 2, 5),
            date(2009, 2, 5),
            date(2009, 2, 2),
            date(2010, 2, 5),
            date(2010, 2, 1),
            date(2015, 2, 5),
            date(2015, 2, 2),
            date(2016, 2, 5),
            date(2016, 2, 1),
            date(2020, 2, 5),
            date(2020, 2, 3),
            date(2021, 2, 5),
            date(2021, 2, 1),
            date(2022, 2, 5),
            date(2022, 2, 7),
        ]:
            self.assertIn(dt, self.holidays)
        self.holidays.observed = False

    def test_benito_juarez(self):
        for dt in [
            date(2005, 3, 21),
            date(2006, 3, 21),
            date(2007, 3, 21),
            date(2008, 3, 21),
            date(2009, 3, 21),
            date(2010, 3, 21),
            date(2015, 3, 21),
            date(2016, 3, 21),
            date(2020, 3, 21),
            date(2021, 3, 21),
            date(2022, 3, 21),
            date(2024, 3, 21),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.holidays.observed = True
        for dt in [
            date(2005, 3, 21),
            date(2006, 3, 21),
            date(2007, 3, 21),
            date(2007, 3, 19),
            date(2008, 3, 21),
            date(2008, 3, 17),
            date(2009, 3, 21),
            date(2009, 3, 16),
            date(2010, 3, 21),
            date(2010, 3, 15),
            date(2015, 3, 21),
            date(2015, 3, 16),
            date(2016, 3, 21),
            date(2020, 3, 21),
            date(2020, 3, 16),
            date(2021, 3, 21),
            date(2021, 3, 15),
            date(2022, 3, 21),
            date(2024, 3, 21),
            date(2024, 3, 18),
        ]:
            self.assertIn(dt, self.holidays)
        self.holidays.observed = False

    def test_labor_day(self):
        self.assertNotIn(date(2010, 4, 30), self.holidays)
        self.assertNotIn(date(2011, 5, 2), self.holidays)
        self.assertNotIn(date(2022, 5, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2010, 4, 30), self.holidays)
        self.assertIn(date(2011, 5, 2), self.holidays)
        self.assertIn(date(2022, 5, 2), self.holidays)
        self.holidays.observed = False
        self.assertNotIn(date(1922, 5, 1), self.holidays)
        for year in range(1923, 2100):
            dt = date(year, 5, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_independence_day(self):
        self.assertNotIn(date(2006, 9, 15), self.holidays)
        self.assertNotIn(date(2007, 9, 17), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2006, 9, 15), self.holidays)
        self.assertIn(date(2007, 9, 17), self.holidays)
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 9, 16)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_revolution_day(self):
        for dt in [
            date(2005, 11, 20),
            date(2006, 11, 20),
            date(2007, 11, 20),
            date(2008, 11, 20),
            date(2009, 11, 20),
            date(2010, 11, 20),
            date(2015, 11, 20),
            date(2016, 11, 20),
            date(2020, 11, 20),
            date(2021, 11, 20),
            date(2022, 11, 20),
            date(2023, 11, 20),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.holidays.observed = True
        for dt in [
            date(2005, 11, 20),
            date(2006, 11, 20),
            date(2007, 11, 19),
            date(2008, 11, 17),
            date(2009, 11, 16),
            date(2010, 11, 15),
            date(2015, 11, 16),
            date(2016, 11, 21),
            date(2020, 11, 16),
        ]:
            self.assertIn(dt, self.holidays)
        self.holidays.observed = False

    def test_change_of_government(self):
        self.assertNotIn(date(2012, 11, 30), self.holidays)
        self.assertNotIn(date(2024, 12, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2012, 11, 30), self.holidays)
        self.assertIn(date(2024, 12, 2), self.holidays)
        self.holidays.observed = False
        for year in range(1950, 2100):
            dt = date(year, 12, 1)
            if (year >= 1970) and ((2096 - year) % 6) == 0:
                self.assertIn(dt, self.holidays)
                self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
                self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            else:
                self.assertNotIn(dt, self.holidays)

    def test_christmas(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.assertNotIn(date(2010, 12, 24), self.holidays)
        self.assertNotIn(date(2016, 12, 26), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2010, 12, 24), self.holidays)
        self.assertIn(date(2016, 12, 26), self.holidays)
