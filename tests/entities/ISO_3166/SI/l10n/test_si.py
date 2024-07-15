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

from holidays.entities.ISO_3166.SI import SiHolidays
from tests.common import CommonCountryTests


class TestSiHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SiHolidays)

    def test_si(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "novo leto"),
            ("2022-01-02", "novo leto"),
            ("2022-02-08", "Prešernov dan"),
            ("2022-04-18", "Velikonočni ponedeljek"),
            ("2022-04-27", "dan upora proti okupatorju"),
            ("2022-05-01", "praznik dela"),
            ("2022-05-02", "praznik dela"),
            ("2022-06-25", "dan državnosti"),
            ("2022-08-15", "Marijino vnebovzetje"),
            ("2022-10-31", "dan reformacije"),
            ("2022-11-01", "dan spomina na mrtve"),
            ("2022-12-25", "Božič"),
            ("2022-12-26", "dan samostojnosti in enotnosti"),
        )
