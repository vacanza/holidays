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

from holidays.countries.south_africa import SouthAfrica
from tests.common import CommonCountryTests


class TestSouthAfrica(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SouthAfrica, years_non_observed=range(1995, 2050))

    def test_special_holidays(self):
        self.assertHoliday(
            "1999-06-02",
            "1999-12-31",
            "2000-01-02",
            "2004-04-14",
            "2006-03-01",
            "2008-05-02",
            "2009-04-22",
            "2011-05-18",
            "2011-12-27",
            "2014-05-07",
            "2016-08-03",
            "2019-05-08",
            "2021-11-01",
            "2022-12-27",
            "2023-12-15",
            # presidential
            "2008-05-02",
            "2011-12-27",
            "2016-12-27",
            # elections
            "1999-06-02",  # Election Day 1999
            "2004-04-14",  # Election Day 2004
            "2006-03-01",  # Local Election
            "2009-04-22",  # Election Day 2008
            "2011-05-18",  # Election Day 2011
            "2014-05-07",  # Election Day 2014
            "2016-08-03",  # Election Day 2016
            "2019-05-08",  # Election Day 2019
            "2021-11-01",  # Election Day 2019
            "2024-05-29",  # Election Day 2024
        )
        obs_dts = (
            # special holiday
            "2000-01-03",
        )
        self.assertHoliday(obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

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

    def test_human_rights_day(self):
        name = "Human Rights Day"
        self.assertHolidayName(name, (f"{year}-03-21" for year in range(1995, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1995))
        obs_dts = (
            "2010-03-22",
            "2021-03-22",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_founders_day(self):
        name_1952 = "Van Riebeeck's Day"
        name_1980 = "Founder's Day"
        self.assertHolidayName(name_1952, (f"{year}-04-06" for year in range(1952, 1974)))
        self.assertHolidayName(name_1980, (f"{year}-04-06" for year in range(1980, 1995)))
        self.assertNoHolidayName(
            name_1952, range(self.start_year, 1952), range(1975, self.end_year)
        )
        self.assertNoHolidayName(
            name_1980, range(self.start_year, 1980), range(1995, self.end_year)
        )

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "1940-03-25",
            "1960-04-18",
            "1970-03-30",
            "1978-03-27",
            "1979-04-16",
        )
        self.assertHolidayName(name, range(self.start_year, 1980))
        self.assertNoHolidayName(name, range(1980, self.end_year))

    def test_family_day(self):
        name = "Family Day"
        self.assertHolidayName(
            name,
            (f"{year}-07-10" for year in range(1961, 1974)),
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
        )
        self.assertHolidayName(name, range(1980, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1961), range(1974, 1980))

    def test_freedom_day(self):
        name = "Freedom Day"
        self.assertHolidayName(name, (f"{year}-04-27" for year in range(1995, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1995))
        obs_dts = (
            "2008-04-28",
            "2014-04-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_workers_day(self):
        name = "Workers' Day"
        self.assertHolidayName(
            name,
            (f"{year}-05-01" for year in range(1995, self.end_year)),
            "1987-05-01",
            "1988-05-06",
            "1989-05-05",
        )
        self.assertNoHolidayName(name, range(self.start_year, 1987), range(1990, 1995))
        obs_dts = (
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_youth_day(self):
        name = "Youth Day"
        self.assertHolidayName(name, (f"{year}-06-16" for year in range(1995, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1995))
        obs_dts = (
            "2013-06-17",
            "2019-06-17",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_national_womens_day(self):
        name = "National Women's Day"
        self.assertHolidayName(name, (f"{year}-08-09" for year in range(1995, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1995))
        obs_dts = (
            "2009-08-10",
            "2015-08-10",
            "2020-08-10",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_heritage_day(self):
        name = "Heritage Day"
        self.assertHolidayName(name, (f"{year}-09-24" for year in range(1995, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1995))
        obs_dts = (
            "2006-09-25",
            "2017-09-25",
            "2023-09-25",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_republic_day(self):
        name_1910 = "Union Day"
        name_1961 = "Republic Day"
        self.assertHolidayName(
            name_1910, (f"{year}-05-31" for year in range(self.start_year, 1961))
        )
        self.assertHolidayName(name_1961, (f"{year}-05-31" for year in range(1961, 1994)))
        self.assertNoHolidayName(name_1910, range(1961, self.end_year))
        self.assertNoHolidayName(
            name_1961, range(self.start_year, 1961), range(1994, self.end_year)
        )

    def test_ascension_day(self):
        name = "Ascension Day"
        self.assertHolidayName(
            name,
            "1940-05-02",
            "1950-05-18",
            "1960-05-26",
            "1970-05-07",
            "1980-05-15",
            "1990-05-24",
            "1993-05-20",
        )
        self.assertHolidayName(name, range(self.start_year, 1994))
        self.assertNoHolidayName(name, range(1994, self.end_year))

    def test_kruger_day(self):
        name = "Kruger Day"
        self.assertHolidayName(name, (f"{year}-10-10" for year in range(1952, 1994)))
        self.assertNoHolidayName(name, range(self.start_year, 1952), range(1994, self.end_year))

    def test_queens_birthday(self):
        name = "Queen's Birthday"
        self.assertHolidayName(
            name,
            "1952-07-14",
            "1953-07-13",
            "1954-07-12",
            "1955-07-11",
            "1956-07-09",
            "1957-07-08",
            "1958-07-14",
            "1959-07-13",
            "1960-07-11",
        )
        self.assertNoHolidayName(name, range(self.start_year, 1952), range(1961, self.end_year))

    def test_settlers_birthday(self):
        name = "Settlers' Day"
        self.assertHolidayName(
            name,
            "1952-09-01",
            "1960-09-05",
            "1970-09-07",
            "1979-09-03",
        )
        self.assertHolidayName(name, range(1952, 1980))
        self.assertNoHolidayName(name, range(self.start_year, 1952), range(1980, self.end_year))

    def test_empire_day(self):
        name = "Empire Day"
        self.assertHolidayName(name, (f"{year}-05-24" for year in range(self.start_year, 1952)))
        self.assertNoHolidayName(name, range(1952, self.end_year))

    def test_kings_birthday(self):
        name = "King's Birthday"
        self.assertHolidayName(
            name,
            "1940-08-05",
            "1941-08-04",
            "1942-08-03",
            "1943-08-02",
            "1944-08-07",
            "1945-08-06",
            "1946-08-05",
            "1947-08-04",
            "1948-08-02",
            "1949-08-01",
            "1950-08-07",
            "1951-08-06",
        )
        self.assertHolidayName(name, range(self.start_year, 1952))
        self.assertNoHolidayName(name, range(1952, self.end_year))

    def test_day_of_reconciliation(self):
        name_1910 = "Dingaan's Day"
        name_1952 = "Day of the Covenant"
        name_1980 = "Day of the Vow"
        name_1995 = "Day of Reconciliation"
        self.assertHolidayName(
            name_1910, (f"{year}-12-16" for year in range(self.start_year, 1952))
        )
        self.assertHolidayName(name_1952, (f"{year}-12-16" for year in range(1952, 1980)))
        self.assertHolidayName(name_1980, (f"{year}-12-16" for year in range(1980, 1995)))
        self.assertHolidayName(name_1995, (f"{year}-12-16" for year in range(1995, self.end_year)))
        self.assertNoHolidayName(name_1910, range(1952, self.end_year))
        self.assertNoHolidayName(
            name_1952, range(self.start_year, 1952), range(1980, self.end_year)
        )
        self.assertNoHolidayName(
            name_1980, range(self.start_year, 1980), range(1995, self.end_year)
        )
        self.assertNoHolidayName(name_1995, range(self.start_year, 1995))
        obs_dts = (
            "2007-12-17",
            "2012-12-17",
            "2018-12-17",
        )
        self.assertHolidayName(f"{name_1995} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in self.full_range))

    def test_day_of_goodwill(self):
        name_1910 = "Boxing Day"
        name_1980 = "Day of Goodwill"
        self.assertHolidayName(
            name_1910, (f"{year}-12-26" for year in range(self.start_year, 1980))
        )
        self.assertHolidayName(name_1980, (f"{year}-12-26" for year in range(1980, self.end_year)))
        self.assertNoHolidayName(name_1910, range(1980, self.end_year))
        self.assertNoHolidayName(name_1980, range(self.start_year, 1980))
        obs_dts = (
            "2010-12-27",
            "2021-12-27",
        )
        self.assertHolidayName(f"{name_1980} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
