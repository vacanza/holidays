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

from holidays.entities.ISO_3166.AM import AmHolidays
from tests.common import CommonCountryTests


class TestAmHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AmHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-01-06", "Christmas and Epiphany Day"),
            ("2022-01-28", "Army Day"),
            ("2022-03-08", "Women's Day"),
            ("2022-04-24", "Genocide Memorial Day"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-09", "Victory and Peace Day"),
            ("2022-05-28", "Republic Day"),
            ("2022-07-05", "Constitution Day"),
            ("2022-09-21", "Independence Day"),
            ("2022-12-31", "New Year's Eve"),
        )
