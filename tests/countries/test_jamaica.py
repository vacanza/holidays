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

from holidays.countries.jamaica import Jamaica
from tests.common import CommonCountryTests


class TestJamaica(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Jamaica)

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "1995-01-02",
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_ash_wednesday(self):
        name = "Ash Wednesday"
        self.assertHolidayName(
            name,
            "2020-02-26",
            "2021-02-17",
            "2022-03-02",
            "2023-02-22",
            "2024-02-14",
            "2025-03-05",
        )
        self.assertHolidayName(name, self.full_range)

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

    def test_national_labor_day(self):
        name = "National Labour Day"
        self.assertHolidayName(name, (f"{year}-05-23" for year in self.full_range))
        obs_dts = (
            "1998-05-25",
            "1999-05-24",
            "2004-05-24",
            "2009-05-25",
            "2010-05-24",
            "2015-05-25",
            "2020-05-25",
            "2021-05-24",
            "2026-05-25",
            "2027-05-24",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_emancipation_day(self):
        name = "Emancipation Day"
        self.assertHolidayName(name, (f"{year}-08-01" for year in range(1998, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1998))
        obs_dts = (
            "1999-08-02",
            "2004-08-02",
            "2010-08-02",
            "2021-08-02",
            "2027-08-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-08-06" for year in self.full_range))
        obs_dts = (
            "2000-08-07",
            "2006-08-07",
            "2017-08-07",
            "2023-08-07",
            "2028-08-07",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_national_heroes_day(self):
        name = "National Heroes Day"
        self.assertHolidayName(
            name,
            "2020-10-19",
            "2021-10-18",
            "2022-10-17",
            "2023-10-16",
            "2024-10-21",
            "2025-10-20",
        )
        self.assertHolidayName(name, self.full_range)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2005-12-27",
            "2011-12-27",
            "2016-12-27",
            "2022-12-27",
            "2033-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_boxing_day(self):
        name = "Boxing Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in self.full_range))
        obs_dts = (
            "2004-12-27",
            "2010-12-27",
            "2021-12-27",
            "2027-12-27",
            "2032-12-27",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
