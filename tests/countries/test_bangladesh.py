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

from holidays.countries.bangladesh import Bangladesh
from tests.common import CommonCountryTests


class TestBangladesh(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Bangladesh)

    def test_international_mothers_language_day(self):
        self.assertHolidayName(
            "International Mother's language Day", (f"{year}-02-21" for year in self.full_range)
        )

    def test_sheikh_mujibur_rahmans_birthday_and_childrens_day(self):
        self.assertHolidayName(
            "Sheikh Mujibur Rahman's Birthday and Children's Day",
            (f"{year}-03-17" for year in self.full_range),
        )

    def test_independence_day(self):
        self.assertHolidayName("Independence Day", (f"{year}-03-26" for year in self.full_range))

    def test_bengali_new_years_day(self):
        self.assertHolidayName(
            "Bengali New Year's Day", (f"{year}-04-14" for year in self.full_range)
        )

    def test_may_day(self):
        self.assertHolidayName("May Day", (f"{year}-05-01" for year in self.full_range))

    def test_national_mourning_day(self):
        self.assertHolidayName(
            "National Mourning Day", (f"{year}-08-15" for year in self.full_range)
        )

    def test_victory_day(self):
        self.assertHolidayName("Victory Day", (f"{year}-12-16" for year in self.full_range))

    def test_2022(self):
        self.assertHolidays(
            Bangladesh(years=2022),
            ("2022-02-21", "International Mother's language Day"),
            ("2022-03-17", "Sheikh Mujibur Rahman's Birthday and Children's Day"),
            ("2022-03-26", "Independence Day"),
            ("2022-04-14", "Bengali New Year's Day"),
            ("2022-05-01", "May Day"),
            ("2022-08-15", "National Mourning Day"),
            ("2022-12-16", "Victory Day"),
        )
