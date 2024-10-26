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

from datetime import date
from unittest import TestCase

from holidays.calendars.gregorian import JAN, MAR, APR, MAY, JUN, AUG, SEP, OCT, NOV, DEC
from holidays.constants import BANK, HALF_DAY, PUBLIC
from holidays.countries.australia import Australia, AU, AUS
from tests.common import CommonCountryTests


class TestAustralia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1900, 2050)
        super().setUpClass(Australia, years=years)
        cls.subdiv_holidays = {
            subdiv: Australia(subdiv=subdiv, years=years) for subdiv in Australia.subdivisions
        }

    def _assertVariableDays(self, year: int, subdiv_holidays: dict):  # noqa: N802
        observed_prov_holidays = {
            subdiv: Australia(subdiv=subdiv, years=year) for subdiv in Australia.subdivisions
        }
        for hol_date, hol_provs in subdiv_holidays.items():
            dt = date(year, *hol_date)
            for subdiv, prov_holidays in observed_prov_holidays.items():
                self.assertEqual(
                    dt in prov_holidays,
                    subdiv in hol_provs,
                    f"Failed date `{dt:%Y-%m-%d}`, "
                    f"province `{subdiv}`: {', '.join(hol_provs)}",
                )

    def test_country_aliases(self):
        self.assertAliases(Australia, AU, AUS)

    def test_new_years(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1900, 2050)))
        for holidays in self.subdiv_holidays.values():
            self.assertHolidayName(name, holidays, range(1900, 2050))

    def test_australia_day(self):
        name_1 = "Anniversary Day"
        name_2 = "Australia Day"
        self.assertHolidayName(name_2, (f"{year}-01-26" for year in range(1935, 2050)))
        self.assertNoHolidayName(name_2, range(1900, 1935))
        self.assertNoHoliday(f"{year}-01-26" for year in range(1900, 1935))

        for subdiv in set(Australia.subdivisions) - {"NSW", "SA"}:
            self.assertHolidayName(
                name_1,
                self.subdiv_holidays[subdiv],
                range(1900, 1935),
            )
            self.assertHolidayName(
                name_2,
                self.subdiv_holidays[subdiv],
                range(1935, 2050),
            )
            self.assertNoHolidayName(name_1, self.subdiv_holidays[subdiv], range(1935, 2050))
            self.assertNoHolidayName(name_2, self.subdiv_holidays[subdiv], range(1900, 1935))
            self.assertNoHolidayName(name_1, Australia(subdiv=subdiv, years=1887))

        nsw_holidays = self.subdiv_holidays["NSW"]
        self.assertHolidayName(name_1, nsw_holidays, range(1900, 1946))
        self.assertHolidayName(name_2, nsw_holidays, range(1946, 2050))
        self.assertNoHolidayName(name_1, nsw_holidays, range(1946, 2050))
        self.assertNoHolidayName(name_2, nsw_holidays, range(1900, 1946))
        self.assertNoHolidayName(name_1, Australia(subdiv="NSW", years=1887))

        sa_holidays = self.subdiv_holidays["SA"]
        self.assertHolidayName(name_2, sa_holidays, range(1935, 2050))
        self.assertNoHolidayName(name_2, sa_holidays, range(1900, 1935))
        self.assertNoHolidayName(name_1, sa_holidays)

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
            "2023-04-07",
            "2024-03-29",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(1900, 2050))
        for holidays in self.subdiv_holidays.values():
            self.assertHolidayName(name, holidays, dt)
            self.assertHolidayName(name, holidays, range(1900, 2050))

    def test_easter_saturday(self):
        name = "Easter Saturday"
        self.assertNoHolidayName(name)

        for subdiv in (
            "ACT",
            "NSW",
            "NT",
            "QLD",
            "SA",
        ):
            self.assertHolidayName(name, self.subdiv_holidays[subdiv], range(1900, 2050))

        vic_holidays = self.subdiv_holidays["VIC"]
        self.assertHolidayName(name, vic_holidays, range(2003, 2050))
        self.assertNoHolidayName(name, vic_holidays, range(1900, 2003))

        for subdiv in ("TAS", "WA"):
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

    def test_easter_sunday(self):
        name = "Easter Sunday"
        self.assertNoHolidayName(name)

        start_years = {
            "ACT": 2016,
            "NSW": 2011,
            "NT": 2024,
            "QLD": 2017,
            "SA": 2024,
            "VIC": 2016,
            "WA": 2022,
        }
        for subdiv, holidays in self.subdiv_holidays.items():
            start_year = start_years.get(subdiv)
            if start_year:
                self.assertHolidayName(name, holidays, range(start_year, 2050))
                self.assertNoHolidayName(name, holidays, range(1900, start_year))
            else:
                self.assertNoHolidayName(name, holidays)

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
            "2023-04-10",
            "2024-04-01",
        )
        self.assertHolidayName(name, dt)
        self.assertHolidayName(name, range(1900, 2050))
        for holidays in self.subdiv_holidays.values():
            self.assertHolidayName(name, holidays, dt)
            self.assertHolidayName(name, holidays, range(1900, 2050))

    def test_anzac_day(self):
        name = "ANZAC Day"
        self.assertHolidayName(name, (f"{year}-04-25" for year in range(1921, 2050)))
        self.assertNoHolidayName(name, range(1900, 1921))
        for holidays in self.subdiv_holidays.values():
            self.assertHolidayName(name, holidays, range(1921, 2050))
            self.assertNoHolidayName(name, holidays, range(1900, 1921))

    def test_labour_day(self):
        name = "Labour Day"
        self.assertNoHolidayName(name)

        names = {"NT": "May Day", "TAS": "Eight Hours Day"}
        for subdiv, holidays in self.subdiv_holidays.items():
            self.assertHolidayName(names.get(subdiv, name), holidays, range(1900, 2050))

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

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1900, 2050)))

        for holidays in self.subdiv_holidays.values():
            self.assertHolidayName(name, holidays, range(1900, 2050))

    def test_boxing_day(self):
        name_common = "Boxing Day"
        name_sa = "Proclamation Day"
        self.assertHolidayName(name_common, (f"{year}-12-26" for year in range(1900, 2050)))

        for subdiv, holidays in self.subdiv_holidays.items():
            name = name_sa if subdiv == "SA" else name_common
            self.assertHolidayName(name, holidays, range(1900, 2050))

    def test_canberra_day(self):
        name = "Canberra Day"
        self.assertNoHolidayName(name)

        act_holidays = self.subdiv_holidays["ACT"]
        self.assertHolidayName(name, act_holidays, (f"{year}-03-12" for year in range(1913, 1959)))
        dt = (
            "1959-03-16",
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
            "2023-03-13",
            "2024-03-11",
        )
        self.assertHolidayName(name, act_holidays, dt)
        self.assertNoHolidayName(name, act_holidays, range(1900, 1913))
        for subdiv in set(Australia.subdivisions) - {"ACT"}:
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

    def test_family_and_community_day(self):
        name = "Family & Community Day"
        self.assertNoHolidayName(name)

        act_holidays = self.subdiv_holidays["ACT"]
        dt = (
            "2010-09-26",
            "2011-10-10",
            "2012-10-08",
            "2013-09-30",
            "2014-09-29",
            "2015-09-28",
            "2016-09-26",
            "2017-09-25",
        )
        self.assertHolidayName(name, act_holidays, dt)
        self.assertNoHolidayName(name, act_holidays, range(1900, 2010), range(2018, 2050))
        for subdiv in set(Australia.subdivisions) - {"ACT"}:
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

    def test_reconciliation_day(self):
        name = "Reconciliation Day"
        self.assertNoHolidayName(name)

        act_holidays = self.subdiv_holidays["ACT"]
        dt = (
            "2018-05-28",
            "2019-05-27",
            "2020-06-01",
            "2021-05-31",
            "2022-05-30",
            "2023-05-29",
            "2024-05-27",
        )
        self.assertHolidayName(name, act_holidays, dt)
        self.assertNoHolidayName(name, act_holidays, range(1900, 2018))
        for subdiv in set(Australia.subdivisions) - {"ACT"}:
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

    def test_bank_holiday(self):
        name = "Bank Holiday"
        self.assertNoHolidayName(name)

        nsw_holidays = self.subdiv_holidays["NSW"]
        dt = (
            "2000-08-07",
            "2007-08-06",
            "2008-08-04",
            "2009-08-03",
            "2010-08-02",
        )
        dt_bank = (
            "2018-08-06",
            "2019-08-05",
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
        )
        self.assertHolidayName(name, nsw_holidays, dt)
        self.assertNoHolidayName(name, nsw_holidays, range(1900, 1912), range(2011, 2050))
        for subdiv in set(Australia.subdivisions) - {"NSW"}:
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])
        self.assertHolidayName(name, Australia(subdiv="NSW", categories=BANK), dt_bank)

    def test_picnic_day(self):
        name = "Picnic Day"
        self.assertNoHolidayName(name)

        nt_holidays = self.subdiv_holidays["NT"]
        dt = (
            "2000-08-07",
            "2010-08-02",
            "2018-08-06",
            "2019-08-05",
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
        )
        self.assertHolidayName(name, nt_holidays, dt)
        self.assertHolidayName(name, nt_holidays, range(1900, 2050))
        for subdiv in set(Australia.subdivisions) - {"NT"}:
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

    def test_royal_queensland_show(self):
        name = "The Royal Queensland Show"
        self.assertNoHolidayName(name)

        qld_holidays = self.subdiv_holidays["QLD"]
        dt = (
            "2000-08-16",
            "2010-08-11",
            "2018-08-15",
            "2019-08-14",
            "2020-08-14",
            "2021-10-29",
            "2022-08-10",
            "2023-08-16",
            "2024-08-14",
        )
        self.assertHolidayName(name, qld_holidays, dt)
        self.assertHolidayName(name, qld_holidays, range(1900, 2050))
        for subdiv in set(Australia.subdivisions) - {"QLD"}:
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

    def test_adelaide_cup_day(self):
        name = "Adelaide Cup Day"
        self.assertNoHolidayName(name)

        sa_holidays = self.subdiv_holidays["SA"]
        dt = (
            "2000-05-15",
            "2005-05-16",
            "2006-03-13",
            "2018-03-12",
            "2019-03-11",
            "2020-03-09",
            "2021-03-08",
            "2022-03-14",
            "2023-03-13",
            "2024-03-11",
        )
        self.assertHolidayName(name, sa_holidays, dt)
        self.assertHolidayName(name, sa_holidays, range(1973, 2050))
        self.assertNoHolidayName(name, sa_holidays, range(1900, 1973))
        for subdiv in set(Australia.subdivisions) - {"SA"}:
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

    def test_melbourne_cup_day(self):
        name = "Melbourne Cup Day"
        self.assertNoHolidayName(name)

        vic_holidays = self.subdiv_holidays["VIC"]
        dt = (
            "2009-11-03",
            "2010-11-02",
            "2018-11-06",
            "2019-11-05",
            "2020-11-03",
            "2021-11-02",
            "2022-11-01",
            "2023-11-07",
            "2024-11-05",
        )
        self.assertHolidayName(name, vic_holidays, dt)
        self.assertHolidayName(name, vic_holidays, range(2009, 2050))
        self.assertNoHolidayName(name, vic_holidays, range(1900, 2009))
        for subdiv in set(Australia.subdivisions) - {"VIC"}:
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

    def test_grand_final_day(self):
        name = "Grand Final Day"
        self.assertNoHolidayName(name)

        vic_holidays = self.subdiv_holidays["VIC"]
        dt = (
            "2015-10-02",
            "2016-09-30",
            "2017-09-29",
            "2018-09-28",
            "2019-09-27",
            "2020-10-23",
            "2021-09-24",
            "2022-09-23",
            "2023-09-29",
            "2024-09-27",
        )
        self.assertHolidayName(name, vic_holidays, dt)
        self.assertHolidayName(name, vic_holidays, range(2015, 2050))
        self.assertNoHolidayName(name, vic_holidays, range(1900, 2015))
        for subdiv in set(Australia.subdivisions) - {"VIC"}:
            self.assertNoHolidayName(name, self.subdiv_holidays[subdiv])

    def test_western_australia_day(self):
        name_1 = "Foundation Day"
        name_2 = "Western Australia Day"
        self.assertNoHolidayName(name_1)
        self.assertNoHolidayName(name_2)

        wa_holidays = self.subdiv_holidays["WA"]
        dt_1 = (
            "2000-06-05",
            "2005-06-06",
            "2010-06-07",
            "2011-06-06",
        )
        dt_2 = (
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
        )
        self.assertHolidayName(name_1, wa_holidays, dt_1)
        self.assertHolidayName(name_2, wa_holidays, dt_2)
        self.assertNoHolidayName(name_1, wa_holidays, range(2012, 2050))
        self.assertNoHolidayName(name_2, wa_holidays, range(1900, 2012))
        self.assertNoHolidayName(name_1, Australia(subdiv="WA", years=1832))

        for subdiv in set(Australia.subdivisions) - {"WA"}:
            self.assertNoHolidayName(name_1, self.subdiv_holidays[subdiv])
            self.assertNoHolidayName(name_2, self.subdiv_holidays[subdiv])

    def test_national_day_of_mourning_for_queen_elizabeth_ii(self):
        name = "National Day of Mourning for Queen Elizabeth II"
        dt = "2022-09-22"
        self.assertHolidayName(name, dt)
        for holidays in self.subdiv_holidays.values():
            self.assertHolidayName(name, holidays, dt)

    def test_special_holidays(self):
        act_holidays = self.subdiv_holidays["ACT"]
        qld_holidays = self.subdiv_holidays["QLD"]
        wa_holidays = self.subdiv_holidays["WA"]
        self.assertHoliday(act_holidays, "2020-04-20", "2021-04-25")
        self.assertHoliday(qld_holidays, "2010-12-28", "2011-01-03", "2012-06-11")
        self.assertNoNonObservedHoliday(
            Australia(subdiv="QLD", observed=False, years=(2010, 2011)), "2010-12-28", "2011-01-03"
        )
        self.assertHoliday(wa_holidays, "2011-04-26")

    def test_all_holidays(self):
        holidays_found = set()
        for subdiv in Australia.subdivisions:
            holidays_found.update(
                Australia(
                    categories=(BANK, HALF_DAY, PUBLIC),
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
            "Christmas Eve (from 7pm)",
            "New Year's Eve (from 7pm)",
        }
        self.assertEqual(all_holidays, holidays_found)

    def test_holidays_2019(self):
        province_days = {
            (JAN, 1): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (JAN, 28): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (MAR, 4): {"WA"},
            (MAR, 11): {"ACT", "SA", "TAS", "VIC"},
            (APR, 19): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (APR, 20): {"ACT", "NSW", "NT", "QLD", "SA", "VIC"},
            (APR, 21): {"ACT", "NSW", "QLD", "VIC"},
            (APR, 22): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (APR, 25): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (MAY, 6): {"NT", "QLD"},
            (MAY, 27): {"ACT"},
            (JUN, 3): {"WA"},
            (JUN, 10): {"ACT", "NSW", "NT", "SA", "TAS", "VIC"},
            (AUG, 5): {"NT"},
            (AUG, 14): {"QLD"},
            (SEP, 27): {"VIC"},
            (SEP, 30): {"WA"},
            (OCT, 7): {"ACT", "NSW", "QLD", "SA"},
            (NOV, 5): {"VIC"},
            (DEC, 25): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (DEC, 26): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
        }
        self._assertVariableDays(2019, province_days)

    def test_holidays_2020(self):
        province_days = {
            (JAN, 1): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (JAN, 26): {"SA"},
            (JAN, 27): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (MAR, 2): {"WA"},
            (MAR, 9): {"ACT", "SA", "TAS", "VIC"},
            (APR, 10): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (APR, 11): {"ACT", "NSW", "NT", "QLD", "SA", "VIC"},
            (APR, 12): {"ACT", "NSW", "QLD", "VIC"},
            (APR, 13): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (APR, 25): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (APR, 27): {"WA"},
            (MAY, 4): {"NT", "QLD"},
            (JUN, 1): {"ACT", "WA"},
            (JUN, 8): {"ACT", "NSW", "NT", "SA", "TAS", "VIC"},
            (AUG, 3): {"NT"},
            (AUG, 14): {"QLD"},
            (SEP, 28): {"WA"},
            (OCT, 5): {"ACT", "NSW", "QLD", "SA"},
            (OCT, 23): {"VIC"},
            (NOV, 3): {"VIC"},
            (DEC, 25): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (DEC, 26): {"ACT", "NSW", "QLD", "VIC", "WA"},
            (DEC, 28): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
        }
        self._assertVariableDays(2020, province_days)

    def test_holidays_2021(self):
        province_days = {
            (JAN, 1): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (JAN, 26): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (MAR, 1): {"WA"},
            (MAR, 8): {"ACT", "SA", "TAS", "VIC"},
            (APR, 2): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (APR, 3): {"ACT", "NSW", "NT", "QLD", "SA", "VIC"},
            (APR, 4): {"ACT", "NSW", "QLD", "VIC"},
            (APR, 5): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (APR, 25): {"ACT", "NSW", "SA", "TAS", "VIC", "WA"},
            (APR, 26): {"ACT", "NT", "QLD", "SA", "WA"},
            (MAY, 3): {"NT", "QLD"},
            (MAY, 31): {"ACT"},
            (JUN, 7): {"WA"},
            (JUN, 14): {"ACT", "NSW", "NT", "SA", "TAS", "VIC"},
            (AUG, 2): {"NT"},
            (SEP, 24): {"VIC"},
            (SEP, 27): {"WA"},
            (OCT, 4): {"ACT", "NSW", "QLD", "SA"},
            (OCT, 29): {"QLD"},
            (NOV, 2): {"VIC"},
            (DEC, 25): {"ACT", "NSW", "NT", "QLD", "TAS", "VIC", "WA"},
            (DEC, 26): {"ACT", "NSW", "QLD", "SA", "VIC", "WA"},
            (DEC, 27): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (DEC, 28): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
        }
        self._assertVariableDays(2021, province_days)

    def test_holidays_2022(self):
        province_days = {
            (JAN, 1): {"ACT", "NSW", "NT", "QLD", "VIC", "WA"},
            (JAN, 3): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (JAN, 26): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (MAR, 7): {"WA"},
            (MAR, 14): {"ACT", "SA", "TAS", "VIC"},
            (APR, 15): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (APR, 16): {"ACT", "NSW", "NT", "QLD", "SA", "VIC"},
            (APR, 17): {"ACT", "NSW", "QLD", "VIC", "WA"},
            (APR, 18): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (APR, 25): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (MAY, 2): {"NT", "QLD"},
            (MAY, 30): {"ACT"},
            (JUN, 6): {"WA"},
            (JUN, 13): {"ACT", "NSW", "NT", "SA", "TAS", "VIC"},
            (AUG, 1): {"NT"},
            (AUG, 10): {"QLD"},
            (SEP, 22): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (SEP, 23): {"VIC"},
            (SEP, 26): {"WA"},
            (OCT, 3): {"ACT", "NSW", "QLD", "SA"},
            (NOV, 1): {"VIC"},
            (DEC, 25): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (DEC, 26): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (DEC, 27): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
        }
        self._assertVariableDays(2022, province_days)

    def test_holidays_2023(self):
        province_days = {
            (JAN, 1): {"ACT", "NSW", "NT", "QLD", "SA", "VIC", "WA"},
            (JAN, 2): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (JAN, 26): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (MAR, 6): {"WA"},
            (MAR, 13): {"ACT", "SA", "TAS", "VIC"},
            (APR, 7): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (APR, 8): {"ACT", "NSW", "NT", "QLD", "SA", "VIC"},
            (APR, 9): {"ACT", "NSW", "QLD", "VIC", "WA"},
            (APR, 10): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (APR, 25): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (MAY, 1): {"NT", "QLD"},
            (MAY, 29): {"ACT"},
            (JUN, 5): {"WA"},
            (JUN, 12): {"ACT", "NSW", "NT", "SA", "TAS", "VIC"},
            (AUG, 7): {"NT"},
            (AUG, 16): {"QLD"},
            (SEP, 29): {"VIC"},
            (SEP, 25): {"WA"},
            (OCT, 2): {"ACT", "NSW", "QLD", "SA"},
            (NOV, 7): {"VIC"},
            (DEC, 25): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (DEC, 26): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
        }
        self._assertVariableDays(2023, province_days)

    def test_holidays_2024(self):
        province_days = {
            (JAN, 1): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (JAN, 26): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (MAR, 4): {"WA"},
            (MAR, 11): {"ACT", "SA", "TAS", "VIC"},
            (MAR, 29): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (MAR, 30): {"ACT", "NSW", "NT", "QLD", "SA", "VIC"},
            (MAR, 31): {"ACT", "NSW", "NT", "QLD", "SA", "VIC", "WA"},
            (APR, 1): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (APR, 25): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (MAY, 6): {"NT", "QLD"},
            (MAY, 27): {"ACT"},
            (JUN, 3): {"WA"},
            (JUN, 10): {"ACT", "NSW", "NT", "SA", "TAS", "VIC"},
            (AUG, 5): {"NT"},
            (AUG, 14): {"QLD"},
            (SEP, 27): {"VIC"},
            (SEP, 23): {"WA"},
            (OCT, 7): {"ACT", "NSW", "QLD", "SA"},
            (NOV, 5): {"VIC"},
            (DEC, 25): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
            (DEC, 26): {"ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"},
        }
        self._assertVariableDays(2024, province_days)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-26", "Australia Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-25", "ANZAC Day"),
            ("2022-09-22", "National Day of Mourning for Queen Elizabeth II"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-26", "Australia Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-04-25", "ANZAC Day"),
            ("2022-09-22", "National Day of Mourning for Queen Elizabeth II"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-26", "วันชาติออสเตรเลีย"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-04-25", "วันแอนแซค"),
            ("2022-09-22", "วันไว้ทุกข์แห่งชาติแด่สมเด็จพระราชินีนาถเอลิซาเบธที่ 2"),
            ("2022-12-25", "วันคริสต์มาส"),
            ("2022-12-26", "วันเปิดกล่องของขวัญ"),
        )
