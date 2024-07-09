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

from holidays.entities.ISO_3166.MC import McHolidays
from tests.common import CommonCountryTests


class TestMcHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(McHolidays)

    def test_fr(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Le jour de l'An"),
            ("2022-01-27", "La Sainte Dévote"),
            ("2022-04-18", "Le lundi de Pâques"),
            ("2022-05-01", "Fête de la Travaille"),
            ("2022-05-02", "Fête de la Travaille (observé)"),
            ("2022-05-26", "L'Ascension"),
            ("2022-06-06", "Le lundi de Pentecôte"),
            ("2022-06-16", "La Fête Dieu"),
            ("2022-08-15", "L'Assomption de Marie"),
            ("2022-11-01", "La Toussaint"),
            ("2022-11-19", "La Fête du Prince"),
            ("2022-12-08", "L'Immaculée Conception"),
            ("2022-12-25", "Noël"),
            ("2022-12-26", "Noël (observé)"),
        )
