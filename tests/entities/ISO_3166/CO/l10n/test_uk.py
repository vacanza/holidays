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

from holidays.entities.ISO_3166.CO import CoHolidays
from tests.common import CommonCountryTests


class TestCoHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CoHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-01-10", "Богоявлення (вихідний)"),
            ("2022-03-21", "День Святого Йосипа (вихідний)"),
            ("2022-04-14", "Великий четвер"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-05-01", "День праці"),
            ("2022-05-30", "Вознесіння Господнє (вихідний)"),
            ("2022-06-20", "Свято Тіла і Крові Христових (вихідний)"),
            ("2022-06-27", "Свято Найсвятішого Серця Ісуса (вихідний)"),
            ("2022-07-04", "День Святих Петра і Павла (вихідний)"),
            ("2022-07-20", "День незалежності"),
            ("2022-08-07", "Річниця перемоги при Бояка"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-10-17", "День Колумба (вихідний)"),
            ("2022-11-07", "День усіх святих (вихідний)"),
            ("2022-11-14", "День незалежності Картахени (вихідний)"),
            ("2022-12-08", "Непорочне зачаття Діви Марії"),
            ("2022-12-25", "Різдво Христове"),
        )
