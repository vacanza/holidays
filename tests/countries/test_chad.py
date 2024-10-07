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

from holidays.countries.chad import Chad, TD, TCD
from tests.common import CommonCountryTests


class TestChad(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Chad)

    def test_country_aliases(self):
        self.assertAliases(Chad, TD, TCD)

    def test_no_holidays(self):
        self.assertNoHolidays(Chad(years=1960))

    def test_special_holidays(self):
        self.assertHoliday("2021-04-23")

    def test_freedom_and_democracy_day(self):
        name = "Freedom and Democracy Day"
        self.assertHolidayName(name, (f"{year}-12-01" for year in range(1991, 2050)))
        self.assertNoHolidayName(name, Chad(years=range(1961, 1991)))
        self.assertNoHoliday(f"{year}-12-01" for year in set(range(1961, 1991)).difference({1976}))

    def test_observed(self):
        dt = (
            # New Year's Day
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
            # International Women's Day
            "2015-03-09",
            "2020-03-09",
            # Labour Day
            "2011-05-02",
            "2016-05-02",
            # Independence Day
            "2013-08-12",
            "2019-08-12",
            # Republic Day
            "2010-11-29",
            "2021-11-29",
            # Freedom and Democracy Day
            "2013-12-02",
            "2019-12-02",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-03-08", "International Women's Day"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Eid al-Fitr; Labour Day (observed)"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-08-11", "Independence Day"),
            ("2022-10-08", "Mawlid"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-28", "Republic Day"),
            ("2022-12-01", "Freedom and Democracy Day"),
            ("2022-12-25", "Christmas Day"),
        )
