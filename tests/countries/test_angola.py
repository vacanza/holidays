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


class TestAngola(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.AO()

    def test_new_years(self):
        self.assertIn("1975-01-01", self.holidays)
        self.assertIn("2017-01-01", self.holidays)
        self.assertIn("2999-01-01", self.holidays)
        self.assertIn("2017-01-02", self.holidays)  # sunday

    def test_easter(self):
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2020, 4, 10), self.holidays)
        self.assertIn(date(1994, 4, 1), self.holidays)

    def test_static(self):
        self.assertIn("2004-03-08", self.holidays)
        self.assertIn("2020-03-23", self.holidays)

    def test_long_weekend(self):
        self.assertIn("2020-02-03", self.holidays)
        self.assertIn("2019-04-05", self.holidays)
        self.assertIn("2050-03-07", self.holidays)

    def test_not_holiday(self):
        self.assertNotIn("2016-12-28", self.holidays)
        self.assertNotIn("2015-03-02", self.holidays)
        self.assertNotIn("2018-03-23", self.holidays)
