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


class TestChile(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Chile()
        self.holidays_AP = holidays.CL(state="AP")
        self.holidays_NB = holidays.CHL(state="NB")

    def test_2009(self):
        self.assertIn(date(2009, 10, 12), self.holidays)

    def test_2017(self):
        self.assertIn(date(2017, 1, 2), self.holidays)

    def test_2018(self):
        self.assertIn(date(2018, 9, 17), self.holidays)

    def test_2019(self):
        # No laborables (sector público) not included
        self.assertIn(date(2019, 1, 1), self.holidays)
        # self.assertIn(date(2019, 4, 18), self.holidays)
        self.assertIn(date(2019, 4, 19), self.holidays)
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 5, 21), self.holidays)
        self.assertIn(date(2019, 6, 29), self.holidays)
        self.assertIn(date(2019, 7, 16), self.holidays)
        self.assertIn(date(2019, 8, 15), self.holidays)
        self.assertIn(date(2019, 9, 18), self.holidays)
        self.assertIn(date(2019, 9, 19), self.holidays)
        self.assertIn(date(2019, 9, 20), self.holidays)
        self.assertIn(date(2019, 10, 12), self.holidays)
        self.assertIn(date(2019, 11, 1), self.holidays)
        self.assertIn(date(2019, 12, 8), self.holidays)
        self.assertIn(date(2019, 12, 25), self.holidays)

    def test_2020(self):
        # from https://feriados.cl/2020.htm
        self.assertIn(date(2020, 1, 1), self.holidays)
        self.assertIn(date(2020, 4, 10), self.holidays)
        self.assertIn(date(2020, 4, 11), self.holidays)
        self.assertIn(date(2020, 5, 1), self.holidays)
        self.assertIn(date(2020, 5, 21), self.holidays)
        self.assertIn(date(2020, 6, 29), self.holidays)
        self.assertIn(date(2020, 7, 16), self.holidays)
        self.assertIn(date(2020, 8, 15), self.holidays)
        self.assertIn(date(2020, 9, 18), self.holidays)
        self.assertIn(date(2020, 9, 19), self.holidays)
        self.assertIn(date(2020, 10, 12), self.holidays)
        self.assertIn(date(2020, 10, 31), self.holidays)
        self.assertIn(date(2020, 11, 1), self.holidays)
        self.assertIn(date(2020, 12, 8), self.holidays)
        self.assertIn(date(2020, 12, 25), self.holidays)
        self.assertIn(date(2020, 6, 7), self.holidays_AP)
        self.assertIn(date(2020, 8, 20), self.holidays_NB)

    def test_2021(self):
        # from https://feriados.cl/2021.htm
        self.assertIn(date(2021, 1, 1), self.holidays)
        self.assertIn(date(2021, 4, 2), self.holidays)
        self.assertIn(date(2021, 4, 3), self.holidays)
        self.assertIn(date(2021, 5, 1), self.holidays)
        self.assertIn(date(2021, 5, 21), self.holidays)
        self.assertIn(date(2021, 6, 28), self.holidays)
        self.assertIn(date(2021, 7, 16), self.holidays)
        self.assertIn(date(2021, 8, 15), self.holidays)
        self.assertIn(date(2021, 9, 18), self.holidays)
        self.assertIn(date(2021, 9, 19), self.holidays)
        self.assertIn(date(2021, 10, 11), self.holidays)
        self.assertIn(date(2021, 10, 31), self.holidays)
        self.assertIn(date(2021, 11, 1), self.holidays)
        self.assertIn(date(2021, 12, 8), self.holidays)
        self.assertIn(date(2021, 12, 25), self.holidays)
        self.assertIn(date(2021, 6, 7), self.holidays_AP)
        self.assertIn(date(2021, 8, 20), self.holidays_NB)

    def test_2024(self):
        self.assertIn(date(2024, 10, 12), self.holidays)

    def test_2029(self):
        self.assertIn(date(2029, 7, 2), self.holidays)
        self.assertIn(date(2029, 10, 15), self.holidays)
