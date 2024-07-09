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

from holidays.entities.ISO_3166.PE import PeHolidays
from tests.common import CommonCountryTests


class TestPeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PeHolidays)

    def test_2019(self):
        self.assertHolidayDates(
            "2019-01-01",
            "2019-04-18",
            "2019-04-19",
            "2019-04-21",
            "2019-05-01",
            "2019-06-29",
            "2019-07-28",
            "2019-07-29",
            "2019-08-30",
            "2019-10-08",
            "2019-11-01",
            "2019-12-08",
            "2019-12-25",
        )

    def test_2022(self):
        self.assertHolidayDates(
            "2022-01-01",
            "2022-04-14",
            "2022-04-15",
            "2022-04-17",
            "2022-05-01",
            "2022-06-29",
            "2022-07-28",
            "2022-07-29",
            "2022-08-06",
            "2022-08-30",
            "2022-10-08",
            "2022-11-01",
            "2022-12-08",
            "2022-12-09",
            "2022-12-25",
        )
