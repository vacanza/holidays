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


class TestKenya(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Kenya()

    def test_2019(self):
        # New Year's Day
        self.assertIn(date(2019, 1, 1), self.holidays)
        # Good Friday
        self.assertIn(date(2019, 4, 19), self.holidays)
        # Easter Monday
        self.assertIn(date(2019, 4, 22), self.holidays)
        # Labour Day
        self.assertIn(date(2019, 5, 1), self.holidays)
        # Madaraka Day
        self.assertIn(date(2019, 6, 1), self.holidays)
        # Mashujaa Day
        self.assertIn(date(2019, 10, 20), self.holidays)
        # Jamhuri (Independence) Day
        self.assertIn(date(2019, 12, 12), self.holidays)
        # Christmas Day
        self.assertIn(date(2019, 12, 25), self.holidays)
        # Boxing Day
        self.assertIn(date(2018, 12, 26), self.holidays)
