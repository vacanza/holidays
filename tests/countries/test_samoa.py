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

from holidays.countries.samoa import Samoa
from tests.common import CommonCountryTests


class TestSamoa(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Samoa)

    def test_special_holidays(self):
        self.assertHolidayName("General Election Holiday", "2025-08-28", "2025-08-29")

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2012-01-03",
            "2017-01-03",
            "2023-01-03",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_new_years_second_day(self):
        name = "The Day After New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-02" for year in self.full_range))
        obs_dts = (
            "2011-01-03",
            "2022-01-03",
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

    def test_day_after_good_friday(self):
        name = "Day After Good Friday"
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

    def test_mothers_day(self):
        name = "Mother's Day"
        self.assertHolidayName(
            name,
            "2020-05-11",
            "2021-05-10",
            "2022-05-09",
            "2023-05-15",
            "2024-05-13",
            "2025-05-12",
        )
        self.assertHolidayName(name, self.full_range)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-06-01" for year in self.full_range))
        obs_dts = (
            "2008-06-02",
            "2014-06-02",
            "2025-06-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_fathers_day(self):
        name = "Father's Day"
        self.assertHolidayName(
            name,
            "2020-08-10",
            "2021-08-09",
            "2022-08-15",
            "2023-08-14",
            "2024-08-12",
            "2025-08-11",
        )
        self.assertHolidayName(name, self.full_range)

    def test_white_sunday(self):
        name = "White Sunday (Lotu a Tamaiti)"
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
            "2010-12-27",
            "2021-12-27",
            "2027-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_2023(self):
        self.assertHolidaysInYear(
            2023,
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "The Day After New Year's Day"),
            ("2023-01-03", "New Year's Day (observed)"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-08", "Day After Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-15", "Mother's Day"),
            ("2023-06-01", "Independence Day"),
            ("2023-08-14", "Father's Day"),
            ("2023-10-09", "White Sunday (Lotu a Tamaiti)"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "New Year's Day"),
            ("2024-01-02", "The Day After New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "Day After Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-13", "Mother's Day"),
            ("2024-06-01", "Independence Day"),
            ("2024-08-12", "Father's Day"),
            ("2024-10-14", "White Sunday (Lotu a Tamaiti)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "New Year's Day"),
            ("2025-01-02", "The Day After New Year's Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-19", "Day After Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-12", "Mother's Day"),
            ("2025-06-01", "Independence Day"),
            ("2025-06-02", "Independence Day (observed)"),
            ("2025-08-11", "Father's Day"),
            ("2025-08-28", "General Election Holiday"),
            ("2025-08-29", "General Election Holiday"),
            ("2025-10-13", "White Sunday (Lotu a Tamaiti)"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_2026(self):
        self.assertHolidaysInYear(
            2026,
            ("2026-01-01", "New Year's Day"),
            ("2026-01-02", "The Day After New Year's Day"),
            ("2026-04-03", "Good Friday"),
            ("2026-04-04", "Day After Good Friday"),
            ("2026-04-06", "Easter Monday"),
            ("2026-05-11", "Mother's Day"),
            ("2026-06-01", "Independence Day"),
            ("2026-08-10", "Father's Day"),
            ("2026-10-12", "White Sunday (Lotu a Tamaiti)"),
            ("2026-12-25", "Christmas Day"),
            ("2026-12-26", "Boxing Day"),
        )
