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

from holidays.countries.mongolia import Mongolia, MN, MNG
from tests.common import CommonCountryTests


class TestMongolia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2004, 2050)
        super().setUpClass(Mongolia, years=years)

    def test_country_aliases(self):
        self.assertAliases(Mongolia, MN, MNG)

    def test_no_holidays(self):
        self.assertNoHolidays(Mongolia(years=2003))

    def test_new_years_day(self):
        self.assertHolidayName("Шинэ жилийн баяр", (f"{year}-01-01" for year in range(2004, 2050)))

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

    def test_womens_day(self):
        self.assertHolidayName(
            "Олон улсын эмэгтэйчүүдийн өдөр", (f"{year}-03-08" for year in range(2004, 2050))
        )

    def test_childrens_day(self):
        self.assertHolidayName("Хүүхдийн баяр", (f"{year}-06-01" for year in range(2004, 2050)))

    def test_buddha_day(self):
        name = "Буддагийн өдөр"
        dt = (
            "2021-05-26",
            "2022-06-14",
            "2023-06-04",
            "2024-05-23",
            "2025-06-11",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(2004, 2050))

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

    def test_genghis_khan_day(self):
        name = "Их эзэн Чингис хааны мэндэлсэн өдөр"
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
        self.assertHolidayName(name, (f"{year}-11-26" for year in range(2012, 2050)))
        self.assertNoHolidayName(name, (f"{year}-11-26" for year in range(2004, 2012)))

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
            ("2025-06-11", "Буддагийн өдөр"),
            ("2025-07-11", "Наадам"),
            ("2025-07-12", "Наадмын баяр"),
            ("2025-07-13", "Наадмын баяр"),
            ("2025-07-14", "Наадмын баяр"),
            ("2025-07-15", "Наадмын баяр"),
            ("2025-11-21", "Их эзэн Чингис хааны мэндэлсэн өдөр"),
            ("2025-11-26", "Бүгд Найрамдах Улс тунхагласан өдөр"),
            ("2025-12-29", "Үндэсний эрх чөлөө, тусгаар тогтнолоо сэргээсний баярын өдөр"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Шинэ жилийн баяр"),
            ("2024-02-10", "Цагаан сар"),
            ("2024-02-11", "Цагаан сарын баяр"),
            ("2024-02-12", "Цагаан сарын баяр"),
            ("2024-03-08", "Олон улсын эмэгтэйчүүдийн өдөр"),
            ("2024-05-23", "Буддагийн өдөр"),
            ("2024-06-01", "Хүүхдийн баяр"),
            ("2024-07-11", "Наадам"),
            ("2024-07-12", "Наадмын баяр"),
            ("2024-07-13", "Наадмын баяр"),
            ("2024-07-14", "Наадмын баяр"),
            ("2024-07-15", "Наадмын баяр"),
            ("2024-11-02", "Их эзэн Чингис хааны мэндэлсэн өдөр"),
            ("2024-11-26", "Бүгд Найрамдах Улс тунхагласан өдөр"),
            ("2024-12-29", "Үндэсний эрх чөлөө, тусгаар тогтнолоо сэргээсний баярын өдөр"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-02-10", "Tsagaan Sar"),
            ("2024-02-11", "Tsagaan Sar Holiday"),
            ("2024-02-12", "Tsagaan Sar Holiday"),
            ("2024-03-08", "International Women's Day"),
            ("2024-05-23", "The Buddha's Birthday"),
            ("2024-06-01", "Children's Day"),
            ("2024-07-11", "Naadam"),
            ("2024-07-12", "Naadam Holiday"),
            ("2024-07-13", "Naadam Holiday"),
            ("2024-07-14", "Naadam Holiday"),
            ("2024-07-15", "Naadam Holiday"),
            ("2024-11-02", "The Birthday of the great emperor Genghis Khan"),
            ("2024-11-26", "Republic Day"),
            ("2024-12-29", "Restoration of Freedom and Independence Day"),
        )
