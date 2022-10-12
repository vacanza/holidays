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


class TestNicaragua(unittest.TestCase):
    def setUp(self):
        self.ni_holidays = holidays.NI()

    def test_ni_holidays_2020(self):
        year = 2020
        mn_holidays = holidays.NI(subdiv="MN")

        # New Year's Day
        self.assertIn(date(year, 1, 1), self.ni_holidays)
        # Maundy Thursday
        self.assertIn(date(year, 4, 9), self.ni_holidays)
        # Good Friday
        self.assertIn(date(year, 4, 10), self.ni_holidays)
        # Labor Day
        self.assertIn(date(year, 5, 1), self.ni_holidays)
        # Revolution Day
        self.assertIn(date(year, 7, 19), self.ni_holidays)
        # Battle of San Jacinto Day
        self.assertIn(date(year, 9, 14), self.ni_holidays)
        # Independence Day
        self.assertIn(date(year, 9, 15), self.ni_holidays)
        # Virgin's Day
        self.assertIn(date(year, 12, 8), self.ni_holidays)
        # Christmas Day
        self.assertIn(date(year, 12, 25), self.ni_holidays)
        # Santo Domingo Day Down
        self.assertIn(date(year, 8, 1), mn_holidays)
        # Santo Domingo Day Up
        self.assertIn(date(year, 8, 10), mn_holidays)

    def test_ni_holidays_1979(self):
        year = 1979
        self.ni_holidays = holidays.NI(years=[year])

        # New Year's Day
        self.assertIn(date(year, 1, 1), self.ni_holidays)
        # Maundy Thursday
        self.assertIn(date(year, 4, 12), self.ni_holidays)
        # Good Friday
        self.assertIn(date(year, 4, 13), self.ni_holidays)
        # Labor Day
        self.assertIn(date(year, 5, 1), self.ni_holidays)
        # Revolution Day
        self.assertIn(date(year, 7, 19), self.ni_holidays)
        # Battle of San Jacinto Day
        self.assertIn(date(year, 9, 14), self.ni_holidays)
        # Independence Day
        self.assertIn(date(year, 9, 15), self.ni_holidays)
        # Virgin's Day
        self.assertIn(date(year, 12, 8), self.ni_holidays)
        # Christmas Day
        self.assertIn(date(year, 12, 25), self.ni_holidays)
