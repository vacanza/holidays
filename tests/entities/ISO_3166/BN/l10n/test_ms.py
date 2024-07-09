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

from holidays.entities.ISO_3166.BN import BnHolidays
from tests.common import CommonCountryTests


class TestBnHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BnHolidays)

    def test_ms(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Awal Tahun Masihi"),
            ("2023-01-02", "Awal Tahun Masihi (diperhatikan)"),
            ("2023-01-22", "Tahun Baru Cina"),
            ("2023-01-23", "Tahun Baru Cina (diperhatikan)"),
            ("2023-02-18", "Israk dan Mikraj"),
            ("2023-02-23", "Hari Kebangsaan"),
            ("2023-03-23", "Hari Pertama Berpuasa"),
            ("2023-04-08", "Hari Nuzul Al-Quran"),
            ("2023-04-22", "Hari Raya Aidil Fitri"),
            ("2023-04-23", "Hari Raya Aidil Fitri"),
            ("2023-04-24", "Hari Raya Aidil Fitri"),
            ("2023-04-25", "Hari Raya Aidil Fitri (diperhatikan)"),
            ("2023-05-31", "Hari Angkatan Bersenjata Diraja Brunei"),
            ("2023-06-29", "Hari Raya Aidil Adha"),
            ("2023-07-15", "Hari Keputeraan KDYMM Sultan Brunei"),
            ("2023-07-19", "Awal Tahun Hijrah"),
            ("2023-09-28", "Maulidur Rasul"),
            ("2023-12-25", "Hari Natal"),
        )
