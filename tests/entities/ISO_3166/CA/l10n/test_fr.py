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

from holidays.entities.ISO_3166.CA import CaHolidays
from tests.common import CommonCountryTests


class TestCaHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CaHolidays, language="fr")

    def test_fr(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Jour de l'an"),
            ("2022-01-03", "Jour de l'an (Observé)"),
            ("2022-04-15", "Vendredi saint"),
            ("2022-05-23", "Fête de la Reine"),
            ("2022-07-01", "Fête du Canada"),
            ("2022-09-05", "Fête du Travail"),
            ("2022-09-30", "Journée nationale de la vérité et de la réconciliation"),
            ("2022-10-10", "Action de grâce"),
            ("2022-11-11", "Jour du Souvenir"),
            ("2022-12-25", "Jour de Noël"),
            ("2022-12-26", "Boxing Day; Jour de Noël (Observé)"),
            ("2022-12-27", "Jour de Noël (Observé)"),
        )
