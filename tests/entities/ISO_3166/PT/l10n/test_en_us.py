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

from holidays.entities.ISO_3166.PT import PtHolidays
from tests.common import CommonCountryTests


class TestPtHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PtHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "New Year's Day"),
            ("2018-02-13", "Carnival"),
            ("2018-03-30", "Good Friday"),
            ("2018-04-01", "Easter Sunday"),
            ("2018-04-25", "Freedom Day"),
            ("2018-05-01", "Labor Day"),
            ("2018-05-31", "Corpus Christi"),
            ("2018-06-10", "Day of Portugal, Camões, and the Portuguese Communities"),
            ("2018-06-13", "St. Anthony's Day"),
            ("2018-08-15", "Assumption Day"),
            ("2018-10-05", "Republic Day"),
            ("2018-11-01", "All Saints' Day"),
            ("2018-12-01", "Restoration of Independence Day"),
            ("2018-12-08", "Immaculate Conception"),
            ("2018-12-24", "Christmas Eve"),
            ("2018-12-25", "Christmas Day"),
            ("2018-12-26", "Second Day of Christmas"),
            ("2018-12-31", "New Year's Eve"),
        )
