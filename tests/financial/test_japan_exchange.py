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

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "元日; 銀行休業日"),
            ("2024-01-02", "銀行休業日"),
            ("2024-01-03", "銀行休業日"),
            ("2024-01-08", "成人の日"),
            ("2024-02-11", "建国記念の日"),
            ("2024-02-12", "振替休日"),
            ("2024-02-23", "天皇誕生日"),
            ("2024-03-20", "春分の日"),
            ("2024-04-29", "昭和の日"),
            ("2024-05-03", "憲法記念日"),
            ("2024-05-04", "みどりの日"),
            ("2024-05-05", "こどもの日"),
            ("2024-05-06", "振替休日"),
            ("2024-07-15", "海の日"),
            ("2024-08-11", "山の日"),
            ("2024-08-12", "振替休日"),
            ("2024-09-16", "敬老の日"),
            ("2024-09-22", "秋分の日"),
            ("2024-09-23", "振替休日"),
            ("2024-10-14", "スポーツの日"),
            ("2024-11-03", "文化の日"),
            ("2024-11-04", "振替休日"),
            ("2024-11-23", "勤労感謝の日"),
            ("2024-12-31", "銀行休業日"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "Bank Holiday; New Year's Day"),
            ("2024-01-02", "Bank Holiday"),
            ("2024-01-03", "Bank Holiday"),
            ("2024-01-08", "Coming of Age Day"),
            ("2024-02-11", "Foundation Day"),
            ("2024-02-12", "Substitute Holiday"),
            ("2024-02-23", "Emperor's Birthday"),
            ("2024-03-20", "Vernal Equinox Day"),
            ("2024-04-29", "Showa Day"),
            ("2024-05-03", "Constitution Day"),
            ("2024-05-04", "Greenery Day"),
            ("2024-05-05", "Children's Day"),
            ("2024-05-06", "Substitute Holiday"),
            ("2024-07-15", "Marine Day"),
            ("2024-08-11", "Mountain Day"),
            ("2024-08-12", "Substitute Holiday"),
            ("2024-09-16", "Respect for the Aged Day"),
            ("2024-09-22", "Autumnal Equinox Day"),
            ("2024-09-23", "Substitute Holiday"),
            ("2024-10-14", "Sports Day"),
            ("2024-11-03", "Culture Day"),
            ("2024-11-04", "Substitute Holiday"),
            ("2024-11-23", "Labor Thanksgiving Day"),
            ("2024-12-31", "Bank Holiday"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2024-01-01", "วันขึ้นปีใหม่; วันหยุดธนาคาร"),
            ("2024-01-02", "วันหยุดธนาคาร"),
            ("2024-01-03", "วันหยุดธนาคาร"),
            ("2024-01-08", "วันฉลองบรรลุนิติภาวะ"),
            ("2024-02-11", "วันชาติญี่ปุ่น"),
            ("2024-02-12", "วันหยุดชดเชย"),
            ("2024-02-23", "วันคล้ายวันพระราชสมภพ สมเด็จพระจักรพรรดินารุฮิโตะ"),
            ("2024-03-20", "วันวสันตวิษุวัต"),
            ("2024-04-29", "วันโชวะ"),
            ("2024-05-03", "วันรัฐธรรมนูญ"),
            ("2024-05-04", "วันพฤกษชาติ"),
            ("2024-05-05", "วันเด็กแห่งชาติ"),
            ("2024-05-06", "วันหยุดชดเชย"),
            ("2024-07-15", "วันแห่งทะเล"),
            ("2024-08-11", "วันแห่งภูเขา"),
            ("2024-08-12", "วันหยุดชดเชย"),
            ("2024-09-16", "วันเคารพผู้สูงอายุ"),
            ("2024-09-22", "วันศารทวิษุวัต"),
            ("2024-09-23", "วันหยุดชดเชย"),
            ("2024-10-14", "วันกีฬาแห่งชาติ"),
            ("2024-11-03", "วันวัฒนธรรม"),
            ("2024-11-04", "วันหยุดชดเชย"),
            ("2024-11-23", "วันขอบคุณแรงงาน"),
            ("2024-12-31", "วันหยุดธนาคาร"),
        )
