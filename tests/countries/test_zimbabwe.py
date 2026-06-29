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

from holidays.countries.zimbabwe import Zimbabwe
from tests.common import CommonCountryTests


class TestZimbabwe(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Zimbabwe)

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "1989-01-02",
            "1995-01-02",
            "2012-01-02",
            "2023-01-02",
            "2040-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_robert_gabriel_mugabe_national_youth_day(self):
        name = "Robert Gabriel Mugabe National Youth Day"
        self.assertHolidayName(name, (f"{year}-02-21" for year in range(2018, 2050)))
        self.assertNoHolidayName(name, range(1988, 2018))
        obs_dts = (
            "2021-02-22",
            "2027-02-22",
            "2038-02-22",
            "2044-02-22",
            "2049-02-22",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

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

    def test_easter_saturday(self):
        name = "Easter Saturday"
        self.assertHolidayName(
            name,
            "2020-04-11",
            "2021-04-03",
            "2022-04-16",
            "2023-04-08",
            "2024-03-30",
            "2025-04-19",
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

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-04-18" for year in self.full_range))
        obs_dts = (
            "1993-04-19",
            "1999-04-19",
            "2010-04-19",
            "2027-04-19",
            "2038-04-19",
            # SUN_TO_NEXT_TUE when Independence Day falls on Easter Sunday.
            "2049-04-20",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_workers_day(self):
        name = "Workers' Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        obs_dts = (
            "1988-05-02",
            "1994-05-02",
            "2011-05-02",
            "2022-05-02",
            "2039-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_africa_day(self):
        name = "Africa Day"
        self.assertHolidayName(name, (f"{year}-05-25" for year in self.full_range))
        obs_dts = (
            "1997-05-26",
            "2003-05-26",
            "2014-05-26",
            "2025-05-26",
            "2036-05-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_zimbabwe_heroes_day(self):
        name = "Zimbabwe Heroes' Day"
        self.assertHolidayName(
            name,
            "2020-08-10",
            "2021-08-09",
            "2022-08-08",
            "2023-08-14",
            "2024-08-12",
            "2025-08-11",
        )
        self.assertHolidayName(name, self.full_range)

    def test_defense_forces_day(self):
        name = "Defense Forces Day"
        self.assertHolidayName(
            name,
            "2020-08-11",
            "2021-08-10",
            "2022-08-09",
            "2023-08-15",
            "2024-08-13",
            "2025-08-12",
        )
        self.assertHolidayName(name, self.full_range)

    def test_unity_day(self):
        name = "Unity Day"
        self.assertHolidayName(name, (f"{year}-12-22" for year in self.full_range))
        obs_dts = (
            "1991-12-23",
            "1996-12-23",
            "2013-12-23",
            "2024-12-23",
            "2041-12-23",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "1988-12-27",
            "1994-12-27",
            "2011-12-27",
            "2022-12-27",
            "2039-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        obs_dts = (
            "1993-12-27",
            "1999-12-27",
            "2010-12-27",
            "2027-12-27",
            "2038-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "New Year's Day"),
            ("2022-02-21", "Robert Gabriel Mugabe National Youth Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-16", "Easter Saturday"),
            ("2022-04-18", "Easter Monday; Independence Day"),
            ("2022-05-01", "Workers' Day"),
            ("2022-05-02", "Workers' Day (observed)"),
            ("2022-05-25", "Africa Day"),
            ("2022-08-08", "Zimbabwe Heroes' Day"),
            ("2022-08-09", "Defense Forces Day"),
            ("2022-12-22", "Unity Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )
