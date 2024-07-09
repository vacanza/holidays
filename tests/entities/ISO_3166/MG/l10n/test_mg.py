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

from holidays.entities.ISO_3166.MG import MgHolidays
from tests.common import CommonCountryTests


class TestMgHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MgHolidays)

    def test_mg(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Taom-baovao"),
            ("2022-03-08", "Fetin'ny vehivavy"),
            ("2022-03-29", "Fetin'ny mahery fo"),
            ("2022-04-17", "Fetin'ny paska"),
            ("2022-04-18", "Alatsinain'ny paska"),
            ("2022-05-01", "Fetin'ny asa"),
            ("2022-05-26", "Fiakaran'ny Jesosy kristy tany an-danitra"),
            ("2022-05-29", "Fetin'ny reny"),
            ("2022-06-05", "Pentekosta"),
            ("2022-06-06", "Alatsinain'ny pentekosta"),
            ("2022-06-19", "Fetin'ny ray"),
            ("2022-06-26", "Fetin'ny fahaleovantena"),
            ("2022-08-15", "Fiakaran'ny Masina Maria tany an-danitra"),
            ("2022-11-01", "Fetin'ny olo-masina"),
            ("2022-12-11", "Fetin'ny Repoblika"),
            ("2022-12-25", "Fetin'ny noely"),
        )
