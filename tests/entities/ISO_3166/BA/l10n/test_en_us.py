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

from holidays.entities.ISO_3166.BA import BaHolidays
from tests.common import CommonCountryTests


class TestBaHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BaHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-01-07", "Orthodox Christmas Day"),
            ("2022-04-18", "Catholic Easter Monday"),
            ("2022-04-22", "Orthodox Good Friday"),
            ("2022-05-01", "International Labor Day"),
            ("2022-05-02", "Eid al-Fitr; International Labor Day"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-12-25", "Catholic Christmas Day"),
        )
