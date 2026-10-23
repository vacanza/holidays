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

from holidays import financial_holidays
from holidays.constants import HALF_DAY
from holidays.financial.euronext import XAMS, XBRU, XDUB, XLIS, XMIL, XOSL, XPAR, Euronext
from tests.common import CommonFinancialTests


class TestEuronext(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Euronext, with_subdiv_categories=True)

    def test_no_holidays(self):
        self.assertNoHolidays(
            Euronext(subdiv="XMIL", categories=HALF_DAY, years=range(2021, 2050))
        )

    def test_market_subclasses_default_subdivision(self):
        # Each market subclass defaults to its own subdivision, so the
        # market-specific holidays are included without an explicit subdiv.
        self.assertEqual(XPAR(years=2025).subdiv, "XPAR")
        self.assertEqual(XAMS(years=2025).subdiv, "XAMS")
        self.assertEqual(XBRU(years=2025).subdiv, "XBRU")
        self.assertEqual(XDUB(years=2025).subdiv, "XDUB")
        self.assertEqual(XLIS(years=2025).subdiv, "XLIS")
        self.assertEqual(XMIL(years=2025).subdiv, "XMIL")
        self.assertEqual(XOSL(years=2025).subdiv, "XOSL")
        # Dublin, Milan and Oslo specific holidays.
        self.assertIn("2025-05-05", XDUB(years=2025))
        self.assertIn("2025-08-15", XMIL(years=2025))
        self.assertIn("2025-04-17", XOSL(years=2025))
        self.assertIn("2025-05-17", XOSL(years=2025))
        # The same applies when the market is requested by its code.
        self.assertIn("2025-05-17", financial_holidays("XOSL", years=2025))
        self.assertIn("2025-08-15", financial_holidays("XMIL", years=2025))
        # An explicitly passed subdivision is respected, whether it is
        # passed as a keyword or as a positional argument.
        self.assertEqual(XOSL(subdiv="XAMS", years=2025).subdiv, "XAMS")
        self.assertEqual(XOSL(2025, True, True, "XAMS").subdiv, "XAMS")

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in self.full_range))

    def test_good_friday(self):
        name = "Good Friday"
        self.assertHolidayName(
            name,
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
            "2026-04-03",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Easter Monday"
        self.assertHolidayName(
            name,
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
            "2026-04-06",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labour_day(self):
        self.assertHolidayName("Labour Day", (f"{year}-05-01" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in self.full_range))

    def test_st_stephens_day(self):
        self.assertHolidayName("St Stephen's Day", (f"{year}-12-26" for year in self.full_range))

    def test_christmas_eve(self):
        name = "Christmas Eve"
        self.assertHalfDayHolidayName(
            name,
            "2021-12-24",
            "2024-12-24",
            "2025-12-24",
            "2026-12-24",
        )
        self.assertNoHalfDayHolidayName(name, "2022-12-24", "2023-12-24")

    def test_new_years_eve(self):
        name = "New Year's Eve"
        self.assertHalfDayHolidayName(
            name,
            "2021-12-31",
            "2024-12-31",
            "2025-12-31",
            "2026-12-31",
        )
        self.assertNoHalfDayHolidayName(name, "2022-12-31", "2023-12-31")

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "New Year's Day"),
            ("2024-03-29", "Good Friday"),
            ("2024-04-01", "Easter Monday"),
            ("2024-05-01", "Labour Day"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "St Stephen's Day"),
        )

    # Dublin (XDUB).

    def test_dublin_irish_may_bank_holiday(self):
        self.assertSubdivXdubHolidayName(
            "Irish May Bank Holiday",
            "2021-05-03",
            "2022-05-02",
            "2023-05-01",
            "2024-05-06",
            "2025-05-05",
            "2026-05-04",
        )

    def test_dublin_weekend_substitutes(self):
        # New Year's Day substitutes.
        self.assertSubdivXdubHolidayName("New Year's Day", "2022-01-03", "2023-01-02")
        # Christmas Day substitutes.
        self.assertSubdivXdubHolidayName("Christmas Day", "2021-12-27", "2022-12-27")
        # St Stephen's Day substitutes.
        self.assertSubdivXdubHolidayName("St Stephen's Day", "2021-12-28", "2026-12-28")
        # Other markets have no weekend substitutes.
        self.assertNoSubdivXparHoliday("2022-01-03", "2023-01-02", "2022-12-27")

    def test_dublin_half_day_substitutes(self):
        # Christmas Eve half trading day observed on the preceding Friday.
        self.assertSubdivXdubHalfDayHolidayName("Christmas Eve", "2022-12-23", "2023-12-22")
        # New Year's Eve half trading day observed on the preceding Friday.
        self.assertSubdivXdubHalfDayHolidayName("New Year's Eve", "2022-12-30", "2023-12-29")
        self.assertNoSubdivXdubHalfDayHolidayName("Christmas Eve", "2022-12-24", "2023-12-24")
        self.assertNoSubdivXdubHalfDayHolidayName("New Year's Eve", "2022-12-31", "2023-12-31")

    def test_dublin_2022(self):
        self.assertSubdivXdubHolidayDatesInYear(
            2022,
            "2022-01-01",
            "2022-01-03",
            "2022-04-15",
            "2022-04-18",
            "2022-05-01",
            "2022-05-02",
            "2022-12-25",
            "2022-12-26",
            "2022-12-27",
        )

    # Milan (XMIL).

    def test_milan_assumption_day(self):
        name = "Assumption Day"
        self.assertSubdivXmilHolidayName(
            name, (f"{year}-08-15" for year in range(2023, self.end_year))
        )
        self.assertNoSubdivXmilHolidayName(name, 2021, 2022)

    def test_milan_christmas_eve_and_new_years_eve(self):
        # Full-day closures in Milan (not half trading days).
        self.assertSubdivXmilHolidayName("Christmas Eve", "2024-12-24", "2025-12-24", "2026-12-24")
        self.assertSubdivXmilHolidayName(
            "New Year's Eve", "2024-12-31", "2025-12-31", "2026-12-31"
        )
        self.assertNoSubdivXmilHalfDayHolidayName("Christmas Eve", "2024-12-24")
        self.assertNoSubdivXmilHalfDayHolidayName("New Year's Eve", "2024-12-31")

    def test_milan_2025(self):
        self.assertSubdivXmilHolidayDatesInYear(
            2025,
            "2025-01-01",
            "2025-04-18",
            "2025-04-21",
            "2025-05-01",
            "2025-08-15",
            "2025-12-24",
            "2025-12-25",
            "2025-12-26",
            "2025-12-31",
        )

    # Oslo (XOSL).

    def test_oslo_maundy_thursday(self):
        name = "Maundy Thursday"
        self.assertSubdivXoslHolidayName(
            name,
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
            "2026-04-02",
        )
        self.assertSubdivXoslHolidayName(name, self.full_range)

    def test_oslo_ascension_day(self):
        name = "Ascension Day"
        self.assertSubdivXoslHolidayName(
            name,
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
            "2026-05-14",
        )
        self.assertSubdivXoslHolidayName(name, self.full_range)

    def test_oslo_constitution_day(self):
        self.assertSubdivXoslHolidayName(
            "Constitution Day", (f"{year}-05-17" for year in self.full_range)
        )

    def test_oslo_whit_monday(self):
        name = "Whit Monday"
        self.assertSubdivXoslHolidayName(
            name,
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
            "2026-05-25",
        )
        self.assertSubdivXoslHolidayName(name, self.full_range)

    def test_oslo_christmas_eve_and_new_years_eve(self):
        # Full-day closures in Oslo (not half trading days).
        self.assertSubdivXoslHolidayName("Christmas Eve", "2024-12-24", "2025-12-24", "2026-12-24")
        self.assertSubdivXoslHolidayName(
            "New Year's Eve", "2024-12-31", "2025-12-31", "2026-12-31"
        )
        self.assertNoSubdivXoslHalfDayHolidayName("Christmas Eve", "2024-12-24")
        self.assertNoSubdivXoslHalfDayHolidayName("New Year's Eve", "2024-12-31")

    def test_oslo_wednesday_before_easter(self):
        name = "Wednesday before Easter"
        self.assertSubdivXoslHalfDayHolidayName(
            name,
            "2021-03-31",
            "2022-04-13",
            "2023-04-05",
            "2024-03-27",
            "2025-04-16",
            "2026-04-01",
        )
        self.assertSubdivXoslHalfDayHolidayName(name, self.full_range)

    def test_oslo_2024(self):
        self.assertSubdivXoslHolidayDatesInYear(
            2024,
            "2024-01-01",
            "2024-03-28",
            "2024-03-29",
            "2024-04-01",
            "2024-05-01",
            "2024-05-09",
            "2024-05-17",
            "2024-05-20",
            "2024-12-24",
            "2024-12-25",
            "2024-12-26",
            "2024-12-31",
        )
