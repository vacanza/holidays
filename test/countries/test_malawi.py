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


class TestMalawi(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.MW()

    def test_new_years(self):
        self.assertIn("2015-01-01", self.holidays)
        self.assertIn("2017-01-01", self.holidays)
        self.assertIn("2999-01-01", self.holidays)
        self.assertIn("2017-01-02", self.holidays)  # sunday
        self.assertNotIn("2017-01-02", holidays.MW(observed=False))  # sunday

    def test_good_friday(self):
        self.assertIn("2022-04-15", self.holidays)
        self.assertIn("2018-03-30", self.holidays)

    def test_easter(self):
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2020, 4, 10), self.holidays)
        self.assertIn(date(2015, 4, 6), self.holidays)

    def test_static(self):
        self.assertIn("2004-03-03", self.holidays)

    def test_not_holiday(self):
        self.assertNotIn("2016-12-28", self.holidays)
        self.assertNotIn("2015-03-02", self.holidays)

    def test_pre_1999(self):
        self.holidays = holidays.MW(years=[1990])
        self.assertEqual(0, len(self.holidays))
