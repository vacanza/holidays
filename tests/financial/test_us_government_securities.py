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

from holidays.calendars.gregorian import JAN, FEB, APR, MAY, JUN, JUL, SEP, OCT, NOV, DEC, _timedelta
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
        for dt in (
            date(1950, FEB, 20),
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
        for dt in (
            date(1950, MAY, 29),
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
        for dt in (
            date(1950, OCT, 9),
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
