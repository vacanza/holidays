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

    def test_eager_year_population(self):
        hol = ColomboStockExchange(years=[2020])
        self.assertEqual(hol.years, {2020})
        self.assertIn("2020-01-01", hol)

    def test_eager_year_population_positional(self):
        hol = ColomboStockExchange([2020])
        self.assertEqual(hol.years, {2020})
        self.assertIn("2020-01-01", hol)

    def test_base_srilanka_holidays(self):
        self.assertIn(date(2020, 2, 4), self.holidays)

    def test_ad_hoc_closures(self):
        expected_ad_hoc_closures = (
            ("2018-02-05", "National Day Holiday"),
            ("2018-04-30", "Vesak Holiday"),
            ("2019-01-01", "CSE Customary Holiday"),
            (
                "2019-04-15",
                "Special Bank Holiday on account of Sinhala & Tamil New Year Day "
                "falling on a Sunday",
            ),
            (
                "2019-05-20",
                "Special Bank Holiday on account of Day Following Vesak Full Moon Poya Day "
                "falling on a Sunday",
            ),
            (
                "2019-11-11",
                "Special Bank Holiday on account of Holy Prophet's Birthday falling on a Sunday",
            ),
            ("2020-01-01", "CSE Customary Holiday"),
            ("2020-03-20", "Market closure due to COVID-19"),
            (
                "2020-04-14",
                "Special Bank Holiday on account of the Day prior to Sinhala & Tamil New Year Day "
                "falling on a Sunday",
            ),
            ("2021-01-01", "CSE Customary Holiday"),
            ("2022-05-02", "Additional holiday in lieu of May Day falling on Sunday"),
            (
                "2022-10-10",
                "Additional holiday in lieu of Milad-Un-Nabi (Holy Prophet's Birthday) "
                "falling on Sunday",
            ),
            ("2022-12-26", "Additional holiday in lieu of Christmas Day falling on Sunday"),
            (
                "2023-01-16",
                "Additional holiday in lieu of Tamil Thai Pongal Day falling on Sunday",
            ),
            ("2024-01-01", "CSE Customary Holiday"),
            ("2024-02-05", "Additional holiday in lieu of Independence Day falling on Sunday"),
            ("2025-01-01", "Customary Holiday"),
            ("2025-04-15", "Special Bank Holiday"),
            ("2026-01-01", "CSE Customary Holiday"),
        )
        for dt_str, name in expected_ad_hoc_closures:
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
