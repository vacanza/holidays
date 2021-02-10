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


class TestJapan(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Japan(observed=False)

    def test_new_years_day(self):
        self.assertIn(date(1949, 1, 1), self.holidays)
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2050, 1, 1), self.holidays)

    def test_coming_of_age(self):
        self.assertIn(date(1999, 1, 15), self.holidays)
        self.assertIn(date(2000, 1, 10), self.holidays)
        self.assertIn(date(2017, 1, 9), self.holidays)
        self.assertIn(date(2030, 1, 14), self.holidays)
        self.assertIn(date(2050, 1, 10), self.holidays)

        self.assertNotIn(date(2000, 1, 15), self.holidays)
        self.assertNotIn(date(2017, 1, 15), self.holidays)
        self.assertNotIn(date(2030, 1, 15), self.holidays)

    def test_foundation_day(self):
        self.assertIn(date(1949, 2, 11), self.holidays)
        self.assertIn(date(2017, 2, 11), self.holidays)
        self.assertIn(date(2050, 2, 11), self.holidays)

    def test_vernal_equinox_day(self):
        self.assertIn(date(1956, 3, 21), self.holidays)
        self.assertIn(date(1960, 3, 20), self.holidays)
        self.assertIn(date(1970, 3, 21), self.holidays)
        self.assertIn(date(1980, 3, 20), self.holidays)
        self.assertIn(date(1990, 3, 21), self.holidays)
        self.assertIn(date(2000, 3, 20), self.holidays)
        self.assertIn(date(2010, 3, 21), self.holidays)
        self.assertIn(date(2017, 3, 20), self.holidays)
        self.assertIn(date(2020, 3, 20), self.holidays)
        self.assertIn(date(2030, 3, 20), self.holidays)
        self.assertIn(date(2040, 3, 20), self.holidays)
        self.assertIn(date(2092, 3, 19), self.holidays)

    def test_showa_day(self):
        self.assertIn(date(1950, 4, 29), self.holidays)
        self.assertIn(date(1990, 4, 29), self.holidays)
        self.assertIn(date(2010, 4, 29), self.holidays)

    def test_constitution_memorial_day(self):
        self.assertIn(date(1950, 5, 3), self.holidays)
        self.assertIn(date(2000, 5, 3), self.holidays)
        self.assertIn(date(2050, 5, 3), self.holidays)

    def test_greenery_day(self):
        self.assertNotIn(date(1950, 5, 4), self.holidays)
        self.assertIn(date(2007, 5, 4), self.holidays)
        self.assertIn(date(2050, 5, 4), self.holidays)

    def test_childrens_day(self):
        self.assertIn(date(1950, 5, 5), self.holidays)
        self.assertIn(date(2000, 5, 5), self.holidays)
        self.assertIn(date(2050, 5, 5), self.holidays)

    def test_marine_day(self):
        self.assertNotIn(date(1950, 7, 20), self.holidays)
        self.assertIn(date(2000, 7, 20), self.holidays)
        self.assertIn(date(2003, 7, 21), self.holidays)
        self.assertIn(date(2017, 7, 17), self.holidays)
        self.assertIn(date(2020, 7, 23), self.holidays)
        self.assertIn(date(2021, 7, 22), self.holidays)
        self.assertIn(date(2050, 7, 18), self.holidays)

    def test_mountain_day(self):
        self.assertNotIn(date(1950, 8, 11), self.holidays)
        self.assertNotIn(date(2015, 8, 11), self.holidays)
        self.assertIn(date(2016, 8, 11), self.holidays)
        self.assertIn(date(2017, 8, 11), self.holidays)
        self.assertIn(date(2020, 8, 10), self.holidays)
        self.assertIn(date(2021, 8, 8), self.holidays)
        self.assertIn(date(2050, 8, 11), self.holidays)

    def test_respect_for_the_aged_day(self):
        self.assertNotIn(date(1965, 9, 15), self.holidays)
        self.assertIn(date(1966, 9, 15), self.holidays)
        self.assertIn(date(2002, 9, 15), self.holidays)
        self.assertIn(date(2003, 9, 15), self.holidays)
        self.assertNotIn(date(2004, 9, 15), self.holidays)
        self.assertIn(date(2004, 9, 20), self.holidays)
        self.assertIn(date(2017, 9, 18), self.holidays)
        self.assertIn(date(2050, 9, 19), self.holidays)

    def test_autumnal_equinox_day(self):
        self.assertIn(date(2000, 9, 23), self.holidays)
        self.assertIn(date(2010, 9, 23), self.holidays)
        self.assertIn(date(2017, 9, 23), self.holidays)
        self.assertIn(date(2020, 9, 22), self.holidays)
        self.assertIn(date(2030, 9, 23), self.holidays)
        self.assertIn(date(1979, 9, 24), self.holidays)
        self.assertIn(date(2032, 9, 21), self.holidays)

    def test_health_and_sports_day(self):
        self.assertNotIn(date(1965, 10, 10), self.holidays)
        self.assertIn(date(1966, 10, 10), self.holidays)
        self.assertIn(date(1999, 10, 10), self.holidays)
        self.assertNotIn(date(2000, 10, 10), self.holidays)
        self.assertIn(date(2000, 10, 9), self.holidays)
        self.assertIn(date(2017, 10, 9), self.holidays)
        self.assertIn(date(2020, 7, 24), self.holidays)
        self.assertIn(date(2021, 7, 23), self.holidays)
        self.assertIn(date(2050, 10, 10), self.holidays)

    def test_culture_day(self):
        self.assertIn(date(1950, 11, 3), self.holidays)
        self.assertIn(date(2000, 11, 3), self.holidays)
        self.assertIn(date(2050, 11, 3), self.holidays)

    def test_labour_thanks_giving_day(self):
        self.assertIn(date(1950, 11, 23), self.holidays)
        self.assertIn(date(2000, 11, 23), self.holidays)
        self.assertIn(date(2050, 11, 23), self.holidays)

    def test_emperors_birthday(self):
        self.assertIn(date(1989, 12, 23), self.holidays)
        self.assertIn(date(2017, 12, 23), self.holidays)
        self.assertNotIn(date(2019, 12, 23), self.holidays)
        self.assertIn(date(2020, 2, 23), self.holidays)

    def test_reiwa_emperor_holidays(self):
        self.assertIn(date(1993, 6, 9), self.holidays)
        self.assertIn(date(2019, 4, 30), self.holidays)
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 5, 2), self.holidays)
        self.assertIn(date(2019, 10, 22), self.holidays)

    def test_invalid_years(self):
        self.assertRaises(
            NotImplementedError, lambda: date(1948, 1, 1) in self.holidays
        )
        self.assertRaises(
            NotImplementedError, lambda: date(2100, 1, 1) in self.holidays
        )
