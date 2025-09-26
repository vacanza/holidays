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


from unittest import TestCase

from holidays.countries.antarctica import Antarctica, AQ, ATA
from tests.common import CommonCountryTests


class TestAntarctica(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Antarctica)

    def test_country_aliases(self):
        self.assertAliases(Antarctica, AQ, ATA)

    def test_fixed_holidays(self):
        # Standard fixed holidays
        self.assertHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-06-21", "Midwinter Day"),
            ("2025-12-01", "Antarctica Day"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_midwinter_day_leap_years(self):
        # Midwinter Day shifts: leap years → June 20
        for year in [2000, 2012, 2016, 2020, 2024, 2028, 2032]:
            self.assertHolidayName("Midwinter Day", f"{year}-06-20")
            self.assertNoHoliday(f"{year}-06-21")

    def test_midwinter_day_non_leap_years(self):
        # Non-leap years → June 21
        for year in [2013, 2015, 2017, 2021, 2025, 2029, 2100]:
            self.assertHolidayName("Midwinter Day", f"{year}-06-21")
            self.assertNoHoliday(f"{year}-06-20")

    def test_all_holidays(self):
        # Ensure all holidays appear in the calendar
        holidays = Antarctica(years=(2025,))
        self.assertIn("2025-01-01", holidays)
        self.assertIn("2025-06-21", holidays)
        self.assertIn("2025-12-01", holidays)
        self.assertIn("2025-12-25", holidays)
        self.assertEqual(len(holidays), 4)

    def test_l10n_default(self):
        # Localization test (default language)
        self.assertLocalizedHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-06-21", "Midwinter Day"),
            ("2025-12-01", "Antarctica Day"),
            ("2025-12-25", "Christmas Day"),
        )
