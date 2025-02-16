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
from unittest.mock import patch

from holidays import find_long_weekends


class TestLongWeekends(unittest.TestCase):
    def test_valid_input(self):
        long_weekends = find_long_weekends("IN", 2025)
        self.assertIsInstance(long_weekends, list)
        self.assertTrue(all(isinstance(lw, dict) for lw in long_weekends))

    def test_specific_month(self):
        long_weekends = find_long_weekends("IN", 2025, month=8)
        self.assertTrue(all(lw["start_date"].startswith("2025-08") for lw in long_weekends))

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
