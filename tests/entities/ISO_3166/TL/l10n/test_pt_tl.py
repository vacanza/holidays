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
        super().setUpClass(TlHolidays)

    def test_pt_tl(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Dia de Ano Novo"),
            ("2023-01-02", "Feriados Nacionais (Especiais)"),
            ("2023-01-23", "Feriados Nacionais (Especiais)"),
            ("2023-02-22", "Feriados Nacionais (Especiais); Quarta-Feira de Cinzas"),
            ("2023-03-03", "Dia dos Veteranos"),
            ("2023-04-06", "Quinta-Feira Santa"),
            ("2023-04-07", "Sexta-Feira Santa"),
            ("2023-04-22", "Idul Fitri"),
            ("2023-05-01", "Dia Mundial do Trabalhador"),
            ("2023-05-18", "Dia da Ascensão de Jesus Cristo ao Céu"),
            ("2023-05-20", "Dia da Restauração da Independência"),
            ("2023-06-01", "Dia Mundial da Criança"),
            ("2023-06-08", "Festa do Corpo de Deus"),
            ("2023-06-29", "Idul Adha"),
            (
                "2023-08-20",
                "Dia das Forças Armadas de Libertação Nacional de Timor-Leste (FALINTIL)",
            ),
            ("2023-08-30", "Dia da Consulta Popular"),
            ("2023-11-01", "Dia de Todos os Santos"),
            ("2023-11-02", "Dia de Todos os Fiéis Defuntos"),
            ("2023-11-03", "Dia Nacional da Mulher"),
            ("2023-11-12", "Dia Nacional da Juventude"),
            ("2023-11-28", "Dia da Proclamação da Independência"),
            ("2023-12-07", "Dia da Memória"),
            (
                "2023-12-08",
                "Dia de Nossa Senhora da Imaculada Conceição, padroeira de Timor-Leste",
            ),
            ("2023-12-10", "Dia Mundial dos Direitos Humanos"),
            ("2023-12-25", "Dia de Natal"),
            ("2023-12-31", "Dia dos Heróis Nacionais"),
        )
