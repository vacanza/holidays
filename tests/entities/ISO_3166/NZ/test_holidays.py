#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.entities.ISO_3166.NZ import NzHolidays
from tests.common import CommonCountryTests


class TestNZ(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            NzHolidays, years=range(1900, 2050), years_non_observed=range(2000, 2024)
        )

    def test_no_holidays(self):
        self.assertNoHolidays(NzHolidays(years=1893))

    def test_new_years(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1900, 2050)))
        years_observed = (2005, 2006, 2011, 2012, 2017)
        self.assertHolidayName(f"{name} (observed)", (f"{year}-01-03" for year in years_observed))
        self.assertNoNonObservedHoliday(f"{year}-01-03" for year in years_observed)

    def test_day_after_new_years(self):
        name = "Day after New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-02" for year in range(1900, 2050)))
        years_observed = (2010, 2011, 2016, 2021, 2022)
        self.assertHolidayName(f"{name} (observed)", (f"{year}-01-04" for year in years_observed))
        self.assertNoNonObservedHoliday(f"{year}-01-04" for year in years_observed)

    def test_waitangi_day(self):
        name1 = "New Zealand Day"
        name2 = "Waitangi Day"
        self.assertHolidayName(
            name2,
            NzHolidays(subdiv="NTL"),
            "1964-02-03",
            "1965-02-08",
            "1966-02-07",
            "1967-02-06",
            "1968-02-05",
        )

        self.assertNoHolidayName(name1, range(1900, 1974))
        self.assertNoHolidayName(name2, range(1900, 1977))
        self.assertNoHoliday(f"{year}-02-06" for year in range(1900, 1974))
        self.assertHolidayName(name1, (f"{year}-02-06" for year in range(1974, 1977)))
        self.assertHolidayName(name2, (f"{year}-02-06" for year in range(1977, 2050)))
        obs_dt = ("2016-02-08", "2021-02-08", "2022-02-07")
        self.assertHolidayName(f"{name2} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_good_friday(self):
        self.assertHoliday(
            "1999-04-02",
            "2000-04-21",
            "2010-04-02",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
        )

    def test_easter_monday(self):
        self.assertHoliday(
            "1999-04-05",
            "2000-04-24",
            "2010-04-05",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
        )

    def test_anzac_day(self):
        name = "Anzac Day"
        self.assertHolidayName(name, (f"{year}-04-25" for year in range(1921, 2050)))
        obs_dt = ("2015-04-27", "2020-04-27", "2021-04-26")
        self.assertHolidayName(f"{name} (observed)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        self.assertNoHolidayName(name, range(1900, 1921))
        self.assertNoHoliday(f"{year}-04-25" for year in range(1900, 1921))

    def test_sovereigns_birthday(self):
        name1 = "King's Birthday"
        name2 = "Queen's Birthday"

        self.assertHoliday(
            "1909-11-09",
            "1936-06-23",
            "1937-06-09",
            "1940-06-03",
            "1952-06-02",
            "2023-06-05",
        )
        self.assertHolidayName(name1, (f"{year}-06-03" for year in range(1912, 1936)))

        self.assertHolidayName(
            name2,
            "2001-06-04",
            "2002-06-03",
            "2003-06-02",
            "2004-06-07",
            "2005-06-06",
            "2006-06-05",
            "2007-06-04",
            "2008-06-02",
            "2009-06-01",
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
        )

        self.assertNoHolidayName(name1, range(1952, 2023))
        self.assertNoHolidayName(name2, range(1900, 1952), range(2023, 2050))

    def test_matariki(self):
        self.assertHolidayName(
            "Matariki",
            "2022-06-24",
            "2023-07-14",
            "2024-06-28",
            "2025-06-20",
            "2026-07-10",
            "2027-06-25",
            "2028-07-14",
            "2029-07-06",
            "2030-06-21",
            "2031-07-11",
            "2032-07-02",
            "2033-06-24",
            "2034-07-07",
            "2035-06-29",
            "2036-07-18",
            "2037-07-10",
            "2038-06-25",
            "2039-07-15",
            "2040-07-06",
            "2041-07-19",
            "2042-07-11",
            "2043-07-03",
            "2044-06-24",
            "2045-07-07",
            "2046-06-29",
            "2047-07-19",
            "2048-07-03",
            "2049-06-25",
            "2050-07-15",
            "2051-06-30",
            "2052-06-21",
        )

    def test_labour_day(self):
        name = "Labour Day"
        self.assertHolidayName(
            name,
            "2001-10-22",
            "2002-10-28",
            "2003-10-27",
            "2004-10-25",
            "2005-10-24",
            "2006-10-23",
            "2007-10-22",
            "2008-10-27",
            "2009-10-26",
            "2010-10-25",
            "2011-10-24",
            "2012-10-22",
            "2013-10-28",
            "2014-10-27",
            "2015-10-26",
            "2016-10-24",
            "2017-10-23",
            "2018-10-22",
            "2019-10-28",
            "2020-10-26",
            "2021-10-25",
            "2022-10-24",
        )
        self.assertNoHolidayName(name, NzHolidays(years=1899))

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1900, 2050)))
        years_observed = (2004, 2005, 2010, 2011, 2016, 2021, 2022)
        self.assertHolidayName(f"{name} (observed)", (f"{year}-12-27" for year in years_observed))
        self.assertNoNonObservedHoliday(f"{year}-12-27" for year in years_observed)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1900, 2050)))
        years_observed = (2004, 2009, 2010, 2015, 2020, 2021)
        self.assertHolidayName(f"{name} (observed)", (f"{year}-12-28" for year in years_observed))
        self.assertNoNonObservedHoliday(f"{year}-12-28" for year in years_observed)

    def test_auckland_anniversary_day(self):
        self.assertHolidayName(
            "Auckland Anniversary Day",
            NzHolidays(subdiv="AUK", years=range(2001, 2023)),
            "2001-01-29",
            "2002-01-28",
            "2003-01-27",
            "2004-01-26",
            "2005-01-31",
            "2006-01-30",
            "2007-01-29",
            "2008-01-28",
            "2009-01-26",
            "2010-02-01",
            "2011-01-31",
            "2012-01-30",
            "2013-01-28",
            "2014-01-27",
            "2015-01-26",
            "2016-02-01",
            "2017-01-30",
            "2018-01-29",
            "2019-01-28",
            "2020-01-27",
            "2021-02-01",
            "2022-01-31",
        )

    def test_taranaki_anniversary_day(self):
        self.assertHolidayName(
            "Taranaki Anniversary Day",
            NzHolidays(subdiv="TKI", years=range(2001, 2023)),
            "2001-03-12",
            "2002-03-11",
            "2003-03-10",
            "2004-03-08",
            "2005-03-14",
            "2006-03-13",
            "2007-03-12",
            "2008-03-10",
            "2009-03-09",
            "2010-03-08",
            "2011-03-14",
            "2012-03-12",
            "2013-03-11",
            "2014-03-10",
            "2015-03-09",
            "2016-03-14",
            "2017-03-13",
            "2018-03-12",
            "2019-03-11",
            "2020-03-09",
            "2021-03-08",
            "2022-03-14",
        )

    def test_hawkes_bay_anniversary_day(self):
        self.assertHolidayName(
            "Hawke's Bay Anniversary Day",
            NzHolidays(subdiv="HKB", years=range(2001, 2023)),
            "2001-10-19",
            "2002-10-25",
            "2003-10-24",
            "2004-10-22",
            "2005-10-21",
            "2006-10-20",
            "2007-10-19",
            "2008-10-24",
            "2009-10-23",
            "2010-10-22",
            "2011-10-21",
            "2012-10-19",
            "2013-10-25",
            "2014-10-24",
            "2015-10-23",
            "2016-10-21",
            "2017-10-20",
            "2018-10-19",
            "2019-10-25",
            "2020-10-23",
            "2021-10-22",
            "2022-10-21",
        )

    def test_wellington_anniversary_day(self):
        self.assertHolidayName(
            "Wellington Anniversary Day",
            NzHolidays(subdiv="WGN", years=range(2001, 2023)),
            "2001-01-22",
            "2002-01-21",
            "2003-01-20",
            "2004-01-19",
            "2005-01-24",
            "2006-01-23",
            "2007-01-22",
            "2008-01-21",
            "2009-01-19",
            "2010-01-25",
            "2011-01-24",
            "2012-01-23",
            "2013-01-21",
            "2014-01-20",
            "2015-01-19",
            "2016-01-25",
            "2017-01-23",
            "2018-01-22",
            "2019-01-21",
            "2020-01-20",
            "2021-01-25",
            "2022-01-24",
        )

    def test_marlborough_anniversary_day(self):
        self.assertHolidayName(
            "Marlborough Anniversary Day",
            NzHolidays(subdiv="MBH", years=range(2001, 2023)),
            "2001-10-29",
            "2002-11-04",
            "2003-11-03",
            "2004-11-01",
            "2005-10-31",
            "2006-10-30",
            "2007-10-29",
            "2008-11-03",
            "2009-11-02",
            "2010-11-01",
            "2011-10-31",
            "2012-10-29",
            "2013-11-04",
            "2014-11-03",
            "2015-11-02",
            "2016-10-31",
            "2017-10-30",
            "2018-10-29",
            "2019-11-04",
            "2020-11-02",
            "2021-11-01",
            "2022-10-31",
        )

    def test_nelson_anniversary_day(self):
        self.assertHolidayName(
            "Nelson Anniversary Day",
            NzHolidays(subdiv="NSN", years=range(2001, 2023)),
            "2001-01-29",
            "2002-02-04",
            "2003-02-03",
            "2004-02-02",
            "2005-01-31",
            "2006-01-30",
            "2007-01-29",
            "2008-02-04",
            "2009-02-02",
            "2010-02-01",
            "2011-01-31",
            "2012-01-30",
            "2013-02-04",
            "2014-02-03",
            "2015-02-02",
            "2016-02-01",
            "2017-01-30",
            "2018-01-29",
            "2019-02-04",
            "2020-02-03",
            "2021-02-01",
            "2022-01-31",
        )

    def test_canterbury_anniversary_day(self):
        self.assertHolidayName(
            "Canterbury Anniversary Day",
            NzHolidays(subdiv="CAN", years=range(2001, 2023)),
            "2001-11-16",
            "2002-11-15",
            "2003-11-14",
            "2004-11-12",
            "2005-11-11",
            "2006-11-17",
            "2007-11-16",
            "2008-11-14",
            "2009-11-13",
            "2010-11-12",
            "2011-11-11",
            "2012-11-16",
            "2013-11-15",
            "2014-11-14",
            "2015-11-13",
            "2016-11-11",
            "2017-11-17",
            "2018-11-16",
            "2019-11-15",
            "2020-11-13",
            "2021-11-12",
            "2022-11-11",
        )

    def test_west_coast_anniversary_day(self):
        self.assertHolidayName(
            "West Coast Anniversary Day",
            NzHolidays(subdiv="WTC", years=range(2001, 2023)),
            "2001-12-03",
            "2002-12-02",
            "2003-12-01",
            "2004-11-29",
            "2005-12-05",
            "2006-12-04",
            "2007-12-03",
            "2008-12-01",
            "2009-11-30",
            "2010-11-29",
            "2011-11-28",
            "2012-12-03",
            "2013-12-02",
            "2014-12-01",
            "2015-11-30",
            "2016-11-28",
            "2017-12-04",
            "2018-12-03",
            "2019-12-02",
            "2020-11-30",
            "2021-11-29",
            "2022-11-28",
        )

    def test_otago_anniversary_day(self):
        self.assertHolidayName(
            "Otago Anniversary Day",
            NzHolidays(subdiv="OTA", years=range(2001, 2023)),
            "2001-03-26",
            "2002-03-25",
            "2003-03-24",
            "2004-03-22",
            "2005-03-21",
            "2006-03-20",
            "2007-03-26",
            "2008-03-25",
            "2009-03-23",
            "2010-03-22",
            "2011-03-21",
            "2012-03-26",
            "2013-03-25",
            "2014-03-24",
            "2015-03-23",
            "2016-03-21",
            "2017-03-20",
            "2018-03-26",
            "2019-03-25",
            "2020-03-23",
            "2021-03-22",
            "2022-03-21",
        )

    def test_southland_anniversary_day(self):
        self.assertHolidayName(
            "Southland Anniversary Day",
            NzHolidays(subdiv="STL", years=range(2001, 2023)),
            "2001-01-15",
            "2002-01-14",
            "2003-01-20",
            "2004-01-19",
            "2005-01-17",
            "2006-01-16",
            "2007-01-15",
            "2008-01-14",
            "2009-01-19",
            "2010-01-18",
            "2011-01-17",
            "2012-04-10",
            "2013-04-02",
            "2014-04-22",
            "2015-04-07",
            "2016-03-29",
            "2017-04-18",
            "2018-04-03",
            "2019-04-23",
            "2020-04-14",
            "2021-04-06",
            "2022-04-19",
        )

    def test_chatham_islands_anniversary_day(self):
        self.assertHolidayName(
            "Chatham Islands Anniversary Day",
            NzHolidays(subdiv="CIT", years=range(2001, 2023)),
            "2001-12-03",
            "2002-12-02",
            "2003-12-01",
            "2004-11-29",
            "2005-11-28",
            "2006-11-27",
            "2007-12-03",
            "2008-12-01",
            "2009-11-30",
            "2010-11-29",
            "2011-11-28",
            "2012-12-03",
            "2013-12-02",
            "2014-12-01",
            "2015-11-30",
            "2016-11-28",
            "2017-11-27",
            "2018-12-03",
            "2019-12-02",
            "2020-11-30",
            "2021-11-29",
            "2022-11-28",
        )

    def test_all_holidays_present(self):
        all_subdivisions = set(NzHolidays.subdivisions)
        holidays_1969 = set()
        for p in all_subdivisions:
            holidays_1969.update(NzHolidays(years=1969, subdiv=p, observed=False).values())
        holidays_2015 = set()
        for p in all_subdivisions:
            holidays_2015.update(NzHolidays(years=2015, subdiv=p, observed=False).values())
        holidays_1974 = set()
        for p in all_subdivisions:
            holidays_1974.update(NzHolidays(years=1974, subdiv=p, observed=False).values())
        all_holidays = {
            "New Year's Day",
            "Day after New Year's Day",
            "Waitangi Day",
            "Good Friday",
            "Easter Monday",
            "Anzac Day",
            "Queen's Birthday",
            "Labour Day",
            "Christmas Day",
            "Boxing Day",
            "Auckland Anniversary Day",
            "Taranaki Anniversary Day",
            "Hawke's Bay Anniversary Day",
            "Wellington Anniversary Day",
            "Marlborough Anniversary Day",
            "Nelson Anniversary Day",
            "Canterbury Anniversary Day",
            "West Coast Anniversary Day",
            "Otago Anniversary Day",
            "Southland Anniversary Day",
            "Chatham Islands Anniversary Day",
            "Queen's Birthday",
            "Labour Day",
            "Christmas Day",
            "Boxing Day",
        }
        self.assertEqual(all_holidays, holidays_1969)
        self.assertEqual(all_holidays, holidays_2015)
        all_holidays.remove("Waitangi Day")
        all_holidays.add("New Zealand Day")
        self.assertEqual(all_holidays, holidays_1974)
