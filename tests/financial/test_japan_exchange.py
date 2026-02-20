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
        self.assertHoliday(JapanExchange(years=2024), "2024-02-12")

        # Additional substitute dates moved from special closures test.
        self.assertHoliday(JapanExchange(years=2019), "2019-05-06")
        self.assertHoliday(
            JapanExchange(years=2025),
            "2025-02-24",
            "2025-05-06",
            "2025-11-24",
        )

    def test_citizens_holiday(self):
        """Citizens' Holiday (国民の休日) is inherited from Japan (e.g., Silver Week 2026)."""
        self.assertHolidayName(
            "国民の休日",  # Citizens' Holiday
            "2026-09-22",
        )

    def test_special_one_off_closures(self):
        """Static one-off market closures (special bank holidays) are included."""
        jpx_2019 = JapanExchange(years=2019)
        self.assertHoliday(
            jpx_2019,
            "2019-04-30",
            "2019-05-01",
            "2019-05-02",
        )

    def test_no_holidays(self):
        """Testing years before JapanExchange's start_year (1949) to cover all branches."""
        self.assertNoHolidays(JapanExchange(years=1880))
        self.assertNoHolidays(JapanExchange(years=1948))

    def test_post_end_year(self):
        """Testing years after JapanExchange's end_year (2099) to cover all branches."""
        self.assertNoHolidays(JapanExchange(years=2101))

    def test_localized_holidays(self):
        """Validate localization for XJPX locale."""
        self.assertLocalizedHolidays(
            "en_US",
            ("1949-01-01", "New Year's Day"),
            ("1949-01-02", "Market Holiday"),
            ("1949-01-03", "Market Holiday"),
            ("1949-01-15", "Coming of Age Day"),
            ("1949-03-21", "Vernal Equinox Day"),
            ("1949-04-29", "Emperor's Birthday"),
            ("1949-05-03", "Constitution Day"),
            ("1949-05-05", "Children's Day"),
            ("1949-09-23", "Autumnal Equinox Day"),
            ("1949-11-03", "Culture Day"),
            ("1949-11-23", "Labor Thanksgiving Day"),
            ("1949-12-31", "Market Holiday"),
        )
        self.assertLocalizedHolidays(
            "ja",
            ("1949-01-01", "元日"),
            ("1949-01-02", "市場休業日"),
            ("1949-01-03", "市場休業日"),
            ("1949-01-15", "成人の日"),
            ("1949-03-21", "春分の日"),
            ("1949-04-29", "天皇誕生日"),
            ("1949-05-03", "憲法記念日"),
            ("1949-05-05", "こどもの日"),
            ("1949-09-23", "秋分の日"),
            ("1949-11-03", "文化の日"),
            ("1949-11-23", "勤労感謝の日"),
            ("1949-12-31", "市場休業日"),
        )
        self.assertLocalizedHolidays(
            "th",
            ("1949-01-01", "วันขึ้นปีใหม่"),
            ("1949-01-02", "วันหยุดตลาดหลักทรัพย์"),
            ("1949-01-03", "วันหยุดตลาดหลักทรัพย์"),
            ("1949-01-15", "วันฉลองบรรลุนิติภาวะ"),
            ("1949-03-21", "วันวสันตวิษุวัต"),
            ("1949-04-29", "วันคล้ายวันพระราชสมภพ สมเด็จพระจักรพรรดินารุฮิโตะ"),
            ("1949-05-03", "วันรัฐธรรมนูญ"),
            ("1949-05-05", "วันเด็กแห่งชาติ"),
            ("1949-09-23", "วันศารทวิษุวัต"),
            ("1949-11-03", "วันวัฒนธรรม"),
            ("1949-11-23", "วันขอบคุณแรงงาน"),
            ("1949-12-31", "วันหยุดตลาดหลักทรัพย์"),
        )

    def test_code(self):
        """Check market code availability while allowing country=None."""
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))
