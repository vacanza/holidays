from datetime import date

from holidays.countries.pitcairn_islands import PitcairnIslands, PN
from tests.common import CommonCountryTests


class TestPitcairnIslands(CommonCountryTests):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            PitcairnIslands, years=range(2000, 2050), years_non_observed=range(2000, 2050)
        )

    def test_country_aliases(self):
        self.assertAliases(PitcairnIslands, PN)

    def test_no_holidays_before_2000(self):
        self.assertNoHolidays(PitcairnIslands(years=1999))

    def test_2024(self):
        self.assertHolidays(
            PitcairnIslands(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-01-23", "Bounty Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-06-08", "King's Birthday"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_translation_pitkern(self):
        holidays = PitcairnIslands(year=2024, language="pih")
        self.assertEqual(holidays[date(2024, 1, 1)], "Niu Ier Dei")
        self.assertEqual(holidays[date(2024, 1, 23)], "Bauti Dei")
        self.assertEqual(holidays[date(2024, 12, 25)], "Krismas Dei")

    def test_random_non_holiday(self):
        self.assertNoHoliday(PitcairnIslands(year=2024), date(2024, 2, 2))
        