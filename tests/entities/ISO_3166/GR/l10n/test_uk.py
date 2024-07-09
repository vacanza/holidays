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

from holidays.entities.ISO_3166.GR import GrHolidays
from tests.common import CommonCountryTests


class TestGrHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(GrHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-01-06", "Богоявлення"),
            ("2022-03-07", "Чистий понеділок"),
            ("2022-03-25", "День незалежності"),
            ("2022-04-22", "Страсна пʼятниця"),
            ("2022-04-25", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-02", "День праці (вихідний)"),
            ("2022-06-13", "День Святого Духа"),
            ("2022-08-15", "Успіння Пресвятої Богородиці"),
            ("2022-10-28", "День Охі"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Собор Пресвятої Богородиці"),
            ("2022-12-31", "Переддень Нового року"),
        )
