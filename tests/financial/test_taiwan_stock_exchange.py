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

from holidays.financial.taiwan_stock_exchange import TaiwanStockExchange
from tests.common import CommonFinancialTests


class TestTaiwanStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full_range = range(2008, 2030)
        super().setUpClass(TaiwanStockExchange)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_labor_day(self):
        name = "勞動節"
        years_absent = {2010, 2011, 2016, 2021, 2022}
        self.assertNoHolidayName(name, (f"{year}-05-01" for year in years_absent))
        self.assertHolidayName(
            name,
            (f"{year}-05-01" for year in range(self.start_year, 2026) if year not in years_absent),
        )
        self.assertHolidayName(
            name,
            "2010-04-30",
            "2011-05-02",
            "2016-05-02",
            "2021-04-30",
            "2022-05-02",
        )

    def test_clearing_and_settlement(self):
        name = "無交易（僅辦理結算交割）"
        self.assertHolidayName(
            name,
            "2021-02-08",
            "2021-02-09",
            "2022-01-27",
            "2022-01-28",
            "2023-01-18",
            "2023-01-19",
            "2024-02-06",
            "2024-02-07",
            "2025-01-23",
            "2025-01-24",
            "2026-02-12",
            "2026-02-13",
        )
        self.assertHolidayName(name, range(self.start_year, self.end_year))

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "中華民國開國紀念日"),
            ("2025-01-23", "無交易（僅辦理結算交割）"),
            ("2025-01-24", "無交易（僅辦理結算交割）"),
            ("2025-01-27", "放假日（2025-02-08 補班）"),
            ("2025-01-28", "農曆除夕"),
            ("2025-01-29", "春節"),
            ("2025-01-30", "春節"),
            ("2025-01-31", "春節"),
            ("2025-02-28", "和平紀念日"),
            ("2025-04-03", "兒童節"),
            ("2025-04-04", "兒童節; 民族掃墓節"),
            ("2025-05-01", "勞動節"),
            ("2025-05-30", "端午節"),
            ("2025-09-29", "孔子誕辰紀念日"),
            ("2025-10-06", "中秋節"),
            ("2025-10-10", "國慶日"),
            ("2025-10-24", "臺灣光復暨金門古寧頭大捷紀念日"),
            ("2025-12-25", "行憲紀念日"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "中華民國開國紀念日"),
            ("2024-02-06", "無交易（僅辦理結算交割）"),
            ("2024-02-07", "無交易（僅辦理結算交割）"),
            ("2024-02-08", "放假日（2024-02-17 補班）"),
            ("2024-02-09", "農曆除夕"),
            ("2024-02-12", "春節"),
            ("2024-02-13", "春節"),
            ("2024-02-14", "春節"),
            ("2024-02-28", "和平紀念日"),
            ("2024-04-04", "兒童節; 民族掃墓節"),
            ("2024-04-05", "兒童節"),
            ("2024-05-01", "勞動節"),
            ("2024-06-10", "端午節"),
            ("2024-09-17", "中秋節"),
            ("2024-10-10", "國慶日"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "Founding Day of the Republic of China"),
            ("2024-02-06", "No Trading (Market opens only for Clearing & Settlement)"),
            ("2024-02-07", "No Trading (Market opens only for Clearing & Settlement)"),
            ("2024-02-08", "Day off (substituted from 02/17/2024)"),
            ("2024-02-09", "Chinese New Year's Eve"),
            ("2024-02-12", "Chinese New Year"),
            ("2024-02-13", "Chinese New Year"),
            ("2024-02-14", "Chinese New Year"),
            ("2024-02-28", "Peace Memorial Day"),
            ("2024-04-04", "Children's Day; Tomb-Sweeping Day"),
            ("2024-04-05", "Children's Day"),
            ("2024-05-01", "Labor Day"),
            ("2024-06-10", "Dragon Boat Festival"),
            ("2024-09-17", "Mid-Autumn Festival"),
            ("2024-10-10", "National Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2024-01-01", "วันสถาปนาสาธารณรัฐจีน(ไต้หวัน)"),
            ("2024-02-06", "ไม่มีการซื้อขาย (เปิดตลาดสำหรับการชำระราคาและส่งมอบหลักทรัพย์เท่านั้น)"),
            ("2024-02-07", "ไม่มีการซื้อขาย (เปิดตลาดสำหรับการชำระราคาและส่งมอบหลักทรัพย์เท่านั้น)"),
            ("2024-02-08", "วันหยุด (แทน 17/02/2024)"),
            ("2024-02-09", "วันก่อนวันตรุษจีน"),
            ("2024-02-12", "วันตรุษจีน"),
            ("2024-02-13", "วันตรุษจีน"),
            ("2024-02-14", "วันตรุษจีน"),
            ("2024-02-28", "วันรำลึกสันติภาพ"),
            ("2024-04-04", "วันเช็งเม้ง; วันเด็กแห่งชาติ"),
            ("2024-04-05", "วันเด็กแห่งชาติ"),
            ("2024-05-01", "วันแรงงาน"),
            ("2024-06-10", "วันไหว้บ๊ะจ่าง"),
            ("2024-09-17", "วันไหว้พระจันทร์"),
            ("2024-10-10", "วันชาติสาธารณรัฐจีน(ไต้หวัน)"),
        )

    def test_l10n_zh_cn(self):
        self.assertLocalizedHolidays(
            "zh_CN",
            ("2024-01-01", "中华民国开国纪念日"),
            ("2024-02-06", "无交易（仅办理结算交割）"),
            ("2024-02-07", "无交易（仅办理结算交割）"),
            ("2024-02-08", "休息日（由 2024-02-17 调休）"),
            ("2024-02-09", "农历除夕"),
            ("2024-02-12", "春节"),
            ("2024-02-13", "春节"),
            ("2024-02-14", "春节"),
            ("2024-02-28", "和平纪念日"),
            ("2024-04-04", "儿童节; 民族扫墓节"),
            ("2024-04-05", "儿童节"),
            ("2024-05-01", "劳动节"),
            ("2024-06-10", "端午节"),
            ("2024-09-17", "中秋节"),
            ("2024-10-10", "国庆日"),
        )
