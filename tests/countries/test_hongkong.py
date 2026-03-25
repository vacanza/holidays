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

from holidays.constants import OPTIONAL
from holidays.countries.hongkong import HongKong, CHRISTMAS, WINTER_SOLSTICE
from tests.common import CommonCountryTests


class TestHongKong(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full_range = range(1963, 2050)
        super().setUpClass(HongKong, years_optional=range(HongKong.start_year, 2050))

    def test_no_holidays(self):
        self.assertNoHolidays(HongKong(years=range(HongKong.start_year - 1, self.start_year - 1)))
        self.assertNoHolidays(HongKong(categories=OPTIONAL, years=HongKong.start_year - 1))

    def test_special_holidays(self):
        self.assertHoliday(
            "1981-07-29",
            "1986-10-22",
            "1997-07-02",
            "2015-09-03",
        )
        self.assertOptionalHoliday(
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

    def test_new_years_day(self):
        name = "一月一日"
        name_observed = f"{name}（補假）"
        name_following = f"{name}翌日"

        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1977, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1977))
        obs_dts = (
            "1978-01-02",
            "1984-01-02",
            "1989-01-02",
            "1995-01-02",
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

        years_special = {
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
        self.assertOptionalHolidayName(
            name,
            (
                f"{year}-01-01"
                for year in range(HongKong.start_year, self.end_year)
                if year not in years_special
            ),
        )
        self.assertOptionalHolidayName(name_following, (f"{year}-01-02" for year in years_special))

    def test_chinese_new_year(self):
        name_eve = "農曆年初一的前一日"
        name = "農曆年初一"
        name_second = "農曆年初二"
        name_third = "農曆年初三"
        name_fourth = "農曆年初四"

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
        self.assertNoHolidayName(
            name_eve, range(self.start_year, 1983), range(2012, self.end_year)
        )
        self.assertNoOptionalHolidayName(
            name_eve, range(HongKong.start_year, 1983), range(2012, self.end_year)
        )

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
        years_special = {1983, 1986, 2006, 2007, 2010, 2013, 2023, 2030, 2034, 2037, 2040}
        self.assertHolidayName(name, set(self.full_range) - years_special)
        self.assertNoHolidayName(name, years_special)
        self.assertOptionalHolidayName(
            name,
            (
                year
                for year in range(HongKong.start_year, self.end_year)
                if year not in years_special
            ),
        )
        self.assertNoOptionalHolidayName(name, years_special)

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
        years_special = {1990, 1993, 2000, 2003, 2017, 2020, 2024, 2027, 2044, 2047}
        self.assertHolidayName(name_second, set(self.full_range) - years_special)
        self.assertNoHolidayName(name_second, years_special)
        self.assertOptionalHolidayName(
            name_second,
            (
                year
                for year in range(HongKong.start_year, self.end_year)
                if year not in years_special
            ),
        )
        self.assertNoOptionalHolidayName(name_second, years_special)

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
        years_special = {1991, 1997, 2014, 2018, 2021, 2041, 2045, 2048}
        self.assertHolidayName(name_third, set(range(1977, self.end_year)) - years_special)
        self.assertNoHolidayName(name_third, years_special, range(self.start_year, 1977))
        self.assertOptionalHolidayName(name_third, set(range(1968, self.end_year)) - years_special)
        self.assertNoOptionalHolidayName(
            name_third, years_special, range(HongKong.start_year, 1968)
        )

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
        years_special = {
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
        self.assertHolidayName(name_fourth, years_special)
        self.assertNoHolidayName(name_fourth, set(self.full_range) - years_special)
        self.assertOptionalHolidayName(name_fourth, years_special)
        self.assertNoOptionalHolidayName(
            name_fourth, set(range(HongKong.start_year, self.end_year)) - years_special
        )

    def test_good_friday(self):
        name = "耶穌受難節"

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
        self.assertOptionalHolidayName(
            name,
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
        self.assertHolidayName(name, range(2028, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2028))
        self.assertOptionalHolidayName(name, range(HongKong.start_year, self.end_year))

    def test_holy_saturday(self):
        name = "耶穌受難節翌日"

        self.assertHolidayName(
            name,
            "2030-04-20",
            "2031-04-12",
            "2032-03-27",
            "2033-04-16",
            "2034-04-08",
            "2035-03-24",
        )
        self.assertOptionalHolidayName(
            name,
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
        self.assertHolidayName(name, range(2030, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2030))
        self.assertOptionalHolidayName(name, range(HongKong.start_year, self.end_year))

    def test_easter_monday(self):
        name = "復活節星期一"
        name_following = f"{name}翌日"

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
        self.assertOptionalHolidayName(
            name,
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
        years_special = {2015, 2021, 2026}
        self.assertHolidayName(name, range(2026, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2026))
        self.assertOptionalHolidayName(
            name,
            (
                year
                for year in range(HongKong.start_year, self.end_year)
                if year not in years_special
            ),
        )
        self.assertOptionalHolidayName(
            name_following,
            "2015-04-07",
            "2021-04-06",
            "2026-04-07",
        )

    def test_tomb_sweeping_day(self):
        name = "清明節"
        name_observed = f"{name}（補假）"
        name_following = f"{name}翌日"

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
        obs_dts = (
            "1970-04-06",
            "1976-04-05",
            "1981-04-06",
            "1987-04-06",
            "1998-04-06",
            "2004-04-05",
            "2015-04-06",
            "2021-04-05",
        )
        self.assertHolidayName(name, self.full_range)
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

        self.assertOptionalHolidayName(
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
        years_special = {
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
        self.assertOptionalHolidayName(
            name_following,
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
        self.assertOptionalHolidayName(name, set(range(1968, self.end_year)) - years_special)
        self.assertNoOptionalHolidayName(name, years_special, range(HongKong.start_year, 1968))

    def test_the_buddhas_birthday(self):
        name = "佛誕"
        name_observed = f"{name}（補假）"
        name_following = f"{name}翌日"

        self.assertHolidayName(
            name,
            "2022-05-08",
            "2023-05-26",
            "2024-05-15",
            "2025-05-05",
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
        obs_dts = ("2022-05-09",)
        self.assertHolidayName(name, range(2022, self.end_year))
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoHolidayName(name, range(self.start_year, 2022))
        self.assertNoNonObservedHoliday(obs_dts)

        self.assertOptionalHolidayName(
            name,
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
        years_special = {2002, 2005, 2019, 2022, 2026, 2029, 2032, 2046, 2049}
        self.assertOptionalHolidayName(
            name_following,
            "2002-05-20",
            "2005-05-16",
            "2019-05-13",
            "2022-05-09",
        )
        self.assertOptionalHolidayName(name, set(range(1999, self.end_year)) - years_special)
        self.assertNoOptionalHolidayName(name, years_special, range(HongKong.start_year, 1999))

    def test_labor_day(self):
        name = "勞動節"
        name_observed = f"{name}（補假）"
        name_following = f"{name}翌日"

        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1999, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1999))
        obs_dts = (
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

        years_special = {2005, 2011, 2016, 2022, 2033, 2039, 2044}
        self.assertOptionalHolidayName(
            name,
            (f"{year}-05-01" for year in range(1999, self.end_year) if year not in years_special),
        )
        self.assertOptionalHolidayName(name_following, (f"{year}-05-02" for year in years_special))
        self.assertNoOptionalHolidayName(name, range(HongKong.start_year, 1999))

    def test_dragon_boat_festival(self):
        name = "端午節"
        name_observed = f"{name}（補假）"
        name_following = f"{name}翌日"

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
        obs_dts = (
            "1964-06-15",
            "1987-06-01",
            "1991-06-17",
            "2008-06-09",
        )
        self.assertHolidayName(name, self.full_range)
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

        self.assertOptionalHolidayName(
            name,
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
        years_special = {1987, 1991, 2008, 2028, 2035, 2042}
        self.assertOptionalHolidayName(
            name_following,
            "1987-06-01",
            "1991-06-17",
            "2008-06-09",
        )
        self.assertOptionalHolidayName(name, set(range(1968, self.end_year)) - years_special)
        self.assertNoOptionalHolidayName(name, years_special, range(HongKong.start_year, 1968))

    def test_hong_kong_sar_day(self):
        name = "香港特別行政區成立紀念日"
        name_observed = f"{name}（補假）"
        name_following = f"{name}翌日"

        self.assertHolidayName(name, (f"{year}-07-01" for year in range(1997, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1997))
        obs_dts = (
            "2001-07-02",
            "2007-07-02",
            "2012-07-02",
            "2018-07-02",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

        years_special = {2001, 2007, 2012, 2018, 2029, 2035, 2040, 2046}
        self.assertOptionalHolidayName(
            name,
            (f"{year}-07-01" for year in range(1997, self.end_year) if year not in years_special),
        )
        self.assertOptionalHolidayName(name_following, (f"{year}-07-02" for year in years_special))
        self.assertNoOptionalHolidayName(name, range(1983, 1997))

    def test_mid_autumn_festival(self):
        name = "中秋節"
        name_following = f"{name}翌日"
        name_second = "中秋節後第二日"

        dts = (
            "1963-10-02",
            "1965-09-10",
            "1966-09-29",
            "1967-09-18",
            "1995-09-09",
            "2002-09-21",
            "2009-10-03",
        )
        years_special = {self.start_year, 1965, 1966, 1967, 1995, 2002, 2009}
        self.assertHolidayName(name, dts)
        self.assertNoHolidayName(name, set(self.full_range) - years_special)
        self.assertOptionalHolidayName(name, dts)
        self.assertNoOptionalHolidayName(name, set(self.full_range) - years_special, 1957, 1961)

        dts = (
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
        years_special = {
            self.start_year,
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
        self.assertHolidayName(name_following, dts)
        self.assertOptionalHolidayName(name_following, dts)
        self.assertHolidayName(name_following, set(self.full_range) - years_special)
        self.assertOptionalHolidayName(name_following, set(self.full_range) - years_special)

        dts = (
            "1975-09-22",
            "1981-09-14",
            "2022-09-12",
        )
        years_special = {1975, 1981, 2022, 2029, 2036, 2046, 2049}
        self.assertHolidayName(name_second, dts)
        self.assertOptionalHolidayName(name_second, dts)
        self.assertNoHolidayName(name_second, set(self.full_range) - years_special)
        self.assertNoOptionalHolidayName(
            name_second, set(range(HongKong.start_year, self.end_year)) - years_special
        )

    def test_double_ninth_festival(self):
        name = "重陽節"
        name_observed = f"{name}（補假）"
        name_following = f"{name}翌日"

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
        obs_dts = (
            "1986-10-13",
            "1989-10-09",
            "1992-10-05",
            "1996-10-21",
            "1999-10-18",
            "2013-10-14",
            "2016-10-10",
            "2020-10-26",
        )
        self.assertHolidayName(name, range(1977, self.end_year))
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoHolidayName(name, range(self.start_year, 1977))
        self.assertNoNonObservedHoliday(obs_dts)

        self.assertOptionalHolidayName(
            name,
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
        years_special = {
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
        self.assertOptionalHolidayName(
            name_following,
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
        self.assertOptionalHolidayName(name, set(range(1968, self.end_year)) - years_special)
        self.assertNoOptionalHolidayName(name, years_special, range(HongKong.start_year, 1968))

    def test_national_day(self):
        name = "國慶日"
        name_observed = f"{name}（補假）"
        name_following = f"{name}翌日"

        self.assertHolidayName(name, (f"{year}-10-01" for year in range(1997, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1997))
        obs_dts = (
            "2000-10-02",
            "2006-10-02",
            "2012-10-02",
            "2017-10-02",
            "2023-10-02",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

        years_special = {2000, 2006, 2012, 2017, 2023, 2028, 2033, 2034, 2045}
        self.assertOptionalHolidayName(
            name,
            (
                f"{year}-10-01"
                for year in set(range(1997, self.end_year))
                if year not in years_special
            ),
        )
        self.assertOptionalHolidayName(
            name_following,
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
        self.assertNoOptionalHolidayName(name, range(HongKong.start_year, 1997))

    def test_winter_solstice(self):
        name = "冬節"
        name_observed = f"{name}（補假）"

        holidays_with_winter_solstice = HongKong(
            preferred_discretionary_holidays=(WINTER_SOLSTICE,), years=self.full_range
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
        self.assertHolidayName(name, holidays_with_winter_solstice, self.full_range)
        self.assertNoHolidayName("聖誕節", holidays_with_winter_solstice)

        obs_dts = (
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
        self.assertHolidayName(name_observed, holidays_with_winter_solstice, obs_dts)
        self.assertNoNonObservedHoliday(
            HongKong(observed=False, preferred_discretionary_holidays=(WINTER_SOLSTICE,)), obs_dts
        )

        self.assertNoOptionalHolidayName(name)

    def test_christmas_day(self):
        name = "聖誕節"
        name_observed = f"{name}（補假）"
        name_first = "聖誕節後第一個周日"
        name_first_observed = f"{name_first}（補假）"
        name_second = "聖誕節後第二個周日"

        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
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
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

        self.assertHolidayName(
            name_first, (f"{year}-12-26" for year in range(2024, self.end_year))
        )
        self.assertNoHolidayName(name_first, range(self.start_year, 2024))
        obs_dts = (
            "2027-12-27",
            "2032-12-27",
            "2038-12-27",
            "2049-12-27",
        )
        self.assertHolidayName(name_first_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

        years_special = {
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
        self.assertOptionalHolidayName(
            name,
            (
                f"{year}-12-25"
                for year in range(HongKong.start_year, self.end_year)
                if year not in years_special
            ),
        )
        self.assertOptionalHolidayName(name_second, (f"{year}-12-27" for year in years_special))
        years_special = {
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
        self.assertOptionalHolidayName(
            name_first,
            (
                f"{year}-12-26"
                for year in range(HongKong.start_year, self.end_year)
                if year not in years_special
            ),
        )
        self.assertOptionalHolidayName(name_first, (f"{year}-12-27" for year in years_special))

    def test_queens_birthday(self):
        name = "英女皇壽辰"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(name, range(1952, 1998))
        self.assertNoOptionalHolidayName(
            name, range(HongKong.start_year, 1952), range(1998, self.end_year)
        )
        self.assertOptionalHolidayName(name, "1952-06-05")
        self.assertOptionalHolidayName(name, (f"{year}-04-21" for year in range(1953, 1983)))
        self.assertOptionalHolidayName(
            name,
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
        name = "靈降臨節後星期一"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
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
        self.assertNoOptionalHolidayName(name, range(1968, self.end_year))

    def test_national_day_of_the_republic(self):
        name = "中華民國國慶日"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
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
        self.assertNoOptionalHolidayName(name, range(1968, self.end_year))

    def test_monday_after_remembrance_day(self):
        name = "和平紀念日後星期一"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
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
        self.assertNoOptionalHolidayName(name, range(1968, self.end_year))

    def test_2020(self):
        # https://www.labour.gov.hk/eng/news/latest_holidays2020.htm
        self.assertHolidays(
            HongKong(years=2020, preferred_discretionary_holidays=(CHRISTMAS, WINTER_SOLSTICE)),
            ("2020-01-01", "一月一日"),
            ("2020-01-25", "農曆年初一"),
            ("2020-01-27", "農曆年初三"),
            ("2020-01-28", "農曆年初四"),
            ("2020-04-04", "清明節"),
            ("2020-05-01", "勞動節"),
            ("2020-06-25", "端午節"),
            ("2020-07-01", "香港特別行政區成立紀念日"),
            ("2020-10-01", "國慶日"),
            ("2020-10-02", "中秋節翌日"),
            ("2020-10-25", "重陽節"),
            ("2020-10-26", "重陽節（補假）"),
            ("2020-12-21", "冬節"),
            ("2020-12-25", "聖誕節"),
        )

    def test_2021(self):
        # https://www.labour.gov.hk/eng/news/latest_holidays2021.htm
        self.assertHolidays(
            HongKong(years=2021, preferred_discretionary_holidays=(CHRISTMAS, WINTER_SOLSTICE)),
            ("2021-01-01", "一月一日"),
            ("2021-02-12", "農曆年初一"),
            ("2021-02-13", "農曆年初二"),
            ("2021-02-15", "農曆年初四"),
            ("2021-04-04", "清明節"),
            ("2021-04-05", "清明節（補假）"),
            ("2021-05-01", "勞動節"),
            ("2021-06-14", "端午節"),
            ("2021-07-01", "香港特別行政區成立紀念日"),
            ("2021-09-22", "中秋節翌日"),
            ("2021-10-01", "國慶日"),
            ("2021-10-14", "重陽節"),
            ("2021-12-21", "冬節"),
            ("2021-12-25", "聖誕節"),
        )

    def test_2022(self):
        # https://www.labour.gov.hk/eng/news/latest_holidays2022.htm
        self.assertHolidays(
            HongKong(years=2022, preferred_discretionary_holidays=(CHRISTMAS, WINTER_SOLSTICE)),
            ("2022-01-01", "一月一日"),
            ("2022-02-01", "農曆年初一"),
            ("2022-02-02", "農曆年初二"),
            ("2022-02-03", "農曆年初三"),
            ("2022-04-05", "清明節"),
            ("2022-05-01", "勞動節"),
            ("2022-05-02", "勞動節（補假）"),
            ("2022-05-08", "佛誕"),
            ("2022-05-09", "佛誕（補假）"),
            ("2022-06-03", "端午節"),
            ("2022-07-01", "香港特別行政區成立紀念日"),
            ("2022-09-12", "中秋節後第二日"),
            ("2022-10-01", "國慶日"),
            ("2022-10-04", "重陽節"),
            ("2022-12-22", "冬節"),
            ("2022-12-25", "聖誕節"),
            ("2022-12-26", "聖誕節（補假）"),
        )

    def test_2023(self):
        # https://www.labour.gov.hk/eng/news/latest_holidays2023.htm
        self.assertHolidays(
            HongKong(years=2023, preferred_discretionary_holidays=(CHRISTMAS, WINTER_SOLSTICE)),
            ("2023-01-01", "一月一日"),
            ("2023-01-02", "一月一日（補假）"),
            ("2023-01-23", "農曆年初二"),
            ("2023-01-24", "農曆年初三"),
            ("2023-01-25", "農曆年初四"),
            ("2023-04-05", "清明節"),
            ("2023-05-01", "勞動節"),
            ("2023-05-26", "佛誕"),
            ("2023-06-22", "端午節"),
            ("2023-07-01", "香港特別行政區成立紀念日"),
            ("2023-09-30", "中秋節翌日"),
            ("2023-10-01", "國慶日"),
            ("2023-10-02", "國慶日（補假）"),
            ("2023-10-23", "重陽節"),
            ("2023-12-22", "冬節"),
            ("2023-12-25", "聖誕節"),
        )

    def test_2024(self):
        # https://www.labour.gov.hk/eng/news/latest_holidays2024.htm
        self.assertHolidays(
            HongKong(years=2024, preferred_discretionary_holidays=(CHRISTMAS, WINTER_SOLSTICE)),
            ("2024-01-01", "一月一日"),
            ("2024-02-10", "農曆年初一"),
            ("2024-02-12", "農曆年初三"),
            ("2024-02-13", "農曆年初四"),
            ("2024-04-04", "清明節"),
            ("2024-05-01", "勞動節"),
            ("2024-05-15", "佛誕"),
            ("2024-06-10", "端午節"),
            ("2024-07-01", "香港特別行政區成立紀念日"),
            ("2024-09-18", "中秋節翌日"),
            ("2024-10-01", "國慶日"),
            ("2024-10-11", "重陽節"),
            ("2024-12-21", "冬節"),
            ("2024-12-25", "聖誕節"),
            ("2024-12-26", "聖誕節後第一個周日"),
        )

    def test_2025(self):
        # https://www.labour.gov.hk/eng/news/latest_holidays2025.htm
        self.assertHolidays(
            HongKong(years=2025, preferred_discretionary_holidays=(CHRISTMAS, WINTER_SOLSTICE)),
            ("2025-01-01", "一月一日"),
            ("2025-01-29", "農曆年初一"),
            ("2025-01-30", "農曆年初二"),
            ("2025-01-31", "農曆年初三"),
            ("2025-04-04", "清明節"),
            ("2025-05-01", "勞動節"),
            ("2025-05-05", "佛誕"),
            ("2025-05-31", "端午節"),
            ("2025-07-01", "香港特別行政區成立紀念日"),
            ("2025-10-01", "國慶日"),
            ("2025-10-07", "中秋節翌日"),
            ("2025-10-29", "重陽節"),
            ("2025-12-21", "冬節"),
            ("2025-12-22", "冬節（補假）"),
            ("2025-12-25", "聖誕節"),
            ("2025-12-26", "聖誕節後第一個周日"),
        )

    def test_optional_2020(self):
        # https://www.gov.hk/en/about/abouthk/holiday/2020.htm
        self.assertOptionalHolidaysInYear(
            2020,
            ("2020-01-01", "一月一日"),
            ("2020-01-25", "農曆年初一"),
            ("2020-01-27", "農曆年初三"),
            ("2020-01-28", "農曆年初四"),
            ("2020-04-04", "清明節"),
            ("2020-04-10", "耶穌受難節"),
            ("2020-04-11", "耶穌受難節翌日"),
            ("2020-04-13", "復活節星期一"),
            ("2020-04-30", "佛誕"),
            ("2020-05-01", "勞動節"),
            ("2020-06-25", "端午節"),
            ("2020-07-01", "香港特別行政區成立紀念日"),
            ("2020-10-01", "國慶日"),
            ("2020-10-02", "中秋節翌日"),
            ("2020-10-26", "重陽節翌日"),
            ("2020-12-25", "聖誕節"),
            ("2020-12-26", "聖誕節後第一個周日"),
        )

    def test_optional_2021(self):
        # https://www.gov.hk/en/about/abouthk/holiday/2021.htm
        self.assertOptionalHolidaysInYear(
            2021,
            ("2021-01-01", "一月一日"),
            ("2021-02-12", "農曆年初一"),
            ("2021-02-13", "農曆年初二"),
            ("2021-02-15", "農曆年初四"),
            ("2021-04-02", "耶穌受難節"),
            ("2021-04-03", "耶穌受難節翌日"),
            ("2021-04-05", "清明節翌日"),
            ("2021-04-06", "復活節星期一翌日"),
            ("2021-05-01", "勞動節"),
            ("2021-05-19", "佛誕"),
            ("2021-06-14", "端午節"),
            ("2021-07-01", "香港特別行政區成立紀念日"),
            ("2021-09-22", "中秋節翌日"),
            ("2021-10-01", "國慶日"),
            ("2021-10-14", "重陽節"),
            ("2021-12-25", "聖誕節"),
            ("2021-12-27", "聖誕節後第一個周日"),
        )

    def test_optional_2022(self):
        # https://www.gov.hk/en/about/abouthk/holiday/2022.htm
        self.assertOptionalHolidaysInYear(
            2022,
            ("2022-01-01", "一月一日"),
            ("2022-02-01", "農曆年初一"),
            ("2022-02-02", "農曆年初二"),
            ("2022-02-03", "農曆年初三"),
            ("2022-04-05", "清明節"),
            ("2022-04-15", "耶穌受難節"),
            ("2022-04-16", "耶穌受難節翌日"),
            ("2022-04-18", "復活節星期一"),
            ("2022-05-02", "勞動節翌日"),
            ("2022-05-09", "佛誕翌日"),
            ("2022-06-03", "端午節"),
            ("2022-07-01", "香港特別行政區成立紀念日"),
            ("2022-09-12", "中秋節後第二日"),
            ("2022-10-01", "國慶日"),
            ("2022-10-04", "重陽節"),
            ("2022-12-26", "聖誕節後第一個周日"),
            ("2022-12-27", "聖誕節後第二個周日"),
        )

    def test_optional_2023(self):
        # https://www.gov.hk/en/about/abouthk/holiday/2023.htm
        self.assertOptionalHolidaysInYear(
            2023,
            ("2023-01-02", "一月一日翌日"),
            ("2023-01-23", "農曆年初二"),
            ("2023-01-24", "農曆年初三"),
            ("2023-01-25", "農曆年初四"),
            ("2023-04-05", "清明節"),
            ("2023-04-07", "耶穌受難節"),
            ("2023-04-08", "耶穌受難節翌日"),
            ("2023-04-10", "復活節星期一"),
            ("2023-05-01", "勞動節"),
            ("2023-05-26", "佛誕"),
            ("2023-06-22", "端午節"),
            ("2023-07-01", "香港特別行政區成立紀念日"),
            ("2023-09-30", "中秋節翌日"),
            ("2023-10-02", "國慶日翌日"),
            ("2023-10-23", "重陽節"),
            ("2023-12-25", "聖誕節"),
            ("2023-12-26", "聖誕節後第一個周日"),
        )

    def test_optional_2024(self):
        # https://www.gov.hk/en/about/abouthk/holiday/2024.htm
        self.assertOptionalHolidaysInYear(
            2024,
            ("2024-01-01", "一月一日"),
            ("2024-02-10", "農曆年初一"),
            ("2024-02-12", "農曆年初三"),
            ("2024-02-13", "農曆年初四"),
            ("2024-03-29", "耶穌受難節"),
            ("2024-03-30", "耶穌受難節翌日"),
            ("2024-04-01", "復活節星期一"),
            ("2024-04-04", "清明節"),
            ("2024-05-01", "勞動節"),
            ("2024-05-15", "佛誕"),
            ("2024-06-10", "端午節"),
            ("2024-07-01", "香港特別行政區成立紀念日"),
            ("2024-09-18", "中秋節翌日"),
            ("2024-10-01", "國慶日"),
            ("2024-10-11", "重陽節"),
            ("2024-12-25", "聖誕節"),
            ("2024-12-26", "聖誕節後第一個周日"),
        )

    def test_optional_2025(self):
        # https://www.gov.hk/en/about/abouthk/holiday/2025.htm
        self.assertOptionalHolidaysInYear(
            2025,
            ("2025-01-01", "一月一日"),
            ("2025-01-29", "農曆年初一"),
            ("2025-01-30", "農曆年初二"),
            ("2025-01-31", "農曆年初三"),
            ("2025-04-04", "清明節"),
            ("2025-04-18", "耶穌受難節"),
            ("2025-04-19", "耶穌受難節翌日"),
            ("2025-04-21", "復活節星期一"),
            ("2025-05-01", "勞動節"),
            ("2025-05-05", "佛誕"),
            ("2025-05-31", "端午節"),
            ("2025-07-01", "香港特別行政區成立紀念日"),
            ("2025-10-01", "國慶日"),
            ("2025-10-07", "中秋節翌日"),
            ("2025-10-29", "重陽節"),
            ("2025-12-25", "聖誕節"),
            ("2025-12-26", "聖誕節後第一個周日"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "一月一日"),
            ("2024-02-10", "農曆年初一"),
            ("2024-02-12", "農曆年初三"),
            ("2024-02-13", "農曆年初四"),
            ("2024-03-29", "耶穌受難節"),
            ("2024-03-30", "耶穌受難節翌日"),
            ("2024-04-01", "復活節星期一"),
            ("2024-04-04", "清明節"),
            ("2024-05-01", "勞動節"),
            ("2024-05-15", "佛誕"),
            ("2024-06-10", "端午節"),
            ("2024-07-01", "香港特別行政區成立紀念日"),
            ("2024-09-18", "中秋節翌日"),
            ("2024-10-01", "國慶日"),
            ("2024-10-11", "重陽節"),
            ("2024-12-25", "聖誕節"),
            ("2024-12-26", "聖誕節後第一個周日"),
        )

    def test_l10n_en_hk(self):
        self.assertLocalizedHolidays(
            "en_HK",
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

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-02-10", "Chinese New Year"),
            ("2024-02-12", "The third day of Chinese New Year"),
            ("2024-02-13", "The fourth day of Chinese New Year"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "The day following Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-04", "Tomb-Sweeping Day"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-15", "The Buddha's Birthday"),
            ("2024-06-10", "Dragon Boat Festival"),
            ("2024-07-01", "Hong Kong S.A.R. Establishment Day"),
            ("2024-09-18", "The Day following Mid-Autumn Festival"),
            ("2024-10-01", "National Day"),
            ("2024-10-11", "Double Ninth Festival"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "The first weekday after Christmas Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2024-01-01", "วันขึ้นปีใหม่"),
            ("2024-02-10", "วันตรุษจีน"),
            ("2024-02-12", "วันตรุษจีนวันที่สาม"),
            ("2024-02-13", "วันตรุษจีนวันที่สี่"),
            ("2024-03-29", "วันศุกร์ประเสริฐ"),
            ("2024-03-30", "วันหลังวันศุกร์ประเสริฐ"),
            ("2024-04-01", "วันจันทร์อีสเตอร์"),
            ("2024-04-04", "วันเช็งเม้ง"),
            ("2024-05-01", "วันแรงงาน"),
            ("2024-05-15", "วันวิสาขบูชา"),
            ("2024-06-10", "วันไหว้บ๊ะจ่าง"),
            ("2024-07-01", "วันสถาปนาเขตบริหารพิเศษฮ่องกง"),
            ("2024-09-18", "วันหลังวันไหว้พระจันทร์"),
            ("2024-10-01", "วันชาติจีน"),
            ("2024-10-11", "วันไหว้บรรพบุรุษ"),
            ("2024-12-25", "วันคริสต์มาส"),
            ("2024-12-26", "วันหลังวันคริสต์มาส"),
        )

    def test_l10n_zh_cn(self):
        self.assertLocalizedHolidays(
            "zh_CN",
            ("2024-01-01", "一月一日"),
            ("2024-02-10", "农历年初一"),
            ("2024-02-12", "农历年初三"),
            ("2024-02-13", "农历年初四"),
            ("2024-03-29", "耶稣受难节"),
            ("2024-03-30", "耶稣受难节翌日"),
            ("2024-04-01", "复活节星期一"),
            ("2024-04-04", "清明节"),
            ("2024-05-01", "劳动节"),
            ("2024-05-15", "佛诞"),
            ("2024-06-10", "端午节"),
            ("2024-07-01", "香港特别行政区成立纪念日"),
            ("2024-09-18", "中秋节翌日"),
            ("2024-10-01", "国庆日"),
            ("2024-10-11", "重阳节"),
            ("2024-12-25", "圣诞节"),
            ("2024-12-26", "圣诞节后第一个周日"),
        )
