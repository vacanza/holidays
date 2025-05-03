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

from holidays.countries.grenada import Grenada, GD, GRD
from tests.common import CommonCountryTests


class TestGrenada(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1975, 2050)
        super().setUpClass(Grenada, years=years, years_non_observed=years)

    def test_country_aliases(self):
        self.assertAliases(Grenada, GD, GRD)

    def test_no_holidays(self):
        self.assertNoHolidays(Grenada(years=1974))

    def test_special_holidays(self):
        self.assertHoliday(
            "2012-04-27",
            "2012-04-28",
            "2012-04-29",
            "2012-10-16",
            "2012-10-17",
            "2012-10-18",
            "2012-10-19",
            "2012-10-20",
            "2012-11-30",
            "2012-12-01",
            "2012-12-02",
            "2013-04-26",
            "2013-04-27",
            "2013-04-28",
            "2013-10-16",
            "2013-10-17",
            "2013-10-18",
            "2013-10-19",
            "2013-10-20",
            "2013-11-29",
            "2013-11-30",
            "2013-12-01",
            "2014-04-25",
            "2014-04-26",
            "2014-04-27",
            "2014-10-15",
            "2014-10-16",
            "2014-10-17",
            "2014-10-18",
            "2014-10-19",
            "2014-12-05",
            "2014-12-06",
            "2014-12-07",
            "2015-04-24",
            "2015-04-25",
            "2015-04-26",
            "2015-10-15",
            "2015-10-16",
            "2015-10-17",
            "2015-10-18",
            "2015-10-19",
            "2015-12-04",
            "2015-12-05",
            "2015-12-06",
            "2023-07-04",
        )

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1975, 2050)))
        dt = (
            "1978-01-02",
            "1984-01-02",
            "1989-01-02",
            "1995-01-02",
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
            "2034-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNonObservedHoliday(dt)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-02-07" for year in range(1975, 2050)))
        dt = (
            "1982-02-08",
            "1988-02-08",
            "1993-02-08",
            "1999-02-08",
            "2010-02-08",
            "2016-02-08",
            "2021-02-08",
            "2027-02-08",
            "2038-02-08",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNonObservedHoliday(dt)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
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
            "2025-04-18",
        )
        self.assertHolidayName(name, range(1975, 2050))

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2015-04-06",
            "2016-03-28",
            "2017-04-17",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
        )
        self.assertHolidayName(name, range(1975, 2050))

    def test_labor_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1975, 2050)))
        dt = (
            "1977-05-02",
            "1983-05-02",
            "1988-05-02",
            "1994-05-02",
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
            "2033-05-02",
            "2039-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNonObservedHoliday(dt)

    def test_whit_monday(self):
        name = "Whit Monday"
        self.assertHolidayName(
            name,
            "2015-05-25",
            "2016-05-16",
            "2017-06-05",
            "2018-05-21",
            "2019-06-10",
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, range(1975, 2050))

    def test_corpus_christi_day(self):
        name = "Corpus Christi"
        self.assertHolidayName(
            name,
            "2015-06-04",
            "2016-05-26",
            "2017-06-15",
            "2018-05-31",
            "2019-06-20",
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
            "2025-06-19",
        )
        self.assertHolidayName(name, range(1975, 2050))

    def emancipation_day(self):
        name = "Emancipation Day"
        self.assertHolidayName(
            name,
            "2015-08-03",
            "2016-08-01",
            "2017-08-07",
            "2018-08-06",
            "2019-08-05",
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
        )
        self.assertHolidayName(name, range(1975, 2024))
        self.assertHolidayName(name, (f"{year}-08-01" for year in range(2025, 2050)))
        dt = (
            "2027-08-02",
            "2032-08-02",
            "2038-08-02",
            "2049-08-02",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNonObservedHoliday(dt)

    def test_carnival_monday_day(self):
        name = "Carnival Monday"
        self.assertHolidayName(
            name,
            "2015-08-10",
            "2016-08-08",
            "2017-08-14",
            "2018-08-13",
            "2019-08-12",
            "2020-08-10",
            "2021-08-09",
            "2022-08-08",
            "2023-08-14",
            "2024-08-12",
            "2025-08-11",
        )
        self.assertHolidayName(name, range(1975, 2050))

    def test_carnival_tuesday_day(self):
        name = "Carnival Tuesday"
        self.assertHolidayName(
            name,
            "2015-08-11",
            "2016-08-09",
            "2017-08-08",
            "2018-08-14",
            "2019-08-13",
            "2020-08-11",
            "2021-08-10",
            "2022-08-09",
            "2023-08-08",
            "2024-08-13",
            "2025-08-12",
        )
        self.assertHolidayName(name, range(1975, 2050))

    def test_national_heroes_day(self):
        name = "National Heroes' Day"
        self.assertHolidayName(name, (f"{year}-10-19" for year in range(2023, 2050)))
        dt = (
            "2025-10-20",
            "2031-10-20",
            "2036-10-20",
            "2042-10-20",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNonObservedHoliday(dt)

    def test_thanksgiving_day(self):
        name = "Thanksgiving Day"
        self.assertHolidayName(name, (f"{year}-10-25" for year in range(1975, 2050)))
        dt = (
            "1981-10-26",
            "1987-10-26",
            "1992-10-26",
            "1998-10-26",
            "2009-10-26",
            "2015-10-26",
            "2020-10-26",
            "2026-10-26",
            "2037-10-26",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNonObservedHoliday(dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1975, 2050)))
        dt = (
            "1977-12-26",
            "1983-12-26",
            "1988-12-26",
            "1994-12-26",
            "2005-12-26",
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
            "2033-12-26",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNonObservedHoliday(dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1975, 2050)))
        dt = (
            "1976-12-27",
            "1982-12-27",
            "1993-12-27",
            "1999-12-27",
            "2004-12-27",
            "2010-12-27",
            "2021-12-27",
            "2027-12-27",
            "2032-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", dt)
        self.assertNonObservedHoliday(dt)
