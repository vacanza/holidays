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

from holidays.entities.ISO_3166.CU import CuHolidays
from tests.common import CommonCountryTests


class TestCuHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CuHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Тріумф революції"),
            ("2022-01-02", "День перемоги"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-05-01", "Міжнародний день трудящих"),
            ("2022-05-02", "Міжнародний день трудящих (вихідний)"),
            ("2022-07-25", "Вшанування памʼяті штурму Монкади"),
            ("2022-07-26", "День національного повстання"),
            ("2022-07-27", "Вшанування памʼяті штурму Монкади"),
            ("2022-10-10", "Початок війни за незалежність"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-31", "Переддень Нового року"),
        )
