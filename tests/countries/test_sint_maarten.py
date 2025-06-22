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

from holidays.countries.sint_maarten import SintMaarten, SX, SXM
from tests.common import CommonCountryTests


class TestSintMaarten(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2011, 2050)
        super().setUpClass(SintMaarten, years=years, years_non_observed=years)

    def test_country_aliases(self):
        self.assertAliases(SintMaarten, SX, SXM)

    def test_no_holidays(self):
        self.assertNoHolidays(SintMaarten(years=2010))

    def test_2017(self):
        self.assertHolidays(
            SintMaarten(years=2017),
            ("2017-01-01", "New Year's Day"),
            ("2017-04-14", "Good Friday"),
            ("2017-04-16", "Easter Sunday"),
            ("2017-04-17", "Easter Monday"),
            ("2017-04-27", "King's Day"),
            ("2017-05-02", "Carnival Day"),
            ("2017-05-01", "Labour Day"),
            ("2017-05-25", "Ascension Day"),
            ("2017-06-04", "Whit Sunday"),
            ("2017-07-01", "Emancipation Day"),
            ("2017-10-09", "Constitution Day"),
            ("2017-11-11", "Sint Maarten Day"),
            ("2017-12-25", "Christmas Day"),
            ("2017-12-26", "Second Day of Christmas"),
        )

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(2011, 2050)))

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
        self.assertHolidayName(name, range(2011, 2050))

    def test_easter_sunday(self):
        name = "Easter Sunday"
        self.assertHolidayName(
            name,
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, range(2011, 2050))

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
        self.assertHolidayName(name, range(2011, 2050))

    def test_kings_day(self):
        name_queen = "Queen's Day"
        name_king = "King's Day"
        self.assertHolidayName(name_queen, (f"{year}-04-30" for year in range(2012, 2014)))
        self.assertHolidayName(
            name_king,
            "2014-04-26",
            "2015-04-27",
            "2017-04-27",
            "2019-04-27",
            "2020-04-27",
            "2024-04-27",
            "2025-04-26",
        )
        self.assertHolidayName(name_king, range(2014, 2050))
        self.assertNoHolidayName(name_queen, range(2014, 2050))
        self.assertNoHolidayName(name_king, range(2011, 2014))
        # No Sunday Observances.
        self.assertNoHoliday(
            "2014-04-27",
            "2025-04-27",
        )

    def test_carnival_day(self):
        name = "Carnival Day"
        self.assertHolidayName(
            name,
            "2013-04-29",
            "2020-04-30",
            "2021-04-30",
            "2022-04-29",
            "2023-05-02",
            "2024-04-30",
            "2025-04-30",
        )
        self.assertHolidayName(name, range(2011, 2050))

    def test_labor_day(self):
        self.assertHolidayName("Labour Day", (f"{year}-05-01" for year in range(2011, 2050)))

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
        self.assertHolidayName(name, range(2011, 2050))

    def test_whit_sunday(self):
        name = "Whit Sunday"
        self.assertHolidayName(
            name,
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
            "2025-06-08",
        )
        self.assertHolidayName(name, range(2011, 2050))

    def test_emancipation_day(self):
        name = "Emancipation Day"
        self.assertNoHolidayName(name, range(2011, 2012))  # Started 2012
        self.assertHolidayName(name, "2012-07-02")
        self.assertHolidayName(name, (f"{year}-07-01" for year in range(2013, 2018)))
        self.assertHolidayName(name, "2018-07-02")
        self.assertHolidayName(name, (f"{year}-07-01" for year in range(2020, 2025)))

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertNoHolidayName(name, range(2011, 2015))
        self.assertHolidayName(name, range(2015, 2050))
        self.assertHolidayName(
            name,
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
            "2024-10-14",
            "2025-10-13",
        )

    def test_kingdom_day(self):
        name = "Kingdom Day"
        self.assertHolidayName(
            name,
            "2011-12-15",
            "2012-12-15",
            "2013-12-16",
            "2014-12-15",
        )
        self.assertNoHolidayName(name, range(2015, 2050))

    def test_sint_maarten_day(self):
        self.assertHolidayName("Sint Maarten Day", (f"{year}-11-11" for year in range(2011, 2050)))

    def test_christmas(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(2011, 2050)))
        self.assertHolidayName(
            "Second Day of Christmas", (f"{year}-12-26" for year in range(2011, 2050))
        )
