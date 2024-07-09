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

from holidays.entities.ISO_3166.LT import LtHolidays
from tests.common import CommonCountryTests


class TestLithuania(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(LtHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-02-16", "День відновлення Литовської держави"),
            ("2022-03-11", "День відновлення незалежності Литви"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День матері; Міжнародний день трудящих"),
            ("2022-06-05", "День батька"),
            ("2022-06-24", "День роси та День Івана Купала"),
            ("2022-07-06", "День державності та День національного гімну"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-02", "День памʼяті (День всіх померлих)"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )
