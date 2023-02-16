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
    def setUpClass(cls, test_class=None):
        super().setUpClass()

        if test_class is None:
            return None

        cls.test_class = test_class

        if (
            not hasattr(test_class, "default_language")
            or test_class.default_language is None
            # Can be either 2 (e.g., en, fr, uk) or 5 (e.g., en_US, en_GB).
            or len(test_class.default_language) not in {2, 5}
        ):
            raise ValueError(
                f"`{test_class.__name__}.default_language` value is invalid."
            )

        # Generate translation files for a specific entity.
        name = getattr(
            test_class, "country", getattr(test_class, "market", None)
        )
        for po_path in Path(os.path.join("holidays", "locale")).rglob(
            f"{name}.po"
        ):
            po_file = str(po_path)
            mo_file = po_file.replace(".po", ".mo")
            subprocess.run(
                (
                    sys.executable,
                    os.path.join("scripts", "l10n", "msgfmt.py"),
                    "-o",
                    mo_file,
                    po_file,
                ),
                check=True,
            )

    def setUp(self):
        super().setUp()

        self.set_language(self.test_class.default_language.lower())
        self.holidays = self.test_class()

    def set_language(self, language):
        os.environ["LANGUAGE"] = language

    def _parse_arguments(self, args, expand_items=True):
        item_args = args
        instance = None

        if issubclass(args[0].__class__, HolidayBase):
            instance = args[0]
            item_args = args[1:]
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

        items = []
        if expand_items:
            for item_arg in item_args:
                if type(item_arg) in {list, tuple}:
                    items.extend(item_arg)
                elif expand_items and isinstance(item_arg, Generator):
                    items.extend(tuple(item_arg))
                else:
                    items.append(item_arg)
        else:
            items.extend(item_args)

        return instance, items

    def _verify_type(self, holidays):
        self.assertTrue(
            issubclass(holidays.__class__, HolidayBase),
            "`holidays` object must be a subclass of `HolidayBase`",
        )

    def assertCountryAliases(self, cls, alpha_2, alpha_3):
        """Assert country aliases match."""

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

    def assertHoliday(self, *args):
        """Assert each date is a holiday."""

        holidays, dates = self._parse_arguments(args)
        for dt in dates:
            self.assertIn(dt, holidays, dt)

    def assertHolidayDates(self, *args):
        """Assert holiday dates exactly match expected dates."""

        holidays, dates = self._parse_arguments(args)
        self._verify_type(holidays)

        for dt in dates:  # Check one by one for descriptive error messages.
            self.assertIn(dt, holidays, dt)

        self.assertEqual(
            len(dates),
            len(holidays.keys()),
            set(dates).difference(holidays.keys()),
        )

    def assertHolidayName(self, name, *args):
        """Assert a holiday with a specific name exists."""

        holidays, _ = self._parse_arguments(args)
        self.assertEqual(
            len(holidays.years), len(holidays.get_named(name)), name
        )

    def assertHolidays(self, *args):
        """Assert holidays exactly match expected holidays."""

        holidays, expected_holidays = self._parse_arguments(
            args, expand_items=False
        )
        self._verify_type(holidays)

        # Check one by one for descriptive error messages.
        for dt, name in expected_holidays:
            self.assertIn(dt, holidays)
            self.assertEqual(name, holidays.get(dt), dt)

        self.assertEqual(
            len(holidays),
            len(expected_holidays),
            set(
                (dt.strftime("%Y-%m-%d"), name)
                for dt, name in holidays.items()
            ).difference((dt, name) for dt, name in expected_holidays),
        )

    def assertHolidaysName(self, name, *args):
        """Assert each holiday name matches an expected one."""

        holidays, dates = self._parse_arguments(args)
        for dt in dates:
            self.assertIn(name, holidays.get_list(dt))

    def assertNoHoliday(self, *args):
        """Assert each date is not a holiday."""

        holidays, dates = self._parse_arguments(args)
        for dt in dates:
            self.assertNotIn(dt, holidays, dt)

    def assertNoHolidayName(self, name, *args):
        """Assert a holiday with a specific name doesn't exist."""

        holidays, _ = self._parse_arguments(args)
        self.assertFalse(holidays.get_named(name), name)

    def assertNoHolidays(self, holidays):
        """Assert holidays dict is empty."""

        self._verify_type(holidays)

        self.assertFalse(holidays)
        self.assertEqual(0, len(holidays))


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
