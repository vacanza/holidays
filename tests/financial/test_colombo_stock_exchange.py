#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date

from holidays.financial.colombo_stock_exchange import ColomboStockExchange


class TestColomboStockExchange(unittest.TestCase):
    def setUp(self):
        self.holidays = ColomboStockExchange()

        self.holidays_half_day = ColomboStockExchange(categories=("half_day"))

    def test_market_code(self):
        self.assertEqual(self.holidays.market, "XCOL")

    def test_base_srilanka_holidays(self):
        self.assertIn(date(2020, 2, 4), self.holidays)

    def test_ad_hoc_closures(self):
        for dt_str, name in self.holidays.static_holidays.items():
            year, month, day = (int(x) for x in dt_str.split("-"))
            self.assertIn(date(year, month, day), self.holidays)
            self.assertIn(name, self.holidays.get(dt_str))

    def test_half_days(self):
        for dt_str, name in self.holidays_half_day.static_half_days.items():
            year, month, day = (int(x) for x in dt_str.split("-"))
            self.assertIn(date(year, month, day), self.holidays_half_day)
            self.assertIn(name, self.holidays_half_day.get(dt_str))
