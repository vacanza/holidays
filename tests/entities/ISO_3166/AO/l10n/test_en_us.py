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

from holidays.entities.ISO_3166.AO import AoHolidays
from tests.common import CommonCountryTests


class TestAoHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AoHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-02-04", "Liberation Movement Day"),
            ("2023-02-20", "Day off for Carnival Day"),
            ("2023-02-21", "Carnival Day"),
            ("2023-03-08", "International Women's Day"),
            ("2023-03-23", "Southern Africa Liberation Day"),
            ("2023-03-24", "Day off for Southern Africa Liberation Day"),
            ("2023-04-03", "Day off for Peace and National Reconciliation Day"),
            ("2023-04-04", "Peace and National Reconciliation Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-05-01", "International Worker's Day"),
            ("2023-09-17", "National Heroes' Day"),
            ("2023-11-02", "All Souls' Day"),
            ("2023-11-03", "Day off for All Souls' Day"),
            ("2023-11-11", "National Independence Day"),
            ("2023-12-25", "Christmas and Family Day"),
        )
