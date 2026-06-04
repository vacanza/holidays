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

from holidays.calendars.gregorian import FEB, MAR, APR, MAY, JUN, JUL, OCT, NOV, DEC
from holidays.calendars.islamic import _IslamicMabimsLunar


class TestIslamicMabimsLunar(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.calendar = _IslamicMabimsLunar()

    def test_eid_al_fitr_dates(self):
        eid_al_fitr_dates = {
            2001: date(2001, DEC, 16),
            2002: date(2002, DEC, 6),
            2003: date(2003, NOV, 25),
            2006: date(2006, OCT, 24),
            2019: date(2019, JUN, 5),
            2022: date(2022, MAY, 3),
            2023: date(2023, APR, 22),
            2024: date(2024, APR, 10),
            2025: date(2025, MAR, 31),
            2026: date(2026, MAR, 21),
        }
        for year, expected_date in eid_al_fitr_dates.items():
            dates = {dt: is_estimated for dt, is_estimated in self.calendar.eid_al_fitr_dates(year)}
            self.assertIn(expected_date, dates)
            self.assertFalse(dates[expected_date], f"Eid al-Fitr {year} should be confirmed, not estimated")

    def test_eid_al_adha_dates(self):
        eid_al_adha_dates = {
            2001: date(2001, MAR, 6),
            2002: date(2002, FEB, 23),
            2006: date(2006, DEC, 31),
            2010: date(2010, NOV, 17),
            2014: date(2014, OCT, 5),
            2022: date(2022, JUL, 10),
            2023: date(2023, JUN, 29),
            2024: date(2024, JUN, 17),
            2025: date(2025, JUN, 7),
            2026: date(2026, MAY, 27),
        }
        for year, expected_date in eid_al_adha_dates.items():
            dates = {dt: is_estimated for dt, is_estimated in self.calendar.eid_al_adha_dates(year)}
            self.assertIn(expected_date, dates)
            self.assertFalse(dates[expected_date], f"Eid al-Adha {year} should be confirmed, not estimated")

    def test_eid_al_adha_2006_dual_date(self):
        """2006 has two Eid al-Adha dates - Jan 10 and Dec 31."""
        dates = {dt for dt, _ in self.calendar.eid_al_adha_dates(2006)}
        self.assertIn(date(2006, 1, 10), dates)
        self.assertIn(date(2006, 12, 31), dates)

    def test_fallback_to_base_outside_range(self):
        """Years outside 2001-2026 should fall back to base _IslamicLunar dates."""
        dates_1990 = list(self.calendar.eid_al_fitr_dates(1990))
        dates_2030 = list(self.calendar.eid_al_fitr_dates(2030))
        self.assertTrue(len(dates_1990) > 0)
        self.assertTrue(len(dates_2030) > 0)
        # Outside confirmed range should be estimated
        for _, is_estimated in dates_1990:
            self.assertTrue(is_estimated)


if __name__ == "__main__":
    unittest.main()
