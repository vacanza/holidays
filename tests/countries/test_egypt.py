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


class TestEgypt(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.EG()

    def test_2019(self):
        self.assertIn(date(2019, 1, 7), self.holidays)
        self.assertIn(date(2019, 1, 25), self.holidays)
        self.assertIn(date(2019, 4, 25), self.holidays)
        self.assertIn(date(2019, 4, 28), self.holidays)
        self.assertIn(date(2019, 4, 29), self.holidays)
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 6, 30), self.holidays)
        self.assertIn(date(2019, 7, 23), self.holidays)
        self.assertIn(date(2019, 10, 6), self.holidays)

    def test_coptic_christmas(self):
        self.assertIn(date(2019, 1, 7), self.holidays)

    def test_25_jan(self):
        self.assertIn(date(2019, 1, 25), self.holidays)

    def test_labour_day(self):
        self.assertIn(date(2019, 5, 1), self.holidays)

    def test_25_jan_from_2009(self):
        # Before 2009 Jan 25th wasn't celebrated
        self.holidays = holidays.EG(years=[2010])
        self.assertIn(date(2010, 1, 25), self.holidays)

    def test_hijri_based(self):
        if sys.version_info >= (3, 6):
            import importlib.util

            if importlib.util.find_spec("hijri_converter"):
                self.holidays = holidays.EG(years=[2010])
                self.assertIn(date(2019, 6, 5), self.holidays)
                self.assertIn(date(2019, 8, 10), self.holidays)
                self.assertIn(date(2019, 8, 11), self.holidays)
                self.assertIn(date(2019, 8, 12), self.holidays)
                self.assertIn(date(2019, 8, 31), self.holidays)
                self.assertIn(date(2019, 11, 9), self.holidays)
                # eid_alfitr
                self.assertIn(date(2019, 6, 4), self.holidays)
                # eid_aladha
                self.assertIn(date(2019, 8, 11), self.holidays)
                # islamic_new_year
                self.assertIn(date(2019, 8, 31), self.holidays)
                # eid_elfetr_2010
                self.assertIn(date(2010, 9, 10), self.holidays)
                # arafat_2010
                self.assertIn(date(2010, 11, 15), self.holidays)
                # muhammad's birthday
                self.assertIn(date(2010, 2, 26), self.holidays)
