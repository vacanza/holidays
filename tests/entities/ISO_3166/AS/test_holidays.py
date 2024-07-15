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

from holidays.constants import UNOFFICIAL
from holidays.entities.ISO_3166.AS import AsHolidays
from tests.common import CommonCountryTests


class TestAsHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AsHolidays)

    def test_as_only(self):
        self.assertHoliday("2021-01-01")

    def test_unofficial_holidays(self):
        self.assertHolidays(
            AsHolidays(categories=UNOFFICIAL, years=2024),
            ("2024-02-14", "Valentine's Day"),
            ("2024-03-17", "St. Patrick's Day"),
            ("2024-10-31", "Halloween"),
        )

    def test_2021(self):
        self.assertHolidays(
            AsHolidays(years=2021),
            ("2021-01-01", "New Year's Day"),
            ("2021-01-18", "Martin Luther King Jr. Day"),
            ("2021-02-15", "Washington's Birthday"),
            ("2021-05-31", "Memorial Day"),
            ("2021-06-18", "Juneteenth National Independence Day (observed)"),
            ("2021-06-19", "Juneteenth National Independence Day"),
            ("2021-07-04", "Independence Day"),
            ("2021-07-05", "Independence Day (observed)"),
            ("2021-09-06", "Labor Day"),
            ("2021-10-11", "Columbus Day"),
            ("2021-11-11", "Veterans Day"),
            ("2021-11-25", "Thanksgiving"),
            ("2021-12-23", "Christmas Eve (observed)"),
            ("2021-12-24", "Christmas Day (observed); Christmas Eve"),
            ("2021-12-25", "Christmas Day"),
            ("2021-12-31", "New Year's Day (observed)"),
        )
