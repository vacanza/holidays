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

from datetime import date

import holidays


class TestBelarus(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.BY()

    def test_2018(self):
        # http://calendar.by/procal.php?year=2018
        # https://www.officeholidays.com/countries/belarus/index.php
        self.assertIn(date(2018, 1, 1), self.holidays)
        self.assertIn(date(2018, 1, 7), self.holidays)
        self.assertIn(date(2018, 3, 8), self.holidays)
        self.assertIn(date(2018, 4, 17), self.holidays)
        self.assertIn(date(2018, 5, 1), self.holidays)
        self.assertIn(date(2018, 5, 9), self.holidays)
        self.assertIn(date(2018, 7, 3), self.holidays)
        self.assertIn(date(2018, 11, 7), self.holidays)
        self.assertIn(date(2018, 12, 25), self.holidays)

    def test_new_year(self):
        self.assertIn(date(2019, 1, 1), self.holidays)
        self.assertNotIn(date(2019, 1, 2), self.holidays)
        self.assertIn(date(2020, 1, 1), self.holidays)
        self.assertIn(date(2020, 1, 2), self.holidays)
        self.assertIn(date(2021, 1, 1), self.holidays)
        self.assertIn(date(2021, 1, 2), self.holidays)

    def test_radunitsa(self):
        # http://calendar.by/content.php?id=20
        self.assertIn(date(2012, 4, 24), self.holidays)
        self.assertIn(date(2013, 5, 14), self.holidays)
        self.assertIn(date(2014, 4, 29), self.holidays)
        self.assertIn(date(2015, 4, 21), self.holidays)
        self.assertIn(date(2016, 5, 10), self.holidays)
        self.assertIn(date(2017, 4, 25), self.holidays)
        self.assertIn(date(2018, 4, 17), self.holidays)
        self.assertIn(date(2019, 5, 7), self.holidays)
        self.assertIn(date(2020, 4, 28), self.holidays)
        self.assertIn(date(2021, 5, 11), self.holidays)
        self.assertIn(date(2022, 5, 3), self.holidays)
        self.assertIn(date(2023, 4, 25), self.holidays)
        self.assertIn(date(2024, 5, 14), self.holidays)
        self.assertIn(date(2025, 4, 29), self.holidays)
        self.assertIn(date(2026, 4, 21), self.holidays)
        self.assertIn(date(2027, 5, 11), self.holidays)
        self.assertIn(date(2028, 4, 25), self.holidays)
        self.assertIn(date(2029, 4, 17), self.holidays)
        self.assertIn(date(2030, 5, 7), self.holidays)

    def test_before_1998(self):
        self.assertNotIn(date(1997, 7, 3), self.holidays)
