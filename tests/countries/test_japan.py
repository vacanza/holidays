#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from holidays.countries.japan import Japan, JP, JPN
from tests.common import TestCase


class TestJapan(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Japan)

    def test_country_aliases(self):
        self.assertCountryAliases(Japan, JP, JPN)

    def test_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            Japan(years=[1945])
        with self.assertRaises(NotImplementedError):
            Japan(years=[2100])

    def test_new_years_day(self):
        for year in range(1949, 2050):
            self.assertIn(date(year, 1, 1), self.holidays)

    def test_coming_of_age(self):
        for year in range(1949, 2000):
            self.assertIn(date(year, 1, 15), self.holidays)
        for dt in (
            (2000, 1, 10),
            (2001, 1, 8),
            (2002, 1, 14),
            (2003, 1, 13),
            (2004, 1, 12),
            (2005, 1, 10),
            (2006, 1, 9),
            (2007, 1, 8),
            (2008, 1, 14),
            (2009, 1, 12),
            (2010, 1, 11),
            (2011, 1, 10),
            (2012, 1, 9),
            (2013, 1, 14),
            (2014, 1, 13),
            (2015, 1, 12),
            (2016, 1, 11),
            (2017, 1, 9),
            (2018, 1, 8),
            (2019, 1, 14),
            (2020, 1, 13),
            (2021, 1, 11),
            (2022, 1, 10),
            (2023, 1, 9),
            (2024, 1, 8),
            (2025, 1, 13),
            (2026, 1, 12),
            (2027, 1, 11),
            (2028, 1, 10),
            (2029, 1, 8),
            (2030, 1, 14),
            (2031, 1, 13),
            (2032, 1, 12),
            (2033, 1, 10),
            (2034, 1, 9),
            (2035, 1, 8),
            (2036, 1, 14),
            (2037, 1, 12),
            (2038, 1, 11),
            (2039, 1, 10),
            (2040, 1, 9),
            (2041, 1, 14),
            (2042, 1, 13),
            (2043, 1, 12),
            (2044, 1, 11),
            (2045, 1, 9),
            (2046, 1, 8),
            (2047, 1, 14),
            (2048, 1, 13),
            (2049, 1, 11),
            (2050, 1, 10),
        ):
            self.assertIn(date(*dt), self.holidays)

        self.assertNotIn(date(2000, 1, 15), self.holidays)
        self.assertNotIn(date(2017, 1, 15), self.holidays)
        self.assertNotIn(date(2030, 1, 15), self.holidays)

    def test_foundation_day(self):
        self.assertNotIn(date(1949, 2, 11), self.holidays)
        self.assertNotIn(date(1966, 2, 11), self.holidays)
        for year in range(1969, 2051):
            self.assertIn(date(year, 2, 11), self.holidays)

    def test_vernal_equinox_day(self):
        for dt in (
            (1949, 3, 21),
            (1950, 3, 21),
            (1951, 3, 21),
            (1952, 3, 21),
            (1953, 3, 21),
            (1954, 3, 21),
            (1955, 3, 21),
            (1956, 3, 21),
            (1957, 3, 21),
            (1958, 3, 21),
            (1959, 3, 21),
            (1960, 3, 20),
            (1961, 3, 21),
            (1962, 3, 21),
            (1963, 3, 21),
            (1964, 3, 20),
            (1965, 3, 21),
            (1966, 3, 21),
            (1967, 3, 21),
            (1968, 3, 20),
            (1969, 3, 21),
            (1970, 3, 21),
            (1971, 3, 21),
            (1972, 3, 20),
            (1973, 3, 21),
            (1974, 3, 21),
            (1975, 3, 21),
            (1976, 3, 20),
            (1977, 3, 21),
            (1978, 3, 21),
            (1979, 3, 21),
            (1980, 3, 20),
            (1981, 3, 21),
            (1982, 3, 21),
            (1983, 3, 21),
            (1984, 3, 20),
            (1985, 3, 21),
            (1986, 3, 21),
            (1987, 3, 21),
            (1988, 3, 20),
            (1989, 3, 21),
            (1990, 3, 21),
            (1991, 3, 21),
            (1992, 3, 20),
            (1993, 3, 20),
            (1994, 3, 21),
            (1995, 3, 21),
            (1996, 3, 20),
            (1997, 3, 20),
            (1998, 3, 21),
            (1999, 3, 21),
            (2000, 3, 20),
            (2001, 3, 20),
            (2002, 3, 21),
            (2003, 3, 21),
            (2004, 3, 20),
            (2005, 3, 20),
            (2006, 3, 21),
            (2007, 3, 21),
            (2008, 3, 20),
            (2009, 3, 20),
            (2010, 3, 21),
            (2011, 3, 21),
            (2012, 3, 20),
            (2013, 3, 20),
            (2014, 3, 21),
            (2015, 3, 21),
            (2016, 3, 20),
            (2017, 3, 20),
            (2018, 3, 21),
            (2019, 3, 21),
            (2020, 3, 20),
            (2021, 3, 20),
            (2022, 3, 21),
            (2023, 3, 21),
            (2024, 3, 20),
            (2025, 3, 20),
            (2026, 3, 20),
            (2027, 3, 21),
            (2028, 3, 20),
            (2029, 3, 20),
            (2030, 3, 20),
            (2031, 3, 21),
            (2032, 3, 20),
            (2033, 3, 20),
            (2034, 3, 20),
            (2035, 3, 21),
            (2036, 3, 20),
            (2037, 3, 20),
            (2038, 3, 20),
            (2039, 3, 21),
            (2040, 3, 20),
            (2041, 3, 20),
            (2042, 3, 20),
            (2043, 3, 21),
            (2044, 3, 20),
            (2045, 3, 20),
            (2046, 3, 20),
            (2047, 3, 21),
            (2048, 3, 20),
            (2049, 3, 20),
            (2050, 3, 20),
            (2051, 3, 21),
            (2052, 3, 20),
            (2055, 3, 21),
            (2056, 3, 20),
            (2092, 3, 19),
            (2093, 3, 20),
            (2096, 3, 19),
            (2097, 3, 20),
        ):
            self.assertIn(date(*dt), self.holidays)
        self.assertIn(date(2092, 3, 19), self.holidays)

    def test_showa_day(self):
        for year in range(1949, 2007):
            self.assertIn(date(year, 4, 29), self.holidays)
            self.assertNotEqual(self.holidays[date(year, 4, 29)], "昭和の日")
        for year in range(2007, 2051):
            self.assertIn(date(year, 4, 29), self.holidays)
            self.assertEqual(self.holidays[date(year, 4, 29)], "昭和の日")

    def test_constitution_memorial_day(self):
        for year in range(1949, 2051):
            self.assertIn(date(year, 5, 3), self.holidays)
            self.assertEqual(self.holidays[date(year, 5, 3)], "憲法記念日")

    def test_greenery_day(self):
        for year in range(1949, 1989):
            self.assertIn(date(year, 4, 29), self.holidays)
            self.assertNotIn(self.holidays[date(year, 4, 29)], "みどりの日")
        for year in range(1989, 2007):
            self.assertIn(date(year, 4, 29), self.holidays)
            self.assertEqual(self.holidays[date(year, 4, 29)], "みどりの日")
        for year in range(2007, 2051):
            self.assertIn(date(year, 5, 4), self.holidays)
            self.assertEqual(self.holidays[date(year, 5, 4)], "みどりの日")

    def test_national_holiday(self):
        for year in (
            1988,
            1989,
            1990,
            1991,
            1993,
            1994,
            1995,
            1996,
            1999,
            2000,
            2001,
            2002,
            2004,
            2005,
            2006,
        ):
            self.assertIn(date(year, 5, 4), self.holidays)
            self.assertEqual(self.holidays[date(year, 5, 4)], "国民の休日")

        for dt in (
            (2009, 9, 22),
            (2015, 9, 22),
            (2026, 9, 22),
            (2032, 9, 21),
            (2037, 9, 22),
            (2043, 9, 22),
            (2049, 9, 21),
        ):
            self.assertIn(date(*dt), self.holidays)
            self.assertEqual(self.holidays[date(*dt)], "国民の休日")

    def test_childrens_day(self):
        for year in range(1949, 2051):
            self.assertIn(date(year, 5, 5), self.holidays)
            self.assertEqual(self.holidays[date(year, 5, 5)], "こどもの日")

    def test_marine_day(self):
        for dt in (
            (1996, 7, 20),
            (1997, 7, 20),
            (1998, 7, 20),
            (1999, 7, 20),
            (2000, 7, 20),
            (2001, 7, 20),
            (2002, 7, 20),
            (2003, 7, 21),
            (2004, 7, 19),
            (2005, 7, 18),
            (2006, 7, 17),
            (2007, 7, 16),
            (2008, 7, 21),
            (2009, 7, 20),
            (2010, 7, 19),
            (2011, 7, 18),
            (2012, 7, 16),
            (2013, 7, 15),
            (2014, 7, 21),
            (2015, 7, 20),
            (2016, 7, 18),
            (2017, 7, 17),
            (2018, 7, 16),
            (2019, 7, 15),
            (2020, 7, 23),
            (2021, 7, 22),
            (2022, 7, 18),
            (2023, 7, 17),
            (2024, 7, 15),
            (2025, 7, 21),
            (2026, 7, 20),
            (2027, 7, 19),
            (2028, 7, 17),
            (2029, 7, 16),
            (2030, 7, 15),
            (2031, 7, 21),
            (2032, 7, 19),
            (2033, 7, 18),
            (2034, 7, 17),
            (2035, 7, 16),
            (2036, 7, 21),
            (2037, 7, 20),
            (2038, 7, 19),
            (2039, 7, 18),
            (2040, 7, 16),
            (2041, 7, 15),
            (2042, 7, 21),
            (2043, 7, 20),
            (2044, 7, 18),
            (2045, 7, 17),
            (2046, 7, 16),
            (2047, 7, 15),
            (2048, 7, 20),
            (2049, 7, 19),
            (2050, 7, 18),
        ):
            self.assertIn(date(*dt), self.holidays)
            self.assertEqual(self.holidays[date(*dt)], "海の日")
        self.assertNotIn(date(1950, 7, 20), self.holidays)

    def test_mountain_day(self):
        for year in range(1949, 2016):
            self.assertNotIn(date(year, 8, 11), self.holidays)
        for year in range(2016, 2051):
            if year == 2020:
                self.assertIn(date(year, 8, 10), self.holidays)
                self.assertEqual(self.holidays[date(year, 8, 10)], "山の日")
            elif year == 2021:
                self.assertIn(date(year, 8, 8), self.holidays)
                self.assertEqual(self.holidays[date(year, 8, 8)], "山の日")
            else:
                self.assertIn(date(year, 8, 11), self.holidays)
                self.assertEqual(self.holidays[date(year, 8, 11)], "山の日")

    def test_respect_for_the_aged_day(self):
        for year in range(1949, 1966):
            self.assertNotIn(date(year, 9, 15), self.holidays)
        for year in range(1966, 2004):
            self.assertIn(date(year, 9, 15), self.holidays)
            self.assertEqual(self.holidays[date(year, 9, 15)], "敬老の日")
        for dt in (
            (2004, 9, 20),
            (2005, 9, 19),
            (2006, 9, 18),
            (2007, 9, 17),
            (2008, 9, 15),
            (2009, 9, 21),
            (2010, 9, 20),
            (2011, 9, 19),
            (2012, 9, 17),
            (2013, 9, 16),
            (2014, 9, 15),
            (2015, 9, 21),
            (2016, 9, 19),
            (2017, 9, 18),
            (2018, 9, 17),
            (2019, 9, 16),
            (2020, 9, 21),
            (2021, 9, 20),
            (2022, 9, 19),
            (2023, 9, 18),
            (2024, 9, 16),
            (2025, 9, 15),
            (2026, 9, 21),
            (2027, 9, 20),
            (2028, 9, 18),
            (2029, 9, 17),
            (2030, 9, 16),
            (2031, 9, 15),
            (2032, 9, 20),
            (2033, 9, 19),
            (2034, 9, 18),
            (2035, 9, 17),
            (2036, 9, 15),
            (2037, 9, 21),
            (2038, 9, 20),
            (2039, 9, 19),
            (2040, 9, 17),
            (2041, 9, 16),
            (2042, 9, 15),
            (2043, 9, 21),
            (2044, 9, 19),
            (2045, 9, 18),
            (2046, 9, 17),
            (2047, 9, 16),
            (2048, 9, 21),
            (2049, 9, 20),
            (2050, 9, 19),
        ):
            self.assertIn(date(*dt), self.holidays)
            self.assertEqual(self.holidays[date(*dt)], "敬老の日")

    def test_autumnal_equinox_day(self):
        for dt in (
            (1949, 9, 23),
            (1950, 9, 23),
            (1951, 9, 24),
            (1952, 9, 23),
            (1953, 9, 23),
            (1954, 9, 23),
            (1955, 9, 24),
            (1956, 9, 23),
            (1957, 9, 23),
            (1958, 9, 23),
            (1959, 9, 24),
            (1960, 9, 23),
            (1961, 9, 23),
            (1962, 9, 23),
            (1963, 9, 24),
            (1964, 9, 23),
            (1965, 9, 23),
            (1966, 9, 23),
            (1967, 9, 24),
            (1968, 9, 23),
            (1969, 9, 23),
            (1970, 9, 23),
            (1971, 9, 24),
            (1972, 9, 23),
            (1973, 9, 23),
            (1974, 9, 23),
            (1975, 9, 24),
            (1976, 9, 23),
            (1977, 9, 23),
            (1978, 9, 23),
            (1979, 9, 24),
            (1980, 9, 23),
            (1981, 9, 23),
            (1982, 9, 23),
            (1983, 9, 23),
            (1984, 9, 23),
            (1985, 9, 23),
            (1986, 9, 23),
            (1987, 9, 23),
            (1988, 9, 23),
            (1989, 9, 23),
            (1990, 9, 23),
            (1991, 9, 23),
            (1992, 9, 23),
            (1993, 9, 23),
            (1994, 9, 23),
            (1995, 9, 23),
            (1996, 9, 23),
            (2021, 9, 23),
            (2024, 9, 22),
            (2027, 9, 23),
            (2056, 9, 22),
            (2068, 9, 22),
            (2087, 9, 23),
            (2089, 9, 22),
        ):
            self.assertIn(date(*dt), self.holidays)
            self.assertEqual(self.holidays[date(*dt)], "秋分の日")

    def test_health_and_sports_day(self):
        for year in range(1949, 1966):
            self.assertNotIn(date(year, 10, 10), self.holidays)
        for year in range(1966, 2000):
            self.assertIn(date(year, 10, 10), self.holidays)
            self.assertEqual(self.holidays[date(year, 10, 10)], "体育の日")
        for dt in (
            (2000, 10, 9),
            (2001, 10, 8),
            (2002, 10, 14),
            (2003, 10, 13),
            (2004, 10, 11),
            (2005, 10, 10),
            (2006, 10, 9),
            (2007, 10, 8),
            (2008, 10, 13),
            (2009, 10, 12),
            (2010, 10, 11),
            (2011, 10, 10),
            (2012, 10, 8),
            (2013, 10, 14),
            (2014, 10, 13),
            (2015, 10, 12),
            (2016, 10, 10),
            (2017, 10, 9),
            (2018, 10, 8),
            (2019, 10, 14),
        ):
            self.assertIn(date(*dt), self.holidays)
            self.assertEqual(self.holidays[date(*dt)], "体育の日")
        for dt in (
            (2020, 7, 24),
            (2021, 7, 23),
            (2022, 10, 10),
            (2023, 10, 9),
            (2024, 10, 14),
            (2025, 10, 13),
            (2026, 10, 12),
            (2027, 10, 11),
            (2028, 10, 9),
            (2029, 10, 8),
            (2030, 10, 14),
            (2031, 10, 13),
            (2032, 10, 11),
            (2033, 10, 10),
            (2034, 10, 9),
            (2035, 10, 8),
            (2036, 10, 13),
            (2037, 10, 12),
            (2038, 10, 11),
            (2039, 10, 10),
            (2040, 10, 8),
            (2041, 10, 14),
            (2042, 10, 13),
            (2043, 10, 12),
            (2044, 10, 10),
            (2045, 10, 9),
            (2046, 10, 8),
            (2047, 10, 14),
            (2048, 10, 12),
            (2049, 10, 11),
            (2050, 10, 10),
        ):
            self.assertIn(date(*dt), self.holidays)
            self.assertEqual(self.holidays[date(*dt)], "スポーツの日")
        self.assertNotIn(date(2000, 10, 10), self.holidays)

    def test_culture_day(self):
        for year in range(1949, 2050):
            self.assertIn(date(year, 11, 3), self.holidays)
            self.assertEqual(self.holidays[date(year, 11, 3)], "文化の日")

    def test_labour_thanks_giving_day(self):
        for year in range(1949, 2050):
            self.assertIn(date(year, 11, 23), self.holidays)
            self.assertEqual(self.holidays[date(year, 11, 23)], "勤労感謝の日")

    def test_emperors_birthday(self):
        for year in range(1949, 1989):
            self.assertIn(date(year, 4, 29), self.holidays)
            self.assertEqual(self.holidays[date(year, 4, 29)], "天皇誕生日")
        for year in range(1989, 2019):
            self.assertIn(date(year, 12, 23), self.holidays)
            self.assertEqual(self.holidays[date(year, 12, 23)], "天皇誕生日")
        for year in range(2020, 2051):
            self.assertIn(date(year, 2, 23), self.holidays)
            self.assertEqual(self.holidays[date(year, 2, 23)], "天皇誕生日")
        self.assertNotIn(date(2019, 12, 23), self.holidays)

    def test_showa_emperor_holidays(self):
        self.assertIn(date(1989, 2, 24), self.holidays)

    def test_heisei_emperor_holidays(self):
        self.assertIn(date(1959, 4, 10), self.holidays)
        self.assertIn(date(1990, 11, 12), self.holidays)

    def test_reiwa_emperor_holidays(self):
        self.assertIn(date(1993, 6, 9), self.holidays)
        self.assertIn(date(2019, 4, 30), self.holidays)
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 5, 2), self.holidays)
        self.assertIn(date(2019, 10, 22), self.holidays)

    def test_observed_holidays(self):
        no_observed = Japan(observed=False)
        hol_list = (
            # 振替休日
            (1973, 4, 30),
            (1973, 9, 24),
            (1974, 5, 6),
            (1974, 9, 16),
            (1974, 11, 4),
            (1975, 11, 24),
            (1976, 10, 11),
            (1978, 1, 2),
            (1978, 1, 16),
            (1979, 2, 12),
            (1979, 4, 30),
            (1980, 11, 24),
            (1981, 5, 4),
            (1982, 3, 22),
            (1982, 10, 11),
            (1984, 1, 2),
            (1984, 1, 16),
            (1984, 4, 30),
            (1984, 9, 24),
            (1985, 5, 6),
            (1985, 9, 16),
            (1985, 11, 4),
            (1986, 11, 24),
            (1987, 5, 4),
            (1988, 3, 21),
            (1989, 1, 2),
            (1989, 1, 16),
            (1990, 2, 12),
            (1990, 4, 30),
            (1990, 9, 24),
            (1990, 12, 24),
            (1991, 5, 6),
            (1991, 9, 16),
            (1991, 11, 4),
            (1992, 5, 4),
            (1993, 10, 11),
            (1995, 1, 2),
            (1995, 1, 16),
            (1996, 2, 12),
            (1996, 5, 6),
            (1996, 9, 16),
            (1996, 11, 4),
            (1997, 7, 21),
            (1997, 11, 24),
            (1998, 5, 4),
            (1999, 3, 22),
            (1999, 10, 11),
            (2001, 2, 12),
            (2001, 4, 30),
            (2001, 9, 24),
            (2001, 12, 24),
            (2002, 5, 6),
            (2002, 9, 16),
            (2002, 11, 4),
            (2003, 11, 24),
            (2005, 3, 21),
            (2006, 1, 2),
            (2007, 2, 12),
            (2007, 4, 30),
            (2007, 9, 24),
            (2007, 12, 24),
            (2008, 5, 6),
            (2008, 11, 24),
            (2009, 5, 6),
            (2010, 3, 22),
            (2012, 1, 2),
            (2012, 4, 30),
            (2012, 12, 24),
            (2013, 5, 6),
            (2013, 11, 4),
            (2014, 5, 6),
            (2014, 11, 24),
            (2015, 5, 6),
            (2016, 3, 21),
            (2017, 1, 2),
            (2018, 2, 12),
            (2018, 4, 30),
            (2018, 9, 24),
            (2018, 12, 24),
            (2019, 5, 6),
            (2019, 8, 12),
            (2019, 11, 4),
            (2020, 2, 24),
            (2020, 5, 6),
            (2023, 1, 2),
            (2024, 2, 12),
            (2024, 5, 6),
            (2024, 8, 12),
            (2024, 9, 23),
            (2024, 11, 4),
            (2025, 2, 24),
            (2025, 5, 6),
            (2025, 11, 24),
            (2026, 5, 6),
            (2027, 3, 22),
            (2029, 2, 12),
            (2029, 4, 30),
            (2029, 9, 24),
            (2030, 5, 6),
            (2030, 8, 12),
            (2030, 11, 4),
            (2031, 2, 24),
            (2031, 5, 6),
            (2031, 11, 24),
            (2033, 3, 21),
            (2034, 1, 2),
            (2035, 2, 12),
            (2035, 4, 30),
            (2035, 9, 24),
            (2036, 5, 6),
            (2036, 11, 24),
            (2037, 5, 6),
            (2040, 1, 2),
            (2040, 4, 30),
            (2041, 5, 6),
            (2041, 8, 12),
            (2041, 11, 4),
            (2042, 2, 24),
            (2042, 5, 6),
            (2042, 11, 24),
            (2043, 5, 6),
            (2044, 3, 21),
            (2045, 1, 2),
            (2046, 2, 12),
            (2046, 4, 30),
            (2046, 9, 24),
            (2047, 5, 6),
            (2047, 8, 12),
            (2047, 11, 4),
            (2048, 2, 24),
            (2048, 5, 6),
            (2050, 3, 21),
            # 国民の休日
            (2019, 4, 30),
            (2019, 5, 2),
            (2026, 9, 22),
            (2032, 9, 21),
            (2037, 9, 22),
        )
        for dt in hol_list:
            self.assertIn(date(*dt), self.holidays)
            self.assertNotIn(date(*dt), no_observed)

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                jp = Japan(language=language)
                self.assertEqual(jp["2022-01-01"], "元日")
                self.assertEqual(jp["2022-11-23"], "勤労感謝の日")

        run_tests((Japan.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Japan.default_language,))

    # def test_l10n_en_us(self):
    #     en_us = "en_US"

    #     pl = Poland(language=en_us)
    #     self.assertEqual(
    #         pl["2018-11-12"],
    #         "National Independence Day - 100th anniversary",
    #     )
    #     self.assertEqual(pl["2022-01-01"], "New Year's Day")
    #     self.assertEqual(pl["2022-12-25"], "Christmas (Day 1)")

    #     self.set_language(en_us)
    #     for language in (None, en_us, "invalid"):
    #         pl = Poland(language=language)
    #         self.assertEqual(pl["2022-01-01"], "New Year's Day")
    #         self.assertEqual(pl["2022-12-25"], "Christmas (Day 1)")
