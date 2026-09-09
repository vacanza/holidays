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

from holidays.calendars.gregorian import JAN, MAR, APR, MAY, JUN, JUL, SEP, DEC
from holidays.calendars.islamic import _CustomIslamicMabimsHolidays


class _MockMabimsCalendar(_CustomIslamicMabimsHolidays):
    EID_AL_FITR_DATES_CONFIRMED_YEARS = (1998, 2077)
    EID_AL_ADHA_DATES_CONFIRMED_YEARS = (1998, 2077)
    HIJRI_NEW_YEAR_DATES_CONFIRMED_YEARS = (1998, 2077)
    MAWLID_DATES_CONFIRMED_YEARS = (1998, 2077)


class TestIslamicMabimsLunar(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.calendar = _MockMabimsCalendar()

    def _get_dates(self, holiday_func, year: int) -> dict:
        """Helper to fetch holiday dates for a specific year as {date: is_estimated}."""
        return {dt: is_estimated for dt, is_estimated in holiday_func(year) if dt.year == year}

    def test_eid_al_fitr_dates(self):
        eid_al_fitr_dates = {
            2020: date(2020, MAY, 24),
            2021: date(2021, MAY, 13),
            2022: date(2022, MAY, 2),
            2023: date(2023, APR, 22),
            2024: date(2024, APR, 10),
            2025: date(2025, MAR, 31),
            2026: date(2026, MAR, 21),
        }
        for year, expected_date in eid_al_fitr_dates.items():
            dates = self._get_dates(self.calendar.eid_al_fitr_dates, year)
            self.assertIn(expected_date, dates)
            self.assertFalse(dates[expected_date], f"Eid al-Fitr {year} should be confirmed")

    def test_eid_al_adha_dates(self):
        eid_al_adha_dates = {
            2020: date(2020, JUL, 31),
            2021: date(2021, JUL, 20),
            2022: date(2022, JUL, 10),
            2023: date(2023, JUN, 29),
            2024: date(2024, JUN, 17),
            2025: date(2025, JUN, 7),
            2026: date(2026, MAY, 27),
        }
        for year, expected_date in eid_al_adha_dates.items():
            dates = self._get_dates(self.calendar.eid_al_adha_dates, year)
            self.assertIn(expected_date, dates)
            self.assertFalse(dates[expected_date], f"Eid al-Adha {year} should be confirmed")

    def test_eid_al_adha_2006_dual_date(self):
        """2006 has two Eid al-Adha dates."""
        dates_2006 = self._get_dates(self.calendar.eid_al_adha_dates, 2006)
        self.assertIn(date(2006, JAN, 10), dates_2006)
        self.assertIn(date(2006, DEC, 31), dates_2006)
        self.assertEqual(len(dates_2006), 2)

    def test_hijri_new_year_dates(self):
        dates_2025 = self._get_dates(self.calendar.hijri_new_year_dates, 2025)
        self.assertIn(date(2025, JUN, 27), dates_2025)
        self.assertEqual(len(dates_2025), 1)

    def test_coverage_range(self):
        """Dates before 1998 should exists but marked as estimated."""
        dates_1930 = self._get_dates(self.calendar.hijri_new_year_dates, 1930)
        self.assertEqual(len(dates_1930), 1)
        for is_estimated in dates_1930.values():
            self.assertTrue(is_estimated, "Dates prior to 1998 should be estimated")

    def test_mawlid_dates(self):
        dates_2025 = self._get_dates(self.calendar.mawlid_dates, 2025)
        self.assertIn(date(2025, SEP, 5), dates_2025)
        self.assertEqual(len(dates_2025), 1)


if __name__ == "__main__":
    unittest.main()
