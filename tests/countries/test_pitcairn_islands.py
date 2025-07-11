#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date

from holidays.countries.pitcairn_islands import PitcairnIslands, PN, PCN
from tests.common import CommonCountryTests


class TestPitcairnIslands(CommonCountryTests, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            PitcairnIslands, years=range(2000, 2050), years_non_observed=range(2000, 2050)
        )

    def test_country_aliases(self):
        self.assertAliases(PitcairnIslands, PN, PCN)

    def test_2024(self):
        self.assertHolidays(
            PitcairnIslands(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-01-23", "Bounty Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-06-08", "King's Birthday"),  # 2nd Saturday in June
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_2025(self):
        """Test holidays for another year to verify consistency."""
        self.assertHolidays(
            PitcairnIslands(years=2025),
            ("2025-01-01", "New Year's Day"),
            ("2025-01-23", "Bounty Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-06-14", "King's Birthday"),  # 2nd Saturday in June
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_kings_birthday_calculation(self):
        """Test that King's Birthday is always the 2nd Saturday in June."""
        test_years = [2020, 2021, 2022, 2023, 2024, 2025, 2026]

        for year in test_years:
            holidays = PitcairnIslands(years=year)

            # Find the King's Birthday date
            kings_birthday_date = None
            for holiday_date, holiday_name in holidays.items():
                if "Birthday" in holiday_name:
                    kings_birthday_date = holiday_date
                    break

            self.assertIsNotNone(
                kings_birthday_date, f"King's/Queen's Birthday not found in {year}"
            )

            # Verify it's in June
            self.assertEqual(
                kings_birthday_date.month, 6, f"King's/Queen's Birthday not in June for {year}"
            )

            # Verify it's a Saturday (weekday() returns 5 for Saturday)
            self.assertEqual(
                kings_birthday_date.weekday(),
                5,
                f"King's/Queen's Birthday not on Saturday for {year}",
            )

            # Verify it's between 8th and 14th (2nd Saturday range)
            self.assertGreaterEqual(
                kings_birthday_date.day, 8, f"King's/Queen's Birthday too early for {year}"
            )
            self.assertLessEqual(
                kings_birthday_date.day, 14, f"King's/Queen's Birthday too late for {year}"
            )

    def test_bounty_day_fixed_date(self):
        """Test that Bounty Day is always January 23."""
        test_years = [2020, 2021, 2022, 2023, 2024, 2025]

        for year in test_years:
            holidays = PitcairnIslands(years=year)
            expected_date = date(year, 1, 23)

            self.assertIn(expected_date, holidays, f"Bounty Day missing for {year}")
            self.assertEqual(
                holidays[expected_date], "Bounty Day", f"Wrong name for Bounty Day in {year}"
            )

    def test_christian_holidays(self):
        """Test that Christian holidays are calculated correctly."""
        holidays = PitcairnIslands(years=2024)

        # Good Friday should be 2 days before Easter Sunday
        good_friday = date(2024, 3, 29)
        easter_monday = date(2024, 4, 1)

        self.assertIn(good_friday, holidays)
        self.assertIn(easter_monday, holidays)
        self.assertEqual(holidays[good_friday], "Good Friday")
        self.assertEqual(holidays[easter_monday], "Easter Monday")

        # Verify the relationship between Good Friday and Easter Monday
        self.assertEqual((easter_monday - good_friday).days, 3)

    def test_holiday_count_consistency(self):
        """Test that the number of holidays is consistent across years."""
        expected_count = 7  # 7 regular holidays

        test_years = [2020, 2021, 2022, 2023, 2024, 2025]
        for year in test_years:
            holidays = PitcairnIslands(years=year)
            # Allow for observed holidays (weekends may add extra days)
            self.assertGreaterEqual(
                len(holidays), expected_count, f"Too few holidays in {year}: {len(holidays)}"
            )
            self.assertLessEqual(
                len(holidays), expected_count + 2, f"Too many holidays in {year}: {len(holidays)}"
            )

    def test_alias_classes_equivalence(self):
        """Test that alias classes produce identical results."""
        year = 2024

        pitcairn = PitcairnIslands(years=year)
        pn = PN(years=year)
        pcn = PCN(years=year)

        # All should have the same holidays
        self.assertEqual(dict(pitcairn), dict(pn), "PitcairnIslands and PN differ")
        self.assertEqual(dict(pitcairn), dict(pcn), "PitcairnIslands and PCN differ")
        self.assertEqual(dict(pn), dict(pcn), "PN and PCN differ")

    def test_random_non_holiday(self):
        self.assertNoHoliday(PitcairnIslands(years=2024), date(2024, 2, 2))

    def test_multiple_random_non_holidays(self):
        """Test multiple dates that should not be holidays."""
        holidays = PitcairnIslands(years=2024)

        non_holiday_dates = [
            date(2024, 2, 14),  # Valentine's Day
            date(2024, 3, 17),  # St. Patrick's Day
            date(2024, 7, 4),  # US Independence Day
            date(2024, 10, 31),  # Halloween
            date(2024, 11, 11),  # Remembrance Day
        ]

        for test_date in non_holiday_dates:
            self.assertNotIn(test_date, holidays, f"{test_date} should not be a holiday")

    def test_monarch_birthday_naming(self):
        """Test that monarch's birthday uses correct title based on year."""

        # Test Queen's Birthday (before 2023)
        holidays_2022 = PitcairnIslands(years=2022)
        queen_birthday = None
        for _, name in holidays_2022.items():
            if "Birthday" in name:
                queen_birthday = name
                break
        self.assertEqual(queen_birthday, "Queen's Birthday")

        # Test King's Birthday (from 2023 onwards)
        holidays_2023 = PitcairnIslands(years=2023)
        king_birthday = None
        for _, name in holidays_2023.items():
            if "Birthday" in name:
                king_birthday = name
                break
        self.assertEqual(king_birthday, "King's Birthday")
