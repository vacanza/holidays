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

from holidays.countries.united_kingdom import UnitedKingdom, UK, GB, GBR
from tests.common import TestCase


class TestUnitedKingdom(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            UnitedKingdom, years=range(1950, 2050), years_non_observed=range(2000, 2024)
        )

        warnings.simplefilter("ignore", category=DeprecationWarning)
        cls.subdiv_holidays = {
            subdiv: UnitedKingdom(subdiv=subdiv, years=(range(1950, 2050)))
            for subdiv in set(UnitedKingdom.subdivisions).union(
                set(UnitedKingdom._deprecated_subdivisions)
            )
        }

    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_country_aliases(self):
        self.assertCountryAliases(UnitedKingdom, UK, GBR)
        self.assertCountryAliases(UnitedKingdom, GB, GBR)

    def test_special_holidays(self):
        self.assertHoliday(
            "1977-06-07",
            "1981-07-29",
            "1999-12-31",
            "2002-06-03",
            "2011-04-29",
            "2012-06-05",
            "2022-06-03",
            "2022-09-19",
            "2023-05-08",
        )

    def test_new_years(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1974, 2050)))
        self.assertNoHolidayName(name, range(1950, 1974))
        obs_dt = (
            "2000-01-03",
            "2005-01-03",
            "2006-01-02",
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (Observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_new_year_scotland(self):
        name_new_year = "New Year's Day"
        name_new_year_holiday = "New Year Holiday"
        ny_obs_dt = (
            "2000-01-04",
            "2005-01-04",
            "2006-01-02",
            "2011-01-04",
            "2012-01-02",
            "2017-01-02",
            "2022-01-04",
        )
        nyh_obs_dt = (
            "2000-01-03",
            "2005-01-03",
            "2006-01-03",
            "2010-01-04",
            "2011-01-03",
            "2012-01-03",
            "2016-01-04",
            "2017-01-03",
            "2021-01-04",
            "2022-01-03",
        )

        for subdiv in ("SCT", "Scotland"):
            holidays = self.subdiv_holidays[subdiv]
            self.assertHolidayName(
                name_new_year, holidays, (f"{year}-01-01" for year in range(1950, 2050))
            )
            self.assertHolidayName(f"{name_new_year} (Observed)", holidays, ny_obs_dt)
            self.assertHolidayName(
                name_new_year_holiday, holidays, (f"{year}-01-02" for year in range(1950, 2050))
            )
            self.assertHolidayName(f"{name_new_year_holiday} (Observed)", holidays, nyh_obs_dt)
            self.assertNoNonObservedHoliday(
                UnitedKingdom(subdiv=subdiv, observed=False), nyh_obs_dt
            )

        for subdiv in (
            "ENG",
            "NIR",
            "WLS",
            "England",
            "Northern Ireland",
            "Wales",
        ):
            self.assertNoHolidayName(
                name_new_year_holiday, self.subdiv_holidays[subdiv], range(1950, 2050)
            )

    def test_st_patricks_day(self):
        name = "St. Patrick's Day"
        obs_dt = (
            "2001-03-19",
            "2002-03-18",
            "2007-03-19",
            "2012-03-19",
            "2013-03-18",
            "2018-03-19",
            "2019-03-18",
        )
        for subdiv in ("NIR", "Northern Ireland"):
            self.assertHolidayName(
                name, self.subdiv_holidays[subdiv], (f"{year}-03-17" for year in range(1950, 2050))
            )
            self.assertHolidayName(f"{name} (Observed)", self.subdiv_holidays[subdiv], obs_dt)
            self.assertNoNonObservedHoliday(UnitedKingdom(subdiv=subdiv, observed=False), obs_dt)

        for subdiv in ("ENG", "SCT", "WLS", "England", "Scotland", "Wales"):
            self.assertNoHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-03-17" for year in range(1950, 2050))
            )
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv], range(1950, 2050))
        self.assertNoHoliday(f"{year}-03-17" for year in range(1950, 2050))
        self.assertNoHolidayName(name, range(1950, 2050))

    def test_good_friday(self):
        self.assertHolidayName(
            "Good Friday",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )

    def test_easter_monday(self):
        name = "Easter Monday"
        dt = (
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )
        for subdiv in (
            "ENG",
            "NIR",
            "WLS",
            "England",
            "Northern Ireland",
            "Wales",
        ):
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], dt)

        for subdiv in ("SCT", "Scotland"):
            self.assertNoHoliday(self.subdiv_holidays[subdiv], dt)
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv], range(1950, 2050))

        self.assertNoHoliday(dt)
        self.assertNoHolidayName(name, range(1950, 2050))

    def test_may_day(self):
        name = "May Day"
        self.assertHolidayName(
            name,
            "1978-05-01",
            "1979-05-07",
            "1980-05-05",
            "1995-05-08",
            "1999-05-03",
            "2000-05-01",
            "2010-05-03",
            "2016-05-02",
            "2018-05-07",
            "2019-05-06",
            "2020-05-08",
        )
        self.assertNoHolidayName(name, range(1950, 1978))

    def test_spring_bank_holiday(self):
        name = "Spring Bank Holiday"
        self.assertHolidayName(
            name,
            "2001-05-28",
            "2002-06-04",
            "2003-05-26",
            "2011-05-30",
            "2012-06-04",
            "2013-05-27",
            "2018-05-28",
            "2019-05-27",
            "2020-05-25",
            "2021-05-31",
            "2022-06-02",
            "2023-05-29",
        )
        self.assertNoHolidayName(name, range(1950, 1971))

    def test_battle_of_the_boyne_day(self):
        name = "Battle of the Boyne"
        for subdiv in ("NIR", "Northern Ireland"):
            self.assertHolidayName(
                name, self.subdiv_holidays[subdiv], (f"{year}-07-12" for year in range(1950, 2050))
            )

        for subdiv in ("ENG", "SCT", "WLS", "England", "Scotland", "Wales"):
            self.assertNoHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-07-12" for year in range(1950, 2050))
            )
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv], range(1950, 2050))
        self.assertNoHoliday(f"{year}-07-12" for year in range(1950, 2050))
        self.assertNoHolidayName(name, range(1950, 2050))

    def test_summer_bank_holiday(self):
        name = "Summer Bank Holiday"
        dt = (
            "2001-08-06",
            "2002-08-05",
            "2003-08-04",
            "2011-08-01",
            "2012-08-06",
            "2013-08-05",
            "2018-08-06",
            "2019-08-05",
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
        )
        for subdiv in ("SCT", "Scotland"):
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], dt)

        for subdiv in (
            "ENG",
            "NIR",
            "WLS",
            "England",
            "Northern Ireland",
            "Wales",
        ):
            self.assertNoHoliday(self.subdiv_holidays[subdiv], dt)
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv], range(1950, 2050))

        self.assertNoHoliday(dt)
        self.assertNoHolidayName(name, range(1950, 2050))

    def test_late_summer_bank_holiday(self):
        name = "Late Summer Bank Holiday"
        dt = (
            "2001-08-27",
            "2002-08-26",
            "2003-08-25",
            "2011-08-29",
            "2012-08-27",
            "2013-08-26",
            "2018-08-27",
            "2019-08-26",
            "2020-08-31",
            "2021-08-30",
            "2022-08-29",
            "2023-08-28",
        )

        for subdiv in (
            "ENG",
            "NIR",
            "WLS",
            "England",
            "Northern Ireland",
            "Wales",
        ):
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], dt)
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], range(1971, 2050))
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv], range(1950, 1971))

        for subdiv in ("SCT", "Scotland"):
            self.assertNoHoliday(self.subdiv_holidays[subdiv], dt)
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv], range(1950, 2050))

        self.assertNoHoliday(dt)
        self.assertNoHolidayName(name, range(1950, 2050))

    def test_st_andrews_day(self):
        name = "St. Andrew's Day"
        for subdiv in ("SCT", "Scotland"):
            self.assertHolidayName(
                name, self.subdiv_holidays[subdiv], (f"{year}-11-30" for year in range(1950, 2050))
            )
        for subdiv in (
            "ENG",
            "NIR",
            "WLS",
            "England",
            "Northern Ireland",
            "Wales",
        ):
            self.assertNoHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-11-30" for year in range(1950, 2050))
            )
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv], range(1950, 2050))
        self.assertNoHoliday(f"{year}-11-30" for year in range(1950, 2050))
        self.assertNoHolidayName(name, range(1950, 2050))

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1950, 2050)))
        obs_dt = (
            "2004-12-27",
            "2005-12-27",
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (Observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1950, 2050)))
        obs_dt = (
            "2004-12-28",
            "2009-12-28",
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (Observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_all_holidays_present(self):
        uk_2015 = sum(
            UnitedKingdom(years=2015, subdiv=subdiv, observed=False)
            for subdiv in UnitedKingdom.subdivisions
        )
        y_2015 = set(uk_2015.values())
        all_holidays = {
            "New Year's Day",
            "New Year Holiday",
            "St. Patrick's Day",
            "Good Friday",
            "Easter Monday",
            "May Day",
            "Spring Bank Holiday",
            "Summer Bank Holiday",
            "Battle of the Boyne",
            "Late Summer Bank Holiday",
            "St. Andrew's Day",
            "Christmas Day",
            "Boxing Day",
        }
        self.assertEqual(all_holidays, y_2015)

    def test_subdiv_deprecation(self):
        self.assertDeprecatedSubdivisions("This subdivision is deprecated and will be removed")
