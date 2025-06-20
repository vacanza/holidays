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

from datetime import date, timedelta
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
            "2011-04-22",
            "2012-04-06",
            "2013-03-29",
            "2014-04-18",
            "2015-04-03",
            "2016-03-25",
        )
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
            "2011-04-24",
            "2012-04-08",
            "2013-03-31",
            "2014-04-20",
            "2015-04-05",
            "2016-03-27",
        )
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
            "2011-04-25",
            "2012-04-09",
            "2013-04-01",
            "2014-04-21",
            "2015-04-06",
            "2016-03-28",
        )
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
        name = "King's Day"
        self.assertNoHolidayName(name, range(1900, 2014))
        self.assertHolidayName(
            name,
            "2014-04-26",  # Sunday, observed on Saturday
            "2015-04-27",  # Monday
            "2017-04-27",  # Thursday
            "2019-04-27",  # Saturday
            "2020-04-27",  # Monday
            "2024-04-27",  # Saturday
            "2025-04-26",  # Sunday, observed on Saturday
        )
        self.assertNoHoliday(
            "2013-04-27",  # No King's Day
            "2014-04-27",  # No Sunday observance
            "2025-04-27",  # No Sunday observance
        )

    def test_kings_day_shifted_sunday(self):
        name = "King's Day"
        self.assertHolidayName(name, "2014-04-26")  # 2014: April 27 is Sunday
        self.assertHolidayName(name, "2025-04-26")  # 2025: April 27 is Sunday
        self.assertNoHoliday("2014-04-27")
        self.assertNoHoliday("2025-04-27")

    def test_carnival_day(self):
        name = "Carnival Day"
        self.assertHolidayName(
            name,
            "2014-04-30",
            "2015-04-30",
            "2016-04-29",
            "2017-05-02",
            "2018-04-30",
            "2019-04-30",
        )
        self.assertHolidayName(
            name,
            "2020-04-30",
            "2021-04-30",
            "2022-04-29",
            "2023-05-02",
            "2024-04-30",
            "2025-04-30",
        )
        self.assertHolidayName(name, range(2014, 2050))

    def test_labor_day(self):
        self.assertHolidayName("Labour Day", (f"{year}-05-01" for year in range(2011, 2050)))

    def test_ascension_day(self):
        name = "Ascension Day"
        self.assertHolidayName(
            name, "2011-06-02", "2012-05-17", "2013-05-09", "2014-05-29", "2019-05-30"
        )
        self.assertHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
        )
        self.assertHolidayName(name, range(2011, 2050))

    def test_whit_sunday(self):
        name = "Whit Sunday"
        self.assertHolidayName(
            name,
            "2011-06-12",
            "2012-05-27",
            "2013-05-19",
            "2014-06-08",
            "2015-05-24",
        )
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
        self.assertNoHolidayName(name, range(1900, 2012))
        self.assertHolidayName(name, (f"{year}-07-01" for year in range(2012, 2050)))

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertNoHolidayName(name, range(1900, 2015))
        second_monday_dates = {
            2015: "2015-10-12",
            2017: "2017-10-09",
            2018: "2018-10-08",
            2019: "2019-10-14",
            2020: "2020-10-12",
            2025: "2025-10-13",
        }
        for year, date_str in second_monday_dates.items():
            self.assertHolidayName(name, date_str)
        for year in range(2015, 2050):
            base_date = date(year, 10, 1)
            second_monday = base_date + timedelta(days=(7 - base_date.weekday()) % 7 + 7)
            self.assertHolidayName(name, second_monday)

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
