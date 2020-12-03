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


class TestKorea(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.KR()

    def test_common(self):
        holidaysNoObserved = holidays.KR(observed=False)
        self.assertEqual(holidaysNoObserved[date(2019, 1, 1)], "New Year's Day")

        self.assertNotIn(date(1582, 10, 2), self.holidays)
        self.assertNotIn(date(1582, 11, 14), self.holidays)

    def test_first_day_of_january(self):
        for year in range(2006, 2021):
            self.assertIn(self.holidays[date(year, 1, 1)], "New Year's Day")

    def test_lunar_new_year(self):
        for year, month, day in [
            (2006, 1, 28),
            (2007, 2, 17),
            (2010, 2, 13),
            (2014, 1, 30),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The day preceding of Lunar New Year's Day",
            )

        for year, month, day in [
            (1916, 2, 4),
            (1944, 1, 26),
            (1954, 2, 4),
            (1958, 2, 19),
            (1966, 1, 22),
            (1988, 2, 18),
            (1997, 2, 8),
            (2008, 2, 7),
            (2009, 1, 26),
            (2011, 2, 3),
            (2012, 1, 23),
            (2014, 1, 31),
            (2015, 2, 19),
            (2016, 2, 8),
            (2017, 1, 28),
            (2018, 2, 16),
            (2019, 2, 5),
            (2020, 1, 25),
            (2027, 2, 7),
            (2028, 1, 27),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)], "Lunar New Year's Day"
            )

        for year, month, day in [
            (2006, 1, 30),
            (2007, 2, 19),
            (2008, 2, 8),
            (2009, 1, 27),
            (2010, 2, 15),
            (2011, 2, 4),
            (2012, 1, 24),
            (2013, 2, 11),
            (2014, 2, 1),
            (2015, 2, 20),
            (2016, 2, 9),
            (2018, 2, 17),
            (2019, 2, 6),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The second day of Lunar New Year's Day",
            )

        for year, month, day in [(2016, 2, 10), (2017, 1, 30), (2020, 1, 27)]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "Alternative holiday of Lunar New Year's Day",
            )

        self.assertNotIn(date(2015, 2, 21), self.holidays)
        self.assertNotIn(date(2015, 2, 7), self.holidays)

    def test_independence_movement_day(self):
        for year, month, day in [
            (2006, 3, 1),
            (2007, 3, 1),
            (2008, 3, 1),
            (2009, 3, 1),
            (2010, 3, 1),
            (2011, 3, 1),
            (2012, 3, 1),
            (2013, 3, 1),
            (2014, 3, 1),
            (2016, 3, 1),
            (2017, 3, 1),
            (2018, 3, 1),
            (2019, 3, 1),
            (2020, 3, 1),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)], "Independence Movement Day"
            )

    def test_tree_planting_day(self):
        for year, month, day in [
            (1949, 4, 5),
            (1962, 4, 5),
            (1982, 4, 5),
            (1990, 4, 5),
            (1995, 4, 5),
            (1998, 4, 5),
            (2000, 4, 5),
            (2007, 4, 5),
        ]:
            self.assertEqual(self.holidays[date(year, month, day)], "Tree Planting Day")

    def test_childrens_day(self):
        for year, month, day in [
            (2015, 5, 5),
            (2016, 5, 5),
            (2017, 5, 5),
            (2018, 5, 5),
        ]:
            self.assertEqual(self.holidays[date(year, month, day)], "Children's Day")

        for year, month, day in [(2018, 5, 7), (2019, 5, 6)]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "Alternative holiday of Children's Day",
            )
        for year, month, day in [(2025, 5, 6), (2044, 5, 6)]:
            self.assertIn(
                "Alternative holiday of Children's Day",
                self.holidays[date(year, month, day)],
            )

    def test_birthday_of_buddha(self):
        name = "Birthday of the Buddha"
        for year, month, day in [
            (1931, 5, 25),
            (1968, 5, 5),
            (2010, 5, 21),
            (2011, 5, 10),
            (2012, 5, 28),
            (2013, 5, 17),
            (2014, 5, 6),
            (2015, 5, 25),
            (2016, 5, 14),
            (2017, 5, 3),
            (2018, 5, 22),
            (2019, 5, 12),
            (2020, 4, 30),
            (2021, 5, 19),
            (2022, 5, 8),
            (2023, 5, 27),
            (2024, 5, 15),
            (2026, 5, 24),
            (2027, 5, 13),
            (2028, 5, 2),
            (2029, 5, 20),
            (2030, 5, 9),
        ]:
            self.assertEqual(self.holidays[date(year, month, day)], name)

        for year, month, day in [(2001, 5, 1)]:
            self.assertIn(
                "Birthday of the Buddha", self.holidays[date(year, month, day)]
            )

    def test_labour_day(self):
        for year in [
            2006,
            2007,
            2008,
            2009,
            2010,
            2012,
            2013,
            2014,
            2015,
            2017,
            2018,
            2019,
            2020,
        ]:
            self.assertEqual(self.holidays[date(year, 5, 1)], "Labour Day")

    def test_memorial_day(self):
        for year in [
            2006,
            2007,
            2008,
            2009,
            2010,
            2012,
            2013,
            2014,
            2015,
            2017,
            2018,
            2019,
            2020,
        ]:
            self.assertEqual(self.holidays[date(year, 6, 6)], "Memorial Day")

    def test_constitution_day(self):
        for year in range(1948, 2007):
            self.assertEqual(self.holidays[date(year, 7, 17)], "Constitution Day")
        self.assertNotIn(date(2008, 7, 17), self.holidays)
        self.assertNotIn(date(1947, 7, 17), self.holidays)

    def test_liberation_day(self):
        for year in range(1945, 2020):
            self.assertEqual(self.holidays[date(year, 8, 15)], "Liberation Day")

    def test_chuseok(self):
        for year, month, day in [
            (2010, 9, 21),
            (2011, 9, 11),
            (2012, 9, 29),
            (2013, 9, 18),
            (2014, 9, 7),
            (2015, 9, 26),
            (2016, 9, 14),
            (2018, 9, 23),
            (2019, 9, 12),
            (2020, 9, 30),
            (2021, 9, 20),
            (2022, 9, 9),
            (2023, 9, 28),
            (2024, 9, 16),
            (2025, 10, 5),
            (2026, 9, 24),
            (2027, 9, 14),
            (2028, 10, 2),
            (2029, 9, 21),
            (2030, 9, 11),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)], "The day preceding of Chuseok"
            )

        for year, month, day in [(2017, 10, 3)]:
            self.assertIn(
                "The day preceding of Chuseok", self.holidays[date(year, month, day)]
            )

        for year, month, day in [
            (1942, 9, 25),
            (1978, 9, 17),
            (2010, 9, 22),
            (2011, 9, 12),
            (2012, 9, 30),
            (2013, 9, 19),
            (2014, 9, 8),
            (2015, 9, 27),
            (2016, 9, 15),
            (2017, 10, 4),
            (2018, 9, 24),
            (2019, 9, 13),
            (2020, 10, 1),
            (2021, 9, 21),
            (2022, 9, 10),
            (2023, 9, 29),
            (2024, 9, 17),
            (2025, 10, 6),
            (2026, 9, 25),
            (2027, 9, 15),
            (2029, 9, 22),
            (2030, 9, 12),
            (2040, 9, 21),
        ]:
            self.assertEqual(self.holidays[date(year, month, day)], "Chuseok")

        for year, month, day in [(2028, 10, 3)]:
            self.assertIn("Chuseok", self.holidays[date(year, month, day)])

        for year, month, day in [
            (2010, 9, 23),
            (2011, 9, 13),
            (2012, 10, 1),
            (2013, 9, 20),
            (2014, 9, 9),
            (2015, 9, 28),
            (2016, 9, 16),
            (2017, 10, 5),
            (2018, 9, 25),
            (2019, 9, 14),
            (2020, 10, 2),
            (2021, 9, 22),
            (2022, 9, 11),
            (2023, 9, 30),
            (2024, 9, 18),
            (2025, 10, 7),
            (2026, 9, 26),
            (2027, 9, 16),
            (2028, 10, 4),
            (2029, 9, 23),
            (2030, 9, 13),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)], "The second day of Chuseok"
            )

        for year, month, day in [
            (2014, 9, 10),
            (2015, 9, 29),
            (2018, 9, 26),
            (2022, 9, 12),
            (2025, 10, 8),
            (2029, 9, 24),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)], "Alternative holiday of Chuseok"
            )

    def test_national_foundation_day(self):
        for year in range(1948, 2050):
            if year in [1952, 1963, 1971, 1990, 2009, 2017, 2028, 2036, 2039, 2047]:
                self.assertIn(
                    "National Foundation Day", self.holidays[date(year, 10, 3)]
                )
            else:
                self.assertEqual(
                    self.holidays[date(year, 10, 3)], "National Foundation Day"
                )

    def test_hangeul_day(self):
        for year in range(1948, 2007):
            self.assertEqual(self.holidays[date(year, 10, 9)], "Hangeul Day")

    def test_christmas_day(self):
        for year in range(1948, 2050):
            self.assertEqual(self.holidays[date(year, 12, 25)], "Christmas Day")

    def test_years_range(self):
        self.holidays = holidays.KR(years=range(2006, 2021))
        for year in range(2006, 2021):
            self.assertIn(self.holidays[date(year, 1, 1)], "New Year's Day")
