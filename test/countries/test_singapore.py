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

import importlib.util
import unittest
from datetime import date

import holidays
from holidays.constants import APR, AUG, DEC, JAN, JUN, MAY, NOV


class TestSingapore(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Singapore()

    def test_Singapore(self):
        # <= 1968 holidays
        self.assertIn(date(1968, 4, 13), self.holidays)
        self.assertIn(date(1968, 4, 15), self.holidays)
        self.assertIn(date(1968, 12, 26), self.holidays)
        # latest polling day
        self.assertIn(date(2015, 9, 11), self.holidays)
        # SG50
        self.assertIn(date(2015, 8, 7), self.holidays)
        # Year with lunar leap month
        self.assertIn(date(2015, 8, 7), self.holidays)
        # Latest holidays
        # Source: https://www.mom.gov.sg/employment-practices/public-holidays
        # 2018
        self.assertIn(date(2018, 1, 1), self.holidays)
        self.assertIn(date(2018, 2, 16), self.holidays)
        self.assertIn(date(2018, 2, 17), self.holidays)
        self.assertIn(date(2018, 3, 30), self.holidays)
        self.assertIn(date(2018, 5, 1), self.holidays)
        self.assertIn(date(2018, 5, 29), self.holidays)
        self.assertIn(date(2018, 6, 15), self.holidays)
        self.assertIn(date(2018, 8, 9), self.holidays)
        self.assertIn(date(2018, 8, 22), self.holidays)
        self.assertIn(date(2018, 11, 6), self.holidays)
        self.assertIn(date(2018, 12, 25), self.holidays)
        # 2018: total holidays (11 + 0 falling on a Sunday)
        self.assertEqual(len(holidays.Singapore(years=[2018])), 11 + 0)
        # 2022
        self.assertIn(date(2022, 1, 1), self.holidays)
        self.assertIn(date(2022, 2, 1), self.holidays)
        self.assertIn(date(2022, 2, 2), self.holidays)
        self.assertIn(date(2022, 4, 15), self.holidays)
        self.assertIn(date(2022, 5, 1), self.holidays)
        self.assertIn(date(2022, 5, 2), self.holidays)
        self.assertIn(date(2022, 5, 3), self.holidays)
        self.assertIn(date(2022, 5, 15), self.holidays)
        self.assertIn(date(2022, 5, 16), self.holidays)
        self.assertIn(date(2022, 7, 9), self.holidays)
        self.assertIn(date(2022, 8, 9), self.holidays)
        self.assertIn(date(2022, 10, 24), self.holidays)
        self.assertIn(date(2022, 12, 25), self.holidays)
        self.assertIn(date(2022, 12, 26), self.holidays)
        # 2022: total holidays (11 + 3 falling on a Sunday)
        self.assertEqual(len(holidays.Singapore(years=[2022])), 11 + 3)
        # 2023
        self.assertIn(date(2023, JAN, 1), self.holidays)
        self.assertIn(date(2023, JAN, 2), self.holidays)
        self.assertIn(date(2023, JAN, 22), self.holidays)
        self.assertIn(date(2023, JAN, 23), self.holidays)
        self.assertIn(date(2023, JAN, 24), self.holidays)
        self.assertIn(date(2023, APR, 7), self.holidays)
        self.assertIn(date(2023, APR, 22), self.holidays)
        self.assertIn(date(2023, MAY, 1), self.holidays)
        self.assertIn(date(2023, JUN, 2), self.holidays)
        self.assertIn(date(2023, JUN, 29), self.holidays)
        self.assertIn(date(2023, AUG, 9), self.holidays)
        self.assertIn(date(2023, NOV, 12), self.holidays)
        self.assertIn(date(2023, NOV, 13), self.holidays)
        self.assertIn(date(2023, DEC, 25), self.holidays)
        # 2023: total holidays (11 + 3 falling on a Sunday)
        self.assertEqual(len(holidays.Singapore(years=[2023])), 11 + 3)

        # holidays estimated using lunar calendar
        self.assertIn(date(2050, 6, 4), self.holidays)  # Vesak Day
        self.assertIn(date(2050, 11, 12), self.holidays)  # Deepavali
        # holidays estimated using library hijri-converter
        if importlib.util.find_spec("hijri_converter"):
            # <= 1968 holidays
            self.assertIn(date(1968, 1, 2), self.holidays)
            # 2021
            self.assertIn(date(2050, 6, 20), self.holidays)  # Hari Raya Puasa
            self.assertIn(date(2050, 8, 28), self.holidays)  # Hari Raya Haji

    def test_aliases(self):
        """For coverage purposes"""
        h = holidays.SG()
        self.assertIsInstance(h, holidays.Singapore)
        h = holidays.SGP()
        self.assertIsInstance(h, holidays.Singapore)
