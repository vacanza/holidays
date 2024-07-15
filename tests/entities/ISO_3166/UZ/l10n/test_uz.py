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
        super().setUpClass(UzHolidays)

    def test_uz(self):
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
