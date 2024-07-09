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

from holidays.entities.ISO_3166.EE import EeHolidays
from tests.common import CommonCountryTests


class TestEeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(EeHolidays)

    def test_et(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "uusaasta"),
            ("2022-02-24", "iseseisvuspäev"),
            ("2022-04-15", "suur reede"),
            ("2022-04-17", "ülestõusmispühade 1. püha"),
            ("2022-05-01", "kevadpüha"),
            ("2022-06-05", "nelipühade 1. püha"),
            ("2022-06-23", "võidupüha"),
            ("2022-06-24", "jaanipäev"),
            ("2022-08-20", "taasiseseisvumispäev"),
            ("2022-12-24", "jõululaupäev"),
            ("2022-12-25", "esimene jõulupüha"),
            ("2022-12-26", "teine jõulupüha"),
        )
