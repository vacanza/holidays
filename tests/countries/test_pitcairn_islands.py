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

from holidays.countries.pitcairn_islands import PitcairnIslands, PN, PCN
from tests.common import CommonCountryTests


class TestPitcairnIslands(CommonCountryTests, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PitcairnIslands, years=range(2000, 2050))

    def test_country_aliases(self):
        self.assertAliases(PitcairnIslands, PN, PCN)

    def test_2024(self):
        self.assertHolidays(
            PitcairnIslands(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-01-23", "Bounty Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-06-08", "King's Birthday"),  # 2nd Saturday in June
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_2025(self):
        """Test holidays for another year to verify consistency."""
        self.assertHolidays(
            PitcairnIslands(years=2025),
            ("2025-01-01", "New Year's Day"),
            ("2025-01-23", "Bounty Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-06-14", "King's Birthday"),  # 2nd Saturday in June
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_kings_birthday(self):
        """Test King's Birthday holiday."""
        # Test specific known dates
        self.assertHolidayName("King's Birthday", "2024-06-08", "2025-06-14")
        # Test Queen's Birthday for earlier years
        self.assertHolidayName("Queen's Birthday", "2022-06-11")

    def test_bounty_day(self):
        """Test Bounty Day holiday."""
        self.assertHolidayName("Bounty Day", (f"{year}-01-23" for year in range(2000, 2050)))

    def test_good_friday(self):
        """Test Good Friday holiday."""
        self.assertHolidayName("Good Friday", "2024-03-29", "2025-04-18")

    def test_easter_monday(self):
        """Test Easter Monday holiday."""
        self.assertHolidayName("Easter Monday", "2024-04-01", "2025-04-21")

    def test_monarch_birthday_naming(self):
        """Test that monarch's birthday uses correct title based on year."""
        # Test Queen's Birthday (before 2023) and King's Birthday (from 2023)
        self.assertHolidayName("Queen's Birthday", "2022-06-11")
        self.assertHolidayName("King's Birthday", "2023-06-10")
