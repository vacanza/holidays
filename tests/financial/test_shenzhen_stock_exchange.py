#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.financial.shanghai_stock_exchange import ShanghaiStockExchange
from holidays.financial.shenzhen_stock_exchange import ShenzhenStockExchange
from tests.common import CommonFinancialTests


class TestShenzhenStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ShenzhenStockExchange)

    def _assert_same_as_shanghai(self, year, language=None):
        self.assertDictEqual(
            dict(ShenzhenStockExchange(years=year, language=language)),
            dict(ShanghaiStockExchange(years=year, language=language)),
        )

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertEqual(self.holidays.market, "XSHE")
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_same_as_shanghai(self):
        for year in (2024, 2025):
            self._assert_same_as_shanghai(year)

    def test_l10n_default(self):
        self._assert_same_as_shanghai(2024)

    def test_l10n_en_us(self):
        self._assert_same_as_shanghai(2024, "en_US")

    def test_l10n_th(self):
        self._assert_same_as_shanghai(2024, "th")

    def test_l10n_zh_tw(self):
        self._assert_same_as_shanghai(2024, "zh_TW")
