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


class TestIndonesia(unittest.TestCase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_Indonesia
    def setUp(self):
        self.holidays = holidays.ID()

    def test_holidays(self):
        self.assertIn(date(2020, 1, 1), self.holidays)  # New Year's Day
        self.assertIn(date(2020, 1, 25), self.holidays)  # Chinese New Year
        self.assertIn(date(2020, 3, 22), self.holidays)  # Ascension of the Prophet
        self.assertIn(date(2020, 3, 25), self.holidays)  # Day of Silence
        self.assertIn(date(2020, 4, 10), self.holidays)  # Good Friday
        self.assertIn(date(2020, 5, 7), self.holidays)  # Buddha's Birthday (differs in Indonesia and China)
        self.assertIn(date(2020, 5, 1), self.holidays) 	# Labour Day
        self.assertIn(date(2020, 5, 21), self.holidays)  # Ascension Day
        self.assertIn(date(2020, 6, 1), self.holidays)  # Pancasila Day
        self.assertIn(date(2020, 5, 24), self.holidays)  # Eid al-Fitr day 1
        self.assertIn(date(2020, 5, 25), self.holidays)  # Eid al-Fitr day 2
        self.assertIn(date(2020, 7, 31), self.holidays)  # Eid al-Adha
        self.assertIn(date(2020, 8, 17), self.holidays)  # Independence Day
        self.assertIn(date(2020, 8, 20), self.holidays)  # Islamic New Year
        self.assertIn(date(2020, 10, 29), self.holidays)  # Birthday of the Prophet
        self.assertIn(date(2020, 12, 25), self.holidays)  # Christmas Day
