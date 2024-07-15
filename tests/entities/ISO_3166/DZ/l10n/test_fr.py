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

from holidays.entities.ISO_3166.DZ import DzHolidays
from tests.common import CommonCountryTests


class TestDzHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(DzHolidays, language="fr")

    def test_fr(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nouvel an"),
            ("2022-01-12", "Nouvel an Amazigh"),
            ("2022-05-01", "Fête du Travail"),
            ("2022-05-02", "Fête de la rupture du jeûne (estimé)"),
            ("2022-05-03", "Congé de fête de la rupture du jeûne (estimé)"),
            ("2022-07-05", "Fête de l'indépendance"),
            ("2022-07-09", "Fête du sacrifice (estimé)"),
            ("2022-07-10", "Congé de fête du sacrifice (estimé)"),
            ("2022-07-30", "Nouvel an musulman (estimé)"),
            ("2022-08-08", "Achoura (estimé)"),
            ("2022-10-08", "Anniversaire du prophète (estimé)"),
            ("2022-11-01", "Fête de la Révolution"),
        )
