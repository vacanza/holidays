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

from holidays.financial.london_stock_exchange import LondonStockExchange, XLON, LSE
from tests.common import CommonFinancialTests


class TestLondonStockExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(LondonStockExchange)

    def test_market_aliases(self):
        self.assertAliases(LondonStockExchange, XLON, LSE)

    def test_no_holidays(self):
        self.assertNoHolidays(LondonStockExchange(years=1999))

    def test_2002(self):
        self.assertHolidays(
            LondonStockExchange(years=2002),
            ("2002-01-01", "New Year's Day"),
            ("2002-03-29", "Good Friday"),
            ("2002-04-01", "Easter Monday"),
            ("2002-05-06", "May Day"),
            ("2002-06-03", "Golden Jubilee of Elizabeth II"),
            ("2002-06-04", "Spring Bank Holiday"),
            ("2002-08-26", "Late Summer Bank Holiday"),
            ("2002-12-25", "Christmas Day"),
            ("2002-12-26", "Boxing Day"),
        )

    def test_2011(self):
        self.assertHolidays(
            LondonStockExchange(years=2011),
            ("2011-01-01", "New Year's Day"),
            ("2011-01-03", "New Year's Day (observed)"),
            ("2011-04-22", "Good Friday"),
            ("2011-04-25", "Easter Monday"),
            ("2011-04-29", "Wedding of William and Catherine"),
            ("2011-05-02", "May Day"),
            ("2011-05-30", "Spring Bank Holiday"),
            ("2011-08-29", "Late Summer Bank Holiday"),
            ("2011-12-25", "Christmas Day"),
            ("2011-12-26", "Boxing Day"),
            ("2011-12-27", "Christmas Day (observed)"),
        )

    def test_2020(self):
        self.assertHolidays(
            LondonStockExchange(years=2020),
            ("2020-01-01", "New Year's Day"),
            ("2020-04-10", "Good Friday"),
            ("2020-04-13", "Easter Monday"),
            ("2020-05-08", "May Day"),
            ("2020-05-25", "Spring Bank Holiday"),
            ("2020-08-31", "Late Summer Bank Holiday"),
            ("2020-12-25", "Christmas Day"),
            ("2020-12-26", "Boxing Day"),
            ("2020-12-28", "Boxing Day (observed)"),
        )

    def test_2021(self):
        self.assertHolidays(
            LondonStockExchange(years=2021),
            ("2021-01-01", "New Year's Day"),
            ("2021-04-02", "Good Friday"),
            ("2021-04-05", "Easter Monday"),
            ("2021-05-03", "May Day"),
            ("2021-05-31", "Spring Bank Holiday"),
            ("2021-08-30", "Late Summer Bank Holiday"),
            ("2021-12-25", "Christmas Day"),
            ("2021-12-26", "Boxing Day"),
            ("2021-12-27", "Christmas Day (observed)"),
            ("2021-12-28", "Boxing Day (observed)"),
        )

    def test_2022(self):
        self.assertHolidays(
            LondonStockExchange(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "New Year's Day (observed)"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-02", "May Day"),
            ("2022-06-02", "Spring Bank Holiday"),
            ("2022-06-03", "Platinum Jubilee of Elizabeth II"),
            ("2022-08-29", "Late Summer Bank Holiday"),
            ("2022-09-19", "State Funeral of Queen Elizabeth II"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
            ("2022-12-27", "Christmas Day (observed)"),
        )

    def test_2023(self):
        self.assertHolidays(
            LondonStockExchange(years=2023),
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-01", "May Day"),
            ("2023-05-08", "Coronation of Charles III"),
            ("2023-05-29", "Spring Bank Holiday"),
            ("2023-08-28", "Late Summer Bank Holiday"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Boxing Day"),
        )

    def test_2024(self):
        self.assertHolidays(
            LondonStockExchange(years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-06", "May Day"),
            ("2024-05-27", "Spring Bank Holiday"),
            ("2024-08-26", "Late Summer Bank Holiday"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Boxing Day"),
        )

    def test_2025(self):
        self.assertHolidays(
            LondonStockExchange(years=2025),
            ("2025-01-01", "New Year's Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-05-05", "May Day"),
            ("2025-05-26", "Spring Bank Holiday"),
            ("2025-08-25", "Late Summer Bank Holiday"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )
