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

from holidays.countries.gibraltar import Gibraltar, GI, GIB
from tests.common import CommonCountryTests


class TestGibraltar(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2000, 2050)
        super().setUpClass(Gibraltar, years=years, years_non_observed=years)

    def test_country_aliases(self):
        self.assertAliases(Gibraltar, GI, GIB)

    def test_no_holidays(self):
        self.assertNoHolidays(Gibraltar(years=1999, categories=self.holidays.supported_categories))

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
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(2000, 2050)))
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
        dts = (
            "2023-02-20",
            "2024-02-12",
            "2025-02-17",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(2023, 2050))
        self.assertNoHolidayName(name, range(2000, 2023))

    def test_commonwealth_day(self):
        name = "Commonwealth Day"
        dts = (
            "2019-03-11",
            "2020-03-09",
            "2021-02-15",
            "2022-02-21",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(2000, 2023))
        self.assertNoHolidayName(name, range(2023, 2050))

    def test_good_friday(self):
        name = "Good Friday"
        dts = (
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(2000, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        dts = (
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(2000, 2050))

    def test_may_day(self):
        name = "May Day"
        dts = (
            "2021-05-01",
            "2022-05-01",
            "2023-05-01",
            "2024-05-01",
            "2025-05-01",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(2000, 2050))
        obs_dt = (
            "2004-05-03",
            "2005-05-02",
            "2021-05-03",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_spring_bank_holiday(self):
        name = "Spring Bank Holiday"
        dts = (
            "2022-06-02",
            "2023-05-29",
            "2024-05-27",
            "2025-05-26",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(2000, 2050))

    def test_queens_birthday(self):
        name = "Queen's Birthday"
        dts = (
            "2019-06-17",
            "2020-06-15",
            "2021-06-14",
            "2022-06-13",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(2000, 2023))
        self.assertNoHolidayName(name, range(2023, 2050))

    def test_kings_birthday(self):
        name = "King's Birthday"
        dts = (
            "2023-06-19",
            "2024-06-17",
            "2025-06-16",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(2023, 2050))
        self.assertNoHolidayName(name, range(2000, 2023))

    def test_summer_bank_holiday(self):
        first_name = "Summer Bank Holiday"
        dts = (
            "2003-08-25",
            "2004-08-30",
            "2005-08-29",
            "2006-08-28",
            "2007-08-27",
        )
        self.assertHolidayName(first_name, dts)
        second_name = "Late Summer Bank Holiday"
        dts = (
            "2022-08-29",
            "2023-08-28",
            "2024-08-26",
            "2025-08-25",
        )
        self.assertHolidayName(second_name, dts)
        self.assertHolidayName(second_name, range(2000, 2002), range(2008, 2050))
        self.assertNoHolidayName(second_name, range(2003, 2008))

    def test_national_day(self):
        name = "Gibraltar National Day"
        self.assertHolidayName(name, (f"{year}-09-10" for year in range(2000, 2016)))
        self.assertHolidayName(name, (f"{year}-09-10" for year in range(2018, 2050)))
        special_dts = (
            "2016-09-05",
            "2017-09-04",
        )
        self.assertHolidayName(name, special_dts)
        obs_dt = (
            "2011-09-12",
            "2022-09-12",
            "2023-09-11",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(2000, 2050)))
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
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(2000, 2050)))
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
            ("2024-05-01", "May Day"),
            ("2024-05-27", "Spring Bank Holiday"),
            ("2024-06-17", "King's Birthday"),
            ("2024-08-26", "Late Summer Bank Holiday"),
            ("2024-09-10", "Gibraltar National Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )
