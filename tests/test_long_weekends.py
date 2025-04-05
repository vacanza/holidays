import unittest
from datetime import date
from utils.long_weekends import get_long_weekends


class TestLongWeekends(unittest.TestCase):
    def test_basic_long_weekends(self):
        holidays_dict = {
            date(2025, 8, 15): "Independence Day",  # Friday
            date(2025, 10, 6): "Some Monday Holiday",  # Monday
            date(2025, 12, 25): "Christmas",  # Thursday, not long weekend
        }

        expected = [
            (date(2025, 8, 15), date(2025, 8, 17), "Independence Day"),
            (date(2025, 10, 4), date(2025, 10, 6), "Some Monday Holiday"),
        ]

        result = get_long_weekends(holidays_dict)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
