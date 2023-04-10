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

import warnings

from holidays.countries.south_korea import SouthKorea, KR, KOR, Korea
from tests.common import TestCase


class TestSouthKorea(TestCase):
    @classmethod
    def setUpClass(cls):
        years = [1944, 1945, 1947, 1948, 1949, 1960, 1974, 1975] + list(
            range(1981, 2031)
        )
        super().setUpClass(SouthKorea, years=years)

    def test_country_aliases(self):
        self.assertCountryAliases(SouthKorea, KR, KOR)

    def test_common(self):
        self.assertNonObservedHolidaysName("New Year's Day", "2019-01-01")

    def test_first_day_of_january(self):
        self.assertHolidaysName(
            "New Year's Day", (f"{year}-01-01" for year in range(2001, 2031))
        )

    def test_lunar_new_year(self):
        self.assertHolidaysName(
            "The day preceding of Lunar New Year's Day",
            "2014-01-30",
            "2015-02-18",
            "2016-02-07",
            "2017-01-27",
            "2018-02-15",
            "2019-02-04",
            "2020-01-24",
            "2021-02-11",
            "2022-01-31",
            "2023-01-21",
        )

        self.assertHolidaysName(
            "Lunar New Year's Day",
            "1988-02-18",
            "1997-02-08",
            "2008-02-07",
            "2009-01-26",
            "2010-02-14",
            "2011-02-03",
            "2012-01-23",
            "2013-02-10",
            "2014-01-31",
            "2015-02-19",
            "2016-02-08",
            "2017-01-28",
            "2018-02-16",
            "2019-02-05",
            "2020-01-25",
            "2021-02-12",
            "2022-02-01",
            "2023-01-22",
        )

        self.assertHolidaysName(
            "The second day of Lunar New Year's Day",
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
            "2017-01-29",
            "2018-02-17",
            "2019-02-06",
            "2020-01-26",
            "2021-02-13",
            "2022-02-02",
            "2023-01-23",
        )

        self.assertHolidaysName(
            "Alternative holiday of Lunar New Year's Day",
            "2016-02-10",
            "2017-01-30",
            "2020-01-27",
            "2023-01-24",
            "2024-02-12",
            "2027-02-09",
        )

        self.assertNoHoliday("2015-02-07", "2015-02-21")

    def test_independence_movement_day(self):
        self.assertHolidaysName(
            "Independence Movement Day",
            (f"{year}-03-01" for year in range(2001, 2031)),
        )

        self.assertHolidaysName(
            "Alternative holiday of Independence Movement Day",
            "2025-03-03",
            "2026-03-02",
        )

    def test_tree_planting_day(self):
        name = "Tree Planting Day"
        self.assertHolidaysName(
            name, (f"{year}-04-05" for year in range(2001, 2006))
        )
        self.assertHolidaysName(name, "1949-04-05")
        self.assertNoHolidayNameInYears(name, 1948, 1960, 2006)
        self.assertNoHoliday("1948-04-05", "1960-04-05", "2006-04-05")

    def test_childrens_day(self):
        name = "Children's Day"
        self.assertHolidaysName(
            name,
            (f"{year}-05-05" for year in range(2001, 2031)),
        )
        self.assertHolidaysName(name, "1975-05-05")
        self.assertNoHolidayNameInYears(name, 1974)
        self.assertNoHoliday("1974-05-05")

        self.assertHolidaysName(
            "Alternative holiday of Children's Day",
            "2018-05-07",
            "2019-05-06",
            "2024-05-06",
            "2025-05-06",
            "2029-05-07",
            "2030-05-06",
        )

    def test_birthday_of_buddha(self):
        self.assertHolidaysName(
            "Birthday of the Buddha",
            "2006-05-05",
            "2007-05-24",
            "2008-05-12",
            "2009-05-02",
            "2010-05-21",
            "2011-05-10",
            "2012-05-28",
            "2013-05-17",
            "2014-05-06",
            "2015-05-25",
            "2016-05-14",
            "2017-05-03",
            "2018-05-22",
            "2019-05-12",
            "2020-04-30",
            "2021-05-19",
            "2022-05-08",
            "2023-05-27",
        )

    def test_labour_day(self):
        name = "Labour Day"
        self.assertHolidaysName(
            name,
            (f"{year}-03-10" for year in range(1990, 1994)),
        )
        self.assertHolidaysName(
            name,
            (f"{year}-05-01" for year in range(1994, 2031)),
        )
        self.assertNoHoliday("1993-05-01", "1994-03-10")

    def test_memorial_day(self):
        self.assertHolidaysName(
            "Memorial Day",
            (f"{year}-06-06" for year in range(2001, 2031)),
        )

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertHolidaysName(
            name,
            (f"{year}-07-17" for year in range(2001, 2008)),
        )
        self.assertHolidaysName(name, "1948-07-17")
        self.assertNoHoliday("1947-07-17", "2008-07-17")
        self.assertNoHolidayNameInYears(name, 1947, 2008)

    def test_liberation_day(self):
        name = "Liberation Day"
        self.assertHolidaysName(
            name,
            (f"{year}-08-15" for year in range(2001, 2031)),
        )
        self.assertHolidaysName(name, "1945-08-15")
        self.assertNoHoliday("1944-08-15")
        self.assertNoHolidayNameInYears(name, 1944)

        self.assertHolidaysName(
            "Alternative holiday of Liberation Day",
            "2021-08-16",
            "2026-08-17",
            "2027-08-16",
        )

    def test_chuseok(self):
        self.assertHolidaysName(
            "The day preceding of Chuseok",
            "2014-09-07",
            "2015-09-26",
            "2016-09-14",
            "2017-10-03",
            "2018-09-23",
            "2019-09-12",
            "2020-09-30",
            "2021-09-20",
            "2022-09-09",
            "2023-09-28",
        )

        self.assertHolidaysName(
            "Chuseok",
            "1942-09-25",
            "1978-09-17",
            "2010-09-22",
            "2011-09-12",
            "2012-09-30",
            "2013-09-19",
            "2014-09-08",
            "2015-09-27",
            "2016-09-15",
            "2017-10-04",
            "2018-09-24",
            "2019-09-13",
            "2020-10-01",
            "2021-09-21",
            "2022-09-10",
            "2023-09-29",
        )

        self.assertHolidaysName(
            "The second day of Chuseok",
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
            "2022-09-11",
            "2023-09-30",
        )

        self.assertHolidaysName(
            "Alternative holiday of Chuseok",
            "2014-09-10",
            "2015-09-29",
            "2018-09-26",
            "2022-09-12",
            "2025-10-08",
            "2029-09-24",
        )

    def test_national_foundation_day(self):
        self.assertHolidaysName(
            "National Foundation Day",
            (f"{year}-10-03" for year in range(2001, 2031)),
        )

        self.assertHolidaysName(
            "Alternative holiday of National Foundation Day",
            "2021-10-04",
            "2026-10-05",
            "2027-10-04",
        )

    def test_hangeul_day(self):
        name = "Hangeul Day"
        self.assertHolidaysName(
            name,
            (f"{year}-10-09" for year in range(1981, 1991)),
        )
        self.assertHolidaysName(
            name,
            (f"{year}-10-09" for year in range(2013, 2031)),
        )
        self.assertHolidaysName(name, "1990-10-09", "2013-10-09")
        self.assertNoHoliday("1991-10-09", "2012-10-09")
        self.assertNoHolidayNameInYears(name, 1991, 2012)

        self.assertHolidaysName(
            "Alternative holiday of Hangeul Day",
            "2021-10-11",
            "2022-10-10",
            "2027-10-11",
        )

    def test_christmas_day(self):
        self.assertHolidaysName(
            "Christmas Day",
            (f"{year}-12-25" for year in range(2001, 2031)),
        )

    def test_special_holidays(self):
        self.assertHoliday("2020-08-17")

    def test_korea_deprecation_warning(self):
        warnings.simplefilter("default")
        with self.assertWarns(Warning):
            Korea()

        warnings.simplefilter("error")
        with self.assertRaises(Warning):
            Korea()
