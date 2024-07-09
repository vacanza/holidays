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

from holidays.entities.ISO_3166.GT import GtHolidays
from tests.common import CommonCountryTests


class TestGtHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(GtHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-03-28", "Maundy Thursday"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "Holy Saturday"),
            ("2024-05-01", "Labor Day"),
            ("2024-07-01", "Army Day"),
            ("2024-08-15", "Assumption Day"),
            ("2024-09-15", "Independence Day"),
            ("2024-10-20", "Revolution Day"),
            ("2024-11-01", "All Saints' Day"),
            ("2024-12-25", "Christmas Day"),
        )
