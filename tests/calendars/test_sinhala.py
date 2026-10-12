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

from datetime import date
from unittest import TestCase

from holidays.calendars.gregorian import MAY
from holidays.calendars.sinhala import (
    _CustomSinhalaHolidays,
    _SinhalaLunar,
)


class _MockCustomSinhalaCalendar(_CustomSinhalaHolidays):
    VESAK_POYA_DATES = {
        2027: (MAY, 15),
    }


class TestSinhalaCalendar(TestCase):
    def setUp(self):
        super().setUp()
        self.calendar = _SinhalaLunar()

    def test_historical_dates_confirmed(self):
        # 2003-2026 dates are based on official government gazettes and are confirmed.
        for year in range(2003, 2027):
            for poya_func in (
                self.calendar.bak_poya_date,
                self.calendar.binara_poya_date,
                self.calendar.esala_poya_date,
                self.calendar.il_poya_date,
                self.calendar.medin_poya_date,
                self.calendar.nawam_poya_date,
                self.calendar.nikini_poya_date,
                self.calendar.poson_poya_date,
                self.calendar.unduvap_poya_date,
                self.calendar.vap_poya_date,
                self.calendar.vesak_poya_date,
            ):
                dt, is_estimated = poya_func(year)
                self.assertIsNotNone(dt, f"{poya_func.__name__} returned None for {year}")
                self.assertFalse(
                    is_estimated,
                    f"{poya_func.__name__} for {year} should be confirmed (not estimated)",
                )

            # Duruthu Poya returns an iterable of dates (2010 had no Duruthu Poya in gazette).
            if year != 2010:
                duruthu_dts = list(self.calendar.duruthu_poya_date(year))
                self.assertTrue(duruthu_dts)
                for dt, is_estimated in duruthu_dts:
                    self.assertEqual(dt.year, year)
                    self.assertFalse(is_estimated, f"Duruthu {year} should be confirmed")
            else:
                self.assertEqual(list(self.calendar.duruthu_poya_date(2010)), [])

    def test_future_dates_estimated(self):
        # Future years (2027+) are calculated astronomically and marked as estimated.
        for year in (2027, 2028, 2029, 2030):
            for poya_func in (
                self.calendar.bak_poya_date,
                self.calendar.binara_poya_date,
                self.calendar.esala_poya_date,
                self.calendar.il_poya_date,
                self.calendar.medin_poya_date,
                self.calendar.nawam_poya_date,
                self.calendar.nikini_poya_date,
                self.calendar.poson_poya_date,
                self.calendar.unduvap_poya_date,
                self.calendar.vap_poya_date,
                self.calendar.vesak_poya_date,
            ):
                dt, is_estimated = poya_func(year)
                self.assertIsNotNone(dt, f"{poya_func.__name__} returned None for {year}")
                self.assertTrue(
                    is_estimated,
                    f"{poya_func.__name__} for {year} should be estimated",
                )

            duruthu_dts = list(self.calendar.duruthu_poya_date(year))
            self.assertTrue(duruthu_dts)
            for dt, is_estimated in duruthu_dts:
                self.assertEqual(dt.year, year)
                self.assertTrue(is_estimated, f"Duruthu {year} should be estimated")

    def test_future_2027_calculated_dates(self):
        # Precise astronomical dates in Sri Lanka Standard Time (UTC+5:30) for 2027.
        expected = {
            self.calendar.nawam_poya_date: date(2027, 2, 21),
            self.calendar.medin_poya_date: date(2027, 3, 22),
            self.calendar.bak_poya_date: date(2027, 4, 21),
            self.calendar.vesak_poya_date: date(2027, 5, 20),
            self.calendar.poson_poya_date: date(2027, 6, 19),
            self.calendar.esala_poya_date: date(2027, 7, 18),
            self.calendar.nikini_poya_date: date(2027, 8, 17),
            self.calendar.binara_poya_date: date(2027, 9, 16),
            self.calendar.vap_poya_date: date(2027, 10, 15),
            self.calendar.il_poya_date: date(2027, 11, 14),
            self.calendar.unduvap_poya_date: date(2027, 12, 13),
        }
        for func, expected_dt in expected.items():
            dt, is_estimated = func(2027)
            self.assertEqual(dt, expected_dt)
            self.assertTrue(is_estimated)

        duruthu_2027 = [dt for dt, _ in self.calendar.duruthu_poya_date(2027)]
        self.assertEqual(duruthu_2027, [date(2027, 1, 22)])

    def test_future_2028_calculated_dates(self):
        # In 2028 (13 full moons): Duruthu is observed only on Jan 12 (not Dec 31).
        expected = {
            self.calendar.nawam_poya_date: date(2028, 2, 10),
            self.calendar.medin_poya_date: date(2028, 3, 11),
            self.calendar.bak_poya_date: date(2028, 4, 9),
            self.calendar.vesak_poya_date: date(2028, 5, 9),
            self.calendar.poson_poya_date: date(2028, 6, 7),
            self.calendar.esala_poya_date: date(2028, 7, 6),
            self.calendar.nikini_poya_date: date(2028, 8, 5),
            self.calendar.binara_poya_date: date(2028, 9, 4),
            self.calendar.vap_poya_date: date(2028, 10, 3),
            self.calendar.il_poya_date: date(2028, 11, 2),
            self.calendar.unduvap_poya_date: date(2028, 12, 2),
        }
        for func, expected_dt in expected.items():
            dt, is_estimated = func(2028)
            self.assertEqual(dt, expected_dt)
            self.assertTrue(is_estimated)

        duruthu_2028 = [dt for dt, _ in self.calendar.duruthu_poya_date(2028)]
        self.assertEqual(duruthu_2028, [date(2028, 1, 12)])

    def test_future_2089_calculated_dates(self):
        # In 2089: Nikini is Aug 21, Binara is Sep 20 without duplicate or misassignment.
        dt_nikini, est_nikini = self.calendar.nikini_poya_date(2089)
        self.assertEqual(dt_nikini, date(2089, 8, 21))
        self.assertTrue(est_nikini)

        dt_binara, est_binara = self.calendar.binara_poya_date(2089)
        self.assertEqual(dt_binara, date(2089, 9, 20))
        self.assertTrue(est_binara)

    def test_duruthu_leap_year_double_dates(self):
        # 2009 historical gazette: two Duruthu Poyas (Jan 10 and Dec 31).
        dts_2009 = [dt for dt, _ in self.calendar.duruthu_poya_date(2009)]
        self.assertEqual(dts_2009, [date(2009, 1, 10), date(2009, 12, 31)])

        # 2028 future: single Duruthu Poya (Jan 12).
        dts_2028 = [dt for dt, _ in self.calendar.duruthu_poya_date(2028)]
        self.assertEqual(dts_2028, [date(2028, 1, 12)])

    def test_custom_sinhala_holidays(self):
        custom_cal = _MockCustomSinhalaCalendar()
        dt, is_estimated = custom_cal.vesak_poya_date(2027)
        self.assertEqual(dt, date(2027, 5, 15))
        self.assertFalse(is_estimated)
