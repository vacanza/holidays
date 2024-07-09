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

from holidays.entities.ISO_3166.BE import BeHolidays
from tests.common import CommonCountryTests


class TestBeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BeHolidays, language="fr")

    def test_fr(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nouvel An"),
            ("2022-04-15", "Vendredi Saint"),
            ("2022-04-17", "Pâques"),
            ("2022-04-18", "Lundi de Pâques"),
            ("2022-05-01", "Fête du Travail"),
            ("2022-05-26", "Ascension"),
            ("2022-05-27", "Vendredi suivant l'Ascension"),
            ("2022-06-05", "Pentecôte"),
            ("2022-06-06", "Lundi de Pentecôte"),
            ("2022-07-21", "Fête nationale"),
            ("2022-08-15", "Assomption"),
            ("2022-11-01", "Toussaint"),
            ("2022-11-11", "Jour de l'Armistice"),
            ("2022-12-25", "Noël"),
            ("2022-12-26", "Jour de fermeture bancaire"),
        )
