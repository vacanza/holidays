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
from dateutil.relativedelta import relativedelta

import holidays


class TestUnitedStatesMarket(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.UnitedStatesMarket()

    def test_new_years(self):
        for dt in [
            date(1900, 1, 1),
            date(1930, 1, 1),
            date(1950, 1, 2),
            date(1999, 1, 1),
            date(2000, 1, 3),
            date(2010, 1, 1),
            date(2018, 1, 1),
            date(2019, 1, 1),
            date(2020, 1, 1),
            date(2021, 1, 1),
            date(2022, 1, 3),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)

    def test_mlk(self):
        for dt in [
            date(1900, 1, 15),
            date(1930, 1, 20),
            date(1950, 1, 16),
            date(1999, 1, 18),
            date(2000, 1, 17),
            date(2010, 1, 18),
            date(2018, 1, 15),
            date(2019, 1, 21),
            date(2020, 1, 20),
            date(2021, 1, 18),
            date(2022, 1, 17),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

    def test_pres(self):
        for dt in [
            date(1900, 2, 19),
            date(1930, 2, 17),
            date(1950, 2, 20),
            date(1999, 2, 15),
            date(2000, 2, 21),
            date(2010, 2, 15),
            date(2018, 2, 19),
            date(2019, 2, 18),
            date(2020, 2, 17),
            date(2021, 2, 15),
            date(2022, 2, 21),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

    def test_good_friday(self):
        for dt in [
            date(1900, 4, 13),
            date(1901, 4, 5),
            date(1902, 3, 28),
            date(1999, 4, 2),
            date(2000, 4, 21),
            date(2010, 4, 2),
            date(2018, 3, 30),
            date(2019, 4, 19),
            date(2020, 4, 10),
            date(2021, 4, 2),
            date(2022, 4, 15),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

    def test_memday(self):
        for dt in [
            date(1901, 5, 27),
            date(1902, 5, 26),
            date(1950, 5, 29),
            date(1999, 5, 31),
            date(2000, 5, 29),
            date(2010, 5, 31),
            date(2018, 5, 28),
            date(2019, 5, 27),
            date(2020, 5, 25),
            date(2021, 5, 31),
            date(2022, 5, 30),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

    def test_juneteenth(self):
        for dt in [
            date(1901, 6, 19),
            date(1902, 6, 19),
            date(1950, 6, 19),
            date(1999, 6, 18),
            date(2000, 6, 19),
            date(2010, 6, 18),
            date(2018, 6, 19),
            date(2019, 6, 19),
            date(2020, 6, 19),
            date(2021, 6, 18),
            date(2022, 6, 20),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

    def test_laborday(self):
        for dt in [
            date(1901, 9, 2),
            date(1902, 9, 1),
            date(1950, 9, 4),
            date(1999, 9, 6),
            date(2000, 9, 4),
            date(2010, 9, 6),
            date(2018, 9, 3),
            date(2019, 9, 2),
            date(2020, 9, 7),
            date(2021, 9, 6),
            date(2022, 9, 5),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

    def test_thxgiving(self):
        for dt in [
            date(1901, 11, 28),
            date(1902, 11, 27),
            date(1950, 11, 23),
            date(1999, 11, 25),
            date(2000, 11, 23),
            date(2010, 11, 25),
            date(2018, 11, 22),
            date(2019, 11, 28),
            date(2020, 11, 26),
            date(2021, 11, 25),
            date(2022, 11, 24),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+7), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

    def test_christmas_day(self):
        for dt in [
            date(1901, 12, 25),
            date(1902, 12, 25),
            date(1950, 12, 25),
            date(1999, 12, 24),
            date(2000, 12, 25),
            date(2010, 12, 24),
            date(2018, 12, 25),
            date(2019, 12, 25),
            date(2020, 12, 25),
            date(2021, 12, 24),
            date(2022, 12, 26),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-7), self.holidays)

    def test_all_holidays_present(self):
        usmkt_2015 = holidays.UnitedStatesMarket(years=[2015])
        all_holidays = [
            "New Year's Day (observed)",
            "MLK Jr. Day",
            "President's Day",
            "Good Friday",
            "Memorial Day",
            "Juneteenth (observed)",
            "Independence Day (observed)",
            "Labor Day",
            "Thanksgiving Day",
            "Christmas Day (observed)",
        ]
        for holiday in all_holidays:
            self.assertIn(holiday, usmkt_2015.values())
