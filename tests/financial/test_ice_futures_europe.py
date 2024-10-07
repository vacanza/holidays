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

from holidays.financial.ice_futures_europe import ICEFuturesEurope, IFEU
from tests.common import CommonFinancialTests


class TestICEFuturesEurope(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ICEFuturesEurope, years=range(2000, 2100))

    def test_market_aliases(self):
        self.assertAliases(ICEFuturesEurope, IFEU)

    def test_no_holidays(self):
        self.assertNoHolidays(ICEFuturesEurope(years=2013))

    def test_2021(self):
        self.assertHolidays(
            ICEFuturesEurope(years=2021),
            ("2021-01-01", "New Year's Day"),
            ("2021-04-02", "Good Friday"),
        )

    def test_2022(self):
        self.assertHolidays(
            ICEFuturesEurope(years=2022),
            ("2022-04-15", "Good Friday"),
            ("2022-12-26", "Christmas Day"),
        )

    def test_2023(self):
        self.assertHolidays(
            ICEFuturesEurope(years=2023),
            ("2023-01-02", "New Year's Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_2024(self):
        self.assertHolidays(
            ICEFuturesEurope(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-12-25", "Christmas Day"),
        )
