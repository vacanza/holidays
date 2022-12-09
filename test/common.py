#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)
#  Copyright: Arkadii Yakovets <ark@cho.red>, 2022

import unittest

from dateutil.parser import parse

from holidays import HolidayBase
from holidays.constants import SUN


class TestCase(unittest.TestCase):
    """Base class for python-holiday test cases."""

    def parse_arguments(self, args):
        if issubclass(args[0].__class__, HolidayBase):
            return args[0], args[1:]

        if not hasattr(self, "holidays"):
            raise ValueError(
                "Either pass country holidays object (`HolidayBase` subclass) "
                "as a first argument or initialize `self.holidays` in the "
                "`setUp()` method."
            )

        return self.holidays, args

    def verify_type(self, holidays):
        self.assertTrue(
            issubclass(holidays.__class__, HolidayBase),
            "`holidays` object must be a subclass of `HolidayBase`",
        )

    def assertCountryAliases(self, cls, *aliases):
        """Asserts country aliases match."""

        self.assertTrue(
            issubclass(cls, HolidayBase),
            "Country holidays object must be a subclass of `HolidayBase`",
        )

        has_alpha_2 = False
        has_alpha_3 = False
        for alias in aliases:
            self.assertTrue(
                issubclass(alias, cls),
                "Country alias object must be a subclass of the "
                "main country class.",
            )
            self.assertEqual(alias(), cls())

            class_name = alias.__name__
            if len(class_name) == 2:
                has_alpha_2 = True
            elif len(class_name) == 3:
                has_alpha_3 = True
            else:
                raise ValueError(
                    "Alias class name must match either alpha-2 or alpha-3 "
                    f"country code. Got: `{class_name}`."
                )

        self.assertTrue(
            has_alpha_2, "Country alpha-2 code must also be included."
        )
        self.assertTrue(
            has_alpha_3, "Country alpha-3 code must also be included."
        )
        self.assertEqual(
            2,
            len(aliases),
            "Please include alpha-2 and alpha-3 country code aliases.",
        )

    def assertNoHolidays(self, holidays):
        """Asserts holidays dict is empty."""

        self.verify_type(holidays)

        self.assertEqual(0, len(holidays))
        self.assertFalse(holidays)

    def assertHolidaysEqual(self, holidays, *expected_holidays):
        """Asserts holidays exactly match expected holidays."""

        self.verify_type(holidays)

        self.assertEqual(len(holidays), len(expected_holidays))
        # Check one by one for descriptive error messages.
        for dt, name in expected_holidays:
            self.assertIn(dt, holidays)
            self.assertEqual(name, holidays[dt])

    def assertHolidayDatesEqual(self, holidays, *dates):
        """Asserts holiday dates exactly match expected dates."""

        self.verify_type(holidays)

        self.assertEqual(len(dates), len(holidays.keys()))
        for date in dates:  # Check one by one for descriptive error messages.
            self.assertIn(date, holidays)

    def assertHoliday(self, *args):
        """Asserts each date is a holiday."""

        holidays, dates = self.parse_arguments(args)
        for dt in dates:
            self.assertIn(dt, holidays)

    def assertNoHoliday(self, *args):
        """Asserts each date is not a holiday."""

        holidays, dates = self.parse_arguments(args)
        for dt in dates:
            self.assertNotIn(dt, holidays)


class SundayHolidays(TestCase):
    """Common class to test countries with Sundays as a holidays."""

    def assertSundays(self, cls):
        holidays = cls(years=1989, include_sundays=True)
        self.assertHoliday(
            holidays,
            "1989-12-31",
        )
        self.assertEqual(53, len([s for s in holidays if s.weekday() == SUN]))

        holidays = cls(years=2032, include_sundays=True)
        self.assertHoliday(
            holidays,
            "2032-01-04",
        )
        self.assertEqual(52, len([s for s in holidays if s.weekday() == SUN]))

        self.assertNoHolidays(cls(include_sundays=True))

        for sunday in (
            "1989-12-31",
            "2017-02-05",
            "2017-02-12",
            "2032-02-29",
        ):
            self.assertEqual(parse(sunday).weekday(), SUN)
            self.assertHoliday(holidays, sunday)

        for non_sunday in (
            "2001-05-16",
            "2001-05-18",
            "2016-12-27",
            "2016-12-28",
            "2017-02-06",
            "2017-02-07",
            "2017-02-08",
            "2017-02-09",
            "2017-02-10",
        ):
            self.assertNotEqual(parse(non_sunday).weekday(), SUN)
            self.assertNoHoliday(holidays, non_sunday)
