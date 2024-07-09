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

from holidays.entities.ISO_3166.VE import VeHolidays
from tests.common import CommonCountryTests


class TestVeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(VeHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2021-01-01", "Новий рік"),
            ("2021-02-15", "Карнавальний понеділок"),
            ("2021-02-16", "Карнавальний вівторок"),
            ("2021-04-01", "Великий четвер"),
            ("2021-04-02", "Страсна пʼятниця"),
            ("2021-04-19", "День проголошення незалежності"),
            ("2021-05-01", "Міжнародний день трудящих"),
            ("2021-06-24", "День битви при Карабобо"),
            ("2021-07-05", "День незалежності"),
            ("2021-07-24", "Річниця Сімона Болівара"),
            ("2021-10-12", "День спротиву корінних народів"),
            ("2021-12-24", "Святий вечір"),
            ("2021-12-25", "Різдво Христове"),
            ("2021-12-31", "Переддень Нового року"),
        )
