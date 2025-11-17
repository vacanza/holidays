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

from holidays.countries.saint_vincent_and_the_grenadines import (
    SaintVincentAndTheGrenadines,
)
from tests.common import CommonCountryTests


class TestSaintVincentAndTheGrenadines(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1979, 2050)
        super().setUpClass(SaintVincentAndTheGrenadines, years=years, years_non_observed=years)

    def test_special_holidays(self):
        self.assertHolidayName("Public Health Holiday", "2021-01-22", "2021-01-25")

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1979, 2050)))
        obs_dt = (
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_national_heroes_day(self):
        name = "National Heroes' Day"
        self.assertHolidayName(name, (f"{year}-03-14" for year in range(1979, 2050)))
        obs_dt = (
            "2004-03-15",
            "2010-03-15",
            "2021-03-15",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

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
        self.assertHolidayName(name, range(1979, 2050))

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
        self.assertHolidayName(name, range(1979, 2050))

    def test_national_workers_day(self):
        name = "National Workers' Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1979, 2050)))
        obs_dt = (
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_spiritual_baptist_day(self):
        name = "National Spiritual Baptist Day"
        self.assertHolidayName(name, (f"{year}-05-21" for year in range(2025, 2050)))
        self.assertNoHolidayName(name, range(1979, 2025))

    def test_whit_monday(self):
        name = "Whit Monday"
        self.assertHolidayName(
            name,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, range(1979, 2050))

    def test_carnival_monday(self):
        name = "Carnival Monday"
        self.assertHolidayName(
            name,
            "2020-08-03",
            "2021-09-06",
            "2022-07-04",
            "2023-07-10",
            "2024-07-08",
            "2025-07-07",
        )
        self.assertHolidayName(name, range(1979, 2050))

    def test_carnival_tuesday(self):
        name = "Carnival Tuesday"
        self.assertHolidayName(
            name,
            "2020-08-04",
            "2021-09-07",
            "2022-07-05",
            "2023-07-11",
            "2024-07-09",
            "2025-07-08",
        )
        self.assertHolidayName(name, range(1979, 2050))

    def test_emancipation_day(self):
        name = "Emancipation Day"
        self.assertHolidayName(name, (f"{year}-08-01" for year in range(1979, 2050)))
        obs_dt = (
            "2004-08-02",
            "2010-08-02",
            "2021-08-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-10-27" for year in range(1979, 2050)))
        obs_dt = (
            "2002-10-28",
            "2013-10-28",
            "2019-10-28",
            "2024-10-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1979, 2050)))
        obs_dt = (
            "2005-12-27",
            "2011-12-27",
            "2016-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1979, 2050)))
        obs_dt = (
            "2004-12-27",
            "2010-12-27",
            "2021-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_2024_holidays(self):
        self.assertHolidays(
            SaintVincentAndTheGrenadines(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-03-14", "National Heroes' Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-01", "National Workers' Day"),
            ("2024-05-20", "Whit Monday"),
            ("2024-07-08", "Carnival Monday"),
            ("2024-07-09", "Carnival Tuesday"),
            ("2024-08-01", "Emancipation Day"),
            ("2024-10-27", "Independence Day"),
            ("2024-10-28", "Independence Day (observed)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-03-14", "National Heroes' Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "National Workers' Day"),
            ("2025-05-21", "National Spiritual Baptist Day"),
            ("2025-06-09", "Whit Monday"),
            ("2025-07-07", "Carnival Monday"),
            ("2025-07-08", "Carnival Tuesday"),
            ("2025-08-01", "Emancipation Day"),
            ("2025-10-27", "Independence Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-03-14", "National Heroes' Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "National Workers' Day"),
            ("2025-05-21", "National Spiritual Baptist Day"),
            ("2025-06-09", "Whit Monday"),
            ("2025-07-07", "Carnival Monday"),
            ("2025-07-08", "Carnival Tuesday"),
            ("2025-08-01", "Emancipation Day"),
            ("2025-10-27", "Independence Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )
