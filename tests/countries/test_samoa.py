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

from holidays.countries.samoa import Samoa, WS, WSM
from tests.common import CommonCountryTests


class TestSamoa(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Samoa, years=range(1950, 2050))

    def test_country_aliases(self):
        self.assertAliases(Samoa, WS, WSM)

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1950, 2050)))

    def test_new_years_second_day(self):
        self.assertHolidayName(
            "The Day After New Year's Day", (f"{year}-01-02" for year in range(1950, 2050))
        )

    def test_independence_day(self):
        self.assertHolidayName("Independence Day", (f"{year}-06-01" for year in range(1950, 2050)))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(1950, 2050)))

    def test_boxing_day(self):
        self.assertHolidayName("Boxing Day", (f"{year}-12-26" for year in range(1950, 2050)))

    def test_2023(self):
        self.assertHolidays(
            Samoa(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "The Day After New Year's Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-08", "Day After Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-15", "Mother's Day"),
            ("2023-06-01", "Independence Day"),
            ("2023-08-14", "Father's Day"),
            ("2023-10-09", "White Sunday (Lotu a Tamaiti)"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_2024(self):
        self.assertHolidays(
            Samoa(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-01-02", "The Day After New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "Day After Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-13", "Mother's Day"),
            ("2024-06-01", "Independence Day"),
            ("2024-08-12", "Father's Day"),
            ("2024-10-14", "White Sunday (Lotu a Tamaiti)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )
