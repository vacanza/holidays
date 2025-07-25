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

from holidays.constants import GOVERNMENT, WORKDAY
from holidays.countries.pitcairn_islands import PitcairnIslands, PN, PCN
from tests.common import CommonCountryTests


class TestPitcairnIslands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2016, 2050)
        super().setUpClass(PitcairnIslands, years=years)
        cls.government_holidays = PitcairnIslands(categories=GOVERNMENT, years=years)
        cls.workday_holidays = PitcairnIslands(categories=WORKDAY, years=years)

    def test_country_aliases(self):
        self.assertAliases(PitcairnIslands, PN, PCN)

    def test_no_holidays(self):
        self.assertNoHolidays(PitcairnIslands(years=2015))

    def test_new_years_day(self):
        name = "New Year's Day"
        # Public Holidays.
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(2016, 2050)))
        # Government Holidays.
        self.assertHolidayName(
            name, self.government_holidays, (f"{year}-01-02" for year in range(2016, 2050))
        )
        self.assertNoHolidayName(name, (f"{year}-01-02" for year in range(2016, 2050)))

    def test_bounty_day(self):
        self.assertHolidayName("Bounty Day", (f"{year}-01-23" for year in range(2016, 2050)))

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
        self.assertHolidayName(name, range(2016, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, range(2016, 2050))

    def test_queens_birthday(self):
        name = "Queen's Birthday"
        self.assertHolidayName(
            name,
            "2016-06-11",
            "2017-06-10",
            "2018-06-09",
            "2019-06-08",
            "2020-06-13",
            "2021-06-12",
            "2022-06-11",
        )
        self.assertNoHolidayName(name, range(2023, 2050))

    def test_kings_birthday(self):
        name = "King's Birthday"
        self.assertHolidayName(
            name,
            "2023-06-05",
            "2024-06-03",
            "2025-06-02",
        )
        self.assertHolidayName(name, range(2023, 2050))
        self.assertNoHolidayName(name, range(2016, 2023))

    def test_pitcairn_day(self):
        self.assertHolidayName("Pitcairn Day", (f"{year}-07-02" for year in range(2016, 2050)))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(2016, 2050)))

    def test_boxing_day(self):
        self.assertHolidayName("Boxing Day", (f"{year}-12-26" for year in range(2016, 2050)))

    def test_anzac_day(self):
        name = "ANZAC Day"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-04-25" for year in range(2016, 2050))
        )

    def test_remembrance_day(self):
        name = "Remembrance Day"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-11-11" for year in range(2016, 2050))
        )

    def test_2022_public(self):
        self.assertHolidays(
            PitcairnIslands(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-01-23", "Bounty Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-06-11", "Queen's Birthday"),
            ("2022-07-02", "Pitcairn Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
        )

    def test_2022_government(self):
        self.assertHolidays(
            PitcairnIslands(categories=GOVERNMENT, years=2022), ("2022-01-02", "New Year's Day")
        )

    def test_2022_workday(self):
        self.assertHolidays(
            PitcairnIslands(categories=WORKDAY, years=2022),
            ("2022-04-25", "ANZAC Day"),
            ("2022-11-11", "Remembrance Day"),
        )
