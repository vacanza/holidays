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

from holidays.countries.hongkong import HongKong, HK, HKG
from tests.common import CommonCountryTests


class TestHongKong(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HongKong, years=range(2006, 2024))

    def test_country_aliases(self):
        self.assertAliases(HongKong, HK, HKG)

    def test_no_holidays(self):
        self.assertNoHolidays(HongKong(years=1945))

    def test_special_holidays(self):
        self.assertHoliday("1997-07-02", "2015-09-03")

    def test_common(self):
        self.assertNonObservedHoliday("2019-01-01")
        self.assertNonObservedHolidayName(
            "The first day of January",
            "2019-01-01",
        )

    def test_first_day_of_january(self):
        exception_years = {2006, 2012, 2017, 2023}
        self.assertHolidayName(
            "The first day of January",
            (f"{year}-01-01" for year in set(range(2006, 2024)).difference(exception_years)),
        )
        self.assertHolidayName(
            "The day following The first day of January",
            (f"{year}-01-02" for year in exception_years),
        )

    def test_lunar_new_year(self):
        self.assertHolidayName(
            "The day preceding Lunar New Year's Day",
            "2006-01-28",
            "2007-02-17",
            "2010-02-13",
        )

        self.assertHolidayName(
            "Lunar New Year's Day",
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
        )

        self.assertHolidayName(
            "The second day of Lunar New Year",
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

        self.assertHolidayName(
            "The third day of Lunar New Year",
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
        )

        self.assertHolidayName(
            "The fourth day of Lunar New Year",
            "2013-02-13",
            "2014-02-03",
            "2017-01-31",
            "2018-02-19",
            "2020-01-28",
            "2021-02-15",
            "2023-01-25",
        )

    def test_ching_ming_festival(self):
        self.assertHolidayName(
            "Ching Ming Festival",
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
        )

        self.assertHolidayName(
            "The day following Ching Ming Festival",
            "2010-04-06",
            "2015-04-06",
            "2021-04-05",
        )

    def test_easter(self):
        self.assertHolidayName(
            "Good Friday",
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
        )

        self.assertHolidayName(
            "The day following Good Friday",
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
        )

        self.assertHolidayName(
            "Easter Monday",
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
        )

        self.assertHolidayName("The day following Easter Monday", "2015-04-07", "2021-04-06")

    def test_birthday_of_buddha(self):
        name = "The Birthday of the Buddha"
        name_following = f"The day following {name}"

        self.assertHolidayName(
            name,
            "1999-05-22",
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
        )

        self.assertHolidayName(name_following, "2019-05-13", "2022-05-09")

        self.assertNoHolidayName(name, 1998)
        self.assertNoHolidayName(name_following, 1998)

    def test_labour_day(self):
        exception_years = {2005, 2011, 2016, 2022}
        name = "Labour Day"
        name_following = f"The day following {name}"
        self.assertHolidayName(
            name, (f"{year}-05-01" for year in set(range(1999, 2024)).difference(exception_years))
        )
        self.assertHolidayName(name_following, (f"{year}-05-02" for year in exception_years))
        self.assertNoHolidayName(name, 1998)
        self.assertNoHolidayName(name_following, 1998)

    def test_tuen_ng_festival(self):
        self.assertHolidayName(
            "Tuen Ng Festival",
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
        )

        self.assertHolidayName("The day following Tuen Ng Festival", "2008-06-09")

    def test_hksar_day(self):
        exception_years = {2001, 2007, 2012, 2018}
        name = "Hong Kong Special Administrative Region Establishment Day"
        name_following = f"The day following {name}"
        self.assertHolidayName(
            name, (f"{year}-07-01" for year in set(range(1997, 2024)).difference(exception_years))
        )
        self.assertHolidayName(name_following, (f"{year}-07-02" for year in exception_years))
        self.assertNoHolidayName(name, 1996)
        self.assertNoHolidayName(name_following, 1996)

    def test_mid_autumn_festival(self):
        self.assertHolidayName(
            "The day following the Chinese Mid-Autumn Festival",
            "2003-09-12",
            "2004-09-29",
            "2005-09-19",
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
            "2025-10-07",
            "2026-09-26",
        )

        self.assertHolidayName("Chinese Mid-Autumn Festival", "2002-09-21", "2009-10-03")

        self.assertHolidayName(
            "The second day of the Chinese Mid-Autumn Festival (Monday)",
            "2022-09-12",
        )

    def test_national_day(self):
        exception_years = {2000, 2006, 2012, 2017, 2023}
        name = "National Day"
        name_following = f"The day following {name}"
        self.assertHolidayName(
            name, (f"{year}-10-01" for year in set(range(1997, 2024)).difference(exception_years))
        )
        self.assertHolidayName(name, "1997-10-02", "1998-10-02")
        self.assertHolidayName(name_following, (f"{year}-10-02" for year in exception_years))
        self.assertNoHolidayName(name, 1996)
        self.assertNoHolidayName(name_following, 1996)

    def test_chung_yeung_festival(self):
        self.assertHolidayName(
            "Chung Yeung Festival",
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
        )

        self.assertHolidayName(
            "The day following Chung Yeung Festival",
            "2013-10-14",
            "2016-10-10",
            "2020-10-26",
        )

    def test_christmas_day(self):
        exception_years = {2011, 2016, 2022}
        name = "Christmas Day"
        self.assertHolidayName(
            name, (f"{year}-12-25" for year in set(range(2006, 2024)).difference(exception_years))
        )
        self.assertNoHolidayName(name, exception_years)

        exception_years = {2010, 2021}
        name = "The first weekday after Christmas Day"
        self.assertHolidayName(
            name, (f"{year}-12-26" for year in set(range(2006, 2024)).difference(exception_years))
        )
        self.assertHolidayName(name, (f"{year}-12-27" for year in exception_years))

        self.assertHolidayName(
            "The second weekday after Christmas Day",
            "2011-12-27",
            "2016-12-27",
            "2022-12-27",
        )

    def test_old_holidays(self):
        self.assertHoliday(
            # Queen's Birthday
            "1952-06-09",
            "1987-06-08",
            "1990-06-11",
            "1997-06-09",
            # Anniversary of the liberation of Hong Kong
            "1980-08-24",
            "1990-08-26",
            "1996-08-25",
            # Anniversary of the victory in the Second Sino-Japanese War
            "1980-08-25",
            "1990-08-27",
            "1996-08-26",
            "1997-08-24",
            "1998-08-30",
        )

        self.assertNoHolidayName("Queen's Birthday", 1951, 1998)
        self.assertNoHolidayName("Anniversary of the liberation of Hong Kong", 1997)
        self.assertNoHolidayName(
            "Anniversary of the victory in the Second Sino-Japanese War", 1999
        )
