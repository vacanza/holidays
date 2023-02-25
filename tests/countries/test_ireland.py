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


class TestIreland(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Ireland()

    def test_2020(self):
        self.assertIn("2020-01-01", self.holidays)  # New Year's Day
        self.assertIn("2020-03-17", self.holidays)  # St. Patrick's Day
        self.assertIn("2020-04-13", self.holidays)  # Easter Monday
        self.assertIn("2020-05-04", self.holidays)  # May Day in IE
        self.assertNotIn("2020-05-08", self.holidays)  # May Day in UK not IE
        self.assertIn("2020-06-01", self.holidays)  # June Bank Holiday
        self.assertIn("2020-08-03", self.holidays)  # Summer Bank Holiday
        self.assertIn("2020-10-26", self.holidays)  # October Bank Holiday
        self.assertIn("2020-12-25", self.holidays)  # Christmas Day
        self.assertIn("2020-12-26", self.holidays)  # Boxing Day
        self.assertIn("2020-12-28", self.holidays)  # Boxing Day (Observed)

    def test_st_brigids_day(self):
        # St. Brigid's Day
        for dt in (
            date(2023, 2, 6),
            date(2024, 2, 5),
            date(2025, 2, 3),
            date(2026, 2, 2),
            date(2027, 2, 1),
            date(2028, 2, 7),
            date(2029, 2, 5),
            date(2030, 2, 1),
            date(2031, 2, 3),
            date(2032, 2, 2),
        ):
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)

    def test_may_day(self):
        # Specific Ireland "May Day"
        for dt in [
            date(1978, 5, 1),
            date(1979, 5, 7),
            date(1980, 5, 5),
            date(1995, 5, 8),
            date(1999, 5, 3),
            date(2000, 5, 1),
            date(2010, 5, 3),
            date(2018, 5, 7),
            date(2019, 5, 6),
            date(2020, 5, 4),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)

    def test_st_stephens_day(self):
        # St. Stephen's Day
        self.holidays.observed = False

        for year in range(1900, 2100):
            dt = date(year, 12, 26)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
        self.assertNotIn(date(2009, 12, 28), self.holidays)
        self.assertNotIn(date(2010, 12, 27), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2004, 12, 28), self.holidays)
        self.assertIn(date(2010, 12, 28), self.holidays)
        for year, day in enumerate(
            [
                26,
                26,
                26,
                28,
                26,
                26,
                26,
                26,
                28,
                28,
                26,
                26,
                26,
                26,
                26,
                26,
                26,
                26,
                26,
                26,
                28,
            ],
            2001,
        ):
            dt = date(year, 12, day)
            self.assertIn(dt, self.holidays, dt)
            self.assertIn(
                self.holidays[dt],
                [
                    "St. Stephen's Day",
                    "St. Stephen's Day (Observed)",
                    "Christmas Day (Observed); St. Stephen's Day",
                    "St. Stephen's Day; Christmas Day (Observed)",
                ],
            )

    def test_special_holidays(self):
        self.assertIn("2022-03-18", self.holidays)
