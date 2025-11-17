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

from calendar import isleap
from unittest import TestCase

from holidays.countries.antarctica import Antarctica
from tests.common import CommonCountryTests


class TestAntarctica(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Antarctica)

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in self.full_range))

    def test_midwinter_day(self):
        self.assertHolidayName(
            "Midwinter Day",
            (f"{year}-06-20" for year in self.full_range if isleap(year)),
            (f"{year}-06-21" for year in self.full_range if not isleap(year)),
        )

    def test_antarctica_day(self):
        name = "Antarctica Day"
        self.assertHolidayName(name, (f"{year}-12-01" for year in range(2010, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2010))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in self.full_range))

    def test_2025(self):
        self.assertHolidays(
            Antarctica(years=2025),
            ("2025-01-01", "New Year's Day"),
            ("2025-06-21", "Midwinter Day"),
            ("2025-12-01", "Antarctica Day"),
            ("2025-12-25", "Christmas Day"),
        )
