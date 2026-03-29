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

from holidays.countries.botswana import Botswana
from tests.common import CommonCountryTests


class TestBotswana(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Botswana, years_non_observed=range(2010, 2024))

    def test_special_holidays(self):
        self.assertHoliday("2019-07-02")

    def test_new_years_day(self):
        name = "New Year's Day"
        name_holiday = f"{name} Holiday"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        self.assertHolidayName(name_holiday, (f"{year}-01-02" for year in self.full_range))

        obs_dts = (
            "2012-01-03",
            "2017-01-03",
            "2023-01-03",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        dts_holiday = (
            "2005-01-03",
            "2011-01-03",
            "2022-01-03",
        )
        self.assertHolidayName(f"{name_holiday} (observed)", dts_holiday)
        self.assertNoNonObservedHoliday(obs_dts, dts_holiday)

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

    def test_holy_saturday(self):
        name = "Holy Saturday"
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

    def test_labor_day(self):
        name = "Labour Day"
        self.assertHoliday(f"{year}-05-01" for year in self.full_range)

        obs_dts = (
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        dts_sat = (
            "2021-05-03",
            "2027-05-03",
            "2032-05-03",
        )
        self.assertHolidayName(f"{name} Holiday", dts_sat)
        self.assertNoNonObservedHoliday(obs_dts, dts_sat)

    def test_presidents_day(self):
        name = "President's Day"
        name_holiday = f"{name} Holiday"
        self.assertHolidayName(
            name,
            "2020-07-20",
            "2021-07-19",
            "2022-07-18",
            "2023-07-17",
            "2024-07-15",
            "2025-07-21",
        )
        self.assertHolidayName(name, self.full_range)
        self.assertHolidayName(
            name_holiday,
            "2020-07-21",
            "2021-07-20",
            "2022-07-19",
            "2023-07-18",
            "2024-07-16",
            "2025-07-22",
        )
        self.assertHolidayName(name_holiday, self.full_range)

    def test_botswana_day(self):
        name = "Botswana Day"
        name_holiday = f"{name} Holiday"
        self.assertHolidayName(name, (f"{year}-09-30" for year in self.full_range))
        self.assertHolidayName(name_holiday, (f"{year}-10-01" for year in self.full_range))

        obs_dts = (
            "2007-10-02",
            "2012-10-02",
            "2018-10-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        dts_holiday = (
            "2006-10-02",
            "2017-10-02",
            "2023-10-02",
        )
        self.assertHolidayName(f"{name_holiday} (observed)", dts_holiday)
        self.assertNoNonObservedHoliday(obs_dts, dts_holiday)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))

        obs_dts = (
            "2011-12-27",
            "2016-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))

        obs_dts = (
            "2004-12-27",
            "2010-12-27",
            "2021-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        dts_holiday = (
            "2020-12-28",
            "2026-12-28",
            "2037-12-28",
        )
        self.assertHolidayName(f"{name} Holiday", dts_holiday)
        self.assertNoNonObservedHoliday(obs_dts, dts_holiday)

    def test_2021(self):
        self.assertHolidayDatesInYear(
            2021,
            "2021-01-01",
            "2021-01-02",
            "2021-04-02",
            "2021-04-03",
            "2021-04-05",
            "2021-05-01",
            "2021-05-03",
            "2021-05-13",
            "2021-07-01",
            "2021-07-19",
            "2021-07-20",
            "2021-09-30",
            "2021-10-01",
            "2021-12-25",
            "2021-12-26",
            "2021-12-27",
        )

    def test_2022(self):
        self.assertHolidayDatesInYear(
            2022,
            "2022-01-01",
            "2022-01-02",
            "2022-01-03",
            "2022-04-15",
            "2022-04-16",
            "2022-04-18",
            "2022-05-01",
            "2022-05-02",
            "2022-05-26",
            "2022-07-01",
            "2022-07-18",
            "2022-07-19",
            "2022-09-30",
            "2022-10-01",
            "2022-12-25",
            "2022-12-26",
            "2022-12-27",
        )

    def test_2023(self):
        self.assertHolidayDatesInYear(
            2023,
            "2023-01-01",
            "2023-01-02",
            "2023-01-03",
            "2023-04-07",
            "2023-04-08",
            "2023-04-10",
            "2023-05-01",
            "2023-05-18",
            "2023-07-01",
            "2023-07-17",
            "2023-07-18",
            "2023-09-30",
            "2023-10-01",
            "2023-10-02",
            "2023-12-25",
            "2023-12-26",
        )
