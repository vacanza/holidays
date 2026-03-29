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


class TestNorthernMarianaIslands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(NorthernMarianaIslands)

    def test_commonwealth_covenant_day(self):
        name = "Commonwealth Covenant Day"
        self.assertHolidayName(name, (f"{year}-03-24" for year in self.full_range))
        obs_dt = (
            "2012-03-23",
            "2013-03-25",
            "2018-03-23",
            "2019-03-25",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_commonwealth_cultural_day(self):
        name = "Commonwealth Cultural Day"
        self.assertHolidayName(
            name,
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
            "2024-10-14",
            "2025-10-13",
        )
        self.assertHolidayName(name, self.full_range)

    def test_election_day(self):
        name = "Election Day"
        self.assertHolidayName(
            name,
            "2008-11-04",
            "2010-11-02",
            "2012-11-06",
            "2014-11-04",
            "2016-11-08",
            "2018-11-06",
            "2020-11-03",
            "2022-11-08",
            "2024-11-05",
        )
        self.assertNoHolidayName(name, range(self.start_year, 2008), range(2009, self.end_year, 2))

    def test_citizenship_day(self):
        name = "Citizenship Day"
        self.assertHolidayName(name, (f"{year}-11-04" for year in self.full_range))
        obs_dts = (
            "2012-11-05",
            "2017-11-03",
            "2018-11-05",
            "2023-11-03",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHolidayName(f"{name} (observed)", obs_dts)

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertHolidayName(name, (f"{year}-12-08" for year in self.full_range))
        obs_dts = (
            "2012-12-07",
            "2013-12-09",
            "2018-12-07",
            "2019-12-09",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHolidayName(f"{name} (observed)", obs_dts)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-17", "Martin Luther King Jr. Day"),
            ("2022-02-14", "Valentine's Day"),
            ("2022-02-21", "Washington's Birthday"),
            ("2022-03-17", "Saint Patrick's Day"),
            ("2022-03-24", "Commonwealth Covenant Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-05-08", "Mother's Day"),
            ("2022-05-30", "Memorial Day"),
            ("2022-06-19", "Father's Day; Juneteenth National Independence Day"),
            ("2022-06-20", "Juneteenth National Independence Day (observed)"),
            ("2022-07-04", "Independence Day"),
            ("2022-09-05", "Labor Day"),
            ("2022-10-10", "Commonwealth Cultural Day"),
            ("2022-10-31", "Halloween"),
            ("2022-11-04", "Citizenship Day"),
            ("2022-11-08", "Election Day"),
            ("2022-11-11", "Veterans Day"),
            ("2022-11-24", "Thanksgiving Day"),
            ("2022-12-08", "Constitution Day"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-17", "วันมาร์ติน ลูเทอร์ คิง จูเนียร์"),
            ("2022-02-14", "วันวาเลนไทน์"),
            ("2022-02-21", "วันเกิดวอชิงตัน"),
            ("2022-03-17", "วันนักบุญแพทริก"),
            ("2022-03-24", "วันปฏิญญาเครือรัฐ"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-17", "วันอาทิตย์อีสเตอร์"),
            ("2022-05-08", "วันแม่"),
            ("2022-05-30", "วันรำลึก"),
            ("2022-06-19", "วันประกาศอิสรภาพแห่งชาติจูนทีนท์; วันพ่อ"),
            ("2022-06-20", "ชดเชยวันประกาศอิสรภาพแห่งชาติจูนทีนท์"),
            ("2022-07-04", "วันประกาศอิสรภาพ"),
            ("2022-09-05", "วันแรงงาน"),
            ("2022-10-10", "วันวัฒนธรรมแห่งเครือรัฐ"),
            ("2022-10-31", "วันฮาโลวีน"),
            ("2022-11-04", "วันแห่งความเป็นพลเมือง"),
            ("2022-11-08", "วันเลือกตั้ง"),
            ("2022-11-11", "วันทหารผ่านศึก"),
            ("2022-11-24", "วันขอบคุณพระเจ้า"),
            ("2022-12-08", "วันรัฐธรรมนูญ"),
            ("2022-12-24", "วันคริสต์มาสอีฟ"),
            ("2022-12-25", "วันคริสต์มาส"),
            ("2022-12-26", "ชดเชยวันคริสต์มาส"),
            ("2022-12-31", "วันสิ้นปี"),
        )
