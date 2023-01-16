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


class TestMT(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.MT()

    def test_2022(self):
        # https://www.gov.mt/en/About%20Malta/Pages/Public%20Holidays.aspx
        self.assertIn(date(2022, 1, 1), self.holidays)
        self.assertIn(date(2022, 2, 10), self.holidays)
        self.assertIn(date(2022, 3, 19), self.holidays)
        self.assertIn(date(2022, 3, 31), self.holidays)
        self.assertIn(date(2022, 4, 15), self.holidays)
        self.assertIn(date(2022, 5, 1), self.holidays)
        self.assertIn(date(2022, 6, 7), self.holidays)
        self.assertIn(date(2022, 6, 29), self.holidays)
        self.assertIn(date(2022, 8, 15), self.holidays)
        self.assertIn(date(2022, 9, 8), self.holidays)
        self.assertIn(date(2022, 9, 21), self.holidays)
        self.assertIn(date(2022, 12, 8), self.holidays)
        self.assertIn(date(2022, 12, 13), self.holidays)
        self.assertIn(date(2022, 12, 25), self.holidays)

        self.assertNotIn(date(2022, 11, 12), self.holidays)
