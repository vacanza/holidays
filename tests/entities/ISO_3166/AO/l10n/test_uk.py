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

from holidays.entities.ISO_3166.AO import AoHolidays
from tests.common import CommonCountryTests


class TestAoHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AoHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Новий рік"),
            ("2023-02-04", "День початку збройної боротьби за національне визволення"),
            ("2023-02-20", "Вихідний за Карнавал"),
            ("2023-02-21", "Карнавал"),
            ("2023-03-08", "Міжнародний жіночий день"),
            ("2023-03-23", "День визволення південної Африки"),
            ("2023-03-24", "Вихідний за День визволення південної Африки"),
            ("2023-04-03", "Вихідний за День миру та національного примирення"),
            ("2023-04-04", "День миру та національного примирення"),
            ("2023-04-07", "Страсна пʼятниця"),
            ("2023-05-01", "Міжнародний день трудящих"),
            ("2023-09-17", "День засновника нації та національного героя"),
            ("2023-11-02", "День усіх померлих"),
            ("2023-11-03", "Вихідний за День усіх померлих"),
            ("2023-11-11", "День національної незалежності"),
            ("2023-12-25", "Різдво Христове та День родини"),
        )
