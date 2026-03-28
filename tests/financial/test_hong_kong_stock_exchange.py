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

    def test_add_holiday_requires_arguments(self):
        with self.assertRaises(TypeError):
            self.holidays._add_holiday("Test holiday")

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "一月一日"),
            ("2024-02-12", "農曆年初三"),
            ("2024-02-13", "農曆年初四"),
            ("2024-03-29", "耶穌受難節"),
            ("2024-04-01", "復活節星期一"),
            ("2024-04-04", "清明節"),
            ("2024-05-01", "勞動節"),
            ("2024-05-15", "佛誕"),
            ("2024-06-10", "端午節"),
            ("2024-07-01", "香港特別行政區成立紀念日"),
            ("2024-09-18", "中秋節翌日"),
            ("2024-10-01", "國慶日"),
            ("2024-10-11", "重陽節"),
            ("2024-12-25", "聖誕節"),
            ("2024-12-26", "聖誕節後第一個周日"),
        )
        self.assertNoHoliday("2024-05-31")
        self.assertNoHoliday("2024-03-30")

    def test_2024_half_day(self):
        self.assertHalfDayHolidaysInYear(
            2024,
            ("2024-02-09", "農曆年初一的前一日（半日交易日）"),
            ("2024-12-24", "平安夜（半日交易日）"),
            ("2024-12-31", "新年前夕（半日交易日）"),
        )
        self.assertNoHalfDayHoliday("2024-05-31")

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "一月一日"),
            ("2024-02-09", "農曆年初一的前一日（半日交易日）"),
            ("2024-02-12", "農曆年初三"),
            ("2024-02-13", "農曆年初四"),
            ("2024-03-29", "耶穌受難節"),
            ("2024-04-01", "復活節星期一"),
            ("2024-04-04", "清明節"),
            ("2024-05-01", "勞動節"),
            ("2024-05-15", "佛誕"),
            ("2024-06-10", "端午節"),
            ("2024-07-01", "香港特別行政區成立紀念日"),
            ("2024-09-18", "中秋節翌日"),
            ("2024-10-01", "國慶日"),
            ("2024-10-11", "重陽節"),
            ("2024-12-24", "平安夜（半日交易日）"),
            ("2024-12-25", "聖誕節"),
            ("2024-12-26", "聖誕節後第一個周日"),
            ("2024-12-31", "新年前夕（半日交易日）"),
        )

    def test_l10n_en_hk(self):
        self.assertLocalizedHolidays(
            "en_HK",
            ("2024-01-01", "The first day of January"),
            ("2024-02-09", "The day preceding Lunar New Year's Day (Half-Day Trading Day)"),
            ("2024-02-12", "The third day of Lunar New Year"),
            ("2024-02-13", "The fourth day of Lunar New Year"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-04", "Ching Ming Festival"),
            ("2024-05-01", "Labour Day"),
            ("2024-05-15", "The Birthday of the Buddha"),
            ("2024-06-10", "Tuen Ng Festival"),
            ("2024-07-01", "Hong Kong Special Administrative Region Establishment Day"),
            ("2024-09-18", "The day following the Chinese Mid-Autumn Festival"),
            ("2024-10-01", "National Day"),
            ("2024-10-11", "Chung Yeung Festival"),
            ("2024-12-24", "Christmas Eve (Half-Day Trading Day)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "The first weekday after Christmas Day"),
            ("2024-12-31", "New Year's Eve (Half-Day Trading Day)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-02-09", "Chinese New Year's Eve (Half-Day Trading Day)"),
            ("2024-02-12", "The third day of Chinese New Year"),
            ("2024-02-13", "The fourth day of Chinese New Year"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-04", "Tomb-Sweeping Day"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-15", "The Buddha's Birthday"),
            ("2024-06-10", "Dragon Boat Festival"),
            ("2024-07-01", "Hong Kong S.A.R. Establishment Day"),
            ("2024-09-18", "The Day following Mid-Autumn Festival"),
            ("2024-10-01", "National Day"),
            ("2024-10-11", "Double Ninth Festival"),
            ("2024-12-24", "Christmas Eve (Half-Day Trading Day)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "The first weekday after Christmas Day"),
            ("2024-12-31", "New Year's Eve (Half-Day Trading Day)"),
        )

    def test_l10n_zh_cn(self):
        self.assertLocalizedHolidays(
            "zh_CN",
            ("2024-01-01", "一月一日"),
            ("2024-02-09", "农历年初一的前一日（半日交易日）"),
            ("2024-02-12", "农历年初三"),
            ("2024-02-13", "农历年初四"),
            ("2024-03-29", "耶稣受难节"),
            ("2024-04-01", "复活节星期一"),
            ("2024-04-04", "清明节"),
            ("2024-05-01", "劳动节"),
            ("2024-05-15", "佛诞"),
            ("2024-06-10", "端午节"),
            ("2024-07-01", "香港特别行政区成立纪念日"),
            ("2024-09-18", "中秋节翌日"),
            ("2024-10-01", "国庆日"),
            ("2024-10-11", "重阳节"),
            ("2024-12-24", "平安夜（半日交易日）"),
            ("2024-12-25", "圣诞节"),
            ("2024-12-26", "圣诞节后第一个周日"),
            ("2024-12-31", "新年前夕（半日交易日）"),
        )

    def test_l10n_zh_hk(self):
        self.assertLocalizedHolidays(
            "zh_HK",
            ("2024-01-01", "一月一日"),
            ("2024-02-09", "農曆年初一的前一日（半日交易日）"),
            ("2024-02-12", "農曆年初三"),
            ("2024-02-13", "農曆年初四"),
            ("2024-03-29", "耶穌受難節"),
            ("2024-04-01", "復活節星期一"),
            ("2024-04-04", "清明節"),
            ("2024-05-01", "勞動節"),
            ("2024-05-15", "佛誕"),
            ("2024-06-10", "端午節"),
            ("2024-07-01", "香港特別行政區成立紀念日"),
            ("2024-09-18", "中秋節翌日"),
            ("2024-10-01", "國慶日"),
            ("2024-10-11", "重陽節"),
            ("2024-12-24", "平安夜（半日交易日）"),
            ("2024-12-25", "聖誕節"),
            ("2024-12-26", "聖誕節後第一個周日"),
            ("2024-12-31", "新年前夕（半日交易日）"),
        )
