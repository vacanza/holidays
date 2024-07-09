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

from holidays.entities.ISO_3166.CO import CoHolidays
from tests.common import CommonCountryTests


class TestCoHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CoHolidays)

    def test_2016(self):
        # https://www.officeholidays.com/countries/colombia/2016
        self.assertHolidayDates(
            "2016-01-01",
            "2016-01-11",
            "2016-03-21",
            "2016-03-24",
            "2016-03-25",
            "2016-05-01",
            "2016-05-09",
            "2016-05-30",
            "2016-06-06",
            "2016-07-04",
            "2016-07-20",
            "2016-08-07",
            "2016-08-15",
            "2016-10-17",
            "2016-11-07",
            "2016-11-14",
            "2016-12-08",
            "2016-12-25",
        )

    def test_2017(self):
        # https://www.officeholidays.com/countries/colombia/2017
        self.assertHolidayDates(
            "2017-01-01",
            "2017-01-09",
            "2017-03-20",
            "2017-04-13",
            "2017-04-14",
            "2017-05-01",
            "2017-05-29",
            "2017-06-19",
            "2017-06-26",
            "2017-07-03",
            "2017-07-20",
            "2017-08-07",
            "2017-08-21",
            "2017-10-16",
            "2017-11-06",
            "2017-11-13",
            "2017-12-08",
            "2017-12-25",
        )

    def test_2018(self):
        # https://publicholidays.co/2018-dates/
        self.assertHolidayDates(
            "2018-01-01",
            "2018-01-08",
            "2018-03-19",
            "2018-03-29",
            "2018-03-30",
            "2018-05-01",
            "2018-05-14",
            "2018-06-04",
            "2018-06-11",
            "2018-07-02",
            "2018-07-20",
            "2018-08-07",
            "2018-08-20",
            "2018-10-15",
            "2018-11-05",
            "2018-11-12",
            "2018-12-08",
            "2018-12-25",
        )

    def test_2019(self):
        # https://www.officeholidays.com/countries/colombia/2019
        self.assertHolidayDates(
            "2019-01-01",
            "2019-01-07",
            "2019-03-25",
            "2019-04-18",
            "2019-04-19",
            "2019-05-01",
            "2019-06-03",
            "2019-06-24",
            "2019-07-01",
            "2019-07-20",
            "2019-08-07",
            "2019-08-19",
            "2019-10-14",
            "2019-11-04",
            "2019-11-11",
            "2019-12-08",
            "2019-12-25",
        )

    def test_2020(self):
        # https://www.officeholidays.com/countries/colombia/2020
        self.assertHolidayDates(
            "2020-01-01",
            "2020-01-06",
            "2020-03-23",
            "2020-04-09",
            "2020-04-10",
            "2020-05-01",
            "2020-05-25",
            "2020-06-15",
            "2020-06-22",
            "2020-06-29",
            "2020-07-20",
            "2020-08-07",
            "2020-08-17",
            "2020-10-12",
            "2020-11-02",
            "2020-11-16",
            "2020-12-08",
            "2020-12-25",
        )

    def test_2021(self):
        # https://www.officeholidays.com/countries/colombia/2021
        self.assertHolidayDates(
            "2021-01-01",
            "2021-01-11",
            "2021-03-22",
            "2021-04-01",
            "2021-04-02",
            "2021-05-01",
            "2021-05-17",
            "2021-06-07",
            "2021-06-14",
            "2021-07-05",
            "2021-07-20",
            "2021-08-07",
            "2021-08-16",
            "2021-10-18",
            "2021-11-01",
            "2021-11-15",
            "2021-12-08",
            "2021-12-25",
        )

    def test_2022(self):
        # https://www.officeholidays.com/countries/colombia/2022
        self.assertHolidayDates(
            "2022-01-01",
            "2022-01-10",
            "2022-03-21",
            "2022-04-14",
            "2022-04-15",
            "2022-05-01",
            "2022-05-30",
            "2022-06-20",
            "2022-06-27",
            "2022-07-04",
            "2022-07-20",
            "2022-08-07",
            "2022-08-15",
            "2022-10-17",
            "2022-11-07",
            "2022-11-14",
            "2022-12-08",
            "2022-12-25",
        )

    def test_2023(self):
        # https://publicholidays.co/2023-dates/
        self.assertHolidayDates(
            "2023-01-01",
            "2023-01-09",
            "2023-03-20",
            "2023-04-06",
            "2023-04-07",
            "2023-05-01",
            "2023-05-22",
            "2023-06-12",
            "2023-06-19",
            "2023-07-03",
            "2023-07-20",
            "2023-08-07",
            "2023-08-21",
            "2023-10-16",
            "2023-11-06",
            "2023-11-13",
            "2023-12-08",
            "2023-12-25",
        )

    def test_1984(self):
        self.assertHolidayDates(
            "1984-01-01",
            "1984-01-09",
            "1984-03-19",
            "1984-04-19",
            "1984-04-20",
            "1984-05-01",
            "1984-06-04",
            "1984-06-25",
            "1984-07-02",
            "1984-07-20",
            "1984-08-07",
            "1984-08-20",
            "1984-10-15",
            "1984-11-05",
            "1984-11-12",
            "1984-12-08",
            "1984-12-25",
        )

    def test_1983(self):
        self.assertHolidayDates(
            "1983-01-01",
            "1983-01-06",
            "1983-03-19",
            "1983-03-31",
            "1983-04-01",
            "1983-05-01",
            "1983-05-12",
            "1983-06-02",
            "1983-06-29",
            "1983-07-20",
            "1983-08-07",
            "1983-08-15",
            "1983-10-12",
            "1983-11-01",
            "1983-11-11",
            "1983-12-08",
            "1983-12-25",
        )

    def test_1951(self):
        self.assertHolidayDates(
            "1951-01-01",
            "1951-01-06",
            "1951-03-19",
            "1951-03-22",
            "1951-03-23",
            "1951-05-01",
            "1951-05-03",
            "1951-05-24",
            "1951-06-29",
            "1951-07-20",
            "1951-08-07",
            "1951-08-15",
            "1951-10-12",
            "1951-11-01",
            "1951-11-11",
            "1951-12-08",
            "1951-12-25",
        )

    def test_1950(self):
        self.assertHolidayDates(
            "1950-01-01",
            "1950-05-01",
            "1950-07-20",
            "1950-08-07",
            "1950-10-12",
            "1950-11-11",
            "1950-12-25",
        )
