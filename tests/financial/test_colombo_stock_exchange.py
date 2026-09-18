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
        expected_half_days = (
            ("2018-04-13", "Day prior to Sinhala & Tamil New Year day"),
            (
                "2019-04-12",
                "Special Bank Half-holiday on account of Day prior "
                "to Sinhala & Tamil New Year Day falling on a Saturday",
            ),
            (
                "2021-04-30",
                "Additional half-holiday on account of the May Day falling on a Saturday",
            ),
            (
                "2021-12-24",
                "Additional half-holiday on account of the Christmas Day falling on a Saturday",
            ),
            (
                "2023-02-03",
                "Additional half holiday in lieu of the Independence Day falling on Saturday",
            ),
            (
                "2023-05-04",
                "Additional half holiday in lieu of Day Following Vesak "
                "Full Moon Poya Day falling on Saturday",
            ),
            (
                "2024-04-10",
                "Additional half holiday in lieu of Sinhala "
                "& Tamil New Year Day falling on Saturday",
            ),
            (
                "2026-04-30",
                "Additional half holiday in lieu of Day Following Vesak "
                "Full Moon Poya Day falling on Saturday",
            ),
        )
        for dt_str, name in expected_half_days:
            year, month, day = (int(x) for x in dt_str.split("-"))
            self.assertIn(date(year, month, day), self.holidays_half_day)
            self.assertIn(name, self.holidays_half_day.get(dt_str))
