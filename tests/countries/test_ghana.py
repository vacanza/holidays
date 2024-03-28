#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
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

    def test_2023(self):
        self.assertHolidays(
            Ghana(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-07", "Constitution Day"),
            ("2023-01-09", "Constitution Day (observed)"),
            ("2023-03-06", "Independence Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-01", "May Day"),
            ("2023-04-21", "Eid ul-Fitr (estimated)"),
            ("2023-06-28", "Eid ul-Adha (estimated)"),
            ("2023-08-04", "Founders' Day"),
            ("2023-09-21", "Kwame Nkrumah Memorial Day"),
            ("2023-12-01", "Farmer's Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_2024(self):
        self.assertHolidays(
            Ghana(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-01-07", "Constitution Day"),
            ("2024-01-08", "Constitution Day (observed)"),
            ("2024-03-06", "Independence Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-01", "May Day"),
            ("2024-04-10", "Eid ul-Fitr (estimated)"),
            ("2024-06-16", "Eid ul-Adha (estimated)"),
            ("2024-06-17", "Eid ul-Adha (observed, estimated)"),
            ("2024-08-04", "Founders' Day"),
            ("2024-08-05", "Founders' Day (observed)"),
            ("2024-09-21", "Kwame Nkrumah Memorial Day"),
            ("2024-09-23", "Kwame Nkrumah Memorial Day (observed)"),
            ("2024-12-06", "Farmer's Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )
