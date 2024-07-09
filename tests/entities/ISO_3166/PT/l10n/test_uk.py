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

from holidays.entities.ISO_3166.PT import PtHolidays
from tests.common import CommonCountryTests


class TestPtHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PtHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-03-01", "Карнавал"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-25", "День Свободи"),
            ("2022-05-01", "День праці"),
            ("2022-06-10", "День Португалії, Камоенса і португальських громад"),
            ("2022-06-13", "День Святого Антонія"),
            ("2022-06-16", "Свято Тіла і Крові Христових"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-10-05", "День Республіки"),
            ("2022-11-01", "День усіх святих"),
            ("2022-12-01", "День відновлення незалежності"),
            ("2022-12-08", "Непорочне зачаття Діви Марії"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
            ("2022-12-31", "Переддень Нового року"),
        )
