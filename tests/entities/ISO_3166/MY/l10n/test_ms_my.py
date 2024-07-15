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

from holidays.entities.ISO_3166.MY import MyHolidays
from tests.common import CommonCountryTests


class TestMyHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MyHolidays)

    def test_ms_my(self):
        self.assertLocalizedHolidays(
            ("2023-01-22", "Tahun Baharu Cina"),
            ("2023-01-23", "Tahun Baharu Cina (Hari Kedua)"),
            ("2023-01-24", "Cuti Tahun Baharu Cina"),
            ("2023-04-21", "Hari Raya Puasa (pergantian hari)"),
            ("2023-04-22", "Hari Raya Puasa"),
            ("2023-04-23", "Hari Raya Puasa (Hari Kedua)"),
            ("2023-04-24", "Cuti Hari Raya Puasa (Hari Kedua)"),
            ("2023-05-01", "Hari Pekerja"),
            ("2023-05-04", "Hari Wesak"),
            ("2023-06-05", "Hari Keputeraan Rasmi Seri Paduka Baginda Yang di-Pertuan Agong"),
            ("2023-06-29", "Hari Raya Qurban"),
            ("2023-07-19", "Awal Muharam"),
            ("2023-08-31", "Hari Kebangsaan"),
            ("2023-09-16", "Hari Malaysia"),
            ("2023-09-28", "Hari Keputeraan Nabi Muhammad S.A.W."),
            ("2023-12-25", "Hari Krismas"),
        )
