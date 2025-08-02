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

from holidays.countries.liberia import Liberia, LR, LBR
from tests.common import CommonCountryTests


class TestLiberia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1957, 2050)
        super().setUpClass(Liberia, years=years, years_non_observed=years)

    def test_country_aliases(self):
        self.assertAliases(Liberia, LR, LBR)

    def test_no_holidays(self):
        self.assertNoHolidays(Liberia(years=1956))

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1957, 2050)))

    def test_inauguration_day(self):
        years_after_election = {1960, 1964, 1968, 1972, 1976, 1986, 1998, 2006, 2012, 2018, 2024}
        years_not_after_election = {
            year for year in range(1957, 2050) if year not in years_after_election
        }
        name = "Inauguration Day"
        self.assertHolidayName(
            name,
            "2006-01-02",
            "2012-01-02",
            "2018-01-01",
            "2024-01-01",
        )
        self.assertHolidayName(name, years_after_election)
        self.assertNoHolidayName(name, years_not_after_election)

    def test_armed_forces_day(self):
        self.assertHolidayName("Armed Forces Day", (f"{year}-02-11" for year in range(1957, 2050)))

    def test_decoration_day(self):
        name = "Decoration Day"
        self.assertHolidayName(
            name, "2021-03-10", "2022-03-09", "2023-03-08", "2024-03-13", "2025-03-12"
        )
        self.assertHolidayName(name, range(1957, 2050))

    def test_jj_roberts_memorial_day(self):
        self.assertHolidayName(
            "J. J. Roberts Memorial Birthday",
            (f"{year}-03-15" for year in range(1957, 2050)),
        )

    def test_fasting_and_prayer_day(self):
        name = "Fasting and Prayer Day"
        self.assertHolidayName(
            name, "2020-04-10", "2021-04-09", "2022-04-08", "2023-04-14", "2024-04-12"
        )
        self.assertHolidayName(name, range(1957, 2050))

    def test_national_unification_and_integration_day(self):
        self.assertHolidayName(
            "National Unification and Integration Day",
            (f"{year}-05-14" for year in range(1957, 2050)),
        )

    def test_independence_day(self):
        self.assertHolidayName("Independence Day", (f"{year}-07-26" for year in range(1957, 2050)))

    def test_national_flag_day(self):
        self.assertHolidayName(
            "National Flag Day", (f"{year}-08-24" for year in range(1957, 2050))
        )

    def test_thanksgiving_day(self):
        name = "Thanksgiving Day"
        self.assertHolidayName(
            name, "2020-11-05", "2021-11-04", "2022-11-03", "2023-11-02", "2024-11-07"
        )
        self.assertHolidayName(name, range(1957, 2050))

    def test_tubman_administration_goodwill_day(self):
        self.assertHolidayName(
            "Tubman Administration Goodwill Day", (f"{year}-11-29" for year in range(1957, 2050))
        )

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(1957, 2050)))

    def test_2025(self):
        self.assertHolidays(
            Liberia(years=2025),
            ("2025-01-01", "New Year's Day"),
            ("2025-02-11", "Armed Forces Day"),
            ("2025-03-12", "Decoration Day"),
            ("2025-03-15", "J. J. Roberts Memorial Birthday"),
            ("2025-04-11", "Fasting and Prayer Day"),
            ("2025-05-14", "National Unification and Integration Day"),
            ("2025-07-26", "Independence Day"),
            ("2025-08-24", "National Flag Day"),
            ("2025-11-06", "Thanksgiving Day"),
            ("2025-11-29", "Tubman Administration Goodwill Day"),
            ("2025-12-25", "Christmas Day"),
        )
