#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date, timedelta

from dateutil.relativedelta import WE, relativedelta

import holidays
from holidays.constants import (APR, AUG, DEC, FEB, JAN, JUL, JUN, MAR, MAY,
                                NOV, OCT, SEP)


class TestNewYorkStockExchange(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.NewYorkStockExchange()

    def test_new_years(self):
        for dt in [
            date(1900, JAN, 1),
            date(1930, JAN, 1),
            date(1950, JAN, 2),
            date(1999, JAN, 1),
            date(1999, DEC, 31),
            date(2010, JAN, 1),
            date(2018, JAN, 1),
            date(2019, JAN, 1),
            date(2020, JAN, 1),
            date(2021, JAN, 1),
            date(2021, DEC, 31),
            date(2027, DEC, 31),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)

    def test_mlk(self):
        for dt in [
            date(1999, JAN, 18),
            date(2000, JAN, 17),
            date(2010, JAN, 18),
            date(2018, JAN, 15),
            date(2019, JAN, 21),
            date(2020, JAN, 20),
            date(2021, JAN, 18),
            date(2022, JAN, 17),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

        for dt in [
            date(1997, JAN, 20),
            date(1985, JAN, 21),
        ]:
            self.assertNotIn(dt, self.holidays)

    def test_lincoln(self):
        for dt in [
            date(1900, FEB, 12),
            date(1930, FEB, 12),
            date(1953, FEB, 12),
            date(1968, FEB, 12),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

        for dt in [
            date(1954, FEB, 12),
            date(1967, FEB, 10),
            date(1967, FEB, 11),
            date(1967, FEB, 12),
            date(1967, FEB, 13),
            date(1969, FEB, 12),
            date(2015, FEB, 12),
        ]:
            self.assertNotIn(dt, self.holidays)

    def test_washington(self):
        for dt in [
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
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

    def test_good_friday(self):
        for dt in [
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
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

    def test_memday(self):
        for dt in [
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
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

    def test_flagday(self):
        for dt in [
            date(1916, JUN, 14),
            date(1934, JUN, 14),
            date(1935, JUN, 14),
            date(1936, JUN, 15),
            date(1941, JUN, 13),
            date(1953, JUN, 15),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

        for dt in [
            date(1954, JUN, 14),
            date(1967, JUN, 14),
            date(2022, JUN, 14),
        ]:
            self.assertNotIn(dt, self.holidays)

    def test_juneteenth(self):
        for dt in [
            date(2021, JUN, 18),
            date(2022, JUN, 20),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

        for dt in [
            date(1954, JUN, 18),
            date(1967, JUN, 19),
        ]:
            self.assertNotIn(dt, self.holidays)

    def test_laborday(self):
        for dt in [
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
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

        for dt in [
            date(1886, SEP, 6),
        ]:
            self.assertNotIn(dt, self.holidays)

    def test_columbusday(self):
        for dt in [
            date(1909, OCT, 12),
            date(1915, OCT, 12),
            date(1920, OCT, 12),
            date(1935, OCT, 11),
            date(1945, OCT, 12),
            date(1953, OCT, 12),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

        for dt in [
            date(1908, OCT, 12),
            date(1954, OCT, 12),
            date(2022, OCT, 12),
        ]:
            self.assertNotIn(dt, self.holidays)

    def test_electionday(self):
        for dt in [
            date(1887, NOV, 1),
            date(1901, NOV, 5),
            date(1902, NOV, 4),
            date(1920, NOV, 2),
            date(1935, NOV, 5),
            date(1950, NOV, 7),
            date(1968, NOV, 5),
            date(1972, NOV, 7),
            date(1976, NOV, 2),
            date(1980, NOV, 4),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

        for dt in [
            date(1969, NOV, 4),
            date(1970, NOV, 3),
            date(1971, NOV, 2),
            date(1973, NOV, 6),
            date(1974, NOV, 5),
            date(1975, NOV, 4),
            date(1977, NOV, 1),
            date(1978, NOV, 7),
            date(1979, NOV, 6),
            date(1981, NOV, 3),
            date(2021, NOV, 2),
            date(2022, NOV, 1),
        ]:
            self.assertNotIn(dt, self.holidays)

    def test_veteransday(self):
        for dt in [
            date(1918, NOV, 11),
            date(1921, NOV, 11),
            date(1934, NOV, 12),
            date(1938, NOV, 11),
            date(1942, NOV, 11),
            date(1946, NOV, 11),
            date(1950, NOV, 10),
            date(1953, NOV, 11),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

        for dt in [
            date(1917, NOV, 12),
            date(1919, NOV, 11),
            date(1920, NOV, 11),
            date(1922, NOV, 10),
            date(1933, NOV, 10),
            date(1954, NOV, 11),
            date(2021, NOV, 11),
            date(2022, NOV, 11),
        ]:
            self.assertNotIn(dt, self.holidays)

    def test_thxgiving(self):
        for dt in [
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
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

    def test_christmas_day(self):
        for dt in [
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
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

    def test_special_holidays(self):
        # add to this list as new historical holidays are added
        special_holidays = [
            date(1888, MAR, 12),  # Blizzard of 1888
            date(1888, MAR, 13),  # Blizzard of 1888
            date(1888, NOV, 30),  # Thanksgiving Friday 1888
            date(1889, APR, 29),  # Centennial of Washington Inauguration
            date(1889, APR, 30),  # Centennial of Washington Inauguration
            date(1889, MAY, 1),  # Centennial of Washington Inauguration
            date(1892, OCT, 12),  # Columbian Celebration
            date(1892, OCT, 21),  # Columbian Celebration
            date(1893, APR, 27),  # Columbian Celebration
            date(1897, APR, 27),  # Grant's Birthday
            date(1898, MAY, 4),  # Charter Day
            date(1899, MAY, 29),  # Monday before Decoration Day
            date(1899, JUL, 3),  # Monday before Independence Day
            date(1899, SEP, 29),  # Admiral Dewey Celebration
            date(1900, DEC, 24),  # Christmas Eve
            date(1901, JUL, 5),  # Friday after Independence Day
            date(1901, SEP, 19),  # Funeral of President McKinley
            date(1903, APR, 22),  # Opening of new NYSE building
            date(1917, JUN, 5),  # Draft Registration Day
            date(1918, JAN, 28),  # Heatless Day
            date(1918, FEB, 4),  # Heatless Day
            date(1918, FEB, 11),  # Heatless Day
            date(1918, JUN, 14),  # Heatless Day
            date(1918, SEP, 12),  # Draft Registration Day
            date(1918, NOV, 11),  # Armistice Day
            date(1919, MAR, 25),  # Homecoming Day for 27th Division
            date(1919, MAY, 6),  # Parade Day for 77th Division
            date(1919, SEP, 10),  # Return of General Pershing
            date(1923, AUG, 3),  # Death of President Warren G. Harding
            date(1923, AUG, 10),  # Funeral of President Warren G. Harding
            date(1927, JUN, 13),  # Parade for Colonel Charles Lindbergh
            date(1929, NOV, 29),  # Catch Up Day
            date(1945, AUG, 15),  # V-J Day (WWII)
            date(1945, AUG, 16),  # V-J Day (WWII)
            date(1945, DEC, 24),  # Christmas Eve
            date(1954, DEC, 24),  # Christmas Eve
            date(1956, DEC, 24),  # Christmas Eve
            date(1958, DEC, 26),  # Day after Christmas
            date(1961, MAY, 29),  # Day before Decoration Day
            date(1963, NOV, 25),  # Funeral of President John F. Kennedy
            date(1965, DEC, 24),  # Christmas Eve
            date(1968, APR, 9),  # Day of Mourning for Martin Luther King Jr.
            date(1968, JUL, 5),  # Day after Independence Day
            date(1969, FEB, 10),  # Heavy Snow
            date(1969, MAR, 31),  # Funeral of President Dwight D. Eisenhower
            date(1969, JUL, 21),  # National Participation in Lunar Exploration
            date(1972, DEC, 28),  # Funeral for President Harry S. Truman
            date(1973, JAN, 25),  # Funeral for President Lyndon B. Johnson
            date(1977, JUL, 14),  # Blackout in New Yor City
            date(1994, APR, 27),  # Funeral for President Richard M. Nixon
            date(2001, SEP, 11),  # Closed for Sept 11, 2001 Attacks
            date(2001, SEP, 12),  # Closed for Sept 11, 2001 Attacks
            date(2001, SEP, 13),  # Closed for Sept 11, 2001 Attacks
            date(2001, SEP, 14),  # Closed for Sept 11, 2001 Attacks
            date(
                2004, JUN, 11
            ),  # Day of Mourning for President Ronald W. Reagan
            date(2007, JAN, 2),  # Day of Mourning for President Gerald R. Ford
        ]

        def _make_special_holiday_list(begin, end, days=None, weekends=False):
            _list = []
            for d in (
                begin + timedelta(days=n)
                for n in range((end - begin).days + 1)
            ):
                if not weekends and d.isoweekday() in [6, 7]:
                    continue
                if days is None or d.isoweekday() in days:
                    _list.append(d)
            return _list

        wwi_holidays = _make_special_holiday_list(
            date(1914, JUL, 31), date(1914, NOV, 27)
        )
        oneoff_bank_holidays = _make_special_holiday_list(
            date(1933, MAR, 6), date(1933, MAR, 14)
        )
        paper_crisis_holidays = _make_special_holiday_list(
            date(1968, JUN, 12), date(1968, DEC, 31), days=[WE]
        )
        for dt in (
            special_holidays
            + wwi_holidays
            + oneoff_bank_holidays
            + paper_crisis_holidays
        ):
            self.assertIn(dt, self.holidays)

        # double check that we catch beginning/ending of holiday periods -
        # covers off-by-one errors
        for dt in [
            date(1914, JUL, 31),  # begin WWI holidays
            date(1933, MAR, 6),  # begin oneoff bank holidays
            date(1968, JUN, 12),  # begin paper crisis holidays
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt - timedelta(days=1), self.holidays)

        for dt in [
            date(1914, NOV, 27),  # end WWI holidays
            date(1933, MAR, 14),  # end oneoff bank holidays
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + timedelta(days=1), self.holidays)

    def test_all_modern_holidays_present(self):
        nyse_2021 = holidays.NewYorkStockExchange(years=[2021])
        all_holidays = [
            "New Year's Day",
            "Martin Luther King Jr. Day",
            "Washington's Birthday",
            "Good Friday",
            "Memorial Day",
            "Juneteenth National Independence Day (Observed)",
            "Independence Day (Observed)",
            "Labor Day",
            "Thanksgiving Day",
            "Christmas Day (Observed)",
        ]
        for holiday in all_holidays:
            self.assertIn(holiday, nyse_2021.values())
