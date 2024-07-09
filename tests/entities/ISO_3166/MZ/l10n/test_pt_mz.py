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

from holidays.entities.ISO_3166.MZ import MzHolidays
from tests.common import CommonCountryTests


class TestMzHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MzHolidays)

    def test_pt_mz(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Dia da Fraternidade universal"),
            ("2023-01-02", "Dia da Fraternidade universal (ponte)"),
            ("2023-02-03", "Dia dos Heróis Moçambicanos"),
            ("2023-04-07", "Dia da Mulher Moçambicana"),
            ("2023-05-01", "Dia Internacional dos Trabalhadores"),
            ("2023-06-25", "Dia da Independência Nacional"),
            ("2023-06-26", "Dia da Independência Nacional (ponte)"),
            ("2023-09-07", "Dia da Vitória"),
            ("2023-09-25", "Dia das Forças Armadas de Libertação Nacional"),
            ("2023-10-04", "Dia da Paz e Reconciliação"),
            ("2023-12-25", "Dia da Família"),
        )
