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

from holidays.entities.ISO_3166.MA import MaHolidays
from tests.common import CommonCountryTests


class TestMAHolicays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MaHolidays, language="fr")

    def test_fr(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Nouvel an"),
            ("2023-01-11", "Manifeste de l'indépendance"),
            ("2023-04-21", "Fête de la rupture du jeûne (estimé)"),
            ("2023-04-22", "Fête de la rupture du jeûne (estimé)"),
            ("2023-05-01", "Fête du Travail"),
            ("2023-06-28", "Fête du sacrifice (estimé)"),
            ("2023-06-29", "Fête du sacrifice (estimé)"),
            ("2023-07-19", "Nouvel an musulman (estimé)"),
            ("2023-07-30", "Fête du Trône"),
            ("2023-08-14", "Allégeance Oued Eddahab"),
            ("2023-08-20", "La révolution du roi et du peuple"),
            ("2023-08-21", "Fête de la Jeunesse"),
            ("2023-09-27", "Anniversaire du prophète (estimé)"),
            ("2023-09-28", "Anniversaire du prophète (estimé)"),
            ("2023-11-06", "La marche verte"),
            ("2023-11-18", "Fête de l'indépendance"),
        )
