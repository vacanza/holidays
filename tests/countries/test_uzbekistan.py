#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.uzbekistan import Uzbekistan, UZ, UZB
from tests.common import CommonCountryTests


class TestUzbekistan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Uzbekistan, years=range(1992, 2050))

    def test_country_aliases(self):
        self.assertAliases(Uzbekistan, UZ, UZB)

    def test_no_holidays(self):
        self.assertNoHolidays(Uzbekistan(years=1991))

    def test_new_years_day(self):
        self.assertHolidayName("Yangi yil", (f"{year}-01-01" for year in range(1992, 2050)))

    def test_womens_day(self):
        self.assertHolidayName(
            "Xotin-qizlar kuni", (f"{year}-03-08" for year in range(1992, 2050))
        )

    def test_nowruz(self):
        self.assertHolidayName("Navro‘z bayrami", (f"{year}-03-21" for year in range(1992, 2050)))

    def test_memory_and_honor_day(self):
        name_1 = "G‘alaba kuni"
        name_2 = "Xotira va qadrlash kuni"
        self.assertHolidayName(name_1, (f"{year}-05-09" for year in range(1992, 1999)))
        self.assertHolidayName(name_2, (f"{year}-05-09" for year in range(1999, 2050)))
        self.assertNoHolidayName(name_1, range(1999, 2050))
        self.assertNoHolidayName(name_2, range(1992, 1999))

    def test_independence_day(self):
        self.assertHolidayName("Mustaqillik kuni", (f"{year}-09-01" for year in range(1992, 2050)))

    def test_teachers_and_instructors_day(self):
        name = "O‘qituvchi va murabbiylar kuni"
        self.assertHolidayName(name, (f"{year}-10-01" for year in range(1997, 2050)))
        self.assertNoHolidayName(name, range(1992, 1997))

    def test_constitution_day(self):
        name = "O‘zbekiston Respublikasi Konstitutsiyasi kuni"
        self.assertHolidayName(name, (f"{year}-12-08" for year in range(1993, 2050)))
        self.assertNoHolidayName(name, 1992)

    def test_eid_al_fitr(self):
        self.assertHolidayName(
            "Ro‘za hayit",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
        )

    def test_eid_al_adha(self):
        self.assertHolidayName(
            "Qurbon hayit",
            "2006-01-10",
            "2006-12-30",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
        )

    def test_observed(self):
        dt = (
            "2023-10-02",
            "2024-06-17",
            "2024-09-02",
            "2024-12-09",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test2020(self):
        self.assertHolidayDates(
            Uzbekistan(years=2020),
            "2020-01-01",
            "2020-01-02",
            "2020-03-08",
            "2020-03-21",
            "2020-03-23",
            "2020-05-09",
            "2020-05-24",
            "2020-07-31",
            "2020-08-31",
            "2020-09-01",
            "2020-10-01",
            "2020-12-08",
        )

    def test2021(self):
        self.assertHolidayDates(
            Uzbekistan(years=2021),
            "2021-01-01",
            "2021-03-08",
            "2021-03-21",
            "2021-03-22",
            "2021-05-09",
            "2021-05-13",
            "2021-05-14",
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            "2021-09-01",
            "2021-09-02",
            "2021-09-03",
            "2021-10-01",
            "2021-12-08",
            "2021-12-31",
        )

    def test2022(self):
        self.assertHolidays(
            Uzbekistan(years=2022),
            ("2022-01-01", "Yangi yil"),
            ("2022-01-03", "Prezidentining farmoni bilan qo‘shimcha dam olish kuni"),
            ("2022-01-04", "Dam olish kuni (08/01 2022 dan ko‘chirilgan)"),
            ("2022-03-08", "Xotin-qizlar kuni"),
            ("2022-03-21", "Navro‘z bayrami"),
            ("2022-03-22", "Prezidentining farmoni bilan qo‘shimcha dam olish kuni"),
            ("2022-03-23", "Prezidentining farmoni bilan qo‘shimcha dam olish kuni"),
            ("2022-05-02", "Ro‘za hayit"),
            ("2022-05-03", "Prezidentining farmoni bilan qo‘shimcha dam olish kuni"),
            ("2022-05-04", "Dam olish kuni (07/05 2022 dan ko‘chirilgan)"),
            ("2022-05-09", "Xotira va qadrlash kuni"),
            ("2022-07-09", "Qurbon hayit"),
            ("2022-07-11", "Prezidentining farmoni bilan qo‘shimcha dam olish kuni"),
            ("2022-07-12", "Dam olish kuni (16/07 2022 dan ko‘chirilgan)"),
            ("2022-09-01", "Mustaqillik kuni"),
            ("2022-09-02", "Prezidentining farmoni bilan qo‘shimcha dam olish kuni"),
            ("2022-10-01", "O‘qituvchi va murabbiylar kuni"),
            ("2022-12-08", "O‘zbekiston Respublikasi Konstitutsiyasi kuni"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Yangi yil"),
            ("2023-01-02", "Prezidentining farmoni bilan qo‘shimcha dam olish kuni"),
            ("2023-01-03", "Dam olish kuni (07/01 2023 dan ko‘chirilgan)"),
            ("2023-03-08", "Xotin-qizlar kuni"),
            ("2023-03-20", "Dam olish kuni (11/03 2023 dan ko‘chirilgan)"),
            ("2023-03-21", "Navro‘z bayrami"),
            ("2023-03-22", "Dam olish kuni (25/03 2023 dan ko‘chirilgan)"),
            ("2023-04-21", "Ro‘za hayit"),
            ("2023-04-24", "Prezidentining farmoni bilan qo‘shimcha dam olish kuni"),
            ("2023-05-09", "Xotira va qadrlash kuni"),
            ("2023-06-28", "Qurbon hayit"),
            ("2023-06-29", "Prezidentining farmoni bilan qo‘shimcha dam olish kuni"),
            ("2023-06-30", "Prezidentining farmoni bilan qo‘shimcha dam olish kuni"),
            ("2023-09-01", "Mustaqillik kuni"),
            ("2023-10-01", "O‘qituvchi va murabbiylar kuni"),
            ("2023-10-02", "O‘qituvchi va murabbiylar kuni (ko‘chirilgan)"),
            ("2023-12-08", "O‘zbekiston Respublikasi Konstitutsiyasi kuni"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "Additional day off by Presidential decree"),
            ("2023-01-03", "Day off (substituted from 01/07/2023)"),
            ("2023-03-08", "Women's Day"),
            ("2023-03-20", "Day off (substituted from 03/11/2023)"),
            ("2023-03-21", "Nowruz"),
            ("2023-03-22", "Day off (substituted from 03/25/2023)"),
            ("2023-04-21", "Eid al-Fitr"),
            ("2023-04-24", "Additional day off by Presidential decree"),
            ("2023-05-09", "Day of Memory and Honor"),
            ("2023-06-28", "Eid al-Adha"),
            ("2023-06-29", "Additional day off by Presidential decree"),
            ("2023-06-30", "Additional day off by Presidential decree"),
            ("2023-09-01", "Independence Day"),
            ("2023-10-01", "Teachers and Instructors Day"),
            ("2023-10-02", "Teachers and Instructors Day (observed)"),
            ("2023-12-08", "Constitution Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2023-01-01", "Новий рік"),
            ("2023-01-02", "Додатковий вихідний згідно указу Президента"),
            ("2023-01-03", "Вихідний день (перенесено з 07.01.2023)"),
            ("2023-03-08", "Жіночий день"),
            ("2023-03-20", "Вихідний день (перенесено з 11.03.2023)"),
            ("2023-03-21", "Свято Новруз"),
            ("2023-03-22", "Вихідний день (перенесено з 25.03.2023)"),
            ("2023-04-21", "Рамазан-байрам"),
            ("2023-04-24", "Додатковий вихідний згідно указу Президента"),
            ("2023-05-09", "День памʼяті і шани"),
            ("2023-06-28", "Курбан-байрам"),
            ("2023-06-29", "Додатковий вихідний згідно указу Президента"),
            ("2023-06-30", "Додатковий вихідний згідно указу Президента"),
            ("2023-09-01", "День Незалежності"),
            ("2023-10-01", "День Вчителя і Наставника"),
            ("2023-10-02", "День Вчителя і Наставника (вихідний)"),
            ("2023-12-08", "День Конституції Республіки Узбекистан"),
        )
