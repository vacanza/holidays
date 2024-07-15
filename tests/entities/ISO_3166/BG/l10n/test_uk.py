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

from holidays.entities.ISO_3166.BG import BgHolidays
from tests.common import CommonCountryTests


class TestBgHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BgHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-01-03", "Новий рік (вихідний)"),
            ("2022-03-03", "День визволення Болгарії від османського іга"),
            ("2022-04-22", "Страсна пʼятниця"),
            ("2022-04-23", "Велика субота"),
            ("2022-04-24", "Великдень"),
            ("2022-04-25", "Великдень"),
            ("2022-05-01", "День праці та міжнародної солідарності трудящих"),
            ("2022-05-02", "День праці та міжнародної солідарності трудящих (вихідний)"),
            ("2022-05-06", "День Святого Георгія та День хоробрості і болгарської армії"),
            (
                "2022-05-24",
                "День святих братів Кирила і Мефодія, болгарської писемності, "
                "освіти і культури та словʼянської літератури",
            ),
            ("2022-09-06", "День обʼєднання"),
            ("2022-09-22", "День незалежності Болгарїі"),
            ("2022-11-01", "День національних будителів"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Різдво Христове"),
            ("2022-12-27", "Святий вечір (вихідний)"),
            ("2022-12-28", "Різдво Христове (вихідний)"),
        )
