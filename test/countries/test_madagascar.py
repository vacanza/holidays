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

import unittest
from datetime import date

import holidays


class TestMadagascar(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.MG()

    def test_new_years(self):
        self.assertIn(date(2010, 1, 1), self.holidays)
        self.assertIn(date(2020, 1, 1), self.holidays)

    def test_mahery_fo(self):
        self.assertIn(date(2010, 3, 29), self.holidays)
        self.assertIn(date(2015, 3, 29), self.holidays)
        self.assertIn(date(2022, 3, 29), self.holidays)

    def test_paska(self):
        self.assertIn(date(2022, 4, 17), self.holidays)  # Andron'ny paska
        self.assertIn(date(2022, 4, 18), self.holidays)  # Alatsinain'ny Paska
        self.assertIn(date(2022, 5, 26), self.holidays)
        self.assertIn(date(2022, 6, 5), self.holidays)
        self.assertIn(date(2022, 6, 6), self.holidays)

    def test_womens_day(self):
        self.assertIn(date(2010, 3, 8), self.holidays)
        self.assertIn(date(2020, 3, 8), self.holidays)

    def test_labour_day(self):
        self.assertIn(date(2010, 5, 1), self.holidays)
        self.assertIn(date(2020, 5, 1), self.holidays)

    def test_mother_day(self):
        self.assertIn(date(2010, 5, 30), self.holidays)
        self.assertIn(date(2018, 5, 27), self.holidays)
        self.assertIn(date(2020, 6, 7), self.holidays)
        self.assertIn(date(2022, 5, 29), self.holidays)

    def test_father_day(self):
        self.assertIn(date(2010, 6, 20), self.holidays)
        self.assertIn(date(2018, 6, 17), self.holidays)
        self.assertIn(date(2020, 6, 21), self.holidays)
        self.assertIn(date(2022, 6, 19), self.holidays)

    def test_independence_day(self):
        self.assertIn(date(1960, 6, 26), self.holidays)
        self.assertIn(date(2010, 6, 26), self.holidays)
        self.assertIn(date(2020, 6, 26), self.holidays)
        self.assertNotIn(date(1959, 6, 26), self.holidays)

    def test_assumption_day(self):
        self.assertIn(date(2010, 8, 15), self.holidays)
        self.assertIn(date(2020, 8, 15), self.holidays)
        self.assertIn(date(2022, 8, 15), self.holidays)

    def test_all_saints_day(self):
        self.assertIn(date(2010, 11, 1), self.holidays)
        self.assertIn(date(2020, 11, 1), self.holidays)
        self.assertIn(date(2022, 11, 1), self.holidays)

    def test_republic_day(self):
        self.assertIn(date(2011, 12, 11), self.holidays)
        self.assertIn(date(2020, 12, 11), self.holidays)
        self.assertIn(date(2022, 12, 11), self.holidays)
        self.assertNotIn(date(2010, 12, 11), self.holidays)

    def test_christmas_day(self):
        self.assertIn(date(2010, 12, 25), self.holidays)
        self.assertIn(date(2020, 12, 25), self.holidays)
        self.assertIn(date(2022, 12, 25), self.holidays)

    def test_1946(self):
        mg_holidays = holidays.MG(years=1946)
        self.assertEqual(0, len(mg_holidays))
