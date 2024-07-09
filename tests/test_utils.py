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

import unittest
from datetime import date
from pathlib import Path
from unittest import mock

import pytest

import holidays
from holidays.utils import (
    iso_3166_holidays,
    iso_10383_holidays,
    list_localized_iso_3166_entities,
    list_localized_iso_10383_entities,
    list_iso_3166_entities,
    list_iso_10383_entities,
)
from tests.common import PYTHON_LATEST_SUPPORTED_VERSION, PYTHON_VERSION


class TestCountryHolidays(unittest.TestCase):
    def setUp(self):
        self.holidays = iso_3166_holidays("US")

    def test_country(self):
        self.assertEqual(self.holidays.country, "US")

    def test_country_single_year(self):
        h = iso_3166_holidays("US", years=2021)
        self.assertEqual(h.years, {2021})

    def test_country_years(self):
        h = iso_3166_holidays("US", years=(2015, 2016))
        self.assertEqual(h.years, {2015, 2016})

    def test_country_state(self):
        h = iso_3166_holidays("US", subdiv="NY")
        self.assertEqual(h.subdiv, "NY")

    def test_country_province(self):
        h = iso_3166_holidays("AU", subdiv="NT")
        self.assertEqual(h.subdiv, "NT")

    def test_exceptions(self):
        self.assertRaises(NotImplementedError, lambda: iso_3166_holidays("XXXX"))
        self.assertRaises(NotImplementedError, lambda: iso_3166_holidays("US", subdiv="XXXX"))
        self.assertRaises(NotImplementedError, lambda: iso_3166_holidays("US", subdiv="XXXX"))


class TestFinancialHolidays(unittest.TestCase):
    def setUp(self):
        self.holidays = iso_10383_holidays("XNYS")

    def test_market(self):
        self.assertEqual(self.holidays.market, "XNYS")

    def test_market_single_year(self):
        h = iso_10383_holidays("XNYS", years=2021)
        self.assertEqual(h.years, {2021})

    def test_market_years(self):
        h = iso_10383_holidays("XNYS", years=(2015, 2016))
        self.assertEqual(h.years, {2015, 2016})

    def test_exceptions(self):
        self.assertRaises(NotImplementedError, lambda: iso_10383_holidays("XXXX"))
        self.assertRaises(NotImplementedError, lambda: iso_10383_holidays("XNYS", subdiv="XXXX"))


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
        for country in list_iso_3166_entities():
            for year in self.years:
                for dt in iso_3166_holidays(country, years=year):
                    self.assertEqual(dt.year, year)
                    self.assertEqual(type(dt), date)
        self.assertEqual(self.years, iso_3166_holidays(country, years=self.years).years)

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
        for market in list_iso_10383_entities():
            for year in self.years:
                for dt in iso_10383_holidays(market, years=year):
                    self.assertEqual(dt.year, year)
                    self.assertEqual(type(dt), date)
        self.assertEqual(self.years, iso_10383_holidays(market, years=self.years).years)


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
            list_localized_iso_3166_entities(),
            list_iso_3166_entities(include_aliases=False),
        )

    def test_localized_financial(self):
        self.assertLocalizedEntities(
            list_localized_iso_10383_entities(),
            list_iso_10383_entities(include_aliases=False),
        )


class TestListSupportedEntities(unittest.TestCase):
    def test_list_supported_countries(self):
        supported_countries = list_iso_3166_entities(include_aliases=False)

        self.assertIn("AR", supported_countries)
        self.assertIn("CA", supported_countries["US"])
        self.assertIn("IM", supported_countries)
        self.assertIn("ZA", supported_countries)

        us_subdivisions = supported_countries["US"]
        self.assertIn("CA", us_subdivisions)
        self.assertIsInstance(us_subdivisions, tuple)

        countries_files = [
            path
            for path in Path("holidays/entities/ISO_3166").glob("*.py")
            if path.stem != "__init__"
        ]
        self.assertEqual(
            len(countries_files),
            len(supported_countries),
        )

    def test_list_supported_financial(self):
        iso_10383_entities = list_iso_10383_entities(include_aliases=False)

        for code in ("IFEU", "XECB", "XNYS"):
            self.assertIn(code, iso_10383_entities)

        xnys = iso_10383_entities["XNYS"]
        self.assertIsInstance(xnys, tuple)

        financial_files = [
            path
            for path in Path("holidays/entities/ISO_10383").glob("*.py")
            if path.stem != "__init__"
        ]
        self.assertEqual(
            len(financial_files),
            len(iso_10383_entities),
        )
