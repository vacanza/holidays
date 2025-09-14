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

from holidays.countries.american_samoa import HolidaysAS, AmericanSamoa, AS, ASM
from tests.common import CommonCountryTests


class TestAS(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HolidaysAS)

    def test_country_aliases(self):
        self.assertAliases(HolidaysAS, AmericanSamoa, AS, ASM)

    def test_no_holidays(self):
        self.assertNoHolidays(
            HolidaysAS(categories=HolidaysAS.supported_categories, years=self.start_year - 1)
        )

    def test_as_only(self):
        """Check for a holiday that is not returned by US unless the subdivision is specified."""
        self.assertHolidayName("American Samoa Flag Day", "2016-04-17")
        self.assertHolidayName("American Samoa Flag Day (observed)", "2016-04-18")
        self.assertHolidayName("Manu'a Islands Cession Day (observed)", "2016-07-15")
        self.assertHolidayName("Manu'a Islands Cession Day", "2016-07-16")
        self.assertHolidayName("White Sunday", "2016-10-09")

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-17", "Birthday of Martin Luther King, Jr.; Martin Luther King Jr. Day"),
            ("2022-02-14", "Valentine's Day"),
            ("2022-02-21", "Washington's Birthday"),
            ("2022-03-17", "Saint Patrick's Day"),
            ("2022-04-17", "American Samoa Flag Day"),
            ("2022-04-18", "American Samoa Flag Day (observed)"),
            ("2022-05-30", "Memorial Day"),
            ("2022-06-19", "Juneteenth National Independence Day"),
            ("2022-06-20", "Juneteenth National Independence Day (observed)"),
            ("2022-07-04", "Independence Day"),
            ("2022-07-15", "Manu'a Islands Cession Day (observed)"),
            ("2022-07-16", "Manu'a Islands Cession Day"),
            ("2022-09-05", "Labor Day"),
            ("2022-10-09", "White Sunday"),
            ("2022-10-10", "Columbus Day"),
            ("2022-10-31", "Halloween"),
            ("2022-11-11", "Veterans Day"),
            ("2022-11-24", "Thanksgiving Day"),
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
            ("2022-04-17", "วันธงชาติอเมริกันซามัว"),
            ("2022-04-18", "ชดเชยวันธงชาติอเมริกันซามัว"),
            ("2022-05-30", "วันรำลึก"),
            ("2022-06-19", "วันประกาศอิสรภาพแห่งชาติจูนทีนท์"),
            ("2022-06-20", "ชดเชยวันประกาศอิสรภาพแห่งชาติจูนทีนท์"),
            ("2022-07-04", "วันประกาศอิสรภาพ"),
            ("2022-07-15", "ชดเชยวันส่งมอบหมู่เกาะมานูอา"),
            ("2022-07-16", "วันส่งมอบหมู่เกาะมานูอา"),
            ("2022-09-05", "วันแรงงาน"),
            ("2022-10-09", "วันอาทิตย์ขาว"),
            ("2022-10-10", "วันโคลัมบัส"),
            ("2022-10-31", "วันฮาโลวีน"),
            ("2022-11-11", "วันทหารผ่านศึก"),
            ("2022-11-24", "วันขอบคุณพระเจ้า"),
            ("2022-12-25", "วันคริสต์มาส"),
            ("2022-12-26", "ชดเชยวันคริสต์มาส"),
        )
