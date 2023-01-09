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
from unittest import mock

from dateutil.relativedelta import relativedelta

import holidays
from holidays.countries.israel import Israel


class TestIsrael(unittest.TestCase):
    def test_purim_day(self):
        il_holidays = holidays.IL(years=[2017], observed=True)
        self.assertListEqual(
            il_holidays.get_list(date(2017, 3, 11)), ["Purim - Eve"]
        )
        self.assertListEqual(
            il_holidays.get_list(date(2017, 3, 12)), ["Purim"]
        )
        self.assertListEqual(
            il_holidays.get_list(date(2017, 3, 13)), ["Shushan Purim"]
        )

    def test_memorial_day(self):
        self._test_observed_holidays("Memorial Day")
        self._test_nonobserved_holidays("Memorial Day")

    def test_independence_day(self):
        self._test_observed_holidays("Independence Day")

    def _test_observed_holidays(self, holiday_name):
        days_delta = 0 if holiday_name == "Memorial Day" else 1

        # Postponed
        il_holidays = holidays.IL(years=[2017], observed=True)
        official_memorial_day = date(2017, 4, 30) + relativedelta(
            days=days_delta
        )
        observed_memorial_day = date(2017, 5, 1) + relativedelta(
            days=days_delta
        )
        self.assertIn(official_memorial_day, il_holidays)
        self.assertIn(holiday_name, il_holidays[official_memorial_day])
        self.assertIn(observed_memorial_day, il_holidays)
        self.assertIn(
            holiday_name + " (Observed)", il_holidays[observed_memorial_day]
        )

        # Earlier
        il_holidays = holidays.IL(years=[2018], observed=True)
        official_memorial_day = date(2018, 4, 19) + relativedelta(
            days=days_delta
        )
        observed_memorial_day = date(2018, 4, 18) + relativedelta(
            days=days_delta
        )
        self.assertIn(official_memorial_day, il_holidays)
        self.assertIn(holiday_name, il_holidays[official_memorial_day])
        self.assertIn(observed_memorial_day, il_holidays)
        self.assertIn(
            holiday_name + " (Observed)", il_holidays[observed_memorial_day]
        )

        # On time
        il_holidays = holidays.IL(years=[2020], observed=True)
        official_memorial_day = date(2020, 4, 28) + relativedelta(
            days=days_delta
        )
        self.assertIn(official_memorial_day, il_holidays)
        self.assertIn(holiday_name, il_holidays[official_memorial_day])

        for names in il_holidays.values():
            self.assertNotIn(holiday_name + " (Observed)", names)

    def _test_nonobserved_holidays(self, holiday_name):
        days_delta = 0 if holiday_name == "Memorial Day" else 1

        # Postponed
        il_holidays = holidays.IL(years=[2017], observed=False)
        official_memorial_day = date(2017, 4, 30) + relativedelta(
            days=days_delta
        )
        observed_memorial_day = date(2017, 5, 1) + relativedelta(
            days=days_delta
        )
        self.assertIn(official_memorial_day, il_holidays)
        self.assertIn(holiday_name, il_holidays[official_memorial_day])
        self.assertNotEqual(il_holidays[observed_memorial_day], "Memorial Day")

        # Earlier
        il_holidays = holidays.IL(years=[2018], observed=False)
        official_memorial_day = date(2018, 4, 19) + relativedelta(
            days=days_delta
        )
        observed_memorial_day = date(2018, 4, 18) + relativedelta(
            days=days_delta
        )
        self.assertIn(official_memorial_day, il_holidays)
        self.assertIn(holiday_name, il_holidays[official_memorial_day])
        self.assertNotIn(observed_memorial_day, il_holidays)

        # On time
        il_holidays = holidays.IL(years=[2020], observed=False)
        official_memorial_day = date(2020, 4, 28) + relativedelta(
            days=days_delta
        )
        self.assertIn(official_memorial_day, il_holidays)
        self.assertIn(holiday_name, il_holidays[official_memorial_day])

        for names in il_holidays.values():
            self.assertNotIn(holiday_name + " (Observed)", names)

    @mock.patch("importlib.util.find_spec", return_value=None)
    def test_dependency_convertdate(self, find_spec):
        self.assertRaises(ImportError, lambda: Israel())
