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

from unittest import TestCase

from holidays.financial.germany_exchange import GermanyStockExchange, XETR
from tests.common import CommonFinancialTests


class TestGermanyStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(GermanyStockExchange)

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in self.full_range))

    def test_good_friday(self):
        self.assertHolidayName(
            "Good Friday",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )

    def test_easter_monday(self):
        self.assertHolidayName(
            "Easter Monday",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )

    def test_labour_day(self):
        self.assertHolidayName("Labour Day", (f"{year}-05-01" for year in self.full_range))

    def test_whit_monday(self):
        self.assertHolidayName(
            "Whit Monday",
            "2020-06-01",
            "2021-05-24",
        )
        self.assertNoHolidayName(
            "Whit Monday",
            "2022-06-06",
            "2023-05-29",
        )

    def test_christmas_eve(self):
        self.assertHolidayName("Christmas Eve", (f"{year}-12-24" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in self.full_range))

    def test_boxing_day(self):
        self.assertHolidayName("Boxing Day", (f"{year}-12-26" for year in self.full_range))

    def test_new_years_eve(self):
        self.assertHolidayName("New Year's Eve", (f"{year}-12-31" for year in self.full_range))

    def test_xetr(self):
        self.assertIsInstance(XETR(), GermanyStockExchange)
