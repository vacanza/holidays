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

from holidays.countries.gibraltar import Gibraltar
from tests.common import CommonCountryTests


class TestGibraltar(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Gibraltar)

    def test_special_holidays(self):
        for dt, name in (
            ("2004-08-04", "Tercentenary Holiday"),
            ("2012-06-05", "Queen's Diamond Jubilee"),
            ("2020-05-08", "75th Anniversary of VE Day"),
            ("2022-06-03", "Platinum Jubilee"),
            ("2009-01-12", "Bank Holiday"),
            ("2015-09-07", "Evacuation Commemoration Day"),
            ("2023-05-08", "Special King's Coronation Bank Holiday"),
        ):
            self.assertHolidayName(name, dt)

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dt = (
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_winter_bank_holiday(self):
        name = "Winter Midterm Bank Holiday"
        self.assertHolidayName(
            name,
            "2023-02-20",
            "2024-02-12",
            "2025-02-17",
        )
        self.assertHolidayName(name, range(2023, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2023))

    def test_commonwealth_day(self):
        name = "Commonwealth Day"
        self.assertHolidayName(
            name,
            "2018-03-12",
            "2019-03-11",
            "2020-03-09",
            "2021-02-15",
            "2022-02-21",
        )
        self.assertHolidayName(name, range(self.start_year, 2023))
        self.assertNoHolidayName(name, range(2023, self.end_year))

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

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_workers_memorial_day(self):
        name = "Workers' Memorial Day"
        self.assertHolidayName(
            name,
            "2020-04-28",
            "2021-04-28",
            "2022-04-28",
            "2023-04-28",
            "2024-04-28",
            "2025-04-28",
        )
        self.assertHolidayName(name, range(2013, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2013))
        obs_dt = (
            "2018-04-30",
            "2019-04-29",
            "2024-04-29",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_may_day(self):
        name = "May Day"
        self.assertHolidayName(
            name,
            (
                f"{year}-05-01"
                for year in (*range(self.start_year, 2007), *range(2010, self.end_year))
            ),
        )
        self.assertHolidayName(
            name,
            "2007-05-07",
            "2008-05-05",
            "2009-05-04",
        )
        obs_dt = (
            "2011-05-02",
            "2016-05-02",
            "2021-05-03",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_spring_bank_holiday(self):
        name = "Spring Bank Holiday"
        self.assertHolidayName(
            name,
            "2020-05-25",
            "2021-05-31",
            "2022-06-02",
            "2023-05-29",
            "2024-05-27",
            "2025-05-26",
        )
        self.assertHolidayName(name, self.full_range)

    def test_queens_birthday(self):
        name = "Queen's Birthday"
        self.assertHolidayName(
            name,
            "2018-06-11",
            "2019-06-17",
            "2020-06-15",
            "2021-06-14",
            "2022-06-13",
        )
        self.assertHolidayName(name, range(self.start_year, 2023))
        self.assertNoHolidayName(name, range(2023, self.end_year))

    def test_kings_birthday(self):
        name = "King's Birthday"
        self.assertHolidayName(
            name,
            "2023-06-19",
            "2024-06-17",
            "2025-06-16",
        )
        self.assertHolidayName(name, range(2023, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2023))

    def test_summer_bank_holiday(self):
        first_name = "Summer Bank Holiday"
        self.assertHolidayName(
            first_name,
            "2002-08-26",
            "2003-08-25",
            "2004-08-30",
            "2005-08-29",
            "2006-08-28",
            "2007-08-27",
        )
        self.assertNoHolidayName(
            first_name, range(self.start_year, 2002), range(2008, self.end_year)
        )

        second_name = "Late Summer Bank Holiday"
        self.assertHolidayName(
            second_name,
            "2020-08-31",
            "2021-08-30",
            "2022-08-29",
            "2023-08-28",
            "2024-08-26",
            "2025-08-25",
        )
        self.assertHolidayName(
            second_name, range(self.start_year, 2002), range(2008, self.end_year)
        )
        self.assertNoHolidayName(second_name, range(2002, 2008))

    def test_national_day(self):
        name = "Gibraltar National Day"
        self.assertHolidayName(
            name,
            (
                f"{year}-09-10"
                for year in (*range(self.start_year, 2016), *range(2018, self.end_year))
            ),
        )
        self.assertHolidayName(
            name,
            "2016-09-05",
            "2017-09-04",
        )
        obs_dt = (
            "2011-09-12",
            "2022-09-12",
            "2023-09-11",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dt = (
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        obs_dt = (
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-02-12", "Winter Midterm Bank Holiday"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-28", "Workers' Memorial Day"),
            ("2024-04-29", "Workers' Memorial Day (observed)"),
            ("2024-05-01", "May Day"),
            ("2024-05-27", "Spring Bank Holiday"),
            ("2024-06-17", "King's Birthday"),
            ("2024-08-26", "Late Summer Bank Holiday"),
            ("2024-09-10", "Gibraltar National Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-02-12", "Winter Midterm Bank Holiday"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-28", "Workers' Memorial Day"),
            ("2024-04-29", "Workers' Memorial Day (observed)"),
            ("2024-05-01", "May Day"),
            ("2024-05-27", "Spring Bank Holiday"),
            ("2024-06-17", "King's Birthday"),
            ("2024-08-26", "Late Summer Bank Holiday"),
            ("2024-09-10", "Gibraltar National Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )
