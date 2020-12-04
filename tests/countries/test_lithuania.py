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


class TestLithuania(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.LT()

    def test_2018(self):
        # New Year's Day
        self.assertIn(date(2018, 1, 1), self.holidays)
        # Day of Restoration of the State of Lithuania
        self.assertIn(date(2018, 2, 16), self.holidays)
        # Day of Restoration of Independence of Lithuania
        self.assertIn(date(2018, 3, 11), self.holidays)
        # Easter
        self.assertIn(date(2018, 4, 1), self.holidays)
        # Easter 2nd day
        self.assertIn(date(2018, 4, 2), self.holidays)
        # International Workers' Day
        self.assertIn(date(2018, 5, 1), self.holidays)
        # Mother's day
        self.assertIn(date(2018, 5, 6), self.holidays)
        # Fathers's day
        self.assertIn(date(2018, 6, 3), self.holidays)
        # St. John's Day, Day of Dew
        self.assertIn(date(2018, 6, 24), self.holidays)
        # Statehood Day
        self.assertIn(date(2018, 7, 6), self.holidays)
        # Assumption Day
        self.assertIn(date(2018, 8, 15), self.holidays)
        # All Saints' Day
        self.assertIn(date(2018, 11, 1), self.holidays)
        # Christmas Eve
        self.assertIn(date(2018, 12, 24), self.holidays)
        # Christmas 1st day
        self.assertIn(date(2018, 12, 25), self.holidays)
        # Christmas 2nd day
        self.assertIn(date(2018, 12, 26), self.holidays)

    def test_easter(self):
        self.assertNotIn(date(2019, 4, 20), self.holidays)
        self.assertIn(date(2019, 4, 21), self.holidays)
        self.assertIn(date(2019, 4, 22), self.holidays)
        self.assertNotIn(date(2019, 4, 23), self.holidays)

    def test_mothers_day(self):
        self.assertNotIn(date(2019, 5, 4), self.holidays)
        self.assertIn(date(2019, 5, 5), self.holidays)
        self.assertNotIn(date(2019, 5, 6), self.holidays)
        self.assertIn(date(2020, 5, 3), self.holidays)

    def test_fathers_day(self):
        self.assertNotIn(date(2019, 6, 1), self.holidays)
        self.assertIn(date(2019, 6, 2), self.holidays)
        self.assertNotIn(date(2019, 6, 3), self.holidays)
        self.assertIn(date(2020, 6, 7), self.holidays)

    def test_day_of_dew(self):
        self.assertNotIn(date(2002, 6, 24), self.holidays)
        self.assertIn(date(2020, 6, 24), self.holidays)
