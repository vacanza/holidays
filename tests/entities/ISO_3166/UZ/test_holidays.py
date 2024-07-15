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

from holidays.entities.ISO_3166.UZ import UzHolidays
from tests.common import CommonCountryTests


class TestUzbekistan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(UzHolidays, years=range(1992, 2050))

    def test_no_holidays(self):
        self.assertNoHolidays(UzHolidays(years=1991))

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
            UzHolidays(years=2020),
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
            UzHolidays(years=2021),
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
            UzHolidays(years=2022),
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
