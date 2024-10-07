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

from holidays.countries.south_africa import SouthAfrica, ZA, ZAF
from tests.common import CommonCountryTests


class TestSouthAfrica(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SouthAfrica, years=range(1940, 2050))

    def test_country_aliases(self):
        self.assertAliases(SouthAfrica, ZA, ZAF)

    def test_no_holidays(self):
        self.assertNoHolidays(SouthAfrica(years=1909))

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

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1940, 2050)))

    def test_holidays_from_1995(self):
        for year in range(1995, 2050):
            self.assertHoliday(
                f"{year}-03-21",
                f"{year}-04-27",
                f"{year}-05-01",
                f"{year}-06-16",
                f"{year}-08-09",
                f"{year}-09-24",
            )

    def test_easter(self):
        self.assertHolidayName(
            "Good Friday",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
        )
        self.assertHolidayName(
            "Family Day",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
        )
        self.assertHolidayName(
            "Easter Monday",
            "1940-03-25",
            "1960-04-18",
            "1970-03-30",
            "1978-03-27",
            "1979-04-16",
        )
        self.assertNoHolidayName("Family Day", range(1940, 1961), range(1974, 1980))
        self.assertNoHolidayName("Easter Monday", range(1980, 2050))

    def test_day_of_reconciliation(self):
        self.assertHoliday(f"{year}-12-16" for year in range(1940, 2050))
        self.assertNoHolidayName("Dingaan's Day", range(1952, 2050))
        self.assertNoHolidayName("Day of the Covenant", range(1940, 1952), range(1980, 2050))
        self.assertNoHolidayName("Day of the Vow", range(1940, 1980), range(1995, 2050))
        self.assertNoHolidayName("Day of Reconciliation", range(1940, 1995))
        self.assertHolidayName(
            "Day of Reconciliation", (f"{year}-12-16" for year in range(1995, 2005))
        )

    def test_human_rights_day(self):
        name = "Human Rights Day"
        self.assertHolidayName(name, (f"{year}-03-21" for year in range(1995, 2050)))
        self.assertNoHoliday(f"{year}-03-21" for year in range(1940, 1995))
        self.assertNoHolidayName(name, range(1940, 1995))

    def test_freedom_day(self):
        name = "Freedom Day"
        self.assertHolidayName(name, (f"{year}-04-27" for year in range(1995, 2050)))
        self.assertNoHoliday(f"{year}-04-27" for year in range(1940, 1995))
        self.assertNoHolidayName(name, range(1940, 1995))

    def test_workers_day(self):
        name = "Workers' Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1995, 2050)))
        self.assertNoHoliday(f"{year}-05-01" for year in set(range(1940, 1995)).difference({1987}))
        self.assertNoHolidayName(name, set(range(1940, 1995)).difference(set(range(1987, 1990))))
        self.assertHolidayName(name, "1987-05-01", "1988-05-06", "1989-05-05")

    def test_youth_day(self):
        name = "Youth Day"
        self.assertHolidayName(name, (f"{year}-06-16" for year in range(1995, 2050)))
        self.assertNoHoliday(f"{year}-06-16" for year in range(1940, 1995))
        self.assertNoHolidayName(name, range(1940, 1995))

    def test_national_womens_day(self):
        name = "National Women's Day"
        self.assertHolidayName(name, (f"{year}-08-09" for year in range(1995, 2050)))
        self.assertNoHoliday(f"{year}-08-09" for year in range(1940, 1995))
        self.assertNoHolidayName(name, range(1940, 1995))

    def test_heritage_day(self):
        name = "Heritage Day"
        self.assertHolidayName(name, (f"{year}-09-24" for year in range(1995, 2050)))
        self.assertNoHoliday(f"{year}-09-24" for year in range(1940, 1995))
        self.assertNoHolidayName(name, range(1940, 1995))

    def test_christmas(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(1940, 2050)))
        self.assertHolidayName("Day of Goodwill", (f"{year}-12-26" for year in range(1980, 2050)))
        self.assertHolidayName("Boxing Day", (f"{year}-12-26" for year in range(1940, 1980)))
        self.assertNoHolidayName("Day of Goodwill", range(1940, 1980))
        self.assertNoHolidayName("Boxing Day", range(1980, 2050))

    def test_founders_van_riebeecks_day(self):
        name1 = "Van Riebeeck's Day"
        name2 = "Founder's Day"
        self.assertHolidayName(name1, (f"{year}-04-06" for year in range(1952, 1974)))
        self.assertHolidayName(name2, (f"{year}-04-06" for year in range(1980, 1995)))
        self.assertNoHolidayName(name1, range(1940, 1952), range(1975, 2050))
        self.assertNoHolidayName(name2, range(1940, 1980), range(1995, 2050))

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
        self.assertNoHolidayName(name, range(1994, 2050))

    def test_empire_day(self):
        name = "Empire Day"
        self.assertHolidayName(name, (f"{year}-05-24" for year in range(1940, 1952)))
        self.assertNoHolidayName(name, range(1952, 2050))

    def test_republic_union_day(self):
        name1 = "Union Day"
        name2 = "Republic Day"
        self.assertHolidayName(name1, (f"{year}-05-31" for year in range(1940, 1961)))
        self.assertHolidayName(name2, (f"{year}-05-31" for year in range(1961, 1994)))
        self.assertNoHolidayName(name1, range(1961, 2050))
        self.assertNoHolidayName(name2, range(1940, 1961), range(1994, 2050))

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
        self.assertNoHolidayName(name, range(1940, 1952), range(1961, 2050))

    def test_family_day(self):
        name = "Family Day"
        self.assertHolidayName(name, (f"{year}-07-10" for year in range(1961, 1974)))
        self.assertNoHolidayName(name, range(1940, 1961), range(1974, 1980))

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
        self.assertNoHolidayName(name, range(1952, 2050))

    def test_settlers_birthday(self):
        name = "Settlers' Day"
        self.assertHolidayName(
            name,
            "1952-09-01",
            "1960-09-05",
            "1970-09-07",
            "1979-09-03",
        )
        self.assertNoHolidayName(name, range(1940, 1952), range(1980, 2050))

    def test_kruger_day(self):
        name = "Kruger Day"
        self.assertHolidayName(name, (f"{year}-10-10" for year in range(1952, 1994)))
        self.assertNoHolidayName(name, range(1940, 1952), range(1994, 2050))

    def test_observed(self):
        dt = (
            # New Year's Day
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
            # Human Rights Day
            "2010-03-22",
            "2021-03-22",
            # Freedom Day
            "2008-04-28",
            "2014-04-28",
            # Workers' Day
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
            # Youth Day
            "2013-06-17",
            "2019-06-17",
            # National Women's Day
            "2009-08-10",
            "2015-08-10",
            "2020-08-10",
            # Heritage Day
            "2006-09-25",
            "2017-09-25",
            "2023-09-25",
            # Day of Reconciliation
            "2007-12-17",
            "2012-12-17",
            "2018-12-17",
            # Day of Goodwill
            "2010-12-27",
            "2021-12-27",
            # special holiday
            "2000-01-03",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)
