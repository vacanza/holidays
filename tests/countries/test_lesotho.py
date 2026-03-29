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

from holidays.countries.lesotho import Lesotho
from tests.common import CommonCountryTests


class TestLesotho(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Lesotho)

    def test_special_holidays(self):
        self.assertHoliday("2002-05-25")

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in self.full_range))

    def test_moshoeshoes_day(self):
        self.assertHolidayName("Moshoeshoe's Day", (f"{year}-03-11" for year in self.full_range))

    def test_heroes_day(self):
        name = "Heroes Day"
        self.assertHolidayName(name, (f"{year}-04-04" for year in range(self.start_year, 2003)))
        self.assertNoHolidayName(name, range(2003, self.end_year))

    def test_africa_heroes_day(self):
        name = "Africa/Heroes Day"
        self.assertHolidayName(name, (f"{year}-05-25" for year in range(2003, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2003))

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

    def test_workers_day(self):
        self.assertHolidayName("Workers' Day", (f"{year}-05-01" for year in self.full_range))

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

    def test_kings_birthday(self):
        name = "King's Birthday"
        self.assertHolidayName(
            name,
            (f"{year}-05-02" for year in range(self.start_year, 1998)),
            (f"{year}-07-17" for year in range(1998, self.end_year)),
        )

    def test_independence_day(self):
        self.assertHolidayName("Independence Day", (f"{year}-10-04" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in self.full_range))

    def test_boxing_day(self):
        self.assertHolidayName("Boxing Day", (f"{year}-12-26" for year in self.full_range))

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "New Year's Day"),
            ("2022-03-11", "Moshoeshoe's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Workers' Day"),
            ("2022-05-25", "Africa/Heroes Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-07-17", "King's Birthday"),
            ("2022-10-04", "Independence Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
        )
