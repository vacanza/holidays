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


class TestLesotho(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.LS()

    def test_out_of_range(self):
        self.assertNotIn(date(1995, 1, 1), self.holidays)
        self.assertNotIn(date(1995, 3, 11), self.holidays)

    def test_new_years(self):
        self.assertIn(date(1996, 1, 1), self.holidays)
        self.assertIn(date(2021, 1, 1), self.holidays)

    def test_easter(self):
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 5, 25), self.holidays)
        self.assertIn(date(2021, 5, 13), self.holidays)

    def test_special_holidays(self):
        self.assertIn(date(2002, 4, 4), self.holidays)
        self.assertIn(date(2002, 5, 25), self.holidays)

    def test_africa_heroes_day(self):
        self.assertIn(date(2002, 4, 4), self.holidays)
        self.assertIn(date(2002, 5, 25), self.holidays)
        self.assertIn(date(2001, 4, 4), self.holidays)
        self.assertIn(date(2003, 5, 25), self.holidays)
        self.assertIn(date(1998, 4, 4), self.holidays)
        self.assertNotIn(date(2003, 4, 4), self.holidays)
        self.assertNotIn(date(2001, 5, 25), self.holidays)
        self.assertNotIn(date(2003, 4, 4), self.holidays)

    def test_kings_birthday(self):
        self.assertIn(date(1997, 5, 2), self.holidays)
        self.assertIn(date(1996, 5, 2), self.holidays)
        self.assertIn(date(1998, 7, 17), self.holidays)

    def test_normal_days(self):
        self.assertIn(date(2001, 3, 11), self.holidays)
        self.assertIn(date(2021, 5, 1), self.holidays)
        self.assertIn(date(2018, 10, 4), self.holidays)
        self.assertIn(date(2005, 12, 25), self.holidays)
        self.assertIn(date(1997, 12, 26), self.holidays)
