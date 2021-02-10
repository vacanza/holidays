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


class TestFinland(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.FI()

    def test_fixed_holidays(self):
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertEqual(self.holidays[date(2017, 1, 1)], "Uudenvuodenpäivä")

        self.assertIn(date(2017, 1, 6), self.holidays)
        self.assertEqual(self.holidays[date(2017, 1, 6)], "Loppiainen")

        self.assertIn(date(2017, 5, 1), self.holidays)
        self.assertEqual(self.holidays[date(2017, 5, 1)], "Vappu")

        self.assertIn(date(2017, 12, 6), self.holidays)
        self.assertEqual(self.holidays[date(2017, 12, 6)], "Itsenäisyyspäivä")

        self.assertIn(date(2017, 12, 25), self.holidays)
        self.assertEqual(self.holidays[date(2017, 12, 25)], "Joulupäivä")

        self.assertIn(date(2017, 12, 26), self.holidays)
        self.assertEqual(self.holidays[date(2017, 12, 26)], "Tapaninpäivä")

    def test_relative_holidays(self):
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertEqual(self.holidays[date(2017, 4, 14)], "Pitkäperjantai")

        self.assertIn(date(2017, 4, 16), self.holidays)
        self.assertEqual(self.holidays[date(2017, 4, 16)], "Pääsiäispäivä")

        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertEqual(self.holidays[date(2017, 4, 17)], "2. pääsiäispäivä")

        self.assertIn(date(2017, 5, 25), self.holidays)
        self.assertEqual(self.holidays[date(2017, 5, 25)], "Helatorstai")

        self.assertIn(date(2017, 11, 4), self.holidays)
        self.assertEqual(self.holidays[date(2017, 11, 4)], "Pyhäinpäivä")

    def test_Juhannus(self):
        self.assertIn(date(2017, 6, 24), self.holidays)
        self.assertNotIn(date(2017, 6, 20), self.holidays)
        self.assertIn(date(2020, 6, 20), self.holidays)
        self.assertIn(date(2021, 6, 26), self.holidays)
        self.assertIn(date(2018, 6, 22), self.holidays)
        self.assertEqual(self.holidays[date(2018, 6, 22)], "Juhannusaatto")
        self.assertEqual(self.holidays[date(2018, 6, 23)], "Juhannuspäivä")
