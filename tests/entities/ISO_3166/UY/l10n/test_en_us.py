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

from holidays.entities.ISO_3166.UY import UyHolidays
from tests.common import CommonCountryTests


class TestUyHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(UyHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Children's Day"),
            ("2022-02-28", "Carnival"),
            ("2022-03-01", "Carnival"),
            ("2022-04-11", "Tourism Week"),
            ("2022-04-12", "Tourism Week"),
            ("2022-04-13", "Tourism Week"),
            ("2022-04-14", "Tourism Week"),
            ("2022-04-15", "Tourism Week"),
            ("2022-04-18", "Landing of the 33 Patriots"),
            ("2022-05-01", "International Workers' Day"),
            ("2022-05-16", "Battle of Las Piedras"),
            ("2022-06-19", "Birthday of Artigas"),
            ("2022-07-18", "Constitution Day"),
            ("2022-08-25", "Independence Day"),
            ("2022-10-10", "Cultural Diversity Day"),
            ("2022-11-02", "All Souls' Day"),
            ("2022-12-25", "Day of the Family"),
        )
