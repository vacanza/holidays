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

from holidays.constants import GOVERNMENT, OPTIONAL
from holidays.countries.canada import Canada, CA, CAN
from tests.common import CommonCountryTests


class TestCanada(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Canada, with_subdiv_categories=True)

    def test_country_aliases(self):
        self.assertAliases(Canada, CA, CAN)

    def test_no_holidays(self):
        self.assertNoHolidays(
            Canada(categories=Canada.supported_categories, years=self.start_year - 1)
        )

    def test_new_years_day(self):
        name = "New Year's Day"
        name_observed = f"{name} (observed)"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        self.assertGovernmentHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        for _, holidays in self.subdiv_holidays.items():
            self.assertHolidayName(name, holidays, (f"{year}-01-01" for year in self.full_range))

        obs_dts = (
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertGovernmentHolidayName(name_observed, obs_dts)
        for subdiv, holidays in self.subdiv_holidays.items():
            self.assertHolidayName(name_observed, holidays, obs_dts)
            self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_good_friday(self):
        name = "Good Friday"
        dts = (
            "1900-04-13",
            "1901-04-05",
            "1902-03-28",
            "1999-04-02",
            "2000-04-21",
            "2010-04-02",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.full_range)
        self.assertGovernmentHolidayName(name, dts)
        self.assertGovernmentHolidayName(name, self.full_range)
        for _, holidays in self.subdiv_holidays.items():
            self.assertHolidayName(name, holidays, dts)
            self.assertHolidayName(name, holidays, self.full_range)

    def test_canada_day(self):
        name_1879 = "Dominion Day"
        name_1983 = "Canada Day"
        self.assertHolidayName(name_1879, (f"{year}-07-01" for year in range(1879, 1983)))
        self.assertHolidayName(name_1983, (f"{year}-07-01" for year in range(1983, self.end_year)))
        self.assertNoHolidayName(
            name_1879, range(self.start_year, 1879), range(1983, self.end_year)
        )
        self.assertNoHolidayName(name_1983, range(self.start_year, 1983))
        self.assertNoHoliday(f"{year}-07-01" for year in range(self.start_year, 1879))

        obs_dts_sat = (
            "2000-07-03",
            "2006-07-03",
            "2017-07-03",
            "2023-07-03",
        )
        obs_dts_sun = (
            "2001-07-02",
            "2007-07-02",
            "2012-07-02",
            "2018-07-02",
        )
        name_observed = f"{name_1983} (observed)"
        self.assertNoHoliday(obs_dts_sat, obs_dts_sun)
        self.assertGovernmentHolidayName(name_observed, obs_dts_sat, obs_dts_sun)
        self.assertNoGovernmentNonObservedHoliday(obs_dts_sat, obs_dts_sun)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"AB", "BC", "QC"}:
                self.assertHolidayName(name_observed, holidays, obs_dts_sun)
                self.assertNoHoliday(holidays, obs_dts_sat)
            elif subdiv in {"NL", "PE", "SK", "YT"}:
                self.assertHoliday(holidays, obs_dts_sat, obs_dts_sun)
            else:
                self.assertNoHoliday(holidays, obs_dts_sat, obs_dts_sun)
            self.assertNoNonObservedHoliday(
                self.subdiv_holidays_non_observed[subdiv], obs_dts_sat, obs_dts_sun
            )

    def test_labor_day(self):
        name = "Labour Day"
        self.assertNoHolidayName(name, range(self.start_year, 1894))
        self.assertHolidayName(name, range(1894, self.end_year))
        self.assertNoGovernmentHolidayName(name, range(self.start_year, 1894))
        self.assertGovernmentHolidayName(name, range(1894, self.end_year))

        dts = (
            "1894-09-03",
            "1900-09-03",
            "1999-09-06",
            "2000-09-04",
            "2014-09-01",
            "2015-09-07",
            "2018-09-03",
            "2019-09-02",
            "2020-09-07",
            "2021-09-06",
            "2022-09-05",
            "2023-09-04",
        )
        self.assertHolidayName(name, dts)
        self.assertGovernmentHolidayName(name, dts)
        for _, holidays in self.subdiv_holidays.items():
            self.assertHolidayName(name, holidays, dts)
            self.assertHolidayName(name, holidays, range(1894, self.end_year))
            self.assertNoHolidayName(name, holidays, range(self.start_year, 1894))

    def test_christmas_day(self):
        name = "Christmas Day"
        name_observed = f"{name} (observed)"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        for _, holidays in self.subdiv_holidays.items():
            self.assertHolidayName(name, holidays, (f"{year}-12-25" for year in self.full_range))

        obs_dts_sat = (
            "2004-12-27",
            "2010-12-27",
            "2021-12-27",
        )
        obs_dts_sun_without_boxing = (
            "2005-12-26",
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
        )
        obs_dts_sun_with_boxing = (
            "2005-12-27",
            "2011-12-27",
            "2016-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(name_observed, obs_dts_sat, obs_dts_sun_without_boxing)
        self.assertNoHoliday(obs_dts_sun_with_boxing)
        self.assertNoNonObservedHoliday(
            obs_dts_sat, obs_dts_sun_with_boxing, obs_dts_sun_without_boxing
        )
        self.assertGovernmentHolidayName(name_observed, obs_dts_sat, obs_dts_sun_with_boxing)
        self.assertNoGovernmentNonObservedHoliday(obs_dts_sat, obs_dts_sun_with_boxing)
        self.assertOptionalHolidayName(name_observed, obs_dts_sat, obs_dts_sun_with_boxing)
        self.assertNoOptionalNonObservedHoliday(obs_dts_sat, obs_dts_sun_with_boxing)
        for subdiv, holidays in self.subdiv_holidays.items():
            self.assertHolidayName(
                name_observed, holidays, obs_dts_sat, obs_dts_sun_without_boxing
            )
            self.assertNoHoliday(holidays, obs_dts_sun_with_boxing)
            self.assertNoNonObservedHoliday(
                self.subdiv_holidays_non_observed[subdiv], obs_dts_sat, obs_dts_sun_with_boxing
            )

    def test_victoria_day(self):
        name = "Victoria Day"
        name_observed = f"{name} (observed)"

        dts = (
            "1953-05-18",
            "2000-05-22",
            "2010-05-24",
            "2018-05-21",
            "2019-05-20",
            "2020-05-18",
            "2021-05-24",
            "2022-05-23",
            "2023-05-22",
        )
        obs_dts = (
            "1903-05-25",
            "1908-05-25",
            "1914-05-25",
            "1925-05-25",
            "1931-05-25",
            "1936-05-25",
            "1942-05-25",
        )
        self.assertNoHolidayName(name)
        self.assertGovernmentHolidayName(name, dts)
        self.assertGovernmentHolidayName(name, (f"{year}-05-24" for year in range(1901, 1953)))
        self.assertGovernmentHolidayName(name, range(1953, self.end_year))
        self.assertNoGovernmentHolidayName(name, range(self.start_year, 1901))
        self.assertGovernmentHolidayName(name_observed, obs_dts)
        self.assertNoGovernmentNonObservedHoliday(obs_dts)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"AB", "BC", "MB", "NT", "NU", "ON", "SK", "YT"}:
                self.assertHolidayName(name, holidays, dts)
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-24" for year in range(1901, 1953))
                )
                self.assertHolidayName(name, holidays, range(1953, self.end_year))
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1901))
                self.assertHolidayName(name_observed, holidays, obs_dts)
                self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], obs_dts)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_national_day_for_truth_and_reconciliation(self):
        name = "National Day for Truth and Reconciliation"
        name_observed = f"{name} (observed)"
        self.assertNoHolidayName(name)
        self.assertGovernmentHolidayName(
            name, (f"{year}-09-30" for year in range(2021, self.end_year))
        )
        self.assertNoGovernmentHolidayName(name, range(self.start_year, 2021))

        obs_dts = (
            "2023-10-02",
            "2028-10-02",
            "2029-10-01",
        )
        self.assertGovernmentHolidayName(name_observed, obs_dts)
        self.assertNoGovernmentNonObservedHoliday(obs_dts)

        subdiv_start_years = {
            "BC": 2023,
            "MB": 2024,
            "NT": 2022,
            "NU": 2022,
            "PE": 2022,
            "YT": 2023,
        }
        for subdiv, holidays in self.subdiv_holidays.items():
            if start_year := subdiv_start_years.get(subdiv):
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-30" for year in range(start_year, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, start_year))
            else:
                self.assertNoHolidayName(name, holidays)
            self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], obs_dts)

        obs_dts = (
            "2028-10-02",
            "2029-10-01",
        )
        self.assertSubdivMbHolidayName(name_observed, obs_dts)
        self.assertNoSubdivMbNonObservedHoliday(obs_dts)

        self.assertSubdivAbOptionalHolidayName(
            name, (f"{year}-09-30" for year in range(2021, self.end_year))
        )
        self.assertNoSubdivAbOptionalHolidayName(name, range(self.start_year, 2021))

    def test_thanksgiving_day(self):
        name_1921 = "Armistice Day"
        name_1931 = "Thanksgiving Day"

        dts_1921 = (
            # By Statute.
            "1921-11-07",
            "1922-11-06",
            "1923-11-12",
            "1924-11-10",
            "1925-11-09",
            "1926-11-08",
            "1927-11-07",
            "1928-11-12",
            "1929-11-11",
            "1930-11-10",
        )
        self.assertNoHolidayName(name_1921)
        self.assertGovernmentHolidayName(name_1921, dts_1921)
        self.assertNoGovernmentHolidayName(
            name_1921, range(self.start_year, 1921), range(1931, self.end_year)
        )

        dts_1931 = (
            # By Proclamation.
            "1931-10-12",
            "1935-10-24",
            # Post-Proclamation of 1957.
            "1990-10-08",
            "1999-10-11",
            "2000-10-09",
            "2013-10-14",
            "2018-10-08",
            "2019-10-14",
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
        )
        self.assertNoHolidayName(name_1931)
        self.assertGovernmentHolidayName(name_1931, dts_1931)
        self.assertGovernmentHolidayName(name_1931, range(1931, self.end_year))
        self.assertNoGovernmentHolidayName(name_1931, range(self.start_year, 1931))

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"AB", "BC", "MB", "NT", "NU", "ON", "QC", "SK", "YT"}:
                self.assertHolidayName(name_1931, holidays, dts_1931)
                self.assertHolidayName(name_1921, holidays, range(1921, 1931))
                self.assertHolidayName(name_1931, holidays, range(1931, self.end_year))
                self.assertNoHolidayName(
                    name_1921, holidays, range(self.start_year, 1921), range(1931, self.end_year)
                )
                self.assertNoHolidayName(name_1931, holidays, range(self.start_year, 1931))
            else:
                self.assertNoHolidayName(name_1921, holidays, dts_1921)
                self.assertNoHolidayName(name_1931, holidays, dts_1931)

        for subdiv in ("NB", "NL"):
            self.assertHolidayName(name_1921, self.subdiv_optional_holidays[subdiv], dts_1921)
            self.assertHolidayName(name_1931, self.subdiv_optional_holidays[subdiv], dts_1931)

    def test_remembrance_day(self):
        name = "Remembrance Day"
        name_observed = f"{name} (observed)"
        self.assertNoHolidayName(name)
        self.assertGovernmentHolidayName(
            name, (f"{year}-11-11" for year in range(1931, self.end_year))
        )
        self.assertNoGovernmentHolidayName(name, range(1900, 1931))

        obs_dts = (
            "2006-11-13",
            "2007-11-12",
            "2012-11-12",
            "2017-11-13",
            "2018-11-12",
            "2023-11-13",
        )
        self.assertGovernmentHolidayName(name_observed, obs_dts)
        self.assertNoGovernmentNonObservedHoliday(obs_dts)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"AB", "BC", "NB", "NL", "NS", "NT", "NU", "PE", "SK", "YT"}:
                start_year = 1981 if subdiv == "NS" else 1931
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-11" for year in range(start_year, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(1900, start_year))
            else:
                self.assertNoHolidayName(name, holidays)

            if subdiv in {"AB", "NL", "NS", "PE", "SK", "YT"}:
                self.assertHolidayName(name_observed, holidays, obs_dts)
                self.assertNoNonObservedHoliday(self.subdiv_holidays_non_observed[subdiv], obs_dts)
            else:
                self.assertNoHoliday(holidays, obs_dts)

        self.assertSubdivMbOptionalHolidayName(
            name, (f"{year}-11-11" for year in range(1931, self.end_year))
        )

    def test_boxing_day(self):
        name = "Boxing Day"
        name_observed = f"{name} (observed)"
        self.assertNoHolidayName(name)
        self.assertGovernmentHolidayName(name, (f"{year}-12-26" for year in self.full_range))

        self.assertOptionalHolidayName(name, (f"{year}-12-26" for year in self.full_range))

        obs_dts = (
            "2004-12-28",
            "2009-12-28",
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertOptionalHolidayName(name_observed, obs_dts)
        self.assertNoOptionalNonObservedHoliday(obs_dts)

        obs_dts = (
            "2004-12-28",
            "2010-12-28",
            "2021-12-28",
        )
        self.assertSubdivOnHolidayName(name_observed, obs_dts)
        self.assertNoSubdivOnNonObservedHoliday(obs_dts)

        for subdiv in ("AB", "NB", "NL"):
            self.assertHolidayName(
                name,
                self.subdiv_optional_holidays[subdiv],
                (f"{year}-12-26" for year in self.full_range),
            )

    def test_family_day(self):
        start_years = {
            "AB": 1990,
            "BC": 2019,
            "MB": 2008,
            "NB": 2018,
            "NS": 2015,
            "ON": 2008,
            "PE": 2010,
            "SK": 2007,
        }
        dts = (
            "1990-02-19",
            "1991-02-18",
            "1992-02-17",
            "1993-02-15",
            "1994-02-21",
            "1995-02-20",
            "1996-02-19",
            "1997-02-17",
            "1998-02-16",
            "1999-02-15",
            "2000-02-21",
            "2001-02-19",
            "2002-02-18",
            "2003-02-17",
            "2004-02-16",
            "2005-02-21",
            "2006-02-20",
            "2007-02-19",
            "2008-02-18",
            "2009-02-16",
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
        subdiv_names = {
            "MB": "Louis Riel Day",
            "NS": "Heritage Day",
            "PE": "Islander Day",
        }
        for subdiv, holidays in self.subdiv_holidays.items():
            name = subdiv_names.get(subdiv, "Family Day")
            for year, dt in enumerate(dts, 1990):
                if subdiv in start_years and year >= start_years[subdiv]:
                    self.assertHolidayName(name, holidays, dt)
                else:
                    self.assertNoHoliday(holidays, dt)
        self.assertNoHoliday(dts)
        self.assertNoHolidayName("Family Day")
        for name in subdiv_names.values():
            self.assertNoHolidayName(name)

        self.assertSubdivBcHoliday(
            "2013-02-11",
            "2014-02-10",
            "2015-02-09",
            "2016-02-08",
            "2017-02-13",
            "2018-02-12",
        )
        self.assertSubdivPeHoliday("2009-02-09")

    def test_easter_monday(self):
        name = "Easter Monday"
        dts = (
            "1900-04-16",
            "1901-04-08",
            "1902-03-31",
            "1999-04-05",
            "2000-04-24",
            "2010-04-05",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
        )
        self.assertNoHoliday(dts)
        self.assertNoHolidayName(name)
        self.assertNoGovernmentHoliday(dts)
        self.assertNoGovernmentHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            self.assertNoHoliday(holidays, dts)
            self.assertNoHolidayName(name, holidays)

            if subdiv in {"AB", "QC"}:
                self.assertHolidayName(name, self.subdiv_optional_holidays[subdiv], dts)

    def test_civic_holiday_ab(self):
        name = "Heritage Day"
        self.assertNoSubdivAbHolidayName(name)
        dts = (
            "1974-08-05",
            "1999-08-02",
            "2000-08-07",
            "2010-08-02",
            "2015-08-03",
            "2020-08-03",
        )
        self.assertNoHoliday(dts)
        self.assertNoHolidayName(name)
        self.assertSubdivAbOptionalHolidayName(name, dts)
        self.assertSubdivAbOptionalHolidayName(name, range(1974, self.end_year))
        self.assertNoSubdivAbOptionalHolidayName(name, range(self.start_year, 1974))

    def test_civic_holiday_bc(self):
        name = "British Columbia Day"
        dts = (
            "1974-08-05",
            "1999-08-02",
            "2000-08-07",
            "2010-08-02",
            "2015-08-03",
            "2020-08-03",
        )
        self.assertNoHoliday(dts)
        self.assertNoHolidayName(name)
        self.assertSubdivBcHolidayName(name, dts)
        self.assertSubdivBcHolidayName(name, range(1974, self.end_year))
        self.assertNoSubdivBcHolidayName(name, range(self.start_year, 1974))

    def test_civic_holiday_mb(self):
        old_name = "Civic Holiday"
        new_name = "Terry Fox Day"
        self.assertNoSubdivMbHolidayName(old_name)
        self.assertNoSubdivMbHolidayName(new_name)

        dts_old = (
            "1900-08-06",
            "1999-08-02",
            "2000-08-07",
            "2010-08-02",
            "2014-08-04",
        )
        dts_new = (
            "2015-08-03",
            "2020-08-03",
        )
        self.assertNoHoliday(dts_old, dts_new)
        self.assertNoHolidayName(old_name)
        self.assertNoHolidayName(new_name)

        self.assertSubdivMbOptionalHolidayName(old_name, dts_old)
        self.assertSubdivMbOptionalHolidayName(old_name, range(1900, 2015))
        self.assertNoSubdivMbOptionalHolidayName(
            old_name, range(self.start_year, 1900), range(2015, self.end_year)
        )

        self.assertSubdivMbOptionalHolidayName(new_name, dts_new)
        self.assertSubdivMbOptionalHolidayName(new_name, range(2015, self.end_year))
        self.assertNoSubdivMbOptionalHolidayName(new_name, range(self.start_year, 2015))

    def test_civic_holiday_nb(self):
        name = "New Brunswick Day"
        dts = (
            "1975-08-04",
            "1999-08-02",
            "2000-08-07",
            "2010-08-02",
            "2015-08-03",
            "2020-08-03",
        )
        self.assertNoHoliday(dts)
        self.assertNoHolidayName(name)
        self.assertSubdivNbHolidayName(name, dts)
        self.assertSubdivNbHolidayName(name, range(1975, self.end_year))
        self.assertNoSubdivNbHolidayName(name, range(self.start_year, 1975))

    def test_civic_holiday_ns(self):
        name = "Natal Day"
        self.assertNoSubdivNsHolidayName(name)
        dts = (
            "1996-08-05",
            "1999-08-02",
            "2000-08-07",
            "2010-08-02",
            "2015-08-03",
            "2020-08-03",
        )
        self.assertNoHoliday(dts)
        self.assertNoHolidayName(name)
        self.assertSubdivNsOptionalHolidayName(name, dts)
        self.assertSubdivNsOptionalHolidayName(name, range(1996, self.end_year))
        self.assertNoSubdivNsOptionalHolidayName(name, range(self.start_year, 1996))

    def test_civic_holiday_nt_nu_on_sk(self):
        name = "Civic Holiday"
        name_sk = "Saskatchewan Day"

        dts = (
            "1900-08-06",
            "1999-08-02",
            "2000-08-07",
            "2010-08-02",
            "2015-08-03",
            "2020-08-03",
        )
        self.assertNoHoliday(dts)
        self.assertNoHolidayName(name)

        self.assertSubdivNtHolidayName(name, dts)
        self.assertSubdivNtHolidayName(name, range(1900, self.end_year))
        self.assertNoSubdivNtHolidayName(name, range(self.start_year, 1900))

        self.assertSubdivNuHolidayName(name, dts)
        self.assertSubdivNuHolidayName(name, range(1900, self.end_year))
        self.assertNoSubdivNuHolidayName(name, range(self.start_year, 1900))

        self.assertSubdivOnOptionalHolidayName(name, dts)
        self.assertSubdivOnOptionalHolidayName(name, range(1900, self.end_year))
        self.assertNoSubdivOnOptionalHolidayName(name, range(self.start_year, 1900))

        self.assertSubdivSkHolidayName(name_sk, dts)
        self.assertSubdivSkHolidayName(name_sk, range(1900, self.end_year))
        self.assertNoSubdivSkHolidayName(name_sk, range(self.start_year, 1900))

    def test_memorial_day(self):
        name = "Memorial Day"
        self.assertNoHolidayName(name)
        self.assertSubdivNlHolidayName(
            name, (f"{year}-07-01" for year in range(1917, self.end_year))
        )
        self.assertNoSubdivNlHolidayName(name, range(1900, 1917))

    def test_st_patricks_day(self):
        name = "Saint Patrick's Day"
        self.assertNoSubdivNlHolidayName(name)
        dts = (
            "1900-03-19",
            "1999-03-15",
            "2000-03-20",
            "2012-03-19",
            "2013-03-18",
            "2014-03-17",
            "2015-03-16",
            "2016-03-14",
            "2020-03-16",
        )
        self.assertNoHoliday(dts)
        self.assertNoHolidayName(name)
        self.assertSubdivNlOptionalHolidayName(name, dts)
        self.assertSubdivNlOptionalHolidayName(name, range(1900, self.end_year))
        self.assertNoSubdivNlOptionalHolidayName(name, range(self.start_year, 1900))

    def test_st_georges_day(self):
        name = "Saint George's Day"
        self.assertNoSubdivNlHolidayName(name)
        dts = (
            "1990-04-23",
            "1999-04-26",
            "2010-04-19",
            "2016-04-25",
            "2020-04-20",
        )
        self.assertNoHoliday(dts)
        self.assertNoHolidayName(name)
        self.assertSubdivNlOptionalHolidayName(name, dts)
        self.assertSubdivNlOptionalHolidayName(name, range(1990, self.end_year))
        self.assertNoSubdivNlOptionalHolidayName(name, range(self.start_year, 1990))

    def test_discovery_day_nl(self):
        name = "Discovery Day"
        self.assertNoSubdivNlHolidayName(name)
        dts = (
            "1997-06-23",
            "1999-06-21",
            "2000-06-26",
            "2010-06-21",
            "2016-06-27",
            "2020-06-22",
        )
        self.assertNoHoliday(dts)
        self.assertNoHolidayName(name)
        self.assertSubdivNlOptionalHolidayName(name, dts)
        self.assertSubdivNlOptionalHolidayName(name, range(1997, self.end_year))
        self.assertNoSubdivNlOptionalHolidayName(name, range(self.start_year, 1997))

    def test_orangemans_day(self):
        name = "Orangemen's Day"
        self.assertNoSubdivNlHolidayName(name)
        dts = (
            "1900-07-09",
            "1999-07-12",
            "2000-07-10",
            "2010-07-12",
            "2016-07-11",
            "2020-07-13",
        )
        self.assertNoHoliday(dts)
        self.assertNoHolidayName(name)
        self.assertSubdivNlOptionalHolidayName(name, dts)
        self.assertSubdivNlOptionalHolidayName(name, range(1900, self.end_year))
        self.assertNoSubdivNlOptionalHolidayName(name, range(self.start_year, 1900))

    def test_discovery_day_yt(self):
        name = "Discovery Day"
        dts = (
            "1912-08-19",
            "1999-08-16",
            "2000-08-21",
            "2006-08-21",
            "2016-08-15",
            "2020-08-17",
        )
        self.assertNoHoliday(dts)
        self.assertNoHolidayName(name)
        self.assertSubdivYtHolidayName(name, dts)
        self.assertSubdivYtHolidayName(name, range(1912, self.end_year))
        self.assertNoSubdivYtHolidayName(name, range(self.start_year, 1912))

    def test_national_aboriginal_day(self):
        name = "National Aboriginal Day"
        self.assertSubdivNtHolidayName(
            name, (f"{year}-06-21" for year in range(2001, self.end_year))
        )
        self.assertNoSubdivNtHolidayName(name, range(self.start_year, 2001))
        self.assertSubdivYtHolidayName(
            name, (f"{year}-06-21" for year in range(2017, self.end_year))
        )
        self.assertNoSubdivYtHolidayName(name, range(self.start_year, 2017))
        self.assertNoHoliday(f"{year}-06-21" for year in range(1996, self.end_year))
        self.assertNoHolidayName(name)

    def test_nunavut_day(self):
        name = "Nunavut Day"
        self.assertNoHolidayName(name)
        self.assertNoHoliday(f"{year}-07-09" for year in range(2001, self.end_year))
        self.assertSubdivNuHolidayName(
            name, (f"{year}-07-09" for year in range(2020, self.end_year))
        )
        self.assertNoSubdivNuHolidayName(name, range(self.start_year, 2020))
        self.assertNoSubdivNuOptionalHoliday("1999-07-09", "2000-07-09", "2020-07-09")
        self.assertSubdivNuOptionalHolidayName(
            name,
            "2000-04-01",
            (f"{year}-07-09" for year in range(2001, 2020)),
        )
        self.assertNoSubdivNuOptionalHolidayName(
            name, range(self.start_year, 2000), range(2020, self.end_year)
        )

    def test_national_patriots_day(self):
        name = "National Patriots' Day"
        self.assertNoHolidayName(name)
        self.assertSubdivQcHolidayName(
            name,
            "2010-05-24",
            "2015-05-18",
            "2020-05-18",
            "2021-05-24",
            "2022-05-23",
        )
        self.assertSubdivQcHolidayName(name, range(2003, self.end_year))
        self.assertNoSubdivQcHolidayName(name, range(self.start_year, 2003))

    def test_st_jean_baptiste_day(self):
        name = "Saint Jean Baptiste Day"
        self.assertNoHolidayName(name)
        self.assertSubdivQcHoliday(f"{year}-06-24" for year in range(1925, self.end_year))
        self.assertNoSubdivQcHoliday(f"{year}-06-24" for year in range(self.start_year, 1925))
        self.assertNoHoliday(f"{year}-06-24" for year in range(1925, self.end_year))
        self.assertSubdivQcHoliday("2001-06-25")
        self.assertNoSubdivQcNonObservedHoliday("2001-06-25")

    def test_yukon_heritage_day(self):
        name = "Heritage Day"
        self.assertNoHolidayName(name)
        self.assertNoSubdivYtHolidayName(name)
        dts = (
            "2017-02-24",
            "2018-02-23",
            "2019-02-22",
            "2020-02-21",
            "2021-02-26",
            "2022-02-25",
        )
        self.assertSubdivYtOptionalHolidayName(name, dts)
        self.assertSubdivYtOptionalHolidayName(name, range(1976, self.end_year))
        self.assertNoSubdivYtOptionalHolidayName(name, range(self.start_year, 1976))

    def test_queens_funeral(self):
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"BC", "NB", "NL", "NS", "PE", "YT"}:
                self.assertHoliday(holidays, "2022-09-19")
            else:
                self.assertNoHoliday(holidays, "2022-09-19")

    def test_public_2022(self):
        self.assertHolidays(
            Canada(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-04-15", "Good Friday"),
            ("2022-07-01", "Canada Day"),
            ("2022-09-05", "Labour Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )

    def test_government_2022(self):
        self.assertHolidays(
            Canada(years=2022, categories=GOVERNMENT),
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-23", "Victoria Day"),
            ("2022-07-01", "Canada Day"),
            ("2022-09-05", "Labour Day"),
            ("2022-09-30", "National Day for Truth and Reconciliation"),
            ("2022-10-10", "Thanksgiving Day"),
            ("2022-11-11", "Remembrance Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_optional_2022(self):
        self.assertHolidays(
            Canada(years=2022, categories=OPTIONAL),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_all_holidays_present(self):
        y_2022 = set()
        for subdiv in Canada.subdivisions:
            y_2022.update(Canada(years=2022, subdiv=subdiv, observed=False).values())
        all_h = {  # Holidays names in their chronological order.
            "New Year's Day",
            "Family Day",
            "Heritage Day",
            "Islander Day",
            "Louis Riel Day",
            "Good Friday",
            "National Patriots' Day",
            "Victoria Day",
            "National Aboriginal Day",
            "Saint Jean Baptiste Day",
            "Canada Day",
            "Canada Day; Memorial Day",
            "Nunavut Day",
            "British Columbia Day",
            "Civic Holiday",
            "New Brunswick Day",
            "Saskatchewan Day",
            "Discovery Day",
            "Labour Day",
            "Funeral of Her Majesty the Queen Elizabeth II",
            "National Day for Truth and Reconciliation",
            "Thanksgiving Day",
            "Remembrance Day",
            "Christmas Day",
            "Boxing Day",
        }

        self.assertEqual(
            all_h,
            y_2022,
            f"missing: {all_h - y_2022 or 'no'}, extra: {y_2022 - all_h or 'no'}",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-02-21", "Family Day; Heritage Day; Islander Day; Louis Riel Day"),
            ("2022-02-25", "Heritage Day"),
            ("2022-03-14", "Saint Patrick's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-25", "Saint George's Day"),
            ("2022-05-23", "National Patriots' Day; Victoria Day"),
            ("2022-06-21", "National Aboriginal Day"),
            ("2022-06-24", "Saint Jean Baptiste Day"),
            ("2022-06-27", "Discovery Day"),
            ("2022-07-01", "Canada Day; Memorial Day"),
            ("2022-07-09", "Nunavut Day"),
            ("2022-07-11", "Orangemen's Day"),
            (
                "2022-08-01",
                "British Columbia Day; Civic Holiday; Heritage Day; Natal Day; "
                "New Brunswick Day; Saskatchewan Day; Terry Fox Day",
            ),
            ("2022-08-15", "Discovery Day"),
            ("2022-09-05", "Labour Day"),
            ("2022-09-19", "Funeral of Her Majesty the Queen Elizabeth II"),
            ("2022-09-30", "National Day for Truth and Reconciliation"),
            ("2022-10-10", "Thanksgiving Day"),
            ("2022-11-11", "Remembrance Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day; Christmas Day (observed)"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_l10n_ar(self):
        self.assertLocalizedHolidays(
            "ar",
            ("2022-01-01", "يوم السنة الجديدة"),
            ("2022-01-03", "يوم السنة الجديدة (ملاحظة)"),
            ("2022-02-21", "يوم التراث; يوم الجزيرة; يوم العائلة; يوم لويس رئيل"),
            ("2022-02-25", "يوم التراث"),
            ("2022-03-14", "عيد القديس باتريك"),
            ("2022-04-15", "جمعة جيدة"),
            ("2022-04-18", "عيد الفصح الاثنين"),
            ("2022-04-25", "عيد القديس جورج"),
            ("2022-05-23", "يوم الوطنيين; يوم فيكتوريا"),
            ("2022-06-21", "اليوم الوطني للسكان الأصليين"),
            ("2022-06-24", "عيد القديس جان بابتيست"),
            ("2022-06-27", "يوم الاكتشاف"),
            ("2022-07-01", "يوم الذكرى; يوم كندا"),
            ("2022-07-09", "يوم نونافوت"),
            ("2022-07-11", "يوم رجال البرتقال"),
            (
                "2022-08-01",
                "عطلة المدنية; يوم التأسيس; يوم التراث; يوم تيري فوكس; يوم ساسكاتشوان; "
                "يوم كولومبيا البريطانية; يوم نيو برونزويك",
            ),
            ("2022-08-15", "يوم الاكتشاف"),
            ("2022-09-05", "عيد العمال"),
            ("2022-09-19", "جنازة جلالة الملكة اليزابيث الثانية"),
            ("2022-09-30", "اليوم الوطني للحقيقة والمصالحة"),
            ("2022-10-10", "عيد الشكر"),
            ("2022-11-11", "يوم الذكرى"),
            ("2022-12-25", "عيد الميلاد"),
            ("2022-12-26", "عيد الميلاد (ملاحظة); يوم الملاكمة"),
            ("2022-12-27", "عيد الميلاد (ملاحظة)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-02-21", "Family Day; Heritage Day; Islander Day; Louis Riel Day"),
            ("2022-02-25", "Heritage Day"),
            ("2022-03-14", "Saint Patrick's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-25", "Saint George's Day"),
            ("2022-05-23", "National Patriots' Day; Victoria Day"),
            ("2022-06-21", "National Aboriginal Day"),
            ("2022-06-24", "Saint John the Baptist Day"),
            ("2022-06-27", "Discovery Day"),
            ("2022-07-01", "Canada Day; Memorial Day"),
            ("2022-07-09", "Nunavut Day"),
            ("2022-07-11", "Orangemen's Day"),
            (
                "2022-08-01",
                "British Columbia Day; Civic Holiday; Heritage Day; Natal Day; New Brunswick Day; "
                "Saskatchewan Day; Terry Fox Day",
            ),
            ("2022-08-15", "Discovery Day"),
            ("2022-09-05", "Labor Day"),
            ("2022-09-19", "Funeral of Her Majesty the Queen Elizabeth II"),
            ("2022-09-30", "National Day for Truth and Reconciliation"),
            ("2022-10-10", "Thanksgiving Day"),
            ("2022-11-11", "Remembrance Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day; Christmas Day (observed)"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2022-01-01", "Jour de l'an"),
            ("2022-01-03", "Jour de l'an (Observé)"),
            (
                "2022-02-21",
                "Fête de la famille; Fête des Insulaires; Fête du Patrimoine; Journée Louis Riel",
            ),
            ("2022-02-25", "Fête du Patrimoine"),
            ("2022-03-14", "Fête de la Saint-Patrick"),
            ("2022-04-15", "Vendredi saint"),
            ("2022-04-18", "Lundi de Pâques"),
            ("2022-04-25", "Fête de la Saint-Georges"),
            ("2022-05-23", "Fête de la Reine; Journée nationale des patriotes"),
            ("2022-06-21", "Journée nationale des Autochtones"),
            ("2022-06-24", "Fête nationale du Québec"),
            ("2022-06-27", "Jour de la Découverte"),
            ("2022-07-01", "Fête du Canada; Jour de mémorial"),
            ("2022-07-09", "Jour du Nunavut"),
            ("2022-07-11", "Journée des Orangistes"),
            (
                "2022-08-01",
                "Fête du Patrimoine; Jour de la Colombie Britannique; Jour de la Fondation; "
                "Jour du Nouveau Brunswick; Jour du Saskatchewan; Journée Terry Fox; "
                "Premier lundi d'août",
            ),
            ("2022-08-15", "Jour de la Découverte"),
            ("2022-09-05", "Fête du Travail"),
            ("2022-09-19", "Funéraire de sa majesté la reine Elizabeth II"),
            ("2022-09-30", "Journée nationale de la vérité et de la réconciliation"),
            ("2022-10-10", "Action de grâce"),
            ("2022-11-11", "Jour du Souvenir"),
            ("2022-12-25", "Jour de Noël"),
            ("2022-12-26", "Boxing Day; Jour de Noël (Observé)"),
            ("2022-12-27", "Jour de Noël (Observé)"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-03", "ชดเชยวันขึ้นปีใหม่"),
            (
                "2022-02-21",
                "วันครอบครัว; วันชาวเกาะ (พรินซ์เอดเวิร์ดไอแลนด์); วันมรดก; วันหลุยส์เรียล (แมนิโทบา)",
            ),
            ("2022-02-25", "วันมรดก"),
            ("2022-03-14", "วันเซนต์แพทริก (นิวฟันด์แลนด์และแลบราดอร์)"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-04-25", "วันเซนต์จอร์จ (นิวฟันด์แลนด์และแลบราดอร์)"),
            ("2022-05-23", "วันรำลึกกลุ่มแปตรีออต (ควิเบก); วันวิคตอเรีย"),
            ("2022-06-21", "วันชนพื้นเมือง (นอร์ทเวสต์เทร์ริทอรีส์)"),
            ("2022-06-24", "วันแซงต์-ฌ็อง-บาติสต์ (ควิเบก)"),
            ("2022-06-27", "วันแห่งการค้นภพ"),
            ("2022-07-01", "วันชาติแคนาดา; วันรำลึก (นิวฟันด์แลนด์และแลบราดอร์)"),
            ("2022-07-09", "วันนูนาวุต"),
            ("2022-07-11", "วันออเรนจ์เมนส์"),
            (
                "2022-08-01",
                "วันซัสแคตเชวัน; วันนิวบรันสวิก; วันบริติชโคลัมเบีย; วันมรดก; วันสถาปนา; "
                "วันหยุดราชการ; วันเทร์รี ฟอกซ์",
            ),
            ("2022-08-15", "วันแห่งการค้นภพ"),
            ("2022-09-05", "วันแรงงาน"),
            ("2022-09-19", "พระราชพิธีพระบรมศพของสมเด็จพระราชินีนาถเอลิซาเบธที่ 2"),
            ("2022-09-30", "วันชาติแห่งความจริงและการปรองดอง"),
            ("2022-10-10", "วันขอบคุณพระเจ้า"),
            ("2022-11-11", "วันรำลึก"),
            ("2022-12-25", "วันคริสต์มาส"),
            ("2022-12-26", "ชดเชยวันคริสต์มาส; วันเปิดกล่องของขวัญ"),
            ("2022-12-27", "ชดเชยวันคริสต์มาส"),
        )
