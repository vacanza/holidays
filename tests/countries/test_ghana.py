#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.ghana import Ghana, GH, GHA
from tests.common import CommonCountryTests


class TestGhana(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Ghana, years=range(1957, 2050))

    def test_country_aliases(self):
        self.assertAliases(Ghana, GH, GHA)

    def test_no_holidays(self):
        self.assertNoHolidays(Ghana(years=1956))

    def test_new_year_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1957, 2050))

    def test_constitution_day(self):
        self.assertHoliday(f"{year}-01-07" for year in range(2019, 2050))
        self.assertNoHoliday(f"{year}-01-07" for year in range(1957, 2019))
        self.assertNoHolidayName("Constitution Day", range(1957, 2019))

    def test_founders_day(self):
        self.assertHoliday(f"{year}-08-04" for year in range(2019, 2050))

    def test_independence_day(self):
        self.assertHoliday(f"{year}-03-06" for year in range(1957, 2050))

    def test_farmers_day(self):  # 1st Friday of December
        self.assertHolidayName(
            "Farmer's Day",
            "2023-12-01",
            "2024-12-06",
            "2025-12-05",
            "2026-12-04",
            "2027-12-03",
            "2028-12-01",
            "2029-12-07",
            "2030-12-06",
        )

    def test_eid_ul_fitr(self):
        self.assertHolidayName(
            "Eid ul-Fitr (estimated)",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
        )
