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

from holidays.entities.ISO_3166.JO import JoHolidays
from tests.common import CommonCountryTests


class TestJoHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(JoHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-02-08", "Isra and Miraj (estimated)"),
            ("2024-04-10", "Eid al-Fitr (estimated)"),
            ("2024-04-11", "Eid al-Fitr Holiday (estimated)"),
            ("2024-04-12", "Eid al-Fitr Holiday (estimated)"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-25", "Independence Day"),
            ("2024-06-15", "Arafat Day (estimated)"),
            ("2024-06-16", "Eid al-Adha (estimated)"),
            ("2024-06-17", "Eid al-Adha Holiday (estimated)"),
            ("2024-06-18", "Eid al-Adha Holiday (estimated)"),
            ("2024-07-07", "Islamic New Year (estimated)"),
            ("2024-09-15", "Prophet's Birthday (estimated)"),
            ("2024-12-25", "Christmas Day"),
        )
