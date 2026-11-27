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

from holidays.financial.japan_exchange import JapanExchange
from tests.common import CommonFinancialTests


class TestJapanExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(JapanExchange)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_first_trading_day_of_the_year(self):
        name = "大発会"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "2001-01-04",
            "2002-01-04",
            "2003-01-06",
            "2004-01-05",
            "2005-01-04",
            "2006-01-04",
            "2007-01-04",
            "2008-01-04",
            "2009-01-05",
        )
        self.assertHalfDayHolidayName(name, range(self.start_year, 2010))
        self.assertNoHalfDayHolidayName(name, range(2010, self.end_year))

    def test_last_trading_day_of_the_year(self):
        name = "大納会"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "2000-12-29",
            "2001-12-28",
            "2002-12-30",
            "2003-12-30",
            "2004-12-30",
            "2005-12-30",
            "2006-12-29",
            "2007-12-28",
            "2008-12-30",
        )
        self.assertHalfDayHolidayName(name, range(self.start_year, 2009))
        self.assertNoHalfDayHolidayName(name, range(2009, self.end_year))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2008-01-01", "元日; 銀行休業日"),
            ("2008-01-02", "銀行休業日"),
            ("2008-01-03", "銀行休業日"),
            ("2008-01-04", "大発会"),
            ("2008-01-14", "成人の日"),
            ("2008-02-11", "建国記念の日"),
            ("2008-03-20", "春分の日"),
            ("2008-04-29", "昭和の日"),
            ("2008-05-03", "憲法記念日"),
            ("2008-05-04", "みどりの日"),
            ("2008-05-05", "こどもの日"),
            ("2008-05-06", "振替休日"),
            ("2008-07-21", "海の日"),
            ("2008-09-15", "敬老の日"),
            ("2008-09-23", "秋分の日"),
            ("2008-10-13", "体育の日"),
            ("2008-11-03", "文化の日"),
            ("2008-11-23", "勤労感謝の日"),
            ("2008-11-24", "振替休日"),
            ("2008-12-23", "天皇誕生日"),
            ("2008-12-30", "大納会"),
            ("2008-12-31", "銀行休業日"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2008-01-01", "Bank Holiday; New Year's Day"),
            ("2008-01-02", "Bank Holiday"),
            ("2008-01-03", "Bank Holiday"),
            ("2008-01-04", "First Trading Day of the Year"),
            ("2008-01-14", "Coming of Age Day"),
            ("2008-02-11", "Foundation Day"),
            ("2008-03-20", "Vernal Equinox Day"),
            ("2008-04-29", "Showa Day"),
            ("2008-05-03", "Constitution Day"),
            ("2008-05-04", "Greenery Day"),
            ("2008-05-05", "Children's Day"),
            ("2008-05-06", "Substitute Holiday"),
            ("2008-07-21", "Marine Day"),
            ("2008-09-15", "Respect for the Aged Day"),
            ("2008-09-23", "Autumnal Equinox Day"),
            ("2008-10-13", "Physical Education Day"),
            ("2008-11-03", "Culture Day"),
            ("2008-11-23", "Labor Thanksgiving Day"),
            ("2008-11-24", "Substitute Holiday"),
            ("2008-12-23", "Emperor's Birthday"),
            ("2008-12-30", "Last Trading Day of the Year"),
            ("2008-12-31", "Bank Holiday"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2008-01-01", "วันขึ้นปีใหม่; วันหยุดธนาคาร"),
            ("2008-01-02", "วันหยุดธนาคาร"),
            ("2008-01-03", "วันหยุดธนาคาร"),
            ("2008-01-04", "วันทำการซื้อขายวันแรกของปี"),
            ("2008-01-14", "วันฉลองบรรลุนิติภาวะ"),
            ("2008-02-11", "วันชาติญี่ปุ่น"),
            ("2008-03-20", "วันวสันตวิษุวัต"),
            ("2008-04-29", "วันโชวะ"),
            ("2008-05-03", "วันรัฐธรรมนูญ"),
            ("2008-05-04", "วันพฤกษชาติ"),
            ("2008-05-05", "วันเด็กแห่งชาติ"),
            ("2008-05-06", "วันหยุดชดเชย"),
            ("2008-07-21", "วันแห่งทะเล"),
            ("2008-09-15", "วันเคารพผู้สูงอายุ"),
            ("2008-09-23", "วันศารทวิษุวัต"),
            ("2008-10-13", "วันพลศึกษา"),
            ("2008-11-03", "วันวัฒนธรรม"),
            ("2008-11-23", "วันขอบคุณแรงงาน"),
            ("2008-11-24", "วันหยุดชดเชย"),
            ("2008-12-23", "วันคล้ายวันพระราชสมภพ สมเด็จพระจักรพรรดินารุฮิโตะ"),
            ("2008-12-30", "วันทำการซื้อขายวันสุดท้ายของปี"),
            ("2008-12-31", "วันหยุดธนาคาร"),
        )
