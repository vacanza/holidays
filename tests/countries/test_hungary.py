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


class TestHungary(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.HU(observed=False)
        self.next_year = date.today().year + 1

    def test_national_day_was_not_celebrated_during_communism(self):
        for year in range(1951, 1988):
            self.assertNotIn(date(year, 3, 15), self.holidays)
        self.assertIn(date(1989, 3, 15), self.holidays)

    def test_holidays_during_communism(self):
        for year in range(1950, 1989):
            self.assertIn(date(year, 3, 21), self.holidays)
            self.assertIn(date(year, 4, 4), self.holidays)
            if year != 1956:
                self.assertIn(date(year, 11, 7), self.holidays)
        self.assertIn(date(1989, 3, 21), self.holidays)

    def test_foundation_day_renamed_during_communism(self):
        for year in range(1950, 1990):
            self.assertEqual(self.holidays[date(year, 8, 20)], "A kenyér ünnepe")

    def test_christian_holidays_2nd_day_was_not_held_in_1955(self):
        hu_1955 = holidays.Hungary(years=[1955])
        self.assertNotIn(date(1955, 4, 11), hu_1955)
        self.assertNotIn(date(1955, 12, 26), hu_1955)

    def test_good_friday_since_2017(self):
        self.assertNotIn(date(2016, 3, 25), self.holidays)
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2018, 3, 30), self.holidays)

    def test_whit_monday_since_1992(self):
        self.assertNotIn(date(1991, 5, 20), self.holidays)
        self.assertIn(date(1992, 6, 8), self.holidays)

    def test_labour_day_since_1946(self):
        self.assertNotIn(date(1945, 5, 1), self.holidays)
        for year in range(1946, self.next_year):
            self.assertIn(date(year, 5, 1), self.holidays)

    def test_labour_day_was_doubled_in_early_50s(self):
        for year in range(1950, 1954):
            self.assertIn(date(year, 5, 2), self.holidays)

    def test_october_national_day_since_1991(self):
        for year in range(1991, self.next_year):
            self.assertIn(date(year, 10, 23), self.holidays)

    def test_all_saints_day_since_1999(self):
        for year in range(1999, self.next_year):
            self.assertIn(date(year, 11, 1), self.holidays)

    def test_additional_day_off(self):
        observed_days_off = holidays.HU(
            observed=True, years=range(2010, self.next_year)
        )
        for day in [
            date(2010, 12, 24),
            date(2011, 3, 14),
            date(2011, 10, 31),
            date(2012, 3, 16),
            date(2012, 4, 30),
            date(2012, 10, 22),
            date(2012, 11, 2),
            date(2012, 12, 24),
            date(2013, 8, 19),
            date(2013, 12, 24),
            date(2013, 12, 27),
            date(2014, 5, 2),
            date(2014, 10, 24),
            date(2014, 12, 24),
            date(2015, 1, 2),
            date(2015, 8, 21),
            date(2015, 12, 24),
            date(2016, 3, 14),
            date(2016, 10, 31),
            date(2018, 3, 16),
            date(2018, 4, 30),
            date(2018, 10, 22),
            date(2018, 11, 2),
            date(2018, 12, 24),
            date(2018, 12, 31),
            date(2019, 8, 19),
            date(2019, 12, 24),
            date(2019, 12, 27),
        ]:
            self.assertNotIn(day, self.holidays)
            self.assertIn(day, observed_days_off)

    def test_monday_new_years_eve_day_off(self):
        observed_day_off = holidays.HU(observed=True)
        self.assertIn(date(2018, 12, 31), observed_day_off)

    def test_2018(self):
        self.assertIn(date(2018, 1, 1), self.holidays)  # newyear
        self.assertIn(date(2018, 3, 15), self.holidays)  # national holiday
        self.assertIn(date(2018, 3, 30), self.holidays)  # good friday
        self.assertIn(date(2018, 4, 1), self.holidays)  # easter 1.
        self.assertIn(date(2018, 4, 2), self.holidays)  # easter 2.
        self.assertIn(date(2018, 5, 1), self.holidays)  # Workers' Day
        self.assertIn(date(2018, 5, 20), self.holidays)  # Pentecost
        self.assertIn(date(2018, 5, 21), self.holidays)  # Pentecost monday
        self.assertIn(date(2018, 8, 20), self.holidays)  # State Foundation Day
        self.assertIn(date(2018, 10, 23), self.holidays)  # National Day
        self.assertIn(date(2018, 11, 1), self.holidays)  # All Saints' Day
        self.assertIn(date(2018, 12, 25), self.holidays)  # First christmas
        self.assertIn(date(2018, 12, 26), self.holidays)  # Second christmas
