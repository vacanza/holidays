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

from holidays.entities.ISO_3166.LU import LuHolidays
from tests.common import CommonCountryTests


class TestLuHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(LuHolidays)

    def test_lb(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Neijoerschdag"),
            ("2022-04-18", "Ouschterméindeg"),
            ("2022-05-01", "Dag vun der Aarbecht"),
            ("2022-05-09", "Europadag"),
            ("2022-05-26", "Christi Himmelfaart"),
            ("2022-06-06", "Péngschtméindeg"),
            ("2022-06-23", "Nationalfeierdag"),
            ("2022-08-15", "Léiffrawëschdag"),
            ("2022-11-01", "Allerhellgen"),
            ("2022-12-25", "Chrëschtdag"),
            ("2022-12-26", "Stiefesdag"),
        )
