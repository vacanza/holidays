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

    def test_2018(self):
        self.assertHolidays(
            ("2018-01-01", "Neijoerschdag"),
            ("2018-04-02", "Ouschterméindeg"),
            ("2018-05-01", "Dag vun der Aarbecht"),
            ("2018-05-10", "Christi Himmelfaart"),
            ("2018-05-21", "Péngschtméindeg"),
            ("2018-06-23", "Nationalfeierdag"),
            ("2018-08-15", "Léiffrawëschdag"),
            ("2018-11-01", "Allerhellgen"),
            ("2018-12-25", "Chrëschtdag"),
            ("2018-12-26", "Stiefesdag"),
        )

    def test_2019(self):
        self.assertHolidays(
            ("2019-01-01", "Neijoerschdag"),
            ("2019-04-22", "Ouschterméindeg"),
            ("2019-05-01", "Dag vun der Aarbecht"),
            ("2019-05-09", "Europadag"),
            ("2019-05-30", "Christi Himmelfaart"),
            ("2019-06-10", "Péngschtméindeg"),
            ("2019-06-23", "Nationalfeierdag"),
            ("2019-08-15", "Léiffrawëschdag"),
            ("2019-11-01", "Allerhellgen"),
            ("2019-12-25", "Chrëschtdag"),
            ("2019-12-26", "Stiefesdag"),
        )

    def test_2020(self):
        self.assertHolidays(
            ("2020-01-01", "Neijoerschdag"),
            ("2020-04-13", "Ouschterméindeg"),
            ("2020-05-01", "Dag vun der Aarbecht"),
            ("2020-05-09", "Europadag"),
            ("2020-05-21", "Christi Himmelfaart"),
            ("2020-06-01", "Péngschtméindeg"),
            ("2020-06-23", "Nationalfeierdag"),
            ("2020-08-15", "Léiffrawëschdag"),
            ("2020-11-01", "Allerhellgen"),
            ("2020-12-25", "Chrëschtdag"),
            ("2020-12-26", "Stiefesdag"),
        )
