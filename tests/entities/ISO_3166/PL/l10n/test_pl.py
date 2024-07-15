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

from holidays.entities.ISO_3166.PL import PlHolidays
from tests.common import CommonCountryTests


class TestPlHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PlHolidays)

    def test_pl_2018(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "Nowy Rok"),
            ("2018-01-06", "Święto Trzech Króli"),
            ("2018-04-01", "Niedziela Wielkanocna"),
            ("2018-04-02", "Poniedziałek Wielkanocny"),
            ("2018-05-01", "Święto Państwowe"),
            ("2018-05-03", "Święto Narodowe Trzeciego Maja"),
            ("2018-05-20", "Zielone Świątki"),
            ("2018-05-31", "Dzień Bożego Ciała"),
            ("2018-08-15", "Wniebowzięcie Najświętszej Marii Panny"),
            ("2018-11-01", "Uroczystość Wszystkich Świętych"),
            ("2018-11-11", "Narodowe Święto Niepodległości"),
            ("2018-11-12", "Narodowe Święto Niepodległości - 100-lecie"),
            ("2018-12-25", "Boże Narodzenie (pierwszy dzień)"),
            ("2018-12-26", "Boże Narodzenie (drugi dzień)"),
        )

    def test_pl_2022(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Nowy Rok"),
            ("2022-01-06", "Święto Trzech Króli"),
            ("2022-04-17", "Niedziela Wielkanocna"),
            ("2022-04-18", "Poniedziałek Wielkanocny"),
            ("2022-05-01", "Święto Państwowe"),
            ("2022-05-03", "Święto Narodowe Trzeciego Maja"),
            ("2022-06-05", "Zielone Świątki"),
            ("2022-06-16", "Dzień Bożego Ciała"),
            ("2022-08-15", "Wniebowzięcie Najświętszej Marii Panny"),
            ("2022-11-01", "Uroczystość Wszystkich Świętych"),
            ("2022-11-11", "Narodowe Święto Niepodległości"),
            ("2022-12-25", "Boże Narodzenie (pierwszy dzień)"),
            ("2022-12-26", "Boże Narodzenie (drugi dzień)"),
        )
