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

from holidays.entities.ISO_3166.AW import AwHolidays
from tests.common import CommonCountryTests


class TestAwHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AwHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-25", "Betico Day"),
            ("2023-02-20", "Monday before Ash Wednesday"),
            ("2023-03-18", "National Anthem and Flag Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-27", "King's Day"),
            ("2023-05-01", "Labor Day"),
            ("2023-05-18", "Ascension Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Second Day of Christmas"),
        )
