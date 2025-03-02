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

from holidays import find_long_weekends


class TestLongWeekends(unittest.TestCase):
    def test_valid_input(self):
        long_weekends = find_long_weekends("IN", 2025)
        self.assertIsInstance(long_weekends, list)
        self.assertTrue(all(isinstance(lw, dict) for lw in long_weekends))

    def test_specific_month(self):
        long_weekends = find_long_weekends("IN", 2025, month=8)
        self.assertTrue(all(lw["start_date"].month == 8 for lw in long_weekends))

    def test_invalid_year(self):
        with self.assertRaises(ValueError):
            find_long_weekends("IN", 1800)

    def test_invalid_country(self):
        with self.assertRaises(ValueError):
            find_long_weekends("XYZ", 2025)

    def test_invalid_month(self):
        with self.assertRaises(ValueError):
            find_long_weekends("IN", 2025, month=13)

    def test_no_holidays(self):
        long_weekends = find_long_weekends("IN", 2025, month=2)
        self.assertEqual(long_weekends, [])

    def test_leap_year(self):
        long_weekends = find_long_weekends("IN", 2024)  # 2024 is a leap year
        self.assertIsInstance(long_weekends, list)

    def test_invalid_month_type(self):
        with self.assertRaises(TypeError):
            find_long_weekends("IN", 2025, month="August")

    def test_country_specific_rules(self):
        long_weekends = find_long_weekends("US", 2025)
        self.assertIsInstance(long_weekends, list)

    def test_exact_range_exclusion(self):
        """
        This test ensures exact_range=True excludes long weekends beyond the month.
        """
        country = "US"
        year = 2024
        month = 1  # Looking for long weekends only in January
        exact_range = True

        result = find_long_weekends(country, year, month, exact_range=exact_range)

        # Ensure no long weekend extends beyond January
        for weekend in result:
            start_date = weekend["start_date"]
            end_date = weekend["end_date"]

            self.assertEqual(start_date.month, month, "Start date exceeds month.")
            self.assertEqual(end_date.month, month, "End date exceeds month.")

    def test_holidays_extended_range(self):
        result = find_long_weekends("UA", 2019, month=4, exact_range=True)
        self.assertIsNotNone(result)  # Ensure the result is not None
        self.assertTrue(len(result) > 0)  # Ensure there's at least one long weekend in the result

    def test_without_month(self):
        # Call the function without the month parameter
        result = find_long_weekends("UA", 2019, exact_range=True)

        # Assert that the function runs without errors (basic coverage)
        self.assertIsNotNone(result)  # Ensures result is not None
        self.assertIsInstance(result, list)  # Ensures result is a list

    def test_language_parameter(self):
        """Test that holiday names are returned in the specified language."""
        # Test with default language
        result_default = find_long_weekends("UA", 2023, month=8)

        # Test with specified language if supported
        result_language = find_long_weekends("UA", 2023, month=8, language="en")

        # Verify results are returned in both cases
        self.assertIsNotNone(result_default)
        self.assertIsNotNone(result_language)

        # If both have results, verify the holiday names differ
        if result_default and result_language:
            default_names = [h for weekend in result_default for h in weekend["holidays"]]
            language_names = [h for weekend in result_language for h in weekend["holidays"]]

            # Skip if no holidays in the results
            if default_names and language_names:
                self.assertNotEqual(
                    default_names,
                    language_names,
                    "Holiday names should differ when language is changed",
                )
