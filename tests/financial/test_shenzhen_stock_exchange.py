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

from holidays.financial.shenzhen_stock_exchange import ShenzhenStockExchange
from tests.common import CommonFinancialTests


class TestShenzhenStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ShenzhenStockExchange)

    @staticmethod
    def _get_holidays(language=None):
        return ShenzhenStockExchange(years=2024, language=language)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertEqual(self.holidays.market, "XSHE")
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_l10n_default(self):
        holidays = self._get_holidays()
        self.assertHolidayName("元旦", holidays, "2024-01-01")
        self.assertHolidayName("农历除夕", holidays, "2024-02-09")
        self.assertHolidayName("春节（补假）", holidays, "2024-02-13")
        self.assertHolidayName("休息日（由 2024-02-04 调休）", holidays, "2024-02-15")
        self.assertHolidayName("清明节", holidays, "2024-04-04")
        self.assertHolidayName("中秋节", holidays, "2024-09-17")
        self.assertHolidayName("国庆节", holidays, "2024-10-01")

    def test_l10n_en_us(self):
        holidays = self._get_holidays("en_US")
        self.assertHolidayName("New Year's Day", holidays, "2024-01-01")
        self.assertHolidayName("Chinese New Year's Eve", holidays, "2024-02-09")
        self.assertHolidayName(
            "Chinese New Year (Spring Festival) (observed)",
            holidays,
            "2024-02-13",
        )
        self.assertHolidayName("Day off (substituted from 02/04/2024)", holidays, "2024-02-15")
        self.assertHolidayName("Tomb-Sweeping Day", holidays, "2024-04-04")
        self.assertHolidayName("Mid-Autumn Festival", holidays, "2024-09-17")
        self.assertHolidayName("National Day", holidays, "2024-10-01")

    def test_l10n_th(self):
        holidays = self._get_holidays("th")
        self.assertHolidayName("วันปีใหม่สากล", holidays, "2024-01-01")
        self.assertHolidayName("วันก่อนวันตรุษจีน", holidays, "2024-02-09")
        self.assertHolidayName("ชดเชยวันตรุษจีน", holidays, "2024-02-13")
        self.assertHolidayName("วันหยุด (แทน 04/02/2024)", holidays, "2024-02-15")
        self.assertHolidayName("วันเช็งเม้ง", holidays, "2024-04-04")
        self.assertHolidayName("วันไหว้พระจันทร์", holidays, "2024-09-17")
        self.assertHolidayName("วันชาติจีน", holidays, "2024-10-01")

    def test_l10n_zh_tw(self):
        holidays = self._get_holidays("zh_TW")
        self.assertHolidayName("元旦", holidays, "2024-01-01")
        self.assertHolidayName("農曆除夕", holidays, "2024-02-09")
        self.assertHolidayName("春節（補假）", holidays, "2024-02-13")
        self.assertHolidayName("放假日（2024-02-04 補班）", holidays, "2024-02-15")
        self.assertHolidayName("清明節", holidays, "2024-04-04")
        self.assertHolidayName("中秋節", holidays, "2024-09-17")
        self.assertHolidayName("國慶節", holidays, "2024-10-01")
