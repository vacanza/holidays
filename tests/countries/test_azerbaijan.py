#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.countries.azerbaijan import Azerbaijan, AZ, AZE
from tests.common import TestCase


class TestAzerbaijan(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Azerbaijan, years=range(1990, 2050))

    def test_country_aliases(self):
        self.assertCountryAliases(Azerbaijan, AZ, AZE)

    def test_no_holidays(self):
        self.assertNoHolidays(Azerbaijan(years=1989))

    def test_new_year(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1990, 2050))
        self.assertHoliday(f"{year}-01-02" for year in range(2006, 2050))
        self.assertNoHoliday(f"{year}-01-02" for year in range(1990, 2006))

    def test_black_january(self):
        self.assertHoliday(f"{year}-01-20" for year in range(2000, 2050))
        self.assertNoHoliday(f"{year}-01-20" for year in range(1990, 2000))
        self.assertNoHolidayName("Black January", range(1990, 2000))

    def test_int_women_day(self):
        self.assertHoliday(f"{year}-03-08" for year in range(1990, 2050))

    def test_novruz(self):
        for year in range(2007, 2050):
            self.assertHoliday(
                f"{year}-03-20",
                f"{year}-03-21",
                f"{year}-03-22",
                f"{year}-03-23",
                f"{year}-03-24",
            )
        self.assertNoHolidayName("Novruz", range(1990, 2007))

    def test_victory_day_may(self):
        self.assertHoliday(f"{year}-05-09" for year in range(1990, 2050))

    def test_republic_day(self):
        self.assertHoliday(f"{year}-05-28" for year in range(1992, 2050))
        self.assertNoHoliday(f"{year}-05-28" for year in range(1990, 1992))
        self.assertHolidayName("Republic Day", (f"{year}-05-28" for year in range(1992, 2021)))
        self.assertHolidayName("Independence Day", (f"{year}-05-28" for year in range(2021, 2050)))

    def test_salvation_day(self):
        self.assertHoliday(f"{year}-06-15" for year in range(1997, 2050))
        self.assertNoHoliday(f"{year}-06-15" for year in range(1990, 1997))

    def test_memorial_day(self):
        self.assertHoliday(f"{year}-09-27" for year in range(2021, 2050))
        self.assertNoHoliday(f"{year}-09-27" for year in range(1990, 2021))

    def test_armed_forces_day(self):
        self.assertHoliday(f"{year}-10-09" for year in range(1992, 1998))
        self.assertHoliday(f"{year}-06-26" for year in range(1998, 2050))
        self.assertNoHoliday(f"{year}-10-09" for year in range(1990, 1992))
        self.assertNoHoliday(f"{year}-06-26" for year in range(1990, 1998))

    def test_victory_day(self):
        self.assertHoliday(f"{year}-11-08" for year in range(2021, 2050))
        for year in range(1990, 2021):
            self.assertNotIn("Victory Day", Azerbaijan(years=year).get_list(f"{year}-11-08"))

    def test_independence_day(self):
        self.assertHoliday(f"{year}-10-18" for year in range(1990, 2006))
        self.assertNoHoliday(f"{year}-10-18" for year in range(2006, 2050))

    def test_flag_day(self):
        self.assertHoliday(f"{year}-11-09" for year in range(2010, 2050))
        self.assertNoHoliday(f"{year}-11-09" for year in range(1990, 2010))

    def test_int_solidarity_day(self):
        self.assertHoliday(f"{year}-12-31" for year in range(1993, 2050))
        self.assertNoHoliday(f"{year}-12-31" for year in range(1990, 1993))

    def test_hijri_based(self):
        # Ramazan Bayrami
        for dt in (
            "2020-05-24",
            "2020-05-25",
            "2021-05-13",
            "2021-05-14",
            "2022-05-02",
            "2022-05-03",
        ):
            self.assertIn("Ramazan Bayrami", self.holidays[dt])

        # Gurban Bayrami
        for dt in (
            "2006-01-10",
            "2006-01-11",
            "2006-12-31",
            "2020-07-31",
            "2020-08-01",
            "2020-08-03",
            "2021-07-20",
            "2021-07-21",
            "2022-07-09",
            "2022-07-10",
            "2022-07-11",
            "2022-07-12",
        ):
            self.assertIn("Gurban Bayrami", self.holidays[dt])

    def test_observed_days(self):
        observed_holidays = (
            "2020-03-09",
            "2020-03-25",
            "2020-03-26",
            "2020-05-11",
            "2020-05-26",
            "2020-08-03",
            "2021-01-04",
            "2021-03-25",
            "2021-03-26",
            "2021-05-10",
            "2021-06-28",
            "2022-01-03",
            "2022-01-04",
            "2022-03-25",
            "2022-05-30",
            "2022-06-27",
            "2022-07-11",
            "2022-07-12",
            # special cases
            "2007-01-03",
            "2072-01-05",
        )
        self.assertHoliday(observed_holidays)
        self.assertNoNonObservedHoliday(observed_holidays)

    def test_2020(self):
        self.assertHolidayDates(
            Azerbaijan(years=2020),
            "2020-01-01",
            "2020-01-02",
            "2020-01-20",
            "2020-03-08",
            "2020-03-09",
            "2020-03-20",
            "2020-03-21",
            "2020-03-22",
            "2020-03-23",
            "2020-03-24",
            "2020-03-25",
            "2020-03-26",
            "2020-05-09",
            "2020-05-11",
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            "2020-05-28",
            "2020-06-15",
            "2020-06-26",
            "2020-07-31",
            "2020-08-01",
            "2020-08-03",
            "2020-11-09",
            "2020-12-31",
        )

    def test_2022(self):
        self.assertHolidayDates(
            Azerbaijan(years=2022),
            "2022-01-01",
            "2022-01-02",
            "2022-01-03",
            "2022-01-04",
            "2022-01-20",
            "2022-03-08",
            "2022-03-20",
            "2022-03-21",
            "2022-03-22",
            "2022-03-23",
            "2022-03-24",
            "2022-03-25",
            "2022-05-02",
            "2022-05-03",
            "2022-05-09",
            "2022-05-28",
            "2022-05-30",
            "2022-06-15",
            "2022-06-26",
            "2022-06-27",
            "2022-07-09",
            "2022-07-10",
            "2022-07-11",
            "2022-07-12",
            "2022-09-27",
            "2022-11-08",
            "2022-11-09",
            "2022-12-31",
        )
