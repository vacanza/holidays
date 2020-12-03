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


class TestDjibouti(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.DJ()

    def test_2019(self):
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 6, 27), self.holidays)
        self.assertIn(date(2019, 6, 28), self.holidays)

    def test_labour_day(self):
        self.assertIn(date(2019, 5, 1), self.holidays)

    def test_hijri_based(self):
        if sys.version_info >= (3, 6):
            import importlib.util

            if importlib.util.find_spec("hijri_converter"):
                self.holidays = holidays.DJ(years=[2010])
                self.assertIn(date(2019, 6, 5), self.holidays)
                self.assertIn(date(2019, 8, 10), self.holidays)
                self.assertIn(date(2019, 8, 11), self.holidays)
                self.assertIn(date(2019, 8, 12), self.holidays)
                self.assertIn(date(2019, 8, 31), self.holidays)
                self.assertIn(date(2019, 11, 9), self.holidays)
                # eid_alfitr
                self.assertIn(date(2019, 6, 5), self.holidays)
                # eid_aladha
                self.assertIn(date(2019, 8, 11), self.holidays)
                # islamic_new_year
                self.assertIn(date(2019, 8, 31), self.holidays)
                # arafat_2019
                self.assertIn(date(2019, 8, 10), self.holidays)
                # muhammad's birthday 2019
                self.assertIn(date(2019, 11, 9), self.holidays)
