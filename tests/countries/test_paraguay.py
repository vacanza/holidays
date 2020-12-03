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


class TestParaguay(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.PY()

    def test_fixed_holidays(self):
        checkdates = (
            date(2016, 1, 1),
            date(2020, 1, 1),
            date(2020, 3, 2),
            date(2020, 4, 9),
            date(2020, 5, 1),
            date(2020, 5, 15),
            date(2020, 6, 15),
            date(2020, 8, 15),
            date(2020, 9, 29),
            date(2020, 12, 8),
            date(2020, 12, 25),
        )

        for d in checkdates:
            self.assertIn(d, self.holidays)

    def test_no_observed(self):
        # no observed dates
        self.holidays.observed = False
        checkdates = (
            date(2017, 1, 1),
            date(2014, 3, 2),
            date(2020, 4, 12),
            date(2016, 5, 1),
            date(2016, 5, 15),
            date(2016, 6, 12),
            date(2015, 8, 15),
            date(2018, 9, 29),
            date(2018, 12, 8),
        )

        for d in checkdates:
            self.assertNotIn(d, self.holidays)

    def test_easter(self):
        for year, month, day in [
            (2002, 3, 31),
            (2003, 4, 20),
            (2004, 4, 11),
            (2005, 3, 27),
            (2006, 4, 16),
            (2007, 4, 8),
            (2008, 3, 23),
            (2009, 4, 12),
            (2010, 4, 4),
            (2011, 4, 24),
            (2012, 4, 8),
            (2013, 3, 31),
            (2014, 4, 20),
            (2015, 4, 5),
            (2016, 3, 27),
            (2017, 4, 16),
            (2018, 4, 1),
            (2019, 4, 21),
            (2020, 4, 12),
            (2021, 4, 4),
            (2022, 4, 17),
        ]:
            easter = date(year, month, day)
            easter_thursday = easter - timedelta(days=3)
            easter_friday = easter - timedelta(days=2)
            for holiday in [easter_thursday, easter_friday, easter]:
                self.assertIn(holiday, self.holidays)
