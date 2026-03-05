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

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("1949-01-01", "元日; 銀行休業日"),
            ("1949-01-02", "銀行休業日"),
            ("1949-01-03", "銀行休業日"),
            ("1949-01-15", "成人の日"),
            ("1949-03-21", "春分の日"),
            ("1949-04-29", "天皇誕生日"),
            ("1949-05-03", "憲法記念日"),
            ("1949-05-05", "こどもの日"),
            ("1949-09-23", "秋分の日"),
            ("1949-11-03", "文化の日"),
            ("1949-11-23", "勤労感謝の日"),
            ("1949-12-31", "銀行休業日"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("1949-01-01", "Bank Holiday; New Year's Day"),
            ("1949-01-02", "Bank Holiday"),
            ("1949-01-03", "Bank Holiday"),
            ("1949-01-15", "Coming of Age Day"),
            ("1949-03-21", "Vernal Equinox Day"),
            ("1949-04-29", "Emperor's Birthday"),
            ("1949-05-03", "Constitution Day"),
            ("1949-05-05", "Children's Day"),
            ("1949-09-23", "Autumnal Equinox Day"),
            ("1949-11-03", "Culture Day"),
            ("1949-11-23", "Labor Thanksgiving Day"),
            ("1949-12-31", "Bank Holiday"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("1949-01-01", "วันขึ้นปีใหม่; วันหยุดธนาคาร"),
            ("1949-01-02", "วันหยุดธนาคาร"),
            ("1949-01-03", "วันหยุดธนาคาร"),
            ("1949-01-15", "วันฉลองบรรลุนิติภาวะ"),
            ("1949-03-21", "วันวสันตวิษุวัต"),
            ("1949-04-29", "วันคล้ายวันพระราชสมภพ สมเด็จพระจักรพรรดินารุฮิโตะ"),
            ("1949-05-03", "วันรัฐธรรมนูญ"),
            ("1949-05-05", "วันเด็กแห่งชาติ"),
            ("1949-09-23", "วันศารทวิษุวัต"),
            ("1949-11-03", "วันวัฒนธรรม"),
            ("1949-11-23", "วันขอบคุณแรงงาน"),
            ("1949-12-31", "วันหยุดธนาคาร"),
        )

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))
