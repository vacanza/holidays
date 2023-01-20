#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import os
import subprocess
import sys
import unittest
from pathlib import Path
from typing import Generator

from dateutil.parser import parse

from holidays import HolidayBase
from holidays.constants import SUN


class TestCase(unittest.TestCase):
    """Base class for python-holiday test cases."""

    @classmethod
    def setUpClass(cls, cls_test=None):
        super().setUpClass()

        if cls_test is None:
            return

        if (
            not hasattr(cls_test, "default_language")
            or cls_test.default_language is None
            or len(cls_test.default_language) != 2
        ):
            raise ValueError(
                f"`{cls_test.__name__}.default_language` value is invalid."
            )

        # Generate translation files for a specific entity.
        name = getattr(cls_test, "country", getattr(cls_test, "market", None))
        for po_path in Path(os.path.join("holidays", "locale")).rglob(
            f"{name}.po"
        ):
            po_file = str(po_path)
            mo_file = po_file.replace(".po", ".mo")
            subprocess.run(
                (
                    sys.executable,
                    os.path.join("scripts", "build", "msgfmt.py"),
                    "-o",
                    mo_file,
                    po_file,
                ),
                check=True,
            )

    def setUp(self, cls):
        super().setUp()

        self.set_locale(cls.default_language.lower())
        self.holidays = cls()

    def set_locale(self, language):
        os.environ["LANGUAGE"] = language

    def parse_arguments(self, args):
        date_args = args
        instance = None

        if issubclass(args[0].__class__, HolidayBase):
            instance = args[0]
            date_args = args[1:]
        else:
            try:
                instance = getattr(self, "holidays")
                self.assertTrue(
                    issubclass(instance.__class__, HolidayBase),
                    "The `self.holidays` must be a `HolidayBase` subclass.",
                )
            except AttributeError:
                raise ValueError(
                    "Either pass a holidays object (`HolidayBase` subclass) "
                    "as a first argument or initialize `self.holidays` in the "
                    "`setUp()` method."
                )

        dates = []
        for date_arg in date_args:
            if type(date_arg) in {list, tuple}:
                dates.extend(date_arg)
            elif isinstance(date_arg, Generator):
                dates.extend(tuple(date_arg))
            else:
                dates.append(date_arg)

        return instance, dates

    def verify_type(self, holidays):
        self.assertTrue(
            issubclass(holidays.__class__, HolidayBase),
            "`holidays` object must be a subclass of `HolidayBase`",
        )

    def assertCountryAliases(self, cls, alpha_2, alpha_3):
        """Asserts country aliases match."""

        self.assertTrue(
            issubclass(cls, HolidayBase),
            "Country holidays object must be a subclass of `HolidayBase`",
        )

        type_error_message = (
            "Country alias object must be a subclass of the country class."
        )
        for alias in (alpha_2, alpha_3):
            self.assertIsNotNone(alias, type_error_message)
            self.assertTrue(issubclass(alias, cls), type_error_message)

        length_error_message = (
            "This method accepts exactly 3 arguments "
            "in this specific order: country base class, country alpha-2 "
            "alias, and country alpha-3 alias. For example: "
            "`self.assertCountryAliases(UnitedStates, US, USA)`"
        )
        if len(alpha_2.__name__) != 2:
            raise ValueError(
                f"{length_error_message}. Alias `{alpha_2.__name__}` doesn't "
                "look like alpha-2 country code."
            )

        if len(alpha_3.__name__) != 3:
            raise ValueError(
                f"{length_error_message}. Alias `{alpha_3.__name__}` doesn't "
                "look like alpha-3 country code."
            )

    def assertNoHolidays(self, holidays):
        """Asserts holidays dict is empty."""

        self.verify_type(holidays)

        self.assertEqual(0, len(holidays))
        self.assertFalse(holidays)

    def assertHolidaysEqual(self, holidays, *expected_holidays):
        """Asserts holidays exactly match expected holidays."""

        self.verify_type(holidays)

        # Check one by one for descriptive error messages.
        for dt, name in expected_holidays:
            self.assertIn(dt, holidays)
            self.assertEqual(name, holidays[dt])

        self.assertEqual(len(holidays), len(expected_holidays))

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
