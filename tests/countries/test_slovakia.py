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

import unittest
import warnings

from datetime import date

import holidays


class TestSK(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.SK()

    def test_2018(self):
        # https://www.officeholidays.com/countries/slovakia/2018.php
        self.assertIn(date(2018, 1, 1), self.holidays)
        self.assertIn(date(2018, 1, 6), self.holidays)
        self.assertIn(date(2018, 3, 30), self.holidays)
        self.assertIn(date(2018, 5, 1), self.holidays)
        self.assertIn(date(2018, 5, 8), self.holidays)
        self.assertIn(date(2018, 4, 2), self.holidays)
        self.assertIn(date(2018, 7, 5), self.holidays)
        self.assertIn(date(2018, 8, 29), self.holidays)
        self.assertIn(date(2018, 9, 1), self.holidays)
        self.assertIn(date(2018, 9, 15), self.holidays)
        self.assertIn(date(2018, 10, 30), self.holidays)
        self.assertIn(date(2018, 11, 1), self.holidays)
        self.assertIn(date(2018, 11, 17), self.holidays)
        self.assertIn(date(2018, 12, 24), self.holidays)
        self.assertIn(date(2018, 12, 25), self.holidays)
        self.assertIn(date(2018, 12, 26), self.holidays)

    def test_slovak_deprecated(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            slovakia = holidays.Slovak()
            self.assertIsInstance(slovakia, holidays.Slovakia)
            self.assertEqual(1, len(w))
            self.assertTrue(issubclass(w[-1].category, DeprecationWarning))
