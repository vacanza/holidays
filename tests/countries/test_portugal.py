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


class TestPT(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.PT()

    def test_2014(self):
        year = 2014
        # http://www.officeholidays.com/countries/portugal/2014.php
        self.assertIn(date(year, 1, 1), self.holidays)  # New Year
        self.assertIn(date(year, 4, 18), self.holidays)  # Good Friday
        self.assertIn(date(year, 4, 20), self.holidays)  # Easter
        self.assertIn(date(year, 4, 25), self.holidays)  # Liberation Day
        self.assertIn(date(year, 5, 1), self.holidays)  # Labour Day
        self.assertIn(date(year, 6, 10), self.holidays)  # Portugal Day
        self.assertNotIn(date(year, 6, 15), self.holidays)  # Corpus Christi
        self.assertIn(date(year, 8, 15), self.holidays)  # Assumption Day
        self.assertNotIn(date(year, 10, 5), self.holidays)  # Republic Day
        self.assertNotIn(date(year, 11, 1), self.holidays)  # All Saints Day
        self.assertNotIn(date(year, 12, 1), self.holidays)  # Independence
        self.assertIn(date(year, 12, 8), self.holidays)  # Immaculate
        self.assertIn(date(year, 12, 25), self.holidays)  # Christmas

    def test_2017(self):
        # http://www.officeholidays.com/countries/portugal/2017.php
        self.assertIn(date(2017, 1, 1), self.holidays)  # New Year
        self.assertIn(date(2017, 4, 14), self.holidays)  # Good Friday
        self.assertIn(date(2017, 4, 16), self.holidays)  # Easter
        self.assertIn(date(2017, 4, 25), self.holidays)  # Liberation Day
        self.assertIn(date(2017, 5, 1), self.holidays)  # Labour Day
        self.assertIn(date(2017, 6, 10), self.holidays)  # Portugal Day
        self.assertIn(date(2017, 6, 15), self.holidays)  # Corpus Christi
        self.assertIn(date(2017, 8, 15), self.holidays)  # Assumption Day
        self.assertIn(date(2017, 10, 5), self.holidays)  # Republic Day
        self.assertIn(date(2017, 11, 1), self.holidays)  # All Saints Day
        self.assertIn(date(2017, 12, 1), self.holidays)  # Independence
        self.assertIn(date(2017, 12, 8), self.holidays)  # Immaculate
        self.assertIn(date(2017, 12, 25), self.holidays)  # Christmas


class TestPortugalExt(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Portugal(subdiv="Ext")

    def test_2017(self):
        self.assertIn(date(2017, 12, 24), self.holidays)  # Christmas' Eve
        self.assertIn(date(2017, 12, 26), self.holidays)  # S.Stephan
        self.assertIn(date(2017, 12, 26), self.holidays)  # New Year's Eve


class TestPortugalMunicipal(unittest.TestCase):
    def test_district_specific_days(self):
        district_01 = holidays.PT(subdiv="01", years=[2017])
        district_02 = holidays.PT(subdiv="02", years=[2017])
        district_03 = holidays.PT(subdiv="03", years=[2017])
        district_04 = holidays.PT(subdiv="04", years=[2017])
        district_05 = holidays.PT(subdiv="05", years=[2017])
        district_06 = holidays.PT(subdiv="06", years=[2017])
        district_07 = holidays.PT(subdiv="07", years=[2017])
        district_08 = holidays.PT(subdiv="08", years=[2017])
        district_09 = holidays.PT(subdiv="09", years=[2017])
        district_10 = holidays.PT(subdiv="10", years=[2017])
        district_11 = holidays.PT(subdiv="11", years=[2017])
        district_12 = holidays.PT(subdiv="12", years=[2017])
        district_13 = holidays.PT(subdiv="13", years=[2017])
        district_14 = holidays.PT(subdiv="14", years=[2017])
        district_15 = holidays.PT(subdiv="15", years=[2017])
        district_16 = holidays.PT(subdiv="16", years=[2017])
        district_17 = holidays.PT(subdiv="17", years=[2017])
        district_18 = holidays.PT(subdiv="18", years=[2017])
        self.assertIn("2017-05-12", district_01)
        self.assertIn("2017-05-25", district_02)
        self.assertIn("2017-06-24", district_03)
        self.assertIn("2017-08-22", district_04)
        self.assertIn("2017-05-02", district_05)
        self.assertIn("2017-07-04", district_06)
        self.assertIn("2017-06-29", district_07)
        self.assertIn("2017-09-07", district_08)
        self.assertIn("2017-11-27", district_09)
        self.assertIn("2017-05-22", district_10)
        self.assertIn("2017-06-13", district_11)
        self.assertIn("2017-05-23", district_12)
        self.assertIn("2017-06-24", district_13)
        self.assertIn("2017-03-19", district_14)
        self.assertIn("2017-09-15", district_15)
        self.assertIn("2017-08-20", district_16)
        self.assertIn("2017-06-13", district_17)
        self.assertIn("2017-09-21", district_18)
