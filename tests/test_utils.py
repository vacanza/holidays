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

import unittest
from datetime import date

from holidays import utils


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

    def setUp(self):
        self.countries = utils.list_supported_countries()

    def tearDown(self):
        """https://stackoverflow.com/questions/4414234/"""

        def list2reason(exc_list):
            if exc_list and exc_list[-1][0] is self:
                return exc_list[-1][1]

        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = list2reason(result.errors)
        failure = list2reason(result.failures)
        text = error if error else failure
        if text:
            print(
                f"{text.splitlines()[-1]} in country {self.country}: "
                f"holiday {self.hol} returned for year {self.year}"
            )
            print(
                utils.country_holidays(
                    self.country, subdiv=None, years=[self.year]
                ).get_list(self.hol)
            )

    def test_all_countries(self):
        """
        Only holidays in the year(s) requested should be returned. This
        ensures that we avoid triggering a "RuntimeError: dictionary changed
        size during iteration" error.

        Here we test all countries for the 12-year period starting ten years
        ago and ending 2 years from now.

        This is logic test and not a code compatibility test, so for expediency
        we only run it once on the latest Python version.
        """
        for country in self.countries:
            for year in range(date.today().year - 10, date.today().year + 3):
                for holiday in utils.country_holidays(country, years=year):
                    self.assertEqual(holiday.year, year)
