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

from holidays.entities.ISO_3166.CW import CwHolidays
from tests.common import CommonCountryTests


class TestCwHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CwHolidays)

    def test_pap_cw(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Aña Nobo"),
            ("2023-02-20", "Dialuna despues di Carnaval Grandi"),
            ("2023-04-07", "Bièrnèsantu"),
            ("2023-04-09", "Pasku di Resurekshon"),
            ("2023-04-10", "Di dos dia di Pasku di Resurekshon"),
            ("2023-04-27", "Dia di Rey"),
            ("2023-05-01", "Dia di Obrero"),
            ("2023-05-18", "Dia di Asenshon"),
            ("2023-07-02", "Dia di Himno i Bandera"),
            ("2023-10-10", "Dia di Pais Kòrsou"),
            ("2023-12-25", "Pasku di Nasementu"),
            ("2023-12-26", "Di dos dia di Pasku di Nasementu"),
        )
