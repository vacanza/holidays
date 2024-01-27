#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: vacanza team (https://github.com/orgs/vacanza/teams) (c) 2023-2024
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

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
