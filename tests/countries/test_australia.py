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

from holidays.countries.australia import Australia, AU, AUS
from tests.common import TestCase


class TestAustralia(TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1900, 2050)
        super().setUpClass(Australia, years=years, years_non_observed=range(2000, 2024))
        cls.subdiv_holidays = {
            subdiv: Australia(subdiv=subdiv, years=years) for subdiv in Australia.subdivisions
        }

    def test_country_aliases(self):
        self.assertCountryAliases(Australia, AU, AUS)

    def test_new_years(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1900, 2050)))
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

        for subdiv in Australia.subdivisions:
            self.assertHolidayName(
                name, self.subdiv_holidays[subdiv], (f"{year}-01-01" for year in range(1900, 2050))
            )
            self.assertHolidayName(f"{name} (Observed)", self.subdiv_holidays[subdiv], obs_dt)
            self.assertNoNonObservedHoliday(Australia(subdiv=subdiv, observed=False), obs_dt)

    def test_good_friday(self):
        name = "Good Friday"
        dt = (
            "1999-04-02",
            "2000-04-21",
            "2010-04-02",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(1900, 2050))
        for subdiv in Australia.subdivisions:
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], dt)

    def test_easter_saturday(self):
        name = "Easter Saturday"
        dt = (
            "1999-04-03",
            "2000-04-22",
            "2010-04-03",
            "2018-03-31",
            "2019-04-20",
            "2020-04-11",
            "2021-04-03",
            "2022-04-16",
        )
        for subdiv in ("ACT", "NSW", "NT", "QLD", "SA", "VIC"):
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], dt)
        for subdiv in ("TAS", "WA"):
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])
        self.assertNoHolidayName(name)

    def test_easter_sunday(self):
        name = "Easter Sunday"
        dt = (
            "1999-04-04",
            "2000-04-23",
            "2010-04-04",
            "2018-04-01",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
        )
        for subdiv in ("ACT", "NSW", "QLD", "VIC"):
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], dt)
        for subdiv in ("NT", "SA", "TAS", "WA"):
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])
        self.assertNoHolidayName(name)

    def test_easter_monday(self):
        name = "Easter Monday"
        dt = (
            "1999-04-05",
            "2000-04-24",
            "2010-04-05",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(1900, 2050))
        for subdiv in Australia.subdivisions:
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], dt)

    def test_australia_day(self):
        name_1 = "Anniversary Day"
        name_2 = "Australia Day"
        self.assertHolidayName(name_2, (f"{year}-01-26" for year in range(1935, 2050)))
        self.assertNoHolidayName(name_2, range(1900, 1935))
        for subdiv in set(Australia.subdivisions) - {"NSW"}:
            self.assertHolidayName(
                name_2,
                self.subdiv_holidays[subdiv],
                (f"{year}-01-26" for year in range(1935, 2050)),
            )
            self.assertNoHolidayName(name_2, self.subdiv_holidays[subdiv], range(1900, 1935))
        self.assertHolidayName(
            name_1, self.subdiv_holidays["NSW"], (f"{year}-01-26" for year in range(1935, 1946))
        )
        self.assertHolidayName(
            name_2, self.subdiv_holidays["NSW"], (f"{year}-01-26" for year in range(1946, 2050))
        )

        self.assertHolidayName(name_1, (f"{year}-01-26" for year in range(1900, 1935)))
        self.assertNoHolidayName(name_1, Australia(years=1887))
        for subdiv in set(Australia.subdivisions) - {"SA"}:
            self.assertHolidayName(
                name_1,
                self.subdiv_holidays[subdiv],
                (f"{year}-01-26" for year in range(1900, 1935)),
            )
            self.assertNoHolidayName(name_1, Australia(subdiv=subdiv, years=1887))

        obs_dt = (
            "2002-01-28",
            "2003-01-27",
            "2008-01-28",
            "2013-01-28",
            "2014-01-27",
            "2019-01-28",
            "2020-01-27",
        )
        self.assertHolidayName(f"{name_2} (Observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        self.assertNoHolidayName(f"{name_2} (Observed)", range(1900, 1946))

    def test_anzac_day(self):
        name = "Anzac Day"
        self.assertHolidayName(name, (f"{year}-04-25" for year in range(1921, 2050)))
        self.assertNoHolidayName(name, range(1900, 1921))
        for subdiv in Australia.subdivisions:
            self.assertHolidayName(
                name, self.subdiv_holidays[subdiv], (f"{year}-04-25" for year in range(1921, 2050))
            )
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv], range(1900, 1921))

        obs_dt = (
            "2004-04-26",
            "2010-04-26",
            "2021-04-26",
        )
        for subdiv in ("ACT", "NT", "QLD", "SA", "WA"):
            self.assertHolidayName(f"{name} (Observed)", self.subdiv_holidays[subdiv], obs_dt)
            self.assertNoNonObservedHoliday(Australia(subdiv=subdiv, observed=False), obs_dt)
        for subdiv in ("NSW", "TAS", "VIC"):
            self.assertNoHoliday(self.subdiv_holidays[subdiv], obs_dt)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1900, 2050)))
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

        for subdiv in Australia.subdivisions:
            self.assertHolidayName(
                name, self.subdiv_holidays[subdiv], (f"{year}-12-25" for year in range(1900, 2050))
            )
            self.assertHolidayName(f"{name} (Observed)", self.subdiv_holidays[subdiv], obs_dt)
            self.assertNoNonObservedHoliday(Australia(subdiv=subdiv, observed=False), obs_dt)

    def test_boxing_day(self):
        name_common = "Boxing Day"
        name_sa = "Proclamation Day"
        self.assertHolidayName(name_common, (f"{year}-12-26" for year in range(1900, 2050)))
        obs_dt = (
            "2004-12-28",
            "2009-12-28",
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name_common} (Observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

        for subdiv in Australia.subdivisions:
            name = name_sa if subdiv == "SA" else name_common
            self.assertHolidayName(
                name, self.subdiv_holidays[subdiv], (f"{year}-12-26" for year in range(1900, 2050))
            )
            self.assertHolidayName(f"{name} (Observed)", self.subdiv_holidays[subdiv], obs_dt)
            self.assertNoNonObservedHoliday(Australia(subdiv=subdiv, observed=False), obs_dt)

    def test_labour_day(self):
        name = "Labour Day"
        dt = (
            "2000-10-02",
            "2010-10-04",
            "2018-10-01",
            "2019-10-07",
            "2020-10-05",
            "2021-10-04",
            "2022-10-03",
        )
        for subdiv in ("ACT", "NSW", "SA"):
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], dt)

        dt = (
            "2000-05-01",
            "2010-05-03",
            "2018-05-07",
            "2019-05-06",
            "2020-05-04",
            "2021-05-03",
            "2022-05-02",
        )
        self.assertHolidayName("May Day", self.subdiv_holidays["NT"], dt)

        self.assertHolidayName(name, self.subdiv_holidays["QLD"], dt)
        self.assertHolidayName(
            name, self.subdiv_holidays["QLD"], "2013-10-07", "2014-10-06", "2015-10-05"
        )

        dt = (
            "2000-03-13",
            "2010-03-08",
            "2018-03-12",
            "2019-03-11",
            "2020-03-09",
            "2021-03-08",
            "2022-03-14",
        )
        self.assertHolidayName("Eight Hours Day", self.subdiv_holidays["TAS"], dt)

        self.assertHolidayName(name, self.subdiv_holidays["VIC"], dt)

        dt = (
            "2000-03-06",
            "2010-03-01",
            "2018-03-05",
            "2019-03-04",
            "2020-03-02",
            "2021-03-01",
            "2022-03-07",
        )
        self.assertHolidayName(name, self.subdiv_holidays["WA"], dt)

    def test_sovereigns_birthday(self):
        name_king = "King's Birthday"
        name_queen = "Queen's Birthday"
        self.assertHolidayName(name_king, (f"{year}-11-09" for year in range(1902, 1912)))
        self.assertHolidayName(name_king, (f"{year}-06-03" for year in range(1912, 1936)))
        for subdiv in Australia.subdivisions:
            self.assertHolidayName(
                name_king,
                self.subdiv_holidays[subdiv],
                (f"{year}-11-09" for year in range(1902, 1912)),
            )
            self.assertHolidayName(
                name_king,
                self.subdiv_holidays[subdiv],
                (f"{year}-06-03" for year in range(1912, 1936)),
            )
        self.assertNoHolidayName(name_king, range(1936, 2050))
        self.assertNoHolidayName(name_queen, range(1936, 2050))

        dt = (
            "2000-06-12",
            "2010-06-14",
            "2018-06-11",
            "2019-06-10",
            "2020-06-08",
            "2021-06-14",
            "2022-06-13",
        )
        for subdiv in ("ACT", "NSW", "NT", "SA", "TAS", "VIC"):
            self.assertHolidayName(name_queen, self.subdiv_holidays[subdiv], dt)
            self.assertHolidayName(name_king, self.subdiv_holidays[subdiv], "2023-06-12")

        dt = (
            "2000-06-12",
            "2010-06-14",
            "2012-10-01",
            "2016-10-03",
            "2017-10-02",
            "2018-10-01",
            "2019-10-07",
            "2020-10-05",
            "2021-10-04",
            "2022-10-03",
        )
        self.assertHolidayName(name_queen, self.subdiv_holidays["QLD"], dt)
        self.assertHolidayName(
            "Queen's Diamond Jubilee", self.subdiv_holidays["QLD"], "2012-06-11"
        )
        self.assertHolidayName(name_king, self.subdiv_holidays["QLD"], "2023-10-02")

        dt = (
            "2000-09-25",
            "2010-09-27",
            "2018-10-01",
            "2019-09-30",
            "2020-09-28",
            "2021-09-27",
            "2022-09-26",
        )
        self.assertHolidayName(name_queen, self.subdiv_holidays["WA"], dt)
        self.assertHolidayName(name_king, self.subdiv_holidays["WA"], "2023-09-25")

    def test_canberra_day(self):
        name = "Canberra Day"
        self.assertHolidayName(
            name, self.subdiv_holidays["ACT"], (f"{year}-03-12" for year in range(1913, 1958))
        )
        dt = (
            "1958-03-17",
            "2000-03-20",
            "2007-03-19",
            "2008-03-10",
            "2010-03-08",
            "2012-03-12",
            "2018-03-12",
            "2019-03-11",
            "2020-03-09",
            "2021-03-08",
            "2022-03-14",
        )
        self.assertHolidayName(name, self.subdiv_holidays["ACT"], dt)
        self.assertNoHolidayName(name, self.subdiv_holidays["ACT"], range(1900, 1913))
        self.assertNoHolidayName(name)
        for subdiv in set(Australia.subdivisions) - {"ACT"}:
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

    def test_family_and_community_day(self):
        name = "Family & Community Day"
        dt = (
            "2007-11-06",
            "2008-11-04",
            "2009-11-03",
            "2010-09-26",
            "2011-10-10",
            "2012-10-08",
            "2013-09-30",
            "2014-09-29",
            "2015-09-28",
            "2016-09-26",
            "2017-09-25",
        )
        self.assertHolidayName(name, self.subdiv_holidays["ACT"], dt)
        self.assertNoHolidayName(
            name, self.subdiv_holidays["ACT"], range(1900, 2007), range(2018, 2050)
        )
        self.assertNoHolidayName(name)
        for subdiv in set(Australia.subdivisions) - {"ACT"}:
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

    def test_reconciliation_day(self):
        name = "Reconciliation Day"
        dt = (
            "2018-05-28",
            "2019-05-27",
            "2020-06-01",
            "2021-05-31",
            "2022-05-30",
        )
        self.assertHolidayName(name, self.subdiv_holidays["ACT"], dt)
        self.assertNoHolidayName(name, self.subdiv_holidays["ACT"], range(1900, 2018))
        self.assertNoHolidayName(name)
        for subdiv in set(Australia.subdivisions) - {"ACT"}:
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

    def test_bank_holiday(self):
        name = "Bank Holiday"
        dt = (
            "2000-08-07",
            "2010-08-02",
            "2018-08-06",
            "2019-08-05",
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
        )
        self.assertHolidayName(name, self.subdiv_holidays["NSW"], dt)
        self.assertNoHolidayName(name, self.subdiv_holidays["NSW"], range(1900, 1912))
        self.assertNoHolidayName(name)
        for subdiv in set(Australia.subdivisions) - {"NSW"}:
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

    def test_picnic_day(self):
        name = "Picnic Day"
        dt = (
            "2000-08-07",
            "2010-08-02",
            "2018-08-06",
            "2019-08-05",
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
        )
        self.assertHolidayName(name, self.subdiv_holidays["NT"], dt)
        self.assertHolidayName(name, self.subdiv_holidays["NT"], range(1900, 2050))
        self.assertNoHolidayName(name)
        for subdiv in set(Australia.subdivisions) - {"NT"}:
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

    def test_royal_queensland_show(self):
        name = "The Royal Queensland Show"
        dt = (
            "2000-08-16",
            "2010-08-11",
            "2018-08-15",
            "2019-08-14",
            "2020-08-14",
            "2021-10-29",
            "2022-08-10",
        )
        self.assertHolidayName(name, self.subdiv_holidays["QLD"], dt)
        self.assertHolidayName(name, self.subdiv_holidays["QLD"], range(1900, 2050))
        self.assertNoHolidayName(name)
        for subdiv in set(Australia.subdivisions) - {"QLD"}:
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

    def test_adelaide_cup(self):
        name = "Adelaide Cup"
        dt = (
            "2000-03-20",
            "2005-03-21",
            "2006-03-13",
            "2018-03-12",
            "2019-03-11",
            "2020-03-09",
            "2021-03-08",
            "2022-03-14",
        )
        self.assertHolidayName(name, self.subdiv_holidays["SA"], dt)
        self.assertHolidayName(name, self.subdiv_holidays["SA"], range(1900, 2050))
        self.assertNoHolidayName(name)
        for subdiv in set(Australia.subdivisions) - {"SA"}:
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

    def test_melbourne_cup(self):
        name = "Melbourne Cup"
        dt = (
            "2000-11-07",
            "2010-11-02",
            "2018-11-06",
            "2019-11-05",
            "2020-11-03",
            "2021-11-02",
            "2022-11-01",
        )
        self.assertHolidayName(name, self.subdiv_holidays["VIC"], dt)
        self.assertHolidayName(name, self.subdiv_holidays["VIC"], range(1900, 2050))
        self.assertNoHolidayName(name)
        for subdiv in set(Australia.subdivisions) - {"VIC"}:
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

    def test_grand_final_day(self):
        name = "Grand Final Day"
        dt = (
            "2015-09-25",
            "2016-09-30",
            "2017-09-29",
            "2018-09-28",
            "2019-09-27",
            "2020-10-23",
            "2021-09-24",
            "2022-09-23",
        )
        self.assertHolidayName(name, self.subdiv_holidays["VIC"], dt)
        self.assertHolidayName(name, self.subdiv_holidays["VIC"], range(2015, 2050))
        self.assertNoHolidayName(name, self.subdiv_holidays["VIC"], range(1900, 2015))
        self.assertNoHoliday(self.subdiv_holidays["VIC"], "2020-09-25", "2022-09-30")
        self.assertNoHolidayName(name)
        for subdiv in set(Australia.subdivisions) - {"VIC"}:
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

    def test_western_australia_day(self):
        name_1 = "Foundation Day"
        name_2 = "Western Australia Day"
        dt_1 = (
            "2000-06-05",
            "2005-06-06",
            "2010-06-07",
            "2011-06-06",
            "2012-06-04",
            "2013-06-03",
            "2014-06-02",
        )
        dt_2 = (
            "2015-06-01",
            "2016-06-06",
            "2017-06-05",
            "2018-06-04",
            "2019-06-03",
            "2020-06-01",
            "2021-06-07",
            "2022-06-06",
        )
        self.assertHolidayName(name_1, self.subdiv_holidays["WA"], dt_1)
        self.assertHolidayName(name_2, self.subdiv_holidays["WA"], dt_2)
        self.assertNoHolidayName(name_1, self.subdiv_holidays["WA"], range(2015, 2050))
        self.assertNoHolidayName(name_2, self.subdiv_holidays["WA"], range(1900, 2015))
        self.assertNoHolidayName(name_1, Australia(subdiv="WA", years=1832))
        self.assertNoHolidayName(name_1)
        self.assertNoHolidayName(name_2)

        for subdiv in set(Australia.subdivisions) - {"WA"}:
            self.assertNoHolidayName(name_1, self.subdiv_holidays[subdiv])
            self.assertNoHolidayName(name_2, self.subdiv_holidays[subdiv])

    def test_national_day_of_mourning_for_queen_elizabeth_II(self):
        name = "National Day of Mourning for Queen Elizabeth II"
        dt = "2022-09-22"
        self.assertHolidayName(name, dt)
        for subdiv in Australia.subdivisions:
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], dt)

    def test_all_holidays(self):
        holidays_found = set()
        for subdiv in Australia.subdivisions:
            holidays_found.update(
                Australia(subdiv=subdiv, observed=False, years=(1957, 2012, 2015)).values()
            )
        all_holidays = {
            "New Year's Day",
            "Australia Day",
            "Adelaide Cup",
            "Canberra Day",
            "Good Friday",
            "Easter Saturday",
            "Easter Sunday",
            "Easter Monday",
            "Anzac Day",
            "Queen's Birthday",
            "Queen's Diamond Jubilee",
            "Bank Holiday",
            "The Royal Queensland Show",
            "Western Australia Day",
            "Foundation Day",
            "Family & Community Day",
            "Labour Day",
            "Eight Hours Day",
            "May Day",
            "Picnic Day",
            "Melbourne Cup",
            "Grand Final Day",
            "Christmas Day",
            "Proclamation Day",
            "Boxing Day",
        }
        self.assertEqual(all_holidays, holidays_found)
