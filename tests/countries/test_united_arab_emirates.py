#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import importlib.util
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
        self.holidays = holidays.AE(years=[2014])
        self.assertNotIn(date(2014, 11, 30), self.holidays)

        self.holidays = holidays.AE(years=[2015])
        self.assertIn(date(2015, 11, 30), self.holidays)

        # Since 2019, Commemoration Day celebrated on Dec 1
        self.holidays = holidays.AE(years=[2019])
        self.assertNotIn(date(2019, 11, 30), self.holidays)
        self.assertIn(date(2019, 12, 1), self.holidays)

    def test_hijri_based(self):
        if importlib.util.find_spec("hijri_converter"):
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
            self.assertIn(date(2008, 1, 10), self.holidays)
            self.assertIn(date(2008, 12, 29), self.holidays)
            self.assertIn(date(2020, 8, 23), self.holidays)
            # Leilat Al-Miraj 2018
            self.assertIn(date(2018, 4, 13), self.holidays)
            # Prophet's Birthday 2018
            self.assertIn(date(2018, 11, 19), self.holidays)
