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

from holidays.countries.northern_mariana_islands import NorthernMarianaIslands
from tests.common import CommonCountryTests


class TestMP(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(NorthernMarianaIslands)

    def test_mp_only(self):
        """Check for a holiday that is not returned by US unless the
        subdivision is specified."""
        self.assertHolidayName("Commonwealth Covenant Day", "2016-03-24")
        self.assertHolidayName("Good Friday", "2016-03-25")
        self.assertHolidayName("Commonwealth Cultural Day", "2016-10-10")
        self.assertHolidayName("Citizenship Day", "2016-11-04")
        self.assertHolidayName("Election Day", "2016-11-08")
        self.assertHolidayName("Constitution Day", "2016-12-08")

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-17", "Birthday of Martin Luther King, Jr.; Martin Luther King Jr. Day"),
            ("2022-02-14", "Valentine's Day"),
            ("2022-02-21", "Washington's Birthday"),
            ("2022-03-17", "Saint Patrick's Day"),
            ("2022-03-24", "Commonwealth Covenant Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-08", "Mother's Day"),
            ("2022-05-30", "Memorial Day"),
            ("2022-06-19", "Father's Day; Juneteenth National Independence Day"),
            ("2022-06-20", "Juneteenth National Independence Day (observed)"),
            ("2022-07-04", "Independence Day"),
            ("2022-09-05", "Labor Day"),
            ("2022-10-10", "Columbus Day; Commonwealth Cultural Day"),
            ("2022-10-31", "Halloween"),
            ("2022-11-04", "Citizenship Day"),
            ("2022-11-08", "Election Day"),
            ("2022-11-11", "Veterans Day"),
            ("2022-11-24", "Thanksgiving Day"),
            ("2022-12-08", "Constitution Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-17", "วันมาร์ติน ลูเทอร์ คิง จูเนียร์; วันเกิดมาร์ติน ลูเทอร์ คิง จูเนียร์"),
            ("2022-02-14", "วันวาเลนไทน์"),
            ("2022-02-21", "วันเกิดวอชิงตัน"),
            ("2022-03-17", "วันนักบุญแพทริก"),
            ("2022-03-24", "วันปฏิญญาเครือรัฐ"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-05-08", "วันแม่"),
            ("2022-05-30", "วันรำลึก"),
            ("2022-06-19", "วันประกาศอิสรภาพแห่งชาติจูนทีนท์; วันพ่อ"),
            ("2022-06-20", "ชดเชยวันประกาศอิสรภาพแห่งชาติจูนทีนท์"),
            ("2022-07-04", "วันประกาศอิสรภาพ"),
            ("2022-09-05", "วันแรงงาน"),
            ("2022-10-10", "วันวัฒนธรรมแห่งเครือรัฐ; วันโคลัมบัส"),
            ("2022-10-31", "วันฮาโลวีน"),
            ("2022-11-04", "วันแห่งความเป็นพลเมือง"),
            ("2022-11-08", "วันเลือกตั้ง"),
            ("2022-11-11", "วันทหารผ่านศึก"),
            ("2022-11-24", "วันขอบคุณพระเจ้า"),
            ("2022-12-08", "วันรัฐธรรมนูญ"),
            ("2022-12-25", "วันคริสต์มาส"),
            ("2022-12-26", "ชดเชยวันคริสต์มาส"),
        )
