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


class TestSingapore(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Singapore()

    def test_Singapore(self):
        # <= 1968 holidays
        self.assertIn(date(1968, 4, 13), self.holidays)
        self.assertIn(date(1968, 4, 15), self.holidays)
        self.assertIn(date(1968, 12, 26), self.holidays)
        # latest polling day
        self.assertIn(date(2015, 9, 11), self.holidays)
        # SG50
        self.assertIn(date(2015, 8, 7), self.holidays)
        # Year with lunar leap month
        self.assertIn(date(2015, 8, 7), self.holidays)
        # Latest holidays
        # Source: https://www.mom.gov.sg/employment-practices/public-holidays
        # 2018
        self.assertIn(date(2018, 1, 1), self.holidays)
        self.assertIn(date(2018, 2, 16), self.holidays)
        self.assertIn(date(2018, 2, 17), self.holidays)
        self.assertIn(date(2018, 3, 30), self.holidays)
        self.assertIn(date(2018, 5, 1), self.holidays)
        self.assertIn(date(2018, 5, 29), self.holidays)
        self.assertIn(date(2018, 6, 15), self.holidays)
        self.assertIn(date(2018, 8, 9), self.holidays)
        self.assertIn(date(2018, 8, 22), self.holidays)
        self.assertIn(date(2018, 11, 6), self.holidays)
        self.assertIn(date(2018, 12, 25), self.holidays)
        # total holidays (11 + 0 falling on a Sunday)
        self.assertEqual(len(holidays.Singapore(years=[2018])), 11 + 0)
        # 2019
        self.assertIn(date(2019, 1, 1), self.holidays)
        self.assertIn(date(2019, 2, 5), self.holidays)
        self.assertIn(date(2019, 2, 6), self.holidays)
        self.assertIn(date(2019, 4, 19), self.holidays)
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 5, 19), self.holidays)
        self.assertIn(date(2019, 6, 5), self.holidays)
        self.assertIn(date(2019, 8, 9), self.holidays)
        self.assertIn(date(2019, 8, 11), self.holidays)
        self.assertIn(date(2019, 10, 27), self.holidays)
        self.assertIn(date(2019, 12, 25), self.holidays)
        # total holidays (11 + 3 falling on a Sunday)
        self.assertEqual(len(holidays.Singapore(years=[2019])), 11 + 3)
        # 2020
        self.assertIn(date(2020, 1, 1), self.holidays)
        self.assertIn(date(2020, 1, 25), self.holidays)
        self.assertIn(date(2020, 1, 26), self.holidays)
        self.assertIn(date(2020, 4, 10), self.holidays)
        self.assertIn(date(2020, 5, 1), self.holidays)
        self.assertIn(date(2020, 5, 7), self.holidays)
        self.assertIn(date(2020, 5, 24), self.holidays)
        self.assertIn(date(2020, 7, 31), self.holidays)
        self.assertIn(date(2020, 8, 9), self.holidays)
        self.assertIn(date(2020, 11, 14), self.holidays)
        self.assertIn(date(2020, 12, 25), self.holidays)
        # total holidays (11 + 3 falling on a Sunday)
        self.assertEqual(len(holidays.Singapore(years=[2020])), 11 + 4)
        # holidays estimated using lunar calendar
        self.assertIn(date(2021, 5, 26), self.holidays)
        self.assertIn(date(2021, 11, 4), self.holidays)
        # holidays estimated using library hijri-converter
        if sys.version_info >= (3, 6):
            import importlib.util

            if importlib.util.find_spec("hijri_converter"):
                # <= 1968 holidays
                self.assertIn(date(1968, 1, 2), self.holidays)
                # 2021
                self.assertIn(date(2021, 5, 13), self.holidays)
                self.assertIn(date(2021, 7, 20), self.holidays)
