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

from holidays.entities.ISO_3166.RO import RoHolidays
from tests.common import CommonCountryTests


class TestRoHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(RoHolidays)

    def test_from_2024(self):
        self.assertHoliday("2024-01-06", "2024-01-07")
        self.assertNoHoliday("2023-01-06", "2023-01-07")
        self.assertNoHolidayName("Bobotează", RoHolidays(years=2023))
        self.assertNoHolidayName("Sfântul Ion", RoHolidays(years=2023))

    def test_unification_day(self):
        self.assertHoliday("2016-01-24")
        self.assertNoHoliday("2015-01-24")
        self.assertNoHolidayName("Ziua Unirii Principatelor Române", RoHolidays(years=2015))

    def test_easter(self):
        self.assertHoliday(
            "2017-04-16",
            "2017-04-17",
            "2018-04-06",
            "2018-04-08",
            "2018-04-09",
        )
        self.assertNoHoliday("2016-04-29", "2017-04-14")

    def test_childrens_day(self):
        self.assertHoliday("2017-06-01")
        self.assertNoHoliday("2016-06-01")
        self.assertNoHolidayName("Ziua Copilului", RoHolidays(years=2016))

    def test_assumption_day(self):
        self.assertHoliday("2009-08-15")
        self.assertNoHoliday("2008-08-15")
        self.assertNoHolidayName("Adormirea Maicii Domnului", RoHolidays(years=2008))

    def test_saint_andrews_day(self):
        self.assertHoliday("2012-11-30")
        self.assertNoHoliday("2011-11-30")
        self.assertNoHolidayName("Sfantul Apostol Andrei cel Intai chemat", RoHolidays(years=2011))

    def test_2020(self):
        # https://publicholidays.ro/2020-dates/
        self.assertHolidayDates(
            RoHolidays(years=2020),
            "2020-01-01",
            "2020-01-02",
            "2020-01-24",
            "2020-04-17",
            "2020-04-19",
            "2020-04-20",
            "2020-05-01",
            "2020-06-01",
            "2020-06-07",
            "2020-06-08",
            "2020-08-15",
            "2020-11-30",
            "2020-12-01",
            "2020-12-25",
            "2020-12-26",
        )

    def test_2022(self):
        # https://publicholidays.ro/2022-dates/
        self.assertHolidayDates(
            RoHolidays(years=2022),
            "2022-01-01",
            "2022-01-02",
            "2022-01-24",
            "2022-04-22",
            "2022-04-24",
            "2022-04-25",
            "2022-05-01",
            "2022-06-01",
            "2022-06-12",
            "2022-06-13",
            "2022-08-15",
            "2022-11-30",
            "2022-12-01",
            "2022-12-25",
            "2022-12-26",
        )

    def test_2023(self):
        # https://publicholidays.ro/2023-dates/
        self.assertHolidayDates(
            RoHolidays(years=2023),
            "2023-01-01",
            "2023-01-02",
            "2023-01-24",
            "2023-04-14",
            "2023-04-16",
            "2023-04-17",
            "2023-05-01",
            "2023-06-01",
            "2023-06-04",
            "2023-06-05",
            "2023-08-15",
            "2023-11-30",
            "2023-12-01",
            "2023-12-25",
            "2023-12-26",
        )
