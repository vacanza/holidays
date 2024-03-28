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

from datetime import date
from unittest import TestCase

from holidays.countries.serbia import Serbia, RS, SRB
from tests.common import CommonCountryTests


class TestSerbia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Serbia)

    def test_country_aliases(self):
        self.assertAliases(Serbia, RS, SRB)

    def test_new_year(self):
        # If January 1st is in Weekend, test oberved
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 1, 2), self.holidays)
        self.assertIn(date(2017, 1, 3), self.holidays)
        self.holidays.observed = False
        self.assertNotIn(date(2017, 1, 3), self.holidays)

    def test_statehood_day(self):
        # If February 15th is in Weekend, test oberved
        self.assertIn(date(2020, 2, 15), self.holidays)
        self.assertIn(date(2020, 2, 16), self.holidays)
        self.assertIn(date(2020, 2, 17), self.holidays)
        self.holidays.observed = False
        self.assertNotIn(date(2020, 2, 17), self.holidays)

    def test_labour_day(self):
        # If May 1st is in Weekend, test oberved
        self.assertIn(date(2016, 5, 1), self.holidays)
        self.assertIn(date(2016, 5, 2), self.holidays)
        self.assertIn(date(2016, 5, 3), self.holidays)
        self.assertIn(date(2021, 5, 1), self.holidays)
        self.assertIn(date(2021, 5, 2), self.holidays)
        self.assertIn(date(2021, 5, 3), self.holidays)
        self.assertIn(date(2021, 5, 4), self.holidays)
        self.holidays.observed = False
        self.assertNotIn(date(2016, 5, 3), self.holidays)
        self.assertIn(date(2021, 5, 3), self.holidays)
        self.assertNotIn(date(2021, 5, 4), self.holidays)

    def test_armistice_day(self):
        # If November 11th is in Weekend, test oberved
        self.assertIn(date(2018, 11, 11), self.holidays)
        self.assertIn(date(2018, 11, 12), self.holidays)
        self.holidays.observed = False
        self.assertNotIn(date(2018, 11, 12), self.holidays)

    def test_religious_holidays(self):
        # Orthodox Christmas
        self.assertIn(date(2020, 1, 7), self.holidays)
        self.assertNotIn(date(2020, 1, 8), self.holidays)
        # Orthodox Easter
        self.assertNotIn(date(2020, 4, 16), self.holidays)
        self.assertIn(date(2020, 4, 17), self.holidays)
        self.assertIn(date(2020, 4, 18), self.holidays)
        self.assertIn(date(2020, 4, 19), self.holidays)
        self.assertIn(date(2020, 4, 20), self.holidays)
        self.assertNotIn(date(2020, 4, 21), self.holidays)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Нова година"),
            ("2022-01-02", "Нова година"),
            ("2022-01-03", "Нова година (слободан дан)"),
            ("2022-01-07", "Божић"),
            ("2022-02-15", "Дан државности Србије"),
            ("2022-02-16", "Дан државности Србије"),
            ("2022-04-22", "Велики петак"),
            ("2022-04-23", "Велика субота"),
            ("2022-04-24", "Васкрс"),
            ("2022-04-25", "Други дан Васкрса"),
            ("2022-05-01", "Празник рада"),
            ("2022-05-02", "Празник рада"),
            ("2022-05-03", "Празник рада (слободан дан)"),
            ("2022-11-11", "Дан примирја у Првом светском рату"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-01-07", "Orthodox Christmas Day"),
            ("2022-02-15", "Statehood Day"),
            ("2022-02-16", "Statehood Day"),
            ("2022-04-22", "Good Friday"),
            ("2022-04-23", "Holy Saturday"),
            ("2022-04-24", "Easter Sunday"),
            ("2022-04-25", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Labor Day"),
            ("2022-05-03", "Labor Day (observed)"),
            ("2022-11-11", "Armistice Day"),
        )
