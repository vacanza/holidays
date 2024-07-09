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

from holidays.constants import BANK
from holidays.entities.ISO_3166.BE import BeHolidays
from tests.common import CommonCountryTests


class TestBeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BeHolidays)

    def test_2020(self):
        self.assertHolidays(
            ("2020-01-01", "Nieuwjaar"),
            ("2020-04-12", "Pasen"),
            ("2020-04-13", "Paasmaandag"),
            ("2020-05-01", "Dag van de Arbeid"),
            ("2020-05-21", "O. L. H. Hemelvaart"),
            ("2020-05-31", "Pinksteren"),
            ("2020-06-01", "Pinkstermaandag"),
            ("2020-07-21", "Nationale feestdag"),
            ("2020-08-15", "O. L. V. Hemelvaart"),
            ("2020-11-01", "Allerheiligen"),
            ("2020-11-11", "Wapenstilstand"),
            ("2020-12-25", "Kerstmis"),
        )

    def test_2021(self):
        self.assertHolidays(
            ("2021-01-01", "Nieuwjaar"),
            ("2021-04-04", "Pasen"),
            ("2021-04-05", "Paasmaandag"),
            ("2021-05-01", "Dag van de Arbeid"),
            ("2021-05-13", "O. L. H. Hemelvaart"),
            ("2021-05-23", "Pinksteren"),
            ("2021-05-24", "Pinkstermaandag"),
            ("2021-07-21", "Nationale feestdag"),
            ("2021-08-15", "O. L. V. Hemelvaart"),
            ("2021-11-01", "Allerheiligen"),
            ("2021-11-11", "Wapenstilstand"),
            ("2021-12-25", "Kerstmis"),
        )

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "Nieuwjaar"),
            ("2022-04-17", "Pasen"),
            ("2022-04-18", "Paasmaandag"),
            ("2022-05-01", "Dag van de Arbeid"),
            ("2022-05-26", "O. L. H. Hemelvaart"),
            ("2022-06-05", "Pinksteren"),
            ("2022-06-06", "Pinkstermaandag"),
            ("2022-07-21", "Nationale feestdag"),
            ("2022-08-15", "O. L. V. Hemelvaart"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-11-11", "Wapenstilstand"),
            ("2022-12-25", "Kerstmis"),
        )

    def test_bank_2022(self):
        self.assertHolidays(
            BeHolidays(categories=BANK, years=2022),
            ("2022-04-15", "Goede Vrijdag"),
            ("2022-05-27", "Vrijdag na O. L. H. Hemelvaart"),
            ("2022-12-26", "Banksluitingsdag"),
        )
