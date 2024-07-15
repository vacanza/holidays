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

from holidays.entities.ISO_3166.UZ import UzHolidays
from tests.common import CommonCountryTests


class TestUzbekistan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(UzHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Новий рік"),
            ("2023-01-02", "Додатковий вихідний згідно указу Президента"),
            ("2023-01-03", "Вихідний день (перенесено з 07.01.2023)"),
            ("2023-03-08", "Жіночий день"),
            ("2023-03-20", "Вихідний день (перенесено з 11.03.2023)"),
            ("2023-03-21", "Свято Новруз"),
            ("2023-03-22", "Вихідний день (перенесено з 25.03.2023)"),
            ("2023-04-21", "Рамазан-байрам"),
            ("2023-04-24", "Додатковий вихідний згідно указу Президента"),
            ("2023-05-09", "День памʼяті і шани"),
            ("2023-06-28", "Курбан-байрам"),
            ("2023-06-29", "Додатковий вихідний згідно указу Президента"),
            ("2023-06-30", "Додатковий вихідний згідно указу Президента"),
            ("2023-09-01", "День Незалежності"),
            ("2023-10-01", "День Вчителя і Наставника"),
            ("2023-10-02", "День Вчителя і Наставника (вихідний)"),
            ("2023-12-08", "День Конституції Республіки Узбекистан"),
        )
