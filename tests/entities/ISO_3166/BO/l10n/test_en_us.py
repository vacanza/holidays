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

from holidays.entities.ISO_3166.BO import BoHolidays
from tests.common import CommonCountryTests


class TestBoHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BoHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-22", "Plurinational State Foundation Day"),
            ("2023-01-23", "Plurinational State Foundation Day (observed)"),
            ("2023-02-20", "Carnival"),
            ("2023-02-21", "Carnival"),
            ("2023-04-07", "Good Friday"),
            ("2023-05-01", "Labor Day"),
            ("2023-06-08", "Corpus Christi"),
            ("2023-06-21", "Aymara New Year"),
            ("2023-08-06", "Independence Day"),
            ("2023-08-07", "Independence Day (observed)"),
            ("2023-10-17", "National Dignity Day"),
            ("2023-11-02", "All Souls' Day"),
            ("2023-12-25", "Christmas Day"),
        )
