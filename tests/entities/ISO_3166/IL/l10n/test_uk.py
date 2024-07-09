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

from holidays.entities.ISO_3166.IL import IlHolidays
from tests.common import CommonCountryTests


class TestIlHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(IlHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2021-02-25", "Тааніт-Естер"),
            ("2021-02-26", "Пурім"),
            ("2021-03-28", "Песах"),
            ("2021-03-29", "Свято Песах"),
            ("2021-03-30", "Свято Песах"),
            ("2021-03-31", "Свято Песах"),
            ("2021-04-01", "Свято Песах"),
            ("2021-04-02", "Свято Песах"),
            ("2021-04-03", "Сьомий день Песаха"),
            ("2021-04-14", "День памʼяті (вихідний)"),
            ("2021-04-15", "День незалежності (вихідний)"),
            ("2021-04-30", "Лаг ба-Омер"),
            ("2021-05-10", "День Єрусалиму"),
            ("2021-05-17", "Шавуот"),
            ("2021-07-18", "Тиша Бе-Ав"),
            ("2021-09-07", "Рош га-Шана"),
            ("2021-09-08", "Рош га-Шана"),
            ("2021-09-16", "Йом Кіпур"),
            ("2021-09-21", "Суккот"),
            ("2021-09-22", "Свято Суккот"),
            ("2021-09-23", "Свято Суккот"),
            ("2021-09-24", "Свято Суккот"),
            ("2021-09-25", "Свято Суккот"),
            ("2021-09-26", "Свято Суккот"),
            ("2021-09-28", "Сімхат Тора / Шміні Ацерет"),
            ("2021-11-04", "Сігд"),
            ("2021-11-29", "Ханука"),
            ("2021-11-30", "Ханука"),
            ("2021-12-01", "Ханука"),
            ("2021-12-02", "Ханука"),
            ("2021-12-03", "Ханука"),
            ("2021-12-04", "Ханука"),
            ("2021-12-05", "Ханука"),
            ("2021-12-06", "Ханука"),
        )
