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

from holidays.entities.ISO_3166.CY import CyHolidays
from tests.common import CommonCountryTests


class TestCyHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CyHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-06", "Epiphany"),
            ("2023-02-27", "Green Monday"),
            ("2023-03-25", "Greek Independence Day"),
            ("2023-04-01", "Cyprus National Day"),
            ("2023-04-14", "Good Friday"),
            ("2023-04-15", "Holy Saturday"),
            ("2023-04-16", "Easter Sunday"),
            ("2023-04-17", "Easter Monday"),
            ("2023-04-18", "Easter Tuesday"),
            ("2023-05-01", "Labor Day"),
            ("2023-06-05", "Whit Monday"),
            ("2023-08-15", "Assumption Day"),
            ("2023-10-01", "Cyprus Independence Day"),
            ("2023-10-28", "Greek National Day"),
            ("2023-12-24", "Christmas Eve"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Day After Christmas"),
        )
