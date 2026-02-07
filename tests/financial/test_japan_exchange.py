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

from datetime import date
from unittest import TestCase

from holidays.financial.japan_exchange import JapanExchange
from tests.common import CommonFinancialTests


class TestJapanExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(JapanExchange)

    def test_no_holidays(self):
        super().test_no_holidays()

    def test_market_holidays(self):
        """Test market-specific holidays: Jan 2, Jan 3, Dec 31."""
        # January 2 - only weekdays
        self.assertHolidayName(
            "市場休業日",  # Market Holiday
            "2020-01-02",
            "2024-01-02",
        )
        # January 3 - only weekdays
        self.assertHolidayName(
            "市場休業日",  # Market Holiday
            "2020-01-03",
            "2024-01-03",
        )
        # December 31 - only weekdays
        self.assertHolidayName(
            "市場休業日",  # Market Holiday
            "2020-12-31",
            "2024-12-31",
        )
        # Weekends should not be market holidays
        jpx = JapanExchange(years=2021)
        # 2021-01-02 is Saturday, should not be a holiday
        self.assertNotIn(date(2021, 1, 2), jpx)
        # 2021-01-03 is Sunday, should not be a holiday
        self.assertNotIn(date(2021, 1, 3), jpx)

    def test_substitute_holiday(self):
        """Test substitute holidays when holidays fall on Sunday.

        Coverage test: Dec 31, 2023 is Sunday.
        """
        # 2022-01-02 is Sunday - should not be a market holiday
        # 2023-12-31 is Sunday - should not be a market holiday
        jpx_2022 = JapanExchange(years=2022)
        self.assertNotIn(date(2022, 1, 2), jpx_2022)

        jpx_2023 = JapanExchange(years=2023)
        self.assertNotIn(date(2023, 12, 31), jpx_2023)

    def test_citizens_holiday(self):
        """Test bridge holidays (Citizens' Holidays)."""
        # 2026-09-22 is Silver Week (Citizens' Holiday)
        self.assertHolidayName(
            "国民の休日",  # Citizens' Holiday
            "2026-09-22",
        )
        # Coverage for bridge holiday: check 2026 has the Citizens' Holiday
        jpx_2026 = JapanExchange(years=2026)
        self.assertIn(date(2026, 9, 22), jpx_2026)

    def test_special_bank_holidays(self):
        """Test special bank holidays for specific years."""
        # 2019 Imperial events
        jpx_2019 = JapanExchange(years=2019)
        self.assertIn(date(2019, 4, 30), jpx_2019)
        self.assertIn(date(2019, 5, 1), jpx_2019)
        self.assertIn(date(2019, 5, 2), jpx_2019)
        self.assertIn(date(2019, 5, 6), jpx_2019)
