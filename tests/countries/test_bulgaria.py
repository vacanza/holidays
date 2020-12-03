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



class TestBulgaria(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Bulgaria()

    def test_before_1990(self):
        self.assertEqual(len(holidays.Bulgaria(years=[1989])), 0)

    def test_new_years_day(self):
        for year in range(1990, 2020):
            self.assertIn(date(year, 1, 1), self.holidays)

    def test_liberation_day(self):
        for year in range(1990, 2020):
            self.assertIn(date(year, 3, 3), self.holidays)

    def test_labour_day(self):
        for year in range(1990, 2020):
            self.assertIn(date(year, 5, 1), self.holidays)

    def test_saint_georges_day(self):
        for year in range(1990, 2020):
            self.assertIn(date(year, 5, 6), self.holidays)

    def test_twenty_fourth_of_may(self):
        for year in range(1990, 2020):
            self.assertIn(date(year, 5, 24), self.holidays)

    def test_unification_day(self):
        for year in range(1990, 2020):
            self.assertIn(date(year, 9, 6), self.holidays)

    def test_independence_day(self):
        for year in range(1990, 2020):
            self.assertIn(date(year, 9, 22), self.holidays)

    def test_national_awakening_day(self):
        for year in range(1990, 2020):
            self.assertIn(date(year, 11, 1), self.holidays)

    def test_christmas(self):
        for year in range(1990, 2020):
            self.assertIn(date(year, 12, 24), self.holidays)
            self.assertIn(date(year, 12, 25), self.holidays)
            self.assertIn(date(year, 12, 26), self.holidays)

    def test_easter(self):
        for year, month, day in [
            (2000, 4, 30),
            (2001, 4, 15),
            (2002, 5, 5),
            (2003, 4, 27),
            (2004, 4, 11),
            (2005, 5, 1),
            (2006, 4, 23),
            (2007, 4, 8),
            (2008, 4, 27),
            (2009, 4, 19),
            (2010, 4, 4),
            (2011, 4, 24),
            (2012, 4, 15),
            (2013, 5, 5),
            (2014, 4, 20),
            (2015, 4, 12),
            (2016, 5, 1),
            (2017, 4, 16),
            (2018, 4, 8),
            (2019, 4, 28),
            (2020, 4, 19),
            (2021, 5, 2),
            (2022, 4, 24),
        ]:
            easter = date(year, month, day)
            easter_saturday = easter - timedelta(days=1)
            easter_friday = easter - timedelta(days=2)
            for holiday in [easter_friday, easter_saturday, easter]:
                self.assertIn(holiday, self.holidays)
