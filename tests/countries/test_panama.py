#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.panama import Panama, PA, PAN
from tests.common import CommonCountryTests


class TestPanama(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Panama, years=range(1950, 2050))

    def test_country_aliases(self):
        self.assertAliases(Panama, PA, PAN)

    def test_new_year_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1950, 2050))

    def test_martyrs_day(self):
        self.assertHoliday(f"{year}-01-09" for year in range(1950, 2050))

    def test_labour_day(self):
        self.assertHoliday(f"{year}-05-01" for year in range(1950, 2050))

    def test_separation_day(self):
        self.assertHoliday(f"{year}-11-03" for year in range(1950, 2050))

    def test_national_symbols_day(self):
        self.assertHoliday(f"{year}-11-04" for year in range(1950, 2050))

    def test_colon_day(self):
        self.assertHoliday(f"{year}-11-05" for year in range(1950, 2050))

    def test_los_santos_uprising_day(self):
        self.assertHoliday(f"{year}-11-10" for year in range(1950, 2050))

    def test_independence_day(self):
        self.assertHoliday(f"{year}-11-28" for year in range(1950, 2050))

    def test_mothers_day(self):
        self.assertHoliday(f"{year}-12-08" for year in range(1950, 2050))

    def test_national_mourning_day(self):
        self.assertHoliday(f"{year}-12-20" for year in range(2022, 2050))
        self.assertNoHoliday(f"{year}-12-20" for year in range(1950, 2022))
        self.assertNoHolidayName("National Mourning Day", range(1950, 2022))

    def test_christmas_day(self):
        self.assertHoliday(f"{year}-12-25" for year in range(1950, 2050))

    def test_observed(self):
        observed_holidays = (
            "2011-01-10",
            "2011-05-02",
            "2011-12-26",
            "2012-01-02",
            "2013-12-09",
            "2016-05-02",
            "2016-12-26",
            "2017-01-02",
            "2019-12-09",
            "2021-11-29",
            "2022-01-10",
            "2022-05-02",
            "2022-12-26",
            "2023-01-02",
        )
        self.assertHoliday(observed_holidays)
        self.assertNoNonObservedHoliday(observed_holidays)

    def test_2022(self):
        self.assertHolidays(
            Panama(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-01-09", "Martyrs' Day"),
            ("2022-01-10", "Martyrs' Day (observed)"),
            ("2022-03-01", "Carnival"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Labour Day (observed)"),
            ("2022-11-03", "Separation Day"),
            ("2022-11-04", "National Symbols Day"),
            ("2022-11-05", "Colon Day"),
            ("2022-11-10", "Los Santos Uprising Day"),
            ("2022-11-28", "Independence Day"),
            ("2022-12-08", "Mother's Day"),
            ("2022-12-20", "National Mourning Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )

    def test_2023(self):
        self.assertHolidays(
            Panama(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-09", "Martyrs' Day"),
            ("2023-02-21", "Carnival"),
            ("2023-04-07", "Good Friday"),
            ("2023-05-01", "Labour Day"),
            ("2023-11-03", "Separation Day"),
            ("2023-11-04", "National Symbols Day"),
            ("2023-11-05", "Colon Day"),
            ("2023-11-10", "Los Santos Uprising Day"),
            ("2023-11-28", "Independence Day"),
            ("2023-12-08", "Mother's Day"),
            ("2023-12-20", "National Mourning Day"),
            ("2023-12-25", "Christmas Day"),
        )
