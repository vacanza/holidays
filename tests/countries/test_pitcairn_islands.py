#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date

from holidays.countries.pitcairn_islands import PitcairnIslands, PN, PCN
from tests.common import CommonCountryTests


class TestPitcairnIslands(CommonCountryTests, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            PitcairnIslands, years=range(2000, 2050), years_non_observed=range(2000, 2050)
        )

    def test_country_aliases(self):
        self.assertAliases(PitcairnIslands, PN, PCN)

    def test_no_holidays_before_2000(self):
        self.assertNoHolidays(PitcairnIslands(years=1999))

    def test_2024(self):
        self.assertHolidays(
            PitcairnIslands(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-01-23", "Bounty Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-06-08", "King's Birthday"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_random_non_holiday(self):
        self.assertNoHoliday(PitcairnIslands(years=2024), date(2024, 2, 2))
