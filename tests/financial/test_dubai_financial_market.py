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

from holidays.financial.dubai_financial_market import DubaiFinancialMarket
from tests.common import CommonFinancialTests


class TestDubaiFinancialMarket(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(DubaiFinancialMarket)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_special_holidays(self):
        self.assertHolidayName("اليوم الوطني", "2023-12-04")
        self.assertHolidayName("إغلاق السوق", "2026-03-02", "2026-03-03")

    def test_weekend_holidays_are_not_trading_days(self):
        self.assertNoHoliday(
            "2023-01-01",
            "2023-04-22",
            "2023-04-23",
            "2023-12-02",
            "2023-12-03",
            "2024-06-15",
            "2024-06-16",
            "2024-07-07",
            "2024-09-15",
            "2025-03-30",
            "2025-06-07",
            "2025-06-08",
            "2026-03-21",
            "2026-03-22",
        )

    def test_2023(self):
        self.assertHolidays(
            DubaiFinancialMarket(years=2023),
            ("2023-04-20", "عطلة عيد الفطر"),
            ("2023-04-21", "عيد الفطر"),
            ("2023-06-27", "وقفة عرفة"),
            ("2023-06-28", "عيد الأضحى"),
            ("2023-06-29", "عطلة عيد الأضحى"),
            ("2023-06-30", "عطلة عيد الأضحى"),
            ("2023-07-21", "رأس السنة الهجرية"),
            ("2023-09-29", "عيد المولد النبوي"),
            ("2023-12-01", "يوم الشهيد"),
            ("2023-12-04", "اليوم الوطني"),
        )

    def test_2024(self):
        self.assertHolidays(
            DubaiFinancialMarket(years=2024),
            ("2024-01-01", "رأس السنة الميلادية"),
            ("2024-04-08", "عطلة عيد الفطر"),
            ("2024-04-09", "عطلة عيد الفطر"),
            ("2024-04-10", "عيد الفطر"),
            ("2024-04-11", "عطلة عيد الفطر"),
            ("2024-04-12", "عطلة عيد الفطر"),
            ("2024-06-17", "عطلة عيد الأضحى"),
            ("2024-06-18", "عطلة عيد الأضحى"),
            ("2024-12-02", "اليوم الوطني"),
            ("2024-12-03", "اليوم الوطني"),
        )

    def test_2025(self):
        self.assertHolidays(
            DubaiFinancialMarket(years=2025),
            ("2025-01-01", "رأس السنة الميلادية"),
            ("2025-03-31", "عطلة عيد الفطر"),
            ("2025-04-01", "عطلة عيد الفطر"),
            ("2025-06-05", "وقفة عرفة"),
            ("2025-06-06", "عيد الأضحى"),
            ("2025-06-27", "رأس السنة الهجرية"),
            ("2025-09-05", "عيد المولد النبوي"),
            ("2025-12-01", "اليوم الوطني"),
            ("2025-12-02", "اليوم الوطني"),
        )

    def test_2026(self):
        self.assertHolidays(
            DubaiFinancialMarket(years=2026),
            ("2026-01-01", "رأس السنة الميلادية"),
            ("2026-03-02", "إغلاق السوق"),
            ("2026-03-03", "إغلاق السوق"),
            ("2026-03-19", "عطلة عيد الفطر"),
            ("2026-03-20", "عيد الفطر"),
            ("2026-05-26", "وقفة عرفة"),
            ("2026-05-27", "عيد الأضحى"),
            ("2026-05-28", "عطلة عيد الأضحى"),
            ("2026-05-29", "عطلة عيد الأضحى"),
            ("2026-06-15", "رأس السنة الهجرية"),
            ("2026-08-28", "عيد المولد النبوي"),
            ("2026-12-02", "اليوم الوطني"),
            ("2026-12-03", "اليوم الوطني"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2026-01-01", "رأس السنة الميلادية"),
            ("2026-03-02", "إغلاق السوق"),
            ("2026-03-03", "إغلاق السوق"),
            ("2026-03-19", "عطلة عيد الفطر"),
            ("2026-03-20", "عيد الفطر"),
            ("2026-05-26", "وقفة عرفة"),
            ("2026-05-27", "عيد الأضحى"),
            ("2026-05-28", "عطلة عيد الأضحى"),
            ("2026-05-29", "عطلة عيد الأضحى"),
            ("2026-06-15", "رأس السنة الهجرية"),
            ("2026-08-28", "عيد المولد النبوي"),
            ("2026-12-02", "اليوم الوطني"),
            ("2026-12-03", "اليوم الوطني"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2026-01-01", "New Year's Day"),
            ("2026-03-02", "Market Closure"),
            ("2026-03-03", "Market Closure"),
            ("2026-03-19", "Eid al-Fitr Holiday"),
            ("2026-03-20", "Eid al-Fitr"),
            ("2026-05-26", "Day of Arafah"),
            ("2026-05-27", "Eid al-Adha"),
            ("2026-05-28", "Eid al-Adha Holiday"),
            ("2026-05-29", "Eid al-Adha Holiday"),
            ("2026-06-15", "Islamic New Year"),
            ("2026-08-28", "Prophet's Birthday"),
            ("2026-12-02", "National Day"),
            ("2026-12-03", "National Day"),
        )

    def test_l10n_ur_pk(self):
        self.assertLocalizedHolidays(
            "ur_PK",
            ("2026-01-01", "نئے سال کا دن"),
            ("2026-03-02", "مارکیٹ کی بندش"),
            ("2026-03-03", "مارکیٹ کی بندش"),
            ("2026-03-19", "عید الفطر کی تعطیل"),
            ("2026-03-20", "عید الفطر"),
            ("2026-05-26", "یوم عرفہ"),
            ("2026-05-27", "عید الاضحی"),
            ("2026-05-28", "عید الاضحی کی تعطیل"),
            ("2026-05-29", "عید الاضحی کی تعطیل"),
            ("2026-06-15", "اسلامی نیا سال"),
            ("2026-08-28", "عید میلاد النبی"),
            ("2026-12-02", "قومی دن"),
            ("2026-12-03", "قومی دن"),
        )
