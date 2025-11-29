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

from holidays.countries.united_states_virgin_islands import UnitedStatesVirginIslands
from tests.common import CommonCountryTests


class TestVI(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(UnitedStatesVirginIslands)

    def test_vi_only(self):
        """Check for a holiday that is not returned by US unless the
        subdivision is specified."""
        self.assertHolidayName("Three Kings Day", "2016-01-06")
        self.assertHolidayName("Presidents' Day", "2016-02-15")
        self.assertHolidayName("Holy Thursday", "2016-03-24")
        self.assertHolidayName("Good Friday", "2016-03-25")
        self.assertHolidayName("Easter Monday", "2016-03-28")
        self.assertHolidayName("Transfer Day", "2016-03-31")
        self.assertHolidayName("Emancipation Day", "2016-07-03")
        self.assertHolidayName("Columbus Day and Puerto Rico Friendship Day", "2016-10-10")
        self.assertHolidayName("Liberty Day", "2016-11-01")
        self.assertHolidayName("Christmas Second Day", "2016-12-26")

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Three Kings Day"),
            ("2022-01-17", "Birthday of Martin Luther King, Jr.; Martin Luther King Jr. Day"),
            ("2022-02-14", "Valentine's Day"),
            ("2022-02-21", "Presidents' Day; Washington's Birthday"),
            ("2022-03-17", "Saint Patrick's Day"),
            ("2022-03-31", "Transfer Day"),
            ("2022-04-14", "Holy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-08", "Mother's Day"),
            ("2022-05-30", "Memorial Day"),
            ("2022-06-19", "Father's Day; Juneteenth National Independence Day"),
            ("2022-06-20", "Juneteenth National Independence Day (observed)"),
            ("2022-07-03", "Emancipation Day"),
            ("2022-07-04", "Independence Day"),
            ("2022-09-05", "Labor Day"),
            ("2022-10-10", "Columbus Day; Columbus Day and Puerto Rico Friendship Day"),
            ("2022-10-31", "Halloween"),
            ("2022-11-01", "Liberty Day"),
            ("2022-11-11", "Veterans Day"),
            ("2022-11-24", "Thanksgiving Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed); Christmas Second Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-06", "วันสมโภชพระคริสต์แสดงองค์"),
            ("2022-01-17", "วันมาร์ติน ลูเทอร์ คิง จูเนียร์; วันเกิดมาร์ติน ลูเทอร์ คิง จูเนียร์"),
            ("2022-02-14", "วันวาเลนไทน์"),
            ("2022-02-21", "วันประธานาธิบดี; วันเกิดวอชิงตัน"),
            ("2022-03-17", "วันนักบุญแพทริก"),
            ("2022-03-31", "วันส่งมอบดินแดน"),
            ("2022-04-14", "วันพฤหัสศักดิสิทธิ์"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-05-08", "วันแม่"),
            ("2022-05-30", "วันรำลึก"),
            ("2022-06-19", "วันประกาศอิสรภาพแห่งชาติจูนทีนท์; วันพ่อ"),
            ("2022-06-20", "ชดเชยวันประกาศอิสรภาพแห่งชาติจูนทีนท์"),
            ("2022-07-03", "วันเลิกทาส"),
            ("2022-07-04", "วันประกาศอิสรภาพ"),
            ("2022-09-05", "วันแรงงาน"),
            ("2022-10-10", "วันโคลัมบัส; วันโคลัมบัส และวันมิตรภาพกับเปอร์โตริโก"),
            ("2022-10-31", "วันฮาโลวีน"),
            ("2022-11-01", "วันเลิกทาส"),
            ("2022-11-11", "วันทหารผ่านศึก"),
            ("2022-11-24", "วันขอบคุณพระเจ้า"),
            ("2022-12-25", "วันคริสต์มาส"),
            ("2022-12-26", "ชดเชยวันคริสต์มาส; วันคริสต์มาสวันที่สอง"),
        )
