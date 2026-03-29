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


class TestUnitedStatesVirginIslands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(UnitedStatesVirginIslands)

    def test_three_kings_day(self):
        self.assertHolidayName("Three Kings Day", (f"{year}-01-06" for year in self.full_range))

    def test_presidents_day(self):
        name = "Presidents' Day"
        self.assertHolidayName(
            name,
            "2020-02-17",
            "2021-02-15",
            "2022-02-21",
            "2023-02-20",
            "2024-02-19",
            "2025-02-17",
        )
        self.assertHolidayName(name, range(1971, self.end_year))
        self.assertHolidayName(name, (f"{year}-02-22" for year in range(self.start_year, 1971)))

    def test_transfer_day(self):
        self.assertHolidayName("Transfer Day", (f"{year}-03-31" for year in self.full_range))

    def test_holy_thursday(self):
        name = "Holy Thursday"
        self.assertHolidayName(
            name,
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
        )
        self.assertHolidayName(name, self.full_range)

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

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_emancipation_day(self):
        self.assertHolidayName("Emancipation Day", (f"{year}-07-03" for year in self.full_range))

    def test_columbus_day_and_puerto_rico_friendship_day(self):
        name = "Columbus Day and Puerto Rico Friendship Day"
        self.assertHolidayName(
            name,
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
            "2024-10-14",
            "2025-10-13",
        )
        self.assertHolidayName(name, range(1937, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1937))

    def test_liberty_day(self):
        self.assertHolidayName("Liberty Day", (f"{year}-11-01" for year in self.full_range))

    def test_christmas_second_day(self):
        self.assertHolidayName(
            "Christmas Second Day", (f"{year}-12-26" for year in self.full_range)
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Three Kings Day"),
            ("2022-01-17", "Martin Luther King Jr. Day"),
            ("2022-02-14", "Valentine's Day"),
            ("2022-02-21", "Presidents' Day"),
            ("2022-03-17", "Saint Patrick's Day"),
            ("2022-03-31", "Transfer Day"),
            ("2022-04-14", "Holy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-08", "Mother's Day"),
            ("2022-05-30", "Memorial Day"),
            ("2022-06-19", "Father's Day; Juneteenth National Independence Day"),
            ("2022-06-20", "Juneteenth National Independence Day (observed)"),
            ("2022-07-03", "Emancipation Day"),
            ("2022-07-04", "Independence Day"),
            ("2022-09-05", "Labor Day"),
            ("2022-10-10", "Columbus Day and Puerto Rico Friendship Day"),
            ("2022-10-31", "Halloween"),
            ("2022-11-01", "Liberty Day"),
            ("2022-11-11", "Veterans Day"),
            ("2022-11-24", "Thanksgiving Day"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed); Christmas Second Day"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-06", "วันสมโภชพระคริสต์แสดงองค์"),
            ("2022-01-17", "วันมาร์ติน ลูเทอร์ คิง จูเนียร์"),
            ("2022-02-14", "วันวาเลนไทน์"),
            ("2022-02-21", "วันประธานาธิบดี"),
            ("2022-03-17", "วันนักบุญแพทริก"),
            ("2022-03-31", "วันส่งมอบดินแดน"),
            ("2022-04-14", "วันพฤหัสศักดิ์สิทธิ์"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-17", "วันอาทิตย์อีสเตอร์"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-05-08", "วันแม่"),
            ("2022-05-30", "วันรำลึก"),
            ("2022-06-19", "วันประกาศอิสรภาพแห่งชาติจูนทีนท์; วันพ่อ"),
            ("2022-06-20", "ชดเชยวันประกาศอิสรภาพแห่งชาติจูนทีนท์"),
            ("2022-07-03", "วันเลิกทาส"),
            ("2022-07-04", "วันประกาศอิสรภาพ"),
            ("2022-09-05", "วันแรงงาน"),
            ("2022-10-10", "วันโคลัมบัส และวันมิตรภาพกับเปอร์โตริโก"),
            ("2022-10-31", "วันฮาโลวีน"),
            ("2022-11-01", "วันเลิกทาส"),
            ("2022-11-11", "วันทหารผ่านศึก"),
            ("2022-11-24", "วันขอบคุณพระเจ้า"),
            ("2022-12-24", "วันคริสต์มาสอีฟ"),
            ("2022-12-25", "วันคริสต์มาส"),
            ("2022-12-26", "ชดเชยวันคริสต์มาส; วันคริสต์มาสวันที่สอง"),
            ("2022-12-31", "วันสิ้นปี"),
        )
