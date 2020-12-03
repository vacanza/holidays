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


class TestAT(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.AT()

    def test_new_years(self):
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_christmas(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+2), self.holidays)

    def test_easter_monday(self):
        for dt in [
            date(1900, 4, 16),
            date(1901, 4, 8),
            date(1902, 3, 31),
            date(1999, 4, 5),
            date(2000, 4, 24),
            date(2010, 4, 5),
            date(2018, 4, 2),
            date(2019, 4, 22),
            date(2020, 4, 13),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_national_day(self):
        for year in range(1919, 1934):
            dt = date(year, 11, 12)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        for year in range(1967, 2100):
            dt = date(year, 10, 26)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_all_holidays_present(self):
        at_2015 = holidays.AT(years=[2015])
        all_holidays = [
            "Neujahr",
            "Heilige Drei Könige",
            "Ostermontag",
            "Staatsfeiertag",
            "Christi Himmelfahrt",
            "Pfingstmontag",
            "Fronleichnam",
            "Mariä Himmelfahrt",
            "Nationalfeiertag",
            "Allerheiligen",
            "Mariä Empfängnis",
            "Christtag",
            "Stefanitag",
        ]
        for holiday in all_holidays:
            self.assertIn(holiday, at_2015.values())
