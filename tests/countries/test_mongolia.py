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

from holidays.constants import WORKDAY
from holidays.countries.mongolia import Mongolia
from tests.common import CommonCountryTests


class TestMongolia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2004, 2050)
        super().setUpClass(Mongolia, years=years)
        cls.workday_holidays = Mongolia(categories=WORKDAY, years=years)

    def test_new_years_day(self):
        self.assertHolidayName("Шинэ жил", (f"{year}-01-01" for year in range(2004, 2050)))

    def test_constitutional_day(self):
        name = "Монгол Улсын Үндсэн хуулийн өдөр"
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-01-13" for year in range(2004, 2050))
        )
        self.assertNoHolidayName(name)

    def test_tsagaan_sar(self):
        name = "Цагаан сар"
        # Day 1.
        self.assertHolidayName(
            name,
            "2012-02-22",
            "2013-02-11",
            "2014-01-31",
            "2021-02-12",
            "2022-02-02",
            "2023-02-21",
            "2024-02-10",
            "2025-03-01",
        )
        # Day 2.
        self.assertHolidayName(
            name,
            "2012-02-23",
            "2013-02-12",
            "2014-02-01",
            "2021-02-13",
            "2022-02-03",
            "2023-02-22",
            "2024-02-11",
            "2025-03-02",
        )
        # Day 3.
        self.assertHolidayName(
            name,
            "2014-02-02",
            "2021-02-14",
            "2022-02-04",
            "2023-02-23",
            "2024-02-12",
            "2025-03-03",
        )
        self.assertHolidayName(name, range(2004, 2050))
        self.assertNoHolidayName(name, "2012-02-24", "2013-02-13")

    def test_patriots_day(self):
        name = "Эх орончдын өдөр"
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-03-01" for year in range(2005, 2050))
        )
        self.assertNoHolidayName(name, self.workday_holidays, range(2004, 2005))
        self.assertNoHolidayName(name)

    def test_womens_day(self):
        self.assertHolidayName(
            "Олон улсын эмэгтэйчүүдийн өдөр", (f"{year}-03-08" for year in range(2004, 2050))
        )

    def test_military_day(self):
        name_2004 = "Зэвсэгт хүчний өдөр"
        name_2011 = "Монгол цэргийн өдөр"
        self.assertHolidayName(
            name_2004, self.workday_holidays, (f"{year}-03-18" for year in range(2004, 2011))
        )
        self.assertHolidayName(
            name_2011, self.workday_holidays, (f"{year}-03-18" for year in range(2011, 2050))
        )
        self.assertNoHolidayName(name_2004, self.workday_holidays, range(2011, 2050))
        self.assertNoHolidayName(name_2011, self.workday_holidays, range(2004, 2011))
        self.assertNoHolidayName(name_2004)
        self.assertNoHolidayName(name_2011)

    def test_health_protection_day(self):
        name = "Эрүүл мэндийг хамгаалах өдөр"
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-04-07" for year in range(2004, 2050))
        )
        self.assertNoHolidayName(name)

    def test_intellectual_property_protection_day(self):
        name = "Оюуны өмчийг хамгаалах өдөр"
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-04-26" for year in range(2004, 2050))
        )
        self.assertNoHolidayName(name)

    def test_family_day(self):
        name = "Гэр бүлийн өдөр"
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-05-15" for year in range(2004, 2050))
        )
        self.assertNoHolidayName(name)

    def test_childrens_day(self):
        self.assertHolidayName("Хүүхдийн баяр", (f"{year}-06-01" for year in range(2004, 2050)))

    def test_the_buddhas_birthday(self):
        name = "Бурхан багшийн Их дүйчин өдөр"
        self.assertHolidayName(
            name,
            "2021-05-26",
            "2022-06-14",
            "2023-06-04",
            "2024-05-23",
            "2025-06-11",
        )
        self.assertHolidayName(name, range(2020, 2050))
        self.assertNoHolidayName(name, range(2004, 2020))

    def test_national_flag_day(self):
        name = "Монгол Улсын төрийн далбааны өдөр"
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-07-10" for year in range(2009, 2050))
        )
        self.assertNoHolidayName(name, self.workday_holidays, range(2004, 2009))
        self.assertNoHolidayName(name)

    def test_national_festival_and_peoples_revolution_anniversary(self):
        name = "Үндэсний их баяр наадам, Ардын хувьсгалын ойн баяр"

        # JUL 10.
        self.assertHolidayName(name, (f"{year}-07-10" for year in range(2023, 2050)))
        self.assertNoHolidayName(name, (f"{year}-07-10" for year in range(2004, 2023)))

        # JUL 11, 12, 13.
        for year in range(2004, 2050):
            self.assertHolidayName(name, f"{year}-07-11", f"{year}-07-12", f"{year}-07-13")

        # JUL 14, 15.
        for year in range(2014, 2050):
            self.assertHolidayName(name, f"{year}-07-14", f"{year}-07-15")
        for year in range(2004, 2014):
            self.assertNoHolidayName(name, f"{year}-07-14", f"{year}-07-15")

    def test_youth_day(self):
        name = "Залуучуудын өдөр"
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-08-25" for year in range(2004, 2050))
        )
        self.assertNoHolidayName(name)

    def test_new_harvest_days(self):
        name = "Шинэ ургацын өдрүүд"
        for year in range(2007, 2050):
            self.assertHolidayName(
                name, self.workday_holidays, (f"{year}-09-05", f"{year}-10-01", f"{year}-10-20")
            )
        self.assertNoHolidayName(name, self.workday_holidays, range(2004, 2007))
        self.assertNoHolidayName(name)

    def test_memorial_day_of_political_victims(self):
        name = "Улс төрийн хэлмэгдэгсдийн дурсгалын өдөр"
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-09-10" for year in range(2004, 2050))
        )
        self.assertNoHolidayName(name)

    def test_elders_day(self):
        name = "Ахмадын өдөр"
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-10-01" for year in range(2004, 2050))
        )
        self.assertNoHolidayName(name)

    def test_capital_day(self):
        name_2004 = "Монгол Улсын Нийслэлийн өдөр"
        name_2021 = "Монгол Улсын нийслэл хотын өдөр"
        self.assertHolidayName(
            name_2004, self.workday_holidays, (f"{year}-10-29" for year in range(2004, 2021))
        )
        self.assertHolidayName(
            name_2021, self.workday_holidays, (f"{year}-10-29" for year in range(2021, 2050))
        )
        self.assertNoHolidayName(name_2004, self.workday_holidays, range(2021, 2050))
        self.assertNoHolidayName(name_2021, self.workday_holidays, range(2004, 2021))
        self.assertNoHolidayName(name_2004)
        self.assertNoHolidayName(name_2021)

    def test_genghis_khans_birthday(self):
        name = "Их Эзэн Чингис хааны өдөр"
        self.assertHolidayName(
            name,
            "2021-11-05",
            "2022-11-24",
            "2023-11-14",
            "2024-11-02",
            "2025-11-21",
        )
        self.assertHolidayName(name, range(2012, 2050))
        self.assertNoHolidayName(name, range(2004, 2012))

    def test_republic_day(self):
        name_2004 = "Бүгд Найрамдах Улс тунхагласны баяр"
        name_2012 = "Бүгд Найрамдах Улс тунхагласан өдөр"

        # Public holidays.
        self.assertHolidayName(name_2004, (f"{year}-11-26" for year in range(2004, 2012)))
        self.assertHolidayName(name_2012, (f"{year}-11-26" for year in range(2016, 2050)))
        self.assertNoHolidayName(name_2004, range(2012, 2050))
        self.assertNoHolidayName(name_2012, range(2004, 2016))

        # Workday holidays.
        self.assertHolidayName(
            name_2012, self.workday_holidays, (f"{year}-11-26" for year in range(2012, 2016))
        )
        self.assertNoHolidayName(
            name_2012, self.workday_holidays, range(2004, 2012), range(2016, 2050)
        )

    def test_democracy_and_human_rights_day(self):
        name = "Ардчилал, хүний эрхийн өдөр"
        self.assertHolidayName(
            name, self.workday_holidays, (f"{year}-12-10" for year in range(2004, 2050))
        )
        self.assertNoHolidayName(name)

    def test_independence_day(self):
        name_2007 = "Үндэсний эрх чөлөөний өдөр"
        name_2011 = "Үндэсний эрх чөлөө, тусгаар тогтнолоо сэргээсний баярын өдөр"

        # Public holidays.
        self.assertHolidayName(name_2011, (f"{year}-12-29" for year in range(2011, 2050)))
        self.assertNoHolidayName(name_2007)
        self.assertNoHolidayName(name_2011, range(2004, 2011))

        # Workday holidays.
        self.assertHolidayName(
            name_2007, self.workday_holidays, (f"{year}-12-29" for year in range(2007, 2011))
        )
        self.assertNoHolidayName(
            name_2007, self.workday_holidays, range(2004, 2007), range(2011, 2050)
        )
        self.assertNoHolidayName(name_2011, self.workday_holidays)

    def test_2025(self):
        self.assertHolidays(
            Mongolia(years=2025),
            ("2025-01-01", "Шинэ жил"),
            ("2025-03-01", "Цагаан сар"),
            ("2025-03-02", "Цагаан сар"),
            ("2025-03-03", "Цагаан сар"),
            ("2025-03-08", "Олон улсын эмэгтэйчүүдийн өдөр"),
            ("2025-06-01", "Хүүхдийн баяр"),
            ("2025-06-11", "Бурхан багшийн Их дүйчин өдөр"),
            ("2025-07-10", "Үндэсний их баяр наадам, Ардын хувьсгалын ойн баяр"),
            ("2025-07-11", "Үндэсний их баяр наадам, Ардын хувьсгалын ойн баяр"),
            ("2025-07-12", "Үндэсний их баяр наадам, Ардын хувьсгалын ойн баяр"),
            ("2025-07-13", "Үндэсний их баяр наадам, Ардын хувьсгалын ойн баяр"),
            ("2025-07-14", "Үндэсний их баяр наадам, Ардын хувьсгалын ойн баяр"),
            ("2025-07-15", "Үндэсний их баяр наадам, Ардын хувьсгалын ойн баяр"),
            ("2025-11-21", "Их Эзэн Чингис хааны өдөр"),
            ("2025-11-26", "Бүгд Найрамдах Улс тунхагласан өдөр"),
            ("2025-12-29", "Үндэсний эрх чөлөө, тусгаар тогтнолоо сэргээсний баярын өдөр"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Шинэ жил"),
            ("2024-01-13", "Монгол Улсын Үндсэн хуулийн өдөр"),
            ("2024-02-10", "Цагаан сар"),
            ("2024-02-11", "Цагаан сар"),
            ("2024-02-12", "Цагаан сар"),
            ("2024-03-01", "Эх орончдын өдөр"),
            ("2024-03-08", "Олон улсын эмэгтэйчүүдийн өдөр"),
            ("2024-03-18", "Монгол цэргийн өдөр"),
            ("2024-04-07", "Эрүүл мэндийг хамгаалах өдөр"),
            ("2024-04-26", "Оюуны өмчийг хамгаалах өдөр"),
            ("2024-05-15", "Гэр бүлийн өдөр"),
            ("2024-05-23", "Бурхан багшийн Их дүйчин өдөр"),
            ("2024-06-01", "Хүүхдийн баяр"),
            (
                "2024-07-10",
                "Монгол Улсын төрийн далбааны өдөр; "
                "Үндэсний их баяр наадам, Ардын хувьсгалын ойн баяр",
            ),
            ("2024-07-11", "Үндэсний их баяр наадам, Ардын хувьсгалын ойн баяр"),
            ("2024-07-12", "Үндэсний их баяр наадам, Ардын хувьсгалын ойн баяр"),
            ("2024-07-13", "Үндэсний их баяр наадам, Ардын хувьсгалын ойн баяр"),
            ("2024-07-14", "Үндэсний их баяр наадам, Ардын хувьсгалын ойн баяр"),
            ("2024-07-15", "Үндэсний их баяр наадам, Ардын хувьсгалын ойн баяр"),
            ("2024-08-25", "Залуучуудын өдөр"),
            ("2024-09-05", "Шинэ ургацын өдрүүд"),
            ("2024-09-06", "Шинэ ургацын өдрүүд"),
            ("2024-09-07", "Шинэ ургацын өдрүүд"),
            ("2024-09-08", "Шинэ ургацын өдрүүд"),
            ("2024-09-09", "Шинэ ургацын өдрүүд"),
            ("2024-09-10", "Улс төрийн хэлмэгдэгсдийн дурсгалын өдөр; Шинэ ургацын өдрүүд"),
            ("2024-09-11", "Шинэ ургацын өдрүүд"),
            ("2024-09-12", "Шинэ ургацын өдрүүд"),
            ("2024-09-13", "Шинэ ургацын өдрүүд"),
            ("2024-09-14", "Шинэ ургацын өдрүүд"),
            ("2024-09-15", "Шинэ ургацын өдрүүд"),
            ("2024-09-16", "Шинэ ургацын өдрүүд"),
            ("2024-09-17", "Шинэ ургацын өдрүүд"),
            ("2024-09-18", "Шинэ ургацын өдрүүд"),
            ("2024-09-19", "Шинэ ургацын өдрүүд"),
            ("2024-09-20", "Шинэ ургацын өдрүүд"),
            ("2024-09-21", "Шинэ ургацын өдрүүд"),
            ("2024-09-22", "Шинэ ургацын өдрүүд"),
            ("2024-09-23", "Шинэ ургацын өдрүүд"),
            ("2024-09-24", "Шинэ ургацын өдрүүд"),
            ("2024-09-25", "Шинэ ургацын өдрүүд"),
            ("2024-09-26", "Шинэ ургацын өдрүүд"),
            ("2024-09-27", "Шинэ ургацын өдрүүд"),
            ("2024-09-28", "Шинэ ургацын өдрүүд"),
            ("2024-09-29", "Шинэ ургацын өдрүүд"),
            ("2024-09-30", "Шинэ ургацын өдрүүд"),
            ("2024-10-01", "Ахмадын өдөр; Шинэ ургацын өдрүүд"),
            ("2024-10-02", "Шинэ ургацын өдрүүд"),
            ("2024-10-03", "Шинэ ургацын өдрүүд"),
            ("2024-10-04", "Шинэ ургацын өдрүүд"),
            ("2024-10-05", "Шинэ ургацын өдрүүд"),
            ("2024-10-06", "Шинэ ургацын өдрүүд"),
            ("2024-10-07", "Шинэ ургацын өдрүүд"),
            ("2024-10-08", "Шинэ ургацын өдрүүд"),
            ("2024-10-09", "Шинэ ургацын өдрүүд"),
            ("2024-10-10", "Шинэ ургацын өдрүүд"),
            ("2024-10-11", "Шинэ ургацын өдрүүд"),
            ("2024-10-12", "Шинэ ургацын өдрүүд"),
            ("2024-10-13", "Шинэ ургацын өдрүүд"),
            ("2024-10-14", "Шинэ ургацын өдрүүд"),
            ("2024-10-15", "Шинэ ургацын өдрүүд"),
            ("2024-10-16", "Шинэ ургацын өдрүүд"),
            ("2024-10-17", "Шинэ ургацын өдрүүд"),
            ("2024-10-18", "Шинэ ургацын өдрүүд"),
            ("2024-10-19", "Шинэ ургацын өдрүүд"),
            ("2024-10-20", "Шинэ ургацын өдрүүд"),
            ("2024-10-29", "Монгол Улсын нийслэл хотын өдөр"),
            ("2024-11-02", "Их Эзэн Чингис хааны өдөр"),
            ("2024-11-26", "Бүгд Найрамдах Улс тунхагласан өдөр"),
            ("2024-12-10", "Ардчилал, хүний эрхийн өдөр"),
            ("2024-12-29", "Үндэсний эрх чөлөө, тусгаар тогтнолоо сэргээсний баярын өдөр"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-13", "Constitution Day"),
            ("2024-02-10", "Lunar New Year"),
            ("2024-02-11", "Lunar New Year"),
            ("2024-02-12", "Lunar New Year"),
            ("2024-03-01", "Patriots' Day"),
            ("2024-03-08", "International Women's Day"),
            ("2024-03-18", "Military Day"),
            ("2024-04-07", "Health Protection Day"),
            ("2024-04-26", "Intellectual Property Protection Day"),
            ("2024-05-15", "Family Day"),
            ("2024-05-23", "The Buddha's Birthday"),
            ("2024-06-01", "Children's Day"),
            (
                "2024-07-10",
                "National Festival and People's Revolution Anniversary; National Flag Day",
            ),
            ("2024-07-11", "National Festival and People's Revolution Anniversary"),
            ("2024-07-12", "National Festival and People's Revolution Anniversary"),
            ("2024-07-13", "National Festival and People's Revolution Anniversary"),
            ("2024-07-14", "National Festival and People's Revolution Anniversary"),
            ("2024-07-15", "National Festival and People's Revolution Anniversary"),
            ("2024-08-25", "Youth Day"),
            ("2024-09-05", "New Harvest Days"),
            ("2024-09-06", "New Harvest Days"),
            ("2024-09-07", "New Harvest Days"),
            ("2024-09-08", "New Harvest Days"),
            ("2024-09-09", "New Harvest Days"),
            ("2024-09-10", "Memorial Day of Political Victims; New Harvest Days"),
            ("2024-09-11", "New Harvest Days"),
            ("2024-09-12", "New Harvest Days"),
            ("2024-09-13", "New Harvest Days"),
            ("2024-09-14", "New Harvest Days"),
            ("2024-09-15", "New Harvest Days"),
            ("2024-09-16", "New Harvest Days"),
            ("2024-09-17", "New Harvest Days"),
            ("2024-09-18", "New Harvest Days"),
            ("2024-09-19", "New Harvest Days"),
            ("2024-09-20", "New Harvest Days"),
            ("2024-09-21", "New Harvest Days"),
            ("2024-09-22", "New Harvest Days"),
            ("2024-09-23", "New Harvest Days"),
            ("2024-09-24", "New Harvest Days"),
            ("2024-09-25", "New Harvest Days"),
            ("2024-09-26", "New Harvest Days"),
            ("2024-09-27", "New Harvest Days"),
            ("2024-09-28", "New Harvest Days"),
            ("2024-09-29", "New Harvest Days"),
            ("2024-09-30", "New Harvest Days"),
            ("2024-10-01", "Elders' Day; New Harvest Days"),
            ("2024-10-02", "New Harvest Days"),
            ("2024-10-03", "New Harvest Days"),
            ("2024-10-04", "New Harvest Days"),
            ("2024-10-05", "New Harvest Days"),
            ("2024-10-06", "New Harvest Days"),
            ("2024-10-07", "New Harvest Days"),
            ("2024-10-08", "New Harvest Days"),
            ("2024-10-09", "New Harvest Days"),
            ("2024-10-10", "New Harvest Days"),
            ("2024-10-11", "New Harvest Days"),
            ("2024-10-12", "New Harvest Days"),
            ("2024-10-13", "New Harvest Days"),
            ("2024-10-14", "New Harvest Days"),
            ("2024-10-15", "New Harvest Days"),
            ("2024-10-16", "New Harvest Days"),
            ("2024-10-17", "New Harvest Days"),
            ("2024-10-18", "New Harvest Days"),
            ("2024-10-19", "New Harvest Days"),
            ("2024-10-20", "New Harvest Days"),
            ("2024-10-29", "Capital City Day"),
            ("2024-11-02", "Genghis Khan's Birthday"),
            ("2024-11-26", "Republic Day"),
            ("2024-12-10", "Democracy and Human Rights Day"),
            ("2024-12-29", "National Freedom and Independence Day"),
        )
