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

    def test_korean_new_years_day(self):
        name = "설명절"
        self.assertHolidayName(
            name,
            "2020-01-25",
            "2021-02-12",
            "2022-02-01",
            "2023-01-22",
            "2024-02-10",
            "2025-01-29",
        )
        self.assertNoHolidayName(name, range(1968, 1989))

    def test_daeboreum_day(self):
        name = "대보름"
        self.assertHolidayName(
            name,
            "2020-02-08",
            "2021-02-26",
            "2022-02-15",
            "2023-02-05",
            "2024-02-24",
            "2025-02-12",
        )
        self.assertNoHolidayName(name, range(1948, 2003))

    def test_founding_day_of_peoples_army(self):
        name = "조선인민군창건일"
        self.assertHolidayName(
            name, (f"{year}-02-08" for year in (*range(1948, 1977), *range(2018, 2050)))
        )
        self.assertNoHolidayName(name, range(1978, 2018))

    def test_day_of_shining_star(self):
        name1 = "김정일의 생일"
        self.assertHolidayName(
            name1,
            (f"{year}-02-16" for year in range(1975, 2012)),
            (f"{year}-02-17" for year in range(1986, 2012)),
        )
        self.assertNoHolidayName(name1, range(1948, 1975), range(2012, 2050))
        name2 = "광명성절"
        self.assertHolidayName(
            name2,
            (f"{year}-02-16" for year in range(2012, 2050)),
            (f"{year}-02-17" for year in range(2012, 2050)),
        )
        self.assertNoHolidayName(name2, range(1948, 2012))

    def test_womens_day(self):
        self.assertHolidayName("국제부녀절", (f"{year}-03-08" for year in range(1948, 2050)))

    def test_cheongmyeong_festival(self):
        name = "청명"
        self.assertHolidayName(
            name,
            "2020-04-04",
            "2021-04-04",
            "2022-04-05",
            "2023-04-05",
            "2024-04-04",
            "2025-04-04",
        )
        self.assertNoHolidayName(name, range(1948, 2012))

    def test_hanshi_festival(self):
        name = "寒食节"
        self.assertHolidayName(
            name,
            "1963-04-06",
            "1964-04-05",
            "1965-04-06",
            "1966-04-06",
            "1967-04-06",
        )
        self.assertNoHolidayName(name, range(1968, 2050))

    def test_day_of_sun(self):
        name1 = "김일성의 생일"
        self.assertHolidayName(
            name1, "1962-04-15", (f"{year}-04-15" for year in range(1968, 1998))
        )
        self.assertNoHolidayName(name1, range(1948, 1962), range(1963, 1968), range(1998, 2050))
        name2 = "태양절"
        self.assertHolidayName(
            name2,
            (f"{year}-04-15" for year in range(1998, 2050)),
            (f"{year}-04-16" for year in range(1998, 2050)),
        )
        self.assertNoHolidayName(name2, range(1948, 1998))

    def test_army_day(self):
        name1 = "건군절"
        self.assertHolidayName(name1, (f"{year}-04-25" for year in range(1978, 2018)))
        self.assertNoHolidayName(name1, range(1948, 1978), range(2018, 2050))
        name2 = "조선인민혁명군 창건일"
        self.assertHolidayName(name2, (f"{year}-04-25" for year in range(2018, 2050)))
        self.assertNoHolidayName(name2, range(1948, 2018))

    def test_workers_day(self):
        self.assertHolidayName(
            "전세계근로자들의 국제적명절", (f"{year}-05-01" for year in range(1948, 2050))
        )

    def test_dano_festival(self):
        name = "단오"
        self.assertHolidayName(
            name,
            "1963-06-25",
            "1964-06-14",
            "1965-06-04",
            "1966-06-23",
            "1967-06-12",
        )
        self.assertNoHolidayName(name, range(1968, 2050))

    def test_childrens_union_day(self):
        self.assertHolidayName(
            "조선소년단 창립절", (f"{year}-06-06" for year in range(1948, 2050))
        )

    def test_victory_day(self):
        name = "조국해방전쟁승리기념일"
        self.assertHolidayName(name, (f"{year}-07-27" for year in range(1996, 2050)))
        self.assertNoHolidayName(name, range(1948, 1996))

    def test_liberation_day(self):
        self.assertHolidayName("조국해방절", (f"{year}-08-15" for year in range(1948, 2050)))

    def test_chuseok(self):
        name = "추석"
        self.assertHolidayName(
            name,
            "2020-10-01",
            "2021-09-21",
            "2022-09-10",
            "2023-09-29",
            "2024-09-17",
            "2025-10-06",
        )
        self.assertNoHolidayName(name, range(1967, 1989))

    def test_day_of_songun(self):
        name = "선군절"
        self.assertHolidayName(name, (f"{year}-08-25" for year in range(2013, 2050)))
        self.assertNoHolidayName(name, range(1948, 2013))

    def test_youth_day(self):
        self.assertHolidayName("청년절", (f"{year}-08-28" for year in range(1948, 2050)))

    def test_foundation_day(self):
        self.assertHolidayName(
            "조선민주주의인민공화국창건일", (f"{year}-09-09" for year in range(1948, 2050))
        )

    def test_party_foundation_day(self):
        self.assertHolidayName("조선로동당창건일", (f"{year}-10-10" for year in range(1948, 2050)))

    def test_mothers_day(self):
        name = "어머니날"
        self.assertHolidayName(name, (f"{year}-11-16" for year in range(2012, 2050)))
        self.assertNoHolidayName(name, range(1948, 2012))

    def test_constitution_day(self):
        name = "사회주의헌법절"
        self.assertHolidayName(name, (f"{year}-12-27" for year in range(1972, 2050)))
        self.assertNoHolidayName(name, range(1948, 1972))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "양력설"),
            ("2024-02-08", "조선인민군창건일"),
            ("2024-02-10", "설명절"),
            ("2024-02-16", "광명성절"),
            ("2024-02-17", "광명성절"),
            ("2024-02-24", "대보름"),
            ("2024-03-08", "국제부녀절"),
            ("2024-04-04", "청명"),
            ("2024-04-15", "태양절"),
            ("2024-04-16", "태양절"),
            ("2024-04-25", "조선인민혁명군 창건일"),
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
            ("2024-02-08", "Founding Day of the Korean People's Army"),
            ("2024-02-10", "Korean New Year"),
            ("2024-02-16", "Day of the Shining Star"),
            ("2024-02-17", "Day of the Shining Star"),
            ("2024-02-24", "Daeboreum"),
            ("2024-03-08", "International Women's Day"),
            ("2024-04-04", "Cheongmyeong Festival"),
            ("2024-04-15", "Day of the Sun"),
            ("2024-04-16", "Day of the Sun"),
            ("2024-04-25", "Founding Day of the Korean People's Revolutionary Army"),
            ("2024-05-01", "International Workers' Day"),
            ("2024-06-06", "Foundation Day of the Korean Children's Union"),
            ("2024-07-27", "Day of Victory in the Great Fatherland Liberation War"),
            ("2024-08-15", "Liberation Day"),
            ("2024-08-25", "Day of Songun"),
            ("2024-08-28", "Youth Day"),
            ("2024-09-09", "Founding Day of the DPRK"),
            ("2024-09-17", "Chuseok"),
            ("2024-10-10", "Foundation Day of the Workers' Party of Korea"),
            ("2024-11-16", "Mother's Day"),
            ("2024-12-27", "Socialist Constitution Day"),
        )
