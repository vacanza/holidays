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

from holidays.financial.stock_exchange_of_thailand import StockExchangeOfThailand
from tests.common import CommonFinancialTests


class TestStockExchangeOfThailand(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(StockExchangeOfThailand)

    def test_special_holidays(self):
        self.assertHoliday(
            "2022-07-29",
            "2022-10-14",
            "2023-05-05",
            "2023-12-29",
            "2024-04-12",
            "2025-06-02",
            "2025-08-11",
            "2026-01-02",
            "2026-10-16",
        )

    def test_government_special_holidays_not_adopted(self):
        self.assertNoHoliday(
            "2022-07-15",
            "2022-12-30",
            "2023-07-31",
            "2024-12-30",
        )

    def test_buddhist_lent_day(self):
        self.assertNoHolidayName("วันเข้าพรรษา")
        self.assertNoHoliday(
            "2022-07-14",
            "2023-08-02",
            "2025-07-11",
            "2026-07-30",
        )

    def test_songkran_festival(self):
        name = "วันสงกรานต์"
        self.assertHolidayName(
            name, (f"{year}-04-{day}" for year in self.full_range for day in (13, 14, 15))
        )
        obs_dts = (
            "2024-04-16",
            "2029-04-16",
        )
        self.assertHolidayName(f"ชดเชย{name}", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHoliday(
            "2023-04-17",
            "2025-04-16",
        )

    def test_new_years_eve(self):
        name = "วันสิ้นปี"
        self.assertHolidayName(name, (f"{year}-12-31" for year in self.full_range))
        obs_dts = (
            "2023-01-02",
            "2029-01-02",
        )
        self.assertHolidayName(f"ชดเชย{name}", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHoliday(
            "2023-01-03",
            "2024-01-02",
        )

    def test_asarnha_bucha(self):
        name = "วันอาสาฬหบูชา"
        self.assertHolidayName(
            name,
            "2022-07-13",
            "2023-08-01",
            "2024-07-20",
            "2025-07-10",
            "2026-07-29",
            "2027-07-18",
        )
        obs_dts = (
            "2024-07-22",
            "2027-07-19",
        )
        self.assertHolidayName(f"ชดเชย{name}", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHoliday("2027-07-20")

    def test_shared_in_lieu_day(self):
        self.assertHolidayName("ชดเชยวันขึ้นปีใหม่", "2023-01-02")
        self.assertHolidayName("ชดเชยวันวิสาขบูชา", "2023-06-05")
        self.assertHolidayName(
            "ชดเชยวันเฉลิมพระชนมพรรษาสมเด็จพระนางเจ้าสุทิดา พัชรสุธาพิมลลักษณ พระบรมราชินี",
            "2023-06-05",
        )
        self.assertNoHoliday("2023-06-06")

    def test_2022(self):
        self.assertHolidayDatesInYear(
            2022,
            "2022-01-01",
            "2022-01-03",
            "2022-02-16",
            "2022-04-06",
            "2022-04-13",
            "2022-04-14",
            "2022-04-15",
            "2022-05-01",
            "2022-05-02",
            "2022-05-04",
            "2022-05-15",
            "2022-05-16",
            "2022-06-03",
            "2022-07-13",
            "2022-07-28",
            "2022-07-29",
            "2022-08-12",
            "2022-10-13",
            "2022-10-14",
            "2022-10-23",
            "2022-10-24",
            "2022-12-05",
            "2022-12-10",
            "2022-12-12",
            "2022-12-31",
        )

    def test_2023(self):
        self.assertHolidayDatesInYear(
            2023,
            "2023-01-01",
            "2023-01-02",
            "2023-03-06",
            "2023-04-06",
            "2023-04-13",
            "2023-04-14",
            "2023-04-15",
            "2023-05-01",
            "2023-05-04",
            "2023-05-05",
            "2023-06-03",
            "2023-06-05",
            "2023-07-28",
            "2023-08-01",
            "2023-08-12",
            "2023-08-14",
            "2023-10-13",
            "2023-10-23",
            "2023-12-05",
            "2023-12-10",
            "2023-12-11",
            "2023-12-29",
            "2023-12-31",
        )

    def test_2024(self):
        self.assertHolidayDatesInYear(
            2024,
            "2024-01-01",
            "2024-02-24",
            "2024-02-26",
            "2024-04-06",
            "2024-04-08",
            "2024-04-12",
            "2024-04-13",
            "2024-04-14",
            "2024-04-15",
            "2024-04-16",
            "2024-05-01",
            "2024-05-04",
            "2024-05-06",
            "2024-05-22",
            "2024-06-03",
            "2024-07-20",
            "2024-07-22",
            "2024-07-28",
            "2024-07-29",
            "2024-08-12",
            "2024-10-13",
            "2024-10-14",
            "2024-10-23",
            "2024-12-05",
            "2024-12-10",
            "2024-12-31",
        )

    def test_2025(self):
        self.assertHolidayDatesInYear(
            2025,
            "2025-01-01",
            "2025-02-12",
            "2025-04-06",
            "2025-04-07",
            "2025-04-13",
            "2025-04-14",
            "2025-04-15",
            "2025-05-01",
            "2025-05-04",
            "2025-05-05",
            "2025-05-11",
            "2025-05-12",
            "2025-06-02",
            "2025-06-03",
            "2025-07-10",
            "2025-07-28",
            "2025-08-11",
            "2025-08-12",
            "2025-10-13",
            "2025-10-23",
            "2025-12-05",
            "2025-12-10",
            "2025-12-31",
        )

    def test_2027(self):
        self.assertHolidayDatesInYear(
            2027,
            "2027-01-01",
            "2027-02-21",
            "2027-02-22",
            "2027-04-06",
            "2027-04-13",
            "2027-04-14",
            "2027-04-15",
            "2027-05-01",
            "2027-05-03",
            "2027-05-04",
            "2027-05-20",
            "2027-06-03",
            "2027-07-18",
            "2027-07-19",
            "2027-07-28",
            "2027-08-12",
            "2027-10-13",
            "2027-10-23",
            "2027-10-25",
            "2027-12-05",
            "2027-12-06",
            "2027-12-10",
            "2027-12-31",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2026-01-01", "วันขึ้นปีใหม่"),
            ("2026-01-02", "วันหยุดพิเศษ (เพิ่มเติม)"),
            ("2026-03-03", "วันมาฆบูชา"),
            (
                "2026-04-06",
                "วันพระบาทสมเด็จพระพุทธยอดฟ้าจุฬาโลกมหาราช และวันที่ระลึกมหาจักรีบรมราชวงศ์",
            ),
            ("2026-04-13", "วันสงกรานต์"),
            ("2026-04-14", "วันสงกรานต์"),
            ("2026-04-15", "วันสงกรานต์"),
            ("2026-05-01", "วันแรงงานแห่งชาติ"),
            ("2026-05-04", "วันฉัตรมงคล"),
            ("2026-05-31", "วันวิสาขบูชา"),
            ("2026-06-01", "ชดเชยวันวิสาขบูชา"),
            (
                "2026-06-03",
                "วันเฉลิมพระชนมพรรษาสมเด็จพระนางเจ้าสุทิดา พัชรสุธาพิมลลักษณ พระบรมราชินี",
            ),
            (
                "2026-07-28",
                "วันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระปรเมนทรรามาธิบดี"
                "ศรีสินทรมหาวชิราลงกรณ พระวชิรเกล้าเจ้าอยู่หัว",
            ),
            ("2026-07-29", "วันอาสาฬหบูชา"),
            ("2026-08-12", "วันเฉลิมพระชนมพรรษาสมเด็จพระบรมราชชนนีพันปีหลวง; วันแม่แห่งชาติ"),
            ("2026-10-13", "วันนวมินทรมหาราช"),
            ("2026-10-16", "วันหยุดพิเศษ (เพิ่มเติม)"),
            ("2026-10-23", "วันปิยมหาราช"),
            (
                "2026-12-05",
                "วันคล้ายวันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระบรมชนกาธิเบศร "
                "มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร; วันชาติ; วันพ่อแห่งชาติ",
            ),
            (
                "2026-12-07",
                "ชดเชยวันคล้ายวันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระบรมชนกาธิเบศร "
                "มหาภูมิพลอดุลยเดชมหาราช บรมนาถบพิตร; ชดเชยวันชาติ; ชดเชยวันพ่อแห่งชาติ",
            ),
            ("2026-12-10", "วันรัฐธรรมนูญ"),
            ("2026-12-31", "วันสิ้นปี"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2026-01-01", "New Year's Day"),
            ("2026-01-02", "Bridge Public Holiday"),
            ("2026-03-03", "Makha Bucha"),
            ("2026-04-06", "Chakri Memorial Day"),
            ("2026-04-13", "Songkran Festival"),
            ("2026-04-14", "Songkran Festival"),
            ("2026-04-15", "Songkran Festival"),
            ("2026-05-01", "National Labor Day"),
            ("2026-05-04", "Coronation Day"),
            ("2026-05-31", "Visakha Bucha"),
            ("2026-06-01", "Visakha Bucha (in lieu)"),
            ("2026-06-03", "HM Queen Suthida's Birthday"),
            ("2026-07-28", "HM King Maha Vajiralongkorn's Birthday"),
            ("2026-07-29", "Asarnha Bucha"),
            ("2026-08-12", "HM Queen Sirikit The Queen Mother's Birthday; National Mother's Day"),
            ("2026-10-13", "HM King Bhumibol Adulyadej Memorial Day"),
            ("2026-10-16", "Bridge Public Holiday"),
            ("2026-10-23", "HM King Chulalongkorn Memorial Day"),
            (
                "2026-12-05",
                "HM King Bhumibol Adulyadej the Great's Birthday; National Day; "
                "National Father's Day",
            ),
            (
                "2026-12-07",
                "HM King Bhumibol Adulyadej the Great's Birthday (in lieu); "
                "National Day (in lieu); National Father's Day (in lieu)",
            ),
            ("2026-12-10", "Constitution Day"),
            ("2026-12-31", "New Year's Eve"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2026-01-01", "Новий рік"),
            ("2026-01-02", "Проміжний вихідний"),
            ("2026-03-03", "Маха Буча"),
            ("2026-04-06", "День памʼяті короля Рами I та династії Чакрі"),
            ("2026-04-13", "Тайський Новий рік"),
            ("2026-04-14", "Тайський Новий рік"),
            ("2026-04-15", "Тайський Новий рік"),
            ("2026-05-01", "Національний день праці"),
            ("2026-05-04", "День коронації"),
            ("2026-05-31", "Вісака Буча"),
            ("2026-06-01", "Вісака Буча (вихідний)"),
            ("2026-06-03", "День народження Її Величності королеви Сутіди"),
            ("2026-07-28", "День народження Його Величності короля Маха Вачіралонгкорна"),
            ("2026-07-29", "Асарна Буча"),
            (
                "2026-08-12",
                "День народження Її Величності королеви-матері Сірікіт; Національний день матері",
            ),
            ("2026-10-13", "День памʼяті Його Величності короля Пуміпона Адульядета"),
            ("2026-10-16", "Проміжний вихідний"),
            ("2026-10-23", "День памʼяті Його Величності короля Чулалонгкорна"),
            (
                "2026-12-05",
                "Національний день; Національний день батька; "
                "Річниця дня народження Його Величності короля Пуміпона Адульядета Великого",
            ),
            (
                "2026-12-07",
                "Національний день (вихідний); Національний день батька (вихідний); "
                "Річниця дня народження Його Величності короля Пуміпона Адульядета Великого "
                "(вихідний)",
            ),
            ("2026-12-10", "День Конституції"),
            ("2026-12-31", "Переддень Нового року"),
        )
