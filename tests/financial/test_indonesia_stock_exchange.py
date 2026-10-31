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

from holidays.financial.indonesia_stock_exchange import IndonesiaStockExchange
from tests.common import CommonFinancialTests


class TestIndonesiaStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(IndonesiaStockExchange)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_joint_holidays(self):
        self.assertHoliday(
            "2022-04-29",
            "2022-05-04",
            "2022-05-05",
            "2022-05-06",
            "2023-01-23",
            "2023-03-23",
            "2023-06-28",
            "2023-06-30",
            "2024-02-09",
            "2024-04-15",
            "2025-08-18",
            "2026-12-24",
            "2027-03-25",
        )

    def test_exchange_holiday(self):
        name = "Libur Bursa"
        years_absent = {2022, 2023, 2028, 2033, 2034, 2039, 2044, 2045}
        self.assertHolidayName(
            name, (f"{year}-12-31" for year in self.full_range if year not in years_absent)
        )
        self.assertNoHolidayName(name, years_absent)

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "Tahun Baru Masehi"),
            ("2022-02-01", "Tahun Baru Imlek"),
            ("2022-02-28", "Isra Mikraj Nabi Muhammad"),
            ("2022-03-03", "Hari Suci Nyepi"),
            ("2022-04-15", "Wafat Yesus Kristus"),
            ("2022-04-29", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2022-05-01", "Hari Buruh Internasional"),
            ("2022-05-02", "Hari Raya Idul Fitri"),
            ("2022-05-03", "Hari kedua dari Hari Raya Idul Fitri"),
            ("2022-05-04", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2022-05-05", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2022-05-06", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2022-05-16", "Hari Raya Waisak"),
            ("2022-05-26", "Kenaikan Yesus Kristus"),
            ("2022-06-01", "Hari Lahir Pancasila"),
            ("2022-07-10", "Hari Raya Idul Adha"),
            ("2022-07-30", "Tahun Baru Islam"),
            ("2022-08-17", "Hari Kemerdekaan Republik Indonesia"),
            ("2022-10-08", "Maulid Nabi Muhammad"),
            ("2022-12-25", "Hari Raya Natal"),
        )

    def test_2023(self):
        self.assertHolidaysInYear(
            2023,
            ("2023-01-01", "Tahun Baru Masehi"),
            ("2023-01-22", "Tahun Baru Imlek"),
            ("2023-01-23", "Cuti Bersama Tahun Baru Imlek"),
            ("2023-02-18", "Isra Mikraj Nabi Muhammad"),
            ("2023-03-22", "Hari Suci Nyepi"),
            ("2023-03-23", "Cuti Bersama Hari Suci Nyepi"),
            ("2023-04-07", "Wafat Yesus Kristus"),
            ("2023-04-19", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2023-04-20", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2023-04-21", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2023-04-22", "Hari Raya Idul Fitri"),
            ("2023-04-23", "Hari kedua dari Hari Raya Idul Fitri"),
            ("2023-04-24", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2023-04-25", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2023-05-01", "Hari Buruh Internasional"),
            ("2023-05-18", "Kenaikan Yesus Kristus"),
            ("2023-06-01", "Hari Lahir Pancasila"),
            ("2023-06-02", "Cuti Bersama Hari Raya Waisak"),
            ("2023-06-04", "Hari Raya Waisak"),
            ("2023-06-28", "Cuti Bersama Hari Raya Idul Adha"),
            ("2023-06-29", "Hari Raya Idul Adha"),
            ("2023-06-30", "Cuti Bersama Hari Raya Idul Adha"),
            ("2023-07-19", "Tahun Baru Islam"),
            ("2023-08-17", "Hari Kemerdekaan Republik Indonesia"),
            ("2023-09-28", "Maulid Nabi Muhammad"),
            ("2023-12-25", "Hari Raya Natal"),
            ("2023-12-26", "Cuti Bersama Hari Raya Natal"),
        )

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "Tahun Baru Masehi"),
            ("2024-02-08", "Isra Mikraj Nabi Muhammad"),
            ("2024-02-09", "Cuti Bersama Tahun Baru Imlek"),
            ("2024-02-10", "Tahun Baru Imlek"),
            ("2024-02-14", "Hari Pemilihan Umum"),
            ("2024-03-11", "Hari Suci Nyepi"),
            ("2024-03-12", "Cuti Bersama Hari Suci Nyepi"),
            ("2024-03-29", "Wafat Yesus Kristus"),
            ("2024-03-31", "Kebangkitan Yesus Kristus"),
            ("2024-04-08", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2024-04-09", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2024-04-10", "Hari Raya Idul Fitri"),
            ("2024-04-11", "Hari kedua dari Hari Raya Idul Fitri"),
            ("2024-04-12", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2024-04-15", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2024-05-01", "Hari Buruh Internasional"),
            ("2024-05-09", "Kenaikan Yesus Kristus"),
            ("2024-05-10", "Cuti Bersama Kenaikan Yesus Kristus"),
            ("2024-05-23", "Hari Raya Waisak"),
            ("2024-05-24", "Cuti Bersama Hari Raya Waisak"),
            ("2024-06-01", "Hari Lahir Pancasila"),
            ("2024-06-17", "Hari Raya Idul Adha"),
            ("2024-06-18", "Cuti Bersama Hari Raya Idul Adha"),
            ("2024-07-07", "Tahun Baru Islam"),
            ("2024-08-17", "Hari Kemerdekaan Republik Indonesia"),
            ("2024-09-16", "Maulid Nabi Muhammad"),
            ("2024-11-27", "Hari Pemilihan Kepala Daerah"),
            ("2024-12-25", "Hari Raya Natal"),
            ("2024-12-26", "Cuti Bersama Hari Raya Natal"),
            ("2024-12-31", "Libur Bursa"),
        )

    def test_2026(self):
        self.assertHolidaysInYear(
            2026,
            ("2026-01-01", "Tahun Baru Masehi"),
            ("2026-01-16", "Isra Mikraj Nabi Muhammad"),
            ("2026-02-16", "Cuti Bersama Tahun Baru Imlek"),
            ("2026-02-17", "Tahun Baru Imlek"),
            ("2026-03-18", "Cuti Bersama Hari Suci Nyepi"),
            ("2026-03-19", "Hari Suci Nyepi"),
            ("2026-03-20", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2026-03-21", "Hari Raya Idul Fitri"),
            ("2026-03-22", "Hari kedua dari Hari Raya Idul Fitri"),
            ("2026-03-23", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2026-03-24", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2026-04-03", "Wafat Yesus Kristus"),
            ("2026-04-05", "Kebangkitan Yesus Kristus"),
            ("2026-05-01", "Hari Buruh Internasional"),
            ("2026-05-14", "Kenaikan Yesus Kristus"),
            ("2026-05-15", "Cuti Bersama Kenaikan Yesus Kristus"),
            ("2026-05-27", "Hari Raya Idul Adha"),
            ("2026-05-28", "Cuti Bersama Hari Raya Idul Adha"),
            ("2026-05-31", "Hari Raya Waisak"),
            ("2026-06-01", "Hari Lahir Pancasila"),
            ("2026-06-16", "Tahun Baru Islam"),
            ("2026-08-17", "Hari Kemerdekaan Republik Indonesia"),
            ("2026-08-25", "Maulid Nabi Muhammad"),
            ("2026-12-24", "Cuti Bersama Hari Raya Natal"),
            ("2026-12-25", "Hari Raya Natal"),
            ("2026-12-31", "Libur Bursa"),
        )

    def test_2027(self):
        self.assertHolidaysInYear(
            2027,
            ("2027-01-01", "Tahun Baru Masehi"),
            ("2027-01-05", "Isra Mikraj Nabi Muhammad"),
            ("2027-02-05", "Cuti Bersama Tahun Baru Imlek"),
            ("2027-02-06", "Tahun Baru Imlek"),
            ("2027-03-08", "Hari Suci Nyepi"),
            ("2027-03-09", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2027-03-10", "Hari Raya Idul Fitri (perkiraan)"),
            ("2027-03-11", "Hari kedua dari Hari Raya Idul Fitri (perkiraan)"),
            ("2027-03-12", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2027-03-15", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2027-03-25", "Cuti Bersama Wafat Yesus Kristus"),
            ("2027-03-26", "Wafat Yesus Kristus"),
            ("2027-03-28", "Kebangkitan Yesus Kristus"),
            ("2027-05-01", "Hari Buruh Internasional"),
            ("2027-05-06", "Kenaikan Yesus Kristus"),
            ("2027-05-17", "Hari Raya Idul Adha (perkiraan)"),
            ("2027-05-18", "Cuti Bersama Hari Raya Idul Adha"),
            ("2027-05-19", "Cuti Bersama Hari Raya Waisak"),
            ("2027-05-20", "Hari Raya Waisak"),
            ("2027-06-01", "Hari Lahir Pancasila"),
            ("2027-06-06", "Tahun Baru Islam"),
            ("2027-08-15", "Maulid Nabi Muhammad"),
            ("2027-08-17", "Hari Kemerdekaan Republik Indonesia"),
            ("2027-12-24", "Cuti Bersama Hari Raya Natal"),
            ("2027-12-25", "Hari Raya Natal"),
            ("2027-12-26", "Isra Mikraj Nabi Muhammad"),
            ("2027-12-31", "Libur Bursa"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Tahun Baru Masehi"),
            ("2025-01-27", "Isra Mikraj Nabi Muhammad"),
            ("2025-01-28", "Cuti Bersama Tahun Baru Imlek"),
            ("2025-01-29", "Tahun Baru Imlek"),
            ("2025-03-28", "Cuti Bersama Hari Suci Nyepi"),
            ("2025-03-29", "Hari Suci Nyepi"),
            ("2025-03-31", "Hari Raya Idul Fitri"),
            ("2025-04-01", "Hari kedua dari Hari Raya Idul Fitri"),
            ("2025-04-02", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2025-04-03", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2025-04-04", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2025-04-07", "Cuti Bersama Hari Raya Idul Fitri"),
            ("2025-04-18", "Wafat Yesus Kristus"),
            ("2025-04-20", "Kebangkitan Yesus Kristus"),
            ("2025-05-01", "Hari Buruh Internasional"),
            ("2025-05-12", "Hari Raya Waisak"),
            ("2025-05-13", "Cuti Bersama Hari Raya Waisak"),
            ("2025-05-29", "Kenaikan Yesus Kristus"),
            ("2025-05-30", "Cuti Bersama Kenaikan Yesus Kristus"),
            ("2025-06-01", "Hari Lahir Pancasila"),
            ("2025-06-06", "Hari Raya Idul Adha"),
            ("2025-06-09", "Cuti Bersama Hari Raya Idul Adha"),
            ("2025-06-27", "Tahun Baru Islam"),
            ("2025-08-17", "Hari Kemerdekaan Republik Indonesia"),
            ("2025-08-18", "Cuti Bersama Hari Kemerdekaan Republik Indonesia"),
            ("2025-09-05", "Maulid Nabi Muhammad"),
            ("2025-12-25", "Hari Raya Natal"),
            ("2025-12-26", "Cuti Bersama Hari Raya Natal"),
            ("2025-12-31", "Libur Bursa"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-27", "Isra' and Mi'raj"),
            ("2025-01-28", "Lunar New Year Joint Holiday"),
            ("2025-01-29", "Lunar New Year"),
            ("2025-03-28", "Day of Silence Joint Holiday"),
            ("2025-03-29", "Day of Silence"),
            ("2025-03-31", "Eid al-Fitr"),
            ("2025-04-01", "Eid al-Fitr Second Day"),
            ("2025-04-02", "Eid al-Fitr Joint Holiday"),
            ("2025-04-03", "Eid al-Fitr Joint Holiday"),
            ("2025-04-04", "Eid al-Fitr Joint Holiday"),
            ("2025-04-07", "Eid al-Fitr Joint Holiday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-20", "Easter Sunday"),
            ("2025-05-01", "International Labor Day"),
            ("2025-05-12", "Vesak Day"),
            ("2025-05-13", "Vesak Joint Holiday"),
            ("2025-05-29", "Ascension Day"),
            ("2025-05-30", "Ascension Joint Holiday"),
            ("2025-06-01", "Pancasila Day"),
            ("2025-06-06", "Eid al-Adha"),
            ("2025-06-09", "Eid al-Adha Joint Holiday"),
            ("2025-06-27", "Islamic New Year"),
            ("2025-08-17", "Independence Day"),
            ("2025-08-18", "Independence Day Joint Holiday"),
            ("2025-09-05", "Prophet's Birthday"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Christmas Joint Holiday"),
            ("2025-12-31", "Exchange Holiday"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2025-01-01", "วันขึ้นปีใหม่"),
            ("2025-01-27", "วันเมี๊ยะราจ"),
            ("2025-01-28", "หยุดร่วมพิเศษวันตรุษจีน"),
            ("2025-01-29", "วันตรุษจีน"),
            ("2025-03-28", "หยุดร่วมพิเศษวันแห่งความเงียบ"),
            ("2025-03-29", "วันแห่งความเงียบ"),
            ("2025-03-31", "วันอีฎิ้ลฟิตริ"),
            ("2025-04-01", "วันอีฎิ้ลฟิตริวันที่สอง"),
            ("2025-04-02", "หยุดร่วมพิเศษวันอีฎิ้ลฟิตริ"),
            ("2025-04-03", "หยุดร่วมพิเศษวันอีฎิ้ลฟิตริ"),
            ("2025-04-04", "หยุดร่วมพิเศษวันอีฎิ้ลฟิตริ"),
            ("2025-04-07", "หยุดร่วมพิเศษวันอีฎิ้ลฟิตริ"),
            ("2025-04-18", "วันศุกร์ประเสริฐ"),
            ("2025-04-20", "วันอาทิตย์อีสเตอร์"),
            ("2025-05-01", "วันแรงงานสากล"),
            ("2025-05-12", "วันวิสาขบูชา"),
            ("2025-05-13", "หยุดร่วมพิเศษวันวิสาขบูชา"),
            ("2025-05-29", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2025-05-30", "หยุดร่วมพิเศษวันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2025-06-01", "วันปัญจศีล"),
            ("2025-06-06", "วันอีดิ้ลอัฎฮา"),
            ("2025-06-09", "หยุดร่วมพิเศษวันอีดิ้ลอัฎฮา"),
            ("2025-06-27", "วันขึ้นปีใหม่อิสลาม"),
            ("2025-08-17", "วันประกาศอิสรภาพสาธารณรัฐอินโดนีเซีย"),
            ("2025-08-18", "หยุดร่วมพิเศษวันประกาศอิสรภาพสาธารณรัฐอินโดนีเซีย"),
            ("2025-09-05", "วันเมาลิดนบี"),
            ("2025-12-25", "วันคริสต์มาส"),
            ("2025-12-26", "หยุดร่วมพิเศษวันคริสต์มาส"),
            ("2025-12-31", "วันหยุดตลาดหลักทรัพย์"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2025-01-01", "Новий рік"),
            ("2025-01-27", "Вознесіння пророка Мухаммада"),
            ("2025-01-28", "Додатковий вихідний на Китайський Новий рік"),
            ("2025-01-29", "Китайський Новий рік"),
            ("2025-03-28", "Додатковий вихідний на Священний день тиші"),
            ("2025-03-29", "День тиші"),
            ("2025-03-31", "Рамазан-байрам"),
            ("2025-04-01", "Другий день Рамазан-байрам"),
            ("2025-04-02", "Додатковий вихідний на Рамазан-байрам"),
            ("2025-04-03", "Додатковий вихідний на Рамазан-байрам"),
            ("2025-04-04", "Додатковий вихідний на Рамазан-байрам"),
            ("2025-04-07", "Додатковий вихідний на Рамазан-байрам"),
            ("2025-04-18", "Страсна пʼятниця"),
            ("2025-04-20", "Великдень"),
            ("2025-05-01", "Міжнародний день праці"),
            ("2025-05-12", "День народження Будди"),
            ("2025-05-13", "Додатковий вихідний на День народження Будди"),
            ("2025-05-29", "Вознесіння Господнє"),
            ("2025-05-30", "Додатковий вихідний на Вознесіння Господнє"),
            ("2025-06-01", "День Панчасіла"),
            ("2025-06-06", "Курбан-байрам"),
            ("2025-06-09", "Додатковий вихідний на Курбан-байрам"),
            ("2025-06-27", "Ісламський Новий рік"),
            ("2025-08-17", "День незалежності Республіки Індонезія"),
            ("2025-08-18", "Додатковий вихідний на День незалежності Республіки Індонезія"),
            ("2025-09-05", "День народження пророка Мухаммада"),
            ("2025-12-25", "Різдво Христове"),
            ("2025-12-26", "Додатковий вихідний на Різдво Христове"),
            ("2025-12-31", "Вихідний день біржі"),
        )
