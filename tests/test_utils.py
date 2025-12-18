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

import unittest
import warnings
from collections import defaultdict
from collections.abc import Callable
from concurrent.futures import ProcessPoolExecutor
from datetime import date
from pathlib import Path
from unittest import mock

import pytest

import holidays
from holidays.calendars.gregorian import FRI, SAT, SUN
from holidays.holiday_base import HolidayBase
from holidays.utils import (
    CountryHoliday,
    country_holidays,
    financial_holidays,
    list_localized_countries,
    list_localized_financial,
    list_supported_countries,
    list_supported_financial,
    list_long_weekends,
)
from tests.common import PYTHON_LATEST_SUPPORTED_VERSION, PYTHON_VERSION


class TestCountryHolidays(unittest.TestCase):
    def setUp(self):
        self.holidays = country_holidays("US")

    def test_country(self):
        self.assertEqual(self.holidays.country, "US")

    def test_country_single_year(self):
        test_holidays = country_holidays("US", years=2021)
        self.assertEqual(test_holidays.years, {2021})

    def test_country_multiple_years(self):
        test_holidays = country_holidays("US", years=(2015, 2021))
        self.assertEqual(test_holidays.years, {2015, 2021})

    def test_country_range_years(self):
        test_holidays = country_holidays("US", years=range(2010, 2015))
        self.assertEqual(test_holidays.years, set(range(2010, 2015)))

    def test_country_subdivision(self):
        test_holidays = country_holidays("US", subdiv="NY")
        self.assertEqual(test_holidays.subdiv, "NY")

    def test_invalid_country_raises_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            country_holidays("XXXX")

    def test_invalid_country_subdivision_raises_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            country_holidays("US", subdiv="XXXX")

    def test_country_holiday_class_deprecation(self):
        with self.assertWarns(DeprecationWarning) as ctx:
            CountryHoliday("IT")
        self.assertIn("CountryHoliday is deprecated", str(ctx.warning))


class TestFinancialHolidays(unittest.TestCase):
    def setUp(self):
        self.holidays = financial_holidays("XNYS")

    def test_market(self):
        self.assertEqual(self.holidays.market, "XNYS")

    def test_market_single_year(self):
        test_holidays = financial_holidays("XNYS", years=2021)
        self.assertEqual(test_holidays.years, {2021})

    def test_market_multiple_years(self):
        test_holidays = financial_holidays("XNYS", years=(2015, 2021))
        self.assertEqual(test_holidays.years, {2015, 2021})

    def test_market_range_years(self):
        test_holidays = financial_holidays("XNYS", years=range(2010, 2015))
        self.assertEqual(test_holidays.years, set(range(2010, 2015)))

    def test_invalid_market_raises_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            financial_holidays("XXXX")

    def test_invalid_market_subdivision_raises_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            financial_holidays("XNYS", subdiv="XXXX")


class TestAllInSameYear(unittest.TestCase):
    """Ensure only holidays in the year(s) requested are returned."""

    years = set(range(1950, 2051))

    @staticmethod
    def _check_single_entity_worker(
        args: tuple[str, Callable[..., HolidayBase], set[int]],
    ) -> None:
        entity, entity_func, years = args
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # Check each year individually.
        for year in years:
            for dt in entity_func(entity, years=year):
                if not isinstance(dt, date):
                    raise AssertionError(f"{entity}: {dt} is not a date instance")
                if dt.year != year:
                    raise AssertionError(f"{entity}: date {dt} not in year {year}")

        # Check full range at once.
        all_holidays = entity_func(entity, years=years)
        if all_holidays.years != years:
            raise AssertionError(f"{entity}: years mismatch {all_holidays.years} != {years}")

    def _check_holidays_years(
        self, entity_func: Callable[..., HolidayBase], entity_list: dict[str, list[str]]
    ):
        """
        Only holidays within the requested years should be returned.
        This prevents triggering a `RuntimeError: dictionary changed size during iteration`.

        This is a logic test, not a compatibility test, so for expediency it is executed
        only once using the latest supported Python version.
        """
        with ProcessPoolExecutor() as executor:
            list(
                executor.map(
                    self._check_single_entity_worker,
                    [(entity, entity_func, self.years) for entity in entity_list],
                )
            )

    @pytest.mark.skipif(
        PYTHON_VERSION != PYTHON_LATEST_SUPPORTED_VERSION,
        reason="Run once on the latest Python version only",
    )
    @mock.patch("pathlib.Path.rglob", return_value=())
    def test_all_countries(self, _unused_mock):
        self._check_holidays_years(country_holidays, list_supported_countries())

    @pytest.mark.skipif(
        PYTHON_VERSION != PYTHON_LATEST_SUPPORTED_VERSION,
        reason="Run once on the latest Python version only",
    )
    @mock.patch("pathlib.Path.rglob", return_value=())
    def test_all_financial(self, _unused_mock):
        self._check_holidays_years(financial_holidays, list_supported_financial())


class TestListLocalizedEntities(unittest.TestCase):
    def assertLocalizedEntities(self, localized_entities, supported_entities):  # noqa: N802
        tests_dir = Path(__file__).parent
        locale_dir = tests_dir.parent / "holidays" / "locale"

        # Collect `<locale>` part from
        # holidays/locale/<locale>/LC_MESSAGES/<entity_code>.mo.
        entity_to_languages = defaultdict(list)
        for path in locale_dir.rglob("*.mo"):
            entity_to_languages[path.stem].append(path.parts[-3])

        for entity_code in supported_entities.keys():
            actual_languages = sorted(entity_to_languages.get(entity_code, []))
            expected_languages = localized_entities.get(entity_code, [])

            self.assertEqual(
                actual_languages,
                expected_languages,
                f"The supported languages for {entity_code} don't match its actual languages: "
                f"{set(actual_languages).difference(set(expected_languages))}",
            )

            entity = getattr(holidays, entity_code)
            self.assertEqual(
                list(entity.supported_languages),
                expected_languages,
                f"The supported languages for {entity_code} don't match "
                "its `supported_languages`.",
            )

            if expected_languages:
                self.assertIn(
                    entity.default_language,
                    expected_languages,
                    "The `default_language` must be listed in "
                    f"`supported_languages` for {entity_code}",
                )

    def test_localized_countries(self):
        self.assertLocalizedEntities(
            list_localized_countries(), list_supported_countries(include_aliases=False)
        )

    def test_localized_financial(self):
        self.assertLocalizedEntities(
            list_localized_financial(), list_supported_financial(include_aliases=False)
        )


class TestListSupportedEntities(unittest.TestCase):
    def test_list_supported_countries(self):
        supported_countries = list_supported_countries(include_aliases=False)

        for country in ("AR", "IM", "ZA"):
            self.assertIn(country, supported_countries)

        us_subdivisions = supported_countries["US"]
        self.assertIn("CA", us_subdivisions)
        self.assertIsInstance(us_subdivisions, list)

        countries_count = sum(
            1 for path in Path("holidays/countries").glob("*.py") if path.stem != "__init__"
        )
        self.assertEqual(countries_count, len(supported_countries))

    def test_list_supported_financial(self):
        supported_financial = list_supported_financial(include_aliases=False)

        for market in ("BVMF", "IFEU", "XECB", "XNYS"):
            self.assertIn(market, supported_financial)

        xnys_subdivisions = supported_financial.get("XNYS", [])
        self.assertIsInstance(xnys_subdivisions, list)

        financial_count = sum(
            1 for path in Path("holidays/financial").glob("*.py") if path.stem != "__init__"
        )
        self.assertEqual(financial_count, len(supported_financial))


class MockHolidayBase(HolidayBase):
    def __init__(self, holidays: set[date], weekend: set[int] | None = None) -> None:
        super().__init__()
        self._holidays = set(holidays)
        self.weekend = weekend or {SAT, SUN}

    def keys(self):
        return self._holidays

    def __contains__(self, day):
        return day in self._holidays


class CountryStub1(HolidayBase):
    country = "CS1"
    start_year = 1000
    end_year = 3400

    def _populate(self, year: int) -> None:
        super()._populate(year)
        self._add_holiday_jul_4("Custom July 4th Holiday")
        self._add_holiday_mar_4("Custom March 4th Holiday")
        self._add_holiday_mar_5("Custom March 5th Holiday")
        self._add_holiday_mar_6("Custom March 6th Holiday")


class CountryStub2(HolidayBase):
    country = "CS2"
    start_year = 1000
    end_year = 3400

    def _populate(self, year: int) -> None:
        super()._populate(year)
        self._add_holiday_jul_4("Custom July 4th Holiday")
        self._add_holiday_dec_26("Custom December 26th Holiday")


class CountryStub3(HolidayBase):
    country = "CS3"
    start_year = 1000
    end_year = 3400
    weekend = {FRI, SAT}

    def _populate(self, year: int) -> None:
        super()._populate(year)
        self._add_holiday_apr_10("Custom April 10th Holiday")


class CountryStub4(HolidayBase):
    country = "CS4"
    start_year = 1000
    end_year = 3400

    def _populate(self, year: int) -> None:
        super()._populate(year)
        self._add_holiday_aug_11("Custom August 11th Holiday")
        self._add_holiday_aug_12("Custom August 12th Holiday")
        self._add_holiday_dec_5("Custom December 5th Holiday")


class CountryStub5(HolidayBase):
    country = "CS5"
    start_year = 1000
    end_year = 3400

    def _populate(self, year: int) -> None:
        super()._populate(year)

        if self._year == 2024:
            self._add_holiday_jan_1("Custom January 1st Holiday")
        if self._year == 2021:
            self._add_holiday_dec_31("Custom December 31st Holiday")


class TestListLongWeekends(unittest.TestCase):
    def assertLongWeekendsEqual(  # noqa: N802
        self,
        holidays,
        expected,
        weekend=None,
        minimum_holiday_length=3,
        *,
        require_weekend_overlap=True,
    ):
        instance = MockHolidayBase(holidays, weekend=weekend or {SAT, SUN})
        result = list_long_weekends(
            instance,
            minimum_holiday_length=minimum_holiday_length,
            require_weekend_overlap=require_weekend_overlap,
        )
        self.assertEqual(result, expected)

    def test_long_weekend_single(self):
        cs1 = CountryStub1(years=2025)
        self.assertLongWeekendsEqual(
            cs1,
            [[date(2025, 7, 4), date(2025, 7, 5), date(2025, 7, 6)]],
        )

    def test_long_weekend_multiple(self):
        cs2 = CountryStub2(years=2025)
        self.assertLongWeekendsEqual(
            cs2,
            [
                [date(2025, 7, 4), date(2025, 7, 5), date(2025, 7, 6)],
                [date(2025, 12, 26), date(2025, 12, 27), date(2025, 12, 28)],
            ],
        )

    def test_long_weekend_require_weekend_overlap(self):
        cs1 = CountryStub1(years=2025)
        self.assertLongWeekendsEqual(
            cs1,
            [[date(2025, 7, 4), date(2025, 7, 5), date(2025, 7, 6)]],
        )
        self.assertLongWeekendsEqual(
            cs1,
            [
                [date(2025, 3, 4), date(2025, 3, 5), date(2025, 3, 6)],
                [date(2025, 7, 4), date(2025, 7, 5), date(2025, 7, 6)],
            ],
            require_weekend_overlap=False,
        )

    def test_long_weekend_custom_weekend(self):
        cs3 = CountryStub3(years=2025)
        self.assertLongWeekendsEqual(
            cs3,
            [[date(2025, 4, 10), date(2025, 4, 11), date(2025, 4, 12)]],
            weekend=cs3.weekend,
        )

    def test_long_weekend_no_holidays(self):
        self.assertLongWeekendsEqual(
            [],
            [],
        )

    def test_long_weekend_custom_minimum_length(self):
        cs4 = CountryStub4(years=2025)
        self.assertLongWeekendsEqual(
            cs4,
            [[date(2025, 8, 9), date(2025, 8, 10), date(2025, 8, 11), date(2025, 8, 12)]],
            minimum_holiday_length=4,
        )

    def test_long_weekend_across_years(self):
        cs5 = CountryStub5(years=2024)
        self.assertLongWeekendsEqual(
            cs5,
            [[date(2023, 12, 30), date(2023, 12, 31), date(2024, 1, 1)]],
        )
        cs5 = CountryStub5(years=2021)
        self.assertLongWeekendsEqual(
            cs5,
            [[date(2021, 12, 31), date(2022, 1, 1), date(2022, 1, 2)]],
        )

    def test_long_weekend_real_country_holidays_data(self):
        self.assertEqual(
            list_long_weekends(country_holidays("AU", subdiv="NSW", years=2024)),
            [
                [date(2023, 12, 30), date(2023, 12, 31), date(2024, 1, 1)],
                [date(2024, 1, 26), date(2024, 1, 27), date(2024, 1, 28)],
                [date(2024, 3, 29), date(2024, 3, 30), date(2024, 3, 31), date(2024, 4, 1)],
                [date(2024, 6, 8), date(2024, 6, 9), date(2024, 6, 10)],
                [date(2024, 10, 5), date(2024, 10, 6), date(2024, 10, 7)],
            ],
        )

    def test_long_weekend_real_financial_holidays_data(self):
        self.assertEqual(
            list_long_weekends(financial_holidays("XNSE", years=2024)),
            [
                [date(2024, 1, 26), date(2024, 1, 27), date(2024, 1, 28)],
                [date(2024, 3, 8), date(2024, 3, 9), date(2024, 3, 10)],
                [date(2024, 3, 23), date(2024, 3, 24), date(2024, 3, 25)],
                [date(2024, 3, 29), date(2024, 3, 30), date(2024, 3, 31)],
                [date(2024, 6, 15), date(2024, 6, 16), date(2024, 6, 17)],
                [date(2024, 11, 1), date(2024, 11, 2), date(2024, 11, 3)],
                [date(2024, 11, 15), date(2024, 11, 16), date(2024, 11, 17)],
            ],
        )
