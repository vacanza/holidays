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

from holidays.countries.united_kingdom import UnitedKingdom, UK, GB, GBR
from tests.common import TestCase


class TestUK(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            UnitedKingdom,
            years=range(1950, 2050),
            years_non_observed=range(2000, 2024),
        )
        cls.holidays_england = UnitedKingdom(
            subdiv="England", years=range(2000, 2024)
        )
        cls.holidays_wales = UnitedKingdom(
            subdiv="Wales", years=range(2000, 2024)
        )
        cls.holidays_scotland = UnitedKingdom(
            subdiv="Scotland", years=range(2000, 2024)
        )
        cls.holidays_northern_ireland = UnitedKingdom(
            subdiv="Northern Ireland", years=range(2000, 2024)
        )

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
        self.assertHolidaysName(
            name, (f"{year}-01-01" for year in range(1974, 2050))
        )
        self.assertNoHoliday(f"{year}-01-01" for year in range(1950, 1974))
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
        self.assertHolidaysName(f"{name} (Observed)", obs_dt)

        name = "New Year Holiday [Scotland]"
        self.assertHolidaysName(
            name, (f"{year}-01-02" for year in range(1950, 2050))
        )
        obs_dt = (
            "2000-01-04",
            "2005-01-04",
            "2006-01-03",
            "2010-01-04",
            "2011-01-04",
            "2012-01-03",
            "2016-01-04",
            "2017-01-03",
            "2021-01-04",
            "2022-01-04",
        )
        self.assertHolidaysName(f"{name} (Observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_st_patricks_day(self):
        name = "St. Patrick's Day"
        name_global = f"{name} [Northern Ireland]"
        self.assertHolidaysName(
            name_global, (f"{year}-03-17" for year in range(1950, 2050))
        )
        obs_dt = (
            "2001-03-19",
            "2002-03-18",
            "2007-03-19",
            "2012-03-19",
            "2013-03-18",
            "2018-03-19",
            "2019-03-18",
        )
        self.assertHolidaysName(f"{name_global} (Observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

        self.assertNoHoliday(
            self.holidays_scotland,
            (f"{year}-03-17" for year in range(2000, 2024)),
        )
        self.assertNoHoliday(
            self.holidays_wales,
            (f"{year}-03-17" for year in range(2000, 2024)),
        )
        self.assertNoHolidayName(
            name, self.holidays_scotland, range(2000, 2024)
        )
        self.assertNoHolidayName(name, self.holidays_wales, range(2000, 2024))

    def test_good_friday(self):
        self.assertHolidaysName(
            "Good Friday",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )

    def test_easter_monday(self):
        name = "Easter Monday"
        name_global = f"{name} [England/Wales/Northern Ireland]"
        dt = (
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )
        self.assertHolidaysName(name_global, dt)
        self.assertNoHoliday(self.holidays_scotland, dt)
        self.assertNoHolidayName(
            name, self.holidays_scotland, range(2000, 2024)
        )

    def test_may_day(self):
        name = "May Day"
        self.assertHolidaysName(
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
        self.assertHolidaysName(
            "Spring Bank Holiday",
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

    def test_battle_of_the_boyne_day(self):
        name = "Battle of the Boyne"
        name_global = f"{name} [Northern Ireland]"
        self.assertHolidaysName(
            name_global, (f"{year}-07-12" for year in range(1950, 2050))
        )

        self.assertNoHoliday(
            self.holidays_scotland,
            (f"{year}-07-12" for year in range(2000, 2024)),
        )
        self.assertNoHoliday(
            self.holidays_wales,
            (f"{year}-07-12" for year in range(2000, 2024)),
        )
        self.assertNoHolidayName(
            name, self.holidays_scotland, range(2000, 2024)
        )
        self.assertNoHolidayName(name, self.holidays_wales, range(2000, 2024))

    def test_summer_bank_holiday(self):
        name = "Summer Bank Holiday"
        name_global = f"{name} [Scotland]"
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
        self.assertHolidaysName(name_global, dt)
        self.assertNoHoliday(self.holidays_northern_ireland, dt)
        self.assertNoHoliday(self.holidays_wales, dt)
        self.assertNoHolidayName(
            name, self.holidays_northern_ireland, range(2000, 2024)
        )
        self.assertNoHolidayName(name, self.holidays_wales, range(2000, 2024))

    def test_late_summer_bank_holiday(self):
        name = "Late Summer Bank Holiday"
        name_global = f"{name} [England/Wales/Northern Ireland]"
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
        self.assertHolidaysName(name_global, dt)
        self.assertNoHolidayName(name_global, range(1950, 1971))
        self.assertNoHolidayName(
            name, UnitedKingdom(subdiv="England", years=1970)
        )
        self.assertNoHolidayName(
            name, UnitedKingdom(subdiv="Northern Ireland", years=1970)
        )
        self.assertNoHolidayName(
            name, UnitedKingdom(subdiv="Wales", years=1970)
        )
        self.assertNoHoliday(self.holidays_scotland, dt)
        self.assertNoHolidayName(
            name, self.holidays_scotland, range(2000, 2024)
        )

    def test_st_andrews_day(self):
        name = "St. Andrew's Day"
        name_global = f"{name} [Scotland]"
        self.assertHolidaysName(
            name_global, (f"{year}-11-30" for year in range(1950, 2050))
        )
        self.assertNoHoliday(
            self.holidays_northern_ireland,
            (f"{year}-11-30" for year in range(2000, 2024)),
        )
        self.assertNoHoliday(
            self.holidays_wales,
            (f"{year}-11-30" for year in range(2000, 2024)),
        )
        self.assertNoHolidayName(
            name, self.holidays_northern_ireland, range(2000, 2024)
        )
        self.assertNoHolidayName(name, self.holidays_wales, range(2000, 2024))

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidaysName(
            name, (f"{year}-12-25" for year in range(1950, 2050))
        )
        obs_dt = (
            "2004-12-27",
            "2005-12-27",
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidaysName(f"{name} (Observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidaysName(
            name, (f"{year}-12-26" for year in range(1950, 2050))
        )
        obs_dt = (
            "2004-12-28",
            "2009-12-28",
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidaysName(f"{name} (Observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_all_holidays_present(self):
        uk_2015 = UnitedKingdom(years=2015)
        all_holidays = {
            "New Year's Day",
            "Good Friday",
            "Easter Monday [England/Wales/Northern Ireland]",
            "May Day",
            "Spring Bank Holiday",
            "Late Summer Bank Holiday [England/Wales/Northern Ireland]",
            "Christmas Day",
            "Boxing Day",
            "St. Patrick's Day [Northern Ireland]",
        }
        for holiday in all_holidays:
            self.assertIn(holiday, uk_2015.values())
