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

from holidays.entities.ISO_3166.CY import CyHolidays
from tests.common import CommonCountryTests


class TestCyHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CyHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Новий рік"),
            ("2023-01-06", "Богоявлення"),
            ("2023-02-27", "Чистий понеділок"),
            ("2023-03-25", "День незалежності Греції"),
            ("2023-04-01", "Національне свято Кіпру"),
            ("2023-04-14", "Страсна пʼятниця"),
            ("2023-04-15", "Велика субота"),
            ("2023-04-16", "Великдень"),
            ("2023-04-17", "Великодній понеділок"),
            ("2023-04-18", "Великодній вівторок"),
            ("2023-05-01", "День праці"),
            ("2023-06-05", "День Святого Духа"),
            ("2023-08-15", "Успіння Пресвятої Богородиці"),
            ("2023-10-01", "День незалежності Кіпру"),
            ("2023-10-28", "День Охі"),
            ("2023-12-24", "Святий вечір"),
            ("2023-12-25", "Різдво Христове"),
            ("2023-12-26", "Другий день Різдва"),
        )
