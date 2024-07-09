#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.entities.ISO_3166.KZ import KzHolidays
from tests.common import CommonCountryTests


class TestKzHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(KzHolidays, years=range(1991, 2050))

    def test_no_holidays(self):
        self.assertNoHolidays(KzHolidays(years=1990))

    def test_new_year(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1991, 2050))
        self.assertHoliday(f"{year}-01-02" for year in range(1991, 2050))

    def test_christmas(self):
        self.assertHoliday(f"{year}-01-07" for year in range(2006, 2050))
        self.assertNoHoliday(f"{year}-01-07" for year in range(1991, 2006))

    def test_womens_day(self):
        self.assertHoliday(f"{year}-03-08" for year in range(1991, 2050))

    def test_nauryz(self):
        for year in range(2010, 2050):
            self.assertHoliday(f"{year}-03-21", f"{year}-03-22", f"{year}-03-23")
        for year in range(1991, 2002):
            self.assertNoHoliday(f"{year}-03-21", f"{year}-03-22", f"{year}-03-23")
        for year in range(2002, 2010):
            self.assertNoNonObservedHoliday(
                KzHolidays(observed=False, years=year),
                f"{year}-03-21",
                f"{year}-03-23",
            )

    def test_solidarity_day(self):
        self.assertHoliday(f"{year}-05-01" for year in range(1991, 2050))

    def test_defenders_day(self):
        self.assertHoliday(f"{year}-05-07" for year in range(2013, 2050))
        self.assertNoHoliday(f"{year}-05-07" for year in range(1991, 2013))

    def test_victory_day(self):
        self.assertHoliday(f"{year}-05-09" for year in range(1991, 2050))

    def test_capital_day(self):
        self.assertHoliday(f"{year}-07-06" for year in range(2009, 2050))
        self.assertNoHoliday(f"{year}-07-06" for year in range(1991, 2009))

    def test_constitution_day(self):
        self.assertHoliday(f"{year}-08-30" for year in range(1996, 2050))
        self.assertNoHoliday(f"{year}-08-30" for year in range(1991, 1996))

    def test_republic_day(self):
        self.assertHoliday(f"{year}-10-25" for year in range(1994, 2009))
        self.assertHoliday(f"{year}-10-25" for year in range(2022, 2050))
        self.assertNoHoliday(f"{year}-10-25" for year in range(1991, 1994))
        self.assertNoHoliday(f"{year}-10-25" for year in range(2009, 2022))

    def test_first_president_day(self):
        self.assertHoliday(f"{year}-12-01" for year in range(2012, 2022))
        self.assertNoHoliday(f"{year}-12-01" for year in range(1991, 2012))
        self.assertNoHoliday(f"{year}-12-01" for year in range(2022, 2050))

    def test_independence_day(self):
        self.assertHoliday(f"{year}-12-16" for year in range(1991, 2050))
        self.assertHoliday(f"{year}-12-17" for year in range(2002, 2022))
        self.assertNoHoliday(f"{year}-12-17" for year in range(1991, 2002))
        for year in range(2022, 2050):
            self.assertNoNonObservedHoliday(
                KzHolidays(observed=False, years=year), f"{year}-12-17"
            )

    def test_kurban_ait(self):
        self.assertHoliday(
            "2006-01-10",
            "2006-12-31",
            "2007-12-20",
            "2008-12-08",
            "2009-11-27",
            "2010-11-16",
            "2011-11-06",
            "2012-10-26",
            "2013-10-15",
            "2014-10-04",
            "2015-09-23",
            "2016-09-11",
            "2017-09-01",
            "2018-08-21",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
        )

    def test_observed(self):
        observed_holidays = (
            "2012-01-03",
            "2012-12-18",
            "2013-03-25",
            "2013-07-08",
            "2013-12-02",
            "2014-03-10",
            "2014-03-24",
            "2014-03-25",
            "2014-07-07",
            "2014-09-01",
            "2015-03-09",
            "2015-03-24",
            "2015-03-25",
            "2015-05-11",
            "2015-08-31",
            "2016-01-04",
            "2016-05-02",
            "2016-05-10",
            "2016-12-19",
            "2017-01-03",
            "2017-05-08",
            "2017-12-18",
            "2017-12-19",
            "2018-12-03",
            "2018-12-18",
            "2019-03-25",
            "2019-07-08",
            "2019-12-02",
            "2020-03-09",
            "2020-03-24",
            "2020-03-25",
            "2020-05-11",
            "2020-08-31",
            "2021-01-04",
            "2021-03-24",
            "2021-05-03",
            "2021-05-10",
            "2022-01-04",
            "2022-05-02",
            "2022-05-10",
        )
        self.assertHoliday(observed_holidays)
        self.assertNoNonObservedHoliday(observed_holidays)

    def test2020(self):
        self.assertHolidayDates(
            KzHolidays(years=2020),
            "2020-01-01",
            "2020-01-02",
            "2020-01-07",
            "2020-03-08",
            "2020-03-09",
            "2020-03-21",
            "2020-03-22",
            "2020-03-23",
            "2020-03-24",
            "2020-03-25",
            "2020-05-01",
            "2020-05-07",
            "2020-05-09",
            "2020-05-11",
            "2020-07-06",
            "2020-07-31",
            "2020-08-30",
            "2020-08-31",
            "2020-12-01",
            "2020-12-16",
            "2020-12-17",
        )
