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

from holidays.countries.fiji import Fiji
from tests.common import CommonCountryTests


class TestFiji(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Fiji)

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoWorkdayHoliday(range(self.start_year, 2023))

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))

        dt_obs = (
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt_obs)
        self.assertNoNonObservedHoliday(dt_obs)

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

    def test_girmit_day(self):
        name = "Girmit Day"
        self.assertHolidayName(
            name,
            "2023-05-15",
            "2024-05-13",
            "2025-05-12",
        )
        self.assertHolidayName(name, range(2023, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2023))

    def test_national_sports_day(self):
        name = "National Sports Day"
        self.assertHolidayName(
            name,
            "2016-06-24",
            "2017-06-30",
            "2018-06-29",
        )
        self.assertNoHolidayName(name, range(2019, self.end_year))

    def test_constitution_day(self):
        name = "Constitution Day"

        # Public Holidays
        self.assertHolidayName(name, (f"{year}-09-07" for year in range(self.start_year, 2023)))
        self.assertNoHolidayName(name, range(2023, self.end_year))

        dt_obs = ("2019-09-09",)
        self.assertHolidayName(f"{name} (observed)", dt_obs)
        self.assertNoNonObservedHoliday(dt_obs)

        # Workdays.
        self.assertWorkdayHolidayName(
            name, (f"{year}-09-07" for year in range(2023, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2023))

    def test_ratu_sir_lala_sukuna_day(self):
        name = "Ratu Sir Lala Sukuna Day"
        self.assertHolidayName(
            name,
            "2023-05-29",
            "2024-05-31",
            "2025-05-30",
        )
        self.assertHolidayName(name, range(2023, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2023))

    def test_fiji_day(self):
        self.assertHolidayName("Fiji Day", (f"{year}-10-10" for year in self.full_range))

    def test_diwali(self):
        name = "Diwali"
        self.assertHolidayName(
            name,
            "2016-10-31",
            "2017-10-19",
            "2018-11-07",
            "2019-10-28",
            "2020-11-14",
            "2021-11-04",
            "2022-10-25",
            "2023-11-13",
            "2024-11-01",
            "2025-10-21",
        )

        dt_obs = ("2020-11-16",)
        self.assertHolidayName(f"{name} (observed)", dt_obs)
        self.assertNoNonObservedHoliday(dt_obs)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))

        dt_obs = (
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", dt_obs)
        self.assertNoNonObservedHoliday(dt_obs)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))

        dt_obs = (
            "2020-12-28",
            "2021-12-28",
            "2026-12-28",
            "2027-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", dt_obs)
        self.assertNoNonObservedHoliday(dt_obs)

    def test_prophets_birthday(self):
        name = "Prophet Mohammed's Birthday"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-10-31",
            "2021-10-18",
            "2022-10-07",
            "2023-09-30",
            "2024-09-16",
            "2025-09-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

        dt_obs = (
            "2019-11-11",
            "2020-11-02",
            "2023-10-02",
            "2025-09-08",
        )
        self.assertHolidayName(f"{name} (observed)", dt_obs)
        self.assertNoNonObservedHoliday(dt_obs)

    def test_2019(self):
        # https://web.archive.org/web/20191018023027/https://www.fiji.gov.fj/About-Fiji/Public-Holidays
        self.assertHolidaysInYear(
            2019,
            ("2019-01-01", "New Year's Day"),
            ("2019-04-19", "Good Friday"),
            ("2019-04-20", "Easter Saturday"),
            ("2019-04-22", "Easter Monday"),
            ("2019-09-07", "Constitution Day"),
            ("2019-09-09", "Constitution Day (observed)"),
            ("2019-10-10", "Fiji Day"),
            ("2019-10-28", "Diwali"),
            ("2019-11-09", "Prophet Mohammed's Birthday"),
            ("2019-11-11", "Prophet Mohammed's Birthday (observed)"),
            ("2019-12-25", "Christmas Day"),
            ("2019-12-26", "Boxing Day"),
        )

    def test_2020(self):
        # https://web.archive.org/web/20210103183942/https://www.fiji.gov.fj/About-Fiji/Public-Holidays
        self.assertHolidaysInYear(
            2020,
            ("2020-01-01", "New Year's Day"),
            ("2020-04-10", "Good Friday"),
            ("2020-04-11", "Easter Saturday"),
            ("2020-04-13", "Easter Monday"),
            ("2020-09-07", "Constitution Day"),
            ("2020-10-10", "Fiji Day"),
            ("2020-10-31", "Prophet Mohammed's Birthday"),
            ("2020-11-02", "Prophet Mohammed's Birthday (observed)"),
            ("2020-11-14", "Diwali"),
            ("2020-11-16", "Diwali (observed)"),
            ("2020-12-25", "Christmas Day"),
            ("2020-12-26", "Boxing Day"),
            ("2020-12-28", "Boxing Day (observed)"),
        )

    def test_2021(self):
        # https://web.archive.org/web/20221223004409/https://www.fiji.gov.fj/About-Fiji/Public-Holidays
        self.assertHolidaysInYear(
            2021,
            ("2021-01-01", "New Year's Day"),
            ("2021-04-02", "Good Friday"),
            ("2021-04-03", "Easter Saturday"),
            ("2021-04-05", "Easter Monday"),
            ("2021-09-07", "Constitution Day"),
            ("2021-10-10", "Fiji Day"),
            ("2021-10-18", "Prophet Mohammed's Birthday"),
            ("2021-11-04", "Diwali"),
            ("2021-12-25", "Christmas Day"),
            ("2021-12-26", "Boxing Day"),
            ("2021-12-27", "Christmas Day (observed)"),
            ("2021-12-28", "Boxing Day (observed)"),
        )

    def test_2022(self):
        # https://web.archive.org/web/20221223004409/https://www.fiji.gov.fj/About-Fiji/Public-Holidays
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-16", "Easter Saturday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-09-07", "Constitution Day"),
            ("2022-10-07", "Prophet Mohammed's Birthday"),
            ("2022-10-10", "Fiji Day"),
            ("2022-10-25", "Diwali"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_2023(self):
        # https://web.archive.org/web/20231129154609/https://www.fiji.gov.fj/About-Fiji/Public-Holidays
        self.assertHolidaysInYear(
            2023,
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-08", "Easter Saturday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-15", "Girmit Day"),
            ("2023-05-29", "Ratu Sir Lala Sukuna Day"),
            ("2023-09-30", "Prophet Mohammed's Birthday"),
            ("2023-10-02", "Prophet Mohammed's Birthday (observed)"),
            ("2023-10-10", "Fiji Day"),
            ("2023-11-13", "Diwali"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_2024(self):
        # https://web.archive.org/web/20250121185434/https://www.fiji.gov.fj/About-Fiji/Public-Holidays
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "Easter Saturday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-13", "Girmit Day"),
            ("2024-05-31", "Ratu Sir Lala Sukuna Day"),
            ("2024-09-16", "Prophet Mohammed's Birthday"),
            ("2024-10-10", "Fiji Day"),
            ("2024-11-01", "Diwali"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_2025(self):
        # https://web.archive.org/web/20250121185434/https://www.fiji.gov.fj/About-Fiji/Public-Holidays
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "New Year's Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-19", "Easter Saturday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-12", "Girmit Day"),
            ("2025-05-30", "Ratu Sir Lala Sukuna Day"),
            ("2025-09-06", "Prophet Mohammed's Birthday"),
            ("2025-09-08", "Prophet Mohammed's Birthday (observed)"),
            ("2025-10-10", "Fiji Day"),
            ("2025-10-21", "Diwali"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )
