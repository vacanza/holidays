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
        super().setUpClass(BeHolidays)

    def test_nl(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nieuwjaar"),
            ("2022-04-15", "Goede Vrijdag"),
            ("2022-04-17", "Pasen"),
            ("2022-04-18", "Paasmaandag"),
            ("2022-05-01", "Dag van de Arbeid"),
            ("2022-05-26", "O. L. H. Hemelvaart"),
            ("2022-05-27", "Vrijdag na O. L. H. Hemelvaart"),
            ("2022-06-05", "Pinksteren"),
            ("2022-06-06", "Pinkstermaandag"),
            ("2022-07-21", "Nationale feestdag"),
            ("2022-08-15", "O. L. V. Hemelvaart"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-11-11", "Wapenstilstand"),
            ("2022-12-25", "Kerstmis"),
            ("2022-12-26", "Banksluitingsdag"),
        )
