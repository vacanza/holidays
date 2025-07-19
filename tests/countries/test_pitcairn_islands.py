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

from unittest import TestCase

from holidays.countries.pitcairn_islands import PitcairnIslands, PN, PCN
from tests.common import CommonCountryTests


class TestPitcairnIslands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2016, 2050)
        super().setUpClass(PitcairnIslands, years=years, years_non_observed=years)

    def test_country_aliases(self):
        self.assertAliases(PitcairnIslands, PN, PCN)

    def test_no_holidays(self):
        self.assertNoHolidays(PitcairnIslands(years=2015))

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(2016, 2050)))
        obs_dt = (
            "2017-01-02",  # 2017: Jan 1 was Sunday
            "2022-01-03",  # 2022: Jan 1 was Saturday
            "2023-01-02",  # 2023: Jan 1 was Sunday
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_bounty_day(self):
        name = "Bounty Day"
        self.assertHolidayName(name, (f"{year}-01-23" for year in range(2016, 2050)))
        obs_dt = (
            "2021-01-25",  # 2021: Jan 23 was Saturday
            "2022-01-24",  # 2022: Jan 23 was Sunday
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(2016, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(2016, 2050))

    def test_queens_birthday(self):
        name = "Queen's Birthday"
        # 2nd Saturday in June before 2023
        self.assertHolidayName(
            name,
            "2016-06-11",  # 2nd Saturday in June 2016
            "2017-06-10",  # 2nd Saturday in June 2017
            "2018-06-09",  # 2nd Saturday in June 2018
            "2019-06-08",  # 2nd Saturday in June 2019
            "2020-06-13",  # 2nd Saturday in June 2020
            "2021-06-12",  # 2nd Saturday in June 2021
            "2022-06-11",  # 2nd Saturday in June 2022
        )
        self.assertHolidayName(name, range(2016, 2023))
        self.assertNoHolidayName(name, range(2023, 2050))

    def test_kings_birthday(self):
        name = "King's Birthday"
        # 1st Monday in June from 2023 onwards
        self.assertHolidayName(
            name,
            "2023-06-05",  # 1st Monday in June 2023
            "2024-06-03",  # 1st Monday in June 2024
            "2025-06-02",  # 1st Monday in June 2025
        )
        self.assertHolidayName(name, range(2023, 2050))
        self.assertNoHolidayName(name, range(2016, 2023))

    def test_pitcairn_day(self):
        name = "Pitcairn Day"
        self.assertHolidayName(name, (f"{year}-07-02" for year in range(2016, 2050)))
        obs_dt = (
            "2017-07-03",  # 2017: July 2 was Sunday
            "2022-07-04",  # 2022: July 2 was Saturday
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(2016, 2050)))
        obs_dt = (
            "2016-12-27",  # 2016: Dec 25 was Sunday
            "2021-12-27",  # 2021: Dec 25 was Saturday
            "2022-12-27",  # 2022: Dec 25 was Sunday
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(2016, 2050)))
        obs_dt = (
            "2020-12-28",  # 2020: Dec 26 was Saturday
            "2021-12-28",  # 2021: Dec 26 was Sunday
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_government_holidays(self):
        # Test New Year's Day (Jan 2) for government category
        name = "New Year's Day"
        gov_holidays = PitcairnIslands(categories="GOVERNMENT", years=2022)
        self.assertIn("2022-01-02", gov_holidays)
        self.assertEqual(gov_holidays["2022-01-02"], name)

    def test_workday_holidays(self):
        # Test ANZAC Day and Remembrance Day for workday category
        workday_holidays = PitcairnIslands(categories="WORKDAY", years=2022)

        # ANZAC Day (April 25)
        self.assertIn("2022-04-25", workday_holidays)
        self.assertEqual(workday_holidays["2022-04-25"], "ANZAC Day")

        # Remembrance Day (November 11)
        self.assertIn("2022-11-11", workday_holidays)
        self.assertEqual(workday_holidays["2022-11-11"], "Remembrance Day")

    def test_anzac_day(self):
        name = "ANZAC Day"
        workday_holidays = PitcairnIslands(categories="WORKDAY", years=range(2016, 2050))
        # ANZAC Day is April 25th every year in workday category
        for year in range(2016, 2025):
            expected_date = f"{year}-04-25"
            self.assertIn(expected_date, workday_holidays)
            self.assertEqual(workday_holidays[expected_date], name)

    def test_remembrance_day(self):
        name = "Remembrance Day"
        workday_holidays = PitcairnIslands(categories="WORKDAY", years=range(2016, 2050))
        # Remembrance Day is November 11th every year in workday category
        for year in range(2016, 2025):
            expected_date = f"{year}-11-11"
            self.assertIn(expected_date, workday_holidays)
            self.assertEqual(workday_holidays[expected_date], name)

    def test_monarch_birthday_historical_accuracy(self):
        """Test that monarch's birthday uses correct title based on year."""
        # Verify Queen's Birthday exists before 2023
        self.assertHolidayName("Queen's Birthday", "2022-06-11")
        self.assertNoHolidayName("King's Birthday", "2022-06-11")

        # Verify King's Birthday exists from 2023 onwards
        self.assertHolidayName("King's Birthday", "2023-06-05")
        self.assertNoHolidayName("Queen's Birthday", "2023-06-05")

    def test_holiday_categories(self):
        """Test that different categories return appropriate holidays."""
        public_holidays = PitcairnIslands(years=2022)
        expected_public = {
            "2022-01-01": "New Year's Day",
            "2022-01-23": "Bounty Day",
            "2022-04-15": "Good Friday",
            "2022-04-18": "Easter Monday",
            "2022-06-11": "Queen's Birthday",
            "2022-07-02": "Pitcairn Day",
            "2022-12-25": "Christmas Day",
            "2022-12-26": "Boxing Day",
        }

        for date, name in expected_public.items():
            self.assertIn(date, public_holidays)
            self.assertEqual(public_holidays[date], name)

        government_holidays = PitcairnIslands(categories="GOVERNMENT", years=2022)
        self.assertIn("2022-01-02", government_holidays)
        self.assertEqual(government_holidays["2022-01-02"], "New Year's Day")

        workday_holidays = PitcairnIslands(categories="WORKDAY", years=2022)
        expected_workday = {
            "2022-04-25": "ANZAC Day",
            "2022-11-11": "Remembrance Day",
        }

        for date, name in expected_workday.items():
            self.assertIn(date, workday_holidays)
            self.assertEqual(workday_holidays[date], name)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-23", "Bounty Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-06-11", "Queen's Birthday"),
            ("2022-07-02", "Pitcairn Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-23", "Bounty Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-06-11", "Queen's Birthday"),
            ("2022-07-02", "Pitcairn Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
        )
