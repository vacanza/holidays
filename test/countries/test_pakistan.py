# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest

from datetime import date

import holidays


class TestPakistan(unittest.TestCase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_Pakistan
    def setUp(self):
        self.holidays = holidays.PK()

    def test_holidays(self):
        # National holidays
        self.assertIn(
            date(2020, 2, 5), self.holidays
        )  # Kashmir Solidarity Day
        self.assertIn(date(2020, 3, 23), self.holidays)  # Pakistan Day
        self.assertIn(date(2020, 5, 1), self.holidays)  # Labour Day
        self.assertIn(date(2020, 8, 14), self.holidays)  # Independence Day
        self.assertIn(date(2020, 12, 25), self.holidays)  # Quaid-e-Azam Day
        # Religious holidays
        self.assertIn(date(2020, 7, 31), self.holidays)  # Eid-ul-Adha
        self.assertIn(date(2020, 8, 1), self.holidays)  # Eid-ul-Adha
        self.assertIn(date(2020, 8, 2), self.holidays)  # Eid-ul-Adha
        self.assertIn(date(2020, 5, 24), self.holidays)  # Eid-ul-Fitr
        self.assertIn(date(2020, 5, 25), self.holidays)  # Eid-ul-Fitr
        self.assertIn(date(2020, 5, 26), self.holidays)  # Eid-ul-Fitr
        self.assertIn(date(2020, 10, 29), self.holidays)  # Mawlid
        self.assertIn(date(2020, 8, 29), self.holidays)  # Ashura
        self.assertIn(date(2020, 8, 30), self.holidays)  # Ashura
