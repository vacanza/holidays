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

from collections import namedtuple
from datetime import date
from unittest import TestCase
from unittest.mock import patch

from holidays.calendars.gregorian import MAY
from holidays.calendars.sinhala import (
    POYA_NAMES,
    _CustomSinhalaHolidays,
    _SinhalaLunar,
    _calculate_poya_dates,
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
        # Unconfirmed future years/poyas are calculated astronomically and marked as estimated.
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
                confirmed_2027 = poya_func in {
                    self.calendar.nawam_poya_date,
                    self.calendar.vesak_poya_date,
                }
                if (year == 2027 and confirmed_2027) or (
                    year == 2030 and poya_func == self.calendar.vesak_poya_date
                ):
                    self.assertFalse(
                        is_estimated,
                        f"{poya_func.__name__} for {year} should be confirmed",
                    )
                else:
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
        # Precise dates in Sri Lanka Standard Time (UTC+5:30) for 2027.
        expected = {
            self.calendar.nawam_poya_date: (date(2027, 2, 21), False),
            self.calendar.medin_poya_date: (date(2027, 3, 22), True),
            self.calendar.bak_poya_date: (date(2027, 4, 21), True),
            self.calendar.vesak_poya_date: (date(2027, 5, 20), False),
            self.calendar.poson_poya_date: (date(2027, 6, 19), True),
            self.calendar.esala_poya_date: (date(2027, 7, 18), True),
            self.calendar.nikini_poya_date: (date(2027, 8, 17), True),
            self.calendar.binara_poya_date: (date(2027, 9, 16), True),
            self.calendar.vap_poya_date: (date(2027, 10, 15), True),
            self.calendar.il_poya_date: (date(2027, 11, 14), True),
            self.calendar.unduvap_poya_date: (date(2027, 12, 13), True),
        }
        for func, (expected_dt, expected_est) in expected.items():
            dt, is_estimated = func(2027)
            self.assertEqual(dt, expected_dt)
            self.assertEqual(is_estimated, expected_est)

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
        dts = list(custom_cal.vesak_poya_dates(2027))
        self.assertEqual(dts, [(date(2027, 5, 15), False)])

    def test_vesak_poya_2030(self):
        dt, is_estimated = self.calendar.vesak_poya_date(2030)
        self.assertEqual(dt, date(2030, 5, 24))
        self.assertFalse(is_estimated)

    def test_poya_dates_generator(self):
        # 2027 has 12 poyas in chronological order
        poyas_2027 = list(self.calendar.poya_dates(2027))
        self.assertEqual(len(poyas_2027), 12)
        dates = [dt for _, dt, _ in poyas_2027]
        self.assertEqual(dates, sorted(dates))

        # Check confirmed flags in generator output
        poyas_dict = {name: (dt, est) for name, dt, est in poyas_2027}
        self.assertEqual(poyas_dict["NAWAM_POYA"], (date(2027, 2, 21), False))
        self.assertEqual(poyas_dict["VESAK_POYA"], (date(2027, 5, 20), False))
        self.assertEqual(poyas_dict["MEDIN_POYA"], (date(2027, 3, 22), True))

        # 2009 has 13 poyas (two Duruthu Poyas: Jan 10 and Dec 31)
        poyas_2009 = list(self.calendar.poya_dates(2009))
        self.assertEqual(len(poyas_2009), 13)
        self.assertEqual(poyas_2009[0], ("DURUTHU_POYA", date(2009, 1, 10), False))
        self.assertEqual(poyas_2009[-1], ("DURUTHU_POYA", date(2009, 12, 31), False))

    def test_poya_days_set(self):
        days_2027 = self.calendar.poya_days(2027)
        self.assertIsInstance(days_2027, set)
        self.assertEqual(len(days_2027), 12)
        self.assertIn(date(2027, 2, 21), days_2027)
        self.assertIn(date(2027, 5, 20), days_2027)

        days_2009 = self.calendar.poya_days(2009)
        self.assertEqual(len(days_2009), 13)
        self.assertIn(date(2009, 1, 10), days_2009)
        self.assertIn(date(2009, 12, 31), days_2009)

    def test_generate_poya_dates_range(self):
        range_poyas = list(self.calendar.generate_poya_dates(2027, 2028))
        # 12 poyas in 2027 + 12 poyas in 2028 = 24 poyas
        self.assertEqual(len(range_poyas), 24)
        for _, dt, _ in range_poyas[:12]:
            self.assertEqual(dt.year, 2027)
        for _, dt, _ in range_poyas[12:]:
            self.assertEqual(dt.year, 2028)

    def test_sinhala_lunar_iterator(self):
        cal_year = _SinhalaLunar(year=2027)
        self.assertEqual(list(cal_year), list(self.calendar.poya_dates(2027)))

        cal_range = _SinhalaLunar(year_range=(2027, 2028))
        self.assertEqual(list(cal_range), list(self.calendar.generate_poya_dates(2027, 2028)))

        # Default initialization iterates over START_YEAR to END_YEAR
        cal_default = _SinhalaLunar()
        first_poya = next(iter(cal_default))
        self.assertEqual(first_poya[1].year, _SinhalaLunar.START_YEAR)

    def test_individual_poya_dates_generators(self):
        for poya in POYA_NAMES:
            func = getattr(self.calendar, f"{poya.lower()}_dates")
            res = list(func(2027))
            self.assertTrue(len(res) >= 1)

        self.assertEqual(
            list(self.calendar.vesak_poya_dates(2027)),
            [(date(2027, 5, 20), False)],
        )
        self.assertEqual(
            list(self.calendar.vesak_poya_dates(2030)),
            [(date(2030, 5, 24), False)],
        )
        self.assertEqual(
            list(self.calendar.duruthu_poya_dates(2009)),
            [(date(2009, 1, 10), False), (date(2009, 12, 31), False)],
        )
        self.assertEqual(
            list(self.calendar.duruthu_poya_dates(2010)),
            [],
        )
        self.assertEqual(
            list(self.calendar.bak_poya_dates(2027)),
            [(date(2027, 4, 21), True)],
        )

    def test_unsupported_pre_2003_year(self):
        dt, is_estimated = self.calendar.bak_poya_date(2000)
        self.assertIsNone(dt)
        self.assertFalse(is_estimated)
        self.assertEqual(list(self.calendar.bak_poya_dates(2000)), [])

    def test_unknown_poya_name(self):
        self.assertEqual(list(self.calendar._get_holiday_set("UNKNOWN_POYA", 2030)), [])

    def test_future_year_without_february_full_moon(self):
        # 2037 has 13 full moons and no full moon in February.
        # Duruthu Poya is Jan 2 and Nawam Poya is Jan 31; March has two full moons.
        poyas_2037 = _calculate_poya_dates(2037)
        self.assertEqual(len(poyas_2037), 12)
        self.assertEqual(poyas_2037["DURUTHU_POYA"], date(2037, 1, 2))
        self.assertEqual(poyas_2037["NAWAM_POYA"], date(2037, 1, 31))

    def test_calculate_poya_dates_fallback(self):
        MockDate = namedtuple("MockDate", ["year", "month", "day"])
        mock_dates = tuple(MockDate(2099, i, 1) for i in range(1, 14))
        with patch("holidays.calendars.sinhala._get_slst_full_moons", return_value=mock_dates):
            poyas = _calculate_poya_dates.__wrapped__(2099)
            self.assertEqual(len(poyas), 12)
            self.assertEqual(poyas["UNDUVAP_POYA"], MockDate(2099, 12, 1))


class TestSinhalaCalendarGenerator(TestCase):
    def setUp(self):
        super().setUp()
        from scripts.calendar.sinhala_generator import SinhalaCalendarGenerator

        self.generator = SinhalaCalendarGenerator()

    def test_inheritance(self):
        from scripts.calendar.generator import CalendarGenerator

        self.assertIsInstance(self.generator, CalendarGenerator)
        self.assertEqual(self.generator.class_name, "_SinhalaLunar")

    def test_full_moon_jde(self):
        # Full Moon around January 2000 (k = 0.5)
        jde = self.generator.full_moon_jde(0.5)
        self.assertGreater(jde, 2451550.0)

    def test_slst_full_moons_2027(self):
        fms = self.generator.get_slst_full_moons(2027)
        self.assertEqual(len(fms), 12)
        self.assertEqual(fms[0], date(2027, 1, 22))

    def test_calculate_poya_dates_2027(self):
        poyas = self.generator.calculate_poya_dates(2027)
        self.assertEqual(len(poyas), 12)
        self.assertEqual(poyas["VESAK_POYA"], date(2027, 5, 20))
        self.assertEqual(poyas["NAWAM_POYA"], date(2027, 2, 21))

    def test_calculate_poya_dates_2037(self):
        # 13 full moons without February full moon
        poyas = self.generator.calculate_poya_dates(2037)
        self.assertEqual(len(poyas), 12)
        self.assertEqual(poyas["DURUTHU_POYA"], date(2037, 1, 2))
        self.assertEqual(poyas["NAWAM_POYA"], date(2037, 1, 31))

    def test_calculate_poya_dates_fallback(self):
        MockDate = namedtuple("MockDate", ["year", "month", "day"])
        mock_dates = tuple(MockDate(2099, i, 1) for i in range(1, 14))
        with patch.object(self.generator, "get_slst_full_moons", return_value=mock_dates):
            poyas = self.generator.calculate_poya_dates.__wrapped__(self.generator, 2099)
            self.assertEqual(len(poyas), 12)
            self.assertEqual(poyas["UNDUVAP_POYA"], MockDate(2099, 12, 1))

    def test_poya_date_and_dates(self):
        # Confirmed date
        dt, is_est = self.generator.vesak_poya_date(2027)
        self.assertEqual(dt, date(2027, 5, 20))
        self.assertFalse(is_est)
        self.assertEqual(
            self.generator.vesak_poya_dates(2027),
            [(date(2027, 5, 20), False)],
        )

        # Duruthu 2009 double date
        duruthu_dts = self.generator.duruthu_poya_dates(2009)
        self.assertEqual(
            duruthu_dts,
            [(date(2009, 1, 10), False), (date(2009, 12, 31), False)],
        )
        self.assertEqual(self.generator.duruthu_poya_date(2009), duruthu_dts)

        # Calculated estimated date
        dt, is_est = self.generator.bak_poya_date(2027)
        self.assertEqual(dt, date(2027, 4, 21))
        self.assertTrue(is_est)
        self.assertEqual(
            self.generator.bak_poya_dates(2027),
            [(date(2027, 4, 21), True)],
        )

        # Unsupported year (< 2003 or > 2100)
        self.assertEqual(self.generator.bak_poya_date(2000), (None, False))
        self.assertEqual(self.generator.bak_poya_dates(2000), [])

        # All individual helpers
        for poya in (
            "binara",
            "esala",
            "il",
            "medin",
            "nawam",
            "nikini",
            "poson",
            "unduvap",
            "vap",
        ):
            single_func = getattr(self.generator, f"{poya}_poya_date")
            list_func = getattr(self.generator, f"{poya}_poya_dates")
            res_dt, _ = single_func(2027)
            self.assertIsNotNone(res_dt)
            self.assertTrue(len(list_func(2027)) >= 1)

    def test_get_dates(self):
        dates_confirmed = self.generator.get_dates(2003, 2026, confirmed_only=True)
        self.assertEqual(len(dates_confirmed), 12)
        self.assertIn(2003, dates_confirmed["BAK_POYA"])
        self.assertIn(2026, dates_confirmed["BAK_POYA"])
        self.assertNotIn(2027, dates_confirmed["BAK_POYA"])

        dates_all = self.generator.get_dates(2027, 2028, confirmed_only=False)
        self.assertIn(2027, dates_all["BAK_POYA"])
        self.assertIn(2028, dates_all["BAK_POYA"])

    def test_generate_calendar_and_generate_data(self):
        with patch.object(self.generator, "generate") as mock_generate:
            self.generator.generate_calendar(2003, 2004)
            mock_generate.assert_called_once()

        from scripts.calendar.sinhala_generator import generate_data

        with patch(
            "scripts.calendar.sinhala_generator.SinhalaCalendarGenerator.generate_calendar"
        ) as mock_gen_cal:
            generate_data()
            mock_gen_cal.assert_called_once()
