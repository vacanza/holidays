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

import sys
import unittest

from datetime import date

import holidays


class UnitedArabEmirates(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.AE()

    def test_2020(self):
        self.assertIn(date(2020, 1, 1), self.holidays)
        self.assertIn(date(2020, 12, 1), self.holidays)
        self.assertIn(date(2020, 12, 2), self.holidays)
        self.assertIn(date(2020, 12, 3), self.holidays)

    def test_commemoration_day_since_2015(self):
        # Before 2009 Jan 25th wasn't celebrated
        self.holidays = holidays.AE(years=[2015])
        self.assertIn(date(2015, 11, 30), self.holidays)

    def test_hijri_based(self):
        if sys.version_info >= (3, 6):
            import importlib.util

            if importlib.util.find_spec("hijri_converter"):
                self.holidays = holidays.AE(years=[2020])
                # Eid Al-Fitr
                self.assertIn(date(2020, 5, 24), self.holidays)
                self.assertIn(date(2020, 5, 25), self.holidays)
                self.assertIn(date(2020, 5, 26), self.holidays)
                # Arafat Day & Eid Al-Adha
                self.assertIn(date(2020, 7, 30), self.holidays)
                self.assertIn(date(2020, 7, 31), self.holidays)
                self.assertIn(date(2020, 8, 1), self.holidays)
                self.assertIn(date(2020, 8, 2), self.holidays)
                # Islamic New Year
                self.assertIn(date(2020, 8, 23), self.holidays)
                # Leilat Al-Miraj 2018
                self.assertIn(date(2018, 4, 13), self.holidays)
                # Prophet's Birthday 2018
                self.assertIn(date(2018, 11, 19), self.holidays)
