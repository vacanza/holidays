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

from holidays.entities.ISO_3166.MC import McHolidays
from tests.common import CommonCountryTests


class TestMcHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(McHolidays)

    def test_immaculate_conception_day(self):
        self.assertHoliday(
            "2018-12-08",
            "2019-12-09",
            "2020-12-08",
            "2021-12-08",
            "2022-12-08",
            "2023-12-08",
            "2024-12-09",
        )

    def test_observed(self):
        observed_holidays = (
            "2010-08-16",
            "2011-05-02",
            "2011-12-26",
            "2012-01-02",
            "2015-11-02",
            "2016-05-02",
            "2016-12-26",
            "2017-01-02",
            "2017-11-20",
            "2020-11-02",
            "2021-08-16",
            "2022-05-02",
            "2022-12-26",
            "2023-01-02",
            "2023-11-20",
        )
        self.assertHoliday(observed_holidays)
        self.assertNoNonObservedHoliday(observed_holidays)

    def test_2020(self):
        self.assertHolidayDates(
            "2020-01-01",
            "2020-01-27",
            "2020-04-13",
            "2020-05-01",
            "2020-05-21",
            "2020-06-01",
            "2020-06-11",
            "2020-08-15",
            "2020-11-01",
            "2020-11-02",
            "2020-11-19",
            "2020-12-08",
            "2020-12-25",
        )

    def test_2021(self):
        self.assertHolidayDates(
            "2021-01-01",
            "2021-01-27",
            "2021-04-05",
            "2021-05-01",
            "2021-05-13",
            "2021-05-24",
            "2021-06-03",
            "2021-08-15",
            "2021-08-16",
            "2021-11-01",
            "2021-11-19",
            "2021-12-08",
            "2021-12-25",
        )

    def test_2022(self):
        self.assertHolidayDates(
            "2022-01-01",
            "2022-01-27",
            "2022-04-18",
            "2022-05-01",
            "2022-05-02",
            "2022-05-26",
            "2022-06-06",
            "2022-06-16",
            "2022-08-15",
            "2022-11-01",
            "2022-11-19",
            "2022-12-08",
            "2022-12-25",
            "2022-12-26",
        )

    def test_2023(self):
        self.assertHolidayDates(
            "2023-01-01",
            "2023-01-02",
            "2023-01-27",
            "2023-04-10",
            "2023-05-01",
            "2023-05-18",
            "2023-05-29",
            "2023-06-08",
            "2023-08-15",
            "2023-11-01",
            "2023-11-19",
            "2023-11-20",
            "2023-12-08",
            "2023-12-25",
        )
