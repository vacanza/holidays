import unittest
from datetime import date
import holidays
from holidays.utils import get_holidays_in_range


class TestRangeQueryFilter(unittest.TestCase):

    def test_range_query_with_filter(self):
        us = holidays.US()

        result = get_holidays_in_range(
            us,
            date(2024, 1, 1),
            date(2024, 12, 31),
            keyword="New Year"
        )

        self.assertTrue(
            any("New Year" in name for name in result.values())
        )

    def test_range_query_without_filter(self):
        us = holidays.US()

        result = get_holidays_in_range(
            us,
            date(2024, 1, 1),
            date(2024, 12, 31)
        )

        self.assertGreater(len(result), 0)