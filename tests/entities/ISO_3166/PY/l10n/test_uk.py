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

from holidays.entities.ISO_3166.PY import PyHolidays
from tests.common import CommonCountryTests


class TestPyHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PyHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-02-28", "День національних героїв"),
            ("2022-04-13", "Вихідний державних установ"),
            ("2022-04-14", "Великий четвер"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-05-01", "День трудящих"),
            ("2022-05-02", "Вихідний державних установ"),
            ("2022-05-14", "День незалежності"),
            ("2022-05-15", "День незалежності"),
            ("2022-06-12", "День мирного договору в Чако"),
            ("2022-08-15", "День заснування Асунсьйона"),
            ("2022-10-03", "День битви за Бокерон"),
            ("2022-12-08", "Успіння Пресвятої Богородиці"),
            ("2022-12-25", "Різдво Христове"),
        )
