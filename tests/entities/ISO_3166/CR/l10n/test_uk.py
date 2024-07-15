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

from holidays.entities.ISO_3166.CR import CrHolidays
from tests.common import CommonCountryTests


class TestCrHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CrHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-04-11", "День Хуана Сантамарії"),
            ("2022-04-14", "Великий четвер"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-05-01", "Міжнародний день трудящих"),
            ("2022-07-25", "День приєднання Нікої"),
            ("2022-08-02", "Свято Богоматері Ангелів"),
            ("2022-08-15", "День матері"),
            ("2022-09-04", "День чорношкірої людини та афро-костариканської культури (вихідний)"),
            ("2022-09-19", "День незалежності (вихідний)"),
            ("2022-12-05", "День ліквідації армії (вихідний)"),
            ("2022-12-25", "Різдво Христове"),
        )
