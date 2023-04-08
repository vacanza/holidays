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

import unittest
from datetime import date
from datetime import timedelta as td

import holidays


class TestIsrael(unittest.TestCase):
    def _test_observed_holidays(self, holiday_name):
        days_delta = 0 if holiday_name == "Memorial Day" else 1

        # Postponed
        il_holidays = holidays.IL(years=2017, observed=True)
        official_holiday = date(2017, 4, 30) + td(days=days_delta)
        observed_holiday = official_holiday + td(days=+1)
        self.assertNotIn(holiday_name, il_holidays.get(official_holiday, ""))
        self.assertIn(observed_holiday, il_holidays)
        self.assertIn(
            holiday_name + " (Observed)", il_holidays.get(observed_holiday)
        )

        # Earlier
        il_holidays = holidays.IL(years=2018, observed=True)
        official_holiday = date(2018, 4, 19) + td(days=days_delta)
        observed_holiday = official_holiday + td(days=-1)
        self.assertIn(observed_holiday, il_holidays)
        self.assertNotIn(holiday_name, il_holidays.get(official_holiday, ""))
        self.assertIn(
            holiday_name + " (Observed)", il_holidays.get(observed_holiday)
        )

        # On time
        il_holidays = holidays.IL(years=2020, observed=True)
        official_holiday = date(2020, 4, 28) + td(days=days_delta)
        self.assertIn(official_holiday, il_holidays)
        self.assertIn(holiday_name, il_holidays.get(official_holiday))
        for name in il_holidays.values():
            self.assertNotIn(holiday_name + " (Observed)", name)

    def _test_nonobserved_holidays(self, holiday_name):
        days_delta = 0 if holiday_name == "Memorial Day" else 1

        # Postponed
        il_holidays = holidays.IL(years=2017, observed=False)
        official_holiday = date(2017, 4, 30) + td(days=days_delta)
        observed_holiday = official_holiday + td(days=+1)
        self.assertIn(official_holiday, il_holidays)
        self.assertIn(holiday_name, il_holidays.get(official_holiday))
        self.assertNotEqual(il_holidays.get(observed_holiday), holiday_name)

        # Earlier
        il_holidays = holidays.IL(years=2018, observed=False)
        official_holiday = date(2018, 4, 19) + td(days=days_delta)
        observed_holiday = official_holiday + td(days=-1)
        self.assertIn(official_holiday, il_holidays)
        self.assertIn(holiday_name, il_holidays.get(official_holiday))
        self.assertNotIn(observed_holiday, il_holidays)

        # On time
        il_holidays = holidays.IL(years=2020, observed=False)
        official_holiday = date(2020, 4, 28) + td(days=days_delta)
        self.assertIn(official_holiday, il_holidays)
        self.assertIn(holiday_name, il_holidays.get(official_holiday))
        for name in il_holidays.values():
            self.assertNotIn(holiday_name + " (Observed)", name)

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
