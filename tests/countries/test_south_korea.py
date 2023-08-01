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

from holidays.constants import BANK
from holidays.countries.south_korea import SouthKorea, KR, KOR, Korea
from tests.common import TestCase


class TestSouthKorea(TestCase):
    @classmethod
    def setUpClass(cls):
        years = (1948, 1949, 1960, 1974, 1975) + tuple(range(1981, 2050))
        super().setUpClass(SouthKorea, years=years)

    def test_country_aliases(self):
        self.assertCountryAliases(SouthKorea, KR, KOR)

    def test_no_holidays(self):
        self.assertNoHolidays(SouthKorea(years=1947))
        self.assertNoHolidays(SouthKorea(categories=(BANK,), years=1947))

    def test_special_holidays(self):
        self.assertHoliday(
            "2016-04-13",
            "2017-05-09",
            "2018-06-13",
            "2020-04-15",
            "2020-08-17",
            "2022-03-09",
            "2022-06-01",
        )

    def test_common(self):
        self.assertNonObservedHolidayName("New Year's Day", "2019-01-01")

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1981, 2050)))
        self.assertHolidayName(name, (f"{year}-01-02" for year in range(1981, 1999)))
        self.assertNoHoliday(f"{year}-01-02" for year in range(1999, 2050))

    def test_lunar_new_year(self):
        name = "Lunar New Year"
        self.assertHolidayName(
            f"The day preceding {name}",
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

        self.assertHolidayName(
            name,
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

        self.assertHolidayName(
            f"The second day of {name}",
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

        self.assertHolidayName(
            f"Alternative holiday for {name}",
            "2016-02-10",
            "2017-01-30",
            "2020-01-27",
            "2023-01-24",
            "2024-02-12",
            "2027-02-09",
        )

        self.assertNoHoliday("2015-02-07", "2015-02-21")

    def test_independence_movement_day(self):
        name = "Independence Movement Day"
        self.assertHolidayName(name, (f"{year}-03-01" for year in range(2001, 2050)))

        self.assertHolidayName(
            f"Alternative holiday for {name}",
            "2025-03-03",
            "2026-03-02",
        )

    def test_tree_planting_day(self):
        name = "Tree Planting Day"
        self.assertHolidayName(name, (f"{year}-04-05" for year in range(1981, 2006)))
        self.assertHolidayName(name, "1949-04-05")
        self.assertNoHolidayName(name, 1948, 1960, range(2006, 2050))
        self.assertNoHoliday(
            "1948-04-05", "1960-04-05", (f"{year}-04-05" for year in range(2006, 2050))
        )

    def test_childrens_day(self):
        name = "Children's Day"
        self.assertHolidayName(name, (f"{year}-05-05" for year in range(2001, 2050)))
        self.assertHolidayName(name, "1975-05-05")
        self.assertNoHolidayName(name, 1974)
        self.assertNoHoliday("1974-05-05")

        self.assertHolidayName(
            f"Alternative holiday for {name}",
            "2018-05-07",
            "2019-05-06",
            "2024-05-06",
            "2025-05-06",
            "2029-05-07",
            "2030-05-06",
        )

    def test_birthday_of_buddha(self):
        name = "Buddha's Birthday"
        self.assertHolidayName(
            name,
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
            "2024-05-15",
            "2025-05-05",
            "2026-05-24",
            "2027-05-13",
            "2028-05-02",
            "2029-05-20",
        )

        self.assertHolidayName(
            f"Alternative holiday for {name}",
            "2023-05-29",
            "2026-05-25",
            "2029-05-21",
        )

        self.assertNoHoliday("2022-05-09")

    def test_memorial_day(self):
        self.assertHolidayName("Memorial Day", (f"{year}-06-06" for year in range(2001, 2050)))

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertHolidayName(name, (f"{year}-07-17" for year in range(1981, 2008)))
        self.assertNoHoliday(f"{year}-07-17" for year in range(2008, 2050))
        self.assertNoHolidayName(name, range(2008, 2050))

    def test_liberation_day(self):
        name = "Liberation Day"
        self.assertHolidayName(name, (f"{year}-08-15" for year in range(2001, 2050)))

        self.assertHolidayName(
            f"Alternative holiday for {name}",
            "2021-08-16",
            "2026-08-17",
            "2027-08-16",
        )

    def test_chuseok(self):
        self.assertHolidayName(
            "The day preceding Chuseok",
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

        self.assertHolidayName(
            "Chuseok",
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

        self.assertHolidayName(
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

        self.assertHolidayName(
            "Alternative holiday for Chuseok",
            "2014-09-10",
            "2015-09-29",
            "2018-09-26",
            "2022-09-12",
            "2025-10-08",
            "2029-09-24",
        )

    def test_national_foundation_day(self):
        name = "National Foundation Day"
        self.assertHolidayName(name, (f"{year}-10-03" for year in range(2001, 2050)))

        self.assertHolidayName(
            f"Alternative holiday for {name}",
            "2021-10-04",
            "2026-10-05",
            "2027-10-04",
        )

    def test_hangul_day(self):
        name = "Hangul Day"
        self.assertHolidayName(name, (f"{year}-10-09" for year in range(1981, 1991)))
        self.assertHolidayName(name, (f"{year}-10-09" for year in range(2013, 2050)))
        self.assertNoHoliday(f"{year}-10-09" for year in range(1991, 2013))
        self.assertNoHolidayName(name, range(1991, 2013))

        self.assertHolidayName(
            f"Alternative holiday for {name}",
            "2021-10-11",
            "2022-10-10",
            "2027-10-11",
        )

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(2001, 2050)))

        self.assertHolidayName(
            f"Alternative holiday for {name}",
            "2027-12-27",
            "2032-12-27",
            "2033-12-26",
        )

        self.assertNoHoliday("2022-12-26")

    def test_labour_day(self):
        name = "Labour Day"
        holidays = SouthKorea(categories=(BANK,), years=range(1990, 2050))
        self.assertHolidayName(name, holidays, (f"{year}-03-10" for year in range(1990, 1994)))
        self.assertHolidayName(name, holidays, (f"{year}-05-01" for year in range(1994, 2050)))
        self.assertNoHoliday(holidays, "1993-05-01", "1994-03-10")

    def test_korea_deprecation_warning(self):
        warnings.simplefilter("default")
        with self.assertWarns(Warning):
            Korea()

        warnings.simplefilter("error")
        with self.assertRaises(Warning):
            Korea()
