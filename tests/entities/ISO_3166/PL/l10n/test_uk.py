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

from holidays.entities.ISO_3166.PL import PlHolidays
from tests.common import CommonCountryTests


class TestPlHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PlHolidays, language="uk")

    def test_uk_2018(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "Новий рік"),
            ("2018-01-06", "Богоявлення"),
            ("2018-04-01", "Великдень"),
            ("2018-04-02", "Великодній понеділок"),
            ("2018-05-01", "Національне свято"),
            ("2018-05-03", "Національне свято Третього Травня"),
            ("2018-05-20", "День Святої Трійці"),
            ("2018-05-31", "Свято Тіла і Крові Христових"),
            ("2018-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2018-11-01", "День усіх святих"),
            ("2018-11-11", "День Незалежності"),
            ("2018-11-12", "100-а річниця Дня Незалежності"),
            ("2018-12-25", "Різдво Христове"),
            ("2018-12-26", "Другий день Різдва"),
        )

    def test_uk_2022(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-01-06", "Богоявлення"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "Національне свято"),
            ("2022-05-03", "Національне свято Третього Травня"),
            ("2022-06-05", "День Святої Трійці"),
            ("2022-06-16", "Свято Тіла і Крові Христових"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-11", "День Незалежності"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )
