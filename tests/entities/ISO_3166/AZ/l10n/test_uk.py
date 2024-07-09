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

from holidays.entities.ISO_3166.AZ import AzHolidays
from tests.common import CommonCountryTests


class TestAzHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AzHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Новий рік"),
            ("2023-01-02", "Новий рік"),
            ("2023-01-03", "Всесвітній день солідарності азербайджанців (вихідний)"),
            ("2023-01-04", "Новий рік (вихідний)"),
            ("2023-01-20", "День національної скорботи"),
            ("2023-03-08", "Жіночий день"),
            ("2023-03-20", "Свято Новруз"),
            ("2023-03-21", "Свято Новруз"),
            ("2023-03-22", "Свято Новруз"),
            ("2023-03-23", "Свято Новруз"),
            ("2023-03-24", "Свято Новруз"),
            ("2023-04-21", "Рамазан-байрам"),
            ("2023-04-22", "Рамазан-байрам"),
            ("2023-04-24", "Рамазан-байрам (вихідний)"),
            ("2023-05-09", "День перемоги над фашизмом"),
            ("2023-05-28", "День Незалежності"),
            ("2023-05-29", "День Незалежності (вихідний)"),
            ("2023-06-15", "День національного визволення азербайджанського народу"),
            ("2023-06-26", "День Збройних Сил"),
            ("2023-06-27", "Вихідний день (перенесено з 24.06.2023)"),
            ("2023-06-28", "Курбан-байрам"),
            ("2023-06-29", "Курбан-байрам"),
            ("2023-06-30", "Вихідний день (перенесено з 25.06.2023)"),
            ("2023-09-27", "День памʼяті"),
            ("2023-10-18", "День відновлення незалежності"),
            ("2023-11-08", "День Перемоги"),
            ("2023-11-09", "День державного прапора"),
            ("2023-11-10", "Вихідний день (перенесено з 04.11.2023)"),
            ("2023-11-12", "День Конституції"),
            ("2023-11-17", "День національного відродження"),
            ("2023-12-31", "Всесвітній день солідарності азербайджанців"),
        )
