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

from holidays.entities.ISO_3166.SK import SkHolidays
from tests.common import CommonCountryTests


class TestSkHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SkHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "День утворення Словацької Республіки"),
            ("2022-01-06", "Богоявлення (Три царі і православне Різдво Христове)"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-08", "День перемоги над фашизмом"),
            ("2022-07-05", "День Святих Кирила та Мефодія"),
            ("2022-08-29", "Річниця Словацького національного повстання"),
            ("2022-09-01", "День конституції Словацької Республіки"),
            ("2022-09-15", "День Божої Матері семи скорбот"),
            ("2022-10-28", "День створення незалежної чесько-словацької держави"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-17", "День боротьби за свободу та демократію"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )
