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

from holidays.constants import GOVERNMENT
from holidays.entities.ISO_3166.GE import GeHolidays
from tests.common import CommonCountryTests


class TestGeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(GeHolidays)

    def test_no_holidays(self):
        self.assertNoHolidays(GeHolidays(years=1990))

    def test_family_sanctity_day(self):
        self.assertHolidays(
            GeHolidays(categories=GOVERNMENT, years=2024),
            ("2024-05-17", "ოჯახის სიწმინდისა და მშობლების პატივისცემის დღე"),
        )

    def test_2020(self):
        # https://en.wikipedia.org/wiki/Public_holidays_in_Georgia_(country)
        self.assertHolidayDates(
            "2020-01-01",
            "2020-01-02",
            "2020-01-07",
            "2020-01-19",
            "2020-03-03",
            "2020-03-08",
            "2020-04-09",
            "2020-04-17",
            "2020-04-18",
            "2020-04-19",
            "2020-04-20",
            "2020-05-09",
            "2020-05-12",
            "2020-05-26",
            "2020-08-28",
            "2020-10-14",
            "2020-11-23",
        )
