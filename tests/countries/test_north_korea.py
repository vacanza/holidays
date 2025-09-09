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

from holidays.countries.north_korea import NorthKorea, KP, PRK
from tests.common import CommonCountryTests


class TestNorthKorea(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1948, 2050)
        super().setUpClass(NorthKorea, years=years)

    def test_country_aliases(self):
        self.assertAliases(NorthKorea, KP, PRK)

    def test_no_holidays(self):
        self.assertNoHolidays(NorthKorea(years=1947))

    def test_new_years_day(self):
        self.assertHolidayName("양력설", (f"{year}-01-01" for year in range(1948, 2050)))

    def test_lunar_new_years_day(self):
        self.assertHolidayName(
            "설명절",
            "2020-01-25",
            "2021-02-12",
            "2022-02-01",
            "2023-01-22",
            "2024-02-10",
            "2025-01-29",
        )

    def test_daeboreum_day(self):
        self.assertHolidayName(
            "대보름",
            "2020-02-08",
            "2021-02-26",
            "2022-02-15",
            "2023-02-05",
            "2024-02-24",
            "2025-02-12",
        )

    def test_army_day(self):
        name = "조선인민군"
        self.assertHolidayName(
            name,
            (f"{year}-02-08" for year in range(1948, 1979)),
            (f"{year}-04-25" for year in range(2015, 2050)),
        )
        self.assertNoHolidayName(name, range(1979, 2015))

    def test_day_of_shining_star(self):
        self.assertHolidayName("광명성절", (f"{year}-02-16" for year in range(1948, 2050)))

    def test_womens_day(self):
        self.assertHolidayName("국제부녀절", (f"{year}-03-08" for year in range(1948, 2050)))

    def test_day_of_sun(self):
        self.assertHolidayName("태양절", (f"{year}-04-15" for year in range(1948, 2050)))

    def test_labor_day(self):
        self.assertHolidayName(
            "전세계근로자들의 국제적명절", (f"{year}-05-01" for year in range(1948, 2050))
        )

    def test_childrens_union_day(self):
        self.assertHolidayName(
            "조선소년단 창립절", (f"{year}-06-06" for year in range(1948, 2050))
        )

    def test_victory_day(self):
        name = "조국해방전쟁승리기념일"
        self.assertHolidayName(name, (f"{year}-07-27" for year in range(1953, 2050)))
        self.assertNoHolidayName(name, range(1948, 1953))

    def test_liberation_day(self):
        self.assertHolidayName("조국해방절", (f"{year}-08-15" for year in range(1948, 2050)))

    def test_chuseok(self):
        self.assertHolidayName(
            "추석",
            "2020-10-01",
            "2021-09-21",
            "2022-09-10",
            "2023-09-29",
            "2024-09-17",
            "2025-10-06",
        )

    def test_day_of_songun(self):
        self.assertHolidayName("선군절", (f"{year}-08-25" for year in range(1948, 2050)))

    def test_youth_day(self):
        self.assertHolidayName("청년절", (f"{year}-08-28" for year in range(1948, 2050)))

    def test_foundation_day(self):
        self.assertHolidayName(
            "조선민주주의인민공화국창건일", (f"{year}-09-09" for year in range(1948, 2050))
        )

    def test_party_foundation_day(self):
        self.assertHolidayName("조선로동당창건일", (f"{year}-10-10" for year in range(1948, 2050)))

    def test_mothers_day(self):
        self.assertHolidayName("어머니날", (f"{year}-11-16" for year in range(1948, 2050)))

    def test_constitution_day(self):
        self.assertHolidayName("사회주의헌법절", (f"{year}-12-27" for year in range(1948, 2050)))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "양력설"),
            ("2024-02-10", "설명절"),
            ("2024-02-16", "광명성절"),
            ("2024-02-24", "대보름"),
            ("2024-03-08", "국제부녀절"),
            ("2024-04-15", "태양절"),
            ("2024-04-25", "조선인민군"),
            ("2024-05-01", "전세계근로자들의 국제적명절"),
            ("2024-06-06", "조선소년단 창립절"),
            ("2024-07-27", "조국해방전쟁승리기념일"),
            ("2024-08-15", "조국해방절"),
            ("2024-08-25", "선군절"),
            ("2024-08-28", "청년절"),
            ("2024-09-09", "조선민주주의인민공화국창건일"),
            ("2024-09-17", "추석"),
            ("2024-10-10", "조선로동당창건일"),
            ("2024-11-16", "어머니날"),
            ("2024-12-27", "사회주의헌법절"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-02-10", "Lunar New Year"),
            ("2024-02-16", "Day of the Shining Star"),
            ("2024-02-24", "Daeboreum"),
            ("2024-03-08", "International Women's Day"),
            ("2024-04-15", "Day of the Sun"),
            ("2024-04-25", "Army Day"),
            ("2024-05-01", "Labor Day"),
            ("2024-06-06", "Korean Children's Union Day"),
            ("2024-07-27", "Fatherland Liberation War Victory Day"),
            ("2024-08-15", "Liberation Day"),
            ("2024-08-25", "Day of Songun"),
            ("2024-08-28", "Youth Day"),
            ("2024-09-09", "DPRK Foundation Day"),
            ("2024-09-17", "Chuseok"),
            ("2024-10-10", "Party Foundation Day"),
            ("2024-11-16", "Mother's Day"),
            ("2024-12-27", "Socialist Constitution Day"),
        )
