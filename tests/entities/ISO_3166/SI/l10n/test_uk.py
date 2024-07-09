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

from holidays.entities.ISO_3166.SI import SiHolidays
from tests.common import CommonCountryTests


class TestSiHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SiHolidays, language="uk")

    def test_uk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Новий рік"),
            ("2022-01-02", "Новий рік"),
            ("2022-02-08", "День Прешерена"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-04-27", "День спротиву окупантам"),
            ("2022-05-01", "День праці"),
            ("2022-05-02", "День праці"),
            ("2022-06-25", "День державності"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-10-31", "День Реформації"),
            ("2022-11-01", "День памʼяті померлих"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "День незалежності та єднання"),
        )
