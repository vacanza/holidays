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
        self.assertHolidayName("আন্তর্জাতিক মাতৃভাষা দিবস", (f"{year}-02-21" for year in self.full_range))

    def test_sheikh_mujibur_rahmans_birthday_and_childrens_day(self):
        self.assertHolidayName(
            "শেখ মুজিবুর রহমানের জন্মদিন এবং শিশু দিবস",
            (f"{year}-03-17" for year in self.full_range),
        )

    def test_independence_day(self):
        self.assertHolidayName("স্বাধীনতা দিবস", (f"{year}-03-26" for year in self.full_range))

    def test_bengali_new_years_day(self):
        self.assertHolidayName("পহেলা বৈশাখ", (f"{year}-04-14" for year in self.full_range))

    def test_may_day(self):
        self.assertHolidayName("মে দিবস", (f"{year}-05-01" for year in self.full_range))

    def test_national_mourning_day(self):
        self.assertHolidayName("জাতীয় শোক দিবস", (f"{year}-08-15" for year in self.full_range))

    def test_victory_day(self):
        self.assertHolidayName("বিজয় দিবস", (f"{year}-12-16" for year in self.full_range))

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-02-21", "আন্তর্জাতিক মাতৃভাষা দিবস"),
            ("2022-03-17", "শেখ মুজিবুর রহমানের জন্মদিন এবং শিশু দিবস"),
            ("2022-03-26", "স্বাধীনতা দিবস"),
            ("2022-04-14", "পহেলা বৈশাখ"),
            ("2022-05-01", "মে দিবস"),
            ("2022-08-15", "জাতীয় শোক দিবস"),
            ("2022-12-16", "বিজয় দিবস"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2021-02-21", "আন্তর্জাতিক মাতৃভাষা দিবস"),
            ("2021-03-17", "শেখ মুজিবুর রহমানের জন্মদিন এবং শিশু দিবস"),
            ("2021-03-26", "স্বাধীনতা দিবস"),
            ("2021-04-14", "পহেলা বৈশাখ"),
            ("2021-05-01", "মে দিবস"),
            ("2021-08-15", "জাতীয় শোক দিবস"),
            ("2021-12-16", "বিজয় দিবস"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2021-02-21", "International Mother's language Day"),
            ("2021-03-17", "Sheikh Mujibur Rahman's Birthday and Children's Day"),
            ("2021-03-26", "Independence Day"),
            ("2021-04-14", "Bengali New Year's Day"),
            ("2021-05-01", "May Day"),
            ("2021-08-15", "National Mourning Day"),
            ("2021-12-16", "Victory Day"),
        )
