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

from holidays.countries.serbia import Serbia, RS, SRB
from tests.common import CommonCountryTests


class TestSerbia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Serbia)

    def test_country_aliases(self):
        self.assertAliases(Serbia, RS, SRB)

    def test_no_holidays(self):
        self.assertNoHolidays(Serbia(years=RS.start_year - 1))

    def test_new_years_day(self):
        name = "Нова година"
        self.assertHolidayName(
            name,
            (f"{year}-01-01" for year in self.full_range),
            (f"{year}-01-02" for year in self.full_range),
        )
        obs_dt = (
            "2017-01-03",
            "2022-01-03",
            "2023-01-03",
        )
        self.assertHolidayName(f"{name} (слободан дан)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_orthodox_christmas(self):
        self.assertHolidayName("Божић", (f"{year}-01-07" for year in self.full_range))

    def test_statehood_day(self):
        name = "Дан државности Србије"
        self.assertHolidayName(
            name,
            (f"{year}-02-15" for year in self.full_range),
            (f"{year}-02-16" for year in self.full_range),
        )
        obs_dt = (
            "2015-02-17",
            "2020-02-17",
            "2025-02-17",
        )
        self.assertHolidayName(f"{name} (слободан дан)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_orthodox_good_friday(self):
        name = "Велики петак"
        self.assertHolidayName(
            name,
            "2020-04-17",
            "2021-04-30",
            "2022-04-22",
            "2023-04-14",
            "2024-05-03",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_orthodox_holy_saturday(self):
        name = "Велика субота"
        self.assertHolidayName(
            name,
            "2020-04-18",
            "2021-05-01",
            "2022-04-23",
            "2023-04-15",
            "2024-05-04",
            "2025-04-19",
        )
        self.assertHolidayName(name, self.full_range)

    def test_orthodox_easter_sunday(self):
        name = "Васкрс"
        self.assertHolidayName(
            name,
            "2020-04-19",
            "2021-05-02",
            "2022-04-24",
            "2023-04-16",
            "2024-05-05",
            "2025-04-20",
        )
        self.assertHolidayName(name, self.full_range)

    def test_orthodox_easter_monday(self):
        name = "Други дан Васкрса"
        self.assertHolidayName(
            name,
            "2020-04-20",
            "2021-05-03",
            "2022-04-25",
            "2023-04-17",
            "2024-05-06",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        name = "Празник рада"
        self.assertHolidayName(
            name,
            (f"{year}-05-01" for year in self.full_range),
            (f"{year}-05-02" for year in self.full_range),
        )
        obs_dt = (
            "2016-05-03",
            "2021-05-04",
            "2022-05-03",
        )
        self.assertHolidayName(f"{name} (слободан дан)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_armistice_day(self):
        name = "Дан примирја у Првом светском рату"
        self.assertHolidayName(name, (f"{year}-11-11" for year in self.full_range))
        obs_dt = (
            "2012-11-12",
            "2018-11-12",
        )
        self.assertHolidayName(f"{name} (слободан дан)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Нова година"),
            ("2022-01-02", "Нова година"),
            ("2022-01-03", "Нова година (слободан дан)"),
            ("2022-01-07", "Божић"),
            ("2022-02-15", "Дан државности Србије"),
            ("2022-02-16", "Дан државности Србије"),
            ("2022-04-22", "Велики петак"),
            ("2022-04-23", "Велика субота"),
            ("2022-04-24", "Васкрс"),
            ("2022-04-25", "Други дан Васкрса"),
            ("2022-05-01", "Празник рада"),
            ("2022-05-02", "Празник рада"),
            ("2022-05-03", "Празник рада (слободан дан)"),
            ("2022-11-11", "Дан примирја у Првом светском рату"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-07", "Orthodox Christmas Day"),
            ("2022-02-15", "Statehood Day"),
            ("2022-02-16", "Statehood Day"),
            ("2022-04-22", "Good Friday"),
            ("2022-04-23", "Holy Saturday"),
            ("2022-04-24", "Easter Sunday"),
            ("2022-04-25", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Labor Day"),
            ("2022-05-03", "Labor Day (observed)"),
            ("2022-11-11", "Armistice Day"),
        )
