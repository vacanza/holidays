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

from holidays.entities.ISO_3166.AO import AoHolidays
from tests.common import CommonCountryTests


class TestAoHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AoHolidays)

    def test_pt_ao(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Dia do Ano Novo"),
            ("2023-02-04", "Dia do Início da Luta Armada de Libertação Nacional"),
            ("2023-02-20", "Dia do Carnaval (ponte)"),
            ("2023-02-21", "Dia do Carnaval"),
            ("2023-03-08", "Dia Internacional da Mulher"),
            ("2023-03-23", "Dia da Libertação da África Austral"),
            ("2023-03-24", "Dia da Libertação da África Austral (ponte)"),
            ("2023-04-03", "Dia da Paz e Reconciliação Nacional (ponte)"),
            ("2023-04-04", "Dia da Paz e Reconciliação Nacional"),
            ("2023-04-07", "Sexta-Feira Santa"),
            ("2023-05-01", "Dia Internacional do Trabalhador"),
            ("2023-09-17", "Dia do Fundador da Nação e do Herói Nacional"),
            ("2023-11-02", "Dia dos Finados"),
            ("2023-11-03", "Dia dos Finados (ponte)"),
            ("2023-11-11", "Dia da Independência Nacional"),
            ("2023-12-25", "Dia de Natal e da Família"),
        )
