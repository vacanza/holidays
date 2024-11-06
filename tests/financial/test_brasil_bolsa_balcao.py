#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.financial.brasil_bolsa_balcao import BrasilBolsaBalcao, BVMF, B3
from tests.common import CommonFinancialTests


class TestBrasilBolsaBalcao(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BrasilBolsaBalcao)

    def test_market_aliases(self):
        self.assertAliases(BrasilBolsaBalcao, BVMF, B3)
