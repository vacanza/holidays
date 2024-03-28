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

from holidays.countries.vanuatu import Vanuatu, VU, VTU
from tests.common import CommonCountryTests


class TestVanuatu(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Vanuatu, years=range(1981, 2050), years_non_observed=range(2000, 2024))

    def test_country_aliases(self):
        self.assertAliases(Vanuatu, VU, VTU)

    def test_no_holidays(self):
        self.assertNoHolidays(Vanuatu(years=1980))

    def test_special_holidays(self):
        self.assertHoliday(
            "2020-07-23",
            "2020-07-27",
            "2020-07-28",
            "2020-07-29",
            "2020-07-31",
            "2022-10-13",
        )

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1981, 2050)))
        dt = (
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_father_lini_day(self):
        name = "Father Lini Day"
        self.assertHolidayName(name, (f"{year}-02-21" for year in range(1999, 2050)))
        self.assertNoHolidayName(name, range(1981, 1999))
        self.assertNoHoliday(f"{year}-02-21" for year in range(1981, 1999))
        dt = (
            "2010-02-22",
            "2016-02-22",
            "2021-02-22",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_custom_chiefs_day(self):
        name = "Custom Chief's Day"
        self.assertHolidayName(name, (f"{year}-03-05" for year in range(1981, 2050)))
        dt = (
            "2000-03-06",
            "2006-03-06",
            "2017-03-06",
            "2023-03-06",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )
        self.assertHolidayName(name, range(1981, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )
        self.assertHolidayName(name, range(1981, 2050))

    def test_labour_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1981, 2050)))
        dt = (
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_ascension_day(self):
        name = "Ascension Day"
        self.assertHolidayName(
            name,
            "2018-05-10",
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
        )
        self.assertHolidayName(name, range(1981, 2050))

    def test_childrens_day(self):
        name = "Children's Day"
        self.assertHolidayName(name, (f"{year}-07-24" for year in range(1981, 2050)))
        dt = (
            "2005-07-25",
            "2011-07-25",
            "2016-07-25",
            "2022-07-25",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-07-30" for year in range(1981, 2050)))
        dt = (
            "2000-07-31",
            "2006-07-31",
            "2017-07-31",
            "2023-07-31",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_assumption_day(self):
        name = "Assumption Day"
        self.assertHolidayName(name, (f"{year}-08-15" for year in range(1981, 2050)))
        dt = (
            "2004-08-16",
            "2010-08-16",
            "2021-08-16",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertHolidayName(name, (f"{year}-10-05" for year in range(1981, 2050)))
        dt = (
            "2003-10-06",
            "2008-10-06",
            "2014-10-06",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_unity_day(self):
        name = "Unity Day"
        self.assertHolidayName(name, (f"{year}-11-29" for year in range(1981, 2050)))
        dt = (
            "2009-11-30",
            "2015-11-30",
            "2020-11-30",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(1981, 2050)))

    def test_family_day(self):
        name = "Family Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1981, 2050)))
        dt = (
            "2004-12-27",
            "2005-12-27",
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_2022(self):
        self.assertHolidays(
            Vanuatu(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-02-21", "Father Lini Day"),
            ("2022-03-05", "Custom Chief's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Labour Day (observed)"),
            ("2022-05-26", "Ascension Day"),
            ("2022-07-24", "Children's Day"),
            ("2022-07-25", "Children's Day (observed)"),
            ("2022-07-30", "Independence Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-10-05", "Constitution Day"),
            ("2022-10-13", "Election Day"),
            ("2022-11-29", "Unity Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Family Day"),
            ("2022-12-27", "Family Day (observed)"),
        )
