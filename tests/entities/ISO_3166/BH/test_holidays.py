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

from holidays.entities.ISO_3166.BH import BhHolidays
from tests.common import CommonCountryTests


class TestBhHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BhHolidays)

    def test_2022(self):
        self.assertHoliday(
            "2022-01-01",
            "2022-05-01",
            "2022-05-02",
            "2022-05-03",
            "2022-05-04",
            "2022-07-09",
            "2022-07-10",
            "2022-07-11",
            "2022-07-30",
            "2022-08-07",
            "2022-08-08",
            "2022-10-08",
            "2022-12-16",
            "2022-12-17",
        )

    def test_2023(self):
        self.assertHoliday(
            "2023-01-01",
            "2023-04-21",
            "2023-04-22",
            "2023-04-23",
            "2023-05-01",
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            "2023-07-19",
            "2023-07-27",
            "2023-07-28",
            "2023-09-27",
            "2023-12-16",
            "2023-12-17",
        )

    def test_hijri_based(self):
        # Eid Al-Fitr.
        self.assertHoliday(
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
        )

        # Eid Al-Adha.
        self.assertHoliday(
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
        )

        # Islamic New Year.
        self.assertHoliday(
            "2008-01-10",
            "2008-12-29",
            "2020-08-20",
        )
