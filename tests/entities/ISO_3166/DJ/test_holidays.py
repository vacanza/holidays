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

    def test_no_holidays(self):
        self.assertNoHolidays(DjHolidays(years=1977))

    def test_2019(self):
        self.assertHolidays(
            ("2019-01-01", "Nouvel an"),
            ("2019-04-03", "Al Isra et Al Mirague (estimé)"),
            ("2019-05-01", "Fête du travail"),
            ("2019-06-04", "Eid al-Fitr (estimé)"),
            ("2019-06-05", "Eid al-Fitr deuxième jour (estimé)"),
            ("2019-06-27", "Fête de l'indépendance"),
            ("2019-06-28", "Fête de l'indépendance deuxième jour"),
            ("2019-08-10", "Arafat (estimé)"),
            ("2019-08-11", "Eid al-Adha (estimé)"),
            ("2019-08-12", "Eid al-Adha deuxième jour (estimé)"),
            ("2019-08-31", "Nouvel an musulman (estimé)"),
            ("2019-11-09", "Anniversaire du prophète Muhammad (estimé)"),
            ("2019-12-25", "Noël"),
        )
