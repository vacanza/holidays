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

import importlib
import os
import re
import sys
import warnings
from collections import defaultdict
from collections.abc import Generator
from datetime import date
from functools import cache

from dateutil.parser import parse

from holidays import HolidayBase
from holidays.calendars.gregorian import SUN
from holidays.constants import PUBLIC
from holidays.groups import EasternCalendarHolidays, IslamicHolidays
from holidays.observed_holiday_base import ObservedHolidayBase
from holidays.registry import COUNTRIES, FINANCIAL

PYTHON_LATEST_SUPPORTED_VERSION = "3.14"
PYTHON_VERSION = f"{sys.version_info.major}.{sys.version_info.minor}"


class TestCase:
    """Base class for holidays test cases."""

    @staticmethod
    @cache
    def _get_or_create_lookup(
        test_class, *, with_subdiv_categories=False, with_subdiv_special_flags=False
    ):
        """Build and cache categories and subdivision lookup tables for a holiday test class."""

        non_public_supported_categories = tuple(
            category for category in test_class.supported_categories if category != PUBLIC
        )

        supported_special_flags_list = []
        if issubclass(test_class, IslamicHolidays):
            supported_special_flags_list.append("islamic_no_estimated")
        supported_special_flags = tuple(supported_special_flags_list)

        subdiv_base = {}
        subdiv_category = {}
        subdiv_special_flag = {}
        for subdiv in test_class.subdivisions:
            subdiv_code = subdiv.lower().replace(" ", "_")
            subdiv_base[subdiv_code] = (subdiv, None, subdiv_code)

            if with_subdiv_categories:
                for category in non_public_supported_categories:
                    subdiv_category[f"{subdiv_code}_{category}"] = (subdiv, category, subdiv_code)

            if with_subdiv_special_flags:
                for special_flag in supported_special_flags:
                    subdiv_special_flag[f"{subdiv_code}_{special_flag}"] = (
                        subdiv,
                        special_flag,
                        subdiv_code,
                    )

        return (
            subdiv_base,
            subdiv_category,
            non_public_supported_categories,
            subdiv_special_flag,
            supported_special_flags,
        )

    @classmethod
    def _generate_assert_methods(cls):
        """Dynamically generate assertion methods for all holiday variants."""

        def make_assert(helper_func, instance_name, method_type):
            def _method(self, *args, **kwargs):
                if method_type == "name_count":
                    if len(args) < 2:
                        raise TypeError(
                            f"Expected (name, count, ...) arguments for {instance_name}"
                        )
                    name, count, *rest = args
                    return helper_func(self, name, count, instance_name, *rest, **kwargs)
                elif method_type == "name":
                    if not args:
                        raise TypeError(f"Expected (name, ...) arguments for {instance_name}")
                    name, *rest = args
                    return helper_func(self, name, instance_name, *rest, **kwargs)
                elif method_type == "year":
                    if not args:
                        raise TypeError(f"Expected (year, ...) arguments for {instance_name}")
                    year, *rest = args
                    return helper_func(self, year, instance_name, *rest, **kwargs)
                else:
                    return helper_func(self, instance_name, *args, **kwargs)

            return _method

        method_specs = {
            "_assertHoliday": "assert{variant}Holiday",
            "_assertHolidayDates": "assert{variant}HolidayDates",
            "_assertHolidayDatesInYear": "assert{variant}HolidayDatesInYear",
            "_assertHolidayName": "assert{variant}HolidayName",
            "_assertHolidayNameCount": "assert{variant}HolidayNameCount",
            "_assertHolidays": "assert{variant}Holidays",
            "_assertHolidaysInYear": "assert{variant}HolidaysInYear",
            "_assertNoHoliday": "assertNo{variant}Holiday",
            "_assertNoHolidayName": "assertNo{variant}HolidayName",
            "_assertNoHolidays": "assertNo{variant}Holidays",
        }

        method_types = {
            "_assertHolidayDatesInYear": "year",
            "_assertHolidayNameCount": "name_count",
            "_assertHolidayName": "name",
            "_assertHolidaysInYear": "year",
            "_assertNoHolidayName": "name",
        }

        for attr_name in dir(cls):
            if not attr_name.startswith("holidays"):
                continue

            variant = attr_name.removeprefix("holidays")
            pretty_variant = "".join(part.capitalize() for part in variant.strip("_").split("_"))

            for helper_name, template in method_specs.items():
                method_name = template.format(variant=pretty_variant)
                if hasattr(cls, method_name):
                    continue

                helper = getattr(cls, helper_name)
                method_type = method_types.get(helper_name, "default")
                setattr(cls, method_name, make_assert(helper, attr_name, method_type))

    @classmethod
    def setUpClass(
        cls,
        test_class=None,
        *,
        with_subdiv_categories=False,
        with_subdiv_special_flags=False,
        years=None,
        **year_variants,
    ):
        super().setUpClass()

        if test_class is None:
            return None

        cls.test_class = test_class

        default_lang = getattr(cls.test_class, "default_language", None)
        if default_lang is not None:
            # Normally 2-6 letters (e.g., en, pap, en_US, pap_AW).
            if not (2 <= len(default_lang) <= 6):
                raise ValueError(f"`{cls.test_class.__name__}.default_language` value is invalid.")
            cls.set_language(cls.test_class, default_lang)

        # Use cached lookup instead of rebuilding each time.
        (
            cls._subdiv_base_lookup,
            cls._subdiv_category_lookup,
            cls._non_public_supported_categories_lookup,
            cls._subdiv_special_flag_lookup,
            cls._supported_special_flags_lookup,
        ) = cls._get_or_create_lookup(
            cls.test_class,
            with_subdiv_categories=with_subdiv_categories,
            with_subdiv_special_flags=with_subdiv_special_flags,
        )
        cls._subdiv_lookup = {**cls._subdiv_base_lookup, **cls._subdiv_category_lookup}

        if years is None:
            # Default `self.full_range`
            if not hasattr(cls, "full_range"):
                # `start_year` and `end_year` are used only if they're included directly in
                # country/market entities, not inherited from `HolidayBase`.
                cls.start_year = cls.test_class.__dict__.get("start_year", 1950)
                cls.end_year = cls.test_class.__dict__.get("end_year", 2049) + 1
                cls.full_range = range(cls.start_year, cls.end_year)
            else:
                cls.start_year = cls.full_range.start
                cls.end_year = cls.full_range.stop
            years = cls.full_range

        # Default `years_[insert]` to `years` to prevent redundant initialization.
        is_observed_subclass = issubclass(cls.test_class, ObservedHolidayBase)
        is_islamic_subclass = issubclass(cls.test_class, IslamicHolidays)
        for category in cls._non_public_supported_categories_lookup:
            year_variants.setdefault(f"years_{category}", years)
            if is_observed_subclass:
                year_variants.setdefault(
                    f"years_{category}_non_observed",
                    year_variants.get(
                        "years_non_observed", year_variants.get(f"years_{category}", years)
                    ),
                )
            if is_islamic_subclass:
                year_variants.setdefault(
                    f"years_{category}_islamic_no_estimated",
                    year_variants.get(
                        "years_islamic_no_estimated", year_variants.get(f"years_{category}", years)
                    ),
                )

        # For subdivisions, `years_all_subdivs` can be use for mass-assignments.
        years_all_subdivs = year_variants.get("years_all_subdivs", years)
        years_all_subdivs_non_observed = year_variants.get(
            "years_all_subdivs_non_observed",
            year_variants.get("years_non_observed", year_variants.get("years_all_subdivs", years)),
        )

        for key, (_, _, subdiv_code) in (
            *cls._subdiv_lookup.items(),
            *cls._subdiv_special_flag_lookup.items(),
        ):
            year_variants.setdefault(
                f"years_subdiv_{key}",
                year_variants.get(f"years_subdiv_{subdiv_code}", years_all_subdivs),
            )
            if is_observed_subclass:
                year_variants.setdefault(
                    f"years_subdiv_{key}_non_observed",
                    year_variants.get(
                        f"years_subdiv_{subdiv_code}_non_observed", years_all_subdivs_non_observed
                    ),
                )

        if is_islamic_subclass:
            year_variants.setdefault("years_islamic_no_estimated", years)
        if is_observed_subclass:
            year_variants.setdefault("years_non_observed", years)
        if is_islamic_subclass and is_observed_subclass:
            year_variants.setdefault("years_islamic_no_estimated_non_observed", years)

        variants = {"": years}
        variants.update(year_variants)

        for suffix, ylist in variants.items():
            # Exclude invalid cases & mass-assignment helpers.
            if ylist is None or suffix.startswith("years_all_subdivs"):
                continue

            attr_name_suffix = ""
            init_kwargs = {"years": ylist}

            # Step 1: `_non_observed` suffix.
            if suffix.endswith("_non_observed"):
                suffix = suffix.removesuffix("_non_observed")
                attr_name_suffix = "_non_observed"
                init_kwargs["observed"] = False

            # Step 2: Special flags i.e. `islamic_show_estimated`.
            if suffix.endswith("_islamic_no_estimated"):
                suffix = suffix.removesuffix("_islamic_no_estimated")
                init_kwargs["islamic_show_estimated"] = False
                attr_name_suffix = f"_islamic_no_estimated{attr_name_suffix}"

            # Step 3: Subdivisions
            if suffix.startswith("years_subdiv_"):
                key = suffix.removeprefix("years_subdiv_")
                if key in cls._subdiv_lookup:
                    subdiv, category, subdiv_code = cls._subdiv_lookup[key]
                    init_kwargs["subdiv"] = subdiv
                    if category:
                        init_kwargs["categories"] = (category,)
                        attr_name_suffix = f"_{category}{attr_name_suffix}"
                    attr_name_suffix = f"_subdiv_{subdiv_code}{attr_name_suffix}"

            # Step 4: Categories
            elif suffix.startswith("years_"):
                category = suffix.removeprefix("years_")
                init_kwargs["categories"] = (category,)
                attr_name_suffix = f"_{category}{attr_name_suffix}"

            attr_name = f"holidays{attr_name_suffix}"
            setattr(cls, attr_name, cls.test_class(**init_kwargs))

        # Legacy `cls.subdiv_holidays` / `cls.subdiv_holidays_non_observed` behavior.
        cls.subdiv_holidays = {}
        cls.subdiv_holidays_non_observed = {}
        for subdiv, _, subdiv_code in cls._subdiv_base_lookup.values():
            key_subdiv = f"holidays_subdiv_{subdiv_code}"
            key_subdiv_non_obs = f"{key_subdiv}_non_observed"

            if hasattr(cls, key_subdiv):
                cls.subdiv_holidays[subdiv] = getattr(cls, key_subdiv)
            if is_observed_subclass and hasattr(cls, key_subdiv_non_obs):
                cls.subdiv_holidays_non_observed[subdiv] = getattr(cls, key_subdiv_non_obs)

        if with_subdiv_categories:
            dict_subdiv_cat = defaultdict(dict)
            dict_subdiv_cat_non_obs = defaultdict(dict)
            for category in cls._non_public_supported_categories_lookup:
                setattr(cls, f"subdiv_{category}_holidays", dict_subdiv_cat[category])

                if is_observed_subclass:
                    setattr(
                        cls,
                        f"subdiv_{category}_holidays_non_observed",
                        dict_subdiv_cat_non_obs[category],
                    )

            for subdiv, category, subdiv_code in cls._subdiv_category_lookup.values():
                key_subdiv_cat = f"holidays_subdiv_{subdiv_code}_{category}"
                dict_subdiv_cat[category][subdiv] = getattr(cls, key_subdiv_cat, {})

                if is_observed_subclass:
                    key_subdiv_cat_non_obs = f"{key_subdiv_cat}_non_observed"
                    dict_subdiv_cat_non_obs[category][subdiv] = getattr(
                        cls, key_subdiv_cat_non_obs, {}
                    )

        if with_subdiv_special_flags:
            dict_subdiv_special_flag = defaultdict(dict)
            dict_subdiv_special_flag_non_obs = defaultdict(dict)
            for special_flag in cls._supported_special_flags_lookup:
                setattr(
                    cls, f"subdiv_{special_flag}_holidays", dict_subdiv_special_flag[special_flag]
                )

                if is_observed_subclass:
                    setattr(
                        cls,
                        f"subdiv_{special_flag}_holidays_non_observed",
                        dict_subdiv_special_flag_non_obs[special_flag],
                    )

            for subdiv, special_flag, subdiv_code in cls._subdiv_special_flag_lookup.values():
                key_subdiv_special_flag = f"holidays_subdiv_{subdiv_code}_{special_flag}"
                dict_subdiv_special_flag[special_flag][subdiv] = getattr(
                    cls, key_subdiv_special_flag, {}
                )

                if is_observed_subclass:
                    key_subdiv_special_flag_non_obs = f"{key_subdiv_special_flag}_non_observed"
                    dict_subdiv_special_flag_non_obs[special_flag][subdiv] = getattr(
                        cls, key_subdiv_special_flag_non_obs, {}
                    )

        cls._generate_assert_methods()

    def setUp(self):
        super().setUp()

        if getattr(self.test_class, "default_language") is not None:
            self.set_language(self.test_class.default_language)

    def set_language(self, language):
        os.environ["LANGUAGE"] = language

    def _parse_arguments(
        self, args, *, expand_items=True, instance_name="holidays", raise_on_empty=True
    ):
        item_args = args
        instance = None

        if args and isinstance(args[0], HolidayBase):
            instance = args[0]
            item_args = args[1:]
        else:
            try:
                instance = getattr(self, instance_name)
                self.assertIsInstance(
                    instance,
                    HolidayBase,
                    f"The `self.{instance_name}` must be a `HolidayBase` subclass.",
                )
            except AttributeError:
                raise ValueError(
                    "Either pass a holidays object (`HolidayBase` subclass) "
                    "as a first argument or initialize your `TestCase` class "
                    "properly with `setUpClass()` method."
                )

        items = []
        if expand_items:
            for item_arg in item_args:
                if isinstance(item_arg, (list, set, tuple)):
                    items.extend(item_arg)
                elif isinstance(item_arg, (Generator, range)):
                    items.extend(tuple(item_arg))
                else:
                    items.append(item_arg)
        else:
            items.extend(item_args)

        if instance_name.endswith("_non_observed"):
            self.assertFalse(instance.observed)
        else:
            self.assertTrue(instance.observed)

        if raise_on_empty and not items:
            raise ValueError("The test argument sequence is empty")

        return instance, items

    def _verify_type(self, holidays):
        self.assertTrue(
            issubclass(holidays.__class__, HolidayBase),
            "`holidays` object must be a subclass of `HolidayBase`",
        )

    def assertAliases(self, *aliases):
        """Assert aliases match the test class."""
        self.assertTrue(aliases, "Entity class does not have any aliases.")
        self.assertTrue(
            issubclass(self.test_class, HolidayBase),
            "The entity object must be a subclass of `HolidayBase`",
        )

        type_error_message = "The entity alias object must be a subclass of the entity class."
        for alias in aliases:
            self.assertIsNotNone(alias, type_error_message)
            self.assertTrue(issubclass(alias, self.test_class), type_error_message)

    def assertDeprecatedSubdivisions(self, message):
        warnings.simplefilter("always", category=DeprecationWarning)
        for subdiv in self.test_class._deprecated_subdivisions:
            with warnings.catch_warnings(record=True) as ctx:
                self.test_class(subdiv=subdiv)
                warning = ctx[0]
                self.assertTrue(issubclass(warning.category, DeprecationWarning))
                self.assertIn(message, str(warning.message))

    # Holiday.
    def _assertHoliday(self, instance_name, *args):
        """Helper: assert each date is a holiday."""
        holidays, dates = self._parse_arguments(args, instance_name=instance_name)
        self._verify_type(holidays)

        for dt in dates:
            self.assertIn(dt, holidays, dt)

    # HolidayDates.
    def _assertHolidayDates(self, instance_name, *args):
        """Helper: assert holiday dates exactly match expected dates."""
        holidays, dates = self._parse_arguments(args, instance_name=instance_name)
        self._verify_type(holidays)

        # Check one by one for descriptive error messages.
        for dt in dates:
            self.assertIn(dt, holidays, dt)

        self.assertEqual(len(dates), len(holidays.keys()), set(dates).difference(holidays.keys()))

    # HolidayDatesInYear.
    def _assertHolidayDatesInYear(self, year, instance_name, *args):
        """Helper: assert holiday dates exactly match expected dates in the given year."""
        holidays, dates = self._parse_arguments(args, instance_name=instance_name)
        self._verify_type(holidays)

        filtered_holidays = {dt.strftime("%Y-%m-%d") for dt in holidays.keys() if dt.year == year}

        # Check one by one for descriptive error messages.
        for dt in dates:
            self.assertIn(dt, filtered_holidays, dt)

        self.assertEqual(
            len(dates), len(filtered_holidays), set(dates).difference(filtered_holidays)
        )

    # HolidayName.
    def _assertHolidayName(self, name, instance_name, *args):
        """Helper: assert either a holiday with a specific name exists or
        each holiday name matches an expected one depending on the args nature.
        """
        holidays, items = self._parse_arguments(args, instance_name=instance_name)

        arg = items[0]
        if isinstance(arg, int):  # A holiday name check for a specific year.
            holiday_years = {dt.year for dt in holidays.get_named(name, lookup="exact")}
            self.assertTrue(set(items).issubset(holiday_years), name)
        elif isinstance(arg, date) or parse(arg):  # Exact date check.
            for dt in items:
                self.assertIn(name, holidays.get_list(dt), dt)
        else:
            raise ValueError(f"The {arg} wasn't caught by `assertHolidayName()`")

    # HolidayNameCount.
    def _assertHolidayNameCount(self, name, count, instance_name, *args):
        """Helper: assert number of holidays with a specific name in every year matches
        expected.
        """
        holidays, items = self._parse_arguments(args, instance_name=instance_name)
        self._verify_type(holidays)

        holiday_counts = defaultdict(int)
        for dt in holidays.get_named(name, lookup="exact"):
            holiday_counts[dt.year] += 1

        for year in items:
            self.assertIsInstance(year, int, "Year arguments must be integers")
            holiday_count = holiday_counts.get(year, 0)
            self.assertEqual(
                count,
                holiday_count,
                f"`{name}` occurs {holiday_count} times in year {year}, should be {count}",
            )

    # Holidays.
    def _assertHolidays(self, instance_name, *args):
        """Helper: assert holidays exactly match expected holidays."""
        holidays, expected_holidays = self._parse_arguments(
            args, expand_items=False, instance_name=instance_name
        )
        self._verify_type(holidays)

        # Check one by one for descriptive error messages.
        for dt, name in expected_holidays:
            self.assertIn(dt, holidays)
            self.assertEqual(name, holidays.get(dt), dt)

        self.assertEqual(
            len(holidays),
            len(expected_holidays),
            {(dt.strftime("%Y-%m-%d"), name) for dt, name in holidays.items()}.difference(
                (dt, name) for dt, name in expected_holidays
            ),
        )

    # HolidaysInYear.
    def _assertHolidaysInYear(self, year, instance_name, *args):
        """Helper: assert holidays exactly match expected holidays in the given year."""
        holidays, expected_holidays = self._parse_arguments(
            args, expand_items=False, instance_name=instance_name
        )
        self._verify_type(holidays)

        filtered_holidays = {
            dt.strftime("%Y-%m-%d"): name for dt, name in holidays.items() if dt.year == year
        }

        # Check one by one for descriptive error messages.
        for dt, name in expected_holidays:
            self.assertIn(dt, filtered_holidays)
            self.assertEqual(name, filtered_holidays.get(dt), dt)

        self.assertEqual(
            len(filtered_holidays),
            len(expected_holidays),
            {(dt, name) for dt, name in filtered_holidays.items()}.difference(
                (dt, name) for dt, name in expected_holidays
            ),
        )

    # No Holiday.
    def _assertNoHoliday(self, instance_name, *args):
        """Helper: assert each date is not a holiday."""
        holidays, dates = self._parse_arguments(args, instance_name=instance_name)

        for dt in dates:
            self.assertNotIn(dt, holidays, dt)

    # No HolidayName.
    def _assertNoHolidayName(self, name, instance_name, *args):
        """Helper: assert a holiday with a specific name doesn't exist."""
        holidays, items = self._parse_arguments(
            args, instance_name=instance_name, raise_on_empty=False
        )

        if not items:  # A holiday name check.
            self.assertFalse(holidays.get_named(name, lookup="exact"), name)
            return None

        arg = items[0]
        if isinstance(arg, int):  # A holiday name check for a specific year.
            holiday_years = {dt.year for dt in holidays.get_named(name, lookup="exact")}
            self.assertEqual(0, len(holiday_years.intersection(items)), name)
        elif isinstance(arg, date) or parse(arg):  # Exact date check.
            for dt in items:
                self.assertNotIn(name, holidays.get_list(dt), dt)
        else:
            raise ValueError(f"The {arg} wasn't caught by `assertNoHolidayName()`")

    # No Holidays.
    def _assertNoHolidays(self, instance_name, *args):
        """Helper: assert holidays dict is empty."""
        holidays, _ = self._parse_arguments(
            args, instance_name=instance_name, raise_on_empty=False
        )
        self._verify_type(holidays)

        self.assertFalse(holidays)
        self.assertEqual(0, len(holidays))

    # LocalizedHolidays.
    def _assertLocalizedHolidays(self, localized_holidays, language=None):
        """Helper: assert localized holidays match expected names."""
        instance = self.test_class(
            years=int(localized_holidays[0][0].split("-")[0]),
            language=language,
            categories=self.test_class.supported_categories,
        )

        for subdiv in instance.subdivisions:
            instance.update(
                self.test_class(
                    subdiv=subdiv,
                    years=instance.years,
                    language=language,
                    categories=instance.supported_categories,
                )
            )

        actual_holidays = tuple(
            sorted((dt.strftime("%Y-%m-%d"), name) for dt, name in instance.items())
        )
        self.assertEqual(
            actual_holidays,
            localized_holidays,
            f"Please make sure all holiday names are localized: {actual_holidays}",
        )

    def assertLocalizedHolidays(self, *args):
        """Assert localized holidays match expected names."""
        arg = args[0]
        is_string = isinstance(arg, str)

        language = arg if is_string else None
        localized_holidays = args[1:] if is_string else args

        if language:
            self.set_language(language)
        for language in (language, "invalid", ""):
            self._assertLocalizedHolidays(localized_holidays, language)


class CommonTests(TestCase):
    """Common test cases for all entities."""

    def check_aliases(self, registry, prefix):
        class_name = self.test_class.__name__
        module_name = re.sub(r"(?<!^)(?=[A-Z])", "_", class_name).lower()

        if (entities := registry.get(module_name)) and class_name in entities:
            self.assertAliases(
                *(
                    getattr(
                        importlib.import_module(f"holidays.{prefix}.{module_name}"), alias_name
                    )
                    for alias_name in entities[1:]
                )
            )

    def test_estimated_label(self):
        if isinstance(self.holidays, EasternCalendarHolidays):
            self.assertTrue(
                getattr(self.holidays, "estimated_label", None),
                "The `estimated_label` attribute is required for entities inherited from "
                "`EasternCalendarHolidays`.",
            )

    def test_no_holidays(self):
        self.assertNoHolidays(
            self.test_class(
                categories=self.test_class.supported_categories,
                years=self.test_class.start_year - 1,
            )
        )

    def test_observed_estimated_label(self):
        estimated_label = getattr(self.holidays, "estimated_label", None)
        observed_label = getattr(self.holidays, "observed_label", None)
        observed_estimated_label = getattr(self.holidays, "observed_estimated_label", None)

        if (
            estimated_label
            and observed_label
            # In certain entities, the observed rule applies only to holiday suppression,
            # e.g., XNSE with `SAT_TO_NONE`` or `SUN_TO_NONE``. In these cases, the
            # `observed_estimated_label` is not required.
            and any(
                rule is not None for rule in getattr(self.holidays, "observed_rule", {}).values()
            )
        ):
            self.assertTrue(
                observed_estimated_label,
                "The `observed_estimated_label` attribute is required for entities containing "
                "both `observed_label` and `estimated_label`.",
            )
            self.assertIn(estimated_label.strip("%s ()"), observed_estimated_label)

    def test_observed_label(self):
        if getattr(self.holidays, "observed_label", None):
            self.assertTrue(
                isinstance(self.holidays, ObservedHolidayBase),
                "The `observed_label` attribute is not required as this entity doesn't handle "
                "observed holidays.",
            )

    def test_subdivisions_aliases(self):
        """Validate entity subdivisions aliases."""
        if self.holidays.subdivisions_aliases:
            subdivisions = set(self.holidays.subdivisions)
            for alias, subdiv in self.holidays.subdivisions_aliases.items():
                self.assertIn(
                    subdiv,
                    subdivisions,
                    f"Invalid subdivision alias {alias}: subdivision {subdiv} does not exist.",
                )


class CommonCountryTests(CommonTests):
    """Common test cases for country entities."""

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "country"))
        self.assertFalse(hasattr(self.holidays, "market"))

    def test_aliases(self):
        """Validate entity aliases."""
        self.check_aliases(COUNTRIES, "countries")


class CommonFinancialTests(CommonTests):
    """Common test cases for financial entities."""

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertFalse(hasattr(self.holidays, "country"))

    def test_aliases(self):
        """Validate entity aliases."""
        self.check_aliases(FINANCIAL, "financial")


class SundayHolidays(TestCase):
    """Common class to test countries with Sundays as a holidays."""

    def assertSundays(self, cls):
        holidays = cls(years=1989, include_sundays=True)
        self.assertHoliday(holidays, "1989-12-31")
        self.assertEqual(53, len([s for s in holidays if s.weekday() == SUN]))

        holidays = cls(years=2032, include_sundays=True)
        self.assertHoliday(holidays, "2032-01-04")
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


class WorkingDayTests(TestCase):
    """Common class for testing entity holidays substituted from non-working days."""

    # Workday.
    def _assertWorkingDay(self, instance_name, *args):
        """Helper: assert each date is a working day."""
        holidays, dates = self._parse_arguments(args, instance_name=instance_name)
        self._verify_type(holidays)

        for dt in dates:
            self.assertTrue(
                holidays.is_working_day(dt), f"{dt} should be working day after substitution"
            )

    def assertWorkingDay(self, *args):
        """Assert each date is a working day."""
        self._assertWorkingDay("holidays", *args)

    def assertNonObservedWorkingDay(self, *args):
        """Assert each date is a non-observed working day."""
        self._assertWorkingDay("holidays_non_observed", *args)
