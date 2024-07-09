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
        super().setUpClass(SkHolidays)

    def test_sk(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Deň vzniku Slovenskej republiky"),
            (
                "2022-01-06",
                "Zjavenie Pána (Traja králi a vianočný sviatok pravoslávnych kresťanov)",
            ),
            ("2022-04-15", "Veľký piatok"),
            ("2022-04-18", "Veľkonočný pondelok"),
            ("2022-05-01", "Sviatok práce"),
            ("2022-05-08", "Deň víťazstva nad fašizmom"),
            ("2022-07-05", "Sviatok svätého Cyrila a svätého Metoda"),
            ("2022-08-29", "Výročie Slovenského národného povstania"),
            ("2022-09-01", "Deň Ústavy Slovenskej republiky"),
            ("2022-09-15", "Sedembolestná Panna Mária"),
            ("2022-10-28", "Deň vzniku samostatného česko-slovenského štátu"),
            ("2022-11-01", "Sviatok Všetkých svätých"),
            ("2022-11-17", "Deň boja za slobodu a demokraciu"),
            ("2022-12-24", "Štedrý deň"),
            ("2022-12-25", "Prvý sviatok vianočný"),
            ("2022-12-26", "Druhý sviatok vianočný"),
        )
