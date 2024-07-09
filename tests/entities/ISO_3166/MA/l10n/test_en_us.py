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

from holidays.entities.ISO_3166.MA import MaHolidays
from tests.common import CommonCountryTests


class TestMAHolicays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MaHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-11", "Proclamation of Independence Day"),
            ("2023-04-21", "Eid al-Fitr (estimated)"),
            ("2023-04-22", "Eid al-Fitr (estimated)"),
            ("2023-05-01", "Labor Day"),
            ("2023-06-28", "Eid al-Adha (estimated)"),
            ("2023-06-29", "Eid al-Adha (estimated)"),
            ("2023-07-19", "Islamic New Year (estimated)"),
            ("2023-07-30", "Throne Day"),
            ("2023-08-14", "Oued Ed-Dahab Day"),
            ("2023-08-20", "Revolution Day"),
            ("2023-08-21", "Youth Day"),
            ("2023-09-27", "Prophet's Birthday (estimated)"),
            ("2023-09-28", "Prophet's Birthday (estimated)"),
            ("2023-11-06", "Green March"),
            ("2023-11-18", "Independence Day"),
        )
