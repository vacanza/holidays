# -*- coding: utf-8 -*-

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


class TestMadagascar(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.MG()

    def test_new_years(self):
        self.assertIn(date(2010, 1, 1), self.holidays)
        self.assertIn(date(2020, 1, 1), self.holidays)

    def test_mahery_fo(self):
        self.assertIn(date(2010, 3, 29), self.holidays)
        self.assertIn(date(2015, 3, 29), self.holidays)
        self.assertIn(date(2022, 3, 29), self.holidays)



    def test_paska(self):
        self.assertIn(date(2022, 4, 17), self.holidays)  # Andron'ny paska
        self.assertIn(date(2022, 4, 18), self.holidays)  # Alatsinain'ny Paska


    def test_not_holiday(self):
        self.assertNotIn(date(2022, 4, 20), self.holidays)
