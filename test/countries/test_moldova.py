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


class TestMoldova(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.MD()

    def test_2022(self):
        # https://en.wikipedia.org/wiki/Public_holidays_in_Moldova
        self.assertIn(date(2022, 1, 1), self.holidays)
        self.assertIn(date(2022, 1, 7), self.holidays)
        self.assertIn(date(2022, 1, 8), self.holidays)
        self.assertIn(date(2022, 3, 8), self.holidays)
        self.assertIn(date(2022, 4, 24), self.holidays)
        self.assertIn(date(2022, 4, 25), self.holidays)
        self.assertIn(date(2022, 5, 1), self.holidays)
        self.assertIn(date(2022, 5, 3), self.holidays)
        self.assertIn(date(2022, 5, 9), self.holidays)
        self.assertIn(date(2022, 6, 1), self.holidays)
        self.assertIn(date(2022, 8, 27), self.holidays)
        self.assertIn(date(2022, 8, 31), self.holidays)
        self.assertIn(date(2022, 10, 8), self.holidays)
        self.assertIn(date(2022, 12, 25), self.holidays)
