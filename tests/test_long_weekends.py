import unittest
from datetime import date
from utils.long_weekends import get_long_weekends

class TestLongWeekends(unittest.TestCase):
    def test_empty_holidays(self):
        holidays = {}
        result = get_long_weekends(holidays)
        self.assertEqual(result, [])

    def test_consecutive_holidays(self):
        holidays = {
            date(2023, 1, 26): "Republic Day",       # Thursday
            date(2023, 1, 27): "Bridge Leave",        # Friday
        }
        result = get_long_weekends(holidays)
        self.assertTrue(any("Bridge Leave" in item[2] for item in result))

    def test_year_boundary(self):
        holidays = {
            date(2023, 12, 29): "Year End Friday",    # Friday
            date(2024, 1, 1): "New Year Monday",      # Monday
        }
        result = get_long_weekends(holidays)
        self.assertTrue(any("Year End Friday" in item[2] for item in result))
        self.assertTrue(any("New Year Monday" in item[2] for item in result))

if __name__ == "__main__":
    unittest.main()
