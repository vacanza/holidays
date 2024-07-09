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

from holidays.entities.ISO_3166.AE import AeHolidays
from tests.common import CommonCountryTests


class TestAeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AeHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "New Year's Day"),
            ("2018-04-13", "Isra' and Mi'raj"),
            ("2018-06-14", "Eid al-Fitr"),
            ("2018-06-15", "Eid al-Fitr Holiday"),
            ("2018-06-16", "Eid al-Fitr Holiday"),
            ("2018-08-20", "Arafat Day"),
            ("2018-08-21", "Eid al-Adha"),
            ("2018-08-22", "Eid al-Adha Holiday"),
            ("2018-08-23", "Eid al-Adha Holiday"),
            ("2018-09-11", "Islamic New Year"),
            ("2018-11-19", "Prophet's Birthday"),
            ("2018-11-30", "Commemoration Day"),
            ("2018-12-02", "National Day"),
            ("2018-12-03", "National Day"),
        )
