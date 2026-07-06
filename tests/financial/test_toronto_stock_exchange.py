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

from holidays.financial.toronto_stock_exchange import TorontoStockExchange
from tests.common import CommonFinancialTests


class TestTorontoStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(TorontoStockExchange)

    def test_special_holidays(self):
        self.assertHoliday("2008-12-17")

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertNonObservedHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2022-01-03",
            "2023-01-02",
        )

    def test_family_day(self):
        name = "Family Day"
        self.assertHolidayName(
            name,
            "2020-02-17",
            "2021-02-15",
            "2022-02-21",
            "2023-02-20",
            "2024-02-19",
            "2025-02-17",
        )
        self.assertHolidayName(name, range(2008, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2008))

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_victoria_day(self):
        name = "Victoria Day"
        self.assertHolidayName(
            name,
            "2020-05-18",
            "2021-05-24",
            "2022-05-23",
            "2023-05-22",
            "2024-05-20",
            "2025-05-19",
        )
        self.assertHolidayName(name, self.full_range)

    def test_canada_day(self):
        name = "Canada Day"
        self.assertNonObservedHolidayName(name, (f"{year}-07-01" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2006-07-03",
            "2007-07-02",
            "2012-07-02",
            "2017-07-03",
            "2018-07-02",
            "2023-07-03",
        )

    def test_civic_holiday(self):
        name = "Civic Holiday"
        self.assertHolidayName(
            name,
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
            "2025-08-04",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labour_day(self):
        name = "Labour Day"
        self.assertHolidayName(
            name,
            "2020-09-07",
            "2021-09-06",
            "2022-09-05",
            "2023-09-04",
            "2024-09-02",
            "2025-09-01",
        )
        self.assertHolidayName(name, self.full_range)

    def test_thanksgiving_day(self):
        name = "Thanksgiving Day"
        self.assertHolidayName(
            name,
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
            "2024-10-14",
            "2025-10-13",
        )
        self.assertHolidayName(name, self.full_range)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertNonObservedHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2004-12-27",
            "2005-12-27",
            "2010-12-27",
            "2011-12-26",
            "2016-12-26",
            "2017-12-25",
            "2021-12-27",
            "2022-12-26",
        )

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertNonObservedHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        self.assertHolidayName(
            name,
            "2004-12-28",
            "2005-12-26",
            "2010-12-28",
            "2011-12-27",
            "2016-12-27",
            "2017-12-26",
            "2021-12-28",
            "2022-12-27",
        )

    def test_christmas_eve_half_day(self):
        name = "Christmas Eve (markets close at 1:00 p.m. ET)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "2020-12-24",
            "2021-12-24",
            "2024-12-24",
            "2025-12-24",
            "2026-12-24",
        )
        self.assertNoHalfDayHolidayName(
            name,
            "2022-12-24",
            "2023-12-24",
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "New Year's Day"),
            ("2025-02-17", "Family Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-05-19", "Victoria Day"),
            ("2025-07-01", "Canada Day"),
            ("2025-08-04", "Civic Holiday"),
            ("2025-09-01", "Labour Day"),
            ("2025-10-13", "Thanksgiving Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_half_day_2025(self):
        self.assertHalfDayHolidaysInYear(
            2025,
            ("2025-12-24", "Christmas Eve (markets close at 1:00 p.m. ET)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2008-01-01", "New Year's Day"),
            ("2008-02-18", "Family Day"),
            ("2008-03-21", "Good Friday"),
            ("2008-05-19", "Victoria Day"),
            ("2008-07-01", "Canada Day"),
            ("2008-08-04", "Civic Holiday"),
            ("2008-09-01", "Labour Day"),
            ("2008-10-13", "Thanksgiving Day"),
            ("2008-12-17", "Market Closed (Computer Failure)"),
            ("2008-12-24", "Christmas Eve (markets close at 1:00 p.m. ET)"),
            ("2008-12-25", "Christmas Day"),
            ("2008-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2008-01-01", "New Year's Day"),
            ("2008-02-18", "Family Day"),
            ("2008-03-21", "Good Friday"),
            ("2008-05-19", "Victoria Day"),
            ("2008-07-01", "Canada Day"),
            ("2008-08-04", "Civic Holiday"),
            ("2008-09-01", "Labor Day"),
            ("2008-10-13", "Thanksgiving Day"),
            ("2008-12-17", "Market Closed (Computer Failure)"),
            ("2008-12-24", "Christmas Eve (markets close at 1:00 p.m. ET)"),
            ("2008-12-25", "Christmas Day"),
            ("2008-12-26", "Boxing Day"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2008-01-01", "Jour de l'an"),
            ("2008-02-18", "Fête de la famille"),
            ("2008-03-21", "Vendredi saint"),
            ("2008-05-19", "Fête de la Reine"),
            ("2008-07-01", "Fête du Canada"),
            ("2008-08-04", "Premier lundi d'août"),
            ("2008-09-01", "Fête du Travail"),
            ("2008-10-13", "Action de grâce"),
            ("2008-12-17", "Marché fermé (panne informatique)"),
            ("2008-12-24", "Veille de Noël (fermeture des marchés à 13h00 HE)"),
            ("2008-12-25", "Jour de Noël"),
            ("2008-12-26", "Boxing Day"),
        )

    def test_l10n_ar(self):
        self.assertLocalizedHolidays(
            "ar",
            ("2008-01-01", "يوم السنة الجديدة"),
            ("2008-02-18", "يوم العائلة"),
            ("2008-03-21", "الجمعة العظيمة"),
            ("2008-05-19", "يوم فيكتوريا"),
            ("2008-07-01", "يوم كندا"),
            ("2008-08-04", "عطلة المدنية"),
            ("2008-09-01", "عيد العمال"),
            ("2008-10-13", "عيد الشكر"),
            ("2008-12-17", "السوق مغلق (عطل في الكمبيوتر)"),
            ("2008-12-24", "عشية عيد الميلاد (تغلق الأسواق في الساعة 1:00 مساءً بالتوقيت الشرقي)"),
            ("2008-12-25", "عيد الميلاد"),
            ("2008-12-26", "يوم الملاكمة"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2008-01-01", "วันขึ้นปีใหม่"),
            ("2008-02-18", "วันครอบครัว"),
            ("2008-03-21", "วันศุกร์ประเสริฐ"),
            ("2008-05-19", "วันวิคตอเรีย"),
            ("2008-07-01", "วันชาติแคนาดา"),
            ("2008-08-04", "วันหยุดราชการ"),
            ("2008-09-01", "วันแรงงาน"),
            ("2008-10-13", "วันขอบคุณพระเจ้า"),
            ("2008-12-17", "ตลาดปิด (ระบบคอมพิวเตอร์ขัดข้อง)"),
            ("2008-12-24", "วันคริสต์มาสอีฟ (ตลาดปิดเวลา 13:00 น. ตามเวลา ET)"),
            ("2008-12-25", "วันคริสต์มาส"),
            ("2008-12-26", "วันเปิดกล่องของขวัญ"),
        )
