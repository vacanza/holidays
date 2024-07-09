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

from holidays.entities.ISO_3166.ET import EtHolidays
from tests.common import CommonCountryTests


class TestEtHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(EtHolidays, language="en_US")

    def test_en_us(self):
        self.assertLocalizedHolidays(
            ("2022-01-07", "Christmas Day"),
            ("2022-01-19", "Epiphany Day"),
            ("2022-03-02", "Adwa Victory Day"),
            ("2022-04-22", "Good Friday"),
            ("2022-04-24", "Easter Sunday"),
            ("2022-05-01", "Workers' Day"),
            ("2022-05-02", "Eid al-Fitr"),
            ("2022-05-05", "Patriots' Day"),
            ("2022-05-28", "Downfall of Dergue Regime Day"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-09-11", "Ethiopian New Year"),
            ("2022-09-27", "Finding of True Cross"),
            ("2022-10-08", "Prophet's Birthday"),
        )
