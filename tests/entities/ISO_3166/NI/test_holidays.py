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

from holidays.entities.ISO_3166.NI import NiHolidays
from tests.common import CommonCountryTests


class TestNiHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(NiHolidays)

    def test_2020(self):
        self.assertHoliday(
            "2020-01-01",
            "2020-04-09",
            "2020-04-10",
            "2020-05-01",
            "2020-07-19",
            "2020-09-14",
            "2020-09-15",
            "2020-12-08",
            "2020-12-25",
        )

        self.assertNoHoliday(
            NiHolidays(subdiv="AN"),
            "2020-08-01",
            "2020-08-10",
        )

        self.assertHoliday(
            NiHolidays(subdiv="MN"),
            "2020-08-01",
            "2020-08-10",
        )

    def test_ni_holidays_1979(self):
        self.assertHoliday(
            "1979-01-01",
            "1979-04-12",
            "1979-04-13",
            "1979-05-01",
            "1979-07-19",
            "1979-09-14",
            "1979-09-15",
            "1979-12-08",
            "1979-12-25",
        )

    def test_pre_1979(self):
        self.assertNoHoliday("1978-07-19")
