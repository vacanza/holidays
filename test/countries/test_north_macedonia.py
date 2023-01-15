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


class TestNorthMacedonia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.MK()

    def test_holidays(self):
        # https://en.wikipedia.org/wiki/Public_holidays_in_North_Macedonia
        self.assertIn(date(2019, 1, 1), self.holidays)  # New Year's Day
        self.assertIn(
            date(2019, 1, 7), self.holidays
        )  # Christmas Day(Orthodox)
        self.assertIn(
            date(2019, 4, 29), self.holidays
        )  # Easter Monday (Orthodox)
        self.assertIn(
            date(2020, 4, 20), self.holidays
        )  # Easter Monday (Orthodox)
        self.assertIn(date(2019, 5, 1), self.holidays)  # Labour Day
        self.assertIn(
            date(2019, 5, 24), self.holidays
        )  # Saints Cyril and Methodius Day
        self.assertIn(
            date(2019, 8, 2), self.holidays
        )  # Republic Day (North Macedonia)
        self.assertIn(date(2019, 9, 8), self.holidays)  # Independence Day
        self.assertIn(
            date(2019, 10, 11), self.holidays
        )  # Day of Macedonian Uprising in 1941
        self.assertIn(
            date(2019, 10, 23), self.holidays
        )  # Day of the Macedonian Revolutionary Struggle
        self.assertIn(
            date(2019, 12, 8), self.holidays
        )  # Saint Clement of Ohrid Day
        self.assertIn(date(2019, 6, 4), self.holidays)  # Eid al-Fitr
        self.assertIn(date(2020, 5, 24), self.holidays)  # Eid al-Fitr
