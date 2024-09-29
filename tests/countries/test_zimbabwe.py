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

from holidays.countries.zimbabwe import Zimbabwe, ZW, ZWE
from tests.common import CommonCountryTests


class TestZimbabwe(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Zimbabwe, years=range(1988, 2050))

    def test_country_aliases(self):
        self.assertAliases(Zimbabwe, ZW, ZWE)

    def test_no_holidays(self):
        self.assertNoHolidays(Zimbabwe(years=1987))

    def test_holidays(self):
        for year in range(1988, 2050):
            self.assertHoliday(
                f"{year}-01-01",
                f"{year}-04-18",
                f"{year}-05-01",
                f"{year}-05-25",
                f"{year}-12-22",
                f"{year}-12-25",
                f"{year}-12-26",
            )

        self.assertNoHoliday(f"{year}-02-21" for year in range(1988, 2018))
        self.assertNoHolidayName("Robert Gabriel Mugabe National Youth Day", range(1988, 2018))
        self.assertHoliday(f"{year}-02-21" for year in range(2018, 2050))

    def test_easter(self):
        self.assertHoliday(
            # Good Friday
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            # Holy Saturday
            "2018-03-31",
            "2019-04-20",
            "2020-04-11",
            "2021-04-03",
            "2022-04-16",
            # Easter Monday
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
        )

    def test_moving_holidays(self):
        self.assertHoliday(
            # Zimbabwe Heroes' Day
            "2018-08-13",
            "2019-08-12",
            "2020-08-10",
            "2021-08-09",
            "2022-08-08",
            # Defense Forces Day
            "2018-08-14",
            "2019-08-13",
            "2020-08-11",
            "2021-08-10",
            "2022-08-09",
        )

    def test_observed(self):
        dt = (
            "2002-12-23",
            "2003-05-26",
            "2004-04-19",
            "2004-12-27",
            "2005-05-02",
            "2005-12-27",
            "2006-01-02",
            "2008-05-26",
            "2010-04-19",
            "2010-12-27",
            "2011-05-02",
            "2011-12-27",
            "2012-01-02",
            "2013-12-23",
            "2014-05-26",
            "2016-05-02",
            "2016-12-27",
            "2017-01-02",
            "2019-12-23",
            "2021-02-22",
            "2021-04-19",
            "2021-12-27",
            "2022-05-02",
            "2022-12-27",
            "2023-01-02",
            "2024-12-23",
            "2027-02-22",
            # special cases
            "2049-04-20",
            "2055-04-20",
            "2060-04-20",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_2022(self):
        self.assertHolidays(
            Zimbabwe(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-02-21", "Robert Gabriel Mugabe National Youth Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-16", "Easter Saturday"),
            ("2022-04-18", "Easter Monday; Independence Day"),
            ("2022-05-01", "Workers' Day"),
            ("2022-05-02", "Workers' Day (observed)"),
            ("2022-05-25", "Africa Day"),
            ("2022-08-08", "Zimbabwe Heroes' Day"),
            ("2022-08-09", "Defense Forces Day"),
            ("2022-12-22", "Unity Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )
