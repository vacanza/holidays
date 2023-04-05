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
from datetime import timedelta as td

import holidays


class TestAT(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.AT()

    def test_new_years(self):
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)

    def test_christmas(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertIn(dt + td(days=+1), self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+2), self.holidays)

    def test_easter_monday(self):
        for dt in [
            date(1900, 4, 16),
            date(1901, 4, 8),
            date(1902, 3, 31),
            date(1999, 4, 5),
            date(2000, 4, 24),
            date(2010, 4, 5),
            date(2018, 4, 2),
            date(2019, 4, 22),
            date(2020, 4, 13),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)

    def test_national_day(self):
        for year in range(1919, 1934):
            dt = date(year, 11, 12)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
        for year in range(1967, 2100):
            dt = date(year, 10, 26)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)

    def test_all_holidays_present(self):
        at_2015 = holidays.AT(years=[2015])
        all_holidays = [
            "Neujahr",
            "Heilige Drei Könige",
            "Ostermontag",
            "Staatsfeiertag",
            "Christi Himmelfahrt",
            "Pfingstmontag",
            "Fronleichnam",
            "Mariä Himmelfahrt",
            "Nationalfeiertag",
            "Allerheiligen",
            "Mariä Empfängnis",
            "Christtag",
            "Stefanitag",
        ]
        for holiday in all_holidays:
            self.assertIn(holiday, at_2015.values())

    def test_subdiv(self):
        at_holidays = holidays.AT(subdiv=1)
        self.assertEqual("1", at_holidays.subdiv)
