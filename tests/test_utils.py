#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import unittest
import warnings
from datetime import date
from pathlib import Path
from unittest import mock

import pytest

import holidays
from holidays.utils import (
    CountryHoliday,
    country_holidays,
    financial_holidays,
    list_localized_countries,
    list_localized_financial,
    list_supported_countries,
    list_supported_financial,
)
from tests.common import PYTHON_LATEST_SUPPORTED_VERSION, PYTHON_VERSION


class TestCountryHolidays(unittest.TestCase):
    def setUp(self):
        self.holidays = country_holidays("US")

    def test_country(self):
        self.assertEqual(self.holidays.country, "US")

    def test_country_single_year(self):
        h = country_holidays("US", years=2021)
        self.assertEqual(h.years, {2021})

    def test_country_years(self):
        h = country_holidays("US", years=(2015, 2016))
        self.assertEqual(h.years, {2015, 2016})

    def test_country_state(self):
        h = country_holidays("US", subdiv="NY")
        self.assertEqual(h.subdiv, "NY")

    def test_country_province(self):
        h = country_holidays("AU", subdiv="NT")
        self.assertEqual(h.subdiv, "NT")

    def test_exceptions(self):
        self.assertRaises(NotImplementedError, lambda: country_holidays("XXXX"))
        self.assertRaises(NotImplementedError, lambda: country_holidays("US", subdiv="XXXX"))
        self.assertRaises(NotImplementedError, lambda: country_holidays("US", subdiv="XXXX"))

    def test_country_holiday_class_deprecation(self):
        with warnings.catch_warnings(record=True) as ctx:
            warnings.simplefilter("always")
            CountryHoliday("IT")
            warning = ctx[0]
            self.assertTrue(issubclass(warning.category, DeprecationWarning))
            self.assertIn("CountryHoliday is deprecated", str(warning.message))


class TestFinancialHolidays(unittest.TestCase):
    def setUp(self):
        self.holidays = financial_holidays("NYSE")

    def test_market(self):
        self.assertEqual(self.holidays.market, "NYSE")

    def test_market_single_year(self):
        h = financial_holidays("NYSE", years=2021)
        self.assertEqual(h.years, {2021})

    def test_market_years(self):
        h = financial_holidays("NYSE", years=(2015, 2016))
        self.assertEqual(h.years, {2015, 2016})

    def test_exceptions(self):
        self.assertRaises(NotImplementedError, lambda: financial_holidays("XXXX"))
        self.assertRaises(NotImplementedError, lambda: financial_holidays("NYSE", subdiv="XXXX"))


class TestAllInSameYear(unittest.TestCase):
    """Test that only holidays in the year(s) requested are returned."""

    years = set(range(1950, 2051))

    @pytest.mark.skipif(
        PYTHON_VERSION != PYTHON_LATEST_SUPPORTED_VERSION,
        reason="Run once on the latest Python version only",
    )
    @mock.patch("pathlib.Path.rglob", return_value=())
    def test_all_countries(self, unused_rglob_mock):
        """
        Only holidays in the year(s) requested should be returned. This
        ensures that we avoid triggering a "RuntimeError: dictionary changed
        size during iteration" error.

        This is logic test and not a code compatibility test, so for expediency
        we only run it once on the latest Python version.
        """
        warnings.simplefilter("ignore")

        for country in list_supported_countries():
            for year in self.years:
                for dt in country_holidays(country, years=year):
                    self.assertEqual(dt.year, year)
                    self.assertEqual(type(dt), date)
        self.assertEqual(self.years, country_holidays(country, years=self.years).years)

    @pytest.mark.skipif(
        PYTHON_VERSION != PYTHON_LATEST_SUPPORTED_VERSION,
        reason="Run once on the latest Python version only",
    )
    @mock.patch("pathlib.Path.rglob", return_value=())
    def test_all_financial(self, unused_rglob_mock):
        """
        Only holidays in the year(s) requested should be returned. This
        ensures that we avoid triggering a "RuntimeError: dictionary changed
        size during iteration" error.

        This is logic test and not a code compatibility test, so for expediency
        we only run it once on the latest Python version.
        """
        warnings.simplefilter("ignore")

        for market in list_supported_financial():
            for year in self.years:
                for dt in financial_holidays(market, years=year):
                    self.assertEqual(dt.year, year)
                    self.assertEqual(type(dt), date)
        self.assertEqual(self.years, financial_holidays(market, years=self.years).years)


class TestListLocalizedEntities(unittest.TestCase):
    def assertLocalizedEntities(self, localized_entities, supported_entities):  # noqa: N802
        tests_dir = Path(__file__).parent
        locale_dir = tests_dir.parent / "holidays" / "locale"

        for entity_code in supported_entities.keys():
            actual_languages = sorted(
                # Collect `<locale>` part from
                # holidays/locale/<locale>/LC_MESSAGES/<country_code>.po.
                path.parts[-3]
                for path in Path(locale_dir).rglob(f"{entity_code}.po")
            )
            expected_languages = localized_entities.get(entity_code, [])

            self.assertEqual(
                actual_languages,
                expected_languages,
                f"The supported languages for {entity_code} don't match "
                f"its actual languages: "
                f"{set(actual_languages).difference(set(expected_languages))}",
            )

            entity = getattr(holidays, entity_code)

            self.assertEqual(
                list(entity.supported_languages),
                expected_languages,
                f"The supported languages for {entity_code} don't match "
                "its `supported_languages`.",
            )
            self.assertEqual(
                actual_languages,
                expected_languages,
                f"Actual and expected locales differ for {entity_code}: "
                f"{set(actual_languages).difference(set(expected_languages))}",
            )

            if expected_languages:
                self.assertIsInstance(expected_languages, list, entity_code)
                self.assertIn(
                    entity.default_language,
                    expected_languages,
                    "The `default_language` must be listed in "
                    f"`supported_languages` for {entity_code}",
                )

    def test_localized_countries(self):
        self.assertLocalizedEntities(
            list_localized_countries(),
            list_supported_countries(include_aliases=False),
        )

    def test_localized_financial(self):
        self.assertLocalizedEntities(
            list_localized_financial(),
            list_supported_financial(include_aliases=False),
        )


class TestListSupportedEntities(unittest.TestCase):
    def test_list_supported_countries(self):
        supported_countries = list_supported_countries(include_aliases=False)

        self.assertIn("AR", supported_countries)
        self.assertIn("CA", supported_countries["US"])
        self.assertIn("IM", supported_countries)
        self.assertIn("ZA", supported_countries)

        us_subdivisions = supported_countries["US"]
        self.assertIn("CA", us_subdivisions)
        self.assertIsInstance(us_subdivisions, list)

        countries_files = [
            path for path in Path("holidays/countries").glob("*.py") if path.stem != "__init__"
        ]
        self.assertEqual(
            len(countries_files),
            len(supported_countries),
        )

    def test_list_supported_financial(self):
        supported_financial = list_supported_financial(include_aliases=False)

        self.assertIn("ECB", supported_financial)
        self.assertIn("IFEU", supported_financial)
        self.assertIn("NYSE", supported_financial)

        nyse = supported_financial["NYSE"]
        self.assertIsInstance(nyse, list)

        financial_files = [
            path for path in Path("holidays/financial").glob("*.py") if path.stem != "__init__"
        ]
        self.assertEqual(
            len(financial_files),
            len(supported_financial),
        )
