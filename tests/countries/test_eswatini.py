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

import warnings
from unittest import TestCase

import holidays
from holidays.countries.eswatini import Eswatini
from tests.common import CommonCountryTests


class TestEswatini(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Eswatini)

    def test_special_holidays(self):
        self.assertHolidayName("Y2K changeover", "1999-12-31", "2000-01-03")

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))

        obs_dts = (
            "2023-01-02",
            "2034-01-02",
            "2040-01-02",
            "2045-01-02",
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

    def test_kings_birthday(self):
        name = "King's Birthday"
        self.assertHolidayName(name, (f"{year}-04-19" for year in range(1987, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1987))

        obs_dts = (
            "2026-04-20",
            "2037-04-20",
            "2043-04-20",
            "2048-04-20",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_workers_day(self):
        name = "Worker's Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))

        obs_dts = (
            "2022-05-02",
            "2033-05-02",
            "2039-05-02",
            "2044-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_national_flag_day(self):
        name = "National Flag Day"
        self.assertHolidayName(name, (f"{year}-04-25" for year in range(1969, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1969))

        obs_dts = (
            "2021-04-26",
            "2027-04-26",
            "2032-04-26",
            "2038-04-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_ascension_day(self):
        name = "Ascension Day"
        self.assertHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, self.full_range)

    def test_birthday_of_late_king_sobhuza(self):
        name = "Birthday of Late King Sobhuza"
        self.assertHolidayName(name, (f"{year}-07-22" for year in range(1983, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1983))

        obs_dts = (
            "2029-07-23",
            "2035-07-23",
            "2040-07-23",
            "2046-07-23",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-09-06" for year in self.full_range))

        obs_dts = (
            "2026-09-07",
            "2037-09-07",
            "2043-09-07",
            "2048-09-07",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))

        obs_dts = (
            "2022-12-27",
            "2033-12-27",
            "2039-12-27",
            "2044-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))

        obs_dts = (
            "2021-12-27",
            "2027-12-27",
            "2032-12-27",
            "2038-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_swaziland_deprecation_warning(self):
        warnings.simplefilter("default")
        with self.assertWarns(Warning):
            holidays.Swaziland()
