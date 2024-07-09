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

from holidays.entities.ISO_3166.CL import ClHolidays
from tests.common import CommonCountryTests


class TestClHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ClHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-16", "Велика субота"),
            ("2022-05-01", "День праці"),
            ("2022-05-21", "День військово-морської слави"),
            ("2022-06-21", "Національний день корінних народів"),
            ("2022-06-27", "День Святих Петра і Павла"),
            ("2022-07-16", "Матір Божа Кармельська"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-09-16", "Національне свято"),
            ("2022-09-18", "День Незалежності"),
            ("2022-09-19", "День військової слави"),
            ("2022-10-10", "День зустрічі двох світів"),
            ("2022-10-31", "День Реформації"),
            ("2022-11-01", "День усіх святих"),
            ("2022-12-08", "Непорочне зачаття Діви Марії"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-31", "Банківський вихідний"),
        )
