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

from holidays.constants import PUBLIC
from holidays.financial.japan_exchange import JapanExchange
from tests.common import CommonFinancialTests


class TestJapanExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(JapanExchange)

    def test_init_categories_none(self):
        """Test initialization with categories=None."""
        jpx = JapanExchange(categories=None)
        self.assertIn(PUBLIC, jpx.categories)

    def test_market_holidays(self):
        """JPX-specific market holidays: Jan 2, Jan 3, Dec 31."""
        self.assertHolidayName(
            "市場休業日",  # Market Holiday
            "2020-01-02",
            "2024-01-02",
            "2020-01-03",
            "2024-01-03",
            "2020-12-31",
            "2024-12-31",
        )
        # These are holidays even on weekends.
        self.assertHolidayName(
            "市場休業日",
            "2021-01-02",  # Saturday
            "2021-01-03",  # Sunday
            "2022-01-02",  # Sunday
        )

    def test_substitute_holiday(self):
        """Verify inherited 振替休日 (substitute holiday)."""
        # 2024-02-11 is Sunday, so 2024-02-12 is a substitute holiday.
        self.assertIn(date(2024, 2, 12), JapanExchange(years=2024))

    def test_citizens_holiday(self):
        """Citizens' Holiday (国民の休日) is inherited from Japan (e.g., Silver Week 2026)."""
        self.assertHolidayName(
            "国民の休日",  # Citizens' Holiday
            "2026-09-22",
        )

    def test_special_one_off_closures(self):
        """Static one-off market closures (special bank holidays) are included."""
        jpx_2019 = JapanExchange(years=2019)
        self.assertIn(date(2019, 4, 30), jpx_2019)
        self.assertIn(date(2019, 5, 1), jpx_2019)
        self.assertIn(date(2019, 5, 2), jpx_2019)
        self.assertIn(date(2019, 5, 6), jpx_2019)

        jpx_2025 = JapanExchange(years=2025)
        self.assertIn(date(2025, 2, 24), jpx_2025)
        self.assertIn(date(2025, 5, 6), jpx_2025)
        self.assertIn(date(2025, 11, 24), jpx_2025)

    def test_no_holidays(self):
        """Testing years before JapanExchange's start_year (1948) to cover all branches."""
        self.assertNoHolidays(JapanExchange(years=1880))
        self.assertNoHolidays(JapanExchange(years=1947))

    def test_post_end_year(self):
        """Testing years after JapanExchange's end_year (2099) to cover all branches."""
        self.assertNoHolidays(JapanExchange(years=2101))
