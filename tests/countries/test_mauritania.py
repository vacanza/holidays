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

from holidays.countries.mauritania import Mauritania, MR, MRT
from tests.common import CommonCountryTests


class TestMauritania(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Mauritania, years=range(1950, 2050))

    def test_country_aliases(self):
        self.assertAliases(Mauritania, MR, MRT)

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1950, 2050)))

    def test_labor_day(self):
        self.assertHolidayName("Labor Day", (f"{year}-05-01" for year in range(1950, 2050)))

    def test_africa_day(self):
        self.assertHolidayName("Africa Day", (f"{year}-05-25" for year in range(1950, 2050)))

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-11-28" for year in range(1960, 2050)))
        self.assertNoHolidayName(name, range(1950, 1960))

    def test_2023(self):
        self.assertHolidays(
            Mauritania(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-04-21", "Eid al-Fitr (estimated)"),
            ("2023-04-22", "Eid al-Fitr (estimated)"),
            ("2023-05-01", "Labor Day"),
            ("2023-05-25", "Africa Day"),
            ("2023-06-28", "Eid al-Adha (estimated)"),
            ("2023-06-29", "Eid al-Adha (estimated)"),
            ("2023-07-19", "Islamic New Year (estimated)"),
            ("2023-09-27", "Mawlid al-Nabi (estimated)"),
            ("2023-11-28", "Independence Day"),
        )

    def test_2024(self):
        self.assertHolidays(
            Mauritania(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-04-10", "Eid al-Fitr (estimated)"),
            ("2024-04-11", "Eid al-Fitr (estimated)"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-25", "Africa Day"),
            ("2024-06-16", "Eid al-Adha (estimated)"),
            ("2024-06-17", "Eid al-Adha (estimated)"),
            ("2024-07-07", "Islamic New Year (estimated)"),
            ("2024-09-15", "Mawlid al-Nabi (estimated)"),
            ("2024-11-28", "Independence Day"),
        )
