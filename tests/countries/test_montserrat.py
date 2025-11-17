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

from holidays.countries.montserrat import Montserrat
from tests.common import CommonCountryTests


class TestMontserrat(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2017, 2050)
        super().setUpClass(Montserrat, years=years, years_non_observed=years)

    def test_special_holidays(self):
        self.assertHolidayName(
            "Special Public Holiday",
            "2018-09-14",
            "2019-05-10",
            "2020-07-15",
            "2023-04-12",
        )

        for dt, name in (
            ("2022-06-03", "Platinum Jubilee of Elizabeth II"),
            ("2022-09-19", "National Day of Mourning"),
            ("2023-05-06", "Coronation of King Charles III"),
        ):
            self.assertHolidayName(name, dt)

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(2017, 2050)))
        obs_dt = (
            "2017-01-03",
            "2018-01-02",
            "2022-01-03",
            "2023-01-03",
            "2024-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_saint_patricks_day(self):
        name = "Saint Patrick's Day"
        self.assertHolidayName(name, (f"{year}-03-17" for year in range(2017, 2050)))
        obs_dt = (
            "2018-03-19",
            "2019-03-18",
            "2024-03-18",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_good_friday(self):
        name = "Good Friday"
        dts = (
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(2017, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        dts = (
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(2017, 2050))

    def test_labor_day(self):
        name = "Labour Day"
        dts = (
            "2022-05-02",
            "2023-05-01",
            "2024-05-06",
            "2025-05-05",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(2017, 2050))

    def test_queens_birthday(self):
        name = "Queen's Birthday"
        dts = (
            "2019-06-10",
            "2020-06-15",
            "2021-06-14",
            "2022-06-02",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(2017, 2023))
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
        self.assertNoHolidayName(name, range(2017, 2023))

    def test_whit_monday(self):
        name = "Whit Monday"
        dts = (
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, dts)
        obs_dt = ("2019-06-11",)
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_day_of_prayer_and_thanksgiving(self):
        first_name = "National Day of Prayer and Thanksgiving"
        self.assertHolidayName(
            first_name,
            "2021-07-21",
            "2022-07-20",
            "2023-07-12",
        )
        self.assertNoHolidayName(first_name, range(2017, 2021), range(2024, 2050))
        second_name = "Day of Prayer and Thanksgiving"
        self.assertHolidayName(
            second_name,
            "2024-07-10",
            "2025-07-09",
        )
        self.assertHolidayName(second_name, range(2024, 2050))
        self.assertNoHolidayName(second_name, range(2017, 2024))

    def test_emancipation_day(self):
        name = "Emancipation Day"
        dts = (
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
            "2025-08-04",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, range(2017, 2050))

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(2017, 2050)))
        obs_dt = (
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(2017, 2050)))
        obs_dt = (
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_festival_day(self):
        name = "Festival Day"
        self.assertHolidayName(name, (f"{year}-12-31" for year in range(2017, 2050)))
        obs_dt = (
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-01-02", "New Year's Day (observed)"),
            ("2024-03-17", "Saint Patrick's Day"),
            ("2024-03-18", "Saint Patrick's Day (observed)"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-06", "Labour Day"),
            ("2024-05-20", "Whit Monday"),
            ("2024-06-17", "King's Birthday"),
            ("2024-07-10", "Day of Prayer and Thanksgiving"),
            ("2024-08-05", "Emancipation Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
            ("2024-12-31", "Festival Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-02", "New Year's Day (observed)"),
            ("2024-03-17", "Saint Patrick's Day"),
            ("2024-03-18", "Saint Patrick's Day (observed)"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-06", "Labor Day"),
            ("2024-05-20", "Whit Monday"),
            ("2024-06-17", "King's Birthday"),
            ("2024-07-10", "Day of Prayer and Thanksgiving"),
            ("2024-08-05", "Emancipation Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
            ("2024-12-31", "Festival Day"),
        )
