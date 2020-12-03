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


class TestCroatia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.HR()

    def test_2018(self):
        self.assertIn(date(2018, 1, 1), self.holidays)
        self.assertIn(date(2018, 1, 6), self.holidays)
        self.assertIn(date(2018, 4, 1), self.holidays)
        self.assertIn(date(2018, 4, 2), self.holidays)
        self.assertIn(date(2018, 5, 1), self.holidays)
        self.assertIn(date(2018, 6, 25), self.holidays)
        self.assertIn(date(2018, 8, 15), self.holidays)
        self.assertIn(date(2018, 10, 8), self.holidays)
        self.assertIn(date(2018, 11, 1), self.holidays)
        self.assertIn(date(2018, 12, 25), self.holidays)
        self.assertIn(date(2018, 12, 26), self.holidays)

    def test_2020_new(self):
        self.assertIn(date(2020, 5, 30), self.holidays)
        self.assertIn(date(2020, 11, 18), self.holidays)
