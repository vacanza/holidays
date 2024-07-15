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

from holidays.entities.ISO_3166.LA import LaHolidays
from tests.common import CommonCountryTests


class TestLaHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(LaHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (in lieu)"),
            ("2022-01-20", "Lao People's Armed Force Day"),
            ("2022-02-01", "Lao Federation of Trade Union's Day"),
            ("2022-02-16", "Makha Bousa Festival"),
            ("2022-03-08", "International Women's Rights Day"),
            ("2022-03-22", "Establishment Day of the Lao People's Revolutionary Party"),
            ("2022-04-14", "Lao New Year's Day; Lao People's Revolutionary Youth Union Day"),
            ("2022-04-15", "Lao New Year's Day"),
            ("2022-04-16", "Lao New Year's Day"),
            ("2022-04-18", "Lao New Year's Day (in lieu)"),
            ("2022-05-01", "International Labor Day"),
            ("2022-05-02", "International Labor Day (in lieu)"),
            ("2022-05-15", "Visakha Bousa Festival"),
            ("2022-06-01", "International Children Day; National Arbor Day"),
            (
                "2022-07-13",
                (
                    "Begin of Buddhist Lent; President Souphanouvong's Birthday; "
                    "The National Day for Wildlife and Aquatic Animal Conservation"
                ),
            ),
            ("2022-07-20", "Establishment Day of the Lao Women's Union"),
            ("2022-08-13", "Lao National Mass Media and Publishing Day"),
            ("2022-08-15", "Lao National Constitution Day"),
            ("2022-08-23", "National Uprising Day"),
            ("2022-08-26", "Boun Haw Khao Padapdin"),
            ("2022-09-10", "Boun Haw Khao Salark"),
            ("2022-10-07", "Establishment Day of the BOL; National Teacher Day"),
            ("2022-10-10", "End of Buddhist Lent"),
            ("2022-10-11", "Vientiane Boat Racing Festival"),
            ("2022-10-12", "Indepedence Declaration Day"),
            ("2022-11-08", "Boun That Luang Festival"),
            ("2022-12-02", "Lao National Day"),
            ("2022-12-13", "President Kaysone Phomvihane's Birthday"),
            ("2022-12-28", "Lao Year-End Bank Holiday"),
            ("2022-12-29", "Lao Year-End Bank Holiday"),
            ("2022-12-30", "Lao Year-End Bank Holiday"),
        )
