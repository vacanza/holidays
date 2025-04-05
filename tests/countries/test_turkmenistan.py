import unittest
from datetime import date
from holidays.countries import Turkmenistan

class TestTurkmenistanHolidays(unittest.TestCase):
    def setUp(self):
        """Initialize Turkmenistan holidays for testing."""
        self.holidays_2024 = Turkmenistan(years=2024)
        self.holidays_2017 = Turkmenistan(years=2017)  
        self.holidays_1991 = Turkmenistan(years=1991)  

    def test_fixed_holidays_2024(self):
        """Test fixed date public holidays in 2024."""
        fixed_holidays = {
            date(2024, 1, 1): "New Year's Day",
            date(2024, 3, 8): "International Women's Day",
            date(2024, 3, 21): "Nowruz (Persian New Year)",
            date(2024, 3, 22): "Nowruz (Persian New Year)",
            date(2024, 5, 9): "Victory Day",
            date(2024, 5, 18): "Constitution and Revival Day",
            date(2024, 9, 27): "Independence Day",
            date(2024, 10, 6): "Day of Remembrance",
            date(2024, 12, 12): "Neutrality Day",
        }

        for holiday_date, holiday_name in fixed_holidays.items():
            self.assertIn(holiday_date, self.holidays_2024)
            self.assertEqual(self.holidays_2024[holiday_date], holiday_name)

    
    def test_historical_date_changes(self):
        """Test holidays that changed dates over time."""
        self.assertIn(date(2017, 10, 27), self.holidays_2017)
        self.assertEqual(self.holidays_2017[date(2017, 10, 27)], "Independence Day")

        self.assertIn(date(2024, 9, 27), self.holidays_2024)
        
        self.assertIn(date(2017, 5, 18), self.holidays_2017)
        self.assertEqual(self.holidays_2017[date(2017, 5, 18)], "Revival Day")

        self.assertNotIn(date(1991, 3, 21), self.holidays_1991)

        holidays_2014 = Turkmenistan(years=2014)
        if date(2014, 10, 6) in holidays_2014:
            self.assertNotEqual(holidays_2014[date(2014, 10, 6)], "Day of Remembrance")
    
        holidays_2015 = Turkmenistan(years=2015)
        self.assertIn(date(2015, 10, 6), holidays_2015)
        self.assertEqual(holidays_2015[date(2015, 10, 6)], "Day of Remembrance")

    
    def test_neutrality_day_changes(self):
        """Test Neutrality Day date changes."""
        self.assertIn(date(2017, 12, 12), Turkmenistan(years=2017))
        self.assertEqual("Neutrality Day", Turkmenistan(years=2017)[date(2017, 12, 12)])
        
        self.assertIn(date(2020, 6, 27), Turkmenistan(years=2020))
        self.assertEqual("Day of Turkmenistan's Neutrality", Turkmenistan(years=2020)[date(2020, 6, 27)])
        
        self.assertIn(date(2024, 12, 12), Turkmenistan(years=2024))
        self.assertEqual("Neutrality Day", Turkmenistan(years=2024)[date(2024, 12, 12)])
        
        self.assertNotIn(date(1994, 12, 12), Turkmenistan(years=1994))

    
    def test_islamic_holidays(self):
        """Test if Islamic holidays exist in the dataset."""
        holiday_names = list(self.holidays_2024.values())
        self.assertTrue(any("Eid al-Fitr" in name for name in holiday_names))
        self.assertTrue(any("Eid al-Adha" in name for name in holiday_names))

        eid_al_fitr_2024 = date(2024, 4, 10)  
        eid_al_adha_2024 = date(2024, 6, 16)  
        
        self.assertIn(eid_al_fitr_2024, self.holidays_2024)
        self.assertIn("Eid al-Fitr", self.holidays_2024[eid_al_fitr_2024])
        
        self.assertIn(eid_al_adha_2024, self.holidays_2024)
        self.assertIn("Eid al-Adha", self.holidays_2024[eid_al_adha_2024])
        
        eid_days = [d for d, name in self.holidays_2024.items() if "Eid al-Fitr" in name or "Eid al-Adha" in name]
        self.assertGreaterEqual(len(eid_days), 6)


if __name__ == "__main__":
    unittest.main()