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

from holidays.countries.zambia import Zambia
from tests.common import CommonCountryTests


class TestZambia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Zambia)

    def test_special_holidays(self):
        self.assertHoliday(
            "2014-11-11",
            "2014-12-26",
            "2015-01-02",
            "2015-01-20",
            "2016-09-13",
            "2018-03-09",
            "2018-07-26",
            "2019-10-25",
            "2021-07-02",
            "2021-07-07",
            "2021-08-13",
            "2021-08-24",
            "2022-03-18",
        )

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_international_womens_day(self):
        name = "International Women's Day"
        self.assertHolidayName(name, (f"{year}-03-08" for year in range(2008, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2008))
        obs_dts = (
            "2009-03-09",
            "2015-03-09",
            "2020-03-09",
            "2026-03-09",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_youth_day(self):
        name = "Youth Day"
        self.assertHolidayName(
            name,
            "1984-03-17",
            "1985-03-16",
            "1986-03-15",
            "1987-03-21",
        )
        self.assertHolidayName(name, (f"{year}-03-12" for year in range(1988, self.end_year)))
        obs_dts = (
            "2000-03-13",
            "2006-03-13",
            "2017-03-13",
            "2023-03-13",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
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

    def test_holy_saturday(self):
        name = "Holy Saturday"
        self.assertHolidayName(
            name,
            "2020-04-11",
            "2021-04-03",
            "2022-04-16",
            "2023-04-08",
            "2024-03-30",
            "2025-04-19",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_sunday(self):
        name = "Easter Sunday"
        self.assertHolidayName(
            name,
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_kenneth_kaunda_day(self):
        name = "Kenneth Kaunda Day"
        self.assertHolidayName(name, (f"{year}-04-28" for year in range(2022, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2022))
        obs_dts = (
            "2024-04-29",
            "2030-04-29",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_labor_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        obs_dts = (
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_africa_freedom_day(self):
        name = "Africa Freedom Day"
        self.assertHolidayName(name, (f"{year}-05-25" for year in self.full_range))
        obs_dts = (
            "2003-05-26",
            "2008-05-26",
            "2014-05-26",
            "2025-05-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_heroes_day(self):
        name = "Heroes' Day"
        self.assertHolidayName(
            name,
            "2020-07-06",
            "2021-07-05",
            "2022-07-04",
            "2023-07-03",
            "2024-07-01",
            "2025-07-07",
        )
        self.assertHolidayName(name, self.full_range)

    def test_unity_day(self):
        name = "Unity Day"
        self.assertHolidayName(
            name,
            "2020-07-07",
            "2021-07-06",
            "2022-07-05",
            "2023-07-04",
            "2024-07-02",
            "2025-07-08",
        )
        self.assertHolidayName(name, self.full_range)

    def test_farmers_day(self):
        name = "Farmers' Day"
        self.assertHolidayName(
            name,
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
            "2025-08-04",
        )
        self.assertHolidayName(name, self.full_range)

    def test_general_election_day(self):
        name = "General Election Day"
        self.assertHolidayName(
            name,
            "2016-08-11",
            "2021-08-12",
            "2026-08-13",
        )
        self.assertHolidayName(
            name, (year for year in range(2016, self.end_year) if year % 5 == 1)
        )
        self.assertNoHolidayName(
            name,
            range(self.start_year, 2016),
            (year for year in range(2016, self.end_year) if year % 5 != 1),
        )

    def test_national_prayer_day(self):
        name = "National Prayer Day"
        self.assertHolidayName(name, (f"{year}-10-18" for year in range(2016, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2016))
        obs_dts = (
            "2020-10-19",
            "2026-10-19",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-10-24" for year in self.full_range))
        obs_dts = (
            "1999-10-25",
            "2004-10-25",
            "2010-10-25",
            "2021-10-25",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2005-12-26",
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "New Year's Day"),
            ("2022-03-08", "International Women's Day"),
            ("2022-03-12", "Youth Day"),
            ("2022-03-18", "State Funeral of Rupiah Banda"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-16", "Holy Saturday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-28", "Kenneth Kaunda Day"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Labour Day (observed)"),
            ("2022-05-25", "Africa Freedom Day"),
            ("2022-07-04", "Heroes' Day"),
            ("2022-07-05", "Unity Day"),
            ("2022-08-01", "Farmers' Day"),
            ("2022-10-18", "National Prayer Day"),
            ("2022-10-24", "Independence Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )
