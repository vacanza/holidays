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


class TestTurkey(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.TR()

    def test_2019(self):
        self.assertIn(date(2019, 1, 1), self.holidays)
        self.assertIn(date(2019, 4, 23), self.holidays)
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 5, 19), self.holidays)
        self.assertIn(date(2019, 7, 15), self.holidays)
        self.assertIn(date(2019, 8, 30), self.holidays)
        self.assertIn(date(2019, 10, 29), self.holidays)

    def test_hijri_based(self):
        if sys.version_info >= (3, 6):
            import importlib.util

            if importlib.util.find_spec("hijri_converter"):
                self.holidays = holidays.TR(years=[2020])
                # Ramadan Feast
                self.assertIn(date(2020, 5, 24), self.holidays)
                self.assertIn(date(2020, 5, 25), self.holidays)
                self.assertIn(date(2020, 5, 26), self.holidays)
                # Sacrifice Feast
                self.assertIn(date(2020, 7, 31), self.holidays)
                self.assertIn(date(2020, 8, 1), self.holidays)
                self.assertIn(date(2020, 8, 2), self.holidays)
                self.assertIn(date(2020, 8, 3), self.holidays)
