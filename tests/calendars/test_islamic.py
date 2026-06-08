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
            dates = {dt: est for dt, est in self.calendar.eid_al_fitr_dates(year)}
            self.assertIn(expected_date, dates)
            self.assertFalse(dates[expected_date], f"Eid al-Fitr {year} should be confirmed")

    def test_eid_al_adha_dates(self):
        eid_al_adha_dates = {
            2002: date(2002, FEB, 23),
            2010: date(2010, NOV, 17),
            2022: date(2022, JUL, 10),
            2023: date(2023, JUN, 29),
            2024: date(2024, JUN, 17),
            2025: date(2025, JUN, 7),
            2026: date(2026, MAY, 27),
        }
        for year, expected_date in eid_al_adha_dates.items():
            dates = {dt: est for dt, est in self.calendar.eid_al_adha_dates(year)}
            self.assertIn(expected_date, dates)
            self.assertFalse(dates[expected_date], f"Eid al-Adha {year} should be confirmed")

    def test_eid_al_adha_2006_dual_date(self):
        """2006 has two Eid al-Adha dates."""
        dates = {dt for dt, _ in self.calendar.eid_al_adha_dates(2006)}
        self.assertIn(date(2006, 12, 31), dates)
        self.assertTrue(len(dates) >= 2)

    def test_hijri_new_year_dates(self):
        dates_2025 = {dt for dt, _ in self.calendar.hijri_new_year_dates(2025)}
        self.assertIn(date(2025, 6, 27), dates_2025)

    def test_coverage_range(self):
        """Dates from 1925-2052 should be confirmed."""
        dates_1930 = list(self.calendar.eid_al_fitr_dates(1930))
        self.assertTrue(len(dates_1930) > 0)
        for _, is_estimated in dates_1930:
            self.assertFalse(is_estimated)

    def test_mawlid_dates(self):
        dates_2025 = {dt for dt, _ in self.calendar.mawlid_dates(2025)}
        self.assertIn(date(2025, 9, 5), dates_2025)


if __name__ == "__main__":
    unittest.main()
