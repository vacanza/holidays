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
        """JPX‑specific market holidays: Jan 2, Jan 3, Dec 31 (weekdays only)."""
        # Weekday occurrences should be holidays.
        self.assertHolidayName(
            "市場休業日",  # Market Holiday
            "2020-01-02",
            "2024-01-02",
            "2020-01-03",
            "2024-01-03",
            "2020-12-31",
            "2024-12-31",
        )
        # Weekend occurrences should NOT be holidays.
        jpx = JapanExchange(years=2021)
        self.assertNotIn(date(2021, 1, 2), jpx)  # Saturday
        self.assertNotIn(date(2021, 1, 3), jpx)  # Sunday

    def test_substitute_holiday(self):
        """Substitute holidays are inherited from Japan; only JPX's weekday rule is tested here."""
        # 2022-01-02 (Sunday) – should not be a JPX holiday.
        self.assertNotIn(date(2022, 1, 2), JapanExchange(years=2022))
        # 2023-12-31 (Sunday) – should not be a JPX holiday.
        self.assertNotIn(date(2023, 12, 31), JapanExchange(years=2023))

    def test_citizens_holiday(self):
        """Citizens' Holiday (国民の休日) is inherited from Japan (e.g., Silver Week 2026)."""
        self.assertHolidayName(
            "国民の休日",  # Citizens' Holiday
            "2026-09-22",
        )

    def test_special_one_off_closures(self):
        """Static one‑off market closures (special bank holidays) are included."""
        jpx_2019 = JapanExchange(years=2019)
        self.assertIn(date(2019, 4, 30), jpx_2019)
        self.assertIn(date(2019, 5, 1), jpx_2019)
        self.assertIn(date(2019, 5, 2), jpx_2019)
        self.assertIn(date(2019, 5, 6), jpx_2019)
