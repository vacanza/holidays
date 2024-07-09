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

from holidays.entities.ISO_3166.RO import RoHolidays
from tests.common import CommonCountryTests


class TestRoHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(RoHolidays)

    def test_ro(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "Anul Nou"),
            ("2018-01-02", "Anul Nou"),
            ("2018-01-24", "Ziua Unirii Principatelor Române"),
            ("2018-04-06", "Paștele"),
            ("2018-04-08", "Paștele"),
            ("2018-04-09", "Paștele"),
            ("2018-05-01", "Ziua Muncii"),
            ("2018-05-27", "Rusaliile"),
            ("2018-05-28", "Rusaliile"),
            ("2018-06-01", "Ziua Copilului"),
            ("2018-08-15", "Adormirea Maicii Domnului"),
            ("2018-11-30", "Sfantul Apostol Andrei cel Intai chemat"),
            ("2018-12-01", "Ziua Națională a României"),
            ("2018-12-25", "Crăciunul"),
            ("2018-12-26", "Crăciunul"),
        )
