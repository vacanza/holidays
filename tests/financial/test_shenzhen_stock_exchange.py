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

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "元旦"),
            ("2024-02-09", "农历除夕"),
            ("2024-02-10", "春节"),
            ("2024-02-11", "春节"),
            ("2024-02-12", "春节"),
            ("2024-02-13", "春节（补假）"),
            ("2024-02-14", "春节（补假）"),
            ("2024-02-15", "休息日（由 2024-02-04 调休）"),
            ("2024-02-16", "休息日（由 2024-02-18 调休）"),
            ("2024-04-04", "清明节"),
            ("2024-04-05", "休息日（由 2024-04-07 调休）"),
            ("2024-05-01", "劳动节"),
            ("2024-05-02", "休息日（由 2024-04-28 调休）"),
            ("2024-05-03", "休息日（由 2024-05-11 调休）"),
            ("2024-06-10", "端午节"),
            ("2024-09-16", "休息日（由 2024-09-14 调休）"),
            ("2024-09-17", "中秋节"),
            ("2024-10-01", "国庆节"),
            ("2024-10-02", "国庆节"),
            ("2024-10-03", "国庆节"),
            ("2024-10-04", "休息日（由 2024-09-29 调休）"),
            ("2024-10-07", "休息日（由 2024-10-12 调休）"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-02-09", "Chinese New Year's Eve"),
            ("2024-02-10", "Chinese New Year (Spring Festival)"),
            ("2024-02-11", "Chinese New Year (Spring Festival)"),
            ("2024-02-12", "Chinese New Year (Spring Festival)"),
            ("2024-02-13", "Chinese New Year (Spring Festival) (observed)"),
            ("2024-02-14", "Chinese New Year (Spring Festival) (observed)"),
            ("2024-02-15", "Day off (substituted from 02/04/2024)"),
            ("2024-02-16", "Day off (substituted from 02/18/2024)"),
            ("2024-04-04", "Tomb-Sweeping Day"),
            ("2024-04-05", "Day off (substituted from 04/07/2024)"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-02", "Day off (substituted from 04/28/2024)"),
            ("2024-05-03", "Day off (substituted from 05/11/2024)"),
            ("2024-06-10", "Dragon Boat Festival"),
            ("2024-09-16", "Day off (substituted from 09/14/2024)"),
            ("2024-09-17", "Mid-Autumn Festival"),
            ("2024-10-01", "National Day"),
            ("2024-10-02", "National Day"),
            ("2024-10-03", "National Day"),
            ("2024-10-04", "Day off (substituted from 09/29/2024)"),
            ("2024-10-07", "Day off (substituted from 10/12/2024)"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2024-01-01", "วันปีใหม่สากล"),
            ("2024-02-09", "วันก่อนวันตรุษจีน"),
            ("2024-02-10", "วันตรุษจีน"),
            ("2024-02-11", "วันตรุษจีน"),
            ("2024-02-12", "วันตรุษจีน"),
            ("2024-02-13", "ชดเชยวันตรุษจีน"),
            ("2024-02-14", "ชดเชยวันตรุษจีน"),
            ("2024-02-15", "วันหยุด (แทน 04/02/2024)"),
            ("2024-02-16", "วันหยุด (แทน 18/02/2024)"),
            ("2024-04-04", "วันเช็งเม้ง"),
            ("2024-04-05", "วันหยุด (แทน 07/04/2024)"),
            ("2024-05-01", "วันแรงงาน"),
            ("2024-05-02", "วันหยุด (แทน 28/04/2024)"),
            ("2024-05-03", "วันหยุด (แทน 11/05/2024)"),
            ("2024-06-10", "วันไหว้บ๊ะจ่าง"),
            ("2024-09-16", "วันหยุด (แทน 14/09/2024)"),
            ("2024-09-17", "วันไหว้พระจันทร์"),
            ("2024-10-01", "วันชาติจีน"),
            ("2024-10-02", "วันชาติจีน"),
            ("2024-10-03", "วันชาติจีน"),
            ("2024-10-04", "วันหยุด (แทน 29/09/2024)"),
            ("2024-10-07", "วันหยุด (แทน 12/10/2024)"),
        )

    def test_l10n_zh_tw(self):
        self.assertLocalizedHolidays(
            "zh_TW",
            ("2024-01-01", "元旦"),
            ("2024-02-09", "農曆除夕"),
            ("2024-02-10", "春節"),
            ("2024-02-11", "春節"),
            ("2024-02-12", "春節"),
            ("2024-02-13", "春節（補假）"),
            ("2024-02-14", "春節（補假）"),
            ("2024-02-15", "放假日（2024-02-04 補班）"),
            ("2024-02-16", "放假日（2024-02-18 補班）"),
            ("2024-04-04", "清明節"),
            ("2024-04-05", "放假日（2024-04-07 補班）"),
            ("2024-05-01", "勞動節"),
            ("2024-05-02", "放假日（2024-04-28 補班）"),
            ("2024-05-03", "放假日（2024-05-11 補班）"),
            ("2024-06-10", "端午節"),
            ("2024-09-16", "放假日（2024-09-14 補班）"),
            ("2024-09-17", "中秋節"),
            ("2024-10-01", "國慶節"),
            ("2024-10-02", "國慶節"),
            ("2024-10-03", "國慶節"),
            ("2024-10-04", "放假日（2024-09-29 補班）"),
            ("2024-10-07", "放假日（2024-10-12 補班）"),
        )
