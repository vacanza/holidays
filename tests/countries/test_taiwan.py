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


class TestTaiwan(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.TW()

    def test1911(self):
        # No Holidays before 1911
        self.assertEqual(0, len(holidays.TW(years=[1910])))

    def test1946(self):
        self.assertNotIn(date(1946, 2, 28), self.holidays)  # NO Peace Memorial Day

    def test2021(self):
        self.assertIn(date(2021, 1, 1), self.holidays)  # Founding of the Republic of China
        self.assertIn(date(2021, 2, 11), self.holidays)  # Chinese New Year's Eve
        self.assertIn(date(2021, 2, 12), self.holidays)  # Spring Festival
        self.assertIn(date(2021, 2, 13), self.holidays)  # Spring Festival
        self.assertIn(date(2021, 2, 14), self.holidays)  # Spring Festival
        self.assertIn(date(2021, 2, 15), self.holidays)  # Spring Festival
        self.assertIn(date(2021, 2, 16), self.holidays)  # Spring Festival
        self.assertIn(date(2021, 2, 28), self.holidays)  # Peace Memorial Day
        self.assertIn(date(2021, 4, 4), self.holidays)  # Children's Day
        self.assertIn(date(2021, 6, 14), self.holidays)  # Dragon Boat Festival
        self.assertIn(date(2021, 9, 21), self.holidays)  # Mid-Autumn Festival
        self.assertIn(date(2021, 10, 10), self.holidays)  # National Day day 1
        self.assertIn(date(2021, 10, 11), self.holidays)  # National Day day 2
