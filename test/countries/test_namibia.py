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


class TestNamibia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.NA()

    def test_out_of_range_year(self):
        self.assertNotIn(date(1970, 1, 1), self.holidays)

    def test_new_years(self):
        self.assertIn(date(1991, 1, 1), self.holidays)
        self.assertIn(date(1999, 1, 1), self.holidays)
        self.assertIn(date(2000, 1, 1), self.holidays)
        self.assertIn(date(2017, 1, 2), self.holidays)  # observed holiday

    def test_easter(self):
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 5, 25), self.holidays)
        self.assertIn(date(1994, 4, 1), self.holidays)

    def test_special_holidays(self):
        self.assertIn(date(1999, 12, 31), self.holidays)  # Y2K
        self.assertIn(date(2000, 1, 3), self.holidays)  # Y2K

    def test_namibian_women_int_rights(self):
        self.assertIn(date(2004, 9, 10), self.holidays)
        self.assertIn(
            date(2005, 9, 10), self.holidays
        )  # test namib women and int. human rights day

    def test_holidays(self):
        self.assertIn(date(2020, 5, 1), self.holidays)
        self.assertIn(date(2020, 5, 4), self.holidays)
        self.assertIn(date(2020, 5, 25), self.holidays)
        self.assertIn(date(2020, 8, 26), self.holidays)

    def test_observed(self):
        self.assertIn(date(2021, 3, 22), self.holidays)
        self.assertIn(date(2021, 12, 27), self.holidays)
        self.assertIn(date(2022, 12, 26), self.holidays)
