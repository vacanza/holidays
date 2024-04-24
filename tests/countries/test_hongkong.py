#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.constants import OPTIONAL
from holidays.countries.hongkong import HongKong, HK, HKG, CHRISTMAS, WINTER_SOLSTICE
from tests.common import CommonCountryTests


class TestHongKong(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HongKong, years=range(1963, 2050), years_non_observed=range(1963, 2050))
        cls.opt_holidays = HongKong(categories=(OPTIONAL,), years=range(1946, 2050))

    def test_country_aliases(self):
        self.assertAliases(HongKong, HK, HKG)

    def test_no_holidays(self):
        self.assertNoHolidays(HongKong(years=1962))
        self.assertNoHolidays(HongKong(categories=(OPTIONAL,), years=1945))

    def test_special_holidays(self):
        self.assertHoliday(
            "1981-07-29",
            "1986-10-22",
            "1997-07-02",
            "2015-09-03",
        )
        self.assertHoliday(
            self.opt_holidays,
            "1981-07-29",
            "1986-10-22",
            "1997-06-28",
            "1997-06-30",
            "1997-07-02",
            "1997-08-18",
            "1997-10-02",
            "1998-08-17",
            "1998-10-02",
            "1999-12-31",
            "2015-09-03",
        )

    def test_first_day_of_january(self):
        name = "The first day of January"
        name_observed = f"{name} (observed)"
        name_following = "The day following the first day of January"

        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1977, 2050)))
        self.assertNoHolidayName(name, range(1963, 1977))
        obs_dt = (
            "1978-01-02",
            "1984-01-02",
            "1989-01-02",
            "1995-01-02",
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(name_observed, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

        exception_years = {
            1950,
            1956,
            1961,
            1967,
            1978,
            1984,
            1989,
            1995,
            2006,
            2012,
            2017,
            2023,
            2034,
            2040,
            2045,
        }
        self.assertHolidayName(
            name,
            self.opt_holidays,
            (f"{year}-01-01" for year in set(range(1946, 2050)).difference(exception_years)),
        )
        self.assertHolidayName(
            name_following, self.opt_holidays, (f"{year}-01-02" for year in exception_years)
        )

    def test_lunar_new_year(self):
        name_eve = "The day preceding Lunar New Year's Day"
        name = "Lunar New Year's Day"
        name_second = "The second day of Lunar New Year"
        name_third = "The third day of Lunar New Year"
        name_fourth = "The fourth day of Lunar New Year"

        self.assertHolidayName(
            name_eve,
            "1983-02-12",
            "1986-02-08",
            "1990-01-26",
            "1991-02-14",
            "1993-01-22",
            "1997-02-06",
            "2000-02-04",
            "2003-01-31",
            "2006-01-28",
            "2007-02-17",
            "2010-02-13",
        )
        self.assertNoHolidayName(name_eve, range(1963, 1983), range(2012, 2050))
        self.assertNoHolidayName(name_eve, self.opt_holidays, range(1946, 1983), range(2012, 2050))

        self.assertHolidayName(
            name,
            "2008-02-07",
            "2009-01-26",
            "2011-02-03",
            "2012-01-23",
            "2014-01-31",
            "2015-02-19",
            "2016-02-08",
            "2017-01-28",
            "2018-02-16",
            "2019-02-05",
            "2020-01-25",
            "2021-02-12",
            "2022-02-01",
            "2024-02-10",
        )
        exception_years = {1983, 1986, 2006, 2007, 2010, 2013, 2023, 2030, 2034, 2037, 2040}
        self.assertHolidayName(name, set(range(1963, 2050)).difference(exception_years))
        self.assertNoHolidayName(name, exception_years)
        self.assertHolidayName(
            name, self.opt_holidays, set(range(1946, 2050)).difference(exception_years)
        )
        self.assertNoHolidayName(name, self.opt_holidays, exception_years)

        self.assertHolidayName(
            name_second,
            "2006-01-30",
            "2007-02-19",
            "2008-02-08",
            "2009-01-27",
            "2010-02-15",
            "2011-02-04",
            "2012-01-24",
            "2013-02-11",
            "2014-02-01",
            "2015-02-20",
            "2016-02-09",
            "2018-02-17",
            "2019-02-06",
            "2021-02-13",
            "2022-02-02",
            "2023-01-23",
        )
        exception_years = {1990, 1993, 2000, 2003, 2017, 2020, 2024, 2027, 2044, 2047}
        self.assertHolidayName(name_second, set(range(1963, 2050)).difference(exception_years))
        self.assertNoHolidayName(name_second, exception_years)
        self.assertHolidayName(
            name_second, self.opt_holidays, set(range(1946, 2050)).difference(exception_years)
        )
        self.assertNoHolidayName(name_second, self.opt_holidays, exception_years)

        self.assertHolidayName(
            name_third,
            "2006-01-31",
            "2007-02-20",
            "2008-02-09",
            "2009-01-28",
            "2010-02-16",
            "2011-02-05",
            "2012-01-25",
            "2013-02-12",
            "2015-02-21",
            "2016-02-10",
            "2017-01-30",
            "2019-02-07",
            "2020-01-27",
            "2022-02-03",
            "2023-01-24",
            "2024-02-12",
        )
        exception_years = {1991, 1997, 2014, 2018, 2021, 2041, 2045, 2048}
        self.assertHolidayName(name_third, set(range(1977, 2050)).difference(exception_years))
        self.assertNoHolidayName(name_third, exception_years, range(1963, 1977))
        self.assertHolidayName(
            name_third, self.opt_holidays, set(range(1968, 2050)).difference(exception_years)
        )
        self.assertNoHolidayName(name_third, self.opt_holidays, exception_years, range(1946, 1968))

        self.assertHolidayName(
            name_fourth,
            "2013-02-13",
            "2014-02-03",
            "2017-01-31",
            "2018-02-19",
            "2020-01-28",
            "2021-02-15",
            "2023-01-25",
            "2024-02-13",
        )
        present_years = {
            2013,
            2014,
            2017,
            2018,
            2020,
            2021,
            2023,
            2024,
            2027,
            2030,
            2034,
            2037,
            2040,
            2041,
            2044,
            2045,
            2047,
            2048,
        }
        self.assertHolidayName(name_fourth, present_years)
        self.assertNoHolidayName(name_fourth, set(range(1963, 2050)).difference(present_years))
        self.assertHolidayName(name_fourth, self.opt_holidays, present_years)
        self.assertNoHolidayName(
            name_fourth, self.opt_holidays, set(range(1946, 2050)).difference(present_years)
        )

    def test_good_friday(self):
        name = "Good Friday"

        self.assertHolidayName(
            name,
            "2028-04-14",
            "2029-03-30",
            "2030-04-19",
            "2031-04-11",
            "2032-03-26",
            "2033-04-15",
            "2034-04-07",
            "2035-03-23",
        )
        self.assertHolidayName(
            name,
            self.opt_holidays,
            "2006-04-14",
            "2007-04-06",
            "2008-03-21",
            "2009-04-10",
            "2010-04-02",
            "2011-04-22",
            "2012-04-06",
            "2013-03-29",
            "2014-04-18",
            "2015-04-03",
            "2016-03-25",
            "2017-04-14",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
        )
        self.assertHolidayName(name, range(2028, 2050))
        self.assertNoHolidayName(name, range(1963, 2028))
        self.assertHolidayName(name, self.opt_holidays, range(1946, 2050))

    def test_holy_saturday(self):
        name = "The day following Good Friday"

        self.assertHolidayName(
            name,
            "2030-04-20",
            "2031-04-12",
            "2032-03-27",
            "2033-04-16",
            "2034-04-08",
            "2035-03-24",
        )
        self.assertHolidayName(
            name,
            self.opt_holidays,
            "2006-04-15",
            "2007-04-07",
            "2008-03-22",
            "2009-04-11",
            "2010-04-03",
            "2011-04-23",
            "2012-04-07",
            "2013-03-30",
            "2014-04-19",
            "2015-04-04",
            "2016-03-26",
            "2017-04-15",
            "2018-03-31",
            "2019-04-20",
            "2020-04-11",
            "2021-04-03",
            "2022-04-16",
            "2023-04-08",
            "2024-03-30",
        )
        self.assertHolidayName(name, range(2030, 2050))
        self.assertNoHolidayName(name, range(1963, 2030))
        self.assertHolidayName(name, self.opt_holidays, range(1946, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        name_following = "The day following Easter Monday"

        self.assertHolidayName(
            name,
            "2026-04-06",
            "2027-03-29",
            "2028-04-17",
            "2029-04-02",
            "2030-04-22",
            "2031-04-14",
            "2032-03-29",
            "2033-04-18",
            "2034-04-10",
            "2035-03-26",
        )
        self.assertHolidayName(
            name,
            self.opt_holidays,
            "2006-04-17",
            "2007-04-09",
            "2008-03-24",
            "2009-04-13",
            "2010-04-05",
            "2011-04-25",
            "2012-04-09",
            "2013-04-01",
            "2014-04-21",
            "2016-03-28",
            "2017-04-17",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
        )
        exception_years = {2015, 2021, 2026}
        self.assertHolidayName(name, range(2026, 2050))
        self.assertNoHolidayName(name, range(1963, 2026))
        self.assertHolidayName(
            name, self.opt_holidays, set(range(1946, 2050)).difference(exception_years)
        )
        self.assertHolidayName(
            name_following,
            self.opt_holidays,
            "2015-04-07",
            "2021-04-06",
            "2026-04-07",
        )

    def test_ching_ming_festival(self):
        name = "Ching Ming Festival"
        name_observed = f"{name} (observed)"
        name_following = "The day following Ching Ming Festival"

        self.assertHolidayName(
            name,
            "2006-04-05",
            "2007-04-05",
            "2008-04-04",
            "2009-04-04",
            "2011-04-05",
            "2012-04-04",
            "2013-04-04",
            "2014-04-05",
            "2016-04-04",
            "2017-04-04",
            "2018-04-05",
            "2019-04-05",
            "2020-04-04",
            "2022-04-05",
            "2023-04-05",
            "2024-04-04",
        )
        obs_dt = (
            "1970-04-06",
            "1976-04-05",
            "1981-04-06",
            "1987-04-06",
            "1998-04-06",
            "2004-04-05",
            "2015-04-06",
            "2021-04-05",
        )
        self.assertHolidayName(name, range(1963, 2050))
        self.assertHolidayName(name_observed, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

        self.assertHolidayName(
            name,
            self.opt_holidays,
            "2006-04-05",
            "2007-04-05",
            "2008-04-04",
            "2009-04-04",
            "2011-04-05",
            "2012-04-04",
            "2013-04-04",
            "2014-04-05",
            "2016-04-04",
            "2017-04-04",
            "2018-04-05",
            "2019-04-05",
            "2020-04-04",
            "2022-04-05",
            "2023-04-05",
            "2024-04-04",
        )
        exception_years = {
            1970,
            1976,
            1981,
            1987,
            1988,
            1998,
            1999,
            2004,
            2010,
            2015,
            2021,
            2026,
            2032,
            2043,
            2049,
        }
        self.assertHolidayName(
            name_following,
            self.opt_holidays,
            "1970-04-06",
            "1976-04-05",
            "1981-04-06",
            "1987-04-06",
            "1988-04-05",
            "1998-04-06",
            "1999-04-06",
            "2004-04-05",
            "2010-04-06",
            "2015-04-06",
            "2021-04-05",
        )
        self.assertHolidayName(
            name, self.opt_holidays, set(range(1968, 2050)).difference(exception_years)
        )
        self.assertNoHolidayName(name, self.opt_holidays, exception_years, range(1946, 1968))

    def test_birthday_of_buddha(self):
        name = "The Birthday of the Buddha"
        name_observed = f"{name} (observed)"
        name_following = "The day following the Birthday of the Buddha"

        self.assertHolidayName(
            name,
            "2022-05-08",
            "2023-05-26",
            "2024-05-15",
            "2025-05-04",
            "2026-05-24",
            "2027-05-13",
            "2028-05-02",
            "2029-05-20",
            "2030-05-09",
            "2031-05-28",
            "2032-05-16",
            "2033-05-06",
            "2034-05-25",
            "2035-05-15",
        )
        obs_dt = (
            "2022-05-09",
            "2025-05-05",
        )
        self.assertHolidayName(name, range(2022, 2050))
        self.assertHolidayName(name_observed, obs_dt)
        self.assertNoHolidayName(name, range(1963, 2022))
        self.assertNoNonObservedHoliday(obs_dt)

        self.assertHolidayName(
            name,
            self.opt_holidays,
            "1999-05-22",
            "2000-05-11",
            "2006-05-05",
            "2007-05-24",
            "2008-05-12",
            "2009-05-02",
            "2010-05-21",
            "2011-05-10",
            "2012-04-28",
            "2013-05-17",
            "2014-05-06",
            "2015-05-25",
            "2016-05-14",
            "2017-05-03",
            "2018-05-22",
            "2020-04-30",
            "2021-05-19",
            "2023-05-26",
            "2024-05-15",
        )
        exception_years = {2002, 2005, 2019, 2022, 2025, 2026, 2029, 2032, 2046, 2049}
        self.assertHolidayName(
            name_following,
            self.opt_holidays,
            "2002-05-20",
            "2005-05-16",
            "2019-05-13",
            "2022-05-09",
            "2025-05-05",
        )
        self.assertHolidayName(
            name, self.opt_holidays, set(range(1999, 2050)).difference(exception_years)
        )
        self.assertNoHolidayName(name, self.opt_holidays, exception_years, range(1946, 1999))

    def test_labour_day(self):
        name = "Labour Day"
        name_observed = f"{name} (observed)"
        name_following = "The day following Labour Day"

        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1999, 2050)))
        self.assertNoHolidayName(name, range(1963, 1999))
        obs_dt = (
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(name_observed, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

        exception_years = {2005, 2011, 2016, 2022, 2033, 2039, 2044}
        self.assertHolidayName(
            name,
            self.opt_holidays,
            (f"{year}-05-01" for year in set(range(1999, 2050)).difference(exception_years)),
        )
        self.assertHolidayName(
            name_following, self.opt_holidays, (f"{year}-05-02" for year in exception_years)
        )
        self.assertNoHolidayName(name, self.opt_holidays, range(1946, 1999))

    def test_tuen_ng_festival(self):
        name = "Tuen Ng Festival"
        name_observed = f"{name} (observed)"
        name_following = "The day following Tuen Ng Festival"

        self.assertHolidayName(
            name,
            "2006-05-31",
            "2007-06-19",
            "2008-06-08",
            "2009-05-28",
            "2010-06-16",
            "2011-06-06",
            "2012-06-23",
            "2013-06-12",
            "2014-06-02",
            "2015-06-20",
            "2016-06-09",
            "2017-05-30",
            "2018-06-18",
            "2019-06-07",
            "2020-06-25",
            "2021-06-14",
            "2022-06-03",
            "2023-06-22",
            "2024-06-10",
        )
        obs_dt = (
            "1964-06-15",
            "1987-06-01",
            "1991-06-17",
            "2008-06-09",
        )
        self.assertHolidayName(name, range(1963, 2050))
        self.assertHolidayName(name_observed, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

        self.assertHolidayName(
            name,
            self.opt_holidays,
            "2006-05-31",
            "2007-06-19",
            "2009-05-28",
            "2010-06-16",
            "2011-06-06",
            "2012-06-23",
            "2013-06-12",
            "2014-06-02",
            "2015-06-20",
            "2016-06-09",
            "2017-05-30",
            "2018-06-18",
            "2019-06-07",
            "2020-06-25",
            "2021-06-14",
            "2022-06-03",
            "2023-06-22",
            "2024-06-10",
        )
        exception_years = {1987, 1991, 2008, 2028, 2035, 2042}
        self.assertHolidayName(
            name_following,
            self.opt_holidays,
            "1987-06-01",
            "1991-06-17",
            "2008-06-09",
        )
        self.assertHolidayName(
            name, self.opt_holidays, set(range(1968, 2050)).difference(exception_years)
        )
        self.assertNoHolidayName(name, self.opt_holidays, exception_years, range(1946, 1968))

    def test_hksar_day(self):
        name = "Hong Kong Special Administrative Region Establishment Day"
        name_observed = f"{name} (observed)"
        name_following = (
            "The day following Hong Kong Special Administrative Region Establishment Day"
        )

        self.assertHolidayName(name, (f"{year}-07-01" for year in range(1997, 2050)))
        self.assertNoHolidayName(name, range(1963, 1997))
        obs_dt = (
            "2001-07-02",
            "2007-07-02",
            "2012-07-02",
            "2018-07-02",
        )
        self.assertHolidayName(name_observed, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

        exception_years = {2001, 2007, 2012, 2018, 2029, 2035, 2040, 2046}
        self.assertHolidayName(
            name,
            self.opt_holidays,
            (f"{year}-07-01" for year in set(range(1997, 2050)).difference(exception_years)),
        )
        self.assertHolidayName(
            name_following, self.opt_holidays, (f"{year}-07-02" for year in exception_years)
        )
        self.assertNoHolidayName(name, self.opt_holidays, range(1983, 1997))

    def test_mid_autumn_festival(self):
        name = "Chinese Mid-Autumn Festival"
        name_following = "The day following the Chinese Mid-Autumn Festival"
        name_second = "The second day following the Chinese Mid-Autumn Festival"

        dt = (
            "1963-10-02",
            "1965-09-10",
            "1966-09-29",
            "1967-09-18",
            "1995-09-09",
            "2002-09-21",
            "2009-10-03",
        )
        present_years = {1963, 1965, 1966, 1967, 1995, 2002, 2009}
        self.assertHolidayName(name, dt)
        self.assertNoHolidayName(name, set(range(1963, 2050)).difference(present_years))
        self.assertHolidayName(name, self.opt_holidays, dt)
        self.assertNoHolidayName(
            name, self.opt_holidays, set(range(1963, 2050)).difference(present_years), 1957, 1961
        )

        dt = (
            "2006-10-07",
            "2007-09-26",
            "2008-09-15",
            "2010-09-23",
            "2011-09-13",
            "2012-10-01",
            "2013-09-20",
            "2014-09-09",
            "2015-09-28",
            "2016-09-16",
            "2017-10-05",
            "2018-09-25",
            "2019-09-14",
            "2020-10-02",
            "2021-09-22",
            "2023-09-30",
            "2024-09-18",
        )
        exception_years = {
            1963,
            1965,
            1966,
            1967,
            1975,
            1981,
            1995,
            2002,
            2009,
            2022,
            2029,
            2036,
            2046,
            2049,
        }
        self.assertHolidayName(name_following, dt)
        self.assertHolidayName(name_following, self.opt_holidays, dt)
        self.assertHolidayName(name_following, set(range(1963, 2050)).difference(exception_years))
        self.assertHolidayName(
            name_following, self.opt_holidays, set(range(1963, 2050)).difference(exception_years)
        )

        dt = (
            "1975-09-22",
            "1981-09-14",
            "2022-09-12",
        )
        present_years = {1975, 1981, 2022, 2029, 2036, 2046, 2049}
        self.assertHolidayName(name_second, dt)
        self.assertHolidayName(name_second, self.opt_holidays, dt)
        self.assertNoHolidayName(name_second, set(range(1963, 2050)).difference(present_years))
        self.assertNoHolidayName(
            name_second, self.opt_holidays, set(range(1946, 2050)).difference(present_years)
        )

    def test_chung_yeung_festival(self):
        name = "Chung Yeung Festival"
        name_observed = f"{name} (observed)"
        name_following = "The day following Chung Yeung Festival"

        self.assertHolidayName(
            name,
            "2006-10-30",
            "2007-10-19",
            "2008-10-07",
            "2009-10-26",
            "2010-10-16",
            "2011-10-05",
            "2012-10-23",
            "2013-10-13",
            "2014-10-02",
            "2015-10-21",
            "2016-10-09",
            "2017-10-28",
            "2018-10-17",
            "2019-10-07",
            "2020-10-25",
            "2021-10-14",
            "2022-10-04",
            "2023-10-23",
            "2024-10-11",
        )
        obs_dt = (
            "1986-10-13",
            "1989-10-09",
            "1992-10-05",
            "1996-10-21",
            "1999-10-18",
            "2013-10-14",
            "2016-10-10",
            "2020-10-26",
        )
        self.assertHolidayName(name, range(1977, 2050))
        self.assertHolidayName(name_observed, obs_dt)
        self.assertNoHolidayName(name, range(1963, 1977))
        self.assertNoNonObservedHoliday(obs_dt)

        self.assertHolidayName(
            name,
            self.opt_holidays,
            "2006-10-30",
            "2007-10-19",
            "2008-10-07",
            "2009-10-26",
            "2010-10-16",
            "2011-10-05",
            "2012-10-23",
            "2014-10-02",
            "2015-10-21",
            "2017-10-28",
            "2018-10-17",
            "2019-10-07",
            "2021-10-14",
            "2022-10-04",
            "2023-10-23",
            "2024-10-11",
        )
        exception_years = {
            1969,
            1972,
            1976,
            1986,
            1989,
            1992,
            1996,
            1999,
            2013,
            2016,
            2020,
            2026,
            2040,
            2043,
            2047,
        }
        self.assertHolidayName(
            name_following,
            self.opt_holidays,
            "1969-10-20",
            "1972-10-16",
            "1976-11-01",
            "1986-10-13",
            "1989-10-09",
            "1992-10-05",
            "1996-10-21",
            "1999-10-18",
            "2013-10-14",
            "2016-10-10",
            "2020-10-26",
        )
        self.assertHolidayName(
            name, self.opt_holidays, set(range(1968, 2050)).difference(exception_years)
        )
        self.assertNoHolidayName(name, self.opt_holidays, exception_years, range(1946, 1968))

    def test_national_day(self):
        name = "National Day"
        name_observed = f"{name} (observed)"
        name_following = "The day following National Day"

        self.assertHolidayName(name, (f"{year}-10-01" for year in range(1997, 2050)))
        self.assertNoHolidayName(name, range(1963, 1997))
        obs_dt = (
            "2000-10-02",
            "2006-10-02",
            "2012-10-02",
            "2017-10-02",
            "2023-10-02",
        )
        self.assertHolidayName(name_observed, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

        exception_years = {2000, 2006, 2012, 2017, 2023, 2028, 2033, 2034, 2045}
        self.assertHolidayName(
            name,
            self.opt_holidays,
            (f"{year}-10-01" for year in set(range(1997, 2050)).difference(exception_years)),
        )
        self.assertHolidayName(
            name_following,
            self.opt_holidays,
            "1997-10-02",
            "1998-10-02",
            "2000-10-02",
            "2006-10-02",
            "2012-10-02",
            "2017-10-02",
            "2023-10-02",
            "2028-10-02",
            "2033-10-03",
            "2034-10-02",
            "2045-10-02",
        )
        self.assertNoHolidayName(name, self.opt_holidays, range(1946, 1997))

    def test_winter_solstice(self):
        name = "Chinese Winter Solstice Festival"
        name_observed = f"{name} (observed)"

        holidays_with_winter_solstice = HongKong(
            preferred_discretionary_holidays=(WINTER_SOLSTICE,), years=range(1963, 2050)
        )
        self.assertHolidayName(
            name,
            holidays_with_winter_solstice,
            "2006-12-22",
            "2007-12-22",
            "2008-12-21",
            "2009-12-22",
            "2010-12-22",
            "2011-12-22",
            "2012-12-21",
            "2013-12-22",
            "2014-12-22",
            "2015-12-22",
            "2016-12-21",
            "2017-12-22",
            "2018-12-22",
            "2019-12-22",
            "2020-12-21",
            "2021-12-21",
            "2022-12-22",
            "2023-12-22",
            "2024-12-21",
        )
        self.assertHolidayName(name, holidays_with_winter_solstice, range(1963, 2050))
        self.assertNoHolidayName("Christmas Day", holidays_with_winter_solstice)

        obs_dt = (
            "1963-12-23",
            "1968-12-23",
            "1974-12-23",
            "1985-12-23",
            "1991-12-23",
            "2002-12-23",
            "2008-12-22",
            "2013-12-23",
            "2019-12-23",
        )
        self.assertHolidayName(name_observed, holidays_with_winter_solstice, obs_dt)
        self.assertNoNonObservedHoliday(
            HongKong(observed=False, preferred_discretionary_holidays=(WINTER_SOLSTICE,)), obs_dt
        )

        self.assertNoHolidayName(name, self.opt_holidays)

    def test_christmas_day(self):
        name = "Christmas Day"
        name_observed = f"{name} (observed)"
        name_first = "The first weekday after Christmas Day"
        name_first_observed = f"{name_first} (observed)"
        name_second = "The second weekday after Christmas Day"

        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1963, 2050)))
        obs_dt = (
            "1966-12-26",
            "1977-12-26",
            "1983-12-26",
            "1988-12-26",
            "1994-12-26",
            "2005-12-26",
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
            "2033-12-27",
            "2039-12-27",
            "2044-12-27",
        )
        self.assertHolidayName(name_observed, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

        self.assertHolidayName(name_first, (f"{year}-12-26" for year in range(2024, 2050)))
        self.assertNoHolidayName(name_first, range(1963, 2024))
        obs_dt = (
            "2027-12-27",
            "2032-12-27",
            "2038-12-27",
            "2049-12-27",
        )
        self.assertHolidayName(name_first_observed, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

        exception_years = {
            1949,
            1955,
            1960,
            1966,
            1977,
            1983,
            1988,
            1994,
            2005,
            2011,
            2016,
            2022,
            2033,
            2039,
            2044,
        }
        self.assertHolidayName(
            name,
            self.opt_holidays,
            (f"{year}-12-25" for year in set(range(1946, 2050)).difference(exception_years)),
        )
        self.assertHolidayName(
            name_second, self.opt_holidays, (f"{year}-12-27" for year in exception_years)
        )
        exception_years = {
            1948,
            1954,
            1965,
            1971,
            1976,
            1982,
            1993,
            1999,
            2004,
            2010,
            2021,
            2027,
            2032,
            2038,
            2049,
        }
        self.assertHolidayName(
            name_first,
            self.opt_holidays,
            (f"{year}-12-26" for year in set(range(1946, 2050)).difference(exception_years)),
        )
        self.assertHolidayName(
            name_first, self.opt_holidays, (f"{year}-12-27" for year in exception_years)
        )

    def test_queens_birthday(self):
        name = "Queen's Birthday"
        self.assertNoHolidayName(name)
        self.assertHolidayName(name, self.opt_holidays, range(1952, 1998))
        self.assertNoHolidayName(name, self.opt_holidays, range(1946, 1952), range(1998, 2050))
        self.assertHolidayName(name, self.opt_holidays, "1952-06-05")
        self.assertHolidayName(
            name, self.opt_holidays, (f"{year}-04-21" for year in range(1953, 1983))
        )
        self.assertHolidayName(
            name,
            self.opt_holidays,
            "1983-06-11",
            "1983-06-13",
            "1984-06-09",
            "1984-06-11",
            "1985-06-08",
            "1985-06-10",
            "1986-06-14",
            "1986-06-16",
            "1987-06-13",
            "1987-06-15",
            "1988-06-11",
            "1988-06-13",
            "1989-06-10",
            "1989-06-12",
            "1990-06-09",
            "1990-06-11",
            "1991-06-08",
            "1991-06-10",
            "1992-06-13",
            "1992-06-15",
            "1993-06-12",
            "1993-06-14",
            "1994-06-11",
            "1994-06-13",
            "1995-06-10",
            "1995-06-12",
            "1996-06-08",
            "1996-06-10",
            "1997-06-28",
            "1997-06-30",
        )

    def test_whit_monday(self):
        name = "Monday after Pentecost"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            self.opt_holidays,
            "1946-06-10",
            "1947-05-26",
            "1948-05-17",
            "1949-06-06",
            "1950-05-29",
            "1951-05-14",
            "1952-06-02",
            "1953-05-25",
            "1954-06-07",
            "1955-05-30",
            "1956-05-21",
            "1957-06-10",
            "1958-05-26",
            "1959-05-18",
            "1960-06-06",
            "1961-05-22",
            "1962-06-11",
            "1963-06-03",
            "1964-05-18",
            "1965-06-07",
            "1966-05-30",
            "1967-05-15",
        )
        self.assertNoHolidayName(name, self.opt_holidays, range(1968, 2050))

    def test_national_day_of_the_republic(self):
        name = "National Day of the Republic of China"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            self.opt_holidays,
            "1946-10-14",
            "1947-10-13",
            "1948-10-11",
            "1949-10-10",
            "1950-10-09",
            "1951-10-08",
            "1952-10-13",
            "1953-10-12",
            "1954-10-11",
            "1955-10-10",
            "1956-10-08",
            "1957-10-14",
            "1958-10-13",
            "1959-10-12",
            "1960-10-10",
            "1961-10-09",
            "1962-10-08",
            "1963-10-14",
            "1964-10-12",
            "1965-10-11",
            "1966-10-10",
            "1967-10-09",
        )
        self.assertNoHolidayName(name, self.opt_holidays, range(1968, 2050))

    def test_monday_after_peace_memorial_day(self):
        name = "Monday after Peace Memorial Day"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            self.opt_holidays,
            "1946-11-11",
            "1947-11-10",
            "1948-11-15",
            "1949-11-14",
            "1950-11-13",
            "1951-11-12",
            "1952-11-10",
            "1953-11-09",
            "1954-11-15",
            "1955-11-14",
            "1956-11-12",
            "1957-11-11",
            "1958-11-10",
            "1959-11-09",
            "1960-11-14",
            "1961-11-13",
            "1962-11-12",
            "1963-11-11",
            "1964-11-09",
            "1965-11-15",
            "1966-11-14",
            "1967-11-13",
        )
        self.assertNoHolidayName(name, self.opt_holidays, range(1968, 2050))

    def test_2020(self):
        # https://www.labour.gov.hk/eng/news/latest_holidays2020.htm
        self.assertHolidays(
            HongKong(years=2020, preferred_discretionary_holidays=(CHRISTMAS, WINTER_SOLSTICE)),
            ("2020-01-01", "The first day of January"),
            ("2020-01-25", "Lunar New Year's Day"),
            ("2020-01-27", "The third day of Lunar New Year"),
            ("2020-01-28", "The fourth day of Lunar New Year"),
            ("2020-04-04", "Ching Ming Festival"),
            ("2020-05-01", "Labour Day"),
            ("2020-06-25", "Tuen Ng Festival"),
            ("2020-07-01", "Hong Kong Special Administrative Region Establishment Day"),
            ("2020-10-01", "National Day"),
            ("2020-10-02", "The day following the Chinese Mid-Autumn Festival"),
            ("2020-10-25", "Chung Yeung Festival"),
            ("2020-10-26", "Chung Yeung Festival (observed)"),
            ("2020-12-21", "Chinese Winter Solstice Festival"),
            ("2020-12-25", "Christmas Day"),
        )

    def test_2021(self):
        # https://www.labour.gov.hk/eng/news/latest_holidays2021.htm
        self.assertHolidays(
            HongKong(years=2021, preferred_discretionary_holidays=(CHRISTMAS, WINTER_SOLSTICE)),
            ("2021-01-01", "The first day of January"),
            ("2021-02-12", "Lunar New Year's Day"),
            ("2021-02-13", "The second day of Lunar New Year"),
            ("2021-02-15", "The fourth day of Lunar New Year"),
            ("2021-04-04", "Ching Ming Festival"),
            ("2021-04-05", "Ching Ming Festival (observed)"),
            ("2021-05-01", "Labour Day"),
            ("2021-06-14", "Tuen Ng Festival"),
            ("2021-07-01", "Hong Kong Special Administrative Region Establishment Day"),
            ("2021-09-22", "The day following the Chinese Mid-Autumn Festival"),
            ("2021-10-01", "National Day"),
            ("2021-10-14", "Chung Yeung Festival"),
            ("2021-12-21", "Chinese Winter Solstice Festival"),
            ("2021-12-25", "Christmas Day"),
        )

    def test_2022(self):
        # https://www.labour.gov.hk/eng/news/latest_holidays2022.htm
        self.assertHolidays(
            HongKong(years=2022, preferred_discretionary_holidays=(CHRISTMAS, WINTER_SOLSTICE)),
            ("2022-01-01", "The first day of January"),
            ("2022-02-01", "Lunar New Year's Day"),
            ("2022-02-02", "The second day of Lunar New Year"),
            ("2022-02-03", "The third day of Lunar New Year"),
            ("2022-04-05", "Ching Ming Festival"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Labour Day (observed)"),
            ("2022-05-08", "The Birthday of the Buddha"),
            ("2022-05-09", "The Birthday of the Buddha (observed)"),
            ("2022-06-03", "Tuen Ng Festival"),
            ("2022-07-01", "Hong Kong Special Administrative Region Establishment Day"),
            ("2022-09-12", "The second day following the Chinese Mid-Autumn Festival"),
            ("2022-10-01", "National Day"),
            ("2022-10-04", "Chung Yeung Festival"),
            ("2022-12-22", "Chinese Winter Solstice Festival"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )

    def test_2023(self):
        # https://www.labour.gov.hk/eng/news/latest_holidays2023.htm
        self.assertHolidays(
            HongKong(years=2023, preferred_discretionary_holidays=(CHRISTMAS, WINTER_SOLSTICE)),
            ("2023-01-01", "The first day of January"),
            ("2023-01-02", "The first day of January (observed)"),
            ("2023-01-23", "The second day of Lunar New Year"),
            ("2023-01-24", "The third day of Lunar New Year"),
            ("2023-01-25", "The fourth day of Lunar New Year"),
            ("2023-04-05", "Ching Ming Festival"),
            ("2023-05-01", "Labour Day"),
            ("2023-05-26", "The Birthday of the Buddha"),
            ("2023-06-22", "Tuen Ng Festival"),
            ("2023-07-01", "Hong Kong Special Administrative Region Establishment Day"),
            ("2023-09-30", "The day following the Chinese Mid-Autumn Festival"),
            ("2023-10-01", "National Day"),
            ("2023-10-02", "National Day (observed)"),
            ("2023-10-23", "Chung Yeung Festival"),
            ("2023-12-22", "Chinese Winter Solstice Festival"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_2024(self):
        # https://www.labour.gov.hk/eng/news/latest_holidays2024.htm
        self.assertHolidays(
            HongKong(years=2024, preferred_discretionary_holidays=(CHRISTMAS, WINTER_SOLSTICE)),
            ("2024-01-01", "The first day of January"),
            ("2024-02-10", "Lunar New Year's Day"),
            ("2024-02-12", "The third day of Lunar New Year"),
            ("2024-02-13", "The fourth day of Lunar New Year"),
            ("2024-04-04", "Ching Ming Festival"),
            ("2024-05-01", "Labour Day"),
            ("2024-05-15", "The Birthday of the Buddha"),
            ("2024-06-10", "Tuen Ng Festival"),
            ("2024-07-01", "Hong Kong Special Administrative Region Establishment Day"),
            ("2024-09-18", "The day following the Chinese Mid-Autumn Festival"),
            ("2024-10-01", "National Day"),
            ("2024-10-11", "Chung Yeung Festival"),
            ("2024-12-21", "Chinese Winter Solstice Festival"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "The first weekday after Christmas Day"),
        )

    def test_optional_2020(self):
        # https://www.gov.hk/en/about/abouthk/holiday/2020.htm
        self.assertHolidays(
            HongKong(categories=OPTIONAL, years=2020),
            ("2020-01-01", "The first day of January"),
            ("2020-01-25", "Lunar New Year's Day"),
            ("2020-01-27", "The third day of Lunar New Year"),
            ("2020-01-28", "The fourth day of Lunar New Year"),
            ("2020-04-04", "Ching Ming Festival"),
            ("2020-04-10", "Good Friday"),
            ("2020-04-11", "The day following Good Friday"),
            ("2020-04-13", "Easter Monday"),
            ("2020-04-30", "The Birthday of the Buddha"),
            ("2020-05-01", "Labour Day"),
            ("2020-06-25", "Tuen Ng Festival"),
            ("2020-07-01", "Hong Kong Special Administrative Region Establishment Day"),
            ("2020-10-01", "National Day"),
            ("2020-10-02", "The day following the Chinese Mid-Autumn Festival"),
            ("2020-10-26", "The day following Chung Yeung Festival"),
            ("2020-12-25", "Christmas Day"),
            ("2020-12-26", "The first weekday after Christmas Day"),
        )

    def test_optional_2021(self):
        # https://www.gov.hk/en/about/abouthk/holiday/2021.htm
        self.assertHolidays(
            HongKong(categories=OPTIONAL, years=2021),
            ("2021-01-01", "The first day of January"),
            ("2021-02-12", "Lunar New Year's Day"),
            ("2021-02-13", "The second day of Lunar New Year"),
            ("2021-02-15", "The fourth day of Lunar New Year"),
            ("2021-04-02", "Good Friday"),
            ("2021-04-03", "The day following Good Friday"),
            ("2021-04-05", "The day following Ching Ming Festival"),
            ("2021-04-06", "The day following Easter Monday"),
            ("2021-05-01", "Labour Day"),
            ("2021-05-19", "The Birthday of the Buddha"),
            ("2021-06-14", "Tuen Ng Festival"),
            ("2021-07-01", "Hong Kong Special Administrative Region Establishment Day"),
            ("2021-09-22", "The day following the Chinese Mid-Autumn Festival"),
            ("2021-10-01", "National Day"),
            ("2021-10-14", "Chung Yeung Festival"),
            ("2021-12-25", "Christmas Day"),
            ("2021-12-27", "The first weekday after Christmas Day"),
        )

    def test_optional_2022(self):
        # https://www.gov.hk/en/about/abouthk/holiday/2022.htm
        self.assertHolidays(
            HongKong(categories=OPTIONAL, years=2022),
            ("2022-01-01", "The first day of January"),
            ("2022-02-01", "Lunar New Year's Day"),
            ("2022-02-02", "The second day of Lunar New Year"),
            ("2022-02-03", "The third day of Lunar New Year"),
            ("2022-04-05", "Ching Ming Festival"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-16", "The day following Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-02", "The day following Labour Day"),
            ("2022-05-09", "The day following the Birthday of the Buddha"),
            ("2022-06-03", "Tuen Ng Festival"),
            ("2022-07-01", "Hong Kong Special Administrative Region Establishment Day"),
            ("2022-09-12", "The second day following the Chinese Mid-Autumn Festival"),
            ("2022-10-01", "National Day"),
            ("2022-10-04", "Chung Yeung Festival"),
            ("2022-12-26", "The first weekday after Christmas Day"),
            ("2022-12-27", "The second weekday after Christmas Day"),
        )

    def test_optional_2023(self):
        # https://www.gov.hk/en/about/abouthk/holiday/2023.htm
        self.assertHolidays(
            HongKong(categories=OPTIONAL, years=2023),
            ("2023-01-02", "The day following the first day of January"),
            ("2023-01-23", "The second day of Lunar New Year"),
            ("2023-01-24", "The third day of Lunar New Year"),
            ("2023-01-25", "The fourth day of Lunar New Year"),
            ("2023-04-05", "Ching Ming Festival"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-08", "The day following Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-01", "Labour Day"),
            ("2023-05-26", "The Birthday of the Buddha"),
            ("2023-06-22", "Tuen Ng Festival"),
            ("2023-07-01", "Hong Kong Special Administrative Region Establishment Day"),
            ("2023-09-30", "The day following the Chinese Mid-Autumn Festival"),
            ("2023-10-02", "The day following National Day"),
            ("2023-10-23", "Chung Yeung Festival"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "The first weekday after Christmas Day"),
        )

    def test_optional_2024(self):
        # https://www.gov.hk/en/about/abouthk/holiday/2024.htm
        self.assertHolidays(
            HongKong(categories=OPTIONAL, years=2024),
            ("2024-01-01", "The first day of January"),
            ("2024-02-10", "Lunar New Year's Day"),
            ("2024-02-12", "The third day of Lunar New Year"),
            ("2024-02-13", "The fourth day of Lunar New Year"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "The day following Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-04", "Ching Ming Festival"),
            ("2024-05-01", "Labour Day"),
            ("2024-05-15", "The Birthday of the Buddha"),
            ("2024-06-10", "Tuen Ng Festival"),
            ("2024-07-01", "Hong Kong Special Administrative Region Establishment Day"),
            ("2024-09-18", "The day following the Chinese Mid-Autumn Festival"),
            ("2024-10-01", "National Day"),
            ("2024-10-11", "Chung Yeung Festival"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "The first weekday after Christmas Day"),
        )
