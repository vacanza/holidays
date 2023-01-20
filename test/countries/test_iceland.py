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


class TestIceland(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Iceland()
        self.cur_date = datetime.now()

    def test_new_year(self):
        test_date = date(self.cur_date.year, 1, 1)
        self.assertEqual(self.holidays.get(test_date), "Nýársdagur")
        self.assertIn(test_date, self.holidays)

    def test_maundy_thursday(self):
        test_date = date(2019, 4, 18)
        self.assertEqual(self.holidays.get(test_date), "Skírdagur")
        self.assertIn(test_date, self.holidays)

    def test_first_day_of_summer(self):
        test_date = date(2019, 4, 25)
        self.assertEqual(self.holidays.get(test_date), "Sumardagurinn fyrsti")
        self.assertIn(test_date, self.holidays)

    def test_commerce_day(self):
        test_date = date(2019, 8, 5)
        self.assertEqual(
            self.holidays.get(test_date), "Frídagur verslunarmanna"
        )
        self.assertIn(test_date, self.holidays)

    def test_holy_friday(self):
        test_date = date(2019, 4, 19)
        self.assertEqual(self.holidays.get(test_date), "Föstudagurinn langi")
        self.assertIn(test_date, self.holidays)
