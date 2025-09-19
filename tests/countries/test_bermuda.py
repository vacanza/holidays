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

from holidays.countries.bermuda import Bermuda, BM, BMU
from tests.common import CommonCountryTests


class TestBermuda(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Bermuda)

    def test_country_aliases(self):
        self.assertAliases(Bermuda, BM, BMU)

    def test_no_holidays(self):
        self.assertNoHolidays(Bermuda(years=self.start_year - 1))

    def test_special_holidays(self):
        for dt, name in (
            ("2007-06-05", "Public Holiday"),
            ("2019-11-04", "Portuguese Welcome 170th Anniversary"),
            ("2021-10-18", "Flora Duffy Day"),
            ("2023-05-08", "The Coronation of His Majesty King Charles III"),
        ):
            self.assertHolidayName(name, dt)

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        dt = (
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_bermuda_day(self):
        name = "Bermuda Day"
        self.assertHolidayName(name, (f"{year}-05-24" for year in range(self.start_year, 2018)))
        self.assertHolidayName(
            name,
            "2018-05-25",
            "2019-05-24",
            "2020-05-29",
            "2021-05-28",
            "2022-05-27",
            "2023-05-26",
            "2024-05-24",
            "2025-05-23",
        )
        self.assertHolidayName(name, range(2018, self.end_year))

        dt = (
            "2008-05-26",
            "2009-05-25",
            "2014-05-26",
            "2015-05-25",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_queens_birthday(self):
        name = "Queen's Birthday"
        self.assertHolidayName(
            name,
            "1997-06-16",
            "1998-06-15",
            "1999-06-21",
            "2000-06-12",
            "2001-06-11",
            "2006-06-12",
            "2007-06-11",
            "2008-06-16",
        )
        self.assertHolidayName(name, range(self.start_year, 2009))
        self.assertNoHolidayName(name, range(2009, self.end_year))

    def test_national_heroes_day(self):
        name = "National Heroes Day"
        self.assertHolidayName(
            name,
            "2008-10-13",
            "2009-06-15",
            "2010-06-21",
            "2020-06-15",
            "2021-06-21",
            "2022-06-20",
            "2023-06-19",
            "2024-06-17",
            "2025-06-16",
        )
        self.assertHolidayName(name, range(2008, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2008))

    def test_cup_match_and_emancipation_day(self):
        name_1948 = "Cup Match Day"
        self.assertHolidayName(
            name_1948,
            "1995-08-03",
            "1996-08-01",
            "1997-07-31",
            "1998-07-30",
            "1999-07-29",
        )
        self.assertHolidayName(name_1948, range(self.start_year, 2000))
        self.assertNoHolidayName(name_1948, range(2000, self.end_year))

        name_2000 = "Emancipation Day"
        self.assertHolidayName(
            name_2000,
            "2021-07-29",
            "2022-07-28",
            "2023-08-03",
            "2024-08-01",
            "2025-07-31",
        )
        self.assertHolidayName(name_2000, range(2000, self.end_year))
        self.assertNoHolidayName(name_2000, range(self.start_year, 2000))

    def test_somers_and_mary_prince_day(self):
        name_1948 = "Somers Day"
        self.assertHolidayName(
            name_1948,
            "2016-07-29",
            "2017-08-04",
            "2018-08-03",
            "2019-08-02",
        )
        self.assertHolidayName(name_1948, range(self.start_year, 2020))
        self.assertNoHolidayName(name_1948, range(2020, self.end_year))

        name_2020 = "Mary Prince Day"
        self.assertHolidayName(
            name_2020,
            "2020-07-31",
            "2021-07-30",
            "2022-07-29",
            "2023-08-04",
            "2024-08-02",
            "2025-08-01",
        )
        self.assertHolidayName(name_2020, range(2020, self.end_year))
        self.assertNoHolidayName(name_2020, range(self.start_year, 2020))

    def test_labor_day(self):
        name = "Labour Day"
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

    def test_remembrance_day(self):
        name = "Remembrance Day"
        self.assertHolidayName(name, (f"{year}-11-11" for year in self.full_range))

        dt = (
            "2007-11-12",
            "2012-11-12",
            "2017-11-13",
            "2018-11-12",
            "2023-11-13",
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

    def test_boxing_day(self):
        name = "Boxing Day"
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

    def test_2025(self):
        self.assertHolidays(
            Bermuda(years=2025),
            ("2025-01-01", "New Year's Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-05-23", "Bermuda Day"),
            ("2025-06-16", "National Heroes Day"),
            ("2025-07-31", "Emancipation Day"),
            ("2025-08-01", "Mary Prince Day"),
            ("2025-09-01", "Labour Day"),
            ("2025-11-11", "Remembrance Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-05-24", "Bermuda Day"),
            ("2024-06-17", "National Heroes Day"),
            ("2024-08-01", "Emancipation Day"),
            ("2024-08-02", "Mary Prince Day"),
            ("2024-09-02", "Labour Day"),
            ("2024-11-11", "Remembrance Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-05-24", "Bermuda Day"),
            ("2024-06-17", "National Heroes Day"),
            ("2024-08-01", "Emancipation Day"),
            ("2024-08-02", "Mary Prince Day"),
            ("2024-09-02", "Labor Day"),
            ("2024-11-11", "Remembrance Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )
