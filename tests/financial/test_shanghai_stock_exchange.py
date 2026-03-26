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

from holidays.countries.china import China
from holidays.financial.shanghai_stock_exchange import ShanghaiStockExchange
from tests.common import CommonFinancialTests


class TestShanghaiStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ShanghaiStockExchange)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    @staticmethod
    def _expected_localized_holidays(language=None):
        dates = (
            "2024-01-01",
            "2024-02-10",
            "2024-02-11",
            "2024-02-12",
            "2024-02-13",
            "2024-02-14",
            "2024-02-15",
            "2024-02-16",
            "2024-04-04",
            "2024-04-05",
            "2024-05-01",
            "2024-05-02",
            "2024-05-03",
            "2024-06-10",
            "2024-09-16",
            "2024-09-17",
            "2024-10-01",
            "2024-10-02",
            "2024-10-03",
            "2024-10-04",
            "2024-10-07",
        )
        kwargs = {"years": 2024}
        if language:
            kwargs["language"] = language
        holidays = China(**kwargs)
        return tuple((dt, holidays.get(dt)) for dt in dates)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(*self._expected_localized_holidays())

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US", *self._expected_localized_holidays("en_US")
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays("th", *self._expected_localized_holidays("th"))

    def test_l10n_zh_tw(self):
        self.assertLocalizedHolidays(
            "zh_TW", *self._expected_localized_holidays("zh_TW")
        )
