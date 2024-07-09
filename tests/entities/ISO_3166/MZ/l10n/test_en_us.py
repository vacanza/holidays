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

from holidays.entities.ISO_3166.MZ import MzHolidays
from tests.common import CommonCountryTests


class TestMzHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MzHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "International Fraternalism Day"),
            ("2023-01-02", "International Fraternalism Day (observed)"),
            ("2023-02-03", "Heroes' Day"),
            ("2023-04-07", "Women's Day"),
            ("2023-05-01", "International Workers' Day"),
            ("2023-06-25", "Independence Day"),
            ("2023-06-26", "Independence Day (observed)"),
            ("2023-09-07", "Victory Day"),
            ("2023-09-25", "Armed Forces Day"),
            ("2023-10-04", "Peace and Reconciliation Day"),
            ("2023-12-25", "Family Day"),
        )
