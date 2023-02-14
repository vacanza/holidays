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
from holidays.constants import FEB, MAR, MAY, JUN, JUL, AUG, OCT


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
        for country in utils.list_supported_countries():
            for year in range(date.today().year - 10, date.today().year + 3):
                for holiday in utils.country_holidays(country, years=year):
                    self.assertEqual(holiday.year, year)


class TestThaiLuniSolarCalendar(unittest.TestCase):
    def setUp(self) -> None:
        super().setUpClass()
        self.calendar = utils._ThaiLuniSolar()

    def test_asarnha_bucha_date(self):
        asarnha_bucha_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, JUL, 13),
            2023: date(2023, AUG, 1),
            2024: date(2024, JUL, 20),
            2025: date(2025, JUL, 10),
        }
        for year in asarnha_bucha_year_date:
            self.assertEqual(
                asarnha_bucha_year_date[year],
                self.calendar.asarnha_bucha_date(year),
            )

    def test_atthami_bucha_date(self):
        atthami_bucha_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, MAY, 23),
            2023: date(2023, JUN, 11),
            2024: date(2024, MAY, 30),
            2025: date(2025, MAY, 19),
        }
        for year in atthami_bucha_year_date:
            self.assertEqual(
                atthami_bucha_year_date[year],
                self.calendar.atthami_bucha_date(year),
            )

    def test_khao_phansa_date(self):
        khao_phansa_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, JUL, 14),
            2023: date(2023, AUG, 2),
            2024: date(2024, JUL, 21),
            2025: date(2025, JUL, 11),
        }
        for year in khao_phansa_year_date:
            self.assertEqual(
                khao_phansa_year_date[year],
                self.calendar.khao_phansa_date(year),
            )

    def test_makha_bucha_date(self):
        makha_bucha_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, FEB, 16),
            2023: date(2023, MAR, 6),
            2024: date(2024, FEB, 24),
            2025: date(2025, FEB, 12),
        }
        for year in makha_bucha_year_date:
            self.assertEqual(
                makha_bucha_year_date[year],
                self.calendar.makha_bucha_date(year),
            )

    def test_ok_phansa_date(self):
        ok_phansa_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, OCT, 10),
            2023: date(2023, OCT, 29),
            2024: date(2024, OCT, 17),
            2025: date(2025, OCT, 7),
        }
        for year in ok_phansa_year_date:
            self.assertEqual(
                ok_phansa_year_date[year],
                self.calendar.ok_phansa_date(year),
            )

    def test_visakha_bucha_date(self):
        visakha_bucha_year_date = {
            self.calendar.START_YEAR - 1: None,
            self.calendar.END_YEAR + 1: None,
            2022: date(2022, MAY, 15),
            2023: date(2023, JUN, 3),
            2024: date(2024, MAY, 22),
            2025: date(2025, MAY, 11),
        }
        for year in visakha_bucha_year_date:
            self.assertEqual(
                visakha_bucha_year_date[year],
                self.calendar.visakha_bucha_date(year),
            )
