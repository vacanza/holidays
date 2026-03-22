import unittest
from datetime import date
import holidays
from holidays.utils import get_holidays_in_range


class TestRangeQuery(unittest.TestCase):

    def test_range_query(self):
        us = holidays.US()

        result = get_holidays_in_range(
            us,
            date(2024, 1, 1),
            date(2024, 1, 31)
        )

        # Check inclusion
        self.assertIn(date(2024, 1, 1), result)
        self.assertIn(date(2024, 1, 15), result)

        # Check exclusion
        self.assertNotIn(date(2024, 2, 19), result)