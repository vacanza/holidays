#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date
from datetime import timedelta as td

from dateutil.relativedelta import relativedelta as rd

import holidays


class TestUK(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.UK()
        self.holidays_england = holidays.UK(subdiv="England")
        self.holidays_wales = holidays.UK(subdiv="Wales")
        self.holidays_scotland = holidays.UK(subdiv="Scotland")
        self.holidays_northernireland = holidays.UK(subdiv="Northern Ireland")

    def test_special_holidays(self):
        for dt in (
            "1977-06-07",
            "1981-07-29",
            "1999-12-31",
            "2002-06-03",
            "2011-04-29",
            "2012-06-05",
            "2022-06-03",
            "2022-09-19",
            "2023-05-08",
        ):
            self.assertIn(dt, self.holidays)

    def test_new_years(self):
        for year in range(1974, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            if year == 2000:
                self.assertIn(dt + td(days=-1), self.holidays)
            else:
                self.assertNotIn(dt + td(days=-1), self.holidays)

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
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)

    def test_easter_monday(self):
        for dt in [
            date(1900, 4, 16),
            date(1901, 4, 8),
            date(1902, 3, 31),
            date(1999, 4, 5),
            date(2000, 4, 24),
            date(2010, 4, 5),
            date(2018, 4, 2),
            date(2019, 4, 22),
            date(2020, 4, 13),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)

    def test_royal_weddings(self):
        for dt in [date(1981, 7, 29), date(2011, 4, 29)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + rd(years=-1), self.holidays)
            self.assertNotIn(dt + rd(years=+1), self.holidays)

    def test_queens_jubilees(self):
        for dt in [
            date(1977, 6, 7),
            date(2002, 6, 3),
            date(2012, 6, 5),
            date(2022, 6, 3),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + rd(years=-1), self.holidays)
            self.assertNotIn(dt + rd(years=+1), self.holidays)

    def test_royal_funerals(self):
        for dt in [
            date(2022, 9, 19),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + rd(years=-1), self.holidays)
            self.assertNotIn(dt + rd(years=+1), self.holidays)

    def test_may_day(self):
        for dt in [
            date(1978, 5, 1),
            date(1979, 5, 7),
            date(1980, 5, 5),
            date(1999, 5, 3),
            date(2000, 5, 1),
            date(2010, 5, 3),
            date(2016, 5, 2),
            date(2018, 5, 7),
            date(2019, 5, 6),
            date(2020, 5, 8),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            self.assertNotIn(dt + td(days=+1), self.holidays)
        self.assertNotIn(date(2020, 5, 4), self.holidays)

    def test_spring_bank_holiday(self):
        for dt in [
            date(1978, 5, 29),
            date(1979, 5, 28),
            date(1980, 5, 26),
            date(1999, 5, 31),
            date(2000, 5, 29),
            date(2010, 5, 31),
            date(2018, 5, 28),
            date(2019, 5, 27),
            date(2020, 5, 25),
            date(2022, 6, 2),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
            if dt != date(2022, 6, 2):
                self.assertNotIn(dt + td(days=+1), self.holidays)

    def test_christmas_day(self):
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + td(days=-1), self.holidays)
        self.assertNotIn(date(2010, 12, 24), self.holidays)
        self.assertNotEqual(
            self.holidays[date(2011, 12, 26)],
            "Christmas Day (Observed)",
        )
        self.holidays.observed = True
        self.assertEqual(
            self.holidays[date(2011, 12, 27)],
            "Christmas Day (Observed)",
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
            self.assertNotIn(dt + td(days=+1), self.holidays)
        self.assertNotIn(date(2009, 12, 28), self.holidays)
        self.assertNotIn(date(2010, 12, 27), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2004, 12, 28), self.holidays)
        self.assertIn(date(2010, 12, 28), self.holidays)
        for year, day in enumerate(
            [
                26,
                26,
                26,
                28,
                26,
                26,
                26,
                26,
                28,
                28,
                26,
                26,
                26,
                26,
                26,
                26,
                26,
                26,
                26,
                26,
                28,
            ],
            2001,
        ):
            dt = date(year, 12, day)
            self.assertIn(dt, self.holidays, dt)
            self.assertEqual(self.holidays[dt][:6], "Boxing")

    def test_all_holidays_present(self):
        uk_2015 = holidays.UK(years=[2015])
        all_holidays = [
            "New Year's Day",
            "Good Friday",
            "Easter Monday [England/Wales/Northern Ireland]",
            "May Day",
            "Spring Bank Holiday",
            "Late Summer Bank Holiday [England/Wales/Northern Ireland]",
            "Christmas Day",
            "Boxing Day",
            "St. Patrick's Day [Northern Ireland]",
        ]
        for holiday in all_holidays:
            self.assertIn(holiday, uk_2015.values())

    def test_scotland(self):
        self.assertIn("2017-01-01", self.holidays_scotland)
        self.assertIn("2017-01-02", self.holidays_scotland)
        self.assertIn("2017-01-03", self.holidays_scotland)
        self.assertIn("2017-04-14", self.holidays_scotland)
        self.assertIn("2017-05-01", self.holidays_scotland)
        self.assertIn("2017-05-29", self.holidays_scotland)
        self.assertIn("2017-08-07", self.holidays_scotland)
        self.assertIn("2017-11-30", self.holidays_scotland)
        self.assertIn("2017-12-25", self.holidays_scotland)
        self.assertIn("2017-12-26", self.holidays_scotland)

    def test_northernireland(self):
        self.assertIn("2018-03-17", self.holidays_northernireland)
        self.assertIn("2018-07-12", self.holidays_northernireland)
