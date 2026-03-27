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

from holidays.financial.hong_kong_stock_exchange import HongKongStockExchange
from tests.common import CommonFinancialTests


class TestHongKongStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HongKongStockExchange)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "一月一日"),
            ("2025-01-29", "農曆年初一"),
            ("2025-01-30", "農曆年初二"),
            ("2025-01-31", "農曆年初三"),
            ("2025-04-04", "清明節"),
            ("2025-04-18", "耶穌受難節"),
            ("2025-04-21", "復活節星期一"),
            ("2025-05-01", "勞動節"),
            ("2025-05-05", "佛誕"),
            ("2025-07-01", "香港特別行政區成立紀念日"),
            ("2025-10-01", "國慶日"),
            ("2025-10-07", "中秋節翌日"),
            ("2025-10-29", "重陽節"),
            ("2025-12-25", "聖誕節"),
            ("2025-12-26", "聖誕節後第一個周日"),
        )
        self.assertNoHoliday("2025-05-31")
        self.assertNoHoliday("2025-04-19")

    def test_2025_half_day(self):
        self.assertHalfDayHolidaysInYear(
            2025,
            ("2025-01-28", "農曆年初一的前一日（半日交易日）"),
            ("2025-12-24", "平安夜（半日交易日）"),
            ("2025-12-31", "除夕（半日交易日）"),
        )
        self.assertNoHalfDayHoliday("2025-05-31")

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "一月一日"),
            ("2025-01-28", "農曆年初一的前一日（半日交易日）"),
            ("2025-01-29", "農曆年初一"),
            ("2025-01-30", "農曆年初二"),
            ("2025-01-31", "農曆年初三"),
            ("2025-04-04", "清明節"),
            ("2025-04-18", "耶穌受難節"),
            ("2025-04-21", "復活節星期一"),
            ("2025-05-01", "勞動節"),
            ("2025-05-05", "佛誕"),
            ("2025-07-01", "香港特別行政區成立紀念日"),
            ("2025-10-01", "國慶日"),
            ("2025-10-07", "中秋節翌日"),
            ("2025-10-29", "重陽節"),
            ("2025-12-24", "平安夜（半日交易日）"),
            ("2025-12-25", "聖誕節"),
            ("2025-12-26", "聖誕節後第一個周日"),
            ("2025-12-31", "除夕（半日交易日）"),
        )

    def test_l10n_en_hk(self):
        self.assertLocalizedHolidays(
            "en_HK",
            ("2025-01-01", "The first day of January"),
            ("2025-01-28", "The day preceding Lunar New Year's Day (Half-Day Trading Day)"),
            ("2025-01-29", "Lunar New Year's Day"),
            ("2025-01-30", "The second day of Lunar New Year"),
            ("2025-01-31", "The third day of Lunar New Year"),
            ("2025-04-04", "Ching Ming Festival"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Labour Day"),
            ("2025-05-05", "The Birthday of the Buddha"),
            ("2025-07-01", "Hong Kong Special Administrative Region Establishment Day"),
            ("2025-10-01", "National Day"),
            ("2025-10-07", "The day following the Chinese Mid-Autumn Festival"),
            ("2025-10-29", "Chung Yeung Festival"),
            ("2025-12-24", "Christmas Eve (Half-Day Trading Day)"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "The first weekday after Christmas Day"),
            ("2025-12-31", "New Year's Eve (Half-Day Trading Day)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-28", "Chinese New Year's Eve (Half-Day Trading Day)"),
            ("2025-01-29", "Chinese New Year"),
            ("2025-01-30", "The second day of Chinese New Year"),
            ("2025-01-31", "The third day of Chinese New Year"),
            ("2025-04-04", "Tomb-Sweeping Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-01", "Labor Day"),
            ("2025-05-05", "The Buddha's Birthday"),
            ("2025-07-01", "Hong Kong S.A.R. Establishment Day"),
            ("2025-10-01", "National Day"),
            ("2025-10-07", "The Day following Mid-Autumn Festival"),
            ("2025-10-29", "Double Ninth Festival"),
            ("2025-12-24", "Christmas Eve (Half-Day Trading Day)"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "The first weekday after Christmas Day"),
            ("2025-12-31", "New Year's Eve (Half-Day Trading Day)"),
        )

    def test_l10n_zh_cn(self):
        self.assertLocalizedHolidays(
            "zh_CN",
            ("2025-01-01", "一月一日"),
            ("2025-01-28", "农历年初一的前一日（半日交易日）"),
            ("2025-01-29", "农历年初一"),
            ("2025-01-30", "农历年初二"),
            ("2025-01-31", "农历年初三"),
            ("2025-04-04", "清明节"),
            ("2025-04-18", "耶稣受难节"),
            ("2025-04-21", "复活节星期一"),
            ("2025-05-01", "劳动节"),
            ("2025-05-05", "佛诞"),
            ("2025-07-01", "香港特别行政区成立纪念日"),
            ("2025-10-01", "国庆日"),
            ("2025-10-07", "中秋节翌日"),
            ("2025-10-29", "重阳节"),
            ("2025-12-24", "平安夜（半日交易日）"),
            ("2025-12-25", "圣诞节"),
            ("2025-12-26", "圣诞节后第一个周日"),
            ("2025-12-31", "除夕（半日交易日）"),
        )

    def test_l10n_zh_hk(self):
        self.assertLocalizedHolidays(
            "zh_HK",
            ("2025-01-01", "一月一日"),
            ("2025-01-28", "農曆年初一的前一日（半日交易日）"),
            ("2025-01-29", "農曆年初一"),
            ("2025-01-30", "農曆年初二"),
            ("2025-01-31", "農曆年初三"),
            ("2025-04-04", "清明節"),
            ("2025-04-18", "耶穌受難節"),
            ("2025-04-21", "復活節星期一"),
            ("2025-05-01", "勞動節"),
            ("2025-05-05", "佛誕"),
            ("2025-07-01", "香港特別行政區成立紀念日"),
            ("2025-10-01", "國慶日"),
            ("2025-10-07", "中秋節翌日"),
            ("2025-10-29", "重陽節"),
            ("2025-12-24", "平安夜（半日交易日）"),
            ("2025-12-25", "聖誕節"),
            ("2025-12-26", "聖誕節後第一個周日"),
            ("2025-12-31", "除夕（半日交易日）"),
        )
