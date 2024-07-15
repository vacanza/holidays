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

from holidays.entities.ISO_3166.MY import MyHolidays
from tests.common import CommonCountryTests


class TestMyHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MyHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2023-01-22", "Chinese New Year"),
            ("2023-01-23", "Chinese New Year (Second Day)"),
            ("2023-01-24", "Chinese New Year (observed)"),
            ("2023-04-21", "Eid al-Fitr (additional holiday)"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-04-23", "Eid al-Fitr (Second Day)"),
            ("2023-04-24", "Eid al-Fitr (Second Day) (observed)"),
            ("2023-05-01", "Labor Day"),
            ("2023-05-04", "Vesak Day"),
            ("2023-06-05", "Birthday of HM Yang di-Pertuan Agong"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-07-19", "Islamic New Year"),
            ("2023-08-31", "National Day"),
            ("2023-09-16", "Malaysia Day"),
            ("2023-09-28", "Prophet Muhammad's Birthday"),
            ("2023-12-25", "Christmas Day"),
        )
