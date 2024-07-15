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
        super().setUpClass(RoHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "Новий рік"),
            ("2018-01-02", "Новий рік"),
            ("2018-01-24", "День обʼєднання Дунайських князівств"),
            ("2018-04-06", "Великдень"),
            ("2018-04-08", "Великдень"),
            ("2018-04-09", "Великдень"),
            ("2018-05-01", "День праці"),
            ("2018-05-27", "Трійця"),
            ("2018-05-28", "Трійця"),
            ("2018-06-01", "День захисту дітей"),
            ("2018-08-15", "Успіння Пресвятої Богородиці"),
            ("2018-11-30", "День святого Андрія Первозваного"),
            ("2018-12-01", "Національний день Румунії"),
            ("2018-12-25", "Різдво Христове"),
            ("2018-12-26", "Різдво Христове"),
        )
