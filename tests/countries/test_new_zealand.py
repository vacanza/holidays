# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2020
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest

from datetime import date
from dateutil.relativedelta import relativedelta

import holidays


class TestNZ(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.NZ(observed=True)

    def test_new_years(self):
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
        for year, day in enumerate(
            [
                1,
                1,
                1,
                1,
                3,  # 2001-05
                3,
                1,
                1,
                1,
                1,  # 2006-10
                3,
                3,
                1,
                1,
                1,  # 2011-15
                1,
                3,
                1,
                1,
                1,
                1,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 1, day)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt][:10], "New Year's")
        self.assertNotIn("1893-01-01", self.holidays)
        self.assertIn("1894-01-01", self.holidays)

    def test_day_after_new_years(self):
        for year in range(1900, 2100):
            dt = date(year, 1, 2)
            self.assertIn(dt, self.holidays)
        for year, day in enumerate(
            [
                2,
                2,
                2,
                2,
                2,  # 2001-05
                2,
                2,
                2,
                2,
                4,  # 2006-10
                4,
                2,
                2,
                2,
                2,  # 2011-15
                4,
                2,
                2,
                2,
                2,
                4,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 1, day)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt][:10], "Day after ")
        self.assertNotIn(date(2016, 1, 3), self.holidays)

    def test_waitangi_day(self):
        ntl_holidays = holidays.NZ(prov="Northland")
        for year, day in enumerate([3, 8, 7, 6, 5], 1964):
            dt = date(year, 2, day)
            self.assertIn(dt, ntl_holidays, dt)
            self.assertEqual(ntl_holidays[dt][:8], "Waitangi")
        for year in range(1900, 1974):
            dt = date(year, 2, 6)
            self.assertNotIn(dt, self.holidays)
        for year in range(1974, 2100):
            dt = date(year, 2, 6)
            self.assertIn(dt, self.holidays)
        for year, day in enumerate(
            [
                6,
                6,
                6,
                6,
                6,  # 2001-05
                6,
                6,
                6,
                6,
                6,  # 2006-10
                6,
                6,
                6,
                6,
                6,  # 2011-15
                8,
                6,
                6,
                6,
                6,
                8,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 2, day)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt][:8], "Waitangi")
        self.assertNotIn(date(2005, 2, 7), self.holidays)
        self.assertNotIn(date(2010, 2, 8), self.holidays)
        self.assertNotIn(date(2011, 2, 7), self.holidays)

    def test_good_friday(self):
        for dt in [
            date(1900, 4, 13),
            date(1901, 4, 5),
            date(1902, 3, 28),
            date(1999, 4, 2),
            date(2000, 4, 21),
            date(2010, 4, 2),
            date(2018, 3, 30),
            date(2019, 4, 19),
            date(2020, 4, 10),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_easter_monday(self):
        for dt in [
            date(1900, 4, 16),
            date(1901, 4, 8),
            date(1902, 3, 31),
            date(1999, 4, 5),
            date(2010, 4, 5),
            date(2018, 4, 2),
            date(2019, 4, 22),
            date(2020, 4, 13),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_anzac_day(self):
        for year in range(1900, 1921):
            dt = date(year, 4, 25)
            self.assertNotIn(dt, self.holidays)
        for year in range(1921, 2100):
            dt = date(year, 4, 25)
            self.assertIn(dt, self.holidays)
        for year, day in enumerate(
            [
                25,
                25,
                25,
                25,
                25,  # 2001-05
                25,
                25,
                25,
                25,
                25,  # 2006-10
                25,
                25,
                25,
                25,
                27,  # 2011-15
                25,
                25,
                25,
                25,
                27,
                26,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 4, day)
            self.assertIn(dt, self.holidays, dt)
            self.assertEqual(self.holidays[dt][:5], "Anzac")
        self.assertNotIn(date(2009, 4, 27), self.holidays)
        self.assertNotIn(date(2010, 4, 26), self.holidays)

    def test_sovereigns_birthday(self):
        self.assertIn(date(1909, 11, 9), self.holidays)
        self.assertIn(date(1936, 6, 23), self.holidays)
        self.assertIn(date(1937, 6, 9), self.holidays)
        self.assertIn(date(1940, 6, 3), self.holidays)
        self.assertIn(date(1952, 6, 2), self.holidays)
        for year in range(1912, 1936):
            dt = date(year, 6, 3)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "King's Birthday")
        for year, day in enumerate(
            [
                4,
                3,
                2,
                7,
                6,  # 2001-05
                5,
                4,
                2,
                1,
                7,  # 2006-10
                6,
                4,
                3,
                2,
                1,  # 2011-15
                6,
                5,
                4,
                3,
                1,
                7,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 6, day)
            self.assertIn(dt, self.holidays, dt)
            self.assertEqual(self.holidays[dt], "Queen's Birthday")

    def test_labour_day(self):
        for year, day in enumerate(
            [
                22,
                28,
                27,
                25,
                24,  # 2001-05
                23,
                22,
                27,
                26,
                25,  # 2006-10
                24,
                22,
                28,
                27,
                26,  # 2011-15
                24,
                23,
                22,
                28,
                26,
                25,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 10, day)
            self.assertIn(dt, self.holidays, dt)
            self.assertEqual(self.holidays[dt], "Labour Day")

    def test_christmas_day(self):
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
        self.assertNotIn(date(2010, 12, 24), self.holidays)
        self.assertNotEqual(
            self.holidays[date(2011, 12, 26)], "Christmas Day (Observed)"
        )
        self.holidays.observed = True
        self.assertEqual(
            self.holidays[date(2011, 12, 27)], "Christmas Day (Observed)"
        )
        for year, day in enumerate(
            [
                25,
                25,
                25,
                27,
                27,  # 2001-05
                25,
                25,
                25,
                25,
                27,  # 2006-10
                27,
                25,
                25,
                25,
                25,  # 2011-15
                27,
                25,
                25,
                25,
                25,
                25,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 12, day)
            self.assertIn(dt, self.holidays, dt)
            self.assertEqual(self.holidays[dt][:9], "Christmas")

    def test_boxing_day(self):
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 12, 26)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.assertNotIn(date(2009, 12, 28), self.holidays)
        self.assertNotIn(date(2010, 12, 27), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2009, 12, 28), self.holidays)
        self.assertIn(date(2010, 12, 27), self.holidays)
        for year, day in enumerate(
            [
                26,
                26,
                26,
                28,
                26,  # 2001-05
                26,
                26,
                26,
                28,
                28,  # 2006-10
                26,
                26,
                26,
                26,
                28,  # 2011-15
                26,
                26,
                26,
                26,
                28,
                28,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 12, day)
            self.assertIn(dt, self.holidays, dt)
            self.assertEqual(self.holidays[dt][:6], "Boxing")

    def test_auckland_anniversary_day(self):
        auk_holidays = holidays.NZ(prov="Auckland")
        for year, day in enumerate(
            [
                29,
                28,
                27,
                26,
                31,  # 2001-05
                30,
                29,
                28,
                26,
                1,  # 2006-10
                31,
                30,
                28,
                27,
                26,  # 2011-15
                1,
                30,
                29,
                28,
                27,
                1,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 2 if day < 9 else 1, day)
            self.assertIn(dt, auk_holidays, dt)
            self.assertEqual(auk_holidays[dt], "Auckland Anniversary Day")

    def test_taranaki_anniversary_day(self):
        tki_holidays = holidays.NZ(prov="Taranaki")
        for year, day in enumerate(
            [
                12,
                11,
                10,
                8,
                14,  # 2001-05
                13,
                12,
                10,
                9,
                8,  # 2006-10
                14,
                12,
                11,
                10,
                9,  # 2011-15
                14,
                13,
                12,
                11,
                9,
                8,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 3, day)
            self.assertIn(dt, tki_holidays, dt)
            self.assertEqual(tki_holidays[dt], "Taranaki Anniversary Day")

    def test_hawkes_bay_anniversary_day(self):
        hkb_holidays = holidays.NZ(prov="Hawke's Bay")
        for year, day in enumerate(
            [
                19,
                25,
                24,
                22,
                21,  # 2001-05
                20,
                19,
                24,
                23,
                22,  # 2006-10
                21,
                19,
                25,
                24,
                23,  # 2011-15
                21,
                20,
                19,
                25,
                23,
                22,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 10, day)
            self.assertIn(dt, hkb_holidays, dt)
            self.assertEqual(hkb_holidays[dt], "Hawke's Bay Anniversary Day")

    def test_wellington_anniversary_day(self):
        wgn_holidays = holidays.NZ(prov="Wellington")
        for year, day in enumerate(
            [
                22,
                21,
                20,
                19,
                24,  # 2001-05
                23,
                22,
                21,
                19,
                25,  # 2006-10
                24,
                23,
                21,
                20,
                19,  # 2011-15
                25,
                23,
                22,
                21,
                20,
                25,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 1, day)
            self.assertIn(dt, wgn_holidays, dt)
            self.assertEqual(
                wgn_holidays[dt], "Wellington Anniversary Day", dt
            )

    def test_marlborough_anniversary_day(self):
        mbh_holidays = holidays.NZ(prov="Marlborough")
        for year, day in enumerate(
            [
                29,
                4,
                3,
                1,
                31,  # 2001-05
                30,
                29,
                3,
                2,
                1,  # 2006-10
                31,
                29,
                4,
                3,
                2,  # 2011-15
                31,
                30,
                29,
                4,
                2,
                1,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 11 if day < 9 else 10, day)
            self.assertIn(dt, mbh_holidays, dt)
            self.assertEqual(
                mbh_holidays[dt], "Marlborough Anniversary Day", dt
            )

    def test_nelson_anniversary_day(self):
        nsn_holidays = holidays.NZ(prov="Nelson")
        for year, day in enumerate(
            [
                29,
                4,
                3,
                2,
                31,  # 2001-05
                30,
                29,
                4,
                2,
                1,  # 2006-10
                31,
                30,
                4,
                3,
                2,  # 2011-15
                1,
                30,
                29,
                4,
                3,
                1,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 2 if day < 9 else 1, day)
            self.assertIn(dt, nsn_holidays, dt)
            self.assertEqual(nsn_holidays[dt], "Nelson Anniversary Day", dt)

    def test_canterbury_anniversary_day(self):
        can_holidays = holidays.NZ(prov="Canterbury")
        for year, day in enumerate(
            [
                16,
                15,
                14,
                12,
                11,  # 2001-05
                17,
                16,
                14,
                13,
                12,  # 2006-10
                11,
                16,
                15,
                14,
                13,  # 2011-15
                11,
                17,
                16,
                15,
                13,
                12,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 11, day)
            self.assertIn(dt, can_holidays, dt)
            self.assertEqual(
                can_holidays[dt], "Canterbury Anniversary Day", dt
            )

    def test_south_canterbury_anniversary_day(self):
        stc_holidays = holidays.NZ(prov="South Canterbury")
        for year, day in enumerate(
            [
                24,
                23,
                22,
                27,
                26,  # 2001-05
                25,
                24,
                22,
                28,
                27,  # 2006-10
                26,
                24,
                23,
                22,
                28,  # 2011-15
                26,
                25,
                24,
                23,
                28,
                27,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 9, day)
            self.assertIn(dt, stc_holidays, dt)
            self.assertEqual(
                stc_holidays[dt], "South Canterbury Anniversary Day", dt
            )

    def test_westland_anniversary_day(self):
        wtc_holidays = holidays.NZ(prov="Westland")
        for year, day in enumerate(
            [
                3,
                2,
                1,
                29,
                5,  # 2001-05
                4,
                3,
                1,
                30,
                29,  # 2006-10
                28,
                3,
                2,
                1,
                30,  # 2011-15
                28,
                4,
                3,
                2,
                30,
                29,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 12 if day < 9 else 11, day)
            self.assertIn(dt, wtc_holidays, dt)
            self.assertEqual(wtc_holidays[dt], "Westland Anniversary Day", dt)

    def test_otago_anniversary_day(self):
        ota_holidays = holidays.NZ(prov="Otago")
        for year, day in enumerate(
            [
                26,
                25,
                24,
                22,
                21,  # 2001-05
                20,
                26,
                25,
                23,
                22,  # 2006-10
                21,
                26,
                25,
                24,
                23,  # 2011-15
                21,
                20,
                26,
                25,
                23,
                22,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 3, day)
            self.assertIn(dt, ota_holidays, dt)
            self.assertEqual(ota_holidays[dt], "Otago Anniversary Day", dt)

    def test_southland_anniversary_day(self):
        stl_holidays = holidays.NZ(prov="Southland")
        for year, day in enumerate(
            [15, 14, 20, 19, 17, 16, 15, 14, 19, 18, 17],
            2001,  # 2001-05  # 2006-11
        ):
            dt = date(year, 1, day)
            self.assertIn(dt, stl_holidays, dt)
            self.assertEqual(stl_holidays[dt], "Southland Anniversary Day", dt)
            for year, (month, day) in enumerate(
                [
                    (4, 10),
                    (4, 2),
                    (4, 22),
                    (4, 7),
                    (3, 29),
                    (4, 18),
                    (4, 3),
                    (4, 23),
                    (4, 14),
                    (4, 6),
                ],
                2012,
            ):
                dt = date(year, month, day)
                self.assertIn(dt, stl_holidays, dt)
                self.assertEqual(
                    stl_holidays[dt], "Southland Anniversary Day", dt
                )

    def test_chatham_islands_anniversary_day(self):
        cit_holidays = holidays.NZ(prov="Chatham Islands")
        for year, day in enumerate(
            [
                3,
                2,
                1,
                29,
                28,  # 2001-05
                27,
                3,
                1,
                30,
                29,  # 2006-10
                28,
                3,
                2,
                1,
                30,  # 2011-15
                28,
                27,
                3,
                2,
                30,
                29,
            ],  # 2016-21
            2001,
        ):
            dt = date(year, 12 if day < 9 else 11, day)
            self.assertIn(dt, cit_holidays, dt)
            self.assertEqual(
                cit_holidays[dt], "Chatham Islands Anniversary Day", dt
            )

    def test_all_holidays_present(self):
        nz_1969 = sum(
            holidays.NZ(years=[1969], prov=p) for p in holidays.NZ.PROVINCES
        )
        holidays_in_1969 = sum((nz_1969.get_list(key) for key in nz_1969), [])
        nz_2015 = sum(
            holidays.NZ(years=[2015], prov=p) for p in holidays.NZ.PROVINCES
        )
        holidays_in_2015 = sum((nz_2015.get_list(key) for key in nz_2015), [])
        nz_1974 = sum(
            holidays.NZ(years=[1974], prov=p) for p in holidays.NZ.PROVINCES
        )
        holidays_in_1974 = sum((nz_1974.get_list(key) for key in nz_1974), [])
        all_holidays = [
            "New Year's Day",
            "Day after New Year's Day",
            "Waitangi Day",
            "Good Friday",
            "Easter Monday",
            "Anzac Day",
            "Queen's Birthday",
            "Labour Day",
            "Christmas Day",
            "Boxing Day",
            "Auckland Anniversary Day",
            "Taranaki Anniversary Day",
            "Hawke's Bay Anniversary Day",
            "Wellington Anniversary Day",
            "Marlborough Anniversary Day",
            "Nelson Anniversary Day",
            "Canterbury Anniversary Day",
            "South Canterbury Anniversary Day",
            "Westland Anniversary Day",
            "Otago Anniversary Day",
            "Southland Anniversary Day",
            "Chatham Islands Anniversary Day",
            "Queen's Birthday",
            "Labour Day",
            "Christmas Day",
            "Boxing Day",
        ]
        for holiday in all_holidays:
            self.assertIn(holiday, holidays_in_1969, holiday)
            self.assertIn(holiday, holidays_in_2015, holiday)
        all_holidays.remove("Waitangi Day")
        all_holidays.insert(2, "New Zealand Day")
        for holiday in all_holidays:
            self.assertIn(holiday, holidays_in_1974, holiday)
        self.assertNotIn("Waitangi Day", holidays_in_1974)
