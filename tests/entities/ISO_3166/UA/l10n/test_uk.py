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

from holidays.entities.ISO_3166.UA import UaHolidays
from tests.common import CommonCountryTests


class TestUaHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(UaHolidays)

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2021-01-01", "Новий рік"),
            ("2021-01-07", "Різдво Христове (за юліанським календарем)"),
            ("2021-01-08", "Вихідний день (перенесено з 16.01.2021)"),
            ("2021-03-08", "Міжнародний жіночий день"),
            ("2021-05-01", "День праці"),
            ("2021-05-02", "Великдень (Пасха)"),
            ("2021-05-03", "День праці (вихідний)"),
            ("2021-05-04", "Великдень (Пасха) (вихідний)"),
            ("2021-05-09", "День перемоги над нацизмом у Другій світовій війні (День перемоги)"),
            (
                "2021-05-10",
                "День перемоги над нацизмом у Другій світовій війні (День перемоги) (вихідний)",
            ),
            ("2021-06-20", "Трійця"),
            ("2021-06-21", "Трійця (вихідний)"),
            ("2021-06-28", "День Конституції України"),
            ("2021-08-23", "Вихідний день (перенесено з 28.08.2021)"),
            ("2021-08-24", "День незалежності України"),
            ("2021-10-14", "День захисників і захисниць України"),
            ("2021-10-15", "Вихідний день (перенесено з 23.10.2021)"),
            ("2021-12-25", "Різдво Христове (за григоріанським календарем)"),
            ("2021-12-27", "Різдво Христове (за григоріанським календарем) (вихідний)"),
        )
