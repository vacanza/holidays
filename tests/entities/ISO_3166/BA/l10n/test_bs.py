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

from holidays.entities.ISO_3166.BA import BaHolidays
from tests.common import CommonCountryTests


class TestBaHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BaHolidays)

    def test_bs(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nova godina"),
            ("2022-01-02", "Nova godina"),
            ("2022-01-07", "Božić (Pravoslavni)"),
            ("2022-04-18", "Uskrsni ponedjeljak (Katolički)"),
            ("2022-04-22", "Veliki petak (Pravoslavni)"),
            ("2022-05-01", "Međunarodni praznik rada"),
            ("2022-05-02", "Međunarodni praznik rada; Ramazanski Bajram"),
            ("2022-07-09", "Kurban Bajram"),
            ("2022-12-25", "Božić (Katolički)"),
        )
