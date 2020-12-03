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


class TestPT(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.PT()

    def test_2017(self):
        # http://www.officeholidays.com/countries/portugal/2017.php
        self.assertIn(date(2017, 1, 1), self.holidays)  # New Year
        self.assertIn(date(2017, 4, 14), self.holidays)  # Good Friday
        self.assertIn(date(2017, 4, 16), self.holidays)  # Easter
        self.assertIn(date(2017, 4, 25), self.holidays)  # Liberation Day
        self.assertIn(date(2017, 5, 1), self.holidays)  # Labour Day
        self.assertIn(date(2017, 6, 10), self.holidays)  # Portugal Day
        self.assertIn(date(2017, 6, 15), self.holidays)  # Corpus Christi
        self.assertIn(date(2017, 8, 15), self.holidays)  # Assumption Day
        self.assertIn(date(2017, 10, 5), self.holidays)  # Republic Day
        self.assertIn(date(2017, 11, 1), self.holidays)  # All Saints Day
        self.assertIn(date(2017, 12, 1), self.holidays)  # Independence
        self.assertIn(date(2017, 12, 8), self.holidays)  # Immaculate
        self.assertIn(date(2017, 12, 25), self.holidays)  # Christmas


class TestPortugalExt(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.PortugalExt()

    def test_2017(self):
        self.assertIn(date(2017, 12, 24), self.holidays)  # Christmas' Eve
        self.assertIn(date(2017, 12, 26), self.holidays)  # S.Stephan
        self.assertIn(date(2017, 12, 26), self.holidays)  # New Year's Eve
