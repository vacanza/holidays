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


class TestCZ(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.CZ()

    def test_2017(self):
        # http://www.officeholidays.com/countries/czech_republic/2017.php
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 5, 1), self.holidays)
        self.assertIn(date(2017, 5, 8), self.holidays)
        self.assertIn(date(2017, 7, 5), self.holidays)
        self.assertIn(date(2017, 7, 6), self.holidays)
        self.assertIn(date(2017, 9, 28), self.holidays)
        self.assertIn(date(2017, 10, 28), self.holidays)
        self.assertIn(date(2017, 11, 17), self.holidays)
        self.assertIn(date(2017, 12, 24), self.holidays)
        self.assertIn(date(2017, 12, 25), self.holidays)
        self.assertIn(date(2017, 12, 26), self.holidays)

    def test_others(self):
        self.assertIn(date(1991, 5, 9), self.holidays)

    def test_czech_deprecated(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            czech = holidays.Czech()
            self.assertIsInstance(czech, holidays.Czechia)
            self.assertEqual(1, len(w))
            self.assertTrue(issubclass(w[-1].category, DeprecationWarning))
