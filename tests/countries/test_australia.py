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

from holidays.countries.australia import Australia
from tests.common import CommonCountryTests


class TestAustralia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Australia, with_subdiv_categories=True)

    # All subdivisions holidays.

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in self.full_range))

    def test_new_years_day_act(self):
        name = "New Year's Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivActNonObservedHolidayName(
            name, (f"{year}-01-01" for year in range(self.start_year, 1959))
        )
        self.assertSubdivActNonObservedHolidayName(name, range(1959, self.end_year))

        dts = (
            "1994-01-01",
            "1995-01-01",
            "2000-01-01",
            "2005-01-01",
            "2006-01-01",
            "2011-01-01",
            "2012-01-01",
        )
        self.assertSubdivActNonObservedHolidayName(name, dts)
        self.assertNoSubdivActHoliday(dts)

        mov_dts = (
            "1994-01-03",
            "1995-01-02",
            "2000-01-03",
            "2005-01-03",
            "2006-01-02",
            "2011-01-03",
            "2012-01-02",
        )
        self.assertSubdivActHolidayName(name, mov_dts)
        self.assertNoSubdivActNonObservedHoliday(mov_dts)

        obs_dts = (
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertSubdivActHolidayName(name_observed, obs_dts)
        self.assertNoSubdivActNonObservedHoliday(obs_dts)
        self.assertNoSubdivActHolidayName(name_observed, range(self.start_year, 2015))

    def test_new_years_day_nsw(self):
        name = "New Year's Day"
        self.assertSubdivNswHolidayName(name, (f"{year}-01-01" for year in self.full_range))

        obs_dts = (
            "2006-01-02",
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertSubdivNswHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoSubdivNswNonObservedHoliday(obs_dts)

    def test_new_years_day_nt(self):
        name = "New Year's Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivNtNonObservedHolidayName(
            name, (f"{year}-01-01" for year in range(self.start_year, 1982))
        )
        self.assertSubdivNtNonObservedHolidayName(name, range(1982, self.end_year))

        dts = (
            "1994-01-01",
            "1995-01-01",
            "2000-01-01",
            "2005-01-01",
            "2006-01-01",
            "2011-01-01",
            "2012-01-01",
        )
        self.assertSubdivNtNonObservedHolidayName(name, dts)
        self.assertNoSubdivNtHoliday(dts)

        mov_dts = (
            "1994-01-03",
            "1995-01-02",
            "2000-01-03",
            "2005-01-03",
            "2006-01-02",
            "2011-01-03",
            "2012-01-02",
        )
        self.assertSubdivNtHolidayName(name, mov_dts)
        self.assertNoSubdivNtNonObservedHoliday(mov_dts)

        obs_dts = (
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertSubdivNtHolidayName(name_observed, obs_dts)
        self.assertNoSubdivNtNonObservedHoliday(obs_dts)
        self.assertNoSubdivNtHolidayName(name_observed, range(self.start_year, 2017))

    def test_new_years_day_qld(self):
        name = "New Year's Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivQldNonObservedHolidayName(
            name, (f"{year}-01-01" for year in range(self.start_year, 1984))
        )
        self.assertSubdivQldNonObservedHolidayName(name, range(1984, self.end_year))

        dts = (
            "1984-01-01",
            "1989-01-01",
            "1995-01-01",
            "2006-01-01",
        )
        self.assertSubdivQldNonObservedHolidayName(name, dts)
        self.assertNoSubdivQldHoliday(dts)

        mov_dts = (
            "1984-01-02",
            "1989-01-02",
            "1995-01-02",
            "2006-01-02",
        )
        self.assertSubdivQldHolidayName(name, mov_dts)
        self.assertNoSubdivQldNonObservedHoliday(mov_dts)

        obs_dts = (
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertSubdivQldHolidayName(name_observed, obs_dts)
        self.assertNoSubdivQldNonObservedHoliday(obs_dts)
        self.assertNoSubdivQldHolidayName(name_observed, range(self.start_year, 2011))

    def test_new_years_day_sa(self):
        name = "New Year's Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivSaNonObservedHolidayName(
            name, (f"{year}-01-01" for year in range(self.start_year, 1984))
        )
        self.assertSubdivSaNonObservedHolidayName(name, range(1984, self.end_year))

        dts = (
            "1984-01-01",
            "1989-01-01",
            "1994-01-01",
            "1995-01-01",
            "2000-01-01",
            "2005-01-01",
            "2011-01-01",
            "2022-01-01",
        )
        self.assertSubdivSaNonObservedHolidayName(name, dts)
        self.assertNoSubdivSaHoliday(dts)

        mov_dts = (
            "1984-01-02",
            "1989-01-02",
            "1994-01-03",
            "1995-01-02",
            "2000-01-03",
            "2005-01-03",
            "2011-01-03",
            "2022-01-03",
        )
        self.assertSubdivSaHolidayName(name, mov_dts)
        self.assertNoSubdivSaNonObservedHoliday(mov_dts)

        obs_dts = (
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertSubdivSaHolidayName(name_observed, obs_dts)
        self.assertNoSubdivSaNonObservedHoliday(obs_dts)
        self.assertNoSubdivSaHolidayName(name_observed, range(self.start_year, 2004))

    def test_new_years_day_tas(self):
        name = "New Year's Day"
        self.assertSubdivTasNonObservedHolidayName(
            name, (f"{year}-01-01" for year in range(self.start_year, 2001))
        )
        self.assertSubdivTasNonObservedHolidayName(name, range(2001, self.end_year))

        dts = (
            "2005-01-01",
            "2006-01-01",
            "2011-01-01",
            "2012-01-01",
            "2017-01-01",
            "2022-01-01",
            "2023-01-01",
        )
        self.assertSubdivTasNonObservedHolidayName(name, dts)
        self.assertNoSubdivTasHoliday(dts)

        mov_dts = (
            "2005-01-03",
            "2006-01-02",
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertSubdivTasHolidayName(name, mov_dts)
        self.assertNoSubdivTasNonObservedHoliday(mov_dts)
        self.assertNoSubdivTasHolidayName(f"{name} (observed)")

    def test_new_years_day_vic(self):
        name = "New Year's Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivVicNonObservedHolidayName(
            name, (f"{year}-01-01" for year in range(1998, 2009))
        )
        self.assertSubdivVicNonObservedHolidayName(
            name, range(self.start_year, 1998), range(2009, self.end_year)
        )

        dts = ("2006-01-01",)
        self.assertSubdivVicNonObservedHolidayName(name, dts)
        self.assertNoSubdivVicHoliday(dts)

        mov_dts = ("2006-01-02",)
        self.assertSubdivVicHolidayName(name, mov_dts)
        self.assertNoSubdivVicNonObservedHoliday(mov_dts)

        obs_dts = (
            "1995-01-02",
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertSubdivVicHolidayName(name_observed, obs_dts)
        self.assertNoSubdivVicNonObservedHoliday(obs_dts)
        self.assertNoSubdivVicHolidayName(
            name_observed, range(self.start_year, 1994), range(1998, 2009)
        )

    def test_new_years_day_wa(self):
        name = "New Year's Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivWaHolidayName(name, (f"{year}-01-01" for year in self.full_range))

        obs_dts = (
            "2006-01-02",
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertSubdivWaHolidayName(name_observed, obs_dts)
        self.assertNoSubdivWaNonObservedHoliday(obs_dts)
        self.assertNoSubdivWaHolidayName(name_observed, range(self.start_year, 1973))

    def test_australia_day(self):
        name = "Australia Day"
        self.assertHolidayName(name, (f"{year}-01-26" for year in range(1935, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1935))

    def test_australia_day_act(self):
        name_1888 = "Anniversary Day"
        name_1935 = "Australia Day"
        self.assertSubdivActHolidayName(name_1888, (f"{year}-01-26" for year in range(1888, 1935)))
        self.assertSubdivActHolidayName(name_1935, (f"{year}-01-26" for year in range(1935, 1959)))
        self.assertSubdivActHolidayName(name_1935, range(1959, self.end_year))
        self.assertNoSubdivActHolidayName(
            name_1888, range(self.start_year, 1888), range(1935, self.end_year)
        )
        self.assertNoSubdivActHolidayName(name_1935, range(self.start_year, 1935))

        dts = (
            "1985-01-26",
            "1986-01-26",
            "1988-01-26",
            "1989-01-26",
            "2013-01-26",
            "2014-01-26",
            "2019-01-26",
            "2020-01-26",
            "2025-01-26",
        )
        self.assertSubdivActNonObservedHolidayName(name_1935, dts)
        self.assertNoSubdivActHoliday(dts)

        mov_dts = (
            "1985-01-28",
            "1986-01-27",
            "1988-02-01",
            "1989-01-30",
            "2013-01-28",
            "2014-01-27",
            "2019-01-28",
            "2020-01-27",
            "2025-01-27",
        )
        self.assertSubdivActHolidayName(name_1935, mov_dts)
        self.assertNoSubdivActNonObservedHoliday(mov_dts)

    def test_australia_day_nsw(self):
        name_1888 = "Anniversary Day"
        name_1946 = "Australia Day"
        name_observed = f"{name_1946} (observed)"
        self.assertSubdivNswHolidayName(name_1888, (f"{year}-01-26" for year in range(1888, 1946)))
        self.assertSubdivNswHolidayName(name_1946, (f"{year}-01-26" for year in range(1946, 2011)))
        self.assertSubdivNswHolidayName(name_1946, range(2011, self.end_year))
        self.assertNoSubdivNswHolidayName(
            name_1888, range(self.start_year, 1888), range(1946, self.end_year)
        )
        self.assertNoSubdivNswHolidayName(name_1946, range(self.start_year, 1946))

        dts = (
            "2013-01-26",
            "2014-01-26",
            "2019-01-26",
            "2020-01-26",
            "2025-01-26",
        )
        self.assertSubdivNswNonObservedHolidayName(name_1946, dts)
        self.assertNoSubdivNswHoliday(dts)

        mov_dts = (
            "2013-01-28",
            "2014-01-27",
            "2019-01-28",
            "2020-01-27",
            "2025-01-27",
        )
        self.assertSubdivNswHolidayName(name_1946, mov_dts)
        self.assertNoSubdivNswNonObservedHoliday(mov_dts)

        obs_dts = (
            "1958-01-27",
            "1964-01-27",
            "1969-01-27",
            "1975-01-27",
            "1986-01-27",
            "1992-01-27",
            "1997-01-27",
            "2003-01-27",
        )
        self.assertSubdivNswHolidayName(name_observed, obs_dts)
        self.assertNoSubdivNswNonObservedHoliday(obs_dts)
        self.assertNoSubdivNswHolidayName(name_observed, range(2011, self.end_year))

    def test_australia_day_nt(self):
        name_1888 = "Anniversary Day"
        name_1935 = "Australia Day"
        self.assertSubdivNtHolidayName(name_1888, (f"{year}-01-26" for year in range(1888, 1935)))
        self.assertSubdivNtHolidayName(name_1935, (f"{year}-01-26" for year in range(1935, 1982)))
        self.assertSubdivNtHolidayName(name_1935, range(1982, self.end_year))
        self.assertNoSubdivNtHolidayName(
            name_1888, range(self.start_year, 1888), range(1935, self.end_year)
        )
        self.assertNoSubdivNtHolidayName(name_1935, range(self.start_year, 1935))

        dts = (
            "1985-01-26",
            "1986-01-26",
            "1991-01-26",
            "1992-01-26",
            "1997-01-26",
            "2002-01-26",
            "2003-01-26",
            "2008-01-26",
            "2013-01-26",
            "2014-01-26",
            "2019-01-26",
            "2020-01-26",
            "2025-01-26",
        )
        self.assertSubdivNtNonObservedHolidayName(name_1935, dts)
        self.assertNoSubdivNtHoliday(dts)

        mov_dts = (
            "1985-01-28",
            "1986-01-27",
            "1991-01-28",
            "1992-01-27",
            "1997-01-27",
            "2002-01-28",
            "2003-01-27",
            "2008-01-28",
            "2013-01-28",
            "2014-01-27",
            "2019-01-28",
            "2020-01-27",
            "2025-01-27",
        )
        self.assertSubdivNtHolidayName(name_1935, mov_dts)
        self.assertNoSubdivNtNonObservedHoliday(mov_dts)

    def test_australia_day_qld(self):
        name_1888 = "Anniversary Day"
        name_1935 = "Australia Day"
        self.assertSubdivQldHolidayName(name_1888, (f"{year}-01-26" for year in range(1888, 1935)))
        self.assertSubdivQldHolidayName(name_1935, (f"{year}-01-26" for year in range(1935, 1984)))
        self.assertSubdivQldHolidayName(name_1935, range(1984, self.end_year))
        self.assertNoSubdivQldHolidayName(
            name_1888, range(self.start_year, 1888), range(1935, self.end_year)
        )
        self.assertNoSubdivQldHolidayName(name_1935, range(self.start_year, 1935))

        dts = (
            "1984-01-26",
            "1985-01-26",
            "1986-01-26",
            "1988-01-26",
            "1989-01-26",
            "2013-01-26",
            "2014-01-26",
            "2019-01-26",
            "2020-01-26",
            "2025-01-26",
        )
        self.assertSubdivQldNonObservedHolidayName(name_1935, dts)
        self.assertNoSubdivQldHoliday(dts)

        mov_dts = (
            "1984-01-30",
            "1985-01-28",
            "1986-01-27",
            "1988-02-01",
            "1989-01-30",
            "2013-01-28",
            "2014-01-27",
            "2019-01-28",
            "2020-01-27",
            "2025-01-27",
        )
        self.assertSubdivQldHolidayName(name_1935, mov_dts)
        self.assertNoSubdivQldNonObservedHoliday(mov_dts)

    def test_australia_day_sa(self):
        name = "Australia Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivSaHolidayName(name, (f"{year}-01-26" for year in range(1935, 1984)))
        self.assertSubdivSaHolidayName(name, range(1984, self.end_year))
        self.assertNoSubdivSaHolidayName(name, range(self.start_year, 1935))

        dts = (
            "1984-01-26",
            "1985-01-26",
            "1986-01-26",
            "1988-01-26",
            "1989-01-26",
            "2003-01-26",
            "2008-01-26",
            "2013-01-26",
            "2019-01-26",
            "2025-01-26",
        )
        self.assertSubdivSaNonObservedHolidayName(name, dts)
        self.assertNoSubdivSaHoliday(dts)

        mov_dts = (
            "1984-01-30",
            "1985-01-28",
            "1986-01-27",
            "1988-02-01",
            "1989-01-30",
            "2003-01-27",
            "2008-01-28",
            "2013-01-28",
            "2019-01-28",
            "2025-01-27",
        )
        self.assertSubdivSaHolidayName(name, mov_dts)
        self.assertNoSubdivSaNonObservedHoliday(mov_dts)

        obs_dts = (
            "2014-01-27",
            "2020-01-27",
        )
        self.assertSubdivSaHolidayName(name_observed, obs_dts)
        self.assertNoSubdivSaNonObservedHoliday(obs_dts)
        self.assertNoSubdivSaHolidayName(
            name_observed, range(self.start_year, 2004), range(2024, self.end_year)
        )

    def test_australia_day_tas(self):
        name_1888 = "Anniversary Day"
        name_1935 = "Australia Day"
        self.assertSubdivTasHolidayName(name_1888, (f"{year}-01-26" for year in range(1888, 1935)))
        self.assertSubdivTasHolidayName(name_1935, (f"{year}-01-26" for year in range(1935, 2001)))
        self.assertSubdivTasHolidayName(name_1935, range(2001, self.end_year))
        self.assertNoSubdivTasHolidayName(
            name_1888, range(self.start_year, 1888), range(1935, self.end_year)
        )
        self.assertNoSubdivTasHolidayName(name_1935, range(self.start_year, 1935))

        dts = (
            "2002-01-26",
            "2003-01-26",
            "2008-01-26",
            "2013-01-26",
            "2014-01-26",
            "2019-01-26",
            "2020-01-26",
            "2025-01-26",
        )
        self.assertSubdivTasNonObservedHolidayName(name_1935, dts)
        self.assertNoSubdivTasHoliday(dts)

        mov_dts = (
            "2002-01-28",
            "2003-01-27",
            "2008-01-28",
            "2013-01-28",
            "2014-01-27",
            "2019-01-28",
            "2020-01-27",
            "2025-01-27",
        )
        self.assertSubdivTasHolidayName(name_1935, mov_dts)
        self.assertNoSubdivTasNonObservedHoliday(mov_dts)

    def test_australia_day_vic(self):
        name_1888 = "Anniversary Day"
        name_1935 = "Australia Day"
        self.assertSubdivVicHolidayName(name_1888, (f"{year}-01-26" for year in range(1888, 1935)))
        self.assertSubdivVicHolidayName(name_1935, (f"{year}-01-26" for year in range(1935, 2009)))
        self.assertSubdivVicHolidayName(name_1935, range(2009, self.end_year))
        self.assertNoSubdivVicHolidayName(
            name_1888, range(self.start_year, 1888), range(1935, self.end_year)
        )
        self.assertNoSubdivVicHolidayName(name_1935, range(self.start_year, 1935))

        dts = (
            "2013-01-26",
            "2014-01-26",
            "2019-01-26",
            "2020-01-26",
            "2025-01-26",
        )
        self.assertSubdivVicNonObservedHolidayName(name_1935, dts)
        self.assertNoSubdivVicHoliday(dts)

        mov_dts = (
            "2013-01-28",
            "2014-01-27",
            "2019-01-28",
            "2020-01-27",
            "2025-01-27",
        )

        self.assertSubdivVicHolidayName(name_1935, mov_dts)
        self.assertNoSubdivVicNonObservedHoliday(mov_dts)

    def test_australia_day_wa(self):
        name_1888 = "Anniversary Day"
        name_1935 = "Australia Day"
        self.assertSubdivWaHolidayName(name_1888, (f"{year}-01-26" for year in range(1888, 1935)))
        self.assertSubdivWaHolidayName(name_1935, (f"{year}-01-26" for year in range(1935, 1973)))
        self.assertSubdivWaHolidayName(name_1935, range(1973, self.end_year))
        self.assertNoSubdivWaHolidayName(
            name_1888, range(self.start_year, 1888), range(1935, self.end_year)
        )
        self.assertNoSubdivWaHolidayName(name_1935, range(self.start_year, 1935))

        dts = (
            "1973-01-26",
            "1974-01-26",
            "1975-01-26",
            "1977-01-26",
            "1978-01-26",
            "2013-01-26",
            "2014-01-26",
            "2019-01-26",
            "2020-01-26",
            "2025-01-26",
        )
        self.assertSubdivWaNonObservedHolidayName(name_1935, dts)
        self.assertNoSubdivWaHoliday(dts)

        mov_dts = (
            "1973-01-29",
            "1974-01-28",
            "1975-01-27",
            "1977-01-31",
            "1978-01-30",
            "2013-01-28",
            "2014-01-27",
            "2019-01-28",
            "2020-01-27",
            "2025-01-27",
        )
        self.assertSubdivWaHolidayName(name_1935, mov_dts)
        self.assertNoSubdivWaNonObservedHoliday(mov_dts)

    def test_good_friday(self):
        name = "Good Friday"
        dts = (
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.full_range)
        for holidays in self.subdiv_holidays.values():
            self.assertHolidayName(name, holidays, dts)
            self.assertHolidayName(name, holidays, self.full_range)

    def test_easter_saturday(self):
        name = "Easter Saturday"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            match subdiv:
                case "VIC":
                    self.assertHolidayName(name, holidays, range(2003, self.end_year))
                    self.assertNoHolidayName(name, holidays, range(self.start_year, 2003))
                case "TAS" | "WA":
                    self.assertNoHolidayName(name, holidays)
                case _:
                    self.assertHolidayName(name, holidays, self.full_range)

    def test_easter_sunday(self):
        name = "Easter Sunday"
        self.assertNoHolidayName(name)

        subdiv_start_years = {
            "ACT": 2016,
            "NSW": 2011,
            "NT": 2024,
            "QLD": 2017,
            "SA": 2024,
            "VIC": 2016,
            "WA": 2022,
        }
        for subdiv, holidays in self.subdiv_holidays.items():
            if start_year := subdiv_start_years.get(subdiv):
                self.assertHolidayName(name, holidays, range(start_year, self.end_year))
                self.assertNoHolidayName(name, holidays, range(self.start_year, start_year))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_easter_monday(self):
        name = "Easter Monday"
        dts = (
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, dts)
        self.assertHolidayName(name, self.full_range)
        for holidays in self.subdiv_holidays.values():
            self.assertHolidayName(name, holidays, dts)
            self.assertHolidayName(name, holidays, self.full_range)

    def test_anzac_day(self):
        name = "ANZAC Day"
        self.assertHolidayName(name, (f"{year}-04-25" for year in range(1921, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1921))

    def test_anzac_day_act(self):
        name = "ANZAC Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivActHolidayName(name, (f"{year}-04-25" for year in range(1921, 1959)))
        self.assertSubdivActHolidayName(name, range(1959, self.end_year))
        self.assertNoSubdivActHolidayName(name, range(self.start_year, 1921))

        dts = (
            "1965-04-25",
            "1971-04-25",
            "1976-04-25",
            "1982-04-25",
            "1993-04-25",
            "1999-04-25",
            "2004-04-25",
            "2010-04-25",
        )
        self.assertSubdivActNonObservedHolidayName(name, dts)
        self.assertNoSubdivActHoliday(dts)

        mov_dts = (
            "1965-04-26",
            "1971-04-26",
            "1976-04-26",
            "1982-04-26",
            "1993-04-26",
            "1999-04-26",
            "2004-04-26",
            "2010-04-26",
            "2021-04-26",
        )
        self.assertSubdivActHolidayName(name, mov_dts)
        self.assertNoSubdivActNonObservedHoliday(mov_dts)

        obs_dts = ("2026-04-27",)
        self.assertSubdivActHolidayName(name_observed, obs_dts)
        self.assertNoSubdivActNonObservedHoliday(obs_dts)
        self.assertNoSubdivActHolidayName(
            name_observed, range(self.start_year, 2026), range(2027, self.end_year)
        )

    def test_anzac_day_nsw(self):
        name = "ANZAC Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivNswHolidayName(
            name, (f"{year}-04-25" for year in range(1921, self.end_year))
        )
        self.assertNoSubdivNswHolidayName(name, range(self.start_year, 1921))

        obs_dts = (
            "1993-04-26",
            "1999-04-26",
            "2004-04-26",
            "2010-04-26",
            "2026-04-27",
            "2027-04-26",
        )
        self.assertSubdivNswHolidayName(name_observed, obs_dts)
        self.assertNoSubdivNswNonObservedHoliday(obs_dts)
        self.assertNoSubdivNswHolidayName(
            name_observed, range(2011, 2026), range(2028, self.end_year)
        )

    def test_anzac_day_nt(self):
        name = "ANZAC Day"
        self.assertSubdivNtHolidayName(name, (f"{year}-04-25" for year in range(1921, 1982)))
        self.assertSubdivNtHolidayName(name, range(1982, self.end_year))
        self.assertNoSubdivNtHolidayName(name, range(self.start_year, 1921))

        dts = (
            "1982-04-25",
            "1993-04-25",
            "1999-04-25",
            "2004-04-25",
            "2010-04-25",
            "2021-04-25",
        )
        self.assertSubdivNtNonObservedHolidayName(name, dts)
        self.assertNoSubdivNtHoliday(dts)

        mov_dts = (
            "1982-04-26",
            "1993-04-26",
            "1999-04-26",
            "2004-04-26",
            "2010-04-26",
            "2021-04-26",
        )
        self.assertSubdivNtHolidayName(name, mov_dts)
        self.assertNoSubdivNtNonObservedHoliday(mov_dts)

    def test_anzac_day_qld(self):
        name = "ANZAC Day"
        self.assertSubdivQldHolidayName(name, (f"{year}-04-25" for year in range(1921, 1984)))
        self.assertSubdivQldHolidayName(name, range(1984, self.end_year))
        self.assertNoSubdivQldHolidayName(name, range(self.start_year, 1921))

        dts = (
            "1993-04-25",
            "1999-04-25",
            "2004-04-25",
            "2010-04-25",
            "2021-04-25",
        )
        self.assertSubdivQldNonObservedHolidayName(name, dts)
        self.assertNoSubdivQldHoliday(dts)

        mov_dts = (
            "1993-04-26",
            "1999-04-26",
            "2004-04-26",
            "2010-04-26",
            "2021-04-26",
        )
        self.assertSubdivQldHolidayName(name, mov_dts)
        self.assertNoSubdivQldNonObservedHoliday(mov_dts)

    def test_anzac_day_sa(self):
        name = "ANZAC Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivSaHolidayName(
            name, (f"{year}-04-25" for year in range(1921, self.end_year))
        )
        self.assertNoSubdivSaHolidayName(name, range(self.start_year, 1921))

        obs_dts = (
            "1993-04-26",
            "1999-04-26",
            "2004-04-26",
            "2010-04-26",
            "2021-04-26",
        )
        self.assertSubdivSaHolidayName(name_observed, obs_dts)
        self.assertNoSubdivSaNonObservedHoliday(obs_dts)
        self.assertNoSubdivSaHolidayName(name_observed, range(2023, self.end_year))

    def test_anzac_day_tas(self):
        name = "ANZAC Day"
        self.assertSubdivTasHolidayName(
            name, (f"{year}-04-25" for year in range(1921, self.end_year))
        )
        self.assertNoSubdivTasHolidayName(name, range(self.start_year, 1921))

    def test_anzac_day_vic(self):
        name = "ANZAC Day"
        self.assertSubdivVicHolidayName(
            name, (f"{year}-04-25" for year in range(1921, self.end_year))
        )
        self.assertNoSubdivVicHolidayName(name, range(self.start_year, 1921))

    def test_anzac_day_wa(self):
        name = "ANZAC Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivWaHolidayName(
            name, (f"{year}-04-25" for year in range(1921, self.end_year))
        )
        self.assertNoSubdivWaHolidayName(name, range(self.start_year, 1921))

        obs_dts = (
            "2010-04-26",
            "2015-04-27",
            "2020-04-27",
            "2021-04-26",
            "2026-04-27",
        )
        self.assertSubdivWaHolidayName(name_observed, obs_dts)
        self.assertNoSubdivWaNonObservedHoliday(obs_dts)
        self.assertNoSubdivWaHolidayName(name_observed, range(self.start_year, 1973))

    def test_sovereigns_birthday(self):
        name_king = "King's Birthday"
        name_queen = "Queen's Birthday"
        self.assertHolidayName(
            name_king,
            (f"{year}-11-09" for year in range(1902, 1912)),
            (f"{year}-06-03" for year in range(1912, 1936)),
        )
        self.assertNoHolidayName(name_king, range(1936, self.end_year))
        self.assertNoHolidayName(name_queen, range(1936, self.end_year))

        for subdiv, holidays in self.subdiv_holidays.items():
            match subdiv:
                case "QLD":
                    self.assertHolidayName(
                        name_queen,
                        holidays,
                        "2010-06-14",
                        "2011-06-13",
                        "2012-10-01",
                        "2013-06-10",
                        "2014-06-09",
                        "2015-06-08",
                        "2020-10-05",
                        "2021-10-04",
                        "2022-10-03",
                    )
                    self.assertHolidayName(
                        name_king,
                        holidays,
                        "2023-10-02",
                        "2024-10-07",
                        "2025-10-06",
                    )
                case "WA":
                    self.assertHolidayName(
                        name_queen,
                        holidays,
                        "1980-10-13",
                        "1981-10-12",
                        "1982-10-11",
                        "1983-10-10",
                        "2011-10-28",
                        "2012-10-01",
                        "2020-09-28",
                        "2021-09-27",
                        "2022-09-26",
                    )
                    self.assertHolidayName(
                        name_king,
                        holidays,
                        "2023-09-25",
                        "2024-09-23",
                        "2025-09-29",
                    )
                case _:
                    self.assertHolidayName(
                        name_queen,
                        holidays,
                        "2018-06-11",
                        "2019-06-10",
                        "2020-06-08",
                        "2021-06-14",
                        "2022-06-13",
                    )
                    self.assertHolidayName(
                        name_king,
                        holidays,
                        "2023-06-12",
                        "2024-06-10",
                        "2025-06-09",
                    )

            self.assertHolidayName(name_queen, holidays, range(1952, 2023))
            self.assertHolidayName(
                name_king, holidays, range(1936, 1952), range(2023, self.end_year)
            )
            self.assertNoHolidayName(
                name_queen, holidays, range(1936, 1952), range(2023, self.end_year)
            )
            self.assertNoHolidayName(name_king, holidays, range(1952, 2023))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in self.full_range))

    def test_christmas_day_act(self):
        name = "Christmas Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivActHolidayName(
            name, (f"{year}-12-25" for year in range(self.start_year, 1958))
        )
        self.assertSubdivActHolidayName(name, range(1958, self.end_year))

        dts = (
            "1960-12-25",
            "1966-12-25",
            "1977-12-25",
            "1983-12-25",
            "1988-12-25",
            "1993-12-25",
            "1994-12-25",
            "1999-12-25",
            "2004-12-25",
            "2005-12-25",
            "2010-12-25",
            "2011-12-25",
        )
        self.assertSubdivActNonObservedHolidayName(name, dts)
        self.assertNoSubdivActHoliday(dts)

        mov_dts = (
            "1960-12-26",
            "1966-12-26",
            "1977-12-26",
            "1983-12-26",
            "1988-12-26",
            "1993-12-27",
            "1994-12-26",
            "1999-12-27",
            "2004-12-27",
            "2005-12-26",
            "2010-12-27",
            "2011-12-26",
        )
        self.assertSubdivActHolidayName(name, mov_dts)

        obs_dts = (
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertSubdivActHolidayName(name_observed, obs_dts)
        self.assertNoSubdivActNonObservedHoliday(obs_dts)
        self.assertNoSubdivActHolidayName(name_observed, range(self.start_year, 2014))

    def test_christmas_day_nsw(self):
        name = "Christmas Day"
        self.assertSubdivNswHolidayName(name, (f"{year}-12-25" for year in self.full_range))

        obs_dts = (
            "2005-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertSubdivNswHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoSubdivNswNonObservedHoliday(obs_dts)

    def test_christmas_day_nt(self):
        name = "Christmas Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivNtHolidayName(
            name, (f"{year}-12-25" for year in range(self.start_year, 1981))
        )
        self.assertSubdivNtHolidayName(name, range(1981, self.end_year))

        dts = (
            "1982-12-25",
            "1983-12-25",
            "1988-12-25",
            "1993-12-25",
            "1994-12-25",
            "1999-12-25",
            "2004-12-25",
            "2005-12-25",
            "2010-12-25",
            "2011-12-25",
        )
        self.assertSubdivNtNonObservedHolidayName(name, dts)
        self.assertNoSubdivNtHoliday(dts)

        mov_dts = (
            "1982-12-27",
            "1983-12-26",
            "1988-12-26",
            "1993-12-27",
            "1994-12-26",
            "1999-12-27",
            "2004-12-27",
            "2005-12-26",
            "2010-12-27",
            "2011-12-26",
        )
        self.assertSubdivNtHolidayName(name, mov_dts)

        obs_dts = (
            "2016-12-26",
            "2021-12-27",
            "2022-12-26",
        )
        self.assertSubdivNtHolidayName(name_observed, obs_dts)
        self.assertNoSubdivNtHolidayName(name_observed, range(self.start_year, 2016))

    def test_christmas_day_qld(self):
        name = "Christmas Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivQldHolidayName(
            name, (f"{year}-12-25" for year in range(self.start_year, 1984))
        )
        self.assertSubdivQldHolidayName(name, range(1984, self.end_year))

        dts = (
            "1988-12-25",
            "1994-12-25",
            "2005-12-25",
        )
        self.assertSubdivQldNonObservedHolidayName(name, dts)
        self.assertNoSubdivQldHoliday(dts)

        mov_dts = (
            "1988-12-26",
            "1994-12-26",
            "2005-12-26",
        )
        self.assertSubdivQldHolidayName(name, mov_dts)

        obs_dts = (
            "2010-12-28",  # special holiday.
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertSubdivQldHolidayName(name_observed, obs_dts)
        self.assertNoSubdivQldNonObservedHoliday(obs_dts)
        self.assertNoSubdivQldHolidayName(name_observed, range(self.start_year, 2010))

    def test_christmas_day_sa(self):
        name = "Christmas Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivSaHolidayName(
            name,
            (
                f"{year}-12-25"
                for year in (*range(self.start_year, 1984), *range(2024, self.end_year))
            ),
        )
        self.assertSubdivSaHolidayName(name, range(1984, 2024))

        dts = (
            "1988-12-25",
            "1993-12-25",
            "1994-12-25",
            "1999-12-25",
            "2004-12-25",
            "2010-12-25",
            "2021-12-25",
        )
        self.assertSubdivSaNonObservedHolidayName(name, dts)
        self.assertNoSubdivSaHoliday(dts)

        mov_dts = (
            "1988-12-26",
            "1993-12-27",
            "1994-12-26",
            "1999-12-27",
            "2004-12-27",
            "2010-12-27",
            "2021-12-27",
        )
        self.assertSubdivSaHolidayName(name, mov_dts)

        obs_dts = (
            "2005-12-26",
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
        )
        self.assertSubdivSaHolidayName(name_observed, obs_dts)
        self.assertNoSubdivSaHolidayName(name_observed, range(self.start_year, 2003))

    def test_christmas_day_tas(self):
        name = "Christmas Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivTasHolidayName(
            name,
            (
                f"{year}-12-25"
                for year in (*range(self.start_year, 2000), *range(2010, self.end_year))
            ),
        )
        self.assertSubdivTasHolidayName(name, range(2000, 2010))

        dts = (
            "2004-12-25",
            "2005-12-25",
        )
        self.assertSubdivTasNonObservedHolidayName(name, dts)
        self.assertNoSubdivTasHoliday(dts)

        mov_dts = (
            "2004-12-27",
            "2005-12-27",
        )
        self.assertSubdivTasHolidayName(name, mov_dts)
        self.assertNoSubdivTasNonObservedHoliday(mov_dts)

        obs_dts = (
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertSubdivTasHolidayName(name_observed, obs_dts)
        self.assertNoSubdivTasHolidayName(name_observed, range(self.start_year, 2010))

    def test_christmas_day_vic(self):
        name = "Christmas Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivVicHolidayName(
            name,
            (
                f"{year}-12-25"
                for year in (*range(self.start_year, 2008), *range(2019, self.end_year))
            ),
        )
        self.assertSubdivVicHolidayName(name, range(2008, 2019))

        dts = (
            "2010-12-25",
            "2011-12-25",
            "2016-12-25",
        )
        self.assertSubdivVicNonObservedHolidayName(name, dts)
        self.assertNoSubdivVicHoliday(dts)

        mov_dts = (
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
        )
        self.assertSubdivVicHolidayName(name, mov_dts)
        self.assertNoSubdivVicNonObservedHoliday(mov_dts)

        obs_dts = (
            "2021-12-27",
            "2022-12-27",
        )
        self.assertSubdivVicHolidayName(name_observed, obs_dts)
        self.assertNoSubdivVicNonObservedHoliday(obs_dts)
        self.assertNoSubdivVicHolidayName(name_observed, range(self.start_year, 2019))

    def test_christmas_day_wa(self):
        name = "Christmas Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivWaHolidayName(name, (f"{year}-12-25" for year in self.full_range))

        obs_dts = (
            "2004-12-27",
            "2005-12-26",
            "2010-12-27",
            "2011-12-26",
            "2016-12-26",
            "2021-12-27",
            "2022-12-26",
        )
        self.assertSubdivWaHolidayName(name_observed, obs_dts)
        self.assertNoSubdivWaHolidayName(name_observed, range(self.start_year, 1972))

    def test_boxing_day(self):
        self.assertHolidayName("Boxing Day", (f"{year}-12-26" for year in self.full_range))

    def test_boxing_day_act(self):
        name = "Boxing Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivActHolidayName(
            name, (f"{year}-12-26" for year in range(self.start_year, 1958))
        )
        self.assertSubdivActHolidayName(name, range(1958, self.end_year))

        dts = (
            "1960-12-26",
            "1965-12-26",
            "1966-12-26",
            "1971-12-26",
            "1976-12-26",
            "1977-12-26",
            "1982-12-26",
            "1983-12-26",
            "1988-12-26",
            "1992-12-26",
            "1993-12-26",
            "1994-12-26",
            "1998-12-26",
            "1999-12-26",
            "2004-12-26",
            "2005-12-26",
            "2009-12-26",
            "2010-12-26",
            "2011-12-26",
        )
        self.assertSubdivActNonObservedHolidayName(name, dts)

        mov_dts = (
            "1960-12-27",
            "1965-12-27",
            "1966-12-27",
            "1971-12-27",
            "1976-12-27",
            "1977-12-27",
            "1982-12-27",
            "1983-12-27",
            "1988-12-27",
            "1992-12-28",
            "1993-12-28",
            "1994-12-27",
            "1998-12-28",
            "1999-12-28",
            "2004-12-28",
            "2005-12-27",
            "2009-12-28",
            "2010-12-28",
            "2011-12-27",
        )
        self.assertSubdivActHolidayName(name, mov_dts)

        obs_dts = (
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
            "2026-12-28",
        )
        self.assertSubdivActHolidayName(name_observed, obs_dts)
        self.assertNoSubdivActNonObservedHoliday(obs_dts)
        self.assertNoSubdivActHolidayName(name_observed, range(self.start_year, 2014))

    def test_boxing_day_nsw(self):
        name = "Boxing Day"
        self.assertSubdivNswHolidayName(name, (f"{year}-12-26" for year in self.full_range))

        obs_dts = (
            "2004-12-27",
            "2010-12-27",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
            "2026-12-28",
        )
        self.assertSubdivNswHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoSubdivNswNonObservedHoliday(obs_dts)

    def test_boxing_day_nt(self):
        name = "Boxing Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivNtHolidayName(
            name, (f"{year}-12-26" for year in range(self.start_year, 1981))
        )
        self.assertSubdivNtHolidayName(name, range(1981, self.end_year))

        dts = (
            "1981-12-26",
            "1982-12-26",
            "1983-12-26",
            "1987-12-26",
            "1988-12-26",
            "1992-12-26",
            "1993-12-26",
            "1994-12-26",
            "1998-12-26",
            "1999-12-26",
            "2004-12-26",
            "2005-12-26",
            "2009-12-26",
            "2010-12-26",
            "2011-12-26",
            "2015-12-26",
            "2016-12-26",
            "2020-12-26",
            "2021-12-26",
            "2022-12-26",
        )
        self.assertSubdivNtNonObservedHolidayName(name, dts)

        mov_dts = (
            "1981-12-28",
            "1982-12-28",
            "1983-12-27",
            "1987-12-28",
            "1988-12-27",
            "1992-12-28",
            "1993-12-28",
            "1994-12-27",
            "1998-12-28",
            "1999-12-28",
            "2004-12-28",
            "2005-12-27",
            "2009-12-28",
            "2010-12-28",
            "2011-12-27",
            "2015-12-28",
            "2016-12-27",
            "2020-12-28",
            "2021-12-28",
            "2022-12-27",
        )
        self.assertSubdivNtHolidayName(name, mov_dts)

        obs_dts = ("2026-12-28",)
        self.assertSubdivNtHolidayName(name_observed, obs_dts)
        self.assertNoSubdivNtHolidayName(name_observed, range(self.start_year, 2023))

    def test_boxing_day_qld(self):
        name = "Boxing Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivQldHolidayName(
            name, (f"{year}-12-26" for year in range(self.start_year, 1984))
        )
        self.assertSubdivQldHolidayName(name, range(1984, self.end_year))

        dts = (
            "1988-12-26",
            "1993-12-26",
            "1994-12-26",
            "1999-12-26",
            "2004-12-26",
            "2005-12-26",
            "2010-12-26",
        )
        self.assertSubdivQldNonObservedHolidayName(name, dts)

        mov_dts = (
            "1988-12-27",
            "1993-12-27",
            "1994-12-27",
            "1999-12-27",
            "2004-12-27",
            "2005-12-27",
            "2010-12-27",
        )
        self.assertSubdivQldHolidayName(name, mov_dts)

        obs_dts = (
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
            "2026-12-28",
        )
        self.assertSubdivQldHolidayName(name_observed, obs_dts)
        self.assertNoSubdivQldNonObservedHoliday(obs_dts)
        self.assertNoSubdivQldHolidayName(name_observed, range(self.start_year, 2011))

    def test_boxing_day_sa(self):
        name = "Proclamation Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivSaHolidayName(
            name,
            (
                f"{year}-12-26"
                for year in (*range(self.start_year, 1984), *range(2024, self.end_year))
            ),
        )
        self.assertSubdivSaHolidayName(name, range(1984, 2024))

        dts = (
            "1987-12-26",
            "1992-12-26",
            "1993-12-26",
            "1994-12-26",
            "1998-12-26",
            "1999-12-26",
            "2009-12-26",
            "2015-12-26",
            "2020-12-26",
        )
        self.assertSubdivSaNonObservedHolidayName(name, dts)

        mov_dts = (
            "1987-12-28",
            "1992-12-28",
            "1993-12-28",
            "1994-12-27",
            "1998-12-28",
            "1999-12-28",
            "2009-12-28",
            "2015-12-28",
            "2020-12-28",
        )
        self.assertSubdivSaHolidayName(name, mov_dts)

        obs_dts = (
            "2004-12-28",
            "2005-12-27",
            "2010-12-28",
            "2011-12-27",
            "2016-12-27",
            "2021-12-28",
            "2022-12-27",
            "2026-12-28",
        )
        self.assertSubdivSaHolidayName(name_observed, obs_dts)
        self.assertNoSubdivSaHolidayName(name_observed, range(self.start_year, 2003))

    def test_boxing_day_tas(self):
        name = "Boxing Day"
        self.assertSubdivTasHolidayName(
            name, (f"{year}-12-26" for year in range(self.start_year, 2000))
        )
        self.assertSubdivTasHolidayName(name, range(2000, self.end_year))

        dts = (
            "2004-12-26",
            "2009-12-26",
            "2010-12-26",
            "2015-12-26",
            "2020-12-26",
            "2021-12-26",
            "2026-12-26",
        )
        self.assertSubdivTasNonObservedHolidayName(name, dts)
        self.assertNoSubdivTasHoliday(dts)

        mov_dts = (
            "2004-12-28",
            "2009-12-28",
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
            "2026-12-28",
        )
        self.assertSubdivTasHolidayName(name, mov_dts)
        self.assertNoSubdivTasNonObservedHoliday(mov_dts)

    def test_boxing_day_vic(self):
        name = "Boxing Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivVicHolidayName(
            name,
            (
                f"{year}-12-26"
                for year in (*range(self.start_year, 1994), *range(2008, self.end_year))
            ),
        )
        self.assertSubdivVicHolidayName(name, range(1994, 2008))

        dts = (
            "1999-12-26",
            "2004-12-26",
        )
        self.assertSubdivVicNonObservedHolidayName(name, dts)
        self.assertNoSubdivVicHoliday(dts)

        mov_dts = (
            "1999-12-27",
            "2004-12-27",
        )
        self.assertSubdivVicHolidayName(name, mov_dts)
        self.assertNoSubdivVicNonObservedHoliday(mov_dts)

        obs_dts = (
            "2009-12-28",
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
            "2026-12-28",
        )
        self.assertSubdivVicHolidayName(name_observed, obs_dts)
        self.assertNoSubdivVicNonObservedHoliday(obs_dts)
        self.assertNoSubdivVicHolidayName(name_observed, range(self.start_year, 2008))

    def test_boxing_day_wa(self):
        name = "Boxing Day"
        name_observed = f"{name} (observed)"
        self.assertSubdivWaHolidayName(name, (f"{year}-12-26" for year in self.full_range))

        obs_dts = (
            "2015-12-28",
            "2016-12-27",
            "2020-12-28",
            "2021-12-28",
            "2022-12-27",
            "2026-12-28",
        )
        self.assertSubdivWaHolidayName(name_observed, obs_dts)
        self.assertNoSubdivWaHolidayName(name_observed, range(self.start_year, 1972))

    # Multiple subdivisions holidays.

    def test_labor_day(self):
        name = "Labour Day"
        self.assertNoHolidayName(name)

        dts = (
            "2020-10-05",
            "2021-10-04",
            "2022-10-03",
            "2023-10-02",
            "2024-10-07",
            "2025-10-06",
        )
        self.assertSubdivActHolidayName(name, dts)
        self.assertSubdivNswHolidayName(name, dts)
        self.assertSubdivSaHolidayName(name, dts)
        self.assertSubdivActHolidayName(name, self.full_range)
        self.assertSubdivNswHolidayName(name, self.full_range)
        self.assertSubdivSaHolidayName(name, self.full_range)

        dts = (
            "2011-05-02",
            "2012-05-07",
            "2013-10-07",
            "2014-10-06",
            "2015-10-05",
            "2020-05-04",
            "2021-05-03",
            "2022-05-02",
            "2023-05-01",
            "2024-05-06",
            "2025-05-05",
        )
        self.assertSubdivQldHolidayName(name, dts)
        self.assertSubdivQldHolidayName(name, self.full_range)

        dts = (
            "2020-03-09",
            "2021-03-08",
            "2022-03-14",
            "2023-03-13",
            "2024-03-11",
            "2025-03-10",
        )
        self.assertSubdivVicHolidayName(name, dts)
        self.assertSubdivVicHolidayName(name, self.full_range)

        dts = (
            "2020-03-02",
            "2021-03-01",
            "2022-03-07",
            "2023-03-06",
            "2024-03-04",
            "2025-03-03",
        )
        self.assertSubdivWaHolidayName(name, dts)
        self.assertSubdivWaHolidayName(name, self.full_range)

        self.assertNoSubdivNtHolidayName(name)
        self.assertNoSubdivTasHolidayName(name)

    def test_christmas_eve(self):
        name_common = "Christmas Eve"
        name_6pm = "Christmas Eve (from 6pm)"
        name_7pm = "Christmas Eve (from 7pm)"
        self.assertNoHolidayName(name_common)
        self.assertNoHolidayName(name_6pm)
        self.assertNoHolidayName(name_7pm)

        subdiv_names_start_years = {
            "NT": (name_7pm, 2016),
            "QLD": (name_6pm, 2019),
            "SA": (name_7pm, 2012),
        }
        for subdiv, holidays in self.subdiv_half_day_holidays.items():
            if subdiv in subdiv_names_start_years:
                name, start_year = subdiv_names_start_years[subdiv]
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-24" for year in range(start_year, self.end_year))
                )
                self.assertNoHolidayName(
                    name,
                    holidays,
                    (f"{year}-12-24" for year in range(self.start_year, start_year)),
                )
            else:
                self.assertNoHolidayName(name_common, holidays)
                self.assertNoHolidayName(name_6pm, holidays)
                self.assertNoHolidayName(name_7pm, holidays)

    def test_new_years_eve(self):
        name_common = "New Year's Eve"
        name_7pm = "New Year's Eve (from 7pm)"
        self.assertNoHolidayName(name_common)
        self.assertNoHolidayName(name_7pm)

        subdiv_start_years = {
            "NT": 2016,
            "SA": 2012,
        }
        for subdiv, holidays in self.subdiv_half_day_holidays.items():
            if start_year := subdiv_start_years.get(subdiv):
                self.assertHalfDayHolidayName(
                    name_7pm,
                    holidays,
                    (f"{year}-12-31" for year in range(start_year, self.end_year)),
                )
                self.assertNoHalfDayHolidayName(
                    name_7pm,
                    holidays,
                    (f"{year}-12-31" for year in range(self.start_year, start_year)),
                )
            else:
                self.assertNoHolidayName(name_common, holidays)
                self.assertNoHolidayName(name_7pm, holidays)

    # Single subdivision holidays.

    def test_canberra_day(self):
        name = "Canberra Day"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "ACT":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-12" for year in range(1913, 1959))
                )
                self.assertHolidayName(
                    name,
                    holidays,
                    "1959-03-16",
                    "2000-03-20",
                    "2007-03-19",
                    "2008-03-10",
                    "2010-03-08",
                    "2012-03-12",
                    "2020-03-09",
                    "2021-03-08",
                    "2022-03-14",
                    "2023-03-13",
                    "2024-03-11",
                    "2025-03-10",
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1913))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_reconciliation_day(self):
        name = "Reconciliation Day"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "ACT":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2018-05-28",
                    "2019-05-27",
                    "2020-06-01",
                    "2021-05-31",
                    "2022-05-30",
                    "2023-05-29",
                    "2024-05-27",
                    "2025-06-02",
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2018))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_family_and_community_day(self):
        name = "Family & Community Day"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "ACT":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2010-09-26",
                    "2011-10-10",
                    "2012-10-08",
                    "2013-09-30",
                    "2014-09-29",
                    "2015-09-28",
                    "2016-09-26",
                    "2017-09-25",
                )
                self.assertNoHolidayName(
                    name, holidays, range(self.start_year, 2010), range(2018, self.end_year)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_bank_holiday_act(self):
        name = "Bank Holiday"

        self.assertSubdivActBankHolidayName(
            name,
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
            "2025-08-04",
        )
        self.assertSubdivActBankHolidayName(name, self.full_range)

    def test_bank_holiday_nsw(self):
        name = "Bank Holiday"
        self.assertNoHolidayName(name)

        # PUBLIC.
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NSW":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2000-08-07",
                    "2007-08-06",
                    "2008-08-04",
                    "2009-08-03",
                    "2010-08-02",
                )
                self.assertNoHolidayName(
                    name, holidays, range(self.start_year, 1912), range(2011, self.end_year)
                )
            else:
                self.assertNoHolidayName(name, holidays)

        # BANK.
        self.assertSubdivNswBankHolidayName(
            name,
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
            "2025-08-04",
        )
        self.assertSubdivNswBankHolidayName(name, range(2011, self.end_year))
        self.assertNoSubdivNswBankHolidayName(name, range(self.start_year, 2011))

    def test_may_day(self):
        name = "May Day"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NT":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-05-04",
                    "2021-05-03",
                    "2022-05-02",
                    "2023-05-01",
                    "2024-05-06",
                    "2025-05-05",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_picnic_day(self):
        name = "Picnic Day"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NT":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-08-03",
                    "2021-08-02",
                    "2022-08-01",
                    "2023-08-07",
                    "2024-08-05",
                    "2025-08-04",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_royal_queensland_show(self):
        name = "The Royal Queensland Show"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "QLD":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-08-14",
                    "2021-10-29",
                    "2022-08-10",
                    "2023-08-16",
                    "2024-08-14",
                    "2025-08-13",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_adelaide_cup_day(self):
        name = "Adelaide Cup Day"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SA":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2005-05-16",
                    "2006-03-13",
                    "2020-03-09",
                    "2021-03-08",
                    "2022-03-14",
                    "2023-03-13",
                    "2024-03-11",
                    "2025-03-10",
                )
                self.assertHolidayName(name, holidays, range(1973, self.end_year))
                self.assertNoHolidayName(name, holidays, range(self.start_year, 1973))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_eight_hours_day(self):
        name = "Eight Hours Day"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TAS":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-03-09",
                    "2021-03-08",
                    "2022-03-14",
                    "2023-03-13",
                    "2024-03-11",
                    "2025-03-10",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_easter_tuesday(self):
        name = "Easter Tuesday"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TAS":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2006-04-18",
                    "2007-04-10",
                    "2008-03-25",
                    "2009-04-14",
                    "2010-04-06",
                )
                self.assertHolidayName(name, holidays, range(self.start_year, 2011))
                self.assertNoHolidayName(name, holidays, range(2011, self.end_year))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_grand_final_day(self):
        name = "Grand Final Day"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "VIC":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2015-10-02",
                    "2016-09-30",
                    "2020-10-23",
                    "2021-09-24",
                    "2022-09-23",
                    "2023-09-29",
                    "2024-09-27",
                    "2025-09-26",
                )
                self.assertHolidayName(name, holidays, range(2015, self.end_year))
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2015))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_melbourne_cup_day(self):
        name = "Melbourne Cup Day"
        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "VIC":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-11-03",
                    "2021-11-02",
                    "2022-11-01",
                    "2023-11-07",
                    "2024-11-05",
                    "2025-11-04",
                )
                self.assertHolidayName(name, holidays, range(2009, self.end_year))
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2009))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_western_australia_day(self):
        name_1833 = "Foundation Day"
        name_2012 = "Western Australia Day"
        self.assertNoHolidayName(name_1833)
        self.assertNoHolidayName(name_2012)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "WA":
                self.assertHolidayName(
                    name_1833,
                    holidays,
                    "2007-06-04",
                    "2008-06-02",
                    "2009-06-01",
                    "2010-06-07",
                    "2011-06-06",
                )
                self.assertHolidayName(name_1833, holidays, range(1833, 2012))
                self.assertNoHolidayName(
                    name_1833, holidays, range(self.start_year, 1833), range(2012, self.end_year)
                )

                self.assertHolidayName(
                    name_2012,
                    holidays,
                    "2020-06-01",
                    "2021-06-07",
                    "2022-06-06",
                    "2023-06-05",
                    "2024-06-03",
                    "2025-06-02",
                )
                self.assertHolidayName(name_2012, holidays, range(2012, self.end_year))
                self.assertNoHolidayName(name_2012, holidays, range(self.start_year, 2012))
            else:
                self.assertNoHolidayName(name_1833, holidays)
                self.assertNoHolidayName(name_2012, holidays)

    def test_national_day_of_mourning_for_queen_elizabeth_ii(self):
        name = "National Day of Mourning for Queen Elizabeth II"
        dts = "2022-09-22"
        self.assertHolidayName(name, dts)
        for holidays in self.subdiv_holidays.values():
            self.assertHolidayName(name, holidays, dts)

    def test_special_holidays(self):
        self.assertSubdivActHoliday("2020-04-27", "2021-04-25")

        qld_obs_dts = ("2010-12-28", "2011-01-03")
        self.assertSubdivQldHoliday(qld_obs_dts, "2012-06-11")
        self.assertNoSubdivQldNonObservedHoliday(qld_obs_dts)

        self.assertSubdivWaHoliday("2011-04-26")

    def test_all_holidays(self):
        holidays_found = set()
        for subdiv in Australia.subdivisions:
            holidays_found.update(
                Australia(
                    categories=Australia.supported_categories,
                    subdiv=subdiv,
                    observed=False,
                    years=(1930, 1957, 2012, 2015, 2023),
                ).values()
            )
        all_holidays = {
            "New Year's Day",
            "Anniversary Day",
            "Australia Day",
            "Adelaide Cup Day",
            "Canberra Day",
            "Good Friday",
            "Easter Saturday",
            "Easter Sunday",
            "Easter Monday",
            "Easter Tuesday",
            "ANZAC Day",
            "Reconciliation Day",
            "Queen's Birthday",
            "Queen's Diamond Jubilee",
            "King's Birthday",
            "Bank Holiday",
            "The Royal Queensland Show",
            "Western Australia Day",
            "Foundation Day",
            "Family & Community Day",
            "Labour Day",
            "Eight Hours Day",
            "May Day",
            "Picnic Day",
            "Melbourne Cup Day",
            "Grand Final Day",
            "Christmas Day",
            "Proclamation Day",
            "Boxing Day",
            "Christmas Eve (from 6pm)",
            "Christmas Eve (from 7pm)",
            "New Year's Eve (from 7pm)",
        }
        self.assertEqual(all_holidays, holidays_found)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day; New Year's Day (observed)"),
            ("2022-01-26", "Australia Day"),
            ("2022-03-07", "Labour Day"),
            ("2022-03-14", "Adelaide Cup Day; Canberra Day; Eight Hours Day; Labour Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-16", "Easter Saturday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-25", "ANZAC Day"),
            ("2022-05-02", "Labour Day; May Day"),
            ("2022-05-30", "Reconciliation Day"),
            ("2022-06-06", "Western Australia Day"),
            ("2022-06-13", "Queen's Birthday"),
            ("2022-08-01", "Bank Holiday; Picnic Day"),
            ("2022-08-10", "The Royal Queensland Show"),
            ("2022-09-22", "National Day of Mourning for Queen Elizabeth II"),
            ("2022-09-23", "Grand Final Day"),
            ("2022-09-26", "Queen's Birthday"),
            ("2022-10-03", "Labour Day; Queen's Birthday"),
            ("2022-11-01", "Melbourne Cup Day"),
            ("2022-12-24", "Christmas Eve (from 6pm); Christmas Eve (from 7pm)"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day; Christmas Day (observed); Proclamation Day"),
            (
                "2022-12-27",
                "Boxing Day; Boxing Day (observed); Christmas Day (observed); "
                "Proclamation Day (observed)",
            ),
            ("2022-12-31", "New Year's Eve (from 7pm)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day; New Year's Day (observed)"),
            ("2022-01-26", "Australia Day"),
            ("2022-03-07", "Labor Day"),
            ("2022-03-14", "Adelaide Cup Day; Canberra Day; Eight Hours Day; Labor Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-16", "Easter Saturday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-25", "ANZAC Day"),
            ("2022-05-02", "Labor Day; May Day"),
            ("2022-05-30", "Reconciliation Day"),
            ("2022-06-06", "Western Australia Day"),
            ("2022-06-13", "Queen's Birthday"),
            ("2022-08-01", "Bank Holiday; Picnic Day"),
            ("2022-08-10", "The Royal Queensland Show"),
            ("2022-09-22", "National Day of Mourning for Queen Elizabeth II"),
            ("2022-09-23", "Grand Final Day"),
            ("2022-09-26", "Queen's Birthday"),
            ("2022-10-03", "Labor Day; Queen's Birthday"),
            ("2022-11-01", "Melbourne Cup Day"),
            ("2022-12-24", "Christmas Eve (from 6pm); Christmas Eve (from 7pm)"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day; Christmas Day (observed); Proclamation Day"),
            (
                "2022-12-27",
                "Boxing Day; Boxing Day (observed); Christmas Day (observed); "
                "Proclamation Day (observed)",
            ),
            ("2022-12-31", "New Year's Eve (from 7pm)"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-03", "ชดเชยวันขึ้นปีใหม่; วันขึ้นปีใหม่"),
            ("2022-01-26", "วันชาติออสเตรเลีย"),
            ("2022-03-07", "วันแรงงาน"),
            ("2022-03-14", "วันแคนเบอร์รา; วันแปดชั่วโมง (วันแรงงาน); วันแรงงาน; วันแอดิเลดคัพ"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-16", "วันเสาร์อีสเตอร์"),
            ("2022-04-17", "วันอาทิตย์อีสเตอร์"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-04-25", "วันแอนแซค"),
            ("2022-05-02", "วันเมย์เดย์ (วันแรงงาน); วันแรงงาน"),
            ("2022-05-30", "วันแห่งการปรองดอง"),
            ("2022-06-06", "วันเวสเทิร์นออสเตรเลีย"),
            ("2022-06-13", "วันเฉลิมพระชนมพรรษาสมเด็จพระราชินีนาถ"),
            ("2022-08-01", "วันปิกนิก; วันหยุดธนาคาร"),
            ("2022-08-10", "เทศกาลรอยัลควีนส์แลนด์โชว์"),
            ("2022-09-22", "วันไว้ทุกข์แห่งชาติแด่สมเด็จพระราชินีนาถเอลิซาเบธที่ 2"),
            ("2022-09-23", "วันศุกร์ก่อนวันแข่งฟุตบอลออสเตรเลีย (AFL) รอบสุดท้าย"),
            ("2022-09-26", "วันเฉลิมพระชนมพรรษาสมเด็จพระราชินีนาถ"),
            ("2022-10-03", "วันเฉลิมพระชนมพรรษาสมเด็จพระราชินีนาถ; วันแรงงาน"),
            ("2022-11-01", "วันเมลเบิร์นคัพ"),
            ("2022-12-24", "วันคริสต์มาสอีฟ (ตั้งแต่ 18:00 น.); วันคริสต์มาสอีฟ (ตั้งแต่ 19:00 น.)"),
            ("2022-12-25", "วันคริสต์มาส"),
            ("2022-12-26", "ชดเชยวันคริสต์มาส; วันสถาปนา; วันเปิดกล่องของขวัญ"),
            ("2022-12-27", "ชดเชยวันคริสต์มาส; ชดเชยวันสถาปนา; ชดเชยวันเปิดกล่องของขวัญ; วันเปิดกล่องของขวัญ"),
            ("2022-12-31", "วันสิ้นปี (ตั้งแต่ 19:00 น.)"),
        )
