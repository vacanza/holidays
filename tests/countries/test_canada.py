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

from holidays.constants import GOVERNMENT, OPTIONAL, PUBLIC
from holidays.countries.canada import Canada, CA, CAN
from tests.common import CommonCountryTests


class TestCanada(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1867, 2050)
        years_non_observed = range(2000, 2024)
        super().setUpClass(Canada, years=years, years_non_observed=years_non_observed)
        cls.prov_hols = {prov: CA(subdiv=prov, years=years) for prov in CA.subdivisions}
        cls.prov_hols_nonobs = {
            prov: CA(subdiv=prov, years=years_non_observed, observed=False)
            for prov in CA.subdivisions
        }
        cls.gov_hols = CA(years=years, categories=GOVERNMENT)
        cls.opt_hols = CA(years=years, categories=OPTIONAL)
        cls.prov_opt_hols = {
            prov: CA(subdiv=prov, years=years, categories=OPTIONAL) for prov in CA.subdivisions
        }

    def test_country_aliases(self):
        self.assertAliases(Canada, CA, CAN)

    def test_no_holidays(self):
        self.assertNoHolidays(Canada(categories=(GOVERNMENT, OPTIONAL, PUBLIC), years=1866))

    def test_new_years_day(self):
        name = "New Year's Day"
        name_observed = f"{name} (observed)"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1867, 2050)))
        self.assertHolidayName(
            name, self.gov_hols, (f"{year}-01-01" for year in range(1867, 2050))
        )
        for _, holidays in self.prov_hols.items():
            self.assertHolidayName(name, holidays, (f"{year}-01-01" for year in range(1867, 2050)))

        dts = (
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(name_observed, dts)
        self.assertHolidayName(name_observed, self.gov_hols, dts)
        for prov, holidays in self.prov_hols.items():
            self.assertHolidayName(name_observed, holidays, dts)
            self.assertNoNonObservedHoliday(self.prov_hols_nonobs[prov], dts)
        self.assertNoNonObservedHoliday(dts)

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
        self.assertHolidayName(name, range(1867, 2050))
        self.assertHolidayName(name, self.gov_hols, dts)
        self.assertHolidayName(name, self.gov_hols, range(1867, 2050))
        for _, holidays in self.prov_hols.items():
            self.assertHolidayName(name, holidays, dts)
            self.assertHolidayName(name, holidays, range(1867, 2050))

    def test_canada_day(self):
        name_1 = "Dominion Day"
        name_2 = "Canada Day"
        self.assertHolidayName(name_1, (f"{year}-07-01" for year in range(1879, 1983)))
        self.assertHolidayName(name_2, (f"{year}-07-01" for year in range(1983, 2050)))
        self.assertNoHolidayName(name_1, range(1867, 1879), range(1983, 2050))
        self.assertNoHolidayName(name_2, range(1867, 1983))
        self.assertNoHoliday(f"{year}-07-01" for year in range(1867, 1879))

        dts_sat = (
            "2000-07-03",
            "2006-07-03",
            "2017-07-03",
            "2023-07-03",
        )
        dts_sun = (
            "2001-07-02",
            "2007-07-02",
            "2012-07-02",
            "2018-07-02",
        )
        name_observed = f"{name_2} (observed)"
        self.assertNoHoliday(dts_sat, dts_sun)
        self.assertHolidayName(name_observed, self.gov_hols, dts_sat, dts_sun)
        self.assertNoNonObservedHoliday(
            CA(observed=False, categories=GOVERNMENT), dts_sat, dts_sun
        )
        for prov, holidays in self.prov_hols.items():
            if prov in {"AB", "BC", "QC"}:
                self.assertHolidayName(name_observed, self.prov_hols[prov], dts_sun)
                self.assertNoHoliday(self.prov_hols[prov], dts_sat)
            elif prov in {"NL", "PE", "SK", "YT"}:
                self.assertHoliday(self.prov_hols[prov], dts_sat, dts_sun)
            else:
                self.assertNoHoliday(self.prov_hols[prov], dts_sat, dts_sun)
            self.assertNoNonObservedHoliday(self.prov_hols_nonobs[prov], dts_sat, dts_sun)

    def test_labour_day(self):
        name = "Labour Day"
        self.assertNoHolidayName(name, range(1867, 1894))
        self.assertHolidayName(name, range(1894, 2050))
        self.assertNoHolidayName(name, self.gov_hols, range(1867, 1894))
        self.assertHolidayName(name, self.gov_hols, range(1894, 2050))

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
        self.assertHolidayName(name, self.gov_hols, dts)
        for _, holidays in self.prov_hols.items():
            self.assertHolidayName(name, holidays, dts)
            self.assertHolidayName(name, holidays, range(1894, 2050))
            self.assertNoHolidayName(name, holidays, range(1867, 1894))

    def test_christmas_day(self):
        name = "Christmas Day"
        name_observed = f"{name} (observed)"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1867, 2050)))
        for _, holidays in self.prov_hols.items():
            self.assertHolidayName(name, holidays, (f"{year}-12-25" for year in range(1867, 2050)))

        dts_sat = (
            "2004-12-27",
            "2010-12-27",
            "2021-12-27",
        )
        dts_sun_without_boxing = (
            "2005-12-26",
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
        )
        dts_sun_with_boxing = (
            "2005-12-27",
            "2011-12-27",
            "2016-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(name_observed, dts_sat, dts_sun_without_boxing)
        self.assertNoHoliday(dts_sun_with_boxing)
        self.assertNoNonObservedHoliday(dts_sat, dts_sun_with_boxing, dts_sun_without_boxing)
        self.assertHolidayName(name_observed, self.gov_hols, dts_sat, dts_sun_with_boxing)
        self.assertNoNonObservedHoliday(
            CA(observed=False, categories=GOVERNMENT), dts_sat, dts_sun_with_boxing
        )
        self.assertHolidayName(name_observed, self.opt_hols, dts_sat, dts_sun_with_boxing)
        self.assertNoNonObservedHoliday(
            CA(observed=False, categories=OPTIONAL), dts_sat, dts_sun_with_boxing
        )
        for prov, holidays in self.prov_hols.items():
            self.assertHolidayName(name_observed, holidays, dts_sat, dts_sun_without_boxing)
            self.assertNoHoliday(holidays, dts_sun_with_boxing)
            self.assertNoNonObservedHoliday(
                self.prov_hols_nonobs[prov], dts_sat, dts_sun_with_boxing
            )

    def test_victoria_day(self):
        name = "Victoria Day"
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
        self.assertNoHolidayName(name)
        self.assertHolidayName(name, self.gov_hols, dts)
        self.assertHolidayName(name, self.gov_hols, range(1953, 2050))
        self.assertNoHolidayName(name, self.gov_hols, range(1867, 1953))

        for prov, holidays in self.prov_hols.items():
            if prov in {"AB", "BC", "MB", "NT", "NU", "ON", "SK", "YT"}:
                self.assertHolidayName(name, holidays, dts)
                self.assertHolidayName(name, holidays, range(1953, 2050))
                self.assertNoHolidayName(name, holidays, range(1867, 1953))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_national_day_for_truth_and_reconciliation(self):
        name = "National Day for Truth and Reconciliation"
        name_observed = f"{name} (observed)"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.gov_hols, (f"{year}-09-30" for year in range(2021, 2050))
        )
        self.assertNoHolidayName(name, self.gov_hols, range(1867, 2021))

        dts = (
            "2023-10-02",
            "2028-10-02",
            "2029-10-01",
        )
        self.assertHolidayName(name_observed, self.gov_hols, dts)
        self.assertNoNonObservedHoliday(CA(observed=False, categories=GOVERNMENT), dts)

        start_years = {
            "AB": 2021,
            "BC": 2023,
            "NT": 2022,
            "NU": 2022,
            "PE": 2022,
            "YT": 2023,
        }
        for prov, holidays in self.prov_hols.items():
            if prov in {"BC", "NT", "NU", "PE", "YT"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-30" for year in range(start_years[prov], 2050))
                )
                self.assertNoHolidayName(name, holidays, range(1867, start_years[prov]))
            else:
                self.assertNoHolidayName(name, holidays)
            self.assertNoNonObservedHoliday(self.prov_hols_nonobs[prov], dts)

        self.assertHolidayName(
            name, self.prov_opt_hols["AB"], (f"{year}-09-30" for year in range(2021, 2050))
        )

    def test_thanksgiving_day(self):
        name = "Thanksgiving Day"
        self.assertNoHolidayName(name)
        self.assertHolidayName(name, self.gov_hols, range(1931, 2050))
        self.assertNoHolidayName(name, self.gov_hols, range(1867, 1931))

        dts = (
            "1931-10-12",
            "1935-10-25",
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
        self.assertHolidayName(name, self.gov_hols, dts)
        for prov, holidays in self.prov_hols.items():
            if prov in {"AB", "BC", "MB", "NT", "NU", "ON", "QC", "SK", "YT"}:
                self.assertHolidayName(name, holidays, dts)
                self.assertHolidayName(name, holidays, range(1931, 2050))
                self.assertNoHolidayName(name, holidays, range(1867, 1931))
            else:
                self.assertNoHolidayName(name, holidays, dts)

        for prov in ("NB", "NL"):
            self.assertHolidayName(name, self.prov_opt_hols[prov], dts)

    def test_remembrance_day(self):
        name = "Remembrance Day"
        name_observed = f"{name} (observed)"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.gov_hols, (f"{year}-11-11" for year in range(1931, 2050))
        )
        self.assertNoHoliday(self.gov_hols, (f"{year}-11-11" for year in range(1900, 1931)))
        self.assertNoHolidayName(name, self.gov_hols, range(1900, 1931))

        dts = (
            "2006-11-13",
            "2007-11-12",
            "2012-11-12",
            "2017-11-13",
            "2018-11-12",
            "2023-11-13",
        )
        self.assertHolidayName(name_observed, self.gov_hols, dts)
        self.assertNoNonObservedHoliday(CA(observed=False, categories=GOVERNMENT), dts)

        for prov, holidays in self.prov_hols.items():
            if prov in {"AB", "BC", "NB", "NL", "NS", "NT", "NU", "PE", "SK", "YT"}:
                start_year = 1981 if prov == "NS" else 1931
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-11" for year in range(start_year, 2050))
                )
                self.assertNoHoliday(
                    holidays, (f"{year}-11-11" for year in range(1900, start_year))
                )
                self.assertNoHolidayName(name, holidays, range(1900, start_year))
            else:
                self.assertNoHolidayName(name, holidays)

            if prov in {"AB", "NL", "NS", "PE", "SK", "YT"}:
                self.assertHolidayName(name_observed, holidays, dts)
                self.assertNoNonObservedHoliday(self.prov_hols_nonobs[prov], dts)
            else:
                self.assertNoHoliday(holidays, dts)

        self.assertHolidayName(
            name, self.prov_opt_hols["MB"], (f"{year}-11-11" for year in range(1931, 2050))
        )

    def test_boxing_day(self):
        name = "Boxing Day"
        name_observed = f"{name} (observed)"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.gov_hols, (f"{year}-12-26" for year in range(1867, 2050))
        )

        self.assertHolidayName(
            name, self.opt_hols, (f"{year}-12-26" for year in range(1867, 2050))
        )

        dts = (
            "2004-12-28",
            "2009-12-28",
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(name_observed, self.opt_hols, dts)
        self.assertNoNonObservedHoliday(CA(observed=False, categories=OPTIONAL), dts)

        dts = (
            "2004-12-28",
            "2010-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(name_observed, self.prov_hols["ON"], dts)
        self.assertNoNonObservedHoliday(self.prov_hols_nonobs["ON"], dts)

        for prov in ("AB", "NB", "NL"):
            self.assertHolidayName(
                name, self.prov_opt_hols[prov], (f"{year}-12-26" for year in range(1867, 2050))
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
        prov_names = {
            "MB": "Louis Riel Day",
            "NS": "Heritage Day",
            "PE": "Islander Day",
        }
        for prov, holidays in self.prov_hols.items():
            name = prov_names.get(prov, "Family Day")
            for year, dt in enumerate(dts, 1990):
                if prov in start_years and year >= start_years[prov]:
                    self.assertHolidayName(name, holidays, dt)
                else:
                    self.assertNoHoliday(holidays, dt)
        self.assertNoHoliday(dts)
        self.assertNoHolidayName("Family Day")
        for name in prov_names.values():
            self.assertNoHolidayName(name)

        self.assertHoliday(
            self.prov_hols["BC"],
            "2013-02-11",
            "2014-02-10",
            "2015-02-09",
            "2016-02-08",
            "2017-02-13",
            "2018-02-12",
        )
        self.assertHoliday(self.prov_hols["PE"], "2009-02-09")

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
        self.assertNoHoliday(self.gov_hols, dts)
        self.assertNoHolidayName(name, self.gov_hols)

        for prov, holidays in self.prov_hols.items():
            self.assertNoHoliday(holidays, dts)
            self.assertNoHolidayName(name, holidays)

            if prov in {"AB", "QC"}:
                self.assertHolidayName(name, self.prov_opt_hols[prov], dts)

    def test_civic_holiday_ab(self):
        name = "Heritage Day"
        self.assertNoHolidayName(name, self.prov_hols["AB"])
        ab_opt_holidays = self.prov_opt_hols["AB"]
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
        self.assertHoliday(ab_opt_holidays, dts)
        self.assertNoHoliday(ab_opt_holidays, "1973-08-06")

    def test_civic_holiday_bc(self):
        name = "British Columbia Day"
        bc_holidays = self.prov_hols["BC"]
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
        self.assertHolidayName(name, bc_holidays, dts)
        self.assertNoHoliday(bc_holidays, "1973-08-06")

    def test_civic_holiday_mb(self):
        old_name = "Civic Holiday"
        new_name = "Terry Fox Day"
        self.assertNoHolidayName(old_name, self.prov_hols["MB"])
        self.assertNoHolidayName(new_name, self.prov_hols["MB"])

        mb_opt_holidays = self.prov_opt_hols["MB"]
        dts = (
            "1900-08-06",
            "1999-08-02",
            "2000-08-07",
            "2010-08-02",
            "2015-08-03",
            "2020-08-03",
        )
        self.assertNoHoliday(dts)
        self.assertNoHolidayName(old_name)
        self.assertNoHolidayName(new_name)
        self.assertHoliday(mb_opt_holidays, dts)
        self.assertNoHoliday(mb_opt_holidays, "1899-08-07")
        self.assertHolidayName(old_name, mb_opt_holidays, "2014-08-04")
        self.assertHolidayName(new_name, mb_opt_holidays, "2015-08-03")
        self.assertNoHolidayName(old_name, mb_opt_holidays, 2015)
        self.assertNoHolidayName(new_name, mb_opt_holidays, 2014)

    def test_civic_holiday_nb(self):
        name = "New Brunswick Day"
        nb_holidays = self.prov_hols["NB"]
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
        self.assertHolidayName(name, nb_holidays, dts)
        self.assertNoHoliday(nb_holidays, "1974-08-05")
        self.assertNoHolidayName(name, nb_holidays, range(1867, 1975))

    def test_civic_holiday_ns(self):
        name = "Natal Day"
        self.assertNoHolidayName(name, self.prov_hols["NS"])
        ns_opt_holidays = self.prov_opt_hols["NS"]
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
        self.assertHoliday(ns_opt_holidays, dts)
        self.assertNoHoliday(ns_opt_holidays, "1995-08-07")

    def test_civic_holiday_nt_nu_on_sk(self):
        name = "Civic Holiday"
        nt_holidays = self.prov_hols["NT"]
        nu_holidays = self.prov_hols["NU"]
        on_opt_holidays = self.prov_opt_hols["ON"]
        sk_holidays = self.prov_hols["SK"]
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
        self.assertHolidayName(name, nt_holidays, dts)
        self.assertHolidayName(name, nu_holidays, dts)
        self.assertHolidayName(name, on_opt_holidays, dts)
        self.assertHolidayName("Saskatchewan Day", sk_holidays, dts)
        self.assertNoHoliday(nt_holidays, "1899-08-07")
        self.assertNoHoliday(nu_holidays, "1899-08-07")
        self.assertNoHoliday(on_opt_holidays, "1899-08-07")
        self.assertNoHoliday(sk_holidays, "1899-08-07")

    def test_memorial_day(self):
        name = "Memorial Day"
        self.assertNoHolidayName(name)
        nl_holidays = self.prov_hols["NL"]
        self.assertHolidayName(name, nl_holidays, (f"{year}-07-01" for year in range(1917, 2050)))
        self.assertNoHolidayName(name, nl_holidays, range(1900, 1917))

    def test_st_patricks_day(self):
        name = "Saint Patrick's Day"
        self.assertNoHolidayName(name, self.prov_hols["NL"])
        nl_opt_holidays = self.prov_opt_hols["NL"]
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
        self.assertHolidayName(name, nl_opt_holidays, dts)
        self.assertNoHoliday(nl_opt_holidays, "1899-03-20")

    def test_st_georges_day(self):
        name = "Saint George's Day"
        self.assertNoHolidayName(name, self.prov_hols["NL"])
        nl_opt_holidays = self.prov_opt_hols["NL"]
        dts = (
            "1990-04-23",
            "1999-04-26",
            "2010-04-19",
            "2016-04-25",
            "2020-04-20",
        )
        self.assertNoHoliday(dts)
        self.assertNoHolidayName(name)
        self.assertHolidayName(name, nl_opt_holidays, dts)
        self.assertNoHoliday(nl_opt_holidays, "1989-04-24")

    def test_discovery_day_nl(self):
        name = "Discovery Day"
        self.assertNoHolidayName(name, self.prov_hols["NL"])
        nl_opt_holidays = self.prov_opt_hols["NL"]
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
        self.assertHoliday(nl_opt_holidays, dts)
        self.assertNoHoliday(nl_opt_holidays, "1996-06-24")

    def test_orangemans_day(self):
        name = "Orangemen's Day"
        self.assertNoHolidayName(name, self.prov_hols["NL"])
        nl_opt_holidays = self.prov_opt_hols["NL"]
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
        self.assertHoliday(nl_opt_holidays, dts)
        self.assertNoHoliday(nl_opt_holidays, "1899-07-10")

    def test_discovery_day_yt(self):
        name = "Discovery Day"
        yt_holidays = self.prov_hols["YT"]
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
        self.assertHoliday(yt_holidays, dts)
        self.assertNoHoliday(yt_holidays, "1911-08-21")

    def test_national_aboriginal_day(self):
        name = "National Aboriginal Day"
        nt_holidays = self.prov_hols["NT"]
        yt_holidays = self.prov_hols["YT"]
        self.assertHolidayName(name, nt_holidays, (f"{year}-06-21" for year in range(1996, 2050)))
        self.assertNoHolidayName(nt_holidays, range(1867, 1996))
        self.assertHolidayName(name, yt_holidays, (f"{year}-06-21" for year in range(2017, 2050)))
        self.assertNoHolidayName(yt_holidays, range(1867, 2017))
        self.assertNoHoliday(f"{year}-06-21" for year in range(1996, 2050))
        self.assertNoHolidayName(name)

    def test_nunavut_day(self):
        name = "Nunavut Day"
        self.assertNoHolidayName(name)
        self.assertNoHoliday(f"{year}-07-09" for year in range(2001, 2050))
        self.assertNoHolidayName(name, self.prov_hols["NU"])
        nu_opt_holidays = self.prov_opt_hols["NU"]
        self.assertNoHoliday(nu_opt_holidays, "1999-07-09", "2000-07-09")
        self.assertHoliday(nu_opt_holidays, "2000-04-01")
        self.assertHoliday(nu_opt_holidays, (f"{year}-07-09" for year in range(2001, 2050)))

    def test_national_patriots_day(self):
        name = "National Patriots' Day"
        self.assertNoHolidayName(name)
        qc_holidays = self.prov_hols["QC"]
        self.assertHolidayName(
            name,
            qc_holidays,
            "2010-05-24",
            "2015-05-18",
            "2020-05-18",
            "2021-05-24",
            "2022-05-23",
        )
        self.assertNoHolidayName(name, qc_holidays, range(1867, 2003))

    def test_st_jean_baptiste_day(self):
        name = "Saint Jean Baptiste Day"
        self.assertNoHolidayName(name)
        qc_holidays = self.prov_hols["QC"]
        self.assertHoliday(qc_holidays, (f"{year}-06-24" for year in range(1925, 2050)))
        self.assertNoHoliday(qc_holidays, (f"{year}-06-24" for year in range(1867, 1925)))
        self.assertNoHoliday(f"{year}-06-24" for year in range(1925, 2050))
        self.assertHoliday(qc_holidays, "2001-06-25")
        self.assertNoNonObservedHoliday(self.prov_hols_nonobs["QC"], "2001-06-25")

    def test_yukon_heritage_day(self):
        name = "Heritage Day"
        self.assertNoHolidayName(name)
        self.assertNoHolidayName(name, self.prov_hols["YT"])
        dts = (
            "2017-02-24",
            "2018-02-23",
            "2019-02-22",
            "2020-02-21",
            "2021-02-26",
            "2022-02-25",
        )
        self.assertHolidayName(name, self.prov_opt_hols["YT"], dts)

    def test_queens_funeral(self):
        for prov, holidays in self.prov_hols.items():
            if prov in {"BC", "NB", "NL", "NS", "PE", "YT"}:
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
        for prov in Canada.subdivisions:
            y_2022.update(Canada(years=2022, subdiv=prov, observed=False).values())
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
            f"missing: {all_h - y_2022 if len(all_h - y_2022) > 0 else 'no'},"
            f" extra: {y_2022 - all_h if len(y_2022 - all_h) > 0 else 'no'}",
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
            ("2022-01-03", "(تمت ملاحظته) يوم السنة الجديدة"),
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
            ("2022-12-26", "(تمت ملاحظته) عيد الميلاد; يوم الملاكمة"),
            ("2022-12-27", "(تمت ملاحظته) عيد الميلاد"),
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
