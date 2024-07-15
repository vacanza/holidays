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

from holidays.entities.ISO_3166.DJ import DjHolidays
from tests.common import CommonCountryTests


class TestDjHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(DjHolidays)

    def test_fr(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nouvel an"),
            ("2022-02-28", "Al Isra et Al Mirague (estimé)"),
            ("2022-05-01", "Fête du travail"),
            ("2022-05-02", "Eid al-Fitr (estimé)"),
            ("2022-05-03", "Eid al-Fitr deuxième jour (estimé)"),
            ("2022-06-27", "Fête de l'indépendance"),
            ("2022-06-28", "Fête de l'indépendance deuxième jour"),
            ("2022-07-08", "Arafat (estimé)"),
            ("2022-07-09", "Eid al-Adha (estimé)"),
            ("2022-07-10", "Eid al-Adha deuxième jour (estimé)"),
            ("2022-07-30", "Nouvel an musulman (estimé)"),
            ("2022-10-08", "Anniversaire du prophète Muhammad (estimé)"),
            ("2022-12-25", "Noël"),
        )
