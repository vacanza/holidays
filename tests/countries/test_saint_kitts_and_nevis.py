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

from holidays.constants import PUBLIC, WORKDAY
from holidays.countries.saint_kitts_and_nevis import SaintKittsAndNevis
from tests.common import CommonCountryTests


class TestSaintKittsAndNevis(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SaintKittsAndNevis)

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoWorkdayHoliday(range(self.start_year, 2003))

    def test_special_public_holidays(self):
        self.assertHoliday(
            "2015-02-18",
            "2017-09-20",
            "2017-12-19",
            "2022-08-08",
            "2023-07-04",
        )

    def test_special_half_day_holidays(self):
        self.assertHalfDayHoliday(
            "2017-03-23",
            "2017-04-10",
            "2018-12-31",
            "2019-12-31",
            "2022-04-27",
            "2023-07-20",
            "2023-12-30",
            "2024-08-01",
        )

    def test_carnival_day(self):
        name = "Carnival Day"
        name_lastlap = f"{name} - Last Lap"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        self.assertHolidayName(name_lastlap, (f"{year}-01-02" for year in self.full_range))
        obs_dts = (
            "1995-01-03",
            "2006-01-03",
            "2012-01-03",
            "2017-01-03",
            "2023-01-03",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        obs_dts_lastlap = (
            "1994-01-03",
            "2000-01-03",
            "2005-01-03",
            "2011-01-03",
            "2022-01-03",
        )
        self.assertHolidayName(f"{name_lastlap} (observed)", obs_dts_lastlap)
        self.assertNoNonObservedHoliday(obs_dts, obs_dts_lastlap)

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

    def test_labor_day(self):
        name = "Labour Day"
        self.assertHolidayName(
            name,
            "2020-05-04",
            "2021-05-03",
            "2022-05-02",
            "2023-05-01",
            "2024-05-06",
            "2025-05-05",
        )
        self.assertHolidayName(name, self.full_range)

    def test_whit_monday(self):
        name = "Whit Monday"
        self.assertHolidayName(
            name,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.full_range)

    def test_emancipation_day(self):
        name_1983 = "First Monday of August"
        name_1998 = "Emancipation Day"
        self.assertHolidayName(
            name_1998,
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
            "2025-08-04",
        )
        self.assertHolidayName(name_1983, range(self.start_year, 1998))
        self.assertHolidayName(name_1998, range(1998, self.end_year))
        self.assertNoHolidayName(name_1983, range(1998, self.end_year))
        self.assertNoHolidayName(name_1998, range(self.start_year, 1998))

    def test_culturama_day_last_lap(self):
        name = "Culturama Day - Last Lap"
        self.assertHolidayName(
            name,
            "2020-08-04",
            "2021-08-03",
            "2022-08-02",
            "2023-08-08",
            "2024-08-06",
            "2025-08-05",
        )
        self.assertHolidayName(name, self.full_range)

    def test_national_heroes_day(self):
        name = "National Heroes Day"
        self.assertHolidayName(name, (f"{year}-09-16" for year in range(1998, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1998))
        obs_dts = (
            "2001-09-17",
            "2007-09-17",
            "2012-09-17",
            "2018-09-17",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-09-19" for year in self.full_range))
        obs_dts = (
            "1993-09-20",
            "1999-09-20",
            "2004-09-20",
            "2010-09-20",
            "2021-09-20",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "1994-12-27",
            "2005-12-27",
            "2011-12-27",
            "2016-12-27",
            "2022-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        obs_dts = (
            "1993-12-27",
            "1999-12-27",
            "2004-12-27",
            "2010-12-27",
            "2021-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_kim_collins_day(self):
        name = "Kim Collins Day"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(
            name, (f"{year}-08-25" for year in range(2003, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2003))

    def test_2015_holidays(self):  # ?
        # https://web.archive.org/web/20221102224614/https://www.gov.kn/in-skn-national-public-holidays/
        self.assertHolidays(
            SaintKittsAndNevis(categories=(PUBLIC, WORKDAY), years=2015),
            ("2015-01-01", "Carnival Day"),
            ("2015-01-02", "Carnival Day - Last Lap"),
            ("2015-02-18", "Federal Election Victory Day"),
            ("2015-04-03", "Good Friday"),
            ("2015-04-06", "Easter Monday"),
            ("2015-05-04", "Labour Day"),
            ("2015-05-25", "Whit Monday"),
            ("2015-08-03", "Emancipation Day"),
            ("2015-08-04", "Culturama Day - Last Lap"),
            ("2015-08-25", "Kim Collins Day"),
            ("2015-09-16", "National Heroes Day"),
            ("2015-09-19", "Independence Day"),
            ("2015-12-25", "Christmas Day"),
            ("2015-12-26", "Boxing Day"),
        )

    def test_2021_holidays(self):
        # https://www.facebook.com/photo/?fbid=3623684614351340
        self.assertHolidays(
            SaintKittsAndNevis(categories=(PUBLIC, WORKDAY), years=2021),
            ("2021-01-01", "Carnival Day"),
            ("2021-01-02", "Carnival Day - Last Lap"),
            ("2021-04-02", "Good Friday"),
            ("2021-04-05", "Easter Monday"),
            ("2021-05-03", "Labour Day"),
            ("2021-05-24", "Whit Monday"),
            ("2021-08-02", "Emancipation Day"),
            ("2021-08-03", "Culturama Day - Last Lap"),
            ("2021-08-25", "Kim Collins Day"),
            ("2021-09-16", "National Heroes Day"),
            ("2021-09-19", "Independence Day"),
            ("2021-09-20", "Independence Day (observed)"),
            ("2021-12-25", "Christmas Day"),
            ("2021-12-26", "Boxing Day"),
            ("2021-12-27", "Boxing Day (observed)"),
        )

    def test_2022_holidays(self):
        # https://www.facebook.com/photo/?fbid=525835396250028
        self.assertHolidays(
            SaintKittsAndNevis(categories=(PUBLIC, WORKDAY), years=2022),
            ("2022-01-01", "Carnival Day"),
            ("2022-01-02", "Carnival Day - Last Lap"),
            ("2022-01-03", "Carnival Day - Last Lap (observed)"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-02", "Labour Day"),
            ("2022-06-06", "Whit Monday"),
            ("2022-08-01", "Emancipation Day"),
            ("2022-08-02", "Culturama Day - Last Lap"),
            ("2022-08-08", "Federal Election Victory Day"),
            ("2022-08-25", "Kim Collins Day"),
            ("2022-09-16", "National Heroes Day"),
            ("2022-09-19", "Independence Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_2023_holidays(self):
        # https://www.facebook.com/photo?fbid=525940556239512
        self.assertHolidays(
            SaintKittsAndNevis(categories=(PUBLIC, WORKDAY), years=2023),
            ("2023-01-01", "Carnival Day"),
            ("2023-01-02", "Carnival Day - Last Lap"),
            ("2023-01-03", "Carnival Day (observed)"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-01", "Labour Day"),
            ("2023-05-29", "Whit Monday"),
            (
                "2023-07-04",
                "50th Anniversary of the Establishment of the Caribbean Community (CARICOM)",
            ),
            ("2023-08-07", "Emancipation Day"),
            ("2023-08-08", "Culturama Day - Last Lap"),
            ("2023-09-16", "National Heroes Day"),
            ("2023-09-19", "Independence Day"),
            ("2023-08-25", "Kim Collins Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_2024_holidays(self):
        # https://www.facebook.com/photo/?fbid=769697881863777
        self.assertHolidays(
            SaintKittsAndNevis(categories=(PUBLIC, WORKDAY), years=2024),
            ("2024-01-01", "Carnival Day"),
            ("2024-01-02", "Carnival Day - Last Lap"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-06", "Labour Day"),
            ("2024-05-20", "Whit Monday"),
            ("2024-08-05", "Emancipation Day"),
            ("2024-08-06", "Culturama Day - Last Lap"),
            ("2024-09-16", "National Heroes Day"),
            ("2024-08-25", "Kim Collins Day"),
            ("2024-09-19", "Independence Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )
