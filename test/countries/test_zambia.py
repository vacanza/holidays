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


class TestZambia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.ZM()

    def test_new_years(self):
        self.assertIn("2015-01-01", self.holidays)
        self.assertIn("2017-01-01", self.holidays)
        self.assertIn("2999-01-01", self.holidays)
        self.assertIn("2017-01-02", self.holidays)  # sunday

    def test_good_friday(self):
        self.assertIn("2022-04-15", self.holidays)
        self.assertIn("2018-03-30", self.holidays)

    def test_easter(self):
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2020, 4, 10), self.holidays)
        self.assertIn(date(2015, 4, 6), self.holidays)

    def test_heroes_day(self):
        self.assertIn(date(1997, 7, 7), self.holidays)
        self.assertIn(date(2006, 7, 3), self.holidays)
        self.assertIn(date(2047, 7, 1), self.holidays)

    def test_unity_day(self):
        self.assertIn(date(1992, 7, 7), self.holidays)
        self.assertIn(date(2003, 7, 8), self.holidays)
        self.assertIn(date(2095, 7, 5), self.holidays)

    def test_farmers_day(self):
        self.assertIn(date(1990, 8, 6), self.holidays)
        self.assertIn(date(2021, 8, 2), self.holidays)
        self.assertIn(date(2063, 8, 6), self.holidays)

    def test_static(self):
        # African Freedom Day (on Sunday)
        self.assertIn("1969-05-26", self.holidays)
        # Youth Day
        self.assertIn("2004-03-12", self.holidays)
        # Kenneth Kaunda Day
        self.assertIn("2032-04-28", self.holidays)

    def test_not_holiday(self):
        self.assertNotIn("1958-05-26", self.holidays)
        self.assertNotIn("2016-12-28", self.holidays)
        self.assertNotIn("2015-03-02", self.holidays)
        self.assertNotIn("2017-04-28", self.holidays)

    def test_observed(self):
        self.holidays = holidays.ZM(observed=False)
        # African Freedom Day (on Sunday)
        self.assertNotIn("1969-05-26", self.holidays)

    def test_special_holidays(self):
        self.assertIn(date(2016, 8, 11), self.holidays)
        self.assertIn(date(2016, 9, 13), self.holidays)
        self.assertIn(date(2018, 3, 9), self.holidays)
        self.assertIn(date(2018, 7, 26), self.holidays)
        self.assertIn(date(2021, 7, 2), self.holidays)
        self.assertIn(date(2021, 7, 7), self.holidays)
        self.assertIn(date(2021, 8, 12), self.holidays)
        self.assertIn(date(2021, 8, 13), self.holidays)
        self.assertIn(date(2021, 8, 24), self.holidays)
        self.assertIn(date(2022, 3, 18), self.holidays)
