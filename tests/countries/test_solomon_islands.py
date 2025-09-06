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

from holidays.calendars.gregorian import FEB, JUN, JUL, AUG, DEC
from holidays.countries.solomon_islands import SolomonIslands, SB, SLB
from tests.common import CommonCountryTests


class TestSolomonIslands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SolomonIslands)

    def test_country_aliases(self):
        self.assertAliases(SolomonIslands, SB, SLB)

    def test_no_holidays(self):
        self.assertNoHolidays(SolomonIslands(years=SB.start_year - 1))

    def test_special_holidays(self):
        name = "Public Holiday"
        dt = (
            "2022-09-12",
            "2024-04-17",
        )
        self.assertHolidayName(name, dt)

        dt = "2020-11-18"
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"CH", "GU"}:
                self.assertHolidayName(name, holidays, dt)
            else:
                self.assertNoHoliday(holidays, dt)

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        dt = (
            "2010-12-31",
            "2012-01-02",
            "2017-01-02",
            "2021-12-31",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2019-04-19",
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
            "2019-04-20",
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
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_whit_monday(self):
        name = "Whit Monday"
        self.assertHolidayName(
            name,
            "2019-06-10",
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.full_range)

    def test_queen_king_birthday(self):
        name_1 = "Queen's Birthday"
        self.assertHolidayName(name_1, range(SB.start_year, 2023))
        self.assertHolidayName(
            name_1,
            "2019-06-08",
            "2020-06-13",
            "2021-06-12",
            "2022-06-03",
        )
        dt = (
            "2019-06-07",
            "2020-06-12",
            "2021-06-11",
        )
        self.assertHolidayName(f"{name_1} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

        name_2 = "King's Birthday"
        self.assertHolidayName(name_2, range(2023, 2050))
        self.assertHolidayName(
            name_2,
            "2023-06-16",
            "2024-06-15",
            "2025-06-13",
        )
        dt = "2024-06-14"
        self.assertHolidayName(f"{name_2} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-07-07" for year in self.full_range))
        dt = (
            "2013-07-08",
            "2019-07-08",
            "2024-07-08",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        dt = (
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_national_day_of_thanksgiving(self):
        name = "National Day of Thanksgiving"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        dt = (
            "2009-12-28",
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def _test_province_day_helper(
        self,
        province_code: str,
        holiday_name: str,
        month: int,
        day: int,
        observed_dts: tuple[str, ...],
    ):
        for subdiv, holidays in self.subdiv_holidays.items():  # type: ignore[attr-defined]
            if subdiv == province_code:
                self.assertHolidayName(  # type: ignore[attr-defined]
                    holiday_name,
                    holidays,
                    (f"{year}-{month}-{day}" for year in self.full_range),  # type: ignore[attr-defined]
                )
                observed_name = f"{holiday_name} (observed)"
                self.assertHolidayName(observed_name, holidays, observed_dts)  # type: ignore[attr-defined]
                self.assertNoNonObservedHolidayName(  # type: ignore[attr-defined]
                    observed_name,
                    self.subdiv_holidays_non_observed[subdiv],  # type: ignore[attr-defined]
                    observed_dts,
                )
            else:
                self.assertNoHolidayName(holiday_name, holidays, self.full_range)  # type: ignore[attr-defined]

    def test_central_province_day(self):
        observed_dts = (
            "2013-06-28",
            "2014-06-30",
            "2019-06-28",
            "2024-06-28",
            "2025-06-30",
        )
        self._test_province_day_helper("CE", "Central Province Day", JUN, 29, observed_dts)

    def test_choiseul_province_day(self):
        observed_dts = (
            "2012-02-24",
            "2017-02-24",
            "2018-02-26",
            "2023-02-24",
            "2024-02-26",
        )
        self._test_province_day_helper("CH", "Choiseul Province Day", FEB, 25, observed_dts)

    def test_guadalcanal_province_day(self):
        observed_dts = (
            "2010-08-02",
            "2015-07-31",
            "2020-07-31",
            "2021-08-02",
            "2026-07-31",
        )
        self._test_province_day_helper("GU", "Guadalcanal Province Day", AUG, 1, observed_dts)

    def test_isabel_province_day(self):
        observed_dts = (
            "2012-06-01",
            "2013-06-03",
            "2018-06-01",
            "2019-06-03",
            "2024-06-03",
        )
        self._test_province_day_helper("IS", "Isabel Province Day", JUN, 2, observed_dts)

    def test_makira_ulawa_province_day(self):
        observed_dts = (
            "2013-08-02",
            "2014-08-04",
            "2019-08-02",
            "2024-08-02",
            "2025-08-04",
        )
        self._test_province_day_helper("MK", "Makira-Ulawa Province Day", AUG, 3, observed_dts)

    def test_malaita_province_day(self):
        observed_dts = (
            "2010-08-16",
            "2015-08-14",
            "2020-08-14",
            "2021-08-16",
            "2026-08-14",
        )
        self._test_province_day_helper("ML", "Malaita Province Day", AUG, 15, observed_dts)

    def test_rennell_and_bellona_province_day(self):
        observed_dts = (
            "2013-07-19",
            "2014-07-21",
            "2019-07-19",
            "2024-07-19",
            "2025-07-21",
        )
        self._test_province_day_helper(
            "RB", "Rennell and Bellona Province Day", JUL, 20, observed_dts
        )

    def test_temotu_province_day(self):
        observed_dts = (
            "2013-06-07",
            "2014-06-09",
            "2019-06-07",
            "2024-06-07",
            "2025-06-09",
        )
        self._test_province_day_helper("TE", "Temotu Province Day", JUN, 8, observed_dts)

    def test_western_province_day(self):
        observed_dts = (
            "2013-12-06",
            "2014-12-08",
            "2019-12-06",
            "2024-12-06",
            "2025-12-08",
        )
        self._test_province_day_helper("WE", "Western Province Day", DEC, 7, observed_dts)

    def test_2025(self):
        self.assertHolidays(
            SolomonIslands(years=2025),
            ("2025-01-01", "New Year's Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-19", "Holy Saturday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-06-09", "Whit Monday"),
            ("2025-06-13", "King's Birthday"),
            ("2025-07-07", "Independence Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "National Day of Thanksgiving"),
        )
