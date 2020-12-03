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


class TestLatvia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.LV()

    def test_2020(self):
        # https://www.officeholidays.com/countries/latvia/2020
        # https://en.wikipedia.org/wiki/Public_holidays_in_Latvia
        # https://likumi.lv/ta/id/72608-par-svetku-atceres-un-atzimejamam-dienam
        self.assertIn(date(2020, 1, 1), self.holidays)
        self.assertIn(date(2020, 4, 10), self.holidays)
        self.assertIn(date(2020, 4, 13), self.holidays)
        self.assertIn(date(2020, 5, 1), self.holidays)
        self.assertIn(date(2020, 5, 4), self.holidays)
        self.assertIn(date(2020, 6, 23), self.holidays)
        self.assertIn(date(2020, 6, 24), self.holidays)
        self.assertIn(date(2020, 11, 18), self.holidays)
        self.assertIn(date(2020, 12, 24), self.holidays)
        self.assertIn(date(2020, 12, 25), self.holidays)
        self.assertIn(date(2020, 12, 26), self.holidays)
        self.assertIn(date(2020, 12, 31), self.holidays)

