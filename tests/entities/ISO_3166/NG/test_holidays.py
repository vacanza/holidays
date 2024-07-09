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

from holidays.entities.ISO_3166.NG import NgHolidays
from tests.common import CommonCountryTests


class TestNgHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(NgHolidays, years=range(1979, 2050))

    def test_no_holidays(self):
        self.assertNoHolidays(NgHolidays(years=1978))

    def test_special_holidays(self):
        self.assertHoliday(
            "2019-02-22",
            "2019-05-29",
        )

    def test_new_year_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1979, 2050))

    def test_workers_day(self):
        self.assertHoliday(f"{year}-05-01" for year in range(1981, 2050))
        self.assertNoHoliday(f"{year}-05-01" for year in range(1979, 1981))
        self.assertNoHolidayName("Workers' Day", range(1979, 1981))

    def test_democracy_day(self):
        self.assertHoliday(f"{year}-05-29" for year in range(2000, 2019))
        self.assertHoliday(f"{year}-06-12" for year in range(2019, 2050))
        # in 2019 May 29 is special holiday, so check from 2020
        self.assertNoHoliday(f"{year}-05-29" for year in range(2020, 2050))
        self.assertNoHoliday(f"{year}-06-12" for year in range(2000, 2019))
        self.assertNoHolidayName("Democracy Day", range(1979, 2000))

    def test_independence_day(self):
        self.assertHoliday(f"{year}-10-01" for year in range(1979, 2050))

    def test_christmas_day(self):
        self.assertHoliday(f"{year}-12-25" for year in range(1979, 2050))

    def test_boxing_day(self):
        self.assertHoliday(f"{year}-12-26" for year in range(1979, 2050))

    def test_easter_based(self):
        self.assertHoliday(
            # Good Friday
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            # Easter Monday
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )

    def test_hijri_based(self):
        self.assertHolidayName(
            "Eid-el-Fitr (estimated)",
            "2018-06-15",
            "2019-06-04",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
        )
        self.assertHolidayName(
            "Eid-el-Fitr Holiday (estimated)",
            "2018-06-16",
            "2019-06-05",
            "2020-05-25",
            "2021-05-14",
            "2022-05-03",
            "2023-04-22",
        )
        self.assertHolidayName(
            "Eid-el-Kabir (estimated)",
            "2006-01-10",
            "2006-12-31",
            "2018-08-21",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
        )
        self.assertHolidayName(
            "Eid-el-Kabir Holiday (estimated)",
            "2006-01-11",
            "2007-01-01",
            "2018-08-22",
            "2019-08-12",
            "2020-08-01",
            "2021-07-21",
            "2022-07-10",
            "2023-06-29",
        )
        self.assertHolidayName(
            "Eid-el-Mawlid (estimated)",
            "2018-11-20",
            "2019-11-09",
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
        )

    def test_observed(self):
        dt = (
            # New Year's Day
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
            # Workers' Day
            "2016-05-02",
            "2021-05-03",
            "2022-05-04",
            # Democracy Day
            "2016-05-30",
            "2021-06-14",
            "2022-06-13",
            # Independence Day
            "2016-10-03",
            "2017-10-02",
            "2022-10-03",
            "2023-10-02",
            # Christmas Day
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
            # Boxing Day
            "2020-12-28",
            "2021-12-28",
            # Id el Fitr
            "2018-06-18",
            "2020-05-26",
            "2023-04-24",
            # Id el Kabir
            "2019-08-13",
            "2020-08-03",
            "2022-07-11",
            "2022-07-12",
            # Id el Maulud
            "2019-11-11",
            "2022-10-10",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)
