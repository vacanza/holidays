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

from holidays.entities.ISO_3166.GE import GeHolidays
from tests.common import CommonCountryTests


class TestGeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(GeHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-01-02", "Новий рік"),
            ("2022-01-07", "Різдво Христове"),
            ("2022-01-19", "Богоявлення"),
            ("2022-03-03", "День матері"),
            ("2022-03-08", "Міжнародний жіночий день"),
            ("2022-04-09", "День національної єдності"),
            ("2022-04-22", "Страсна пʼятниця"),
            ("2022-04-23", "Велика субота"),
            ("2022-04-24", "Великдень"),
            ("2022-04-25", "Великодній понеділок"),
            ("2022-05-09", "День перемоги над фашизмом"),
            ("2022-05-12", "День святого Андрія Первозваного"),
            ("2022-05-26", "День незалежності"),
            ("2022-08-28", "Успіння Пресвятої Богородиці"),
            ("2022-10-14", "Свято Светіцховлоба, Ризи Господньої"),
            ("2022-11-23", "День святого Георгія"),
        )
