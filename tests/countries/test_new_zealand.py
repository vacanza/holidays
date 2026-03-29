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

import warnings
from unittest import TestCase

from holidays.countries.new_zealand import NewZealand
from tests.common import CommonCountryTests


class TestNZ(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full_range = range(1894, 2053)
        super().setUpClass(NewZealand)

    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2005-01-03",
            "2006-01-03",
            "2011-01-03",
            "2012-01-03",
            "2017-01-03",
            "2022-01-03",
            "2023-01-03",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_day_after_new_years_day(self):
        name = "Day after New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-02" for year in self.full_range))
        obs_dts = (
            "2010-01-04",
            "2011-01-04",
            "2016-01-04",
            "2021-01-04",
            "2022-01-04",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_waitangi_day(self):
        name_1974 = "New Zealand Day"
        name_1977 = "Waitangi Day"

        self.assertHolidayName(name_1974, (f"{year}-02-06" for year in range(1974, 1977)))
        self.assertHolidayName(name_1977, (f"{year}-02-06" for year in range(1977, self.end_year)))
        self.assertNoHolidayName(
            name_1974, range(self.start_year, 1974), range(1977, self.end_year)
        )
        self.assertNoHolidayName(name_1977, range(self.start_year, 1977))

        self.assertSubdivNtlHolidayName(
            name_1977,
            "1964-02-03",
            "1965-02-08",
            "1966-02-07",
            "1967-02-06",
            "1968-02-05",
            "1969-02-03",
            "1970-02-09",
            "1971-02-08",
            "1972-02-07",
            "1973-02-05",
        )
        self.assertNoSubdivNtlHolidayName(
            name_1977, range(self.start_year, 1964), range(1974, 1977)
        )

        obs_dts = (
            "2016-02-08",
            "2021-02-08",
            "2022-02-07",
        )
        self.assertHolidayName(f"{name_1977} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_anzac_day(self):
        name = "Anzac Day"
        self.assertHolidayName(name, (f"{year}-04-25" for year in range(1921, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1921))
        obs_dts = (
            "2015-04-27",
            "2020-04-27",
            "2021-04-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_sovereigns_birthday(self):
        name_king = "King's Birthday"
        name_queen = "Queen's Birthday"

        self.assertHolidayName(
            name_king,
            (f"{year}-11-09" for year in range(1902, 1912)),
            (f"{year}-06-03" for year in range(1912, 1936)),
            "1936-06-23",
            "1937-06-09",
            "2023-06-05",
            "2024-06-03",
            "2025-06-02",
        )
        self.assertHolidayName(name_king, range(1936, 1952), range(2023, self.end_year))
        self.assertNoHolidayName(name_king, range(self.start_year, 1902), range(1952, 2023))

        self.assertHolidayName(
            name_queen,
            "1952-06-02",
            "2017-06-05",
            "2018-06-04",
            "2019-06-03",
            "2020-06-01",
            "2021-06-07",
            "2022-06-06",
        )
        self.assertHolidayName(name_queen, range(1952, 2023))
        self.assertNoHolidayName(
            name_queen, range(self.start_year, 1952), range(2023, self.end_year)
        )

    def test_matariki(self):
        name = "Matariki"
        self.assertHolidayName(
            name,
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
        self.assertNoHolidayName(name, range(self.start_year, 2022))

    def test_labor_day(self):
        name = "Labour Day"
        self.assertHolidayName(
            name,
            "1907-10-09",
            "1908-10-14",
            "1909-10-13",
            "2020-10-26",
            "2021-10-25",
            "2022-10-24",
            "2023-10-23",
            "2024-10-28",
            "2025-10-27",
        )
        self.assertHolidayName(name, range(1900, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 1900))

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2004-12-27",
            "2005-12-27",
            "2010-12-27",
            "2011-12-27",
            "2016-12-27",
            "2021-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        obs_dts = (
            "2004-12-28",
            "2009-12-28",
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
            "2021-12-28",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_auckland_anniversary_day(self):
        name = "Auckland Anniversary Day"
        self.assertNoHolidayName(name)
        dts = (
            "2020-01-27",
            "2021-02-01",
            "2022-01-31",
            "2023-01-30",
            "2024-01-29",
            "2025-01-27",
        )
        self.assertSubdivAukHolidayName(name, dts)
        self.assertSubdivAukHolidayName(name, self.full_range)
        self.assertSubdivNtlHolidayName(name, dts)
        self.assertSubdivNtlHolidayName(
            name, range(self.start_year, 1964), range(1974, self.end_year)
        )

    def test_canterbury_anniversary_day(self):
        name = "Canterbury Anniversary Day"
        self.assertNoHolidayName(name)
        self.assertSubdivCanHolidayName(
            name,
            "2020-11-13",
            "2021-11-12",
            "2022-11-11",
            "2023-11-17",
            "2024-11-15",
            "2025-11-14",
        )
        self.assertSubdivCanHolidayName(name, self.full_range)

    def test_chatham_islands_anniversary_day(self):
        name = "Chatham Islands Anniversary Day"
        self.assertNoHolidayName(name)
        self.assertSubdivCitHolidayName(
            name,
            "2020-11-30",
            "2021-11-29",
            "2022-11-28",
            "2023-11-27",
            "2024-12-02",
            "2025-12-01",
        )
        self.assertSubdivCitHolidayName(name, self.full_range)

    def test_hawkes_bay_anniversary_day(self):
        name = "Hawke's Bay Anniversary Day"
        self.assertNoHolidayName(name)
        self.assertSubdivHkbHolidayName(
            name,
            "2020-10-23",
            "2021-10-22",
            "2022-10-21",
            "2023-10-20",
            "2024-10-25",
            "2025-10-24",
        )
        self.assertSubdivHkbHolidayName(name, self.full_range)

    def test_marlborough_anniversary_day(self):
        name = "Marlborough Anniversary Day"
        self.assertNoHolidayName(name)
        self.assertSubdivMbhHolidayName(
            name,
            "2020-11-02",
            "2021-11-01",
            "2022-10-31",
            "2023-10-30",
            "2024-11-04",
            "2025-11-03",
        )
        self.assertSubdivMbhHolidayName(name, self.full_range)

    def test_nelson_anniversary_day(self):
        name = "Nelson Anniversary Day"
        self.assertNoHolidayName(name)
        self.assertSubdivNsnHolidayName(
            name,
            "2020-02-03",
            "2021-02-01",
            "2022-01-31",
            "2023-01-30",
            "2024-01-29",
            "2025-02-03",
        )
        self.assertSubdivNsnHolidayName(name, self.full_range)

    def test_otago_anniversary_day(self):
        name = "Otago Anniversary Day"
        self.assertNoHolidayName(name)
        self.assertSubdivOtaHolidayName(
            name,
            "2020-03-23",
            "2021-03-22",
            "2022-03-21",
            "2023-03-20",
            "2024-03-25",
            "2025-03-24",
        )
        self.assertSubdivOtaHolidayName(name, self.full_range)

    def test_south_canterbury_anniversary_day(self):
        name = "South Canterbury Anniversary Day"
        self.assertNoHolidayName(name)
        self.assertSubdivSouthCanterburyHolidayName(
            name,
            "2020-09-28",
            "2021-09-27",
            "2022-09-26",
            "2023-09-25",
            "2024-09-23",
            "2025-09-22",
        )
        self.assertSubdivSouthCanterburyHolidayName(name, self.full_range)

    def test_southland_anniversary_day(self):
        name = "Southland Anniversary Day"
        self.assertNoHolidayName(name)
        self.assertSubdivStlHolidayName(
            name,
            "2009-01-19",
            "2010-01-18",
            "2011-01-17",
            "2020-04-14",
            "2021-04-06",
            "2022-04-19",
            "2023-04-11",
            "2024-04-02",
            "2025-04-22",
        )
        self.assertSubdivStlHolidayName(name, self.full_range)

    def test_taranaki_anniversary_day(self):
        name = "Taranaki Anniversary Day"
        self.assertNoHolidayName(name)
        self.assertSubdivTkiHolidayName(
            name,
            "2020-03-09",
            "2021-03-08",
            "2022-03-14",
            "2023-03-13",
            "2024-03-11",
            "2025-03-10",
        )
        self.assertSubdivTkiHolidayName(name, self.full_range)

    def test_wellington_anniversary_day(self):
        name = "Wellington Anniversary Day"
        self.assertNoHolidayName(name)
        self.assertSubdivWgnHolidayName(
            name,
            "2020-01-20",
            "2021-01-25",
            "2022-01-24",
            "2023-01-23",
            "2024-01-22",
            "2025-01-20",
        )
        self.assertSubdivWgnHolidayName(name, self.full_range)

    def test_west_coast_anniversary_day(self):
        name = "West Coast Anniversary Day"
        self.assertNoHolidayName(name)
        self.assertSubdivWtcHolidayName(
            name,
            "2020-11-30",
            "2021-11-29",
            "2022-11-28",
            "2023-12-04",
            "2024-12-02",
            "2025-12-01",
        )
        self.assertSubdivWtcHolidayName(name, self.full_range)

    def test_all_holidays_present(self):
        all_subdivisions = set(NewZealand.subdivisions)
        holidays_1969 = set()
        for subdiv in all_subdivisions:
            holidays_1969.update(NewZealand(years=1969, subdiv=subdiv, observed=False).values())
        holidays_2015 = set()
        for subdiv in all_subdivisions:
            holidays_2015.update(NewZealand(years=2015, subdiv=subdiv, observed=False).values())
        holidays_1974 = set()
        for subdiv in all_subdivisions:
            holidays_1974.update(NewZealand(years=1974, subdiv=subdiv, observed=False).values())

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
            "South Canterbury Anniversary Day",
            "West Coast Anniversary Day",
            "Otago Anniversary Day",
            "Southland Anniversary Day",
            "Chatham Islands Anniversary Day",
        }
        self.assertEqual(all_holidays, holidays_1969)
        self.assertEqual(all_holidays, holidays_2015)
        all_holidays.remove("Waitangi Day")
        all_holidays.add("New Zealand Day")
        self.assertEqual(all_holidays, holidays_1974)

    def test_deprecated(self):
        # Deprecated Code, Remapped Code.
        for subdiv1, subdiv2 in (
            ("New Plymouth", "TKI"),
            ("STC", "South Canterbury"),
            ("Westland", "WTC"),
            ("WTL", "WTC"),
        ):
            self.assertEqual(
                NewZealand(subdiv=subdiv1, years=2022).keys(),
                NewZealand(subdiv=subdiv2, years=2022).keys(),
            )

    def test_subdiv_deprecation(self):
        self.assertDeprecatedSubdivisions("This subdivision is deprecated and will be removed")
