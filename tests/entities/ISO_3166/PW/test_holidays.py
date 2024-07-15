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

from holidays.constants import ARMED_FORCES, HALF_DAY, PUBLIC
from holidays.entities.ISO_3166.PW import PwHolidays
from tests.common import CommonCountryTests


class TestPwHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            PwHolidays, years=range(1981, 2040), years_non_observed=range(1981, 2040)
        )

    def test_no_holidays(self):
        self.assertNoHolidays(PwHolidays(years=1980))

    def test_special_holidays(self):
        self.assertHoliday(
            "2020-11-03",
        )

    def test_armed_forces_holiday(self):
        self.assertHolidays(
            PwHolidays(categories=ARMED_FORCES, years=2020), ("2020-11-11", "Veterans Day")
        )

    def test_half_day_holiday(self):
        self.assertHolidays(
            PwHolidays(categories=HALF_DAY, years=2019),
            ("2019-09-30", "Preparation for the 25th Independence Day of the Republic of Palau"),
        )

    def test_new_years_day_observed(self):
        self.assertNoNonObservedHoliday(
            "1982-12-31",
            "1993-12-31",
            "1999-12-31",
            "2004-12-31",
            "2010-12-31",
            "2021-12-31",
        )

    def test_memorial_day(self):
        name = "Memorial Day"
        dt = (
            # Last Monday of May.
            "2011-05-30",
            "2012-05-28",
        )
        self.assertHolidayName(name, dt)
        self.assertNoHolidayName(name, range(1981, 2011), range(2013, 2040))

    def test_family_day(self):
        name = "Family Day"
        dt = (
            # 4th Friday of Nov.
            "2017-11-24",
            "2018-11-23",
            "2019-11-22",
            "2020-11-27",
            "2021-11-26",
            "2022-11-25",
            "2023-11-24",
            "2024-11-22",
        )
        self.assertHolidayName(name, dt)
        self.assertNoHolidayName(name, range(1981, 2017))

    def test_presidents_day(self):
        name = "President's Day"
        self.assertHolidayName(name, (f"{year}-06-01" for year in range(2018, 2040)))
        self.assertNoHolidayName(name, range(1981, 2018))
        self.assertNoNonObservedHoliday(
            "2019-05-30",
            "2024-05-30",
            "2025-06-02",
            "2030-05-30",
            "2031-06-02",
        )

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-10-01" for year in range(2018, 2040)))
        self.assertNoHolidayName(name, range(1981, 2018))
        self.assertNoNonObservedHoliday(
            "2022-09-30",
            "2023-10-02",
            "2028-10-02",
            "2033-09-30",
            "2034-10-02",
        )

    def test_2020(self):
        # https://www.facebook.com/photo/?fbid=1499007180251376&set=a.175933635892077
        self.assertHolidays(
            PwHolidays(categories=(ARMED_FORCES, PUBLIC), years=2020),
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
        self.assertHolidays(
            PwHolidays(years=2022),
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
        self.assertHolidays(
            PwHolidays(years=2023),
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
