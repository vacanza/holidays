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

from holidays.countries.marshall_islands import MarshallIslands
from tests.common import CommonCountryTests


class TestMarshallIslands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MarshallIslands)

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2010-12-31",
            "2012-01-02",
            "2017-01-02",
            "2021-12-31",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} Holiday", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_nuclear_victims_remembrance_day(self):
        name_1996 = "Nuclear Victims Remembrance Day"
        name_2003 = "Memorial Day and Nuclear Survivors Remembrance Day"
        self.assertHolidayName(
            name_1996,
            (f"{year}-03-01" for year in (*range(1996, 2004), *range(2006, self.end_year))),
        )
        self.assertHolidayName(name_2003, (f"{year}-03-01" for year in range(2004, 2006)))
        self.assertNoHolidayName(name_1996, range(self.start_year, 1996), range(2004, 2006))
        self.assertNoHolidayName(
            name_2003, range(self.start_year, 2004), range(2006, self.end_year)
        )
        obs_dts = (
            "2014-02-28",
            "2015-03-02",
            "2020-03-02",
            "2025-02-28",
            "2026-03-02",
        )
        self.assertHolidayName(f"{name_1996} Holiday", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(2006, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2006))
        obs_dts = (
            "2010-04-30",
            "2011-05-02",
            "2016-05-02",
            "2021-04-30",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} Holiday", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_fishermans_day(self):
        name = "Fisherman's Day"
        self.assertHolidayName(
            name,
            "2020-07-03",
            "2021-07-02",
            "2022-07-01",
            "2023-07-07",
            "2024-07-05",
            "2025-07-04",
        )
        self.assertHolidayName(name, range(1996, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1996))

    def test_dri_jerbal_day(self):
        name = "Dri-jerbal Day"
        self.assertHolidayName(
            name,
            "2020-09-04",
            "2021-09-03",
            "2022-09-02",
            "2023-09-01",
            "2024-09-06",
            "2025-09-05",
        )
        self.assertHolidayName(name, range(1996, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1996))

    def test_manit_day(self):
        name = "Manit Day"
        self.assertHolidayName(
            name,
            "2020-09-25",
            "2021-09-24",
            "2022-09-30",
            "2023-09-29",
            "2024-09-27",
            "2025-09-26",
        )
        self.assertHolidayName(name, range(1996, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1996))

    def test_presidents_day(self):
        name = "President's Day"
        self.assertHolidayName(name, (f"{year}-11-17" for year in self.full_range))
        obs_dts = (
            "2012-11-16",
            "2013-11-18",
            "2018-11-16",
            "2019-11-18",
            "2024-11-18",
        )
        self.assertHolidayName(f"{name} Holiday", obs_dts)

    def test_general_election_day(self):
        name = "General Election Day"
        self.assertHolidayName(
            name,
            "2015-11-16",
            "2019-11-18",
            "2023-11-20",
        )
        self.assertHolidayName(
            name, (year for year in range(2015, self.end_year) if year % 4 == 3)
        )
        self.assertNoHolidayName(
            name,
            range(self.start_year, 2015),
            (year for year in range(2015, self.end_year) if year % 4 != 3),
        )

    def test_gospel_day(self):
        name = "Gospel Day"
        self.assertHolidayName(
            name,
            "2020-12-04",
            "2021-12-03",
            "2022-12-02",
            "2023-12-01",
            "2024-12-06",
            "2025-12-05",
        )
        self.assertHolidayName(name, self.full_range)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2010-12-24",
            "2011-12-26",
            "2016-12-26",
            "2021-12-24",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} Holiday", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "New Year's Day"),
            ("2024-03-01", "Nuclear Victims Remembrance Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-05-01", "Constitution Day"),
            ("2024-07-05", "Fisherman's Day"),
            ("2024-09-06", "Dri-jerbal Day"),
            ("2024-09-27", "Manit Day"),
            ("2024-11-17", "President's Day"),
            ("2024-11-18", "President's Day Holiday"),
            ("2024-12-06", "Gospel Day"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "New Year's Day"),
            ("2025-02-28", "Nuclear Victims Remembrance Day Holiday"),
            ("2025-03-01", "Nuclear Victims Remembrance Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-05-01", "Constitution Day"),
            ("2025-07-04", "Fisherman's Day"),
            ("2025-09-05", "Dri-jerbal Day"),
            ("2025-09-26", "Manit Day"),
            ("2025-11-17", "President's Day"),
            ("2025-12-05", "Gospel Day"),
            ("2025-12-25", "Christmas Day"),
        )
