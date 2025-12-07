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

from holidays.calendars.gregorian import (
    JAN,
    MAR,
    MAY,
    JUN,
    JUL,
    NOV,
    DEC,
    WED,
    THU,
    _timedelta,
)
from holidays.financial.ny_stock_exchange import NewYorkStockExchange
from tests.common import CommonFinancialTests


class TestNewYorkStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(NewYorkStockExchange)

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
        no_obs_dts = (
            "1943-12-31",
            "1948-12-31",
            "1993-12-31",
            "1999-12-31",
            "2004-12-31",
            "2010-12-31",
            "2021-12-31",
        )
        self.assertNoHolidayName(name_observed, no_obs_dts)
        self.assertNoHoliday(no_obs_dts)

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
        name_observed = f"{name} (observed)"
        self.assertNonObservedHolidayName(name, (f"{year}-02-12" for year in range(1896, 1954)))
        self.assertNoHolidayName(
            name, range(self.start_year, 1896), range(1954, 1968), range(1969, self.end_year)
        )
        obs_dts = (
            "1939-02-13",
            "1950-02-13",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        no_obs_dts = (
            "1944-02-11",
            "1949-02-11",
        )
        self.assertNoHolidayName(name_observed, no_obs_dts)
        self.assertNoHoliday(no_obs_dts)

    def test_washingtons_birthday(self):
        name = "Washington's Birthday"
        name_observed = f"{name} (observed)"
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
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        no_obs_dts = (
            "1941-02-21",
            "1947-02-21",
        )
        self.assertNoHolidayName(name_observed, no_obs_dts)
        self.assertNoHoliday(no_obs_dts)

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
        name_observed = f"{name} (observed)"
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
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        no_obs_dts = (
            "1936-05-29",
            "1942-05-29",
        )
        self.assertNoHolidayName(name_observed, no_obs_dts)
        self.assertNoHoliday(no_obs_dts)

    def test_flag_day(self):
        name = "Flag Day"
        name_observed = f"{name} (observed)"
        self.assertNonObservedHolidayName(name, (f"{year}-06-14" for year in range(1916, 1954)))
        self.assertNoHolidayName(name, range(self.start_year, 1916), range(1954, self.end_year))
        obs_dts = (
            "1936-06-15",
            "1942-06-15",
            "1953-06-15",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        no_obs_dts = (
            "1947-06-13",
            "1952-06-13",
        )
        self.assertNoHolidayName(name_observed, no_obs_dts)
        self.assertNoHoliday(no_obs_dts)

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
        name_observed = f"{name} (observed)"
        self.assertNonObservedHolidayName(name, (f"{year}-07-04" for year in self.full_range))
        obs_dts = (
            "2015-07-03",
            "2020-07-03",
            "2021-07-05",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        no_obs_dts = (
            "1936-07-03",
            "1942-07-03",
        )
        self.assertNoHolidayName(name_observed, no_obs_dts)
        self.assertNoHoliday(no_obs_dts)

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
        name_observed = f"{name} (observed)"
        self.assertNonObservedHolidayName(name, (f"{year}-10-12" for year in range(1909, 1954)))
        self.assertNoHolidayName(name, range(self.start_year, 1909), range(1954, self.end_year))
        obs_dts = (
            "1941-10-13",
            "1947-10-13",
            "1952-10-13",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        no_obs_dts = (
            "1940-10-11",
            "1946-10-11",
        )
        self.assertNoHolidayName(name_observed, no_obs_dts)
        self.assertNoHoliday(no_obs_dts)

    def test_election_day(self):
        name = "Election Day"
        self.assertHolidayName(
            name,
            "1950-11-07",
            "1968-11-05",
            "1972-11-07",
            "1976-11-02",
            "1980-11-04",
        )
        self.assertHolidayName(name, range(self.start_year, 1969))
        self.assertNoHolidayName(
            name,
            range(1969, 1972),
            range(1973, 1976),
            range(1977, 1980),
            range(1981, self.end_year),
        )

    def test_veterans_day(self):
        name = "Veteran's Day"
        name_observed = f"{name} (observed)"
        self.assertNonObservedHolidayName(name, (f"{year}-11-11" for year in range(1934, 1954)))
        self.assertNoHolidayName(
            name,
            range(self.start_year, 1918),
            range(1919, 1921),
            range(1922, 1934),
            range(1954, self.end_year),
        )
        obs_dts = (
            "1945-11-12",
            "1951-11-12",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        no_obs_dts = (
            "1944-11-10",
            "1950-11-10",
        )
        self.assertNoHolidayName(name_observed, no_obs_dts)
        self.assertNoHoliday(no_obs_dts)

    def test_thanksgiving_day(self):
        name = "Thanksgiving Day"
        self.assertHolidayName(
            name,
            # Last Thu of Nov and other exceptions.
            "1863-11-26",
            "1864-11-24",
            "1865-12-07",
            "1866-11-29",
            "1867-11-28",
            "1868-11-26",
            "1869-11-18",
            # Last Thu of Nov.
            "1933-11-30",
            "1934-11-29",
            "1935-11-28",
            "1936-11-26",
            "1937-11-25",
            "1938-11-24",
            # Franksgiving.
            "1939-11-23",
            "1940-11-21",
            "1941-11-20",
            # 4th Thu of Nov.
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
        name_observed = f"{name} (observed)"
        self.assertNonObservedHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2016-12-26",
            "2021-12-24",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        no_obs_dts = (
            "1943-12-24",
            "1948-12-24",
        )
        self.assertNoHolidayName(name_observed, no_obs_dts)
        self.assertNoHoliday(no_obs_dts)

    def _make_special_holiday_list(self, begin, end, *, days=None):
        return [
            day
            for day in (_timedelta(begin, n) for n in range((end - begin).days + 1))
            if self.holidays._is_weekday(day) and (days is None or day.weekday() in days)
        ]

    def test_special_public_holidays(self):
        # NOTE: update the list whenever new historical holidays are added.
        special_holidays = [
            "1885-08-08",  # Funeral of former President Ulysses S. Grant.
            "1887-07-02",  # Saturday before Independence Day.
            "1887-12-24",  # Saturday before Christmas.
            "1888-03-12",  # Blizzard of 1888.
            "1888-03-13",  # Blizzard of 1888.
            "1888-09-01",  # Saturday before Labor Day.
            "1888-11-30",  # Friday after Thanksgiving Day.
            "1889-04-29",  # Centennial of George Washington's Inauguration.
            "1889-04-30",  # Centennial of George Washington's Inauguration.
            "1889-05-01",  # Centennial of George Washington's Inauguration.
            "1890-07-05",  # Saturday after Independence Day.
            "1891-12-26",  # Saturday after Christmas Day.
            "1892-07-02",  # Saturday before Independence Day.
            "1892-10-12",  # Columbian Celebration.
            "1892-10-21",  # Columbian Celebration.
            "1892-10-22",  # Columbian Celebration.
            "1893-04-27",  # Columbian Celebration.
            "1896-12-26",  # Saturday after Christmas Day.
            "1897-04-27",  # Grant's Birthday.
            "1898-05-04",  # Charter Day.
            "1898-07-02",  # Saturday before Independence Day.
            "1898-08-20",  # Welcome of naval commanders.
            "1898-09-03",  # Saturday before Labor Day.
            "1898-12-24",  # Saturday before Christmas.
            "1899-02-11",  # Saturday before Lincoln's Birthday.
            "1899-05-29",  # Monday before Decoration Day.
            "1899-07-03",  # Monday before Independence Day.
            "1899-09-29",  # Admiral Dewey Celebration.
            "1899-09-30",  # Admiral Dewey Celebration.
            "1899-11-25",  # Funeral of Vice-President Garret A. Hobart.
            "1900-04-14",  # Saturday after Good Friday.
            "1900-09-01",  # Saturday before Labor Day.
            "1900-12-24",  # Saturday before Christmas.
            "1901-02-02",  # Funeral of Queen Victoria of England.
            "1901-02-23",  # Saturday after Washington's Birthday.
            "1901-04-06",  # Saturday after Good Friday.
            "1901-04-27",  # Moved to temporary quarters in Produce Exchange.
            "1901-05-11",  # Enlarged temporary quarters in Produce Exchange.
            "1901-07-05",  # Friday after Independence Day.
            "1901-07-06",  # Saturday after Independence Day.
            "1901-08-31",  # Saturday before Labor Day.
            "1901-09-14",  # Death of President William McKinley.
            "1901-09-19",  # Funeral of President William McKinley.
            "1902-03-29",  # Saturday after Good Friday.
            "1902-05-31",  # Saturday after Decoration Day.
            "1902-07-05",  # Saturday after Independence Day.
            "1902-08-09",  # Coronation of King Edward VII of England.
            "1902-08-30",  # Saturday before Labor Day.
            "1903-02-21",  # Saturday before Washington's Birthday.
            "1903-04-11",  # Saturday after Good Friday.
            "1903-04-22",  # Opening of new NYSE building.
            "1903-09-05",  # Saturday before Labor Day.
            "1903-12-26",  # Saturday after Christmas Day.
            "1904-05-28",  # Saturday before Decoration Day.
            "1904-07-02",  # Saturday before Independence Day.
            "1904-09-03",  # Saturday before Labor Day.
            "1904-12-24",  # Saturday before Christmas.
            "1905-04-22",  # Saturday after Good Friday.
            "1907-02-23",  # Saturday after Washington's Birthday.
            "1907-03-30",  # Saturday after Good Friday.
            "1907-08-31",  # Saturday before Labor Day.
            "1908-04-18",  # Saturday after Good Friday.
            "1908-09-05",  # Saturday before Labor Day.
            "1908-12-26",  # Saturday after Christmas Day.
            "1909-02-13",  # Saturday after Lincoln's Birthday.
            "1909-04-10",  # Saturday after Good Friday.
            "1909-05-29",  # Saturday before Decoration Day.
            "1909-07-03",  # Saturday before Independence Day.
            "1909-09-04",  # Saturday before Labor Day.
            "1909-09-25",  # Reception Day of the Hudson-Fulton Celebration.
            "1910-03-26",  # Saturday after Good Friday.
            "1910-05-28",  # Saturday before Decoration Day.
            "1910-07-02",  # Saturday before Independence Day.
            "1910-09-03",  # Saturday before Labor Day.
            "1910-12-24",  # Saturday before Christmas.
            "1911-04-15",  # Saturday after Good Friday.
            "1911-09-02",  # Saturday before Labor Day.
            "1911-12-23",  # Saturday before Christmas.
            "1912-08-31",  # Saturday before Labor Day.
            "1912-11-02",  # Funeral of Vice-President James S. Sherman.
            "1913-03-22",  # Saturday after Good Friday.
            "1913-05-31",  # Saturday after Decoration Day.
            "1913-07-05",  # Saturday after Independence Day.
            "1913-08-30",  # Saturday before Labor Day.
            "1916-12-30",  # Saturday before New Year's Day.
            "1917-06-05",  # Draft Registration Day.
            "1917-08-04",  # Heat.
            "1917-09-01",  # Saturday before Labor Day.
            "1917-10-13",  # Saturday after Columbus Day.
            "1918-01-28",  # Heatless Day.
            "1918-02-04",  # Heatless Day.
            "1918-02-11",  # Heatless Day.
            "1918-09-12",  # Draft Registration Day.
            "1918-11-11",  # Armistice signed.
            "1919-03-25",  # Homecoming of 27th Division.
            "1919-05-06",  # Parade of 77th Division.
            "1919-05-31",  # Saturday after Decoration Day.
            "1919-07-05",  # Saturday after Independence Day.
            "1919-07-19",  # Heat and to allow offices to catch up on work.
            "1919-08-02",  # To allow offices to catch up on work.
            "1919-08-16",  # To allow offices to catch up on work.
            "1919-08-30",  # Saturday before Labor Day.
            "1919-09-10",  # Return of General John J. Pershing.
            "1920-04-03",  # Saturday after Good Friday.
            "1920-05-01",  # Many firms changed office locations.
            "1920-07-03",  # Saturday before Independence Day.
            "1920-09-04",  # Saturday before Labor Day.
            "1921-05-28",  # Saturday before Decoration Day.
            "1921-07-02",  # Saturday before Independence Day.
            "1921-09-03",  # Saturday before Labor Day.
            "1921-11-11",  # Veteran's Day.
            "1922-12-23",  # Saturday before Christmas.
            "1923-08-03",  # Death of President Warren G. Harding.
            "1923-08-10",  # Funeral of President Warren G. Harding.
            "1924-05-31",  # Saturday after Decoration Day.
            "1925-12-26",  # Saturday after Christmas Day.
            "1926-05-29",  # Saturday before Decoration Day.
            "1926-07-03",  # Saturday before Independence Day.
            "1926-09-04",  # Saturday before Labor Day.
            "1927-06-13",  # Parade for Colonel Charles A. Lindbergh.
            "1928-04-07",  # Heavy volume. To allow member firm offices to catch up on work.
            "1928-04-21",  # Heavy volume. To allow member firm offices to catch up on work.
            "1928-05-05",  # Heavy volume. To allow member firm offices to catch up on work.
            "1928-05-12",  # Heavy volume. To allow member firm offices to catch up on work.
            "1928-05-19",  # Heavy volume. To allow member firm offices to catch up on work.
            "1928-05-26",  # Heavy volume. To allow member firm offices to catch up on work.
            "1928-11-24",  # Heavy volume. To allow member firm offices to catch up on work.
            "1929-02-09",  # Heavy volume. To allow member firm offices to catch up on work.
            "1929-02-23",  # Saturday after Washington's Birthday.
            "1929-03-30",  # Saturday after Good Friday.
            "1929-08-31",  # Saturday before Labor Day.
            "1929-11-01",  # Catch Up Day.
            "1929-11-02",  # Catch Up Day.
            "1929-11-09",  # Catch Up Day.
            "1929-11-16",  # Catch Up Day.
            "1929-11-23",  # Catch Up Day.
            "1929-11-29",  # Catch Up Day.
            "1929-11-30",  # Catch Up Day.
            "1930-04-19",  # Saturday after Good Friday.
            "1930-05-31",  # Saturday after Decoration Day.
            "1930-07-05",  # Saturday after Independence Day.
            "1930-08-30",  # Saturday before Labor Day.
            "1931-09-05",  # Saturday before Labor Day.
            "1931-12-26",  # Saturday after Christmas Day.
            "1932-07-02",  # Saturday before Independence Day.
            "1933-01-07",  # Funeral of former President Calvin Coolidge.
            "1933-03-04",  # State Banking Holiday.
            "1933-03-06",  # National Banking Holiday.
            "1933-03-07",  # National Banking Holiday.
            "1933-03-08",  # National Banking Holiday.
            "1933-03-09",  # National Banking Holiday.
            "1933-03-10",  # National Banking Holiday.
            "1933-03-11",  # National Banking Holiday.
            "1933-03-13",  # National Banking Holiday.
            "1933-03-14",  # National Banking Holiday.
            "1933-07-28",  # Volume activity.
            "1933-08-05",  # Volume activity.
            "1933-08-12",  # Volume activity.
            "1933-08-19",  # Volume activity.
            "1933-08-26",  # Volume activity.
            "1933-09-02",  # Volume activity.
            "1936-12-26",  # Saturday after Christmas Day.
            "1937-05-29",  # Saturday before Decoration Day.
            "1937-07-03",  # Saturday before Independence Day.
            "1945-04-14",  # National Day of Mourning for President Franklin D. Roosevelt.
            "1945-08-15",  # V-J Day. End of World War II.
            "1945-08-16",  # V-J Day. End of World War II.
            "1945-10-13",  # Saturday after Columbus Day.
            "1945-10-27",  # Navy Day.
            "1945-12-24",  # Christmas Eve.
            "1946-02-23",  # Saturday after Washington's Birthday.
            "1946-05-25",  # Railroad strike.
            "1948-01-03",  # Severe weather conditions.
            "1949-12-24",  # Christmas Eve.
            "1950-12-23",  # Saturday before Christmas Eve.
            "1954-12-24",  # Christmas Eve.
            "1956-12-24",  # Christmas Eve.
            "1958-12-26",  # Day after Christmas.
            "1961-05-29",  # Day before Decoration Day.
            "1963-11-25",  # Funeral of President John F. Kennedy.
            "1965-12-24",  # Christmas Eve.
            "1968-02-12",  # Lincoln's Birthday.
            "1968-04-09",  # National Day of Mourning for Martin Luther King, Jr..
            "1968-07-05",  # Day after Independence Day.
            "1969-02-10",  # Heavy Snow.
            "1969-03-31",  # Funeral of former President Dwight D. Eisenhower.
            "1969-07-21",  # National Day of Participation for the Lunar Exploration.
            "1972-12-28",  # Funeral of former President Harry S. Truman.
            "1973-01-25",  # Funeral of former President Lyndon B. Johnson.
            "1977-07-14",  # Blackout in New York City.
            "1985-09-27",  # Hurricane Gloria.
            "1994-04-27",  # Funeral of former President Richard M. Nixon.
            "2001-09-11",  # Closed following Attacks on the World Trade Center.
            "2001-09-12",  # Closed following Attacks on the World Trade Center.
            "2001-09-13",  # Closed following Attacks on the World Trade Center.
            "2001-09-14",  # Closed following Attacks on the World Trade Center.
            "2004-06-11",  # National Day of Mourning for former President Ronald Reagan.
            "2007-01-02",  # National Day of Mourning for former President Gerald R. Ford.
            "2012-10-29",  # Hurricane Sandy.
            "2012-10-30",  # Hurricane Sandy.
            "2018-12-05",  # National Day of Mourning for former President George H. W. Bush.
            "2025-01-09",  # National Day of Mourning for former President Jimmy Carter.
        ]

        wwi_holidays = self._make_special_holiday_list(date(1914, JUL, 31), date(1914, NOV, 27))
        special_bank_holidays = self._make_special_holiday_list(
            date(1933, MAR, 6), date(1933, MAR, 14)
        )
        paperwork_crisis_holidays = self._make_special_holiday_list(
            date(1968, JUN, 12), date(1968, DEC, 31), days={WED}
        )
        self.assertHoliday(
            special_holidays,
            wwi_holidays,
            special_bank_holidays,
            paperwork_crisis_holidays,
        )

    def test_day_before_independence_day(self):
        name = "Day before Independence Day (markets close at 1:00pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "1995-07-03",
            "1997-07-03",
            "2000-07-03",
            "2001-07-03",
            "2003-07-03",
            "2006-07-03",
            "2007-07-03",
            "2008-07-03",
            "2012-07-03",
            "2014-07-03",
            "2017-07-03",
            "2018-07-03",
            "2023-07-03",
            "2025-07-03",
        )
        self.assertNoHalfDayHolidayName(name, range(self.start_year, 1993), 1996, 2002)

    def test_day_after_thanksgiving(self):
        name = "Day after Thanksgiving Day (markets close at 1:00pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "2020-11-27",
            "2021-11-26",
            "2022-11-25",
            "2023-11-24",
            "2024-11-29",
            "2025-11-28",
        )
        self.assertHalfDayHolidayName(name, range(1993, self.end_year))
        self.assertNoHalfDayHolidayName(name, range(self.start_year, 1993))

    def test_christmas_eve(self):
        name = "Christmas Eve (markets close at 1:00pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "1996-12-24",
            "1997-12-24",
            "1998-12-24",
            "2001-12-24",
            "2002-12-24",
            "2003-12-24",
            "2007-12-24",
            "2008-12-24",
            "2009-12-24",
            "2012-12-24",
            "2013-12-24",
            "2014-12-24",
            "2015-12-24",
            "2018-12-24",
            "2019-12-24",
            "2020-12-24",
            "2024-12-24",
            "2025-12-24",
        )
        self.assertNoHalfDayHolidayName(name, range(self.start_year, 1951), range(1952, 1993))

    def test_special_half_day_holidays(self):
        special_holidays = [
            "1908-06-26",  # Funeral of former President Grover Cleveland (from 1:00pm).
            "1910-05-07",  # Death of King Edward VII of England (from 11:00am).
            "1917-08-29",  # Parade of National Guard (from 12:00noon).
            "1917-10-24",  # Liberty Day (from 12:00noon).
            "1918-04-26",  # Liberty Day (from 12:00noon).
            "1918-11-07",  # False armistice report (from 2:30pm).
            "1919-01-07",  # Funeral of former President Theodore Roosevelt (from 12:30pm).
            "1920-09-16",  # Wall Street explosion (from 12:00noon).
            "1924-02-06",  # Funeral of former President Woodrow Wilson (from 12:30pm).
            "1925-09-18",  # Funeral of former NYSE president Seymour L. Cromwell (from 2:30pm).
            "1928-05-21",  # Heavy volume. To allow member firm offices to catch up (from 2:00pm).
            "1928-05-22",  # Heavy volume. To allow member firm offices to catch up (from 2:00pm).
            "1928-05-23",  # Heavy volume. To allow member firm offices to catch up (from 2:00pm).
            "1928-05-24",  # Heavy volume. To allow member firm offices to catch up (from 2:00pm).
            "1928-05-25",  # Heavy volume. To allow member firm offices to catch up (from 2:00pm).
            "1929-11-06",  # Catch Up Day (from 1:00pm).
            "1929-11-07",  # Catch Up Day (from 1:00pm).
            "1929-11-08",  # Catch Up Day (from 1:00pm).
            "1929-11-11",  # Catch Up Day (from 1:00pm).
            "1929-11-12",  # Catch Up Day (from 1:00pm).
            "1929-11-13",  # Catch Up Day (from 1:00pm).
            "1929-11-14",  # Catch Up Day (from 1:00pm).
            "1929-11-15",  # Catch Up Day (from 1:00pm).
            "1929-11-18",  # Catch Up Day (from 1:00pm).
            "1929-11-19",  # Catch Up Day (from 1:00pm).
            "1929-11-20",  # Catch Up Day (from 1:00pm).
            "1929-11-21",  # Catch Up Day (from 1:00pm).
            "1929-11-22",  # Catch Up Day (from 1:00pm).
            "1930-03-11",  # Funeral of former President William Howard Taft (from 12:30pm).
            "1933-09-13",  # NRA demonstration (from 12:00noon).
            "1951-12-24",  # Christmas Eve (from 1:00pm).
            "1963-11-22",  # Assassination of President John F. Kennedy (from 2:07pm).
            "1964-10-23",  # Funeral of former President Herbert C. Hoover (from 2:00pm).
            "1966-01-06",  # Transit strike (from 2:00pm).
            "1966-01-07",  # Transit strike (from 2:00pm).
            "1966-01-10",  # Transit strike (from 2:00pm).
            "1966-01-11",  # Transit strike (from 2:00pm).
            "1966-01-12",  # Transit strike (from 2:00pm).
            "1966-01-13",  # Transit strike (from 2:00pm).
            "1966-01-14",  # Transit strike (from 2:00pm).
            "1967-08-08",  # Back office work load (from 2:00pm).
            "1967-08-09",  # Back office work load (from 2:00pm).
            "1967-08-10",  # Back office work load (from 2:00pm).
            "1967-08-11",  # Back office work load (from 2:00pm).
            "1967-08-14",  # Back office work load (from 2:00pm).
            "1967-08-15",  # Back office work load (from 2:00pm).
            "1967-08-16",  # Back office work load (from 2:00pm).
            "1967-08-17",  # Back office work load (from 2:00pm).
            "1967-08-18",  # Back office work load (from 2:00pm).
            "1974-12-24",  # Christmas Eve (from 2:00pm).
            "1975-02-12",  # Snowstorm (from 2:30pm).
            "1975-12-24",  # Christmas Eve (from 2:00pm).
            "1976-08-09",  # Hurricane watch (from 3:00pm).
            "1978-02-06",  # Snowstorm (from 2:00pm).
            "1981-03-30",  # Assassination attempt on President Reagan (from 3:17pm).
            "1981-09-09",  # Con Edison power failure in lower Manhattan (from 3:28pm).
            "1987-10-23",  # Shortened hours following market break (from 2:00pm).
            "1987-10-26",  # Shortened hours following market break (from 2:00pm).
            "1987-10-27",  # Shortened hours following market break (from 2:00pm).
            "1987-10-28",  # Shortened hours following market break (from 2:00pm).
            "1987-10-29",  # Shortened hours following market break (from 2:00pm).
            "1987-10-30",  # Shortened hours following market break (from 2:00pm).
            "1987-11-02",  # Shortened hours following market break (from 2:30pm).
            "1987-11-03",  # Shortened hours following market break (from 2:30pm).
            "1987-11-04",  # Shortened hours following market break (from 2:30pm).
            "1987-11-05",  # Shortened hours following market break (from 3:00pm).
            "1987-11-06",  # Shortened hours following market break (from 3:00pm).
            "1987-11-09",  # Shortened hours following market break (from 3:30pm).
            "1987-11-10",  # Shortened hours following market break (from 3:30pm).
            "1987-11-11",  # Shortened hours following market break (from 3:30pm).
            "1990-12-24",  # Christmas Eve (from 2:00pm).
            "1991-12-24",  # Christmas Eve (from 2:00pm).
            "1992-11-27",  # Day after Thanksgiving Day (from 2:00pm).
            "1992-12-24",  # Christmas Eve (from 2:00pm).
            "1994-02-11",  # Snowstorm (from 2:30pm).
            "1996-07-05",  # Day after Independence Day (from 1:00pm).
            "1997-12-26",  # Friday after Christmas Day (from 1:00pm).
            "1999-12-31",  # New Year's Eve (from 1:00pm).
            "2002-07-05",  # Day after Independence Day (from 1:00pm).
            "2003-12-26",  # Friday after Christmas Day (from 1:00pm).
            "2013-07-03",  # Day before Independence Day (from 1:00pm).
        ]

        back_office_holidays = self._make_special_holiday_list(
            date(1968, JAN, 22), date(1968, MAR, 1)
        )
        paperwork_crisis_holidays_1 = self._make_special_holiday_list(
            date(1969, JAN, 2), date(1969, JUL, 3), days={THU}
        )
        paperwork_crisis_holidays_2 = self._make_special_holiday_list(
            date(1969, JUL, 7), date(1969, DEC, 31)
        )
        paperwork_crisis_holidays_3 = self._make_special_holiday_list(
            date(1970, JAN, 2), date(1970, MAY, 1)
        )
        self.assertHalfDayHoliday(
            special_holidays,
            back_office_holidays,
            paperwork_crisis_holidays_1,
            paperwork_crisis_holidays_2,
            paperwork_crisis_holidays_3,
        )

    def test_2023(self):
        self.assertHolidaysInYear(
            2023,
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

    def test_half_day_2023(self):
        self.assertHalfDayHolidaysInYear(
            2023,
            ("2023-07-03", "Day before Independence Day (markets close at 1:00pm)"),
            ("2023-11-24", "Day after Thanksgiving Day (markets close at 1:00pm)"),
        )

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "New Year's Day"),
            ("2024-01-15", "Martin Luther King Jr. Day"),
            ("2024-02-19", "Washington's Birthday"),
            ("2024-03-29", "Good Friday"),
            ("2024-05-27", "Memorial Day"),
            ("2024-06-19", "Juneteenth National Independence Day"),
            ("2024-07-04", "Independence Day"),
            ("2024-09-02", "Labor Day"),
            ("2024-11-28", "Thanksgiving Day"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_half_day_2024(self):
        self.assertHalfDayHolidaysInYear(
            2024,
            ("2024-07-03", "Day before Independence Day (markets close at 1:00pm)"),
            ("2024-11-29", "Day after Thanksgiving Day (markets close at 1:00pm)"),
            ("2024-12-24", "Christmas Eve (markets close at 1:00pm)"),
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "New Year's Day"),
            ("2025-01-09", "National Day of Mourning for former President Jimmy Carter"),
            ("2025-01-20", "Martin Luther King Jr. Day"),
            ("2025-02-17", "Washington's Birthday"),
            ("2025-04-18", "Good Friday"),
            ("2025-05-26", "Memorial Day"),
            ("2025-06-19", "Juneteenth National Independence Day"),
            ("2025-07-04", "Independence Day"),
            ("2025-09-01", "Labor Day"),
            ("2025-11-27", "Thanksgiving Day"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_half_day_2025(self):
        self.assertHalfDayHolidaysInYear(
            2025,
            ("2025-07-03", "Day before Independence Day (markets close at 1:00pm)"),
            ("2025-11-28", "Day after Thanksgiving Day (markets close at 1:00pm)"),
            ("2025-12-24", "Christmas Eve (markets close at 1:00pm)"),
        )
