#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.barbados import Barbados, BB, BRB
from tests.common import CommonCountryTests


class TestBarbados(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Barbados, years=range(1969, 2050), years_non_observed=range(2000, 2024))

    def test_country_aliases(self):
        self.assertAliases(Barbados, BB, BRB)

    def test_no_holidays(self):
        self.assertNoHolidays(Barbados(years=1968))

    def test_special_holidays(self):
        self.assertHoliday(
            "2021-01-04",
            "2021-01-05",
            "2023-07-31",
        )

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1969, 2050)))
        dt = (
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_errol_barrow_day(self):
        name = "Errol Barrow Day"
        self.assertHolidayName(name, (f"{year}-01-21" for year in range(1989, 2050)))
        self.assertNoHoliday(f"{year}-01-21" for year in range(1969, 1989))
        self.assertNoHolidayName(name, range(1969, 1989))
        dt = (
            "2001-01-22",
            "2007-01-22",
            "2018-01-22",
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
        self.assertHolidayName(name, range(1969, 2050))

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
        self.assertHolidayName(name, range(1969, 2050))

    def test_national_heroes_day(self):
        name = "National Heroes Day"
        self.assertHolidayName(name, (f"{year}-04-28" for year in range(1998, 2050)))
        self.assertNoHoliday(f"{year}-04-28" for year in range(1969, 1998))
        self.assertNoHolidayName(name, range(1969, 1998))
        dt = (
            "2002-04-29",
            "2013-04-29",
            "2019-04-29",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_may_day(self):
        name = "May Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1969, 2050)))
        dt = (
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_whit_monday(self):
        name = "Whit Monday"
        self.assertHolidayName(
            name,
            "2018-05-21",
            "2019-06-10",
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
        )
        self.assertHolidayName(name, range(1969, 2050))

    def test_emancipation_day(self):
        name = "Emancipation Day"
        self.assertHolidayName(name, (f"{year}-08-01" for year in range(1969, 2050)))
        dt = (
            "2004-08-03",
            "2005-08-02",
            "2010-08-03",
            "2011-08-02",
            "2016-08-02",
            "2021-08-03",
            "2022-08-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_kadooment_day(self):
        name = "Kadooment Day"
        self.assertHolidayName(
            name,
            "2018-08-06",
            "2019-08-05",
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
        )
        self.assertHolidayName(name, range(1969, 2050))

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-11-30" for year in range(1969, 2050)))
        dt = (
            "2003-12-01",
            "2008-12-01",
            "2014-12-01",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1969, 2050)))
        dt = (
            "2005-12-27",
            "2011-12-27",
            "2016-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1969, 2050)))
        dt = (
            "2004-12-27",
            "2010-12-27",
            "2021-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_2022(self):
        self.assertHolidays(
            Barbados(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-01-21", "Errol Barrow Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-28", "National Heroes Day"),
            ("2022-05-01", "May Day"),
            ("2022-05-02", "May Day (observed)"),
            ("2022-06-06", "Whit Monday"),
            ("2022-08-01", "Emancipation Day; Kadooment Day"),
            ("2022-08-02", "Emancipation Day (observed)"),
            ("2022-11-30", "Independence Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_2023(self):
        self.assertHolidays(
            Barbados(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-21", "Errol Barrow Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-28", "National Heroes Day"),
            ("2023-05-01", "May Day"),
            ("2023-05-29", "Whit Monday"),
            ("2023-07-31", "50th Anniversary of CARICOM Holiday"),
            ("2023-08-01", "Emancipation Day"),
            ("2023-08-07", "Kadooment Day"),
            ("2023-11-30", "Independence Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )
