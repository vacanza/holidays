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


class TestBurundi(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.BI()

    def test_new_year_day(self):
        for year in range(1979, 2050):
            self.assertIn("New Year's Day", self.holidays[date(year, 1, 1)])

    def test_unity_day(self):
        self.assertIn("Unity Day", self.holidays[date(2017, 2, 5)])
        self.assertIn("Unity Day (Observed)", self.holidays[date(2017, 2, 6)])

    def test_labour_day(self):
        self.assertIn("Labour Day", self.holidays[date(2017, 5, 1)])
        self.assertIn("Labour Day (Observed)", self.holidays[date(2022, 5, 2)])

    def test_rwagasore_day(self):
        self.assertIn(
            "Prince Louis Rwagasore Day", self.holidays[date(2017, 10, 13)]
        )
        self.assertIn(
            "Prince Louis Rwagasore Day (Observed)",
            self.holidays[date(2024, 10, 14)],
        )

    def test_ntaryamira_day(self):
        self.assertIn(
            "President Ntaryamira Day", self.holidays[date(2017, 4, 6)]
        )

    def test_ndadaye_day(self):
        self.assertIn(
            "President Ndadaye's Day", self.holidays[date(2017, 10, 21)]
        )
        self.assertIn(
            "President Ndadaye's Day (Observed)",
            self.holidays[date(2018, 10, 22)],
        )

    def test_independence_day(self):
        for year in range(1962, 2050):
            self.assertIn(date(year, 7, 1), self.holidays)

        for year in range(1930, 1962):
            if year != 1958:
                # in 1958 it's Eid Al Adha (as estimated by convertdate)
                self.assertNotIn(date(year, 7, 1), self.holidays)

        self.assertIn(
            "Independence Day (Observed)", self.holidays[date(2018, 7, 2)]
        )

    def test_ascension_day(self):
        self.assertIn("Ascension Day", self.holidays[date(2020, 5, 21)])

    def test_assumption_Day(self):
        self.assertIn("Assumption Day", self.holidays[date(2020, 8, 15)])

    def test_all_saints_Day(self):
        self.assertIn("All Saints' Day", self.holidays[date(2020, 11, 1)])
        self.assertIn(
            "All Saints' Day (Observed)", self.holidays[date(2020, 11, 2)]
        )

    def test_christmas_Day(self):
        self.assertIn("Christmas Day", self.holidays[date(2020, 12, 25)])

    def test_eid_al_adha(self):
        if sys.version_info >= (3, 6):
            import importlib.util

            if importlib.util.find_spec("hijri_converter"):
                self.holidays = holidays.Burundi(years=[2019, 1999])

                # eid Al Adha
                self.assertIn(date(2020, 7, 31), self.holidays)
                self.assertIn(date(2020, 7, 31), self.holidays)
