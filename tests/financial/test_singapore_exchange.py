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

from holidays.financial.singapore_exchange import SingaporeExchange
from tests.common import CommonFinancialTests


class TestSingaporeExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full_range = range(2000, 2027)
        super().setUpClass(SingaporeExchange)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_christmas_eve(self):
        name = "Christmas Eve (markets close at 12:00 p.m. SGT)"
        years_absent = {2000, 2005, 2006, 2011, 2016, 2017, 2022, 2023}
        self.assertNoHolidayName(name)
        self.assertNoHalfDayHolidayName(name, (f"{year}-12-24" for year in years_absent))
        self.assertHalfDayNonObservedHolidayName(
            name, (f"{year}-12-24" for year in self.full_range if year not in years_absent)
        )

    def test_new_years_eve(self):
        name = "New Year's Eve (markets close at 12:00 p.m. SGT)"
        years_absent = {2000, 2005, 2006, 2011, 2016, 2017, 2022, 2023}
        self.assertNoHolidayName(name)
        self.assertNoHalfDayHolidayName(name, (f"{year}-12-31" for year in years_absent))
        self.assertHalfDayNonObservedHolidayName(
            name, (f"{year}-12-31" for year in self.full_range if year not in years_absent)
        )

    def test_chinese_new_years_eve(self):
        name = "Chinese New Year's Eve (markets close at 12:00 p.m. SGT)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "2020-01-24",
            "2021-02-11",
            "2022-01-31",
            "2024-02-09",
            "2025-01-28",
            "2026-02-16",
        )
        self.assertNoHalfDayHolidayName(
            name,
            "2023-01-21",
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "New Year's Day"),
            ("2025-01-29", "Chinese New Year"),
            ("2025-01-30", "Chinese New Year"),
            ("2025-03-31", "Hari Raya Puasa"),
            ("2025-04-18", "Good Friday"),
            ("2025-05-01", "Labour Day"),
            ("2025-05-12", "Vesak Day"),
            ("2025-10-20", "Deepavali"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_half_day_2025(self):
        self.assertHalfDayHolidaysInYear(
            2025,
            ("2025-01-28", "Chinese New Year's Eve (markets close at 12:00 p.m. SGT)"),
            ("2025-12-24", "Christmas Eve (markets close at 12:00 p.m. SGT)"),
            ("2025-12-31", "New Year's Eve (markets close at 12:00 p.m. SGT)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-02-09", "Chinese New Year's Eve (markets close at 12:00 p.m. SGT)"),
            ("2024-02-12", "Chinese New Year"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-10", "Hari Raya Puasa"),
            ("2024-05-01", "Labour Day"),
            ("2024-05-22", "Vesak Day"),
            ("2024-06-17", "Hari Raya Haji"),
            ("2024-08-09", "National Day"),
            ("2024-10-31", "Deepavali"),
            ("2024-12-24", "Christmas Eve (markets close at 12:00 p.m. SGT)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-31", "New Year's Eve (markets close at 12:00 p.m. SGT)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-02-09", "Chinese New Year's Eve (markets close at 12:00 p.m. SGT)"),
            ("2024-02-12", "Chinese New Year"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-22", "Vesak Day"),
            ("2024-06-17", "Eid al-Adha"),
            ("2024-08-09", "National Day"),
            ("2024-10-31", "Deepavali"),
            ("2024-12-24", "Christmas Eve (markets close at 12:00 p.m. SGT)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-31", "New Year's Eve (markets close at 12:00 p.m. SGT)"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2024-01-01", "วันขึ้นปีใหม่"),
            ("2024-02-09", "วันสิ้นปีจีน (ตลาดปิดเวลา 12:00 น. SGT)"),
            ("2024-02-12", "วันตรุษจีน"),
            ("2024-03-29", "วันศุกร์ประเสริฐ"),
            ("2024-04-10", "วันอีฎิ้ลฟิตริ"),
            ("2024-05-01", "วันแรงงาน"),
            ("2024-05-22", "วันวิสาขบูชา"),
            ("2024-06-17", "วันอีดิ้ลอัฎฮา"),
            ("2024-08-09", "วันชาติสิงคโปร์"),
            ("2024-10-31", "วันดีปาวลี"),
            ("2024-12-24", "วันคริสต์มาสอีฟ (ตลาดปิดเวลา 12:00 น. SGT)"),
            ("2024-12-25", "วันคริสต์มาส"),
            ("2024-12-31", "วันสิ้นปี (ตลาดปิดเวลา 12:00 น. SGT)"),
        )
