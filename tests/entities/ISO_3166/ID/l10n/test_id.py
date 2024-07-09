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

from holidays.entities.ISO_3166.ID import IdHolidays
from tests.common import CommonCountryTests


class TestIdHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(IdHolidays)

    def test_id(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Tahun Baru Masehi"),
            ("2022-02-01", "Tahun Baru Imlek"),
            ("2022-02-28", "Isra Mikraj Nabi Muhammad"),
            ("2022-03-03", "Hari Suci Nyepi"),
            ("2022-04-15", "Wafat Yesus Kristus"),
            ("2022-04-29", "Cuti Bersama Hari Raya Idulfitri"),
            ("2022-05-01", "Hari Buruh Internasional"),
            ("2022-05-02", "Hari Raya Idulfitri"),
            ("2022-05-03", "Hari kedua dari Hari Raya Idulfitri"),
            ("2022-05-04", "Cuti Bersama Hari Raya Idulfitri"),
            ("2022-05-05", "Cuti Bersama Hari Raya Idulfitri"),
            ("2022-05-06", "Cuti Bersama Hari Raya Idulfitri"),
            ("2022-05-16", "Hari Raya Waisak"),
            ("2022-05-26", "Kenaikan Yesus Kristus"),
            ("2022-06-01", "Hari Lahir Pancasila"),
            ("2022-07-10", "Hari Raya Iduladha"),
            ("2022-07-30", "Tahun Baru Islam"),
            ("2022-08-17", "Hari Kemerdekaan Republik Indonesia"),
            ("2022-10-08", "Maulid Nabi Muhammad"),
            ("2022-12-25", "Hari Raya Natal"),
            ("2022-12-26", "Cuti Bersama Hari Raya Natal"),
        )
