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

from holidays.entities.ISO_3166.AW import AwHolidays
from tests.common import CommonCountryTests


class TestAwHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AwHolidays)

    def test_pap(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Aña Nobo"),
            ("2023-01-25", "Dia di Betico"),
            ("2023-02-20", "Dialuna prome cu diaranson di shinish"),
            ("2023-03-18", "Dia di Himno y Bandera"),
            ("2023-04-07", "Bierna Santo"),
            ("2023-04-10", "Di dos dia di Pasco di Resureccion"),
            ("2023-04-27", "Dia di Rey"),
            ("2023-05-01", "Dia di Obrero"),
            ("2023-05-18", "Dia di Asuncion"),
            ("2023-12-25", "Pasco di Nacemento"),
            ("2023-12-26", "Di dos dia di Pasco di Nacemento"),
        )
