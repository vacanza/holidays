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

from holidays.constants import ARMED_FORCES, PUBLIC
from holidays.countries.palau import Palau
from tests.common import CommonCountryTests


class TestPalau(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Palau)

    def test_special_holidays(self):
        self.assertHoliday("2020-11-03")
        self.assertArmedForcesHoliday("2020-11-11")
        self.assertHalfDayHoliday("2019-09-30")

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2010-12-31",
            "2012-01-02",
            "2017-01-02",
            "2021-12-31",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_youth_day(self):
        name = "Youth Day"
        self.assertHolidayName(name, (f"{year}-03-15" for year in self.full_range))
        obs_dts = (
            "2009-03-16",
            "2014-03-14",
            "2015-03-16",
            "2020-03-16",
            "2025-03-14",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_senior_citizens_day(self):
        name = "Senior Citizens Day"
        self.assertHolidayName(name, (f"{year}-05-05" for year in self.full_range))
        obs_dts = (
            "2012-05-04",
            "2013-05-06",
            "2018-05-04",
            "2019-05-06",
            "2024-05-06",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_memorial_day(self):
        name = "Memorial Day"
        self.assertHolidayName(name, "2011-05-30", "2012-05-28")
        self.assertNoHolidayName(name, range(self.start_year, 2011), range(2013, self.end_year))

    def test_presidents_day(self):
        name = "President's Day"
        self.assertHolidayName(name, (f"{year}-06-01" for year in range(2018, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2018))
        obs_dts = (
            "2019-05-31",
            "2024-05-31",
            "2025-06-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_constitution_day(self):
        name = "Constitution Day"
        self.assertHolidayName(name, (f"{year}-07-09" for year in self.full_range))
        obs_dts = (
            "2011-07-08",
            "2016-07-08",
            "2017-07-10",
            "2022-07-08",
            "2023-07-10",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_labor_day(self):
        name = "Labor Day"
        self.assertHolidayName(
            name,
            "2020-09-07",
            "2021-09-06",
            "2022-09-05",
            "2023-09-04",
            "2024-09-02",
            "2025-09-01",
        )
        self.assertHolidayName(name, self.full_range)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-10-01" for year in range(2018, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2018))
        obs_dts = (
            "2022-09-30",
            "2023-10-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_united_nations_day(self):
        name = "United Nations Day"
        self.assertHolidayName(name, (f"{year}-10-24" for year in self.full_range))
        obs_dts = (
            "2009-10-23",
            "2010-10-25",
            "2015-10-23",
            "2020-10-23",
            "2021-10-25",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_thanksgiving_day(self):
        name = "Thanksgiving Day"
        self.assertHolidayName(
            name,
            "2020-11-26",
            "2021-11-25",
            "2022-11-24",
            "2023-11-23",
            "2024-11-28",
            "2025-11-27",
        )
        self.assertHolidayName(name, self.full_range)

    def test_family_day(self):
        name = "Family Day"
        self.assertHolidayName(
            name,
            "2020-11-27",
            "2021-11-26",
            "2022-11-25",
            "2023-11-24",
            "2024-11-22",
            "2025-11-28",
        )
        self.assertHolidayName(name, range(2017, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2017))

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2010-12-24",
            "2011-12-26",
            "2016-12-26",
            "2021-12-24",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_2020(self):
        # https://www.facebook.com/photo/?fbid=1499007180251376&set=a.175933635892077
        self.assertHolidays(
            Palau(categories=(ARMED_FORCES, PUBLIC), years=2020),
            ("2020-01-01", "New Year's Day"),
            ("2020-03-15", "Youth Day"),
            ("2020-03-16", "Youth Day (observed)"),
            ("2020-05-05", "Senior Citizens Day"),
            ("2020-06-01", "President's Day"),
            ("2020-07-09", "Constitution Day"),
            ("2020-09-07", "Labor Day"),
            ("2020-10-01", "Independence Day"),
            ("2020-10-23", "United Nations Day (observed)"),
            ("2020-10-24", "United Nations Day"),
            ("2020-11-03", "National Day of Democracy"),
            ("2020-11-11", "Veterans Day"),
            ("2020-11-26", "Thanksgiving Day"),
            ("2020-11-27", "Family Day"),
            ("2020-12-25", "Christmas Day"),
        )

    def test_2022(self):
        # https://www.facebook.com/photo/?fbid=2076492362502852&set=a.175933635892077
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "New Year's Day"),
            ("2022-03-15", "Youth Day"),
            ("2022-05-05", "Senior Citizens Day"),
            ("2022-06-01", "President's Day"),
            ("2022-07-08", "Constitution Day (observed)"),
            ("2022-07-09", "Constitution Day"),
            ("2022-09-05", "Labor Day"),
            ("2022-09-30", "Independence Day (observed)"),
            ("2022-10-01", "Independence Day"),
            ("2022-10-24", "United Nations Day"),
            ("2022-11-24", "Thanksgiving Day"),
            ("2022-11-25", "Family Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )

    def test_2023(self):
        # https://www.facebook.com/photo/?fbid=510442897789296&set=a.368725625294358
        self.assertHolidaysInYear(
            2023,
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-03-15", "Youth Day"),
            ("2023-05-05", "Senior Citizens Day"),
            ("2023-06-01", "President's Day"),
            ("2023-07-09", "Constitution Day"),
            ("2023-07-10", "Constitution Day (observed)"),
            ("2023-09-04", "Labor Day"),
            ("2023-10-01", "Independence Day"),
            ("2023-10-02", "Independence Day (observed)"),
            ("2023-10-24", "United Nations Day"),
            ("2023-11-23", "Thanksgiving Day"),
            ("2023-11-24", "Family Day"),
            ("2023-12-25", "Christmas Day"),
        )
