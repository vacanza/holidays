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

from holidays.constants import PUBLIC, WORKDAY
from holidays.countries.mongolia import Mongolia, MN, MNG
from tests.common import CommonCountryTests


class TestMongolia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2004, 2050)
        super().setUpClass(Mongolia, years=years)
        cls.workday_holidays = Mongolia(categories=WORKDAY, years=years)

    def test_country_aliases(self):
        self.assertAliases(Mongolia, MN, MNG)

    def test_no_holidays(self):
        self.assertNoHolidays(Mongolia(years=2003, categories=(PUBLIC, WORKDAY)))

    def test_new_years_day(self):
        self.assertHolidayName("Шинэ жилийн баяр", (f"{year}-01-01" for year in range(2004, 2050)))

    def test_constitutional_day(self):
        self.assertHolidayName(
            "Монгол Улсын Үндсэн хуулийн өдөр",
            self.workday_holidays,
            (f"{year}-01-13" for year in range(2004, 2050)),
        )

    def test_tsagaan_sar(self):
        name = "Цагаан сар"
        name_holiday = "Цагаан сарын баяр"
        # Day 1.
        self.assertHolidayName(
            name,
            "2021-02-12",
            "2022-02-02",
            "2023-02-21",
            "2024-02-10",
            "2025-03-01",
        )
        self.assertHolidayName(name, range(2004, 2050))
        # Day 2.
        self.assertHolidayName(
            name_holiday,
            "2021-02-13",
            "2022-02-03",
            "2023-02-22",
            "2024-02-11",
            "2025-03-02",
        )
        # Day 3.
        self.assertHolidayName(
            name_holiday,
            "2021-02-14",
            "2022-02-04",
            "2023-02-23",
            "2024-02-12",
            "2025-03-03",
        )
        self.assertHolidayName(name_holiday, range(2004, 2050))

    def test_patriots_day(self):
        self.assertHolidayName(
            "Эх орончдын өдөр",
            self.workday_holidays,
            (f"{year}-03-01" for year in range(2004, 2050)),
        )

    def test_womens_day(self):
        self.assertHolidayName(
            "Олон улсын эмэгтэйчүүдийн өдөр", (f"{year}-03-08" for year in range(2004, 2050))
        )

    def test_military_day(self):
        name = "Монгол цэргийн өдөр"
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-03-18" for year in range(2011, 2050))
        )
        self.assertNoHolidayName(name, self.workday_holidays, range(2004, 2011))

    def test_health_protection_day(self):
        self.assertHolidayName(
            "Эрүүл мэндийг хамгаалах өдөр",
            self.workday_holidays,
            (f"{year}-04-07" for year in range(2004, 2050)),
        )

    def test_intellectual_property_day(self):
        self.assertHolidayName(
            "Оюуны өмчийг хамгаалах өдөр",
            self.workday_holidays,
            (f"{year}-04-26" for year in range(2004, 2050)),
        )

    def test_family_day(self):
        self.assertHolidayName(
            "Гэр бүлийн өдөр",
            self.workday_holidays,
            (f"{year}-05-15" for year in range(2004, 2050)),
        )

    def test_childrens_day(self):
        self.assertHolidayName("Хүүхдийн баяр", (f"{year}-06-01" for year in range(2004, 2050)))

    def test_the_buddhas_birthday(self):
        name = "Бурхан багшийн Их дүйчин өдөр"
        dt = (
            "2021-05-26",
            "2022-06-14",
            "2023-06-04",
            "2024-05-23",
            "2025-06-11",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2020, 2050))
        self.assertNoHolidayName(name, range(2004, 2020))

    def test_national_flag_day(self):
        name = "Монгол Улсын төрийн далбааны өдөр"
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-07-10" for year in range(2009, 2050))
        )
        self.assertNoHolidayName(name, self.workday_holidays, range(2004, 2009))

    def test_naadam(self):
        for year in range(2004, 2050):
            self.assertHolidayName("Наадам", (f"{year}-07-11"))
            self.assertHolidayName(
                "Наадмын баяр",
                (f"{year}-07-12"),
                (f"{year}-07-13"),
                (f"{year}-07-14"),
                (f"{year}-07-15"),
            )

    def test_youth_day(self):
        self.assertHolidayName(
            "Залуучуудын өдөр",
            self.workday_holidays,
            (f"{year}-08-25" for year in range(2004, 2050)),
        )

    def test_memorial_day_of_political_defendants(self):
        self.assertHolidayName(
            "Улс төрийн хэлмэгдэгсдийн дурсгалын өдөр",
            self.workday_holidays,
            (f"{year}-09-10" for year in range(2004, 2050)),
        )

    def test_elders_day(self):
        self.assertHolidayName(
            "Ахмадын өдөр", self.workday_holidays, (f"{year}-10-01" for year in range(2004, 2050))
        )

    def test_capital_day(self):
        self.assertHolidayName(
            "Монгол Улсын Нийслэлийн өдөр",
            self.workday_holidays,
            (f"{year}-10-29" for year in range(2004, 2050)),
        )

    def test_genghis_khans_birthday(self):
        name = "Их Эзэн Чингис хааны өдөр"
        dt = (
            "2021-11-05",
            "2022-11-24",
            "2023-11-14",
            "2024-11-02",
            "2025-11-21",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2012, 2050))
        self.assertNoHolidayName(name, range(2004, 2012))

    def test_republic_day(self):
        name = "Бүгд Найрамдах Улс тунхагласан өдөр"
        self.assertHolidayName(name, (f"{year}-11-26" for year in range(2016, 2050)))
        self.assertNoHolidayName(name, range(2004, 2016))
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-11-26" for year in range(2012, 2016))
        )
        self.assertNoHolidayName(name, self.workday_holidays, range(2004, 2012), range(2016, 2050))

    def test_democracy_and_human_rights_day(self):
        self.assertHolidayName(
            "Ардчилал, хүний эрхийн өдөр",
            self.workday_holidays,
            (f"{year}-12-10" for year in range(2004, 2050)),
        )

    def test_independence_day(self):
        name_2007 = "Үндэсний эрх чөлөөний өдөр"
        name_2011 = "Үндэсний эрх чөлөө, тусгаар тогтнолоо сэргээсний баярын өдөр"
        self.assertHolidayName(name_2007, (f"{year}-12-29" for year in range(2007, 2011)))
        self.assertHolidayName(name_2011, (f"{year}-12-29" for year in range(2011, 2050)))
        self.assertNoHolidayName(name_2007, range(2004, 2007), range(2011, 2050))
        self.assertNoHolidayName(name_2011, range(2004, 2011))

    def test_2025(self):
        self.assertHolidays(
            Mongolia(years=2025),
            ("2025-01-01", "Шинэ жилийн баяр"),
            ("2025-03-01", "Цагаан сар"),
            ("2025-03-02", "Цагаан сарын баяр"),
            ("2025-03-03", "Цагаан сарын баяр"),
            ("2025-03-08", "Олон улсын эмэгтэйчүүдийн өдөр"),
            ("2025-06-01", "Хүүхдийн баяр"),
            ("2025-06-11", "Бурхан багшийн Их дүйчин өдөр"),
            ("2025-07-11", "Наадам"),
            ("2025-07-12", "Наадмын баяр"),
            ("2025-07-13", "Наадмын баяр"),
            ("2025-07-14", "Наадмын баяр"),
            ("2025-07-15", "Наадмын баяр"),
            ("2025-11-21", "Их Эзэн Чингис хааны өдөр"),
            ("2025-11-26", "Бүгд Найрамдах Улс тунхагласан өдөр"),
            ("2025-12-29", "Үндэсний эрх чөлөө, тусгаар тогтнолоо сэргээсний баярын өдөр"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Шинэ жилийн баяр"),
            ("2024-01-13", "Монгол Улсын Үндсэн хуулийн өдөр"),
            ("2024-02-10", "Цагаан сар"),
            ("2024-02-11", "Цагаан сарын баяр"),
            ("2024-02-12", "Цагаан сарын баяр"),
            ("2024-03-01", "Эх орончдын өдөр"),
            ("2024-03-08", "Олон улсын эмэгтэйчүүдийн өдөр"),
            ("2024-03-18", "Монгол цэргийн өдөр"),
            ("2024-04-07", "Эрүүл мэндийг хамгаалах өдөр"),
            ("2024-04-26", "Оюуны өмчийг хамгаалах өдөр"),
            ("2024-05-15", "Гэр бүлийн өдөр"),
            ("2024-05-23", "Бурхан багшийн Их дүйчин өдөр"),
            ("2024-06-01", "Хүүхдийн баяр"),
            ("2024-07-10", "Монгол Улсын төрийн далбааны өдөр"),
            ("2024-07-11", "Наадам"),
            ("2024-07-12", "Наадмын баяр"),
            ("2024-07-13", "Наадмын баяр"),
            ("2024-07-14", "Наадмын баяр"),
            ("2024-07-15", "Наадмын баяр"),
            ("2024-08-25", "Залуучуудын өдөр"),
            ("2024-09-10", "Улс төрийн хэлмэгдэгсдийн дурсгалын өдөр"),
            ("2024-10-01", "Ахмадын өдөр"),
            ("2024-10-29", "Монгол Улсын Нийслэлийн өдөр"),
            ("2024-11-02", "Их Эзэн Чингис хааны өдөр"),
            ("2024-11-26", "Бүгд Найрамдах Улс тунхагласан өдөр"),
            ("2024-12-10", "Ардчилал, хүний эрхийн өдөр"),
            ("2024-12-29", "Үндэсний эрх чөлөө, тусгаар тогтнолоо сэргээсний баярын өдөр"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-13", "Constitutional Day of Mongolia"),
            ("2024-02-10", "Tsagaan Sar"),
            ("2024-02-11", "Tsagaan Sar Holiday"),
            ("2024-02-12", "Tsagaan Sar Holiday"),
            ("2024-03-01", "Patriots' Day"),
            ("2024-03-08", "International Women's Day"),
            ("2024-03-18", "Mongolia Military Day"),
            ("2024-04-07", "Health Protection Day"),
            ("2024-04-26", "Intellectual Property Day"),
            ("2024-05-15", "Family Day"),
            ("2024-05-23", "The Buddha's Birthday"),
            ("2024-06-01", "Children's Day"),
            ("2024-07-10", "Mongolia National Flag Day"),
            ("2024-07-11", "Naadam"),
            ("2024-07-12", "Naadam Holiday"),
            ("2024-07-13", "Naadam Holiday"),
            ("2024-07-14", "Naadam Holiday"),
            ("2024-07-15", "Naadam Holiday"),
            ("2024-08-25", "Youth Day"),
            ("2024-09-10", "Memorial Day of Political Defendants"),
            ("2024-10-01", "Elders' Day"),
            ("2024-10-29", "Mongolia Capital Day"),
            ("2024-11-02", "Genghis Khan's Birthday"),
            ("2024-11-26", "Republic Day"),
            ("2024-12-10", "Democracy and Human Rights Day"),
            ("2024-12-29", "Restoration of Freedom and Independence Day"),
        )
