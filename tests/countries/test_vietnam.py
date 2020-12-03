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


class TestVietnam(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.VN()

    def test_common(self):
        self.assertEqual(
            self.holidays[date(2020, 1, 1)], "International New Year's Day"
        )

    def test_first_day_of_january(self):
        for year in range(1979, 2050):
            self.assertIn(
                "International New Year's Day", self.holidays[date(year, 1, 1)]
            )

    def test_lunar_new_year(self):
        lunar_new_year_list = [
            (2008, 2, 7),
            (2009, 1, 26),
            (2010, 2, 14),
            (2011, 2, 3),
            (2012, 1, 23),
            (2013, 2, 10),
            (2014, 1, 31),
            (2015, 2, 19),
            (2016, 2, 8),
            (2017, 1, 28),
            (2018, 2, 16),
            (2019, 2, 5),
            (2020, 1, 25),
            (2021, 2, 12),
            (2022, 2, 1),
        ]
        for year, month, day in lunar_new_year_list:
            self.assertEqual(
                self.holidays[date(year, month, day) + relativedelta(days=-1)],
                "Vietnamese New Year's Eve",
            )
            self.assertEqual(
                self.holidays[date(year, month, day) + relativedelta(days=0)],
                "Vietnamese New Year",
            )
            self.assertEqual(
                self.holidays[date(year, month, day) + relativedelta(days=+1)],
                "The second day of Tet Holiday",
            )
            self.assertEqual(
                self.holidays[date(year, month, day) + relativedelta(days=+2)],
                "The third day of Tet Holiday",
            )
            self.assertEqual(
                self.holidays[date(year, month, day) + relativedelta(days=+3)],
                "The forth day of Tet Holiday",
            )
            self.assertEqual(
                self.holidays[date(year, month, day) + relativedelta(days=+4)],
                "The fifth day of Tet Holiday",
            )

    def test_king_hung_day(self):
        for year, month, day in [(2020, 4, 2), (2021, 4, 21), (2022, 4, 10)]:
            self.assertEqual(
                self.holidays[date(year, month, day)], "Hung Kings Commemoration Day"
            )

    def test_liberation_day(self):
        for year in range(1979, 2050):
            self.assertIn(
                "Liberation Day/Reunification Day", self.holidays[date(year, 4, 30)]
            )

    def test_international_labor_day(self):
        for year in range(1979, 2050):
            self.assertIn("International Labor Day", self.holidays[date(year, 5, 1)])

    def test_independence_day(self):
        for year in range(1979, 2050):
            self.assertIn("Independence Day", self.holidays[date(year, 9, 2)])

    def test_years_range(self):
        self.holidays = holidays.VN(years=range(1979, 2050))
        for year in range(1979, 2050):
            self.assertIn(
                "International New Year's Day", self.holidays[date(year, 1, 1)]
            )
