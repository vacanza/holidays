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

from holidays.entities.ISO_3166.TL import TlHolidays
from tests.common import CommonCountryTests


class TestTlHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(TlHolidays, language="tet")

    def test_l10n_tet(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Loron Tinan-Foun nian"),
            ("2023-01-02", "Feriadu Nasional (Espesial)"),
            ("2023-01-23", "Feriadu Nasional (Espesial)"),
            ("2023-02-22", "Feriadu Nasional (Espesial); Kuarta-Feira Sinzas"),
            ("2023-03-03", "Loron Veteranu sira nian"),
            ("2023-04-06", "Quinta-Feira Santa"),
            ("2023-04-07", "Sesta-Feira Santa"),
            ("2023-04-22", "Idul-Fitri"),
            ("2023-05-01", "Loron Mundiál Serbisu-na'in sira nian"),
            ("2023-05-18", "Loron Ascensão do Senhor Jesus Cristo hi'it An ba Lalehan nian"),
            ("2023-05-20", "Loron Restaurasaun Independénsia nian"),
            ("2023-06-01", "Loron Mundial ba Labarik"),
            ("2023-06-08", "Festa Korpu de Deus"),
            ("2023-06-29", "Idul Adha"),
            ("2023-08-20", "Loron Forsa Armada Libertasaun Nasionál Timor-Leste (FALINTIL) nian"),
            ("2023-08-30", "Loron Konsulta Populár nian"),
            ("2023-11-01", "Loron Santu sira Hotu nian"),
            ("2023-11-02", "Loron Matebian sira nian"),
            ("2023-11-03", "Loron Nasionál Feto"),
            ("2023-11-12", "Loron Nasionál Foin-Sa'e sira nian"),
            ("2023-11-28", "Loron Proklamasaun Independénsia nian"),
            ("2023-12-07", "Loron Memória nian"),
            ("2023-12-08", "Loron Nossa Senhora da Imaculada Conceição, mahein Timor-Leste nian"),
            ("2023-12-10", "Loron Mundiál Direitu Umanu"),
            ("2023-12-25", "Loron Natál"),
            ("2023-12-31", "Loron Eroi Nasionál sira nian"),
        )
