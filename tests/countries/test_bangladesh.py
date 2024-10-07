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

from holidays.countries.bangladesh import Bangladesh, BD, BGD
from tests.common import CommonCountryTests


class TestBangladesh(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Bangladesh)

    def test_country_aliases(self):
        self.assertAliases(Bangladesh, BD, BGD)

    def test_2022(self):
        self.assertHolidays(
            ("2022-02-21", "International Mother's language Day"),
            ("2022-03-17", "Sheikh Mujibur Rahman's Birthday and Children's Day"),
            ("2022-03-26", "Independence Day"),
            ("2022-04-14", "Bengali New Year's Day"),
            ("2022-05-01", "May Day"),
            ("2022-08-15", "National Mourning Day"),
            ("2022-12-16", "Victory Day"),
        )
