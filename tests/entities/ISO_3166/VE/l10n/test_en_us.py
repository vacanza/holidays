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

from holidays.entities.ISO_3166.VE import VeHolidays
from tests.common import CommonCountryTests


class TestVeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(VeHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2021-01-01", "New Year's Day"),
            ("2021-02-15", "Monday of Carnival"),
            ("2021-02-16", "Tuesday of Carnival"),
            ("2021-04-01", "Maundy Thursday"),
            ("2021-04-02", "Good Friday"),
            ("2021-04-19", "Declaration of Independence"),
            ("2021-05-01", "International Worker's Day"),
            ("2021-06-24", "Battle of Carabobo"),
            ("2021-07-05", "Independence Day"),
            ("2021-07-24", "Birthday of Simon Bolivar"),
            ("2021-10-12", "Day of Indigenous Resistance"),
            ("2021-12-24", "Christmas Eve"),
            ("2021-12-25", "Christmas Day"),
            ("2021-12-31", "New Year's Eve"),
        )
