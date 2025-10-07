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
    FEB,
    MAR,
    APR,
    MAY,
    JUN,
    JUL,
    SEP,
    OCT,
    NOV,
    DEC,
    WED,
    SAT,
    SUN,
    _timedelta,
)
from holidays.financial.ny_stock_exchange import NewYorkStockExchange, XNYS, NYSE
from tests.common import CommonFinancialTests


class TestNewYorkStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(NewYorkStockExchange)

    def test_market_aliases(self):
        self.assertAliases(NewYorkStockExchange, XNYS, NYSE)

    def test_no_holidays(self):
        self.assertNoHolidays(NewYorkStockExchange(years=1862))

    def test_new_years_day(self):
        for dt in (
            date(1900, JAN, 1),
            date(1930, JAN, 1),
            date(1950, JAN, 2),
            date(1999, JAN, 1),
            date(2010, JAN, 1),
            date(2018, JAN, 1),
            date(2019, JAN, 1),
            date(2020, JAN, 1),
            date(2021, JAN, 1),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))
            self.assertNoHoliday(_timedelta(dt, +7))

        # no observed on previous year Dec 31
        for dt in (
            date(1994, JAN, 1),
            date(2000, JAN, 1),
            date(2005, JAN, 1),
            date(2011, JAN, 1),
            date(2022, JAN, 1),
        ):
            self.assertNoHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))

    def test_martin_luther_king_jr_day(self):
        for dt in (
            date(1999, JAN, 18),
            date(2000, JAN, 17),
            date(2010, JAN, 18),
            date(2018, JAN, 15),
            date(2019, JAN, 21),
            date(2020, JAN, 20),
            date(2021, JAN, 18),
            date(2022, JAN, 17),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))
            self.assertNoHoliday(_timedelta(dt, +7))
            self.assertNoHoliday(_timedelta(dt, -7))

        self.assertNoHoliday("1997-01-20", "1985-01-21")

    def test_lincolns_birthday(self):
        for dt in (
            date(1900, FEB, 12),
            date(1930, FEB, 12),
            date(1953, FEB, 12),
            date(1968, FEB, 12),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))
            self.assertNoHoliday(_timedelta(dt, +7))
            self.assertNoHoliday(_timedelta(dt, -7))

        self.assertNoHoliday(
            "1954-02-12",
            "1967-02-10",
            "1967-02-11",
            "1967-02-12",
            "1967-02-13",
            "1969-02-12",
            "2015-02-12",
        )

    def test_washingtons_birthday(self):
        for dt in (
            date(1900, FEB, 22),
            date(1930, FEB, 21),
            date(1950, FEB, 22),
            date(1960, FEB, 22),
            date(1965, FEB, 22),
            date(1970, FEB, 23),
            date(1971, FEB, 15),
            date(1999, FEB, 15),
            date(2000, FEB, 21),
            date(2010, FEB, 15),
            date(2018, FEB, 19),
            date(2019, FEB, 18),
            date(2020, FEB, 17),
            date(2021, FEB, 15),
            date(2022, FEB, 21),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))
            self.assertNoHoliday(_timedelta(dt, +7))
            self.assertNoHoliday(_timedelta(dt, -7))

    def test_good_friday(self):
        for dt in (
            date(1900, APR, 13),
            date(1901, APR, 5),
            date(1902, MAR, 28),
            date(1999, APR, 2),
            date(2000, APR, 21),
            date(2010, APR, 2),
            date(2018, MAR, 30),
            date(2019, APR, 19),
            date(2020, APR, 10),
            date(2021, APR, 2),
            date(2022, APR, 15),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))
            self.assertNoHoliday(_timedelta(dt, +7))
            self.assertNoHoliday(_timedelta(dt, -7))

    def test_memorial_day(self):
        for dt in (
            date(1901, MAY, 30),
            date(1902, MAY, 30),
            date(1930, MAY, 30),
            date(1950, MAY, 30),
            date(1960, MAY, 30),
            date(1965, MAY, 31),
            date(1971, MAY, 31),
            date(1999, MAY, 31),
            date(2000, MAY, 29),
            date(2010, MAY, 31),
            date(2018, MAY, 28),
            date(2019, MAY, 27),
            date(2020, MAY, 25),
            date(2021, MAY, 31),
            date(2022, MAY, 30),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))
            self.assertNoHoliday(_timedelta(dt, +7))
            self.assertNoHoliday(_timedelta(dt, -7))

        self.assertNoHoliday("1872-05-30")

    def test_flag_day(self):
        for dt in (
            date(1916, JUN, 14),
            date(1934, JUN, 14),
            date(1935, JUN, 14),
            date(1936, JUN, 15),
            date(1941, JUN, 13),
            date(1953, JUN, 15),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))
            self.assertNoHoliday(_timedelta(dt, +7))
            self.assertNoHoliday(_timedelta(dt, -7))

        self.assertNoHoliday(
            "1954-06-14",
            "1967-06-14",
            "2022-06-14",
        )

    def test_juneteenth_national_independence_day(self):
        for dt in (
            date(2022, JUN, 20),
            date(2023, JUN, 19),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))
            self.assertNoHoliday(_timedelta(dt, +7))
            self.assertNoHoliday(_timedelta(dt, -7))

        self.assertNoHoliday("1954-06-18", "1967-06-19", "2021-06-18")

    def test_labor_day(self):
        for dt in (
            date(1887, SEP, 5),
            date(1901, SEP, 2),
            date(1902, SEP, 1),
            date(1950, SEP, 4),
            date(1999, SEP, 6),
            date(2000, SEP, 4),
            date(2010, SEP, 6),
            date(2018, SEP, 3),
            date(2019, SEP, 2),
            date(2020, SEP, 7),
            date(2021, SEP, 6),
            date(2022, SEP, 5),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))
            self.assertNoHoliday(_timedelta(dt, +7))
            self.assertNoHoliday(_timedelta(dt, -7))

        self.assertNoHoliday("1886-09-6")

    def test_columbus_day(self):
        for dt in (
            date(1909, OCT, 12),
            date(1915, OCT, 12),
            date(1920, OCT, 12),
            date(1935, OCT, 11),
            date(1945, OCT, 12),
            date(1953, OCT, 12),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))
            self.assertNoHoliday(_timedelta(dt, +7))
            self.assertNoHoliday(_timedelta(dt, -7))

        self.assertNoHoliday("1908-10-12", "1954-10-12", "2022-10-12")

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
        for dt in (
            date(1918, NOV, 11),
            date(1921, NOV, 11),
            date(1934, NOV, 12),
            date(1938, NOV, 11),
            date(1942, NOV, 11),
            date(1946, NOV, 11),
            date(1950, NOV, 10),
            date(1953, NOV, 11),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))
            self.assertNoHoliday(_timedelta(dt, +7))
            self.assertNoHoliday(_timedelta(dt, -7))

        self.assertNoHoliday(
            "1917-11-12",
            "1919-11-11",
            "1920-11-11",
            "1922-11-10",
            "1933-11-10",
            "1954-11-11",
            "2021-11-11",
            "2022-11-11",
        )

    def test_thanksgiving_day(self):
        for dt in (
            date(1901, NOV, 28),
            date(1902, NOV, 27),
            date(1950, NOV, 23),
            date(1999, NOV, 25),
            date(2000, NOV, 23),
            date(2010, NOV, 25),
            date(2018, NOV, 22),
            date(2019, NOV, 28),
            date(2020, NOV, 26),
            date(2021, NOV, 25),
            date(2022, NOV, 24),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))
            self.assertNoHoliday(_timedelta(dt, +7))
            self.assertNoHoliday(_timedelta(dt, -7))

    def test_christmas_day(self):
        for dt in (
            date(1901, DEC, 25),
            date(1902, DEC, 25),
            date(1950, DEC, 25),
            date(1999, DEC, 24),
            date(2000, DEC, 25),
            date(2010, DEC, 24),
            date(2018, DEC, 25),
            date(2019, DEC, 25),
            date(2020, DEC, 25),
            date(2021, DEC, 24),
            date(2022, DEC, 26),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))
            self.assertNoHoliday(_timedelta(dt, -7))

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

        def _make_special_holiday_list(begin, end, *, days=None, weekends=False):
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

    def test_all_modern_holidays_present(self):
        self.assertHolidays(
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
