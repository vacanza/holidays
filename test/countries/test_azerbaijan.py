# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import sys
import unittest

from datetime import date

import holidays
from holidays.constants import JAN, MAR, MAY, JUN, NOV, DEC


class TestAzerbaijan(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.AZ()

    def test_observed_days(self):
        self.assertIn(date(2021, JUN, 28), self.holidays)
        self.assertIn(date(2021, MAY, 10), self.holidays)
        self.assertIn(date(2021, JAN, 4), self.holidays)
        self.assertIn(date(2020, MAY, 11), self.holidays)
        self.assertIn(date(2020, MAR, 9), self.holidays)

    def test_victory_day(self):
        self.assertNotIn(date(2020, NOV, 8), self.holidays)
        self.assertIn(date(2021, NOV, 8), self.holidays)

    def test_2020(self):
        self.assertIn(date(2020, JAN, 1), self.holidays)
        self.assertIn(date(2020, JAN, 2), self.holidays)
        self.assertIn(date(2020, JAN, 20), self.holidays)
        self.assertIn(date(2020, MAR, 8), self.holidays)
        for day in range(20, 25):
            self.assertIn(date(2020, MAR, day), self.holidays)
        self.assertIn(date(2020, MAY, 9), self.holidays)
        self.assertIn(date(2020, JUN, 15), self.holidays)
        self.assertIn(date(2020, JUN, 26), self.holidays)
        self.assertNotIn(date(2020, NOV, 8), self.holidays)
        self.assertIn(date(2020, NOV, 9), self.holidays)
        self.assertIn(date(2020, DEC, 31), self.holidays)

    def test_hijri_based(self):
        if sys.version_info >= (3, 6):
            import importlib.util

            if importlib.util.find_spec("hijri_converter"):
                self.holidays = holidays.AZ(years=[2020])
                # Ramadan Feast
                self.assertIn(date(2020, 5, 24), self.holidays)
                self.assertIn(date(2020, 5, 25), self.holidays)
                # Sacrifice Feast
                self.assertIn(date(2020, 7, 31), self.holidays)
                self.assertIn(date(2020, 8, 1), self.holidays)
                self.assertIn(date(2020, 8, 3), self.holidays)  # observed

    def test_dec_31_on_weekend(self):
        """Test when Dec 31 of previous year is on a weekend."""
        self.assertIn(date(2023, JAN, 2), self.holidays)
        self.assertIn(date(2024, JAN, 1), self.holidays)
