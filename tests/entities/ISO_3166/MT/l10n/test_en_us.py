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

from holidays.entities.ISO_3166.MT import MtHolidays
from tests.common import CommonCountryTests


class TestMtHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MtHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-02-10", "Feast of St. Paul's Shipwreck"),
            ("2023-03-19", "Feast of St. Joseph"),
            ("2023-03-31", "Freedom Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-05-01", "Worker's Day"),
            ("2023-06-07", "Sette Giugno"),
            ("2023-06-29", "Feast of St. Peter and St. Paul"),
            ("2023-08-15", "Feast of the Assumption"),
            ("2023-09-08", "Feast of Our Lady of Victories"),
            ("2023-09-21", "Independence Day"),
            ("2023-12-08", "Feast of the Immaculate Conception"),
            ("2023-12-13", "Republic Day"),
            ("2023-12-25", "Christmas Day"),
        )
