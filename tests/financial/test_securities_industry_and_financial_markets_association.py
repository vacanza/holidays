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

from holidays.financial.securities_industry_and_financial_markets_association import (
    SecuritiesIndustryAndFinancialMarketsAssociation,
)
from tests.common import CommonFinancialTests


class TestSecuritiesIndustryAndFinancialMarketsAssociation(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SecuritiesIndustryAndFinancialMarketsAssociation)

    def test_new_years_day(self):
        name = "New Year's Day"
        name_observed = f"{name} (observed)"
        self.assertNonObservedHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        no_obs_dts = (
            "1999-12-31",
            "2004-12-31",
            "2010-12-31",
            "2021-12-31",
        )
        self.assertNoHolidayName(name_observed, no_obs_dts)
        self.assertNoHoliday(no_obs_dts)

    def test_martin_luther_king_jr_day(self):
        self.assertHolidayName(
            "Martin Luther King Jr. Day",
            "2020-01-20",
            "2021-01-18",
            "2022-01-17",
            "2023-01-16",
            "2024-01-15",
            "2025-01-20",
        )

    def test_washingtons_birthday(self):
        self.assertHolidayName(
            "Washington's Birthday",
            "2020-02-17",
            "2021-02-15",
            "2022-02-21",
            "2023-02-20",
            "2024-02-19",
            "2025-02-17",
        )

    def test_good_friday(self):
        name = "Good Friday"
        years_early_close = {1999, 2007, 2010, 2012, 2015, 2021, 2023, 2026}
        self.assertHolidayName(
            name,
            "1996-04-05",
            "2011-04-22",
            "2020-04-10",
            "2022-04-15",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(
            name, (year for year in self.full_range if year not in years_early_close)
        )
        self.assertNoHolidayName(name, years_early_close)

    def test_memorial_day(self):
        self.assertHolidayName(
            "Memorial Day",
            "2020-05-25",
            "2021-05-31",
            "2022-05-30",
            "2023-05-29",
            "2024-05-27",
            "2025-05-26",
        )

    def test_juneteenth_national_independence_day(self):
        name = "Juneteenth National Independence Day"
        self.assertHolidayName(
            name,
            "2023-06-19",
            "2024-06-19",
            "2025-06-19",
        )
        self.assertHolidayName(f"{name} (observed)", "2022-06-20", "2027-06-18")
        self.assertNonObservedHolidayName(
            name, (f"{year}-06-19" for year in range(2022, self.end_year))
        )
        self.assertNoHolidayName(name, range(self.start_year, 2022))

    def test_independence_day(self):
        name = "Independence Day"
        name_observed = f"{name} (observed)"
        self.assertNonObservedHolidayName(name, (f"{year}-07-04" for year in self.full_range))
        obs_dts = (
            "1998-07-03",
            "1999-07-05",
            "2004-07-05",
            "2009-07-03",
            "2010-07-05",
            "2015-07-03",
            "2020-07-03",
            "2021-07-05",
            "2026-07-03",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_labor_day(self):
        self.assertHolidayName(
            "Labor Day",
            "2020-09-07",
            "2021-09-06",
            "2022-09-05",
            "2023-09-04",
            "2024-09-02",
            "2025-09-01",
        )

    def test_columbus_day(self):
        self.assertHolidayName(
            "Columbus Day",
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
            "2024-10-14",
            "2025-10-13",
        )

    def test_veterans_day(self):
        name = "Veterans Day"
        name_observed = f"{name} (observed)"
        self.assertNonObservedHolidayName(name, (f"{year}-11-11" for year in self.full_range))
        obs_dts = (
            "2001-11-12",
            "2007-11-12",
            "2012-11-12",
            "2018-11-12",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        no_obs_dts = (
            "2000-11-10",
            "2006-11-10",
            "2017-11-10",
            "2023-11-10",
        )
        self.assertNoHolidayName(name_observed, no_obs_dts)
        self.assertNoHoliday(no_obs_dts)

    def test_thanksgiving_day(self):
        self.assertHolidayName(
            "Thanksgiving Day",
            "2020-11-26",
            "2021-11-25",
            "2022-11-24",
            "2023-11-23",
            "2024-11-28",
            "2025-11-27",
        )

    def test_christmas_day(self):
        name = "Christmas Day"
        name_observed = f"{name} (observed)"
        self.assertNonObservedHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "1999-12-24",
            "2004-12-24",
            "2005-12-26",
            "2010-12-24",
            "2011-12-26",
            "2016-12-26",
            "2021-12-24",
            "2022-12-26",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_special_public_holidays(self):
        self.assertHoliday(
            "2012-10-30",
            "2018-12-05",
        )

    def test_day_before_martin_luther_king_jr_day(self):
        name = "Day before Martin Luther King Jr. Day (markets close at 2:00pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "1996-01-12",
            "2000-01-14",
            "2005-01-14",
            "2009-01-16",
        )
        self.assertHalfDayHolidayName(name, range(self.start_year, 2010))
        self.assertNoHalfDayHolidayName(name, range(2010, self.end_year))

    def test_day_before_washingtons_birthday(self):
        name = "Day before Washington's Birthday (markets close at 2:00pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "1996-02-16",
            "2000-02-18",
            "2005-02-18",
            "2009-02-13",
        )
        self.assertHalfDayHolidayName(name, range(self.start_year, 2010))
        self.assertNoHalfDayHolidayName(name, range(2010, self.end_year))

    def test_day_before_good_friday(self):
        name = "Day before Good Friday (markets close at 2:00pm)"
        years_absent = {1996, 2007, 2010, 2012, 2015, 2021, 2023, 2026}
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "1997-03-27",
            "1999-04-01",
            "2011-04-21",
            "2020-04-09",
            "2024-03-28",
            "2025-04-17",
        )
        self.assertHalfDayHolidayName(
            name, (year for year in self.full_range if year not in years_absent)
        )
        self.assertNoHalfDayHolidayName(name, years_absent)

    def test_day_before_memorial_day(self):
        name = "Day before Memorial Day (markets close at 2:00pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "2020-05-22",
            "2021-05-28",
            "2022-05-27",
            "2023-05-26",
            "2024-05-24",
            "2025-05-23",
        )
        self.assertHalfDayHolidayName(name, self.full_range)

    def test_day_before_independence_day(self):
        name = "Day before Independence Day (markets close at 2:00pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "1996-07-03",
            "1998-07-02",
            "1999-07-02",
            "2004-07-02",
            "2008-07-03",
            "2014-07-03",
            "2015-07-02",
            "2016-07-01",
            "2020-07-02",
            "2021-07-02",
            "2025-07-03",
        )
        self.assertHalfDayHolidayName(
            name, range(self.start_year, 2009), range(2014, self.end_year)
        )
        self.assertNoHalfDayHolidayName(name, range(2009, 2014))

    def test_day_before_labor_day(self):
        name = "Day before Labor Day (markets close at 2:00pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "1996-08-30",
            "2001-08-31",
            "2008-08-29",
        )
        self.assertHalfDayHolidayName(name, range(self.start_year, 2009))
        self.assertNoHalfDayHolidayName(name, range(2009, self.end_year))

    def test_day_before_columbus_day(self):
        name = "Day before Columbus Day (markets close at 2:00pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "1996-10-11",
            "2001-10-05",
            "2008-10-10",
        )
        self.assertHalfDayHolidayName(name, range(self.start_year, 2009))
        self.assertNoHalfDayHolidayName(name, range(2009, self.end_year))

    def test_day_before_veterans_day(self):
        name = "Day before Veterans Day (markets close at 2:00pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "1996-11-08",
            "2001-11-09",
            "2002-11-08",
            "2003-11-10",
            "2005-11-10",
            "2007-11-09",
            "2008-11-10",
        )
        self.assertNoHalfDayHolidayName(
            name, 1997, 1998, 1999, 2000, 2004, 2006, range(2009, self.end_year)
        )

    def test_day_before_thanksgiving_day(self):
        name = "Day before Thanksgiving Day (markets close at 2:00pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "1996-11-27",
            "2001-11-21",
            "2008-11-26",
        )
        self.assertHalfDayHolidayName(name, range(self.start_year, 2009))
        self.assertNoHalfDayHolidayName(name, range(2009, self.end_year))

    def test_day_after_thanksgiving_day(self):
        name = "Day after Thanksgiving Day (markets close at 2:00pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "2020-11-27",
            "2021-11-26",
            "2022-11-25",
            "2023-11-24",
            "2024-11-29",
            "2025-11-28",
        )
        self.assertHalfDayHolidayName(name, self.full_range)

    def test_day_before_christmas_day(self):
        name = "Day before Christmas Day (markets close at 2:00pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "1999-12-23",
            "2004-12-23",
            "2005-12-23",
            "2006-12-22",
            "2017-12-22",
            "2021-12-23",
            "2022-12-23",
            "2023-12-22",
            "2024-12-24",
            "2025-12-24",
        )
        self.assertHalfDayHolidayName(name, self.full_range)

    def test_day_before_new_years_day(self):
        name = "Day before New Year's Day (markets close at 2:00pm)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "2000-12-29",
            "2004-12-31",
            "2005-12-30",
            "2016-12-30",
            "2021-12-31",
            "2023-12-29",
            "2024-12-31",
            "2025-12-31",
        )
        self.assertNoHalfDayHolidayName(name, 1999, 2010)

    def test_special_half_day_holidays(self):
        self.assertHalfDayHoliday(
            "1996-07-05",
            "1997-12-26",
            "1999-04-02",
            "1999-12-31",
            "2004-01-02",
            "2007-01-02",
            "2007-04-06",
            "2010-04-02",
            "2012-04-06",
            "2012-10-29",
            "2015-04-03",
            "2021-04-02",
            "2023-04-07",
            "2025-01-09",
            "2026-04-03",
        )

    def test_2012(self):
        self.assertHolidaysInYear(
            2012,
            ("2012-01-02", "New Year's Day (observed)"),
            ("2012-01-16", "Martin Luther King Jr. Day"),
            ("2012-02-20", "Washington's Birthday"),
            ("2012-05-28", "Memorial Day"),
            ("2012-07-04", "Independence Day"),
            ("2012-09-03", "Labor Day"),
            ("2012-10-08", "Columbus Day"),
            ("2012-10-30", "Hurricane Sandy"),
            ("2012-11-12", "Veterans Day (observed)"),
            ("2012-11-22", "Thanksgiving Day"),
            ("2012-12-25", "Christmas Day"),
        )

    def test_half_day_2012(self):
        self.assertHalfDayHolidaysInYear(
            2012,
            ("2012-04-06", "Good Friday (markets close at 12:00pm)"),
            ("2012-05-25", "Day before Memorial Day (markets close at 2:00pm)"),
            ("2012-10-29", "Hurricane Sandy (markets close at 12:00pm)"),
            ("2012-11-23", "Day after Thanksgiving Day (markets close at 2:00pm)"),
            ("2012-12-24", "Day before Christmas Day (markets close at 2:00pm)"),
            ("2012-12-31", "Day before New Year's Day (markets close at 2:00pm)"),
        )

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "New Year's Day"),
            ("2025-01-20", "Martin Luther King Jr. Day"),
            ("2025-02-17", "Washington's Birthday"),
            ("2025-04-18", "Good Friday"),
            ("2025-05-26", "Memorial Day"),
            ("2025-06-19", "Juneteenth National Independence Day"),
            ("2025-07-04", "Independence Day"),
            ("2025-09-01", "Labor Day"),
            ("2025-10-13", "Columbus Day"),
            ("2025-11-11", "Veterans Day"),
            ("2025-11-27", "Thanksgiving Day"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_half_day_2025(self):
        self.assertHalfDayHolidaysInYear(
            2025,
            (
                "2025-01-09",
                "National Day of Mourning for former President Jimmy Carter "
                "(markets close at 2:00pm)",
            ),
            ("2025-04-17", "Day before Good Friday (markets close at 2:00pm)"),
            ("2025-05-23", "Day before Memorial Day (markets close at 2:00pm)"),
            ("2025-07-03", "Day before Independence Day (markets close at 2:00pm)"),
            ("2025-11-28", "Day after Thanksgiving Day (markets close at 2:00pm)"),
            ("2025-12-24", "Day before Christmas Day (markets close at 2:00pm)"),
            ("2025-12-31", "Day before New Year's Day (markets close at 2:00pm)"),
        )

    def test_half_day_2026(self):
        self.assertHalfDayHolidaysInYear(
            2026,
            ("2026-04-03", "Good Friday (markets close at 12:00pm)"),
            ("2026-05-22", "Day before Memorial Day (markets close at 2:00pm)"),
            ("2026-07-02", "Day before Independence Day (markets close at 2:00pm)"),
            ("2026-11-27", "Day after Thanksgiving Day (markets close at 2:00pm)"),
            ("2026-12-24", "Day before Christmas Day (markets close at 2:00pm)"),
            ("2026-12-31", "Day before New Year's Day (markets close at 2:00pm)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-01-15", "Martin Luther King Jr. Day"),
            ("2024-02-19", "Washington's Birthday"),
            ("2024-03-28", "Day before Good Friday (markets close at 2:00pm)"),
            ("2024-03-29", "Good Friday"),
            ("2024-05-24", "Day before Memorial Day (markets close at 2:00pm)"),
            ("2024-05-27", "Memorial Day"),
            ("2024-06-19", "Juneteenth National Independence Day"),
            ("2024-07-03", "Day before Independence Day (markets close at 2:00pm)"),
            ("2024-07-04", "Independence Day"),
            ("2024-09-02", "Labor Day"),
            ("2024-10-14", "Columbus Day"),
            ("2024-11-11", "Veterans Day"),
            ("2024-11-28", "Thanksgiving Day"),
            ("2024-11-29", "Day after Thanksgiving Day (markets close at 2:00pm)"),
            ("2024-12-24", "Day before Christmas Day (markets close at 2:00pm)"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-31", "Day before New Year's Day (markets close at 2:00pm)"),
        )
