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

from holidays.countries.malaysia import Malaysia
from holidays.financial.bursa_malaysia import BursaMalaysia
from tests.common import CommonFinancialTests


class TestBursaMalaysia(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full_range = range(2000, 2027)
        super().setUpClass(BursaMalaysia)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_no_weekend_holidays(self):
        for dt in self.holidays:
            self.assertLess(dt.weekday(), 5, f"{dt} is a weekend holiday")

    def test_matches_kuala_lumpur_weekdays(self):
        for year in (2024, 2025, 2026):
            kl_weekdays = {
                dt: name
                for dt, name in Malaysia(subdiv="14", years=year).items()
                if dt.weekday() < 5
            }
            self.assertEqual(dict(BursaMalaysia(years=year)), kl_weekdays)

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "Tahun Baharu"),
            ("2025-01-29", "Tahun Baharu Cina"),
            ("2025-01-30", "Tahun Baharu Cina (Hari Kedua)"),
            ("2025-02-11", "Hari Thaipusam"),
            ("2025-03-18", "Hari Nuzul Al-Quran"),
            ("2025-03-31", "Hari Raya Puasa"),
            ("2025-04-01", "Hari Raya Puasa (Hari Kedua)"),
            ("2025-05-01", "Hari Pekerja"),
            ("2025-05-12", "Hari Wesak"),
            ("2025-06-02", "Hari Keputeraan Rasmi Seri Paduka Baginda Yang di-Pertuan Agong"),
            ("2025-06-27", "Awal Muharam"),
            ("2025-09-01", "Cuti Hari Kebangsaan"),
            ("2025-09-05", "Hari Keputeraan Nabi Muhammad S.A.W."),
            ("2025-09-15", "Cuti Peristiwa"),
            ("2025-09-16", "Hari Malaysia"),
            ("2025-10-20", "Hari Deepavali"),
            ("2025-12-25", "Hari Krismas"),
        )

    def test_2026(self):
        self.assertHolidaysInYear(
            2026,
            ("2026-01-01", "Tahun Baharu"),
            ("2026-02-02", "Cuti Hari Thaipusam; Cuti Hari Wilayah Persekutuan"),
            ("2026-02-17", "Tahun Baharu Cina"),
            ("2026-02-18", "Tahun Baharu Cina (Hari Kedua)"),
            ("2026-03-20", "Hari Raya Puasa (pergantian hari)"),
            ("2026-03-23", "Cuti Hari Raya Puasa (Hari Kedua)"),
            ("2026-05-01", "Hari Pekerja"),
            ("2026-05-27", "Hari Raya Qurban"),
            ("2026-06-01", "Hari Keputeraan Rasmi Seri Paduka Baginda Yang di-Pertuan Agong"),
            ("2026-06-02", "Cuti Hari Wesak"),
            ("2026-06-17", "Awal Muharam"),
            ("2026-08-25", "Hari Keputeraan Nabi Muhammad S.A.W."),
            ("2026-08-31", "Hari Kebangsaan"),
            ("2026-09-16", "Hari Malaysia"),
            ("2026-11-09", "Cuti Hari Deepavali"),
            ("2026-12-25", "Hari Krismas"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Tahun Baharu"),
            ("2024-01-25", "Hari Thaipusam"),
            ("2024-02-01", "Hari Wilayah Persekutuan"),
            ("2024-02-12", "Cuti Tahun Baharu Cina (Hari Kedua)"),
            ("2024-03-28", "Hari Nuzul Al-Quran"),
            ("2024-04-10", "Hari Raya Puasa"),
            ("2024-04-11", "Hari Raya Puasa (Hari Kedua)"),
            ("2024-05-01", "Hari Pekerja"),
            ("2024-05-22", "Hari Wesak"),
            ("2024-06-03", "Hari Keputeraan Rasmi Seri Paduka Baginda Yang di-Pertuan Agong"),
            ("2024-06-17", "Hari Raya Qurban"),
            ("2024-09-16", "Hari Keputeraan Nabi Muhammad S.A.W.; Hari Malaysia"),
            ("2024-10-31", "Hari Deepavali"),
            ("2024-12-25", "Hari Krismas"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-25", "Thaipusam"),
            ("2024-02-01", "Federal Territory Day"),
            ("2024-02-12", "Chinese New Year (Second Day) (observed)"),
            ("2024-03-28", "Nuzul Al-Quran Day"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-04-11", "Eid al-Fitr (Second Day)"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-22", "Vesak Day"),
            ("2024-06-03", "Birthday of HM Yang di-Pertuan Agong"),
            ("2024-06-17", "Eid al-Adha"),
            ("2024-09-16", "Malaysia Day; Prophet Muhammad's Birthday"),
            ("2024-10-31", "Diwali"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2024-01-01", "วันขึ้นปีใหม่"),
            ("2024-01-25", "วันไทปูซัม"),
            ("2024-02-01", "วันเขตสหพันธรัฐ"),
            ("2024-02-12", "ชดเชยวันตรุษจีนวันที่สอง"),
            ("2024-03-28", "วันนูซุลอัลกุรอาน"),
            ("2024-04-10", "วันอีฎิ้ลฟิตริ"),
            ("2024-04-11", "วันอีฎิ้ลฟิตริวันที่สอง"),
            ("2024-05-01", "วันแรงงาน"),
            ("2024-05-22", "วันวิสาขบูชา"),
            ("2024-06-03", "วันคล้ายวันพระราชสมภพสมเด็จพระราชาธิบดีแห่งมาเลเซีย"),
            ("2024-06-17", "วันอีดิ้ลอัฎฮา"),
            ("2024-09-16", "วันเฉลิมฉลองการจัดตั้งสหพันธรัฐมาเลเซีย; วันเมาลิดนบี"),
            ("2024-10-31", "วันดีปาวลี"),
            ("2024-12-25", "วันคริสต์มาส"),
        )
