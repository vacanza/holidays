# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
import warnings

from datetime import date

import holidays


class TestPL(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.PL()

    def test_2017(self):
        # http://www.officeholidays.com/countries/poland/2017.php
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 1, 6), self.holidays)
        self.assertIn(date(2017, 4, 16), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 5, 1), self.holidays)
        self.assertIn(date(2017, 5, 3), self.holidays)
        self.assertIn(date(2017, 6, 4), self.holidays)
        self.assertIn(date(2017, 6, 15), self.holidays)
        self.assertIn(date(2017, 8, 15), self.holidays)
        self.assertIn(date(2017, 11, 1), self.holidays)
        self.assertIn(date(2017, 11, 11), self.holidays)
        self.assertIn(date(2017, 12, 25), self.holidays)
        self.assertIn(date(2017, 12, 26), self.holidays)

        self.assertNotIn(date(2017, 11, 12), self.holidays)

    def test_2018(self):
        self.assertIn(date(2018, 11, 12), self.holidays)

    def test_polish_deprecated(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            poland = holidays.Polish()
            self.assertIsInstance(poland, holidays.Poland)
            self.assertEqual(1, len(w))
            self.assertTrue(issubclass(w[-1].category, DeprecationWarning))
