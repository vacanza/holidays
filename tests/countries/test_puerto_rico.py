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

from holidays.countries.puerto_rico import PuertoRico
from tests.common import CommonCountryTests


class TestPR(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PuertoRico)

    def test_pr_only(self):
        """Check for a holiday that is not returned by US unless the
        subdivision is specified."""
        self.assertHolidayName("Epiphany", "2016-01-06")
        self.assertHolidayName(
            "George Washington Day, Presidents' Day, and the Day of the Hero and "
            "the Illustrious Woman of Puerto Rico",
            "2016-02-15",
        )
        self.assertHolidayName("Emancipation Day", "2016-03-22")
        self.assertHolidayName("Good Friday", "2016-03-25")
        self.assertHolidayName("Puerto Rico Constitution Day", "2016-07-25")
        self.assertHolidayName(
            "Puerto Rican Culture and Discovery of Puerto Rico Day", "2016-11-19"
        )
        self.assertHalfDayHolidayName("Christmas Eve (from 12pm)", "2016-12-24")

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-01-17", "Martin Luther King Jr. Day"),
            ("2022-02-14", "Valentine's Day"),
            (
                "2022-02-21",
                "George Washington Day, Presidents' Day, and the Day of the Women and Men "
                "Heroes of Puerto Rico",
            ),
            ("2022-03-02", "American Citizenship Day"),
            ("2022-03-17", "Saint Patrick's Day"),
            ("2022-03-22", "Emancipation Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-08", "Mother's Day"),
            ("2022-05-30", "Memorial Day"),
            ("2022-06-19", "Father's Day; Juneteenth National Independence Day"),
            ("2022-06-20", "Juneteenth National Independence Day (observed)"),
            ("2022-07-04", "Independence Day"),
            ("2022-07-25", "Puerto Rico Constitution Day"),
            ("2022-09-05", "Labor Day"),
            ("2022-10-10", "Columbus Day"),
            ("2022-10-31", "Halloween"),
            ("2022-11-11", "Veterans Day"),
            ("2022-11-19", "Puerto Rican Culture and Discovery of Puerto Rico Day"),
            ("2022-11-24", "Thanksgiving Day"),
            ("2022-12-24", "Christmas Eve (from 12pm)"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-06", "วันสมโภชพระคริสต์แสดงองค์"),
            ("2022-01-17", "วันมาร์ติน ลูเทอร์ คิง จูเนียร์"),
            ("2022-02-14", "วันวาเลนไทน์"),
            ("2022-02-21", "วันจอร์จ วอชิงตัน, วันประธานาธิบดี และวันวีรบุรุษและวีรสตรีแห่งเปอร์โตริโก"),
            ("2022-03-02", "วันแห่งความเป็นพลเมืองอเมริกัน"),
            ("2022-03-17", "วันนักบุญแพทริก"),
            ("2022-03-22", "วันเลิกทาส"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-05-08", "วันแม่"),
            ("2022-05-30", "วันรำลึก"),
            ("2022-06-19", "วันประกาศอิสรภาพแห่งชาติจูนทีนท์; วันพ่อ"),
            ("2022-06-20", "ชดเชยวันประกาศอิสรภาพแห่งชาติจูนทีนท์"),
            ("2022-07-04", "วันประกาศอิสรภาพ"),
            ("2022-07-25", "วันรัฐธรรมนูญเปอร์โตริโก"),
            ("2022-09-05", "วันแรงงาน"),
            ("2022-10-10", "วันโคลัมบัส"),
            ("2022-10-31", "วันฮาโลวีน"),
            ("2022-11-11", "วันทหารผ่านศึก"),
            ("2022-11-19", "วันวัฒนธรรมเปอร์โตริโกและการค้นพบเปอร์โตริโก"),
            ("2022-11-24", "วันขอบคุณพระเจ้า"),
            ("2022-12-24", "วันคริสต์มาสอีฟ (ตั้งแต่ 12:00 น.)"),
            ("2022-12-25", "วันคริสต์มาส"),
            ("2022-12-26", "ชดเชยวันคริสต์มาส"),
        )
