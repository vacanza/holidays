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

from holidays.constants import UNOFFICIAL
from holidays.countries.united_states import UnitedStates
from tests.common import CommonCountryTests


class TestUnitedStates(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(UnitedStates, years_non_observed=range(2000, 2024))

    def test_subdiv_deprecation(self):
        self.assertDeprecatedSubdivisions("This subdivision is deprecated and will be removed")

    def test_new_years_day(self):
        name = "New Year's Day"
        obs_dts = (
            "2004-12-31",
            "2006-01-02",
            "2010-12-31",
            "2012-01-02",
            "2017-01-02",
            "2021-12-31",
            "2023-01-02",
        )
        for holidays, holidays_non_obs in (
            (self.holidays, self.holidays_non_observed),
            (self.holidays_government, self.holidays_government_non_observed),
        ):
            self.assertHolidayName(
                name, holidays, (f"{year}-01-01" for year in range(1871, self.end_year))
            )
            self.assertNoHoliday(
                holidays, (f"{year}-01-01" for year in range(self.start_year, 1871))
            )
            self.assertNoHolidayName(name, holidays, range(self.start_year, 1871))
            self.assertHolidayName(f"{name} (observed)", holidays, obs_dts)
            self.assertNoNonObservedHoliday(holidays_non_obs, obs_dts)

    def test_memorial_day(self):
        name = "Memorial Day"
        self.assertHolidayName(name, (f"{year}-05-30" for year in range(1888, 1971)))
        self.assertNoHolidayName(name, range(self.start_year, 1888))
        self.assertNoGovernmentHolidayName(name, range(self.start_year, 1971))
        dts = (
            "1971-05-31",
            "1972-05-29",
            "2010-05-31",
            "2011-05-30",
            "2012-05-28",
            "2013-05-27",
            "2014-05-26",
            "2015-05-25",
            "2016-05-30",
            "2017-05-29",
            "2018-05-28",
            "2019-05-27",
            "2020-05-25",
            "2021-05-31",
            "2022-05-30",
            "2023-05-29",
        )
        self.assertHolidayName(name, dts)
        self.assertGovernmentHolidayName(name, dts)
        self.assertNoHoliday("1971-05-30", "1972-05-30")
        self.assertNoGovernmentHoliday("1971-05-30", "1972-05-30")

    def test_juneteenth_national_independence_day(self):
        name = "Juneteenth National Independence Day"
        obs_dts = (
            "2021-06-18",
            "2022-06-20",
            "2027-06-18",
            "2032-06-18",
        )
        for holidays, holidays_non_obs in (
            (self.holidays, self.holidays_non_observed),
            (self.holidays_government, self.holidays_government_non_observed),
        ):
            self.assertHolidayName(
                name, holidays, (f"{year}-06-19" for year in range(2021, self.end_year))
            )
            self.assertNoHoliday(
                holidays, (f"{year}-06-19" for year in range(self.start_year, 2021))
            )
            self.assertNoHolidayName(name, holidays, range(self.start_year, 2021))
            self.assertHolidayName(f"{name} (observed)", holidays, obs_dts)
            self.assertNoNonObservedHoliday(holidays_non_obs, obs_dts)

    def test_independence_day(self):
        name = "Independence Day"
        obs_dts = (
            "2004-07-05",
            "2009-07-03",
            "2010-07-05",
            "2015-07-03",
            "2020-07-03",
            "2021-07-05",
        )
        for holidays, holidays_non_obs in (
            (self.holidays, self.holidays_non_observed),
            (self.holidays_government, self.holidays_government_non_observed),
        ):
            self.assertHolidayName(
                name, holidays, (f"{year}-07-04" for year in range(1870, self.end_year))
            )
            self.assertNoHoliday(
                holidays, (f"{year}-07-04" for year in range(self.start_year, 1870))
            )
            self.assertNoHolidayName(name, holidays, range(self.start_year, 1870))
            self.assertHolidayName(f"{name} (observed)", holidays, obs_dts)
            self.assertNoNonObservedHoliday(holidays_non_obs, obs_dts)

    def test_labor_day(self):
        name = "Labor Day"
        dts = (
            "2010-09-06",
            "2011-09-05",
            "2012-09-03",
            "2013-09-02",
            "2014-09-01",
            "2015-09-07",
            "2016-09-05",
            "2017-09-04",
            "2018-09-03",
            "2019-09-02",
            "2020-09-07",
            "2021-09-06",
            "2022-09-05",
            "2023-09-04",
        )
        for holidays in (self.holidays, self.holidays_government):
            self.assertHolidayName(name, holidays, range(1894, self.end_year))
            self.assertNoHolidayName(name, holidays, range(self.start_year, 1894))
            self.assertHolidayName(name, holidays, dts)

    def test_veterans_day(self):
        name_1938 = "Armistice Day"
        name_1954 = "Veterans Day"
        dts = (
            "1971-10-25",
            "1972-10-23",
            "1973-10-22",
            "1974-10-28",
            "1975-10-27",
            "1976-10-25",
            "1977-10-24",
        )
        obs_dt = (
            "2000-11-10",
            "2001-11-12",
            "2006-11-10",
            "2007-11-12",
            "2012-11-12",
            "2017-11-10",
            "2018-11-12",
            "2023-11-10",
        )
        for holidays, holidays_non_obs in (
            (self.holidays, self.holidays_non_observed),
            (self.holidays_government, self.holidays_government_non_observed),
        ):
            self.assertHolidayName(
                name_1938, holidays, (f"{year}-11-11" for year in range(1938, 1954))
            )
            self.assertHolidayName(
                name_1954,
                holidays,
                (f"{year}-11-11" for year in (*range(1954, 1971), *range(1978, self.end_year))),
            )
            self.assertNoHolidayName(
                name_1938, holidays, range(self.start_year, 1938), range(1954, self.end_year)
            )
            self.assertNoHolidayName(name_1954, holidays, range(self.start_year, 1954))
            self.assertHolidayName(name_1954, holidays, dts)
            self.assertHolidayName(f"{name_1954} (observed)", holidays, obs_dt)
            self.assertNoNonObservedHoliday(holidays_non_obs, obs_dt)

    def test_thanksgiving_day(self):
        name = "Thanksgiving Day"
        dts_pre_1870 = (
            # Last Thu of Nov and other exceptions.
            "1862-04-10",
            "1863-11-26",
            "1864-11-24",
            "1865-12-07",
            "1866-11-29",
            "1867-11-28",
            "1868-11-26",
            "1869-11-18",
        )
        dts = (
            # Last Thu of Nov.
            "1933-11-30",
            "1934-11-29",
            "1935-11-28",
            "1936-11-26",
            "1937-11-25",
            "1938-11-24",
            # 'Franksgiving'.
            "1939-11-23",
            "1940-11-21",
            "1941-11-20",
            # 4th Thu of Nov.
            "2010-11-25",
            "2011-11-24",
            "2012-11-22",
            "2013-11-28",
            "2014-11-27",
            "2015-11-26",
            "2016-11-24",
            "2017-11-23",
            "2018-11-22",
            "2019-11-28",
            "2020-11-26",
            "2021-11-25",
            "2022-11-24",
            "2023-11-23",
        )
        # PUBLIC.
        name_1777 = "Public Thanksgiving and Prayer Day"
        self.assertHolidayName(name_1777, "1777-12-18", "1782-11-28", "1789-11-26", "1795-02-19")
        self.assertNoHolidayName(
            name_1777,
            range(1778, 1782),
            range(1783, 1789),
            range(1790, 1795),
            range(1796, self.end_year),
        )
        name_1798 = "Fasting and Humiliation Day"
        self.assertHolidayName(name_1798, "1798-05-09", "1799-04-25")
        self.assertNoHolidayName(name_1798, range(1777, 1798), range(1800, self.end_year))
        name_1813 = "Public Humiliation and Prayer Day"
        self.assertHolidayName(name_1813, "1813-09-09", "1815-04-13")
        self.assertNoHolidayName(name_1813, range(1777, 1813), 1814, range(1816, self.end_year))
        self.assertHolidayName(name, dts_pre_1870, dts)
        self.assertHolidayName(name, range(1862, self.end_year))
        self.assertNoHolidayName(name, range(1777, 1862))

        # FEDERAL.
        self.assertGovernmentHolidayName(name, dts)
        self.assertGovernmentHolidayName(name, range(1870, self.end_year))
        self.assertNoGovernmentHolidayName(name, range(1777, 1870))

    def test_christmas_day(self):
        name = "Christmas Day"
        obs_dt = (
            "2004-12-24",
            "2005-12-26",
            "2010-12-24",
            "2011-12-26",
            "2016-12-26",
            "2021-12-24",
            "2022-12-26",
        )
        for holidays, holidays_non_obs in (
            (self.holidays, self.holidays_non_observed),
            (self.holidays_government, self.holidays_government_non_observed),
        ):
            self.assertHolidayName(
                name, holidays, (f"{year}-12-25" for year in range(1870, self.end_year))
            )
            self.assertNoHoliday(
                holidays, (f"{year}-12-25" for year in range(self.start_year, 1870))
            )
            self.assertNoHolidayName(name, holidays, range(self.start_year, 1870))
            self.assertHolidayName(f"{name} (observed)", holidays, obs_dt)
            self.assertNoNonObservedHoliday(holidays_non_obs, obs_dt)

    def test_martin_luther_king_day(self):
        name = "Martin Luther King Jr. Day"
        name_government = "Birthday of Martin Luther King, Jr."
        dts = (
            "1986-01-20",
            "2010-01-18",
            "2011-01-17",
            "2012-01-16",
            "2013-01-21",
            "2014-01-20",
            "2015-01-19",
            "2016-01-18",
            "2017-01-16",
            "2018-01-15",
            "2019-01-21",
            "2020-01-20",
            "2021-01-18",
            "2022-01-17",
            "2023-01-16",
        )
        for holidays, holiday_name in (
            (self.holidays, name),
            (self.holidays_government, name_government),
        ):
            self.assertHolidayName(holiday_name, holidays, range(1986, self.end_year))
            self.assertNoHolidayName(holiday_name, holidays, range(self.start_year, 1986))
            self.assertHolidayName(holiday_name, holidays, dts)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv not in {"AL", "AR", "AZ", "GA", "ID", "MS", "NH"}:
                self.assertHolidayName(name, holidays, dts)
                self.assertHolidayName(name, holidays, range(1986, self.end_year))
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1986))

    def test_martin_luther_king_day_states(self):
        dts = (
            "1986-01-20",
            "2010-01-18",
            "2011-01-17",
            "2012-01-16",
            "2013-01-21",
            "2014-01-20",
            "2015-01-19",
            "2016-01-18",
            "2017-01-16",
            "2018-01-15",
            "2019-01-21",
            "2020-01-20",
            "2021-01-18",
            "2022-01-17",
            "2023-01-16",
        )

        al_name = "Martin Luther King, Jr & Robert E. Lee's Birthday"
        self.assertSubdivAlHolidayName(al_name, dts)
        self.assertSubdivAlHolidayName(al_name, range(1986, self.end_year))
        self.assertNoSubdivAlHolidayName(al_name, range(self.start_year, 1986))

        ar_name_1986 = "Dr. Martin Luther King Jr. and Robert E. Lee's Birthdays"
        ar_name_2018 = "Martin Luther King Jr. Day"
        self.assertSubdivArHolidayName(
            ar_name_1986,
            "2010-01-18",
            "2011-01-17",
            "2012-01-16",
            "2013-01-21",
            "2014-01-20",
            "2015-01-19",
            "2016-01-18",
            "2017-01-16",
        )
        self.assertSubdivArHolidayName(
            ar_name_2018,
            "2018-01-15",
            "2019-01-21",
            "2020-01-20",
            "2021-01-18",
            "2022-01-17",
            "2023-01-16",
        )
        self.assertSubdivArHolidayName(ar_name_1986, range(1986, 2018))
        self.assertSubdivArHolidayName(ar_name_2018, range(2018, self.end_year))
        self.assertNoSubdivArHolidayName(
            ar_name_1986, range(self.start_year, 1986), range(2018, self.end_year)
        )
        self.assertNoSubdivArHolidayName(ar_name_2018, range(self.start_year, 2018))

        az_name = "Dr. Martin Luther King Jr. / Civil Rights Day"
        self.assertSubdivAzHolidayName(az_name, dts)
        self.assertSubdivAzHolidayName(az_name, range(1986, self.end_year))
        self.assertNoSubdivAzHolidayName(az_name, range(self.start_year, 1986))

        ga_name_1986 = "Robert E. Lee's Birthday"
        ga_name_2012 = "Martin Luther King Jr. Day"
        self.assertSubdivGaHolidayName(
            ga_name_1986,
            "2010-01-18",
            "2011-01-17",
        )
        self.assertSubdivGaHolidayName(
            ga_name_2012,
            "2012-01-16",
            "2013-01-21",
            "2014-01-20",
            "2015-01-19",
            "2016-01-18",
            "2017-01-16",
            "2018-01-15",
            "2019-01-21",
            "2020-01-20",
            "2021-01-18",
            "2022-01-17",
            "2023-01-16",
        )
        self.assertSubdivGaHolidayName(ga_name_1986, range(1986, 2012))
        self.assertSubdivGaHolidayName(ga_name_2012, range(2012, self.end_year))
        self.assertNoSubdivGaHolidayName(ga_name_2012, range(self.start_year, 2012))

        id_name_1986 = "Martin Luther King Jr. Day"
        id_name_2006 = "Martin Luther King Jr. / Idaho Human Rights Day"
        self.assertSubdivIdHolidayName(
            id_name_1986,
            "2000-01-17",
            "2001-01-15",
            "2002-01-21",
            "2003-01-20",
            "2004-01-19",
            "2005-01-17",
        )
        self.assertSubdivIdHolidayName(
            id_name_2006,
            "2006-01-16",
            "2010-01-18",
            "2011-01-17",
            "2012-01-16",
            "2013-01-21",
            "2014-01-20",
            "2015-01-19",
            "2016-01-18",
            "2017-01-16",
            "2018-01-15",
            "2019-01-21",
            "2020-01-20",
            "2021-01-18",
            "2022-01-17",
            "2023-01-16",
        )
        self.assertSubdivIdHolidayName(id_name_1986, range(1986, 2006))
        self.assertSubdivIdHolidayName(id_name_2006, range(2006, self.end_year))
        self.assertNoSubdivIdHolidayName(
            id_name_1986, range(self.start_year, 1986), range(2006, self.end_year)
        )
        self.assertNoSubdivIdHolidayName(id_name_2006, range(self.start_year, 2006))

        ms_name = "Dr. Martin Luther King Jr. and Robert E. Lee's Birthdays"
        self.assertSubdivMsHolidayName(ms_name, dts)
        self.assertSubdivMsHolidayName(ms_name, range(1986, self.end_year))
        self.assertNoSubdivMsHolidayName(ms_name, range(self.start_year, 1986))

        nh_name = "Dr. Martin Luther King Jr. / Civil Rights Day"
        self.assertSubdivNhHolidayName(nh_name, dts)
        self.assertSubdivNhHolidayName(nh_name, range(1986, self.end_year))
        self.assertNoSubdivNhHolidayName(nh_name, range(self.start_year, 1986))

    def test_washingtons_birthday(self):
        name = "Washington's Birthday"
        dts = (
            "2010-02-15",
            "2011-02-21",
            "2012-02-20",
            "2013-02-18",
            "2014-02-17",
            "2015-02-16",
            "2016-02-15",
            "2017-02-20",
            "2018-02-19",
            "2019-02-18",
            "2020-02-17",
            "2021-02-15",
            "2022-02-21",
            "2023-02-20",
        )
        for holidays in (self.holidays, self.holidays_government):
            self.assertHolidayName(name, holidays, (f"{year}-02-22" for year in range(1879, 1971)))
            self.assertHolidayName(name, holidays, dts)
            self.assertHolidayName(name, holidays, range(1971, self.end_year))
            self.assertNoHolidayName(name, holidays, range(self.start_year, 1879))

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv not in {
                "AK",
                "AL",
                "AR",
                "AZ",
                "CA",
                "CO",
                "DE",
                "FL",
                "GA",
                "HI",
                "ID",
                "IN",
                "MD",
                "MN",
                "MT",
                "NJ",
                "NM",
                "OH",
                "OK",
                "OR",
                "PA",
                "PR",
                "SC",
                "TN",
                "TX",
                "UT",
                "VA",
                "VI",
                "VT",
                "WA",
                "WV",
                "WY",
            }:
                self.assertHolidayName(
                    name, holidays, (f"{year}-02-22" for year in range(1879, 1971))
                )
                self.assertHolidayName(name, holidays, dts)
                self.assertHolidayName(name, holidays, range(1971, self.end_year))
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1879))

    def test_washingtons_birthday_states(self):
        dts = (
            "2010-02-15",
            "2011-02-21",
            "2012-02-20",
            "2013-02-18",
            "2014-02-17",
            "2015-02-16",
            "2016-02-15",
            "2017-02-20",
            "2018-02-19",
            "2019-02-18",
            "2020-02-17",
            "2021-02-15",
            "2022-02-21",
            "2023-02-20",
        )

        for subdiv, name in (
            ("AK", "Presidents' Day"),
            ("AL", "George Washington & Thomas Jefferson's Birthday"),
            ("AR", "George Washington's Birthday and Daisy Gatson Bates Day"),
            ("AZ", "Lincoln/Washington Presidents' Day"),
            ("CA", "Presidents' Day"),
            ("CO", "Washington-Lincoln Day"),
            ("DE", None),
            ("HI", "Presidents' Day"),
            ("ID", "Presidents' Day"),
            ("MD", "Presidents' Day"),
            ("MN", "Washington's and Lincoln's Birthday"),
            ("MT", "Lincoln's and Washington's Birthdays"),
            ("NJ", "Presidents Day"),
            ("NM", None),
            ("OH", "Washington-Lincoln Day"),
            ("OK", "Presidents' Day"),
            ("OR", "Presidents Day"),
            ("PA", "Presidents' Day"),
            ("PR", "Presidents' Day"),
            ("SC", "President's Day"),
            ("TN", "President's Day"),
            ("TX", "Presidents' Day"),
            ("UT", "Washington and Lincoln Day"),
            ("VA", "George Washington Day"),
            ("VI", "Presidents' Day"),
            ("VT", "Presidents' Day"),
            ("WA", "Presidents' Day"),
            ("WV", "Presidents' Day"),
            ("WY", "President's Day"),
        ):
            if name:
                self.assertHolidayName(name, self.subdiv_holidays[subdiv], dts)
                self.assertHolidayName(
                    name, self.subdiv_holidays[subdiv], range(1971, self.end_year)
                )
                self.assertNoHolidayName(
                    name, self.subdiv_holidays[subdiv], range(self.start_year, 1879)
                )
            else:
                self.assertNoHoliday(self.subdiv_holidays[subdiv], dts)
                self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

        name = "Washington's Birthday"
        self.assertNoSubdivFlHoliday(
            "2010-02-15",
            "2011-02-21",
            "2012-02-20",
            "2013-02-18",
            "2014-02-17",
            "2015-02-16",
            "2017-02-20",
            "2018-02-19",
            "2019-02-18",
            "2020-02-17",
            "2022-02-21",
            "2023-02-20",
        )
        self.assertNoSubdivFlHolidayName(name)

        dts = (
            "2010-12-23",
            "2011-12-23",
            "2012-12-24",
            "2013-12-24",
            "2014-12-26",
            "2015-12-24",
            "2016-12-23",
            "2017-12-26",
            "2018-12-24",
            "2019-12-24",
            "2020-12-24",
            "2021-12-23",
            "2022-12-23",
            "2023-12-26",
            "2024-12-24",
        )
        for subdiv in ("GA", "IN"):
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], dts)
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], range(1971, self.end_year))
            self.assertNoHolidayName(
                name, self.subdiv_holidays[subdiv], range(self.start_year, 1879)
            )

    def test_columbus_day(self):
        name = "Columbus Day"
        dts = (
            "2010-10-11",
            "2011-10-10",
            "2012-10-08",
            "2013-10-14",
            "2014-10-13",
            "2015-10-12",
            "2016-10-10",
            "2017-10-09",
            "2018-10-08",
            "2019-10-14",
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
        )
        self.assertHolidayName(name, (f"{year}-10-12" for year in range(1937, 1971)))
        self.assertHolidayName(name, range(1971, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1937))
        self.assertHolidayName(name, dts)

        self.assertGovernmentHolidayName(name, range(1971, self.end_year))
        self.assertNoGovernmentHolidayName(name, range(self.start_year, 1937))
        self.assertGovernmentHolidayName(name, dts)

        subdivs_have_columbus_day = {
            "AS",
            "AZ",
            "CT",
            "GA",
            "ID",
            "IL",
            "IN",
            "MA",
            "MD",
            "MO",
            "MT",
            "NJ",
            "NY",
            "OH",
            "PA",
            "UT",
            "WV",
        }
        subdivs_have_columbus_day_with_other_name = {
            "AK",
            "AL",
            "CA",
            "DC",
            "ME",
            "MP",
            "NE",
            "NM",
            "RI",
            "SD",
            "VA",
            "VI",
        }

        for subdiv in subdivs_have_columbus_day:
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], dts)
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], range(1971, self.end_year))
            self.assertNoHolidayName(
                name, self.subdiv_holidays[subdiv], range(self.start_year, 1937)
            )

        for subdiv in (
            set(UnitedStates.subdivisions)
            - subdivs_have_columbus_day
            - subdivs_have_columbus_day_with_other_name
        ):
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])
            self.assertNoHoliday(self.subdiv_holidays[subdiv], dts)

    def test_columbus_day_states(self):
        name_col = "Columbus Day"
        name_ind = "Indigenous Peoples' Day"
        dts = (
            "2010-10-11",
            "2011-10-10",
            "2012-10-08",
            "2013-10-14",
            "2014-10-13",
            "2015-10-12",
            "2016-10-10",
            "2017-10-09",
            "2018-10-08",
            "2019-10-14",
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
        )
        for subdiv, change_year in (
            ("AK", 2015),
            ("DC", 2019),
            ("ME", 2019),
            ("NM", 2019),
            ("NE", 2020),
            ("VA", 2020),
        ):
            self.assertHolidayName(
                name_col, self.subdiv_holidays[subdiv], range(1971, change_year)
            )
            self.assertHolidayName(
                name_ind, self.subdiv_holidays[subdiv], range(change_year, self.end_year)
            )
            self.assertHoliday(self.subdiv_holidays[subdiv], dts)
            self.assertNoHolidayName(
                name_col,
                self.subdiv_holidays[subdiv],
                range(self.start_year, 1971),
                range(change_year, self.end_year),
            )
            self.assertNoHolidayName(
                name_ind, self.subdiv_holidays[subdiv], range(self.start_year, change_year)
            )

        vi_name = "Columbus Day and Puerto Rico Friendship Day"
        self.assertSubdivViHolidayName(vi_name, dts)
        self.assertSubdivViHolidayName(vi_name, range(1937, self.end_year))
        self.assertNoSubdivViHolidayName(vi_name, range(self.start_year, 1937))

    def test_columbus_day_al(self):
        name_1971 = "Columbus Day / Fraternal Day"
        name_2000 = "Columbus Day / American Indian Heritage Day / Fraternal Day"
        dts = (
            "2010-10-11",
            "2011-10-10",
            "2012-10-08",
            "2013-10-14",
            "2014-10-13",
            "2015-10-12",
            "2016-10-10",
            "2017-10-09",
            "2018-10-08",
            "2019-10-14",
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
        )
        self.assertSubdivAlHolidayName(name_1971, range(1971, 2000))
        self.assertSubdivAlHolidayName(name_2000, range(2000, self.end_year))
        self.assertSubdivAlHoliday(dts)
        self.assertNoSubdivAlHolidayName(name_1971, range(self.start_year, 1970))
        self.assertNoSubdivAlHolidayName(name_2000, range(self.start_year, 2000))

    def test_columbus_day_ca(self):
        name = "Columbus Day"
        dts = (
            "1990-10-08",
            "1995-10-09",
            "2000-10-09",
            "2001-10-08",
            "2002-10-14",
            "2003-10-13",
            "2004-10-11",
            "2005-10-10",
            "2006-10-09",
            "2007-10-08",
            "2008-10-13",
        )
        self.assertSubdivCaHolidayName(name, range(1971, 2009))
        self.assertSubdivCaHoliday(dts)
        self.assertNoSubdivCaHolidayName(
            name, range(self.start_year, 1970), range(2009, self.end_year)
        )

    def test_columbus_day_ri(self):
        name_1971 = "Columbus Day"
        name_2022 = "Indigenous Peoples' Day / Columbus Day"
        dts = (
            "2010-10-11",
            "2011-10-10",
            "2012-10-08",
            "2013-10-14",
            "2014-10-13",
            "2015-10-12",
            "2016-10-10",
            "2017-10-09",
            "2018-10-08",
            "2019-10-14",
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
        )
        self.assertSubdivRiHolidayName(name_1971, range(1971, 2022))
        self.assertSubdivRiHolidayName(name_2022, range(2022, self.end_year))
        self.assertSubdivRiHoliday(dts)
        self.assertNoSubdivRiHolidayName(name_1971, range(self.start_year, 1970))
        self.assertNoSubdivRiHolidayName(name_2022, range(self.start_year, 2022))

    def test_columbus_day_sd(self):
        name_1937 = "Columbus Day"
        name_1990 = "Native Americans' Day"
        dts = (
            "2010-10-11",
            "2011-10-10",
            "2012-10-08",
            "2013-10-14",
            "2014-10-13",
            "2015-10-12",
            "2016-10-10",
            "2017-10-09",
            "2018-10-08",
            "2019-10-14",
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
        )
        self.assertSubdivSdHolidayName(name_1937, range(1937, 1990))
        self.assertSubdivSdHolidayName(name_1990, range(1990, self.end_year))
        self.assertSubdivSdHolidayName(name_1990, dts)
        self.assertNoSubdivSdHolidayName(name_1937, range(self.start_year, 1937))
        self.assertNoSubdivSdHolidayName(name_1990, range(self.start_year, 1990))

    def test_epiphany(self):
        name = "Epiphany"
        self.assertNoHolidayName(name)
        self.assertSubdivPrHolidayName(
            name, (f"{year}-01-06" for year in range(self.start_year, self.end_year))
        )

    def test_three_kings_day(self):
        name = "Three Kings Day"
        self.assertNoHolidayName(name)
        self.assertSubdivViHolidayName(
            name, (f"{year}-01-06" for year in range(self.start_year, self.end_year))
        )

    def test_lee_jackson_day(self):
        name = "Lee Jackson Day"
        self.assertNoHolidayName(name)
        self.assertNoSubdivVaHolidayName(
            name, range(self.start_year, 1889), range(2021, self.end_year)
        )
        self.assertSubdivVaHolidayName(name, (f"{year}-01-19" for year in range(1889, 1983)))
        dt = (
            "1983-01-17",
            "1990-01-15",
            "1995-01-16",
            "1999-01-18",
            "2000-01-14",
            "2010-01-15",
            "2011-01-14",
            "2012-01-13",
            "2013-01-18",
            "2014-01-17",
            "2015-01-16",
            "2016-01-15",
            "2017-01-13",
            "2018-01-12",
            "2019-01-18",
            "2020-01-17",
        )
        self.assertSubdivVaHolidayName(name, dt)

    def test_inauguration_day(self):
        name = "Inauguration Day"
        self.assertNoHolidayName(name)
        years_1 = range(1861, 1937, 4)
        years_2 = range(1937, self.end_year, 4)
        years_no = set(range(1865, self.end_year)) - set(years_1) - set(years_2)
        obs_dt = (
            "1877-03-05",
            "1917-03-05",
            "1957-01-21",
            "1985-01-21",
            "2013-01-21",
        )
        for subdiv in ("DC", "MD", "VA"):
            self.assertHolidayName(
                name, self.subdiv_holidays[subdiv], (f"{year}-03-04" for year in years_1)
            )
            self.assertHolidayName(
                name, self.subdiv_holidays[subdiv], (f"{year}-01-20" for year in years_2)
            )
            self.assertHolidayName(name, UnitedStates(subdiv=subdiv), "1789-03-04")
            self.assertNoHolidayName(name, UnitedStates(subdiv=subdiv), "1788-03-04")
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv], years_no)
            self.assertHolidayName(f"{name} (observed)", self.subdiv_holidays[subdiv], obs_dt)
            self.assertNoNonObservedHolidayName(
                f"{name} (observed)", UnitedStates(subdiv=subdiv, observed=False), obs_dt
            )

    def test_lincolns_birthday(self):
        name = "Lincoln's Birthday"
        self.assertNoHolidayName(name)
        obs_dt = (
            "2011-02-11",
            "2012-02-13",
            "2017-02-13",
            "2022-02-11",
            "2023-02-13",
        )
        for subdiv in ("CT", "IA", "IL", "NJ", "NY"):
            self.assertHolidayName(
                name,
                self.subdiv_holidays[subdiv],
                (f"{year}-02-12" for year in range(1971, self.end_year)),
            )
            self.assertHolidayName(f"{name} (observed)", self.subdiv_holidays[subdiv], obs_dt)
            self.assertNoNonObservedHolidayName(
                f"{name} (observed)", UnitedStates(subdiv=subdiv, observed=False), obs_dt
            )
        obs_dt = (
            "1994-02-11",
            "1995-02-13",
            "2000-02-11",
            "2005-02-11",
            "2006-02-13",
        )
        self.assertSubdivCaHolidayName(name, (f"{year}-02-12" for year in range(1971, 2010)))
        self.assertSubdivCaHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivCaNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_susan_b_anthony_day(self):
        name = "Susan B. Anthony Day"
        self.assertNoHolidayName(name)
        for subdiv, start_year in (
            ("CA", 2014),
            ("FL", 2011),
            ("NY", 2004),
            ("WI", 1976),
        ):
            self.assertHolidayName(
                name,
                self.subdiv_holidays[subdiv],
                (f"{year}-02-15" for year in range(start_year, self.end_year)),
            )
            self.assertNoHolidayName(
                name, self.subdiv_holidays[subdiv], range(self.start_year, start_year)
            )

    def test_mardi_gras(self):
        name = "Mardi Gras"
        self.assertNoHolidayName(name)
        self.assertNoSubdivLaHolidayName(name, range(self.start_year, 1856))
        dt = (
            "2010-02-16",
            "2011-03-08",
            "2012-02-21",
            "2013-02-12",
            "2014-03-04",
            "2015-02-17",
            "2016-02-09",
            "2017-02-28",
            "2018-02-13",
            "2019-03-05",
            "2020-02-25",
            "2021-02-16",
            "2022-03-01",
            "2023-02-21",
        )
        self.assertSubdivLaHolidayName(name, dt)

    def test_guam_discovery_day(self):
        name = "Guam Discovery Day"
        self.assertNoHolidayName(name)
        dt = (
            "2010-03-01",
            "2011-03-07",
            "2012-03-05",
            "2013-03-04",
            "2014-03-03",
            "2015-03-02",
            "2016-03-07",
            "2017-03-06",
            "2018-03-05",
            "2019-03-04",
            "2020-03-02",
            "2021-03-01",
            "2022-03-07",
            "2023-03-06",
        )
        self.assertSubdivGuHolidayName(name, dt)
        self.assertNoSubdivGuHolidayName(name, range(self.start_year, 1970))

    def test_casimir_pulaski_day(self):
        name = "Casimir Pulaski Day"
        self.assertNoHolidayName(name)
        dt = (
            "2010-03-01",
            "2011-03-07",
            "2012-03-05",
            "2013-03-04",
            "2014-03-03",
            "2015-03-02",
            "2016-03-07",
            "2017-03-06",
            "2018-03-05",
            "2019-03-04",
            "2020-03-02",
            "2021-03-01",
            "2022-03-07",
            "2023-03-06",
        )
        self.assertSubdivIlHolidayName(name, dt)
        self.assertNoSubdivIlHolidayName(name, range(self.start_year, 1978))

    def test_texas_independence_day(self):
        name = "Texas Independence Day"
        self.assertNoHolidayName(name)
        self.assertSubdivTxHolidayName(
            name, (f"{year}-03-02" for year in range(1874, self.end_year))
        )
        self.assertNoSubdivTxHolidayName(name, range(self.start_year, 1874))

    def test_town_meeting_day(self):
        name = "Town Meeting Day"
        self.assertNoHolidayName(name)
        self.assertNoSubdivVtHolidayName(name, range(self.start_year, 1799))
        dt = (
            "2010-03-02",
            "2011-03-01",
            "2012-03-06",
            "2013-03-05",
            "2014-03-04",
            "2015-03-03",
            "2016-03-01",
            "2017-03-07",
            "2018-03-06",
            "2019-03-05",
            "2020-03-03",
            "2021-03-02",
            "2022-03-01",
            "2023-03-07",
        )
        self.assertSubdivVtHolidayName(name, dt)

    def test_evacuation_day(self):
        name = "Evacuation Day"
        self.assertNoHolidayName(name)
        self.assertSubdivMaHolidayName(
            name, (f"{year}-03-17" for year in range(1901, self.end_year))
        )
        self.assertNoSubdivMaHolidayName(name, range(self.start_year, 1901))
        obs_dt = (
            "2012-03-19",
            "2013-03-18",
            "2018-03-19",
            "2019-03-18",
        )
        self.assertSubdivMaHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivMaNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_emancipation_day_in_puerto_rico(self):
        name = "Emancipation Day"
        self.assertNoHolidayName(name)
        self.assertSubdivPrHolidayName(
            name, (f"{year}-03-22" for year in range(self.start_year, self.end_year))
        )
        obs_dt = (
            "1998-03-23",
            "2009-03-23",
            "2015-03-23",
            "2020-03-23",
        )
        self.assertSubdivPrHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivPrNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_commonwealth_covenant_day(self):
        name = "Commonwealth Covenant Day"
        self.assertNoHolidayName(name)
        self.assertSubdivMpHolidayName(
            name, (f"{year}-03-24" for year in range(self.start_year, self.end_year))
        )
        obs_dt = (
            "2012-03-23",
            "2013-03-25",
            "2018-03-23",
            "2019-03-25",
        )
        self.assertSubdivMpHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivMpNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_prince_jonah_kuhio_kalanianaole_day(self):
        name = "Prince Jonah Kuhio Kalanianaole Day"
        self.assertNoHolidayName(name)
        self.assertSubdivHiHolidayName(
            name, (f"{year}-03-26" for year in range(1949, self.end_year))
        )
        self.assertNoSubdivHiHolidayName(name, range(self.start_year, 1949))
        obs_dt = (
            "2011-03-25",
            "2016-03-25",
            "2017-03-27",
            "2022-03-25",
            "2023-03-27",
        )
        self.assertSubdivHiHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivHiNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_sewards_day(self):
        name = "Seward's Day"
        self.assertNoHolidayName(name)
        self.assertSubdivAkHolidayName(
            name, (f"{year}-03-30" for year in (*range(1918, 1921), *range(1922, 1955)))
        )
        self.assertNoSubdivAkHolidayName(name, range(self.start_year, 1918), 1921)
        dt = (
            "1955-03-28",
            "2010-03-29",
            "2011-03-28",
            "2012-03-26",
            "2013-03-25",
            "2014-03-31",
            "2015-03-30",
            "2016-03-28",
            "2017-03-27",
            "2018-03-26",
            "2019-03-25",
            "2020-03-30",
            "2021-03-29",
            "2022-03-28",
            "2023-03-27",
        )
        self.assertSubdivAkHolidayName(name, dt)

    def test_cesar_chavez_day(self):
        name = "Cesar Chavez Day"
        self.assertNoHolidayName(name)
        for subdiv, start_year in (
            ("CA", 1995),
            ("CO", 2001),
            ("TX", 2000),
        ):
            self.assertHolidayName(
                name,
                self.subdiv_holidays[subdiv],
                (f"{year}-03-31" for year in range(start_year, self.end_year)),
            )
            self.assertNoHolidayName(
                name, self.subdiv_holidays[subdiv], range(self.start_year, start_year)
            )

        obs_dt = (
            "1996-04-01",
            "2002-04-01",
            "2013-04-01",
            "2019-04-01",
        )
        self.assertSubdivCaHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivCaNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_transfer_day(self):
        name = "Transfer Day"
        self.assertNoHolidayName(name)
        self.assertSubdivViHolidayName(
            name, (f"{year}-03-31" for year in range(self.start_year, self.end_year))
        )

    def test_emancipation_day(self):
        name = "Emancipation Day"
        self.assertNoHolidayName(name)
        self.assertSubdivDcHolidayName(
            name, (f"{year}-04-16" for year in range(2005, self.end_year))
        )
        self.assertNoSubdivDcHolidayName(name, range(self.start_year, 2005))
        obs_dt = (
            "2011-04-15",
            "2016-04-15",
            "2017-04-17",
            "2022-04-15",
            "2023-04-17",
        )
        self.assertSubdivDcHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivDcNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_american_samoa_flag_day(self):
        name = "American Samoa Flag Day"
        self.assertNoHolidayName(name)
        self.assertSubdivAsHolidayName(
            name, (f"{year}-04-17" for year in range(1901, self.end_year))
        )
        self.assertNoSubdivAsHolidayName(name, range(self.start_year, 1901))
        obs_dt = (
            "2004-04-16",
            "2005-04-18",
            "2010-04-16",
            "2011-04-18",
            "2016-04-18",
            "2021-04-16",
            "2022-04-18",
        )
        self.assertSubdivAsHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivAsNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_patriots_day(self):
        name = "Patriots' Day"
        self.assertNoHolidayName(name)
        dt = (
            "1969-04-21",
            "2010-04-19",
            "2011-04-18",
            "2012-04-16",
            "2013-04-15",
            "2014-04-21",
            "2015-04-20",
            "2016-04-18",
            "2017-04-17",
            "2018-04-16",
            "2019-04-15",
            "2020-04-20",
            "2021-04-19",
            "2022-04-18",
            "2023-04-17",
        )
        for subdiv in ("MA", "ME"):
            self.assertHolidayName(
                name, self.subdiv_holidays[subdiv], (f"{year}-04-19" for year in range(1894, 1969))
            )
            self.assertNoHolidayName(
                name, self.subdiv_holidays[subdiv], range(self.start_year, 1894)
            )
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], dt)

    def test_holy_thursday(self):
        name = "Holy Thursday"
        self.assertNoHolidayName(name)
        self.assertSubdivViHolidayName(name, range(self.start_year, self.end_year))
        dt = (
            "2010-04-01",
            "2011-04-21",
            "2012-04-05",
            "2013-03-28",
            "2014-04-17",
            "2015-04-02",
            "2016-03-24",
            "2017-04-13",
            "2018-03-29",
            "2019-04-18",
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
        )
        self.assertSubdivViHolidayName(name, dt)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertNoHolidayName(name)
        dt = (
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
        for subdiv in (
            "CT",
            "DE",
            "GU",
            "IN",
            "KY",
            "LA",
            "MP",
            "NC",
            "NJ",
            "PR",
            "TN",
            "TX",
            "VI",
        ):
            self.assertHolidayName(
                name, self.subdiv_holidays[subdiv], range(self.start_year, self.end_year)
            )
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], dt)

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertNoHolidayName(name)
        self.assertSubdivViHolidayName(name, range(self.start_year, self.end_year))
        dt = (
            "2010-04-05",
            "2011-04-25",
            "2012-04-09",
            "2013-04-01",
            "2014-04-21",
            "2015-04-06",
            "2016-03-28",
            "2017-04-17",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )
        self.assertSubdivViHolidayName(name, dt)

    def test_confederate_memorial_day(self):
        name = "Confederate Memorial Day"
        self.assertNoHolidayName(name)
        dt = (
            "2010-04-26",
            "2011-04-25",
            "2012-04-23",
            "2013-04-22",
            "2014-04-28",
            "2015-04-27",
            "2016-04-25",
            "2017-04-24",
            "2018-04-23",
            "2019-04-22",
            "2020-04-27",
            "2021-04-26",
            "2022-04-25",
            "2023-04-24",
        )
        for subdiv in ("AL", "SC"):
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], range(1866, self.end_year))
            self.assertNoHolidayName(
                name, self.subdiv_holidays[subdiv], range(self.start_year, 1866)
            )
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], dt)

        self.assertSubdivMsHolidayName(
            name,
            "2010-04-26",
            "2011-04-25",
            "2012-04-30",
            "2013-04-29",
            "2014-04-28",
            "2015-04-27",
            "2016-04-25",
            "2017-04-24",
            "2018-04-30",
            "2019-04-29",
            "2020-04-27",
            "2021-04-26",
            "2022-04-25",
            "2023-04-24",
            "2024-04-29",
        )
        self.assertSubdivMsHolidayName(name, range(1866, self.end_year))
        self.assertNoSubdivMsHolidayName(name, range(self.start_year, 1866))

        self.assertSubdivTxHolidayName(
            name, (f"{year}-01-19" for year in range(1931, self.end_year))
        )
        self.assertNoSubdivTxHolidayName(name, range(self.start_year, 1931))

        self.assertSubdivGaHolidayName(name, range(1866, 2016))
        self.assertNoSubdivGaHolidayName(name, range(2016, self.end_year))
        self.assertSubdivGaHolidayName(
            name,
            "2010-04-26",
            "2011-04-25",
            "2012-04-23",
            "2013-04-22",
            "2014-04-28",
            "2015-04-27",
        )

        name = "State Holiday"
        self.assertNoHolidayName(name)
        self.assertSubdivGaHolidayName(name, range(2016, self.end_year))
        self.assertSubdivGaHolidayName(
            name,
            "2016-04-25",
            "2017-04-24",
            "2018-04-23",
            "2019-04-22",
            "2020-04-10",
            "2021-04-26",
            "2022-04-25",
            "2023-04-24",
        )

    def test_san_jacinto_day(self):
        name = "San Jacinto Day"
        self.assertNoHolidayName(name)
        self.assertSubdivTxHolidayName(
            name, (f"{year}-04-21" for year in range(1875, self.end_year))
        )
        self.assertNoSubdivTxHolidayName(name, range(self.start_year, 1875))

    def test_arbor_day(self):
        name = "Arbor Day"
        self.assertNoHolidayName(name)
        dt = (
            "1989-04-28",
            "2010-04-30",
            "2011-04-29",
            "2012-04-27",
            "2013-04-26",
            "2014-04-25",
            "2015-04-24",
            "2016-04-29",
            "2017-04-28",
            "2018-04-27",
            "2019-04-26",
            "2020-04-24",
            "2021-04-30",
            "2022-04-29",
            "2023-04-28",
        )
        self.assertSubdivNeHolidayName(name, (f"{year}-04-22" for year in range(1875, 1989)))
        self.assertNoSubdivNeHolidayName(name, range(self.start_year, 1875))
        self.assertSubdivNeHolidayName(name, dt)

    def test_primary_election_day(self):
        name = "Primary Election Day"
        self.assertNoHolidayName(name)
        dt = (
            "2006-05-02",
            "2008-05-06",
            "2010-05-04",
            "2012-05-08",
            "2014-05-06",
            "2015-05-05",
            "2016-05-03",
            "2017-05-02",
            "2018-05-08",
            "2019-05-07",
            "2020-05-05",
            "2021-05-04",
            "2022-05-03",
            "2023-05-02",
        )
        self.assertSubdivInHolidayName(
            name, 2006, 2008, 2010, 2012, 2014, range(2015, self.end_year)
        )
        self.assertNoSubdivInHolidayName(
            name, range(self.start_year, 2006), 2007, 2009, 2011, 2013
        )
        self.assertSubdivInHolidayName(name, dt)

    def test_truman_day(self):
        name = "Truman Day"
        self.assertNoHolidayName(name)
        self.assertSubdivMoHolidayName(
            name, (f"{year}-05-08" for year in range(1949, self.end_year))
        )
        self.assertNoSubdivMoHolidayName(name, range(self.start_year, 1949))
        obs_dt = (
            "2010-05-07",
            "2011-05-09",
            "2016-05-09",
            "2021-05-07",
            "2022-05-09",
        )
        self.assertSubdivMoHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivMoNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_jefferson_davis_birthday(self):
        name = "Jefferson Davis Birthday"
        self.assertNoHolidayName(name)
        self.assertSubdivAlHolidayName(name, range(1890, self.end_year))
        self.assertNoSubdivAlHolidayName(name, range(self.start_year, 1890))
        dt = (
            "2010-06-07",
            "2011-06-06",
            "2012-06-04",
            "2013-06-03",
            "2014-06-02",
            "2015-06-01",
            "2016-06-06",
            "2017-06-05",
            "2018-06-04",
            "2019-06-03",
            "2020-06-01",
            "2021-06-07",
            "2022-06-06",
            "2023-06-05",
        )
        self.assertSubdivAlHolidayName(name, dt)

    def test_kamehameha_day(self):
        name = "Kamehameha Day"
        self.assertNoHolidayName(name)
        self.assertSubdivHiHolidayName(
            name, (f"{year}-06-11" for year in range(1872, self.end_year))
        )
        self.assertNoSubdivHiHolidayName(name, range(self.start_year, 1872))
        obs_dt = (
            "2011-06-10",
            "2016-06-10",
            "2017-06-12",
            "2022-06-10",
            "2023-06-12",
        )
        self.assertSubdivHiHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivHiNonObservedHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivHiHolidayName(f"{name} (observed)", range(1872, 2011))

    def test_emancipation_day_in_texas(self):
        name = "Emancipation Day In Texas"
        self.assertNoHolidayName(name)
        self.assertSubdivTxHolidayName(
            name, (f"{year}-06-19" for year in range(1980, self.end_year))
        )
        self.assertNoSubdivTxHolidayName(name, range(self.start_year, 1980))

    def test_west_virginia_day(self):
        name = "West Virginia Day"
        self.assertNoHolidayName(name)
        self.assertSubdivWvHolidayName(
            name, (f"{year}-06-20" for year in range(1927, self.end_year))
        )
        self.assertNoSubdivWvHolidayName(name, range(self.start_year, 1927))
        obs_dt = (
            "2010-06-21",
            "2015-06-19",
            "2020-06-19",
            "2021-06-21",
        )
        self.assertSubdivWvHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivWvNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_emancipation_day_in_virgin_islands(self):
        name = "Emancipation Day"
        self.assertNoHolidayName(name)
        self.assertSubdivViHolidayName(
            name, (f"{year}-07-03" for year in range(self.start_year, self.end_year))
        )

    def test_manua_islands_cession_day(self):
        name = "Manu'a Islands Cession Day"
        self.assertNoHolidayName(name)
        self.assertSubdivAsHolidayName(
            name, (f"{year}-07-16" for year in range(1983, self.end_year))
        )
        self.assertNoSubdivAsHolidayName(name, range(self.start_year, 1983))
        obs_dt = (
            "2000-07-17",
            "2005-07-15",
            "2006-07-17",
            "2011-07-15",
            "2016-07-15",
            "2017-07-17",
            "2022-07-15",
            "2023-07-17",
        )
        self.assertSubdivAsHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivAsNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_liberation_day_guam(self):
        name = "Liberation Day (Guam)"
        self.assertNoHolidayName(name)
        self.assertSubdivGuHolidayName(
            name, (f"{year}-07-21" for year in range(1945, self.end_year))
        )
        self.assertNoSubdivGuHolidayName(name, range(self.start_year, 1945))

    def test_pioneer_day(self):
        name = "Pioneer Day"
        self.assertNoHolidayName(name)
        self.assertSubdivUtHolidayName(
            name, (f"{year}-07-24" for year in range(1849, self.end_year))
        )
        self.assertNoSubdivUtHolidayName(name, range(self.start_year, 1848))
        obs_dt = (
            "2010-07-23",
            "2011-07-25",
            "2016-07-25",
            "2021-07-23",
            "2022-07-25",
        )
        self.assertSubdivUtHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivUtNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertNoHolidayName(name)
        self.assertSubdivPrHolidayName(
            name, (f"{year}-07-25" for year in range(self.start_year, self.end_year))
        )
        obs_dt = (
            "1999-07-26",
            "2004-07-26",
            "2010-07-26",
            "2021-07-26",
        )
        self.assertSubdivPrHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivPrNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_victory_day(self):
        name = "Victory Day"
        self.assertNoHolidayName(name)
        self.assertSubdivRiHolidayName(name, range(1948, self.end_year))
        self.assertNoSubdivRiHolidayName(name, range(self.start_year, 1948))
        dt = (
            "2010-08-09",
            "2011-08-08",
            "2012-08-13",
            "2013-08-12",
            "2014-08-11",
            "2015-08-10",
            "2016-08-08",
            "2017-08-14",
            "2018-08-13",
            "2019-08-12",
            "2020-08-10",
            "2021-08-09",
            "2022-08-08",
            "2023-08-14",
        )
        self.assertSubdivRiHolidayName(name, dt)

    def test_statehood_day(self):
        name = "Statehood Day"
        self.assertNoHolidayName(name)
        self.assertSubdivHiHolidayName(name, range(1959, self.end_year))
        self.assertNoSubdivHiHolidayName(name, range(self.start_year, 1959))
        dt = (
            "2010-08-20",
            "2011-08-19",
            "2012-08-17",
            "2013-08-16",
            "2014-08-15",
            "2015-08-21",
            "2016-08-19",
            "2017-08-18",
            "2018-08-17",
            "2019-08-16",
            "2020-08-21",
            "2021-08-20",
            "2022-08-19",
            "2023-08-18",
        )
        self.assertSubdivHiHolidayName(name, dt)

    def test_bennington_battle_day(self):
        name = "Bennington Battle Day"
        self.assertNoHolidayName(name)
        self.assertSubdivVtHolidayName(
            name, (f"{year}-08-16" for year in range(1778, self.end_year))
        )
        self.assertNoSubdivVtHolidayName(name, 1777)
        obs_dt = (
            "2009-08-17",
            "2014-08-15",
            "2015-08-17",
            "2020-08-17",
        )
        self.assertSubdivVtHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivVtNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_lyndon_baines_johnson_day(self):
        name = "Lyndon Baines Johnson Day"
        self.assertNoHolidayName(name)
        self.assertSubdivTxHolidayName(
            name, (f"{year}-08-27" for year in range(1973, self.end_year))
        )
        self.assertNoSubdivTxHolidayName(name, range(self.start_year, 1973))

    def test_commonwealth_cultural_day(self):
        name = "Commonwealth Cultural Day"
        self.assertNoHolidayName(name)
        dt = (
            "2010-10-11",
            "2011-10-10",
            "2012-10-08",
            "2013-10-14",
            "2014-10-13",
            "2015-10-12",
            "2016-10-10",
            "2017-10-09",
            "2018-10-08",
            "2019-10-14",
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
        )
        self.assertSubdivMpHolidayName(name, dt)

    def test_white_sunday(self):
        name = "White Sunday"
        self.assertNoHolidayName(name)
        self.assertSubdivAsHolidayName(name, range(self.start_year, self.end_year))
        dt = (
            "2010-10-10",
            "2011-10-09",
            "2012-10-14",
            "2013-10-13",
            "2014-10-12",
            "2015-10-11",
            "2016-10-09",
            "2017-10-08",
            "2018-10-14",
            "2019-10-13",
            "2020-10-11",
            "2021-10-10",
            "2022-10-09",
            "2023-10-08",
            "2024-10-13",
        )
        self.assertSubdivAsHolidayName(name, dt)

    def test_alaska_day(self):
        name = "Alaska Day"
        self.assertNoHolidayName(name)
        self.assertSubdivAkHolidayName(
            name, (f"{year}-10-18" for year in range(1917, self.end_year))
        )
        self.assertNoSubdivAkHolidayName(name, range(self.start_year, 1917))
        obs_dt = (
            "2009-10-19",
            "2014-10-17",
            "2015-10-19",
            "2020-10-19",
        )
        self.assertSubdivAkHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivAkNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_nevada_day(self):
        name = "Nevada Day"
        self.assertNoHolidayName(name)
        self.assertSubdivNvHolidayName(name, (f"{year}-10-31" for year in range(1933, 2000)))
        self.assertNoSubdivNvHolidayName(name, range(self.start_year, 1933))
        dt = (
            "2000-10-27",
            "2010-10-29",
            "2011-10-28",
            "2012-10-26",
            "2013-10-25",
            "2014-10-31",
            "2015-10-30",
            "2016-10-28",
            "2017-10-27",
            "2018-10-26",
            "2019-10-25",
            "2020-10-30",
            "2021-10-29",
            "2022-10-28",
            "2023-10-27",
        )
        self.assertSubdivNvHolidayName(name, dt)

        obs_dt = (
            "1992-10-30",
            "1993-11-01",
            "1998-10-30",
            "1999-11-01",
        )
        self.assertSubdivNvHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivNvNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_liberty_day(self):
        name = "Liberty Day"
        self.assertNoHolidayName(name)
        self.assertSubdivViHolidayName(
            name, (f"{year}-11-01" for year in range(self.start_year, self.end_year))
        )

    def test_election_day(self):
        name = "Election Day"
        self.assertNoHolidayName(name)
        dt = (
            "2008-11-04",
            "2010-11-02",
            "2012-11-06",
            "2014-11-04",
            "2016-11-08",
            "2018-11-06",
            "2020-11-03",
            "2022-11-08",
        )
        for subdiv in ("DE", "HI", "IL", "LA", "MI", "MP", "MT", "NH", "NJ", "WV"):
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], dt)
            self.assertNoHolidayName(
                name,
                self.subdiv_holidays[subdiv],
                range(self.start_year, 2008),
                range(2009, self.end_year, 2),
            )

        dt = (
            "2008-11-04",
            "2010-11-02",
            "2012-11-06",
            "2014-11-04",
            "2015-11-03",
            "2016-11-08",
            "2017-11-07",
            "2018-11-06",
            "2019-11-05",
            "2020-11-03",
            "2021-11-02",
            "2022-11-08",
            "2023-11-07",
        )
        for subdiv in ("IN", "NY"):
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], dt)
            self.assertNoHolidayName(
                name, self.subdiv_holidays[subdiv], range(self.start_year, 2008)
            )

        # For NON_OFFICIAL category
        # This is actually for the Presidential Election, but let's keep the same name
        # to prevent duplicates for states which have them as proper public holidays.

        dt = (
            "1868-11-03",
            "1872-11-05",
            "1876-11-07",
            "1880-11-02",
            "1884-11-04",
            "1888-11-06",
            "1892-11-08",
            "1896-11-03",
            "1900-11-06",
            "1904-11-08",
            "1908-11-03",
            "1912-11-05",
            "1916-11-07",
            "1920-11-02",
            "1924-11-04",
            "1928-11-06",
            "1932-11-08",
            "1936-11-03",
            "1940-11-05",
            "1944-11-07",
            "1948-11-02",
            "1952-11-04",
            "1956-11-06",
            "1960-11-08",
            "1964-11-03",
            "1968-11-05",
            "1972-11-07",
            "1976-11-02",
            "1980-11-04",
            "1984-11-06",
            "1988-11-08",
            "1992-11-03",
            "1996-11-05",
            "2000-11-07",
            "2004-11-02",
            "2008-11-04",
            "2012-11-06",
            "2016-11-08",
            "2020-11-03",
            "2024-11-05",
        )
        for subdiv in UnitedStates.subdivisions:
            holidays = UnitedStates(subdiv=subdiv, categories=UNOFFICIAL, years=self.full_range)
            if subdiv in {"AS", "GU", "MP", "PR", "UM", "VI"}:
                self.assertNoHolidayName(name, holidays)
            else:
                self.assertHolidayName(name, holidays, dt)
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1848))

    def test_valentines_day(self):
        name = "Valentine's Day"
        self.assertNoHolidayName(name)
        self.assertUnofficialHolidayName(
            name, (f"{year}-02-14" for year in range(1847, self.end_year))
        )
        self.assertNoUnofficialHolidayName(name, range(self.start_year, 1847))

    def test_st_patricks_day(self):
        name = "Saint Patrick's Day"
        self.assertNoHolidayName(name)
        self.assertUnofficialHolidayName(
            name, (f"{year}-03-17" for year in range(self.start_year, self.end_year))
        )

    def test_mothers_day(self):
        name = "Mother's Day"
        self.assertNoHolidayName(name)
        self.assertUnofficialHolidayName(
            name,
            "2020-05-10",
            "2021-05-09",
            "2022-05-08",
            "2023-05-14",
            "2024-05-12",
            "2025-05-11",
        )
        self.assertUnofficialHolidayName(name, range(1914, 2050))
        self.assertNoUnofficialHolidayName(name, range(1777, 1914))

    def test_fathers_day(self):
        name = "Father's Day"
        self.assertNoHolidayName(name)
        self.assertUnofficialHolidayName(
            name,
            "2020-06-21",
            "2021-06-20",
            "2022-06-19",
            "2023-06-18",
            "2024-06-16",
            "2025-06-15",
        )
        self.assertUnofficialHolidayName(name, range(1972, 2050))
        self.assertNoUnofficialHolidayName(name, range(1777, 1972))

    def test_halloween(self):
        name = "Halloween"
        self.assertNoHolidayName(name)
        self.assertUnofficialHolidayName(
            name, (f"{year}-10-31" for year in range(self.start_year, self.end_year))
        )

    def test_groundhog_day(self):
        name = "Groundhog Day"
        self.assertNoHolidayName(name)
        self.assertUnofficialHolidayName(
            name, (f"{year}-02-02" for year in range(1886, self.end_year))
        )
        self.assertNoUnofficialHolidayName(name, range(self.start_year, 1886))
        for subdiv in UnitedStates.subdivisions:
            holidays = UnitedStates(subdiv=subdiv, categories=UNOFFICIAL, years=self.full_range)
            if subdiv in {"AS", "GU", "MP", "PR", "UM", "VI"}:
                self.assertNoHolidayName(name, holidays)
            else:
                self.assertHolidayName(
                    name, holidays, (f"{year}-02-02" for year in range(1886, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1886))

    def test_all_souls_day(self):
        name = "All Souls' Day"
        self.assertNoHolidayName(name)
        self.assertSubdivGuHolidayName(
            name, (f"{year}-11-02" for year in range(self.start_year, self.end_year))
        )

    def test_citizenship_day(self):
        name = "Citizenship Day"
        self.assertNoHolidayName(name)
        self.assertSubdivMpHolidayName(
            name, (f"{year}-11-04" for year in range(self.start_year, self.end_year))
        )
        obs_dt = (
            "2012-11-05",
            "2017-11-03",
            "2018-11-05",
            "2023-11-03",
        )
        self.assertSubdivMpHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivMpNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_discovery_day(self):
        name = "Discovery Day"
        self.assertNoHolidayName(name)
        self.assertSubdivPrHolidayName(
            name, (f"{year}-11-19" for year in range(self.start_year, self.end_year))
        )
        obs_dt = (
            "2000-11-20",
            "2006-11-20",
            "2017-11-20",
            "2023-11-20",
        )
        self.assertSubdivPrHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivPrNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_day_after_thanksgiving(self):
        dt = (
            "2017-11-24",
            "2018-11-23",
            "2019-11-29",
            "2020-11-27",
            "2021-11-26",
            "2022-11-25",
            "2023-11-24",
            "2024-11-29",
        )
        for subdiv, name, start_year in (
            ("CA", "Day After Thanksgiving", 1975),
            ("DE", "Day After Thanksgiving", 1975),
            ("FL", "Friday After Thanksgiving", 1975),
            ("IN", "Lincoln's Birthday", 2010),
            ("MD", "American Indian Heritage Day", 2008),
            ("MI", "Day After Thanksgiving", 2017),
            ("NC", "Day After Thanksgiving", 1975),
            ("NH", "Day After Thanksgiving", 1975),
            ("NM", "Presidents' Day", None),
            ("NV", "Family Day", None),
            ("OK", "Day After Thanksgiving", 1975),
            ("PA", "Day After Thanksgiving", None),
            ("TX", "Friday After Thanksgiving", 1975),
            ("WA", "Native American Heritage Day", 2014),
            ("WV", "Day After Thanksgiving", 1975),
        ):
            self.assertNoHolidayName(name)
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], dt)
            self.assertHolidayName(
                name,
                self.subdiv_holidays[subdiv],
                range(start_year or self.start_year, self.end_year),
            )
            if start_year:
                self.assertNoHolidayName(
                    name, self.subdiv_holidays[subdiv], range(self.start_year, start_year)
                )

    def test_robert_lee_birthday(self):
        name_1986 = "Robert E. Lee's Birthday"
        name_2016 = "State Holiday"
        self.assertNoHolidayName(name_1986)
        self.assertNoHolidayName(name_2016)
        self.assertSubdivGaHolidayName(name_1986, range(1986, 2016))
        self.assertSubdivGaHolidayName(name_2016, range(2016, self.end_year))
        self.assertNoSubdivGaHolidayName(
            name_1986, range(self.start_year, 1986), range(2016, self.end_year)
        )
        self.assertNoSubdivGaHolidayName(name_2016, range(self.start_year, 2016))
        self.assertSubdivGaHolidayName(
            name_1986,
            "2010-11-26",
            "2011-11-25",
            "2012-11-23",
            "2013-11-29",
            "2014-11-28",
            "2015-11-27",
        )
        self.assertSubdivGaHolidayName(
            name_2016,
            "2016-11-25",
            "2017-11-24",
            "2018-11-23",
            "2019-11-29",
            "2020-11-27",
            "2021-11-26",
            "2022-11-25",
            "2023-11-24",
        )

    def test_lady_of_camarin_day(self):
        name = "Lady of Camarin Day"
        self.assertNoHolidayName(name)
        self.assertSubdivGuHolidayName(
            name, (f"{year}-12-08" for year in range(self.start_year, self.end_year))
        )

    def test_constitution_day_mp(self):
        name = "Constitution Day"
        self.assertNoHolidayName(name)
        self.assertSubdivMpHolidayName(
            name, (f"{year}-12-08" for year in range(self.start_year, self.end_year))
        )
        obs_dt = (
            "2012-12-07",
            "2013-12-09",
            "2018-12-07",
            "2019-12-09",
        )
        self.assertSubdivMpHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivMpNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_christmas_eve(self):
        name = "Christmas Eve"
        self.assertNoHolidayName(name)
        obs_dt = (
            "2016-12-23",
            "2017-12-22",
            "2021-12-23",
            "2022-12-23",
            "2023-12-22",
        )
        for subdiv, start_year in (
            ("KS", 2013),
            ("MI", 2013),
            ("NC", 2013),
            ("TX", 1981),
            ("WI", 2012),
        ):
            self.assertHolidayName(
                name,
                self.subdiv_holidays[subdiv],
                (f"{year}-12-24" for year in range(start_year, self.end_year)),
            )
            self.assertNoHolidayName(
                name, self.subdiv_holidays[subdiv], range(self.start_year, start_year)
            )
            self.assertHolidayName(f"{name} (observed)", self.subdiv_holidays[subdiv], obs_dt)
            self.assertNoNonObservedHolidayName(
                f"{name} (observed)", UnitedStates(subdiv=subdiv, observed=False), obs_dt
            )

    def test_day_after_christmas(self):
        for subdiv, name, start_year in (
            ("NC", "Day After Christmas", 2013),
            ("TX", "Day After Christmas", 1981),
            ("VI", "Christmas Second Day", -1),
        ):
            self.assertNoHolidayName(name)
            self.assertHolidayName(
                name,
                self.subdiv_holidays[subdiv],
                (
                    f"{year}-12-26"
                    for year in range(
                        start_year if start_year > 0 else self.start_year, self.end_year
                    )
                ),
            )
            if start_year > 0:
                self.assertNoHolidayName(
                    name, self.subdiv_holidays[subdiv], range(self.start_year, start_year)
                )
        obs_dt = (
            "2015-12-28",
            "2016-12-27",
            "2020-12-28",
            "2021-12-27",
            "2022-12-27",
        )
        name = "Day After Christmas"
        self.assertSubdivNcHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoSubdivNcNonObservedHolidayName(f"{name} (observed)", obs_dt)

    def test_new_years_eve(self):
        name = "New Year's Eve"
        self.assertNoHolidayName(name)
        obs_dt = (
            "2016-12-30",
            "2022-12-30",
        )
        for subdiv, start_year in (
            ("KY", 2013),
            ("MI", 2013),
            ("WI", 2012),
        ):
            self.assertHolidayName(
                name,
                self.subdiv_holidays[subdiv],
                (f"{year}-12-31" for year in range(start_year, self.end_year)),
            )
            self.assertNoHolidayName(
                name, self.subdiv_holidays[subdiv], range(self.start_year, start_year)
            )
            self.assertHolidayName(f"{name} (observed)", self.subdiv_holidays[subdiv], obs_dt)
            self.assertNoNonObservedHolidayName(
                f"{name} (observed)", UnitedStates(subdiv=subdiv, observed=False), obs_dt
            )

    def test_frances_xavier_cabrini_day(self):
        name = "Frances Xavier Cabrini Day"
        self.assertNoHolidayName(name)
        self.assertNoSubdivCoHolidayName(name, range(self.start_year, 2020))
        self.assertSubdivCoHolidayName(name, range(2020, self.end_year))
        self.assertSubdivCoHolidayName(
            name,
            "2020-10-05",
            "2021-10-04",
            "2022-10-03",
            "2023-10-02",
            "2024-10-07",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany; Three Kings Day"),
            (
                "2022-01-17",
                (
                    "Birthday of Martin Luther King, Jr.; "
                    "Dr. Martin Luther King Jr. / Civil Rights Day; "
                    "Dr. Martin Luther King Jr. and Robert E. Lee's Birthdays; "
                    "Martin Luther King Jr. / Idaho Human Rights Day; Martin Luther King Jr. Day; "
                    "Martin Luther King, Jr & Robert E. Lee's Birthday"
                ),
            ),
            ("2022-01-19", "Confederate Memorial Day"),
            ("2022-02-02", "Groundhog Day"),
            ("2022-02-11", "Lincoln's Birthday (observed)"),
            ("2022-02-12", "Lincoln's Birthday"),
            ("2022-02-14", "Valentine's Day"),
            ("2022-02-15", "Susan B. Anthony Day"),
            (
                "2022-02-21",
                (
                    "George Washington & Thomas Jefferson's Birthday; George Washington Day; "
                    "George Washington's Birthday and Daisy Gatson Bates Day; "
                    "Lincoln's and Washington's Birthdays; Lincoln/Washington Presidents' Day; "
                    "President's Day; Presidents Day; Presidents' Day; "
                    "Washington and Lincoln Day; Washington's Birthday; "
                    "Washington's and Lincoln's Birthday; Washington-Lincoln Day"
                ),
            ),
            ("2022-03-01", "Mardi Gras; Town Meeting Day"),
            ("2022-03-02", "Texas Independence Day"),
            ("2022-03-07", "Casimir Pulaski Day; Guam Discovery Day"),
            ("2022-03-17", "Evacuation Day; Saint Patrick's Day"),
            ("2022-03-22", "Emancipation Day"),
            ("2022-03-24", "Commonwealth Covenant Day"),
            ("2022-03-25", "Prince Jonah Kuhio Kalanianaole Day (observed)"),
            ("2022-03-26", "Prince Jonah Kuhio Kalanianaole Day"),
            ("2022-03-28", "Seward's Day"),
            ("2022-03-31", "Cesar Chavez Day; Transfer Day"),
            ("2022-04-14", "Holy Thursday"),
            ("2022-04-15", "Emancipation Day (observed); Good Friday"),
            ("2022-04-16", "Emancipation Day"),
            ("2022-04-17", "American Samoa Flag Day"),
            ("2022-04-18", "American Samoa Flag Day (observed); Easter Monday; Patriots' Day"),
            ("2022-04-21", "San Jacinto Day"),
            ("2022-04-25", "Confederate Memorial Day; State Holiday"),
            ("2022-04-29", "Arbor Day"),
            ("2022-05-03", "Primary Election Day"),
            ("2022-05-08", "Mother's Day; Truman Day"),
            ("2022-05-09", "Mother's Day (observed); Truman Day (observed)"),
            ("2022-05-30", "Memorial Day"),
            ("2022-06-06", "Jefferson Davis Birthday"),
            ("2022-06-10", "Kamehameha Day (observed)"),
            ("2022-06-11", "Kamehameha Day"),
            (
                "2022-06-19",
                "Emancipation Day In Texas; Father's Day; Juneteenth National Independence Day",
            ),
            ("2022-06-20", "Juneteenth National Independence Day (observed); West Virginia Day"),
            ("2022-07-03", "Emancipation Day"),
            ("2022-07-04", "Independence Day"),
            ("2022-07-15", "Manu'a Islands Cession Day (observed)"),
            ("2022-07-16", "Manu'a Islands Cession Day"),
            ("2022-07-21", "Liberation Day (Guam)"),
            ("2022-07-24", "Pioneer Day"),
            ("2022-07-25", "Constitution Day; Pioneer Day (observed)"),
            ("2022-08-08", "Victory Day"),
            ("2022-08-16", "Bennington Battle Day"),
            ("2022-08-19", "Statehood Day"),
            ("2022-08-27", "Lyndon Baines Johnson Day"),
            ("2022-09-05", "Labor Day"),
            ("2022-10-03", "Frances Xavier Cabrini Day"),
            ("2022-10-09", "White Sunday"),
            (
                "2022-10-10",
                (
                    "Columbus Day; Columbus Day / American Indian Heritage Day / Fraternal Day; "
                    "Columbus Day and Puerto Rico Friendship Day; Commonwealth Cultural Day; "
                    "Indigenous Peoples' Day; Indigenous Peoples' Day / Columbus Day; "
                    "Native Americans' Day"
                ),
            ),
            ("2022-10-18", "Alaska Day"),
            ("2022-10-28", "Nevada Day"),
            ("2022-10-31", "Halloween"),
            ("2022-11-01", "Liberty Day"),
            ("2022-11-02", "All Souls' Day"),
            ("2022-11-04", "Citizenship Day"),
            ("2022-11-08", "Election Day"),
            ("2022-11-11", "Veterans Day"),
            ("2022-11-19", "Discovery Day"),
            ("2022-11-24", "Thanksgiving Day"),
            (
                "2022-11-25",
                (
                    "American Indian Heritage Day; Day After Thanksgiving; Family Day; "
                    "Friday After Thanksgiving; Lincoln's Birthday; Native American Heritage Day; "
                    "Presidents' Day; State Holiday"
                ),
            ),
            ("2022-12-08", "Constitution Day; Lady of Camarin Day"),
            ("2022-12-23", "Christmas Eve (observed); Washington's Birthday"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed); Christmas Second Day; Day After Christmas"),
            ("2022-12-27", "Day After Christmas (observed)"),
            ("2022-12-30", "New Year's Eve (observed)"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-06", "วันสมโภชพระคริสต์แสดงองค์"),
            (
                "2022-01-17",
                (
                    "วัน ดร. มาร์ติน ลูเทอร์ คิง จูเนียร์ / วันสิทธิพลเมือง; วันมาร์ติน ลูเทอร์ "
                    "คิง จูเนียร์; วันมาร์ติน ลูเทอร์ คิง จูเนียร์ / วันสิทธิมนุษยชนไอดาโฮ; "
                    "วันเกิด ดร. มาร์ติน ลูเทอร์ คิง จูเนียร์และโรเบิร์ต อี. ลี; วันเกิดมาร์ติน "
                    "ลูเทอร์ คิง จูเนียร์; วันเกิดมาร์ติน ลูเทอร์ คิง จูเนียร์และโรเบิร์ต อี. ลี"
                ),
            ),
            ("2022-01-19", "วันรำลึกถึงฝ่ายสมาพันธรัฐ"),
            ("2022-02-02", "วันกราวน์ฮ็อก"),
            ("2022-02-11", "ชดเชยวันเกิดลิงคอล์น"),
            ("2022-02-12", "วันเกิดลิงคอล์น"),
            ("2022-02-14", "วันวาเลนไทน์"),
            ("2022-02-15", "วันซูซาน บี. แอนโทนี"),
            (
                "2022-02-21",
                (
                    "วันจอร์จ วอชิงตัน; วันประธานาธิบดี; วันประธานาธิบดีลิงคอล์น/วอชิงตัน; "
                    "วันลิงคอล์นและวอชิงตัน; วันวอชิงตัน-ลิงคอล์น; วันวอชิงตันและลิงคอล์น; "
                    "วันเกิดจอร์จ วอชิงตัน และทอมัส เจฟเฟอร์สัน; วันเกิดจอร์จ วอชิงตันและวันเดซี่ "
                    "แกตสัน เบตส์; วันเกิดวอชิงตัน; วันเกิดวอชิงตันและลิงคอล์น"
                ),
            ),
            ("2022-03-01", "วันประชาคมท้องถิ่น; วันมาร์ดิกราส์"),
            ("2022-03-02", "วันประกาศอิสรภาพเท็กซัส"),
            ("2022-03-07", "วันคาซิเมียร์ พูลาสกี้; วันค้นพบกวม"),
            ("2022-03-17", "วันนักบุญแพทริก; วันอพยพ"),
            ("2022-03-22", "วันเลิกทาส"),
            ("2022-03-24", "วันปฏิญญาเครือรัฐ"),
            ("2022-03-25", "ชดเชยวันเจ้าชายโจนาห์ คูฮิโอ คาลานิอาเนาโอะเล"),
            ("2022-03-26", "วันเจ้าชายโจนาห์ คูฮิโอ คาลานิอาเนาโอะเล"),
            ("2022-03-28", "วันซีเวิร์ด"),
            ("2022-03-31", "วันซีซาร์ ชาเวซ; วันส่งมอบดินแดน"),
            ("2022-04-14", "วันพฤหัสศักดิสิทธิ์"),
            ("2022-04-15", "ชดเชยวันเลิกทาส; วันศุกร์ประเสริฐ"),
            ("2022-04-16", "วันเลิกทาส"),
            ("2022-04-17", "วันธงชาติอเมริกันซามัว"),
            ("2022-04-18", "ชดเชยวันธงชาติอเมริกันซามัว; วันจันทร์อีสเตอร์; วันแพทริออต"),
            ("2022-04-21", "วันรำลึกยุทธการซานฮาซินโต"),
            ("2022-04-25", "วันรำลึกถึงฝ่ายสมาพันธรัฐ; วันหยุดประจำรัฐ"),
            ("2022-04-29", "วันปลูกต้นไม้"),
            ("2022-05-03", "วันเลือกตั้งขั้นต้น"),
            ("2022-05-08", "วันทรูแมน; วันแม่"),
            ("2022-05-09", "ชดเชยวันทรูแมน; ชดเชยวันแม่"),
            ("2022-05-30", "วันรำลึก"),
            ("2022-06-06", "วันเกิดเจฟเฟอร์สัน เดวิส"),
            ("2022-06-10", "ชดเชยวันคาเมฮาเมฮา"),
            ("2022-06-11", "วันคาเมฮาเมฮา"),
            ("2022-06-19", "วันประกาศอิสรภาพแห่งชาติจูนทีนท์; วันพ่อ; วันเลิกทาสในเท็กซัส"),
            ("2022-06-20", "ชดเชยวันประกาศอิสรภาพแห่งชาติจูนทีนท์; วันเวสต์เวอร์จิเนีย"),
            ("2022-07-03", "วันเลิกทาส"),
            ("2022-07-04", "วันประกาศอิสรภาพ"),
            ("2022-07-15", "ชดเชยวันส่งมอบหมู่เกาะมานูอา"),
            ("2022-07-16", "วันส่งมอบหมู่เกาะมานูอา"),
            ("2022-07-21", "วันปลดปล่อย (กวม)"),
            ("2022-07-24", "วันผู้บุกเบิก"),
            ("2022-07-25", "ชดเชยวันผู้บุกเบิก; วันรัฐธรรมนูญ"),
            ("2022-08-08", "วันแห่งชัยชนะ"),
            ("2022-08-16", "วันรำลึกยุทธการเบนนิงตัน"),
            ("2022-08-19", "วันครบรอบการได้รัฐภาพ"),
            ("2022-08-27", "วันลินดอน เบนส์ จอห์นสัน"),
            ("2022-09-05", "วันแรงงาน"),
            ("2022-10-03", "วันฟรานเซส ซาเวียร์ คาบรินี"),
            ("2022-10-09", "วันอาทิตย์ขาว"),
            (
                "2022-10-10",
                (
                    "วันชนพื้นเมืองอเมริกัน; วันวัฒนธรรมแห่งเครือรัฐ; วันแห่งชนพื้นเมือง; "
                    "วันแห่งชนพื้นเมือง / วันโคลัมบัส; วันโคลัมบัส; วันโคลัมบัส / "
                    "วันอนุรักษ์มรดกชนพื้นเมืองอเมริกัน / วันภราดรภาพ; วันโคลัมบัส "
                    "และวันมิตรภาพกับเปอร์โตริโก"
                ),
            ),
            ("2022-10-18", "วันอะลาสกา"),
            ("2022-10-28", "วันเนวาดา"),
            ("2022-10-31", "วันฮาโลวีน"),
            ("2022-11-01", "วันเลิกทาส"),
            ("2022-11-02", "วันภาวนาอุทิศแด่ผู้ล่วงลับ"),
            ("2022-11-04", "วันแห่งความเป็นพลเมือง"),
            ("2022-11-08", "วันเลือกตั้ง"),
            ("2022-11-11", "วันทหารผ่านศึก"),
            ("2022-11-19", "วันค้นพบ"),
            ("2022-11-24", "วันขอบคุณพระเจ้า"),
            (
                "2022-11-25",
                (
                    "วันครอบครัว; วันประธานาธิบดี; วันหยุดประจำรัฐ; วันหลังวันขอบคุณพระเจ้า; "
                    "วันอนุรักษ์มรดกชนพื้นเมืองอเมริกัน; วันเกิดลิงคอล์น; "
                    "ศุกร์หลังวันขอบคุณพระเจ้า"
                ),
            ),
            ("2022-12-08", "วันรัฐธรรมนูญ; วันแม่พระแห่งคามาริน"),
            ("2022-12-23", "ชดเชยวันคริสต์มาสอีฟ; วันเกิดวอชิงตัน"),
            ("2022-12-24", "วันคริสต์มาสอีฟ"),
            ("2022-12-25", "วันคริสต์มาส"),
            ("2022-12-26", "ชดเชยวันคริสต์มาส; วันคริสต์มาสวันที่สอง; วันหลังวันคริสต์มาส"),
            ("2022-12-27", "ชดเชยวันหลังวันคริสต์มาส"),
            ("2022-12-30", "ชดเชยวันสิ้นปี"),
            ("2022-12-31", "วันสิ้นปี"),
        )
