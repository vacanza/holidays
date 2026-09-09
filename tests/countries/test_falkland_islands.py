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

from holidays.countries.falkland_islands import FalklandIslands
from tests.common import CommonCountryTests


class TestFalklandIslands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(FalklandIslands)

    def test_special_holidays(self):
        self.assertHoliday(
            "2022-09-19",
            "2023-05-08",
        )

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dt = (
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_margaret_thatcher_day(self):
        name = "Margaret Thatcher Day"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(name, (f"{year}-01-10" for year in self.full_range))

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_queens_birthday(self):
        name = "HM The Queen's Birthday"
        self.assertHolidayName(name, (f"{year}-04-21" for year in range(self.start_year, 2023)))
        self.assertNoHolidayName(name, range(2023, self.end_year))
        obs_dt = (
            "2007-04-23",
            "2012-04-23",
            "2013-04-22",
            "2018-04-23",
            "2019-04-22",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_liberation_day(self):
        name = "Liberation Day"
        self.assertHolidayName(name, (f"{year}-06-14" for year in self.full_range))
        obs_dt = (
            "2008-06-16",
            "2009-06-15",
            "2014-06-16",
            "2015-06-15",
            "2020-06-15",
            "2025-06-16",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_falkland_day(self):
        name = "Falkland Day"
        self.assertHolidayName(name, (f"{year}-08-14" for year in range(self.start_year, 2002)))
        self.assertNoHolidayName(name, range(2002, self.end_year))
        obs_dt = (
            "1983-08-15",
            "1988-08-15",
            "1993-08-16",
            "1994-08-15",
            "1999-08-16",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        self.assertWorkdayHolidayName(
            name, (f"{year}-08-14" for year in range(2002, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2002))

    def test_peat_cutting_day(self):
        name = "Peat Cutting Day"
        self.assertHolidayName(
            name,
            "2020-10-05",
            "2021-10-04",
            "2022-10-03",
            "2023-10-02",
            "2024-10-07",
            "2025-10-06",
        )
        self.assertHolidayName(name, range(2002, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2002))

    def test_kings_birthday(self):
        name = "HM The King's Birthday"
        self.assertHolidayName(name, (f"{year}-11-14" for year in range(2022, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2022))
        obs_dt = (
            "2026-11-16",
            "2027-11-15",
            "2032-11-15",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dt = (
            "2010-12-28",
            "2011-12-28",
            "2016-12-28",
            "2021-12-28",
            "2022-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        obs_dt = (
            "2010-12-29",
            "2015-12-28",
            "2020-12-28",
            "2021-12-29",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_christmas_day_three(self):
        name = "Christmas Holiday"
        self.assertHolidayName(name, (f"{year}-12-27" for year in self.full_range))
        obs_dt = (
            "2014-12-29",
            "2015-12-29",
            "2020-12-29",
            "2025-12-29",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_government_holiday(self):
        name = "Government Holiday"
        self.assertNoHolidayName(name)
        self.assertGovernmentHolidayName(
            name,
            "2022-12-29",
            "2022-12-30",
            "2023-12-28",
            "2023-12-29",
            "2024-12-30",
            "2024-12-31",
            "2025-12-30",
            "2025-12-31",
        )
        self.assertGovernmentHolidayName(name, self.full_range)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-01-10", "Margaret Thatcher Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-06-14", "Liberation Day"),
            ("2025-06-16", "Liberation Day (observed)"),
            ("2025-08-14", "Falkland Day"),
            ("2025-10-06", "Peat Cutting Day"),
            ("2025-11-14", "HM The King's Birthday"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
            ("2025-12-27", "Christmas Holiday"),
            ("2025-12-29", "Christmas Holiday (observed)"),
            ("2025-12-30", "Government Holiday"),
            ("2025-12-31", "Government Holiday"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-10", "Margaret Thatcher Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-06-14", "Liberation Day"),
            ("2025-06-16", "Liberation Day (observed)"),
            ("2025-08-14", "Falkland Day"),
            ("2025-10-06", "Peat Cutting Day"),
            ("2025-11-14", "King's Birthday"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
            ("2025-12-27", "Christmas Holiday"),
            ("2025-12-29", "Christmas Holiday (observed)"),
            ("2025-12-30", "Government Holiday"),
            ("2025-12-31", "Government Holiday"),
        )
