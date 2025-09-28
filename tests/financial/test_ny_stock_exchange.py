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

from datetime import date
from unittest import TestCase

from holidays.calendars.gregorian import JAN, MAR, JUN, JUL, NOV, DEC, WED, SAT, SUN, _timedelta
from holidays.financial.ny_stock_exchange import NewYorkStockExchange, XNYS, NYSE
from tests.common import CommonFinancialTests


class TestNewYorkStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(NewYorkStockExchange)

    def test_market_aliases(self):
        self.assertAliases(NewYorkStockExchange, XNYS, NYSE)

    def test_no_holidays(self):
        self.assertNoHolidays(NewYorkStockExchange(years=self.start_year - 1))

    def test_new_years_day(self):
        name = "New Year's Day"
        name_observed = f"{name} (observed)"
        self.assertNonObservedHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

        # no observed on previous year Dec 31.
        for dt in (
            date(1994, JAN, 1),
            date(2000, JAN, 1),
            date(2005, JAN, 1),
            date(2011, JAN, 1),
            date(2022, JAN, 1),
        ):
            self.assertNoHolidayName(name, dt)
            self.assertNoHolidayName(name_observed, _timedelta(dt, -1))

    def test_martin_luther_king_jr_day(self):
        name = "Martin Luther King Jr. Day"
        self.assertHolidayName(
            name,
            "2020-01-20",
            "2021-01-18",
            "2022-01-17",
            "2023-01-16",
            "2024-01-15",
            "2025-01-20",
        )
        self.assertHolidayName(name, range(1998, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1998))

    def test_lincolns_birthday(self):
        name = "Lincoln's Birthday"
        self.assertNonObservedHolidayName(
            name,
            (f"{year}-02-12" for year in range(1896, 1954)),
            "1968-02-12",
        )
        self.assertNoHolidayName(
            name, range(self.start_year, 1896), range(1954, 1968), range(1969, self.end_year)
        )
        obs_dts = (
            "1944-02-11",
            "1949-02-11",
            "1950-02-13",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_washingtons_birthday(self):
        name = "Washington's Birthday"
        self.assertNonObservedHolidayName(
            name, (f"{year}-02-22" for year in range(self.start_year, 1971))
        )
        self.assertHolidayName(
            name,
            "2020-02-17",
            "2021-02-15",
            "2022-02-21",
            "2023-02-20",
            "2024-02-19",
            "2025-02-17",
        )
        self.assertHolidayName(name, range(1971, self.end_year))
        obs_dts = (
            "1964-02-21",
            "1969-02-21",
            "1970-02-23",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_good_friday(self):
        name = "Good Friday"
        years_absent = {1898, 1906, 1907}
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(
            name, (year for year in self.full_range if year not in years_absent)
        )
        self.assertNoHolidayName(name, years_absent)

    def test_memorial_day(self):
        name = "Memorial Day"
        self.assertNonObservedHolidayName(name, (f"{year}-05-30" for year in range(1873, 1971)))
        self.assertHolidayName(
            name,
            "2020-05-25",
            "2021-05-31",
            "2022-05-30",
            "2023-05-29",
            "2024-05-27",
            "2025-05-26",
        )
        self.assertHolidayName(name, range(1971, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1873))
        obs_dts = (
            "1964-05-29",
            "1965-05-31",
            "1970-05-29",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_flag_day(self):
        name = "Flag Day"
        self.assertNonObservedHolidayName(name, (f"{year}-06-14" for year in range(1916, 1954)))
        self.assertNoHolidayName(name, range(self.start_year, 1916), range(1954, self.end_year))
        obs_dts = (
            "1947-06-13",
            "1952-06-13",
            "1953-06-15",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_juneteenth_national_independence_day(self):
        name = "Juneteenth National Independence Day"
        self.assertNonObservedHolidayName(
            name, (f"{year}-06-19" for year in range(2022, self.end_year))
        )
        self.assertNoHolidayName(name, range(self.start_year, 2022))
        obs_dts = (
            "2022-06-20",
            "2027-06-18",
            "2032-06-18",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertNonObservedHolidayName(name, (f"{year}-07-04" for year in self.full_range))
        obs_dts = (
            "2015-07-03",
            "2020-07-03",
            "2021-07-05",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_labor_day(self):
        name = "Labor Day"
        self.assertHolidayName(
            name,
            "2020-09-07",
            "2021-09-06",
            "2022-09-05",
            "2023-09-04",
            "2024-09-02",
            "2025-09-01",
        )
        self.assertHolidayName(name, range(1887, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1887))

    def test_columbus_day(self):
        name = "Columbus Day"
        self.assertNonObservedHolidayName(name, (f"{year}-10-12" for year in range(1909, 1954)))
        self.assertNoHolidayName(name, range(self.start_year, 1909), range(1954, self.end_year))
        obs_dts = (
            "1946-10-11",
            "1947-10-13",
            "1952-10-13",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_election_day(self):
        for dt in (
            date(1887, NOV, 8),
            date(1901, NOV, 5),
            date(1902, NOV, 4),
            date(1920, NOV, 2),
            date(1935, NOV, 5),
            date(1950, NOV, 7),
            date(1968, NOV, 5),
            date(1972, NOV, 7),
            date(1976, NOV, 2),
            date(1980, NOV, 4),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +7))
            self.assertNoHoliday(_timedelta(dt, -7))

        self.assertNoHoliday(
            "1969-11-04",
            "1970-11-03",
            "1971-11-02",
            "1973-11-06",
            "1974-11-05",
            "1975-11-04",
            "1977-11-01",
            "1978-11-07",
            "1979-11-06",
            "1981-11-03",
            "2021-11-02",
            "2022-11-01",
        )

    def test_veterans_day(self):
        name = "Veteran's Day"
        self.assertNonObservedHolidayName(
            name,
            "1918-11-11",
            "1921-11-11",
            (f"{year}-11-11" for year in range(1934, 1954)),
        )
        self.assertNoHolidayName(
            name,
            range(self.start_year, 1918),
            range(1919, 1921),
            range(1922, 1934),
            range(1954, self.end_year),
        )
        obs_dts = (
            "1945-11-12",
            "1950-11-10",
            "1951-11-12",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_thanksgiving_day(self):
        name = "Thanksgiving Day"
        self.assertHolidayName(
            name,
            "2020-11-26",
            "2021-11-25",
            "2022-11-24",
            "2023-11-23",
            "2024-11-28",
            "2025-11-27",
        )
        self.assertHolidayName(name, self.full_range)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertNonObservedHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2016-12-26",
            "2021-12-24",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_special_holidays(self):
        # add to this list as new historical holidays are added
        special_holidays = [
            "1888-03-12",  # Blizzard of 1888
            "1888-03-13",  # Blizzard of 1888
            "1888-11-30",  # Thanksgiving Friday 1888
            "1889-04-29",  # Centennial of George Washington's Inauguration
            "1889-04-30",  # Centennial of George Washington's Inauguration
            "1889-05-01",  # Centennial of George Washington's Inauguration
            "1892-10-12",  # Columbian Celebration
            "1892-10-21",  # Columbian Celebration
            "1893-04-27",  # Columbian Celebration
            "1897-04-27",  # Grant's Birthday
            "1898-05-04",  # Charter Day
            "1899-05-29",  # Monday before Decoration Day
            "1899-07-03",  # Monday before Independence Day
            "1899-09-29",  # Admiral Dewey Celebration
            "1900-12-24",  # Christmas Eve
            "1901-07-05",  # Friday after Independence Day
            "1901-09-19",  # National Day of Mourning for President William McKinley
            "1903-04-22",  # Opening of new NYSE building
            "1917-06-05",  # Draft Registration Day
            "1918-01-28",  # Heatless Day
            "1918-02-04",  # Heatless Day
            "1918-02-11",  # Heatless Day
            "1918-09-12",  # Draft Registration Day
            "1918-11-11",  # Armistice Day
            "1919-03-25",  # Homecoming Day for 27th Division
            "1919-05-06",  # Parade Day for 77th Division
            "1919-09-10",  # Return of General Pershing
            "1923-08-03",  # Death of President Warren G. Harding
            "1923-08-10",  # National Day of Mourning for President Warren G. Harding
            "1927-06-13",  # Parade for Colonel Charles Lindbergh
            "1929-11-01",  # Catch Up Day
            "1929-11-29",  # Catch Up Day
            "1945-08-15",  # V-J Day (WWII)
            "1945-08-16",  # V-J Day (WWII)
            "1945-12-24",  # Christmas Eve
            "1954-12-24",  # Christmas Eve
            "1956-12-24",  # Christmas Eve
            "1958-12-26",  # Day after Christmas
            "1961-05-29",  # Day before Decoration Day
            "1963-11-25",  # National Day of Mourning for President John F. Kennedy
            "1965-12-24",  # Christmas Eve
            "1968-04-09",  # National Day of Mourning for Martin Luther King Jr.
            "1968-07-05",  # Day after Independence Day
            "1969-02-10",  # Heavy Snow
            "1969-03-31",  # National Day of Mourning for former President Dwight D. Eisenhower
            "1969-07-21",  # National Participation in Lunar Exploration
            "1972-12-28",  # National Day of Mourning for former President Harry S. Truman
            "1973-01-25",  # National Day of Mourning for former President Lyndon B. Johnson
            "1977-07-14",  # Blackout in New York City
            "1985-09-27",  # Hurricane Gloria
            "1994-04-27",  # National Day of Mourning for former President Richard M. Nixon
            "2001-09-11",  # Closed for Sept 11, 2001 Attacks
            "2001-09-12",  # Closed for Sept 11, 2001 Attacks
            "2001-09-13",  # Closed for Sept 11, 2001 Attacks
            "2001-09-14",  # Closed for Sept 11, 2001 Attacks
            "2004-06-11",  # National Day of Mourning for former President Ronald Reagan
            "2007-01-02",  # National Day of Mourning for former President Gerald R. Ford
            "2012-10-29",  # Hurricane Sandy
            "2012-10-30",  # Hurricane Sandy
            "2018-12-05",  # National Day of Mourning for former President George H. W. Bush
            "2025-01-09",  # National Day of Mourning for former President Jimmy Carter
        ]

        def _make_special_holiday_list(begin, end, days=None, weekends=False):
            return [
                day
                for day in (_timedelta(begin, n) for n in range((end - begin).days + 1))
                if (weekends or day.weekday() not in {SAT, SUN})
                and (days is None or day.weekday() in days)
            ]

        wwi_holidays = _make_special_holiday_list(date(1914, JUL, 31), date(1914, NOV, 27))
        oneoff_bank_holidays = _make_special_holiday_list(date(1933, MAR, 6), date(1933, MAR, 14))
        paper_crisis_holidays = _make_special_holiday_list(
            date(1968, JUN, 12), date(1968, DEC, 31), days={WED}
        )
        for dt in special_holidays + wwi_holidays + oneoff_bank_holidays + paper_crisis_holidays:
            self.assertHoliday(dt)

        # double check that we catch beginning/ending of holiday periods -
        # covers off-by-one errors
        for dt in (
            date(1914, JUL, 31),  # begin WWI holidays
            date(1933, MAR, 6),  # begin oneoff bank holidays
            date(1968, JUN, 12),  # begin paper crisis holidays
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))

        for dt in (
            date(1914, NOV, 27),  # end WWI holidays
            date(1933, MAR, 14),  # end oneoff bank holidays
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, +1))

    def test_2023(self):
        self.assertHolidays(
            NewYorkStockExchange(years=2023),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-16", "Martin Luther King Jr. Day"),
            ("2023-02-20", "Washington's Birthday"),
            ("2023-04-07", "Good Friday"),
            ("2023-05-29", "Memorial Day"),
            ("2023-06-19", "Juneteenth National Independence Day"),
            ("2023-07-04", "Independence Day"),
            ("2023-09-04", "Labor Day"),
            ("2023-11-23", "Thanksgiving Day"),
            ("2023-12-25", "Christmas Day"),
        )
