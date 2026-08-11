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

from holidays.financial.new_zealand_exchange import NewZealandExchange
from tests.common import CommonFinancialTests


class TestNewZealandExchange(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(NewZealandExchange)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_christmas_eve(self):
        name = "Business Day Prior to Christmas Day (markets close at 13:30 NZDT)"
        self.assertNoHolidayName(name)
        dts = (
            "2020-12-24",
            "2021-12-24",
            "2022-12-23",
            "2023-12-22",
            "2024-12-24",
            "2025-12-24",
            "2026-12-24",
        )
        self.assertHalfDayHolidayName(name, dts)
        self.assertHalfDayNonObservedHolidayName(name, dts)
        no_dts = (
            "2022-12-24",
            "2023-12-24",
        )
        self.assertNoHalfDayHolidayName(name, no_dts)
        self.assertNoHalfDayNonObservedHolidayName(name, no_dts)
        self.assertHalfDayHolidayName(name, self.full_range)

    def test_new_years_eve(self):
        name = "Business Day Prior to New Year's Day (markets close at 13:30 NZDT)"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(
            name,
            "2020-12-31",
            "2021-12-31",
            "2022-12-30",
            "2023-12-29",
            "2024-12-31",
            "2025-12-31",
            "2026-12-31",
        )
        self.assertNoHalfDayHolidayName(
            name,
            "2022-12-31",
            "2023-12-31",
        )
        self.assertHalfDayHolidayName(name, self.full_range)

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "New Year's Day"),
            ("2025-01-02", "Day after New Year's Day"),
            ("2025-02-06", "Waitangi Day"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-25", "Anzac Day"),
            ("2025-06-02", "King's Birthday"),
            ("2025-06-20", "Matariki"),
            ("2025-10-27", "Labour Day"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-26", "Boxing Day"),
        )

    def test_half_day_2025(self):
        self.assertHalfDayHolidaysInYear(
            2025,
            ("2025-12-24", "Business Day Prior to Christmas Day (markets close at 13:30 NZDT)"),
            ("2025-12-31", "Business Day Prior to New Year's Day (markets close at 13:30 NZDT)"),
        )
