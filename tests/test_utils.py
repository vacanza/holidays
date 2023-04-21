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

import pathlib
import sys
import unittest
import warnings
from datetime import date
from unittest import mock

import pytest

from holidays import utils

PYTHON_VERSION = (3, 11)


class TestCountryHolidays(unittest.TestCase):
    def setUp(self):
        self.holidays = utils.country_holidays("US")

    def test_country(self):
        self.assertEqual(self.holidays.country, "US")

    def test_country_single_year(self):
        h = utils.country_holidays("US", years=2021)
        self.assertEqual(h.years, {2021})

    def test_country_years(self):
        h = utils.country_holidays("US", years=(2015, 2016))
        self.assertEqual(h.years, {2015, 2016})

    def test_country_state(self):
        h = utils.country_holidays("US", subdiv="NY")
        self.assertEqual(h.subdiv, "NY")

    def test_country_province(self):
        h = utils.country_holidays("AU", subdiv="NT")
        self.assertEqual(h.subdiv, "NT")

    def test_exceptions(self):
        self.assertRaises(
            NotImplementedError, lambda: utils.country_holidays("XXXX")
        )
        self.assertRaises(
            NotImplementedError,
            lambda: utils.country_holidays("US", subdiv="XXXX"),
        )
        self.assertRaises(
            NotImplementedError,
            lambda: utils.country_holidays("US", subdiv="XXXX"),
        )


class TestFinancialHolidays(unittest.TestCase):
    def setUp(self):
        self.holidays = utils.financial_holidays("NYSE")

    def test_market(self):
        self.assertEqual(self.holidays.market, "NYSE")

    def test_market_single_year(self):
        h = utils.financial_holidays("NYSE", years=2021)
        self.assertEqual(h.years, {2021})

    def test_market_years(self):
        h = utils.financial_holidays("NYSE", years=(2015, 2016))
        self.assertEqual(h.years, {2015, 2016})

    def test_exceptions(self):
        self.assertRaises(
            NotImplementedError, lambda: utils.financial_holidays("XXXX")
        )
        self.assertRaises(
            NotImplementedError,
            lambda: utils.financial_holidays("NYSE", subdiv="XXXX"),
        )


class TestAllInSameYear(unittest.TestCase):
    """Test that only holidays in the year(s) requested are returned."""

    years = set(range(1950, 2051))

    @pytest.mark.skipif(
        sys.version_info < PYTHON_VERSION,
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

        for country in utils.list_supported_countries():
            for year in self.years:
                for dt in utils.country_holidays(country, years=year):
                    self.assertEqual(dt.year, year)
                    self.assertEqual(type(dt), date)
        self.assertEqual(
            self.years,
            utils.country_holidays(country, years=self.years).years,
        )

    @pytest.mark.skipif(
        sys.version_info < PYTHON_VERSION,
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

        for market in utils.list_supported_financial():
            for year in self.years:
                for dt in utils.financial_holidays(market, years=year):
                    self.assertEqual(dt.year, year)
                    self.assertEqual(type(dt), date)
        self.assertEqual(
            self.years,
            utils.financial_holidays(market, years=self.years).years,
        )


class TestListSupportedEntities(unittest.TestCase):
    def test_list_supported_countries(self):
        supported_countries = utils.list_supported_countries(
            include_aliases=False
        )

        self.assertIn("AR", supported_countries)
        self.assertIn("CA", supported_countries["US"])
        self.assertIn("IM", supported_countries)
        self.assertIn("ZA", supported_countries)

        us_subdivisions = supported_countries["US"]
        self.assertIn("CA", us_subdivisions)
        self.assertTrue(isinstance(us_subdivisions, list))

        countries_files = [
            path
            for path in pathlib.Path("holidays/countries").glob("*.py")
            if not str(path).endswith("__init__.py")
        ]
        self.assertEqual(
            len(countries_files),
            len(supported_countries),
        )

    def test_list_supported_financial(self):
        supported_financial = utils.list_supported_financial(
            include_aliases=False
        )

        self.assertIn("ECB", supported_financial)
        self.assertIn("NYSE", supported_financial)

        nyse = supported_financial["NYSE"]
        self.assertTrue(isinstance(nyse, list))

        financial_files = [
            path
            for path in pathlib.Path("holidays/financial").glob("*.py")
            if not str(path).endswith("__init__.py")
        ]
        self.assertEqual(
            len(financial_files),
            len(supported_financial),
        )
