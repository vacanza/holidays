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

from datetime import date
from unittest import TestCase

from holidays.calendars.gregorian import (
    JAN,
    FEB,
    APR,
    MAY,
    JUN,
    JUL,
    SEP,
    OCT,
    NOV,
    DEC,
    _timedelta,
)
from holidays.constants import HALF_DAY, PUBLIC
from holidays.financial.us_government_securities import (
    USGovernmentSecurities,
    USGS,
    USBondMarket,
)
from tests.common import CommonFinancialTests


class TestUSGovernmentSecurities(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(USGovernmentSecurities)

    def test_market_aliases(self):
        self.assertAliases(USGovernmentSecurities, USGS, USBondMarket)

    def test_no_holidays(self):
        self.assertNoHolidays(USGovernmentSecurities(years=1949))

    def test_new_years_day(self):
        # Test observed New Year's when Jan 1 falls on Sunday (observed on Monday Jan 2)
        for dt in (
            date(1950, JAN, 2),
            date(2023, JAN, 2),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))

        # Test when Jan 1 falls on a weekday
        self.assertHoliday(date(2010, JAN, 1))

    def test_martin_luther_king_jr_day(self):
        # Not observed before 1998 in bond markets.
        self.assertNoHoliday("1997-01-20")

        for dt in (
            date(1998, JAN, 19),
            date(2000, JAN, 17),
            date(2010, JAN, 18),
            date(2022, JAN, 17),
            date(2023, JAN, 16),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))

    def test_washingtons_birthday(self):
        # Pre-1971: February 22 (with weekend observance)
        self.assertHoliday(date(1950, FEB, 22))

        # Post-1971: 3rd Monday of February
        for dt in (
            date(2000, FEB, 21),
            date(2010, FEB, 15),
            date(2022, FEB, 21),
            date(2023, FEB, 20),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))

    def test_good_friday(self):
        for dt in (
            date(1950, APR, 7),
            date(2000, APR, 21),
            date(2010, APR, 2),
            date(2022, APR, 15),
            date(2023, APR, 7),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))

    def test_memorial_day(self):
        # Pre-1971: May 30 (with weekend observance)
        self.assertHoliday(date(1950, MAY, 30))

        # Post-1971: Last Monday of May
        for dt in (
            date(2000, MAY, 29),
            date(2010, MAY, 31),
            date(2022, MAY, 30),
            date(2023, MAY, 29),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))

    def test_juneteenth_national_independence_day(self):
        # Not observed before 2021.
        self.assertNoHoliday("2020-06-19")

        for dt in (
            date(2021, JUN, 18),
            date(2022, JUN, 20),
            date(2023, JUN, 19),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))

    def test_independence_day(self):
        for dt in (
            date(1950, JUL, 4),
            date(2000, JUL, 4),
            date(2010, JUL, 5),
            date(2021, JUL, 5),
            date(2022, JUL, 4),
            date(2023, JUL, 4),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, +1) if dt.day == 5 else _timedelta(dt, -1))

    def test_labor_day(self):
        for dt in (
            date(1950, SEP, 4),
            date(2000, SEP, 4),
            date(2010, SEP, 6),
            date(2022, SEP, 5),
            date(2023, SEP, 4),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))

    def test_columbus_day(self):
        # Pre-1971: October 12 (with weekend observance)
        self.assertHoliday(date(1950, OCT, 12))

        # Post-1971: 2nd Monday of October
        for dt in (
            date(2000, OCT, 9),
            date(2010, OCT, 11),
            date(2022, OCT, 10),
            date(2023, OCT, 9),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))

    def test_veterans_day(self):
        for dt in (
            date(1950, NOV, 10),
            date(2000, NOV, 10),
            date(2010, NOV, 11),
            date(2022, NOV, 11),
            date(2023, NOV, 10),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, +1) if dt.day == 10 else _timedelta(dt, -1))

    def test_thanksgiving_day(self):
        for dt in (
            date(1950, NOV, 23),
            date(2000, NOV, 23),
            date(2010, NOV, 25),
            date(2022, NOV, 24),
            date(2023, NOV, 23),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, -1))
            self.assertNoHoliday(_timedelta(dt, +1))

    def test_christmas_day(self):
        for dt in (
            date(1950, DEC, 25),
            date(2000, DEC, 25),
            date(2010, DEC, 24),
            date(2021, DEC, 24),
            date(2022, DEC, 26),
            date(2023, DEC, 25),
        ):
            self.assertHoliday(dt)
            self.assertNoHoliday(_timedelta(dt, +1) if dt.day in {24, 26} else _timedelta(dt, -1))

    def test_2023(self):
        self.assertHolidays(
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-16", "Martin Luther King Jr. Day"),
            ("2023-02-20", "Washington's Birthday"),
            ("2023-04-07", "Good Friday"),
            ("2023-05-29", "Memorial Day"),
            ("2023-06-19", "Juneteenth National Independence Day"),
            ("2023-07-04", "Independence Day"),
            ("2023-09-04", "Labor Day"),
            ("2023-10-09", "Columbus Day"),
            ("2023-11-10", "Veterans Day (observed)"),
            ("2023-11-23", "Thanksgiving Day"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_2024(self):
        self.assertHolidays(
            ("2024-01-01", "New Year's Day"),
            ("2024-01-15", "Martin Luther King Jr. Day"),
            ("2024-02-19", "Washington's Birthday"),
            ("2024-03-29", "Good Friday"),
            ("2024-05-27", "Memorial Day"),
            ("2024-06-19", "Juneteenth National Independence Day"),
            ("2024-07-04", "Independence Day"),
            ("2024-09-02", "Labor Day"),
            ("2024-10-14", "Columbus Day"),
            ("2024-11-11", "Veterans Day"),
            ("2024-11-28", "Thanksgiving Day"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_2025(self):
        self.assertHolidays(
            ("2025-01-01", "New Year's Day"),
            ("2025-01-20", "Martin Luther King Jr. Day"),
            ("2025-02-17", "Washington's Birthday"),
            ("2025-04-18", "Good Friday"),
            ("2025-05-26", "Memorial Day"),
            ("2025-06-19", "Juneteenth National Independence Day"),
            ("2025-07-04", "Independence Day"),
            ("2025-09-01", "Labor Day"),
            ("2025-10-13", "Columbus Day"),
            ("2025-11-11", "Veterans Day"),
            ("2025-11-27", "Thanksgiving Day"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_half_day_holidays_2025(self):
        self.assertHolidays(
            USGovernmentSecurities(years=2025, categories=(HALF_DAY, PUBLIC)),
            # Full closures (PUBLIC)
            ("2025-01-01", "New Year's Day"),
            ("2025-01-20", "Martin Luther King Jr. Day"),
            ("2025-02-17", "Washington's Birthday"),
            ("2025-04-18", "Good Friday"),
            ("2025-05-26", "Memorial Day"),
            ("2025-06-19", "Juneteenth National Independence Day"),
            ("2025-07-04", "Independence Day"),
            ("2025-09-01", "Labor Day"),
            ("2025-10-13", "Columbus Day"),
            ("2025-11-11", "Veterans Day"),
            ("2025-11-27", "Thanksgiving Day"),
            ("2025-12-25", "Christmas Day"),
            # Early closes (HALF_DAY)
            ("2025-04-17", "Markets close at 2:00 PM ET (Good Friday)"),
            ("2025-05-23", "Markets close at 2:00 PM ET (Memorial Day)"),
            ("2025-07-03", "Markets close at 2:00 PM ET (Independence Day)"),
            ("2025-11-28", "Markets close at 2:00 PM ET (Thanksgiving Day)"),
            ("2025-12-24", "Markets close at 2:00 PM ET (Christmas Day)"),
            ("2025-12-31", "Markets close at 2:00 PM ET (New Year's Day)"),
        )

    def test_half_day_holidays_2023(self):
        # 2023: Dec 25 is Monday, Jan 1 2024 is Monday.
        # Early close Friday Dec 22 for Christmas (Monday holiday).
        # Early close Friday Dec 29 for New Year's Day 2024 (Monday holiday).
        self.assertHolidays(
            USGovernmentSecurities(years=2023, categories=(HALF_DAY, PUBLIC)),
            # Full closures (PUBLIC)
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-16", "Martin Luther King Jr. Day"),
            ("2023-02-20", "Washington's Birthday"),
            ("2023-04-07", "Good Friday"),
            ("2023-05-29", "Memorial Day"),
            ("2023-06-19", "Juneteenth National Independence Day"),
            ("2023-07-04", "Independence Day"),
            ("2023-09-04", "Labor Day"),
            ("2023-10-09", "Columbus Day"),
            ("2023-11-10", "Veterans Day (observed)"),
            ("2023-11-23", "Thanksgiving Day"),
            ("2023-12-25", "Christmas Day"),
            # Early closes (HALF_DAY)
            ("2023-04-06", "Markets close at 2:00 PM ET (Good Friday)"),
            ("2023-05-26", "Markets close at 2:00 PM ET (Memorial Day)"),
            ("2023-07-03", "Markets close at 2:00 PM ET (Independence Day)"),
            ("2023-11-24", "Markets close at 2:00 PM ET (Thanksgiving Day)"),
            ("2023-12-22", "Markets close at 2:00 PM ET (Christmas Day)"),
            ("2023-12-29", "Markets close at 2:00 PM ET (New Year's Day)"),
        )

    def test_half_day_holidays_2022(self):
        # 2022: July 4 is Monday, Dec 25 is Sunday (observed Monday Dec 26), Jan 1 2023 is Sunday.
        # Early close Friday July 1 for Independence Day (Monday holiday).
        # Early close Friday Dec 23 for Christmas (Sunday holiday).
        # Early close Friday Dec 30 for New Year's Day 2023 (Sunday holiday).
        self.assertHolidays(
            USGovernmentSecurities(years=2022, categories=(HALF_DAY, PUBLIC)),
            # Full closures (PUBLIC)
            ("2022-01-17", "Martin Luther King Jr. Day"),
            ("2022-02-21", "Washington's Birthday"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-30", "Memorial Day"),
            ("2022-06-20", "Juneteenth National Independence Day (observed)"),
            ("2022-07-04", "Independence Day"),
            ("2022-09-05", "Labor Day"),
            ("2022-10-10", "Columbus Day"),
            ("2022-11-11", "Veterans Day"),
            ("2022-11-24", "Thanksgiving Day"),
            ("2022-12-26", "Christmas Day (observed)"),
            # Early closes (HALF_DAY)
            ("2022-04-14", "Markets close at 2:00 PM ET (Good Friday)"),
            ("2022-05-27", "Markets close at 2:00 PM ET (Memorial Day)"),
            ("2022-07-01", "Markets close at 2:00 PM ET (Independence Day)"),
            ("2022-11-25", "Markets close at 2:00 PM ET (Thanksgiving Day)"),
            ("2022-12-23", "Markets close at 2:00 PM ET (Christmas Day)"),
            ("2022-12-30", "Markets close at 2:00 PM ET (New Year's Day)"),
        )

    def test_half_day_holidays_2024(self):
        # 2024: Jan 1 2025 is Wednesday.
        # Early close Tuesday Dec 31 for New Year's Day 2025 (Wednesday holiday).
        self.assertHolidays(
            USGovernmentSecurities(years=2024, categories=(HALF_DAY, PUBLIC)),
            # Full closures (PUBLIC)
            ("2024-01-01", "New Year's Day"),
            ("2024-01-15", "Martin Luther King Jr. Day"),
            ("2024-02-19", "Washington's Birthday"),
            ("2024-03-29", "Good Friday"),
            ("2024-05-27", "Memorial Day"),
            ("2024-06-19", "Juneteenth National Independence Day"),
            ("2024-07-04", "Independence Day"),
            ("2024-09-02", "Labor Day"),
            ("2024-10-14", "Columbus Day"),
            ("2024-11-11", "Veterans Day"),
            ("2024-11-28", "Thanksgiving Day"),
            ("2024-12-25", "Christmas Day"),
            # Early closes (HALF_DAY)
            ("2024-03-28", "Markets close at 2:00 PM ET (Good Friday)"),
            ("2024-05-24", "Markets close at 2:00 PM ET (Memorial Day)"),
            ("2024-07-03", "Markets close at 2:00 PM ET (Independence Day)"),
            ("2024-11-29", "Markets close at 2:00 PM ET (Thanksgiving Day)"),
            ("2024-12-24", "Markets close at 2:00 PM ET (Christmas Day)"),
            ("2024-12-31", "Markets close at 2:00 PM ET (New Year's Day)"),
        )

    def test_1975_veterans_day_1971_1977(self):
        # Test Veterans Day during 1971-1977 period (4th Monday of October).
        # 1975: Oct 27 is 4th Monday of October, Jan 1 1976 is Thursday.
        # Early close Wednesday Dec 31 for New Year's Day 1976 (Thursday holiday).
        self.assertHolidays(
            USGovernmentSecurities(years=1975, categories=(HALF_DAY, PUBLIC)),
            ("1975-01-01", "New Year's Day"),
            ("1975-02-17", "Washington's Birthday"),
            ("1975-03-28", "Good Friday"),
            ("1975-05-26", "Memorial Day"),
            ("1975-07-04", "Independence Day"),
            ("1975-09-01", "Labor Day"),
            ("1975-10-13", "Columbus Day"),
            ("1975-10-27", "Veterans Day"),
            ("1975-11-27", "Thanksgiving Day"),
            ("1975-12-25", "Christmas Day"),
            # Early closes (HALF_DAY)
            ("1975-03-27", "Markets close at 2:00 PM ET (Good Friday)"),
            ("1975-05-23", "Markets close at 2:00 PM ET (Memorial Day)"),
            ("1975-07-03", "Markets close at 2:00 PM ET (Independence Day)"),
            ("1975-11-28", "Markets close at 2:00 PM ET (Thanksgiving Day)"),
            ("1975-12-24", "Markets close at 2:00 PM ET (Christmas Day)"),
            ("1975-12-31", "Markets close at 2:00 PM ET (New Year's Day)"),
        )

    def test_1970_pre_1971_memorial_day(self):
        # Test pre-1971 Memorial Day (May 30) and early close logic.
        # 1970: Feb 22 is Sunday (observed Mon 23), May 30 is Sat (observed Fri 29),
        # July 4 is Sat (observed Fri July 3), Jan 1 1971 is Friday.
        # Early close Thursday Dec 31 for New Year's Day 1971 (Friday holiday).
        self.assertHolidays(
            USGovernmentSecurities(years=1970, categories=(HALF_DAY, PUBLIC)),
            ("1970-01-01", "New Year's Day"),
            ("1970-02-23", "Washington's Birthday (observed)"),
            ("1970-03-27", "Good Friday"),
            ("1970-05-29", "Memorial Day (observed)"),
            ("1970-07-03", "Independence Day (observed)"),
            ("1970-09-07", "Labor Day"),
            ("1970-10-12", "Columbus Day"),
            ("1970-11-11", "Veterans Day"),
            ("1970-11-26", "Thanksgiving Day"),
            ("1970-12-25", "Christmas Day"),
            # Early closes (HALF_DAY)
            ("1970-03-26", "Markets close at 2:00 PM ET (Good Friday)"),
            ("1970-05-28", "Markets close at 2:00 PM ET (Memorial Day)"),
            ("1970-07-02", "Markets close at 2:00 PM ET (Independence Day)"),
            ("1970-11-27", "Markets close at 2:00 PM ET (Thanksgiving Day)"),
            ("1970-12-24", "Markets close at 2:00 PM ET (Christmas Day)"),
            ("1970-12-31", "Markets close at 2:00 PM ET (New Year's Day)"),
        )
