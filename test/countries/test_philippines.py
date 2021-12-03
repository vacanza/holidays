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


class TestPhilippines(unittest.TestCase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_the_Philippines
    def setUp(self):
        self.holidays = holidays.PH()

    def test_holidays(self):
        self.assertIn(date(2020, 1, 1), self.holidays)  # New Year's Day

        self.assertIn(date(2020, 1, 25), self.holidays)  # Chinese New Year

        self.assertIn(date(2020, 2, 25), self.holidays)  # EDSA Revolution Anniversary
        self.assertIn(date(2020, 4, 9), self.holidays)  # Maundy Thursday
        self.assertIn(date(2020, 4, 10), self.holidays)  # Good Friday
        self.assertIn(date(2020, 4, 11), self.holidays)  # Black Saturday
        self.assertIn(date(2020, 4, 9), self.holidays)  # Day of Valor
        self.assertIn(date(2020, 5, 1), self.holidays)  # Labor Day
        self.assertIn(date(2020, 5, 24), self.holidays)  # Eid al-Fitr
        self.assertIn(date(2020, 6, 12), self.holidays)  # Independence Day
        self.assertIn(date(2020, 7, 31), self.holidays)  # Eid'l Adha
        self.assertIn(date(2020, 8, 21), self.holidays)  # Ninoy Aquino Day
        # National Heroes' Day tests in it own test
        self.assertIn(date(2020, 11, 1), self.holidays)  # All Saints' Day
        self.assertIn(date(2020, 11, 2), self.holidays)  # All Souls Day
        self.assertIn(date(2020, 11, 30), self.holidays)  # Bonifacio Day
        self.assertIn(date(2020, 12, 8), self.holidays)  # Feast of the Immaculate Conception of the Blessed Virgin Mary
        self.assertIn(date(2020, 12, 24), self.holidays)  # Christmas Eve
        self.assertIn(date(2020, 12, 25), self.holidays)  # Christmas Day
        self.assertIn(date(2020, 12, 30), self.holidays)  # Rizal Day
        self.assertIn(date(2020, 12, 31), self.holidays)  # New Year's Eve

    def test_national_heroes_day(self):
        # before 2017 last sunday of august
        self.assertIn(date(2005, 8, 28), self.holidays)  # National Heroes' Day
        self.assertIn(date(2006, 8, 27), self.holidays)  # National Heroes' Day
        # 2007 and after last monday of august
        self.assertIn(date(2007, 8, 27), self.holidays)  # National Heroes' Day
        self.assertIn(date(2020, 8, 31), self.holidays)  # National Heroes' Day
        self.assertIn(date(2021, 8, 30), self.holidays)  # National Heroes' Day
