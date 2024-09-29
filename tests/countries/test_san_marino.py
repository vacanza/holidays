#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.san_marino import SanMarino, SM, SMR
from tests.common import CommonCountryTests


class TestSanMarino(CommonCountryTests, TestCase):
    def setUp(self):
        self.holidays = SanMarino()

    def test_country_aliases(self):
        self.assertAliases(SanMarino, SM, SMR)

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-02-05", "Feast of Saint Agatha"),
            ("2022-03-25", "Anniversary of the Arengo"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labour Day"),
            ("2022-06-16", "Corpus Cristi"),
            ("2022-07-28", "Liberation from Fascism Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-09-03", "Foundation Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-02", "Commemoration of the Dead"),
            ("2022-12-08", "Immaculate Conception Day"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Saint Stephen's Day"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_2023(self):
        self.assertHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-06", "Epiphany"),
            ("2023-02-05", "Feast of Saint Agatha"),
            ("2023-03-25", "Anniversary of the Arengo"),
            ("2023-04-09", "Easter Sunday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-01", "Labour Day"),
            ("2023-06-08", "Corpus Cristi"),
            ("2023-07-28", "Liberation from Fascism Day"),
            ("2023-08-15", "Assumption Day"),
            ("2023-09-03", "Foundation Day"),
            ("2023-11-01", "All Saints' Day"),
            ("2023-11-02", "Commemoration of the Dead"),
            ("2023-12-08", "Immaculate Conception Day"),
            ("2023-12-24", "Christmas Eve"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Saint Stephen's Day"),
            ("2023-12-31", "New Year's Eve"),
        )
