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

from holidays.entities.ISO_3166.ES import EsHolidays
from tests.common import CommonCountryTests


class TestEsHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(EsHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2023-01-06", "Богоявлення"),
            ("2023-04-07", "Страсна пʼятниця"),
            ("2023-05-01", "День праці"),
            ("2023-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2023-10-12", "Національний день Іспанії"),
            ("2023-11-01", "День усіх святих"),
            ("2023-12-06", "День Конституції Іспанії"),
            ("2023-12-08", "Непорочне зачаття Діви Марії"),
            ("2023-12-25", "Різдво Христове"),
        )
