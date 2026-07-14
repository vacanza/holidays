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

from holidays.financial.london_stock_exchange import LondonStockExchange, XLON, LSE
from tests.common import CommonFinancialTests


class TestLondonStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(LondonStockExchange)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_market_aliases(self):
        self.assertAliases(LondonStockExchange, XLON, LSE)

    def test_no_holidays(self):
        self.assertNoHolidays(LondonStockExchange(years=1999))

    def test_2022(self):
        # Exercises the royal one-off bank holidays alongside the regular
        # England & Wales calendar; year-by-year correctness of the underlying
        # calendar itself is covered by the United Kingdom test suite.
        # New Year's Day (Sat) and Christmas Day (Sun) are not trading days in their
        # own right, so only their observed weekday substitutes appear.
        self.assertHolidaysInYear(
            2022,
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-02", "May Day"),
            ("2022-06-02", "Spring Bank Holiday"),
            ("2022-06-03", "Platinum Jubilee of Elizabeth II"),
            ("2022-08-29", "Late Summer Bank Holiday"),
            ("2022-09-19", "State Funeral of Queen Elizabeth II"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_weekend_holidays_are_not_trading_days(self):
        # The exchange is shut at weekends, so a bank holiday landing on a Saturday
        # or Sunday is dropped and only its observed substitute remains.
        self.assertNoHoliday("2011-01-01", "2011-12-25", "2022-01-01", "2022-12-25")
        self.assertHoliday("2011-01-03", "2011-12-27", "2022-01-03", "2022-12-27")

    def test_christmas_eve(self):
        name = "Christmas Eve (markets close at 12:30pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(name, self.full_range)
        # Moved back to the preceding Friday when Dec 24 falls on a weekend.
        self.assertHalfDayHolidayName(
            name,
            "2011-12-23",  # Dec 24 fell on a Saturday.
            "2017-12-22",  # Dec 24 fell on a Sunday.
            "2024-12-24",  # Dec 24 fell on a Tuesday.
        )

    def test_new_years_eve(self):
        name = "New Year's Eve (markets close at 12:30pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(name, self.full_range)
        # Moved back to the preceding Friday when Dec 31 falls on a weekend.
        self.assertHalfDayHolidayName(
            name,
            "2011-12-30",  # Dec 31 fell on a Saturday.
            "2017-12-29",  # Dec 31 fell on a Sunday.
            "2024-12-31",  # Dec 31 fell on a Tuesday.
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-06", "May Day"),
            ("2024-05-27", "Spring Bank Holiday"),
            ("2024-08-26", "Late Summer Bank Holiday"),
            ("2024-12-24", "Christmas Eve (markets close at 12:30pm)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
            ("2024-12-31", "New Year's Eve (markets close at 12:30pm)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-06", "May Day"),
            ("2024-05-27", "Spring Bank Holiday"),
            ("2024-08-26", "Late Summer Bank Holiday"),
            ("2024-12-24", "Christmas Eve (markets close at 12:30pm)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
            ("2024-12-31", "New Year's Eve (markets close at 12:30pm)"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2024-01-01", "วันขึ้นปีใหม่"),
            ("2024-03-29", "วันศุกร์ประเสริฐ"),
            ("2024-04-01", "วันจันทร์อีสเตอร์"),
            ("2024-05-06", "วันเมย์เดย์"),
            ("2024-05-27", "วันหยุดฤดูใบไม้ผลิของธนาคาร"),
            ("2024-08-26", "วันหยุดช่วงปลายฤดูร้อนของธนาคาร"),
            ("2024-12-24", "วันคริสต์มาสอีฟ (ตลาดปิดเวลา 12:30 น.)"),
            ("2024-12-25", "วันคริสต์มาส"),
            ("2024-12-26", "วันเปิดกล่องของขวัญ"),
            ("2024-12-31", "วันสิ้นปี (ตลาดปิดเวลา 12:30 น.)"),
        )
