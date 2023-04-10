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

import warnings
from datetime import date

from holidays.constants import JAN, MAR, APR, MAY, JUL, SEP, NOV, DEC
from holidays.countries.marshall_islands import HolidaysMH, MH, MHL
from tests.common import TestCase


class TestMH(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HolidaysMH)
        warnings.simplefilter("ignore")

    def test_country_aliases(self):
        self.assertCountryAliases(HolidaysMH, MH, MHL)

    def test_2022(self):
        # https://www.register-iri.com/info-center/the-marshall-islands/rmi-national-holidays/
        year = 2022
        self.assertIn(date(year, JAN, 1), self.holidays)
        self.assertIn(date(year, JAN, 3), self.holidays)
        self.assertIn(date(year, APR, 15), self.holidays)
        self.assertIn(date(year, MAY, 1), self.holidays)
        self.assertIn(date(year, JUL, 1), self.holidays)
        self.assertIn(date(year, SEP, 2), self.holidays)
        self.assertIn(date(year, SEP, 30), self.holidays)
        self.assertIn(date(year, NOV, 17), self.holidays)
        self.assertIn(date(year, DEC, 2), self.holidays)
        self.assertIn(date(year, DEC, 25), self.holidays)
        self.assertIn(date(year, DEC, 26), self.holidays)
        # 2023: total holidays (10 + 2 falling on a Sunday)
        self.assertEqual(10 + 2, len(MH(years=[year])))

    def test_2023(self):
        year = 2023
        self.assertIn(date(year, JAN, 1), self.holidays)
        self.assertIn(date(year, JAN, 2), self.holidays)
        self.assertIn(date(year, MAR, 1), self.holidays)
        self.assertIn(date(year, APR, 7), self.holidays)
        self.assertIn(date(year, MAY, 1), self.holidays)
        self.assertIn(date(year, JUL, 7), self.holidays)
        self.assertIn(date(year, SEP, 1), self.holidays)
        self.assertIn(date(year, SEP, 29), self.holidays)
        self.assertIn(date(year, NOV, 17), self.holidays)
        self.assertIn(date(year, DEC, 1), self.holidays)
        self.assertIn(date(year, DEC, 25), self.holidays)
        # 2023: total holidays (10 + 1 falling on a Sunday)
        self.assertEqual(10 + 1, len(MH(years=[year])))

    def test_not_observed(self):
        self.assertNotIn(date(2023, JAN, 2), MH(observed=False))
