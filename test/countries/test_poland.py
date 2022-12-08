#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date

import holidays


class TestPL(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.PL()

    def test_1910(self):
        self.assertNotIn(date(1910, 5, 1), self.holidays)
        self.assertNotIn(date(1910, 5, 3), self.holidays)
        self.assertNotIn(date(1910, 11, 11), self.holidays)

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

    def test_special_holidays(self):
        self.assertIn(date(2018, 11, 12), self.holidays)

    def test_swieto_trzech_kroli(self):
        self.holidays = holidays.Poland(years=[2011])
        self.assertEqual(
            self.holidays[date(2011, 1, 6)], "Święto Trzech Króli"
        )
        self.holidays = holidays.Poland(years=[2010])
        self.assertNotIn(date(2010, 1, 6), self.holidays)

    def test_swieto_panstwowe(self):
        self.holidays = holidays.Poland(years=[1950])
        self.assertEqual(self.holidays[date(1950, 5, 1)], "Święto Państwowe")
        self.holidays = holidays.Poland(years=[1949])
        self.assertNotIn(date(1949, 5, 1), self.holidays)

    def test_swieto_narodowe_trzeciego_maja(self):
        self.holidays = holidays.Poland(years=[1919])
        self.assertEqual(
            self.holidays[date(1919, 5, 3)], "Święto Narodowe Trzeciego Maja"
        )
        self.holidays = holidays.Poland(years=[1918])
        self.assertNotIn(date(1918, 5, 3), self.holidays)

    def test_i18n_en(self):
        pl_en = holidays.Poland(language="en")

        self.assertEqual(
            pl_en["2018-11-12"],
            "National Independence Day - 100th anniversary",
        )
        self.assertEqual(pl_en["2022-12-25"], "Christmas (Day 1)")
        self.assertEqual(pl_en["2022-12-26"], "Christmas (Day 2)")
