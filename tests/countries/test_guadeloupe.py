#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.countries.guadeloupe import Guadeloupe, GP, GLP
from tests.common import TestCase


class TestGuadeloupe(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Guadeloupe)

    def test_country_aliases(self):
        self.assertCountryAliases(Guadeloupe, GP, GLP)

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "Jour de l'an"),
            ("2022-03-24", "Mi-Carême"),
            ("2022-04-15", "Vendredi saint"),
            ("2022-04-18", "Lundi de Pâques"),
            ("2022-05-01", "Fête du Travail"),
            ("2022-05-08", "Fête de la Victoire"),
            ("2022-05-26", "Ascension"),
            ("2022-05-27", "Abolition de l'esclavage"),
            ("2022-06-06", "Lundi de Pentecôte"),
            ("2022-07-14", "Fête nationale"),
            ("2022-07-21", "Fête de Victor Schoelcher"),
            ("2022-08-15", "Assomption"),
            ("2022-11-01", "Toussaint"),
            ("2022-11-11", "Armistice"),
            ("2022-12-25", "Noël"),
        )
