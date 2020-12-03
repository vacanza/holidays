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


class TestCO(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.CO(observed=True)

    def test_2016(self):
        # http://www.officeholidays.com/countries/colombia/
        self.assertIn(date(2016, 1, 1), self.holidays)
        self.assertIn(date(2016, 1, 11), self.holidays)
        self.assertIn(date(2016, 3, 21), self.holidays)
        self.assertIn(date(2016, 3, 24), self.holidays)
        self.assertIn(date(2016, 3, 25), self.holidays)
        self.assertIn(date(2016, 5, 1), self.holidays)
        self.assertIn(date(2016, 5, 9), self.holidays)
        self.assertIn(date(2016, 5, 30), self.holidays)
        self.assertIn(date(2016, 6, 6), self.holidays)
        self.assertIn(date(2016, 7, 4), self.holidays)
        self.assertIn(date(2016, 7, 20), self.holidays)
        self.assertIn(date(2016, 8, 7), self.holidays)
        self.assertIn(date(2016, 8, 15), self.holidays)
        self.assertIn(date(2016, 10, 17), self.holidays)
        self.assertIn(date(2016, 11, 7), self.holidays)
        self.assertIn(date(2016, 11, 14), self.holidays)
        self.assertIn(date(2016, 12, 8), self.holidays)
        self.assertIn(date(2016, 12, 25), self.holidays)

    def test_others(self):
        # holidays falling on weekend
        self.assertNotIn(date(2017, 1, 1), self.holidays)
        self.assertNotIn(date(2014, 7, 20), self.holidays)
        self.assertNotIn(date(2018, 8, 12), self.holidays)

        self.assertIn(date(2014, 1, 6), self.holidays)
        self.assertIn(date(2012, 3, 19), self.holidays)
        self.assertIn(date(2015, 6, 29), self.holidays)
        self.assertIn(date(2010, 8, 16), self.holidays)
        self.assertIn(date(2015, 10, 12), self.holidays)
        self.assertIn(date(2010, 11, 1), self.holidays)
        self.assertIn(date(2013, 11, 11), self.holidays)
        self.holidays.observed = False
        self.assertIn(date(2016, 5, 5), self.holidays)
        self.assertIn(date(2016, 5, 26), self.holidays)
