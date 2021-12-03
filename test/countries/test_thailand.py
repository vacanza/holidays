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


class TestThailand(unittest.TestCase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_Thailand
    def setUp(self):
        self.holidays = holidays.TH()

    def test_holidays(self):
        self.assertIn(date(2020, 1, 1), self.holidays)  # New Year's Day
        self.assertIn(date(2020, 2, 8), self.holidays)  # Magha Puja
        self.assertIn(date(2020, 4, 6), self.holidays)  # Chakri Memorial Day
        self.assertIn(date(2020, 4, 14), self.holidays)  # Songkran Festival
        self.assertIn(date(2020, 5, 4), self.holidays)  # Coronation Day
        # Royal Ploughing Ceremony
        # Vesakb
        self.assertIn(date(2020, 6, 3), self.holidays)  # Queen Suthida's Birthday
        self.assertIn(date(2020, 7, 28), self.holidays)  # King's Birthday
        self.assertIn(date(2020, 7, 5), self.holidays)  # Asalha Puja
        self.assertIn(date(2020, 7, 6), self.holidays)  # Beginning of Vassa
        self.assertIn(date(2020, 8, 12), self.holidays)  # The Queen Mother's Birthday
        self.assertIn(date(2020, 10, 13), self.holidays)  # King Bhumibol Adulyadej Memorial Day
        self.assertIn(date(2020, 10, 23), self.holidays)  # King Chulalongkorn Day
        self.assertIn(date(2020, 12, 5), self.holidays)  # King Bhumibol Adulyadej's Birthday Anniversary
        self.assertIn(date(2020, 12, 10), self.holidays)  # Constitution Day
        self.assertIn(date(2020, 12, 31), self.holidays)  # New Year 's Eve
