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

from holidays.entities.ISO_3166.EE import EeHolidays
from tests.common import CommonCountryTests


class TestEeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(EeHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-02-24", "Independence Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-05-01", "Spring Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-23", "Victory Day"),
            ("2022-06-24", "Midsummer Day"),
            ("2022-08-20", "Independence Restoration Day"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )