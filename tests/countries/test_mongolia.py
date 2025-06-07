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

    def test_new_year(self):
        self.assertHolidayName("Шинэ жилийн баяр", (f"{year}-01-01" for year in range(2004, 2050)))

    def test_womens_day(self):
        self.assertHolidayName(
            "Олон улсын эмэгтэйчүүдийн өдөр", (f"{year}-03-08" for year in range(2004, 2050))
        )

    def test_childrens_day(self):
        self.assertHolidayName("Хүүхдийн баяр", (f"{year}-06-01" for year in range(2004, 2050)))

    def test_republic_day(self):
        self.assertHolidayName(
            "Бүгд Найрамдах Улс тунхагласан өдөр", (f"{year}-11-26" for year in range(2004, 2050))
        )

    def test_independence_day(self):
        name = "Үндэсний эрх чөлөө, тусгаар тогтнолоо сэргээсний баярын өдөр"
        self.assertHolidayName(
            name,
            (f"{year}-12-29" for year in range(2011, 2050)),
        )
        self.assertNoHolidayName(name, range(2004, 2011))
        name = "Үндэсний эрх чөлөөний өдөр"
        self.assertHolidayName(name, (f"{year}-12-29" for year in range(2007, 2011)))
        self.assertNoHolidayName(name, range(2004, 2007), range(2011, 2050))

    def test_2025(self):
        self.assertHolidays(
            Mongolia(years=2025),
            ("2025-01-01", "Шинэ жилийн баяр"),
            ("2025-03-08", "Олон улсын эмэгтэйчүүдийн өдөр"),
            ("2025-06-01", "Хүүхдийн баяр"),
            ("2025-07-11", "Наадам"),
            ("2025-07-12", "Наадмын баяр"),
            ("2025-07-13", "Наадмын баяр"),
            ("2025-07-14", "Наадмын баяр"),
            ("2025-07-15", "Наадмын баяр"),
            ("2025-11-26", "Бүгд Найрамдах Улс тунхагласан өдөр"),
            ("2025-12-29", "Үндэсний эрх чөлөө, тусгаар тогтнолоо сэргээсний баярын өдөр"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Шинэ жилийн баяр"),
            ("2024-03-08", "Олон улсын эмэгтэйчүүдийн өдөр"),
            ("2024-06-01", "Хүүхдийн баяр"),
            ("2024-07-11", "Наадам"),
            ("2024-07-12", "Наадмын баяр"),
            ("2024-07-13", "Наадмын баяр"),
            ("2024-07-14", "Наадмын баяр"),
            ("2024-07-15", "Наадмын баяр"),
            ("2024-11-26", "Бүгд Найрамдах Улс тунхагласан өдөр"),
            ("2024-12-29", "Үндэсний эрх чөлөө, тусгаар тогтнолоо сэргээсний баярын өдөр"),
        )

    def test_l10n_en_mn(self):
        self.assertLocalizedHolidays(
            "en_MN",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-08", "International Women's Day"),
            ("2024-06-01", "Children's Day"),
            ("2024-07-11", "Naadam"),
            ("2024-07-12", "Naadam Holiday"),
            ("2024-07-13", "Naadam Holiday"),
            ("2024-07-14", "Naadam Holiday"),
            ("2024-07-15", "Naadam Holiday"),
            ("2024-11-26", "Republic Day"),
            ("2024-12-29", "Restoration of Freedom and Independence Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-08", "International Women's Day"),
            ("2024-06-01", "Children's Day"),
            ("2024-07-11", "Naadam"),
            ("2024-07-12", "Naadam Holiday"),
            ("2024-07-13", "Naadam Holiday"),
            ("2024-07-14", "Naadam Holiday"),
            ("2024-07-15", "Naadam Holiday"),
            ("2024-11-26", "Republic Day"),
            ("2024-12-29", "Restoration of Freedom and Independence Day"),
        )
