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

from holidays.financial.johannesburg_stock_exchange import JohannesburgStockExchange
from tests.common import CommonFinancialTests


class TestJohannesburgStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(JohannesburgStockExchange)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_christmas_eve(self):
        name = "Christmas Eve (markets close at 12:00 p.m. SAST)"
        self.assertNoHolidayName(name)
        self.assertHalfDayNonObservedHolidayName(
            name, (f"{year}-12-24" for year in self.full_range)
        )
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

    def test_new_years_eve(self):
        name = "New Year's Eve (markets close at 12:00 p.m. SAST)"
        self.assertNoHolidayName(name)
        self.assertHalfDayNonObservedHolidayName(
            name, (f"{year}-12-31" for year in self.full_range)
        )
        self.assertHalfDayHolidayName(
            name,
            "2020-12-31",
            "2021-12-31",
            "2024-12-31",
            "2025-12-31",
            "2026-12-31",
        )
        self.assertNoHalfDayHolidayName(
            name,
            "2022-12-31",
            "2023-12-31",
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "New Year's Day"),
            ("2025-03-21", "Human Rights Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Family Day"),
            ("2025-04-28", "Freedom Day"),
            ("2025-05-01", "Workers' Day"),
            ("2025-06-16", "Youth Day"),
            ("2025-09-24", "Heritage Day"),
            ("2025-12-16", "Day of Reconciliation"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Day of Goodwill"),
        )

    def test_half_day_2025(self):
        self.assertHalfDayHolidaysInYear(
            2025,
            ("2025-12-24", "Christmas Eve (markets close at 12:00 p.m. SAST)"),
            ("2025-12-31", "New Year's Eve (markets close at 12:00 p.m. SAST)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-03-21", "Human Rights Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Family Day"),
            ("2024-05-01", "Workers' Day"),
            ("2024-05-29", "National and Provincial Government Elections"),
            ("2024-06-17", "Youth Day"),
            ("2024-08-09", "National Women's Day"),
            ("2024-09-24", "Heritage Day"),
            ("2024-12-16", "Day of Reconciliation"),
            ("2024-12-24", "Christmas Eve (markets close at 12:00 p.m. SAST)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Day of Goodwill"),
            ("2024-12-31", "New Year's Eve (markets close at 12:00 p.m. SAST)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-21", "Human Rights Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Family Day"),
            ("2024-05-01", "Workers' Day"),
            ("2024-05-29", "National and Provincial Government Elections"),
            ("2024-06-17", "Youth Day"),
            ("2024-08-09", "National Women's Day"),
            ("2024-09-24", "Heritage Day"),
            ("2024-12-16", "Day of Reconciliation"),
            ("2024-12-24", "Christmas Eve (markets close at 12:00 p.m. SAST)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Day of Goodwill"),
            ("2024-12-31", "New Year's Eve (markets close at 12:00 p.m. SAST)"),
        )

    def test_l10n_ur_pk(self):
        self.assertLocalizedHolidays(
            "ur_PK",
            ("2024-01-01", "نئے سال کا دن"),
            ("2024-03-21", "انسانی حقوق کا دن"),
            ("2024-03-29", "گڈ فرائیڈے"),
            ("2024-04-01", "خاندانی دن"),
            ("2024-05-01", "یوم مزدور"),
            ("2024-05-29", "قومی اور صوبائی حکومت کے انتخابات"),
            ("2024-06-17", "یوم نوجوانان"),
            ("2024-08-09", "خواتین کا قومی دن"),
            ("2024-09-24", "یوم ورثہ"),
            ("2024-12-16", "یوم مصالحت"),
            ("2024-12-24", "کرسمس کی شام (مارکیٹیں دوپہر 12:00 بجے SAST بند ہوتی ہیں)"),
            ("2024-12-25", "کرسمس کا دن"),
            ("2024-12-26", "یوم خیر سگالی"),
            ("2024-12-31", "نئے سال کی شام (مارکیٹیں دوپہر 12:00 بجے SAST بند ہوتی ہیں)"),
        )
