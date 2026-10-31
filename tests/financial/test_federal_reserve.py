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

from holidays.financial.federal_reserve import FederalReserve
from tests.common import CommonFinancialTests


class TestFederalReserve(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(FederalReserve)

    def test_new_years_day(self):
        name = "New Year's Day"
        name_observed = f"{name} (observed)"
        self.assertNonObservedHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        no_obs_dts = (
            "1999-12-31",
            "2004-12-31",
            "2010-12-31",
            "2021-12-31",
        )
        self.assertNoHolidayName(name_observed, no_obs_dts)
        self.assertNoHoliday(no_obs_dts)

    def test_birthday_of_martin_luther_king_jr(self):
        name = "Birthday of Martin Luther King, Jr."
        self.assertHolidayName(
            name,
            "2020-01-20",
            "2021-01-18",
            "2022-01-17",
            "2023-01-16",
            "2024-01-15",
            "2025-01-20",
        )
        self.assertHolidayName(name, self.full_range)

    def test_washingtons_birthday(self):
        name = "Washington's Birthday"
        self.assertHolidayName(
            name,
            "2020-02-17",
            "2021-02-15",
            "2022-02-21",
            "2023-02-20",
            "2024-02-19",
            "2025-02-17",
        )
        self.assertHolidayName(name, self.full_range)

    def test_memorial_day(self):
        name = "Memorial Day"
        self.assertHolidayName(
            name,
            "2020-05-25",
            "2021-05-31",
            "2022-05-30",
            "2023-05-29",
            "2024-05-27",
            "2025-05-26",
        )
        self.assertHolidayName(name, self.full_range)

    def test_juneteenth_national_independence_day(self):
        name = "Juneteenth National Independence Day"
        self.assertNonObservedHolidayName(
            name, (f"{year}-06-19" for year in range(2021, self.end_year))
        )
        self.assertNoNonObservedHolidayName(name, range(self.start_year, 2021))
        obs_dts = (
            "2022-06-20",
            "2033-06-20",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHoliday("2021-06-18", "2027-06-18")

    def test_independence_day(self):
        name = "Independence Day"
        self.assertNonObservedHolidayName(name, (f"{year}-07-04" for year in self.full_range))
        obs_dts = (
            "2004-07-05",
            "2010-07-05",
            "2021-07-05",
            "2027-07-05",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHoliday("2009-07-03", "2015-07-03", "2020-07-03", "2026-07-03")

    def test_labor_day(self):
        name = "Labor Day"
        self.assertHolidayName(
            name,
            "2020-09-07",
            "2021-09-06",
            "2022-09-05",
            "2023-09-04",
            "2024-09-02",
            "2025-09-01",
        )
        self.assertHolidayName(name, self.full_range)

    def test_columbus_day(self):
        name = "Columbus Day"
        self.assertHolidayName(
            name,
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
            "2024-10-14",
            "2025-10-13",
        )
        self.assertHolidayName(name, self.full_range)

    def test_veterans_day(self):
        name = "Veterans Day"
        name_observed = f"{name} (observed)"
        self.assertNonObservedHolidayName(name, (f"{year}-11-11" for year in self.full_range))
        obs_dts = (
            "2001-11-12",
            "2007-11-12",
            "2012-11-12",
            "2018-11-12",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        no_obs_dts = (
            "2000-11-10",
            "2006-11-10",
            "2017-11-10",
            "2023-11-10",
        )
        self.assertNoHolidayName(name_observed, no_obs_dts)
        self.assertNoHoliday(no_obs_dts)

    def test_thanksgiving_day(self):
        name = "Thanksgiving Day"
        self.assertHolidayName(
            name,
            "2020-11-26",
            "2021-11-25",
            "2022-11-24",
            "2023-11-23",
            "2024-11-28",
            "2025-11-27",
        )
        self.assertHolidayName(name, self.full_range)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertNonObservedHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2005-12-26",
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHoliday("2004-12-24", "2010-12-24", "2021-12-24", "2027-12-24")

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "New Year's Day"),
            ("2025-01-20", "Birthday of Martin Luther King, Jr."),
            ("2025-02-17", "Washington's Birthday"),
            ("2025-05-26", "Memorial Day"),
            ("2025-06-19", "Juneteenth National Independence Day"),
            ("2025-07-04", "Independence Day"),
            ("2025-09-01", "Labor Day"),
            ("2025-10-13", "Columbus Day"),
            ("2025-11-11", "Veterans Day"),
            ("2025-11-27", "Thanksgiving Day"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_2027(self):
        self.assertHolidaysInYear(
            2027,
            ("2027-01-01", "New Year's Day"),
            ("2027-01-18", "Birthday of Martin Luther King, Jr."),
            ("2027-02-15", "Washington's Birthday"),
            ("2027-05-31", "Memorial Day"),
            ("2027-06-19", "Juneteenth National Independence Day"),
            ("2027-07-05", "Independence Day (observed)"),
            ("2027-09-06", "Labor Day"),
            ("2027-10-11", "Columbus Day"),
            ("2027-11-11", "Veterans Day"),
            ("2027-11-25", "Thanksgiving Day"),
            ("2027-12-25", "Christmas Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-01-15", "Birthday of Martin Luther King, Jr."),
            ("2024-02-19", "Washington's Birthday"),
            ("2024-05-27", "Memorial Day"),
            ("2024-06-19", "Juneteenth National Independence Day"),
            ("2024-07-04", "Independence Day"),
            ("2024-09-02", "Labor Day"),
            ("2024-10-14", "Columbus Day"),
            ("2024-11-11", "Veterans Day"),
            ("2024-11-28", "Thanksgiving Day"),
            ("2024-12-25", "Christmas Day"),
        )
