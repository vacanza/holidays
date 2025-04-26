#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from datetime import date
from unittest import TestCase

from holidays.countries.turks_and_caicos_islands import TurksAndCaicosIslands, TC, TCA
from tests.common import CommonCountryTests


class TestTC(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(TurksAndCaicosIslands, years=range(2020, 2025))

    def test_country_aliases(self):
        self.assertAliases(TurksAndCaicosIslands, TC, TCA)

    def test_no_checks(self):
        self.assertNoChecks(TurksAndCaicosIslands)

    def test_commonwealth_day(self):
        self.assertHolidayName(
            "Commonwealth Day", 
            (f"{year}-03-{day}" for year, day in 
             [(2020, 9), (2021, 8), (2022, 14), (2023, 13), (2024, 11), (2025, 10)])
        )

    def test_good_friday(self):
        self.assertHolidayName(
            "Good Friday", 
            (f"{year}-{month}-{day}" for year, month, day in 
             [(2020, 4, 10), (2021, 4, 2), (2022, 4, 15), (2023, 4, 7), (2024, 3, 29), (2025, 4, 18)])
        )

    def test_easter_monday(self):
        self.assertHolidayName(
            "Easter Monday", 
            (f"{year}-{month}-{day}" for year, month, day in 
             [(2020, 4, 13), (2021, 4, 5), (2022, 4, 18), (2023, 4, 10), (2024, 4, 1), (2025, 4, 21)])
        )

    def test_jags_mccartney_day(self):
        for year in range(2020, 2026):
            if year == 2020:
                dt = date(2020, 5, 25)
            elif year == 2021:
                dt = date(2021, 5, 31)
            elif year == 2022:
                dt = date(2022, 5, 30)
            elif year == 2023:
                dt = date(2023, 5, 29)
            elif year == 2024:
                dt = date(2024, 5, 27)
            else:  # 2025
                dt = date(2025, 5, 26)
            
            self.assertIn(dt, self.holidays)
            
            if year >= 2020:
                self.assertEqual(self.holidays[dt], "JAGS McCartney Day")
            else:
                self.assertEqual(self.holidays[dt], "National Heroes Day")

    def test_sovereign_birthday(self):
        holidays_2022 = TurksAndCaicosIslands(years=2022)
        self.assertIn(date(2022, 6, 13), holidays_2022)
        self.assertEqual(holidays_2022[date(2022, 6, 13)], "Queen's Birthday")
        
        holidays_2023 = TurksAndCaicosIslands(years=2023)
        self.assertIn(date(2023, 6, 12), holidays_2023)
        self.assertEqual(holidays_2023[date(2023, 6, 12)], "King's Birthday")

    def test_national_youth_day(self):
        self.assertHolidayName(
            "National Youth Day", 
            (f"{year}-09-{day}" for year, day in 
             [(2020, 25), (2021, 24), (2022, 30), (2023, 29), (2024, 27), (2025, 26)])
        )

    def test_national_heritage_day(self):
        holidays_2022 = TurksAndCaicosIslands(years=2022)
        self.assertIn(date(2022, 10, 10), holidays_2022)
        self.assertEqual(holidays_2022[date(2022, 10, 10)], "National Heritage Day")
        
        holidays_2025 = TurksAndCaicosIslands(years=2025)
        self.assertIn(date(2025, 10, 13), holidays_2025)
        self.assertEqual(holidays_2025[date(2025, 10, 13)], "National Heritage Day")

    def test_national_day_of_thanksgiving(self):
        self.assertHolidayName(
            "National Day of Thanksgiving", 
            (f"{year}-11-{day}" for year, day in 
             [(2020, 27), (2021, 26), (2022, 25), (2023, 24), (2024, 29), (2025, 28)])
        )

    def test_2023(self):
        self.assertHolidayDates(
            TurksAndCaicosIslands(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-03-13", "Commonwealth Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-29", "JAGS McCartney Day"),
            ("2023-06-12", "King's Birthday"),
            ("2023-08-01", "Emancipation Day"),
            ("2023-09-29", "National Youth Day"),
            ("2023-10-09", "National Heritage Day"),
            ("2023-11-24", "National Day of Thanksgiving"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_2025(self):
        self.assertHolidayDates(
            TurksAndCaicosIslands(years=2025),
            ("2025-01-01", "New Year's Day"),
            ("2025-03-10", "Commonwealth Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-26", "JAGS McCartney Day"),
            ("2025-06-09", "King's Birthday"),
            ("2025-08-01", "Emancipation Day"),
            ("2025-09-26", "National Youth Day"),
            ("2025-10-13", "National Heritage Day"),
            ("2025-11-28", "National Day of Thanksgiving"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-03-10", "Commonwealth Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-26", "JAGS McCartney Day"),
            ("2025-06-09", "King's Birthday"),
            ("2025-08-01", "Emancipation Day"),
            ("2025-09-26", "National Youth Day"),
            ("2025-10-13", "National Heritage Day"),
            ("2025-11-28", "National Day of Thanksgiving"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-03-10", "Commonwealth Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-26", "JAGS McCartney Day"),
            ("2025-06-09", "King's Birthday"),
            ("2025-08-01", "Emancipation Day"),
            ("2025-09-26", "National Youth Day"),
            ("2025-10-13", "National Heritage Day"),
            ("2025-11-28", "National Day of Thanksgiving"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )
