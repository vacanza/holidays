import unittest
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

    def test_exact_range(self):
        long_weekends = find_long_weekends("IN", 2025, month=12, exact_range=True)
        self.assertTrue(all(lw["start_date"].startswith("2025-12") for lw in long_weekends))