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

from holidays.entities.ISO_3166.MD import MdHolidays
from tests.common import CommonCountryTests


class TestMdHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MdHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-01-07", "Різдво Христове (за старим стилем)"),
            ("2022-01-08", "Різдво Христове (за старим стилем)"),
            ("2022-03-08", "Міжнародний жіночий день"),
            ("2022-04-24", "Великдень"),
            ("2022-04-25", "Великдень"),
            ("2022-05-01", "День міжнародної солідарності трудящих"),
            ("2022-05-02", "Проводи"),
            (
                "2022-05-09",
                "День Європи; День Перемоги та вшанування памʼяті героїв, "
                "полеглих за незалежність Батьківщини",
            ),
            ("2022-06-01", "День захисту дітей"),
            ("2022-08-27", "День незалежності Республіки Молдова"),
            ("2022-08-31", "День рідної мови"),
            ("2022-12-25", "Різдво Христове (за новим стилем)"),
        )
