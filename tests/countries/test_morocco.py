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


class TestMorocco(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Morocco()

    def test_2019(self):
        _holidays = [
            date(2019, 1, 1),
            date(2019, 1, 11),
            date(2019, 5, 1),
            date(2019, 7, 30),
            date(2019, 8, 14),
            date(2019, 8, 20),
            date(2019, 8, 21),
            date(2019, 11, 6),
            date(2019, 11, 18),
        ]

        for holiday in _holidays:
            self.assertIn(holiday, self.holidays)

    def test_1999(self):
        self.holidays = holidays.Morocco(years=[1999])
        _holidays = [
            date(1999, 1, 1),
            date(1999, 1, 11),
            date(1999, 5, 1),
            date(1999, 3, 3),
            date(1999, 8, 14),
            date(1999, 8, 20),
            date(1999, 7, 9),
            date(1999, 11, 6),
            date(1999, 11, 18),
        ]

        for holiday in _holidays:
            self.assertIn(holiday, self.holidays)

    def test_1961(self):
        self.holidays = holidays.Morocco(years=[1961])
        _holidays = [
            date(1961, 11, 18),
        ]

        for holiday in _holidays:
            self.assertIn(holiday, self.holidays)

    def test_hijri_based(self):
        if sys.version_info >= (3, 6):
            import importlib.util

            if importlib.util.find_spec("hijri_converter"):
                self.holidays = holidays.Morocco(years=[2019, 1999])
                # eid_alfitr
                self.assertIn(date(2019, 6, 4), self.holidays)
                self.assertIn(date(2019, 6, 5), self.holidays)
                # eid_aladha
                self.assertIn(date(2019, 8, 11), self.holidays)
                self.assertIn(date(2019, 8, 12), self.holidays)
                # islamic_new_year
                self.assertIn(date(2019, 8, 31), self.holidays)

                self.assertIn(date(2019, 11, 9), self.holidays)
                self.assertIn(date(2019, 11, 10), self.holidays)

                self.assertIn(date(1999, 4, 17), self.holidays)
