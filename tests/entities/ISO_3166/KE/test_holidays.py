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

from holidays.entities.ISO_3166.KE import KeHolidays
from tests.common import CommonCountryTests


class TestKeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(KeHolidays, years=range(1963, 2050))

    def test_no_holidays(self):
        self.assertNoHolidays(KeHolidays(years=1962))

    def test_special_holidays(self):
        self.assertHoliday(
            "2020-02-11",
            "2022-04-29",
            "2022-08-09",
            "2022-09-10",
            "2022-09-11",
            "2022-09-12",
            "2022-09-13",
        )

    def test_holidays(self):
        for year in range(1963, 2050):
            self.assertHoliday(
                f"{year}-01-01",
                f"{year}-05-01",
                f"{year}-10-20",
                f"{year}-12-12",
                f"{year}-12-25",
                f"{year}-12-26",
            )

    def test_madaraka_day(self):
        self.assertNoHoliday(f"{year}-06-01" for year in range(1963, 2010))
        self.assertNoHolidayName("Madaraka Day", range(1963, 2010))
        self.assertHoliday(f"{year}-06-01" for year in range(2010, 2050))

    def test_utamaduni_day(self):
        name1 = "Moi Day"
        name2 = "Utamaduni Day"
        self.assertNoHoliday(f"{year}-10-10" for year in range(1963, 2002))
        self.assertNoHoliday(f"{year}-10-10" for year in range(2010, 2018))
        self.assertNoHolidayName(name1, range(1963, 2002), range(2010, 2018))
        self.assertNoHolidayName(name2, range(1963, 2002), range(2010, 2021))
        self.assertHoliday(f"{year}-10-10" for year in range(2002, 2010))
        self.assertHoliday(f"{year}-10-10" for year in range(2018, 2050))

    def test_mashujaa_day(self):
        self.assertNoHolidayName("Mashujaa Day", range(1963, 2010))
        self.assertNoHolidayName("Kenyatta Day", range(2010, 2050))

    def test_easter(self):
        self.assertHoliday(
            # Good Friday
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            # Easter Monday
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
        )

    def test_observed(self):
        dt = (
            # New Year's Day
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
            # Labour Day
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
            # Madaraka Day
            "2014-06-02",
            "2025-06-02",
            # Utamaduni Day / Moi Day
            "2004-10-11",
            "2021-10-11",
            # Mashujaa Day / Kenyatta Day
            "1996-10-21",
            "2002-10-21",
            "2013-10-21",
            "2019-10-21",
            "2024-10-21",
            # Jamhuri Day
            "2010-12-13",
            "2021-12-13",
            # Christmas Day
            "2011-12-27",
            "2016-12-27",
            "2022-12-27",
            # Boxing Day
            "2010-12-27",
            "2021-12-27",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_2019(self):
        self.assertHolidayDates(
            KeHolidays(years=2019),
            "2019-01-01",
            "2019-04-19",
            "2019-04-22",
            "2019-05-01",
            "2019-06-01",
            "2019-10-10",
            "2019-10-20",
            "2019-10-21",
            "2019-12-12",
            "2019-12-25",
            "2019-12-26",
        )

    def test_2022(self):
        self.assertHolidayDates(
            KeHolidays(years=2022),
            "2022-01-01",
            "2022-04-15",
            "2022-04-18",
            "2022-04-29",
            "2022-05-01",
            "2022-05-02",
            "2022-06-01",
            "2022-08-09",
            "2022-09-10",
            "2022-09-11",
            "2022-09-12",
            "2022-09-13",
            "2022-10-10",
            "2022-10-20",
            "2022-12-12",
            "2022-12-25",
            "2022-12-26",
            "2022-12-27",
        )
