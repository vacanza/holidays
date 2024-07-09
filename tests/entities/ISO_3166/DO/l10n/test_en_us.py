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

from holidays.entities.ISO_3166.DO import DoHolidays
from tests.common import CommonCountryTests


class TestDoHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(DoHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-10", "Epiphany"),
            ("2022-01-21", "Lady of Altagracia"),
            ("2022-01-24", "Juan Pablo Duarte Day"),
            ("2022-02-27", "Independence Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-02", "Labor Day"),
            ("2022-06-16", "Corpus Christi"),
            ("2022-08-15", "Restoration Day"),
            ("2022-09-24", "Our Lady of Mercedes Day"),
            ("2022-11-06", "Constitution Day"),
            ("2022-12-25", "Christmas Day"),
        )
