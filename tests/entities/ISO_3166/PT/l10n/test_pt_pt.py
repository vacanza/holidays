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

from holidays.entities.ISO_3166.PT import PtHolidays
from tests.common import CommonCountryTests


class TestPtHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PtHolidays)

    def test_pt_pt(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "Ano Novo"),
            ("2018-02-13", "Carnaval"),
            ("2018-03-30", "Sexta-feira Santa"),
            ("2018-04-01", "Páscoa"),
            ("2018-04-25", "Dia da Liberdade"),
            ("2018-05-01", "Dia do Trabalhador"),
            ("2018-05-31", "Corpo de Deus"),
            ("2018-06-10", "Dia de Portugal, de Camões e das Comunidades Portuguesas"),
            ("2018-06-13", "Dia de Santo António"),
            ("2018-08-15", "Assunção de Nossa Senhora"),
            ("2018-10-05", "Implantação da República"),
            ("2018-11-01", "Dia de Todos os Santos"),
            ("2018-12-01", "Restauração da Independência"),
            ("2018-12-08", "Imaculada Conceição"),
            ("2018-12-24", "Véspera de Natal"),
            ("2018-12-25", "Dia de Natal"),
            ("2018-12-26", "26 de Dezembro"),
            ("2018-12-31", "Véspera de Ano Novo"),
        )
