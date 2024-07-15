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

from holidays.entities.ISO_3166.BO import BoHolidays
from tests.common import CommonCountryTests


class TestBoHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BoHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Новий рік"),
            ("2023-01-02", "Новий рік (вихідний)"),
            ("2023-01-22", "День створення Багатонаціональної Держави Болівія"),
            ("2023-01-23", "День створення Багатонаціональної Держави Болівія (вихідний)"),
            ("2023-02-20", "Карнавал"),
            ("2023-02-21", "Карнавал"),
            ("2023-04-07", "Страсна пʼятниця"),
            ("2023-05-01", "День праці"),
            ("2023-06-08", "Свято Тіла і Крові Христових"),
            ("2023-06-21", "Новий рік Аймара"),
            ("2023-08-06", "День незалежності Болівії"),
            ("2023-08-07", "День незалежності Болівії (вихідний)"),
            ("2023-10-17", "День національної гідності"),
            ("2023-11-02", "День усіх померлих"),
            ("2023-12-25", "Різдво Христове"),
        )
