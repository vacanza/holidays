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

from holidays.entities.ISO_3166.CU import CuHolidays
from tests.common import CommonCountryTests


class TestCuHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CuHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Liberation Day"),
            ("2022-01-02", "Victory Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "International Worker's Day"),
            ("2022-05-02", "International Worker's Day (observed)"),
            ("2022-07-25", "Commemoration of the Assault of the Moncada garrison"),
            ("2022-07-26", "Day of the National Rebellion"),
            ("2022-07-27", "Commemoration of the Assault of the Moncada garrison"),
            ("2022-10-10", "Independence Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-31", "New Year's Eve"),
        )
