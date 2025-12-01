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

from holidays.countries.bahamas import Bahamas
from tests.common import CommonCountryTests


class TestBahamas(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Bahamas)

    def test_special_public_holidays(self):
        self.assertHoliday("2022-09-19")

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            # Pre-2012 Rule Changed & Underflow to Previous Year Cases.
            "1979-12-31",
            "1984-12-31",
            "1990-12-31",
            "2001-12-31",
            "2003-01-03",
            "2004-01-02",
            "2007-12-31",
            "2009-01-02",
            "2011-01-03",
            # 2012 onwards.
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_majority_rule_day(self):
        name = "Majority Rule Day"
        self.assertHolidayName(name, (f"{year}-01-10" for year in range(2014, self.end_year)))
        obs_dts = (
            "2015-01-12",
            "2016-01-11",
            "2021-01-11",
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

    def test_randol_fawkes_labour_day(self):
        name_1974 = "Labour Day"
        name_2013 = "Randol Fawkes Labour Day"

        self.assertHolidayName(
            name_1974,
            "2007-06-01",
            "2008-06-06",
            "2009-06-05",
            "2010-06-04",
            "2011-06-03",
            "2012-06-01",
        )
        self.assertHolidayName(name_1974, range(self.start_year, 2013))
        self.assertNoHolidayName(name_1974, range(2013, self.end_year))

        self.assertHolidayName(
            name_2013,
            "2020-06-05",
            "2021-06-04",
            "2022-06-03",
            "2023-06-02",
            "2024-06-07",
            "2025-06-06",
        )
        self.assertHolidayName(name_2013, range(2013, self.end_year))
        self.assertNoHolidayName(name_2013, range(self.start_year, 2013))

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-07-10" for year in self.full_range))
        obs_dts = (
            "2011-07-11",
            "2016-07-11",
            "2021-07-12",
            "2022-07-11",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_emancipation_day(self):
        name = "Emancipation Day"
        self.assertHolidayName(
            name,
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
            "2024-08-05",
            "2025-08-04",
        )
        self.assertHolidayName(name, self.full_range)

    def test_national_heroes_day(self):
        name_1974 = "Discovery Day"
        name_2013 = "National Heroes Day"

        self.assertHolidayName(
            name_1974, (f"{year}-10-12" for year in range(self.start_year, 2013))
        )
        self.assertNoHolidayName(name_1974, range(2013, self.end_year))

        obs_dts = (
            "2000-10-13",
            "2004-10-11",
            "2005-10-14",
            "2006-10-13",
            "2010-10-11",
            "2011-10-14",
        )
        self.assertHolidayName(f"{name_1974} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

        self.assertHolidayName(
            name_2013,
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
            "2024-10-14",
            "2025-10-13",
        )
        self.assertHolidayName(name_2013, range(2013, self.end_year))
        self.assertNoHolidayName(name_2013, range(self.start_year, 2013))

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
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
            "2015-12-28",
            "2020-12-28",
            "2021-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_2023(self):
        self.assertHolidaysInYear(
            2023,
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-10", "Majority Rule Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-29", "Whit Monday"),
            ("2023-06-02", "Randol Fawkes Labour Day"),
            ("2023-07-10", "Independence Day"),
            ("2023-08-07", "Emancipation Day"),
            ("2023-10-09", "National Heroes Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )
