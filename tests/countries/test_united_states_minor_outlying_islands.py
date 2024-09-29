#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.constants import UNOFFICIAL
from holidays.countries.united_states_minor_outlying_islands import HolidaysUM, UM, UMI
from tests.common import CommonCountryTests


class TestUM(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HolidaysUM)

    def test_country_aliases(self):
        self.assertAliases(HolidaysUM, UM, UMI)

    def test_common(self):
        self.assertIn("Christmas Day", self.holidays["2022-12-25"])

    def test_unofficial_holidays(self):
        self.assertHolidays(
            HolidaysUM(categories=UNOFFICIAL, years=2024),
            ("2024-02-14", "Valentine's Day"),
            ("2024-03-17", "Saint Patrick's Day"),
            ("2024-10-31", "Halloween"),
        )
