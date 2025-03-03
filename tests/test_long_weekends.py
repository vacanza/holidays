#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date

from holidays import find_long_weekends


class TestLongWeekends(unittest.TestCase):
    def test_valid_input(self):
        long_weekends = find_long_weekends("IN", 2025)
        self.assertIsInstance(long_weekends, list)
        self.assertGreater(len(long_weekends), 0, "Expected at least one long weekend")
        self.assertTrue(all(isinstance(lw, dict) for lw in long_weekends))

    def test_specific_month(self):
        long_weekends = find_long_weekends("IN", 2025, month=8)
        self.assertTrue(all(lw["start_date"].month == 8 for lw in long_weekends))
        self.assertGreater(
            len(long_weekends),
            0,
            "Expected at least one long weekend in August 2025",
        )

    def test_invalid_country(self):
        with self.assertRaises(ValueError):
            find_long_weekends("XYZ", 2025)

    def test_invalid_month(self):
        with self.assertRaises(ValueError):
            find_long_weekends("IN", 2025, month=13)

    def test_no_holidays(self):
        long_weekends = find_long_weekends("IN", 2025, month=2)
        self.assertEqual(
            long_weekends,
            [],
            "Expected empty list when no holidays exist in February",
        )

    def test_leap_year(self):
        long_weekends = find_long_weekends("IN", 2024)  # 2024 is a leap year
        self.assertIsInstance(long_weekends, list)
        self.assertGreater(
            len(long_weekends),
            0,
            "Expected at least one long weekend in a leap year",
        )

    def test_country_specific_rules(self):
        long_weekends = find_long_weekends("US", 2025)
        self.assertIsInstance(long_weekends, list)
        self.assertGreater(
            len(long_weekends),
            0,
            "Expected at least one long weekend in the US",
        )

    def test_exact_range_exclusion(self):
        country = "US"
        year = 2024
        month = 1
        exact_range = True

        result = find_long_weekends(country, year, month, exact_range=exact_range)

        for weekend in result:
            start_date = weekend["start_date"]
            end_date = weekend["end_date"]

            self.assertEqual(start_date.month, month, "Start date exceeds month.")
            self.assertEqual(end_date.month, month, "End date exceeds month.")

    def test_holidays_extended_range(self):
        result = find_long_weekends("UA", 2019, month=4, exact_range=True)
        self.assertIsNotNone(result)
        self.assertGreater(
            len(result),
            0,
            "Expected at least one long weekend in April 2019",
        )

    def test_without_month(self):
        result = find_long_weekends("UA", 2019, exact_range=True)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

    def test_known_holidays(self):
        """Check if the function correctly identifies expected long weekends."""
        expected_long_weekends = [
            {
                "start_date": date(2025, 4, 18),
                "end_date": date(2025, 4, 20),
                "duration": 3,
                "holidays": ["Good Friday", "Easter Sunday"],
            }
        ]

        long_weekends = find_long_weekends("IN", 2025, month=4)

        self.assertIsInstance(long_weekends, list)
        self.assertGreater(
            len(long_weekends),
            0,
            "Expected at least one long weekend in April 2025",
        )

        # Compare dictionaries properly
        match_found = any(
            lw["start_date"] == expected["start_date"]
            and lw["end_date"] == expected["end_date"]
            and lw["duration"] == expected["duration"]
            and set(lw["holidays"]) == set(expected["holidays"])
            for lw in long_weekends
            for expected in expected_long_weekends
        )

        self.assertTrue(
            match_found,
            f"Expected long weekend {expected_long_weekends} not found in {long_weekends}",
        )
