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
from datetime import date, datetime

import holidays


class TestEstonia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.EE()
        self.cur_date = datetime.now()

    def test_new_years(self):
        test_date = date(self.cur_date.year, 1, 1)
        self.assertEqual(self.holidays.get(test_date), "uusaasta")
        self.assertIn(test_date, self.holidays)

    def test_independence_day(self):
        test_date = date(self.cur_date.year, 2, 24)
        self.assertEqual(self.holidays.get(test_date), "iseseisvuspäev")
        self.assertIn(test_date, self.holidays)

    def test_good_friday(self):
        test_date = date(2019, 4, 19)
        self.assertEqual(self.holidays.get(test_date), "suur reede")
        self.assertIn(test_date, self.holidays)

    def test_easter_sunday(self):
        test_date = date(2019, 4, 21)
        self.assertEqual(
            self.holidays.get(test_date), "ülestõusmispühade 1. püha"
        )
        self.assertIn(test_date, self.holidays)

    def test_spring_day(self):
        test_date = date(self.cur_date.year, 5, 1)
        self.assertEqual(self.holidays.get(test_date), "kevadpüha")
        self.assertIn(test_date, self.holidays)

    def test_pentecost(self):
        test_date = date(2019, 6, 9)
        self.assertEqual(self.holidays.get(test_date), "nelipühade 1. püha")
        self.assertIn(test_date, self.holidays)

    def test_victory_day(self):
        test_date = date(self.cur_date.year, 6, 23)
        self.assertEqual(self.holidays.get(test_date), "võidupüha")
        self.assertIn(test_date, self.holidays)

    def test_midsummers_day(self):
        test_date = date(self.cur_date.year, 6, 24)
        self.assertEqual(self.holidays.get(test_date), "jaanipäev")
        self.assertIn(test_date, self.holidays)

    def test_restoration_of_independence_day(self):
        test_date = date(self.cur_date.year, 8, 20)
        self.assertEqual(self.holidays.get(test_date), "taasiseseisvumispäev")
        self.assertIn(test_date, self.holidays)

    def test_christmas_eve(self):
        test_date = date(self.cur_date.year, 12, 24)
        self.assertEqual(self.holidays.get(test_date), "jõululaupäev")
        self.assertIn(test_date, self.holidays)

    def test_christmas_day(self):
        test_date = date(self.cur_date.year, 12, 25)
        self.assertEqual(self.holidays.get(test_date), "esimene jõulupüha")
        self.assertIn(test_date, self.holidays)

    def test_boxing_day(self):
        test_date = date(self.cur_date.year, 12, 26)
        self.assertEqual(self.holidays.get(test_date), "teine jõulupüha")
        self.assertIn(test_date, self.holidays)
