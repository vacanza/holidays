#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date

import holidays


class TestUkraine(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.UA(observed=False)
        self.holidays_full = holidays.UA(observed=True)

    def test_before_1918(self):
        self.assertNotIn(date(1917, 12, 31), self.holidays)

    def test_1950(self):
        self.assertEqual(
            self.holidays[date(1950, 5, 1)],
            "День міжнародної солідарності трудящих",
        )

    def test_2018(self):
        # https://www.buhoblik.org.ua/kadry-zarplata/vremya/3678-3678-normi-trivalosti-robochogo-chasu.html
        self.assertIn(date(2018, 1, 1), self.holidays)
        self.assertIn(date(2018, 1, 7), self.holidays)
        self.assertIn(date(2018, 3, 8), self.holidays)
        self.assertIn(date(2018, 4, 8), self.holidays)
        self.assertIn(date(2018, 5, 1), self.holidays)
        self.assertIn(date(2018, 5, 9), self.holidays)
        self.assertIn(date(2018, 5, 27), self.holidays)
        self.assertIn(date(2018, 6, 28), self.holidays)
        self.assertIn(date(2018, 8, 24), self.holidays)
        self.assertIn(date(2018, 10, 14), self.holidays)
        self.assertIn(date(2018, 12, 25), self.holidays)
        self.assertIn(date(2018, 1, 8), self.holidays_full)
        self.assertIn(date(2018, 4, 9), self.holidays_full)
        self.assertIn(date(2018, 5, 28), self.holidays_full)
        self.assertIn(date(2018, 10, 15), self.holidays_full)

    def test_2019(self):
        # https://www.buhoblik.org.ua/kadry-zarplata/vremya/3946-3946-normi-trivalosti-robochogo-chasu.html
        self.assertIn(date(2019, 1, 1), self.holidays)
        self.assertIn(date(2019, 1, 7), self.holidays)
        self.assertIn(date(2019, 3, 8), self.holidays)
        self.assertIn(date(2019, 4, 28), self.holidays)
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 5, 9), self.holidays)
        self.assertIn(date(2019, 6, 16), self.holidays)
        self.assertIn(date(2019, 6, 28), self.holidays)
        self.assertIn(date(2019, 8, 24), self.holidays)
        self.assertIn(date(2019, 10, 14), self.holidays)
        self.assertIn(date(2019, 12, 25), self.holidays)
        self.assertIn(date(2019, 4, 29), self.holidays_full)
        self.assertIn(date(2019, 6, 17), self.holidays_full)
        self.assertIn(date(2019, 8, 26), self.holidays_full)

    def test_2020(self):
        # https://www.buhoblik.org.ua/kadry-zarplata/vremya/4058-4058-normi-trivalosti-robochogo-chasu.html
        self.assertIn(date(2020, 1, 1), self.holidays)
        self.assertIn(date(2020, 1, 7), self.holidays)
        self.assertIn(date(2020, 3, 8), self.holidays)
        self.assertIn(date(2020, 4, 19), self.holidays)
        self.assertIn(date(2020, 5, 1), self.holidays)
        self.assertIn(date(2020, 5, 9), self.holidays)
        self.assertIn(date(2020, 6, 7), self.holidays)
        self.assertIn(date(2020, 6, 28), self.holidays)
        self.assertIn(date(2020, 8, 24), self.holidays)
        self.assertIn(date(2020, 10, 14), self.holidays)
        self.assertIn(date(2020, 12, 25), self.holidays)
        self.assertIn(date(2020, 3, 9), self.holidays_full)
        self.assertIn(date(2020, 4, 20), self.holidays_full)
        self.assertIn(date(2020, 5, 11), self.holidays_full)
        self.assertIn(date(2020, 6, 8), self.holidays_full)
        self.assertIn(date(2020, 6, 29), self.holidays_full)

    def test_2021(self):
        # https://www.buhoblik.org.ua/kadry-zarplata/vremya/4221-4221-norma-trivalosti-robochogo-chasu.html
        self.assertIn(date(2021, 1, 1), self.holidays)
        self.assertIn(date(2021, 1, 7), self.holidays)
        self.assertIn(date(2021, 3, 8), self.holidays)
        self.assertIn(date(2021, 5, 1), self.holidays)
        self.assertIn(date(2021, 5, 2), self.holidays)
        self.assertIn(date(2021, 5, 9), self.holidays)
        self.assertIn(date(2021, 6, 20), self.holidays)
        self.assertIn(date(2021, 6, 28), self.holidays)
        self.assertIn(date(2021, 8, 24), self.holidays)
        self.assertIn(date(2021, 10, 14), self.holidays)
        self.assertIn(date(2021, 12, 25), self.holidays)
        self.assertIn(date(2021, 5, 3), self.holidays_full)
        self.assertIn(date(2021, 5, 4), self.holidays_full)
        self.assertIn(date(2021, 5, 10), self.holidays_full)
        self.assertIn(date(2021, 6, 21), self.holidays_full)
        self.assertIn(date(2021, 12, 27), self.holidays_full)

    def test_2022(self):
        # https://www.buhoblik.org.ua/kadry-zarplata/vremya/4246-norma-trivalosti-robochogo-chasu-2022.html
        self.assertIn(date(2022, 1, 1), self.holidays)
        self.assertIn(date(2022, 1, 7), self.holidays)
        self.assertIn(date(2022, 3, 8), self.holidays)
        self.assertIn(date(2022, 4, 24), self.holidays)
        self.assertIn(date(2022, 5, 1), self.holidays)
        self.assertIn(date(2022, 5, 9), self.holidays)
        self.assertIn(date(2022, 6, 12), self.holidays)
        self.assertIn(date(2022, 6, 28), self.holidays)
        self.assertIn(date(2022, 7, 28), self.holidays)
        self.assertIn(date(2022, 8, 24), self.holidays)
        self.assertIn(date(2022, 10, 14), self.holidays)
        self.assertIn(date(2022, 12, 25), self.holidays)

    def test_old_holidays(self):
        self.assertIn(date(2018, 5, 1), self.holidays)
        self.assertIn(date(2016, 5, 2), self.holidays)
        self.assertIn(date(1991, 7, 16), self.holidays)
        self.assertIn(date(1950, 1, 22), self.holidays)
        self.assertIn(date(1999, 11, 7), self.holidays)
        self.assertIn(date(1999, 11, 8), self.holidays)
        self.assertIn(date(1945, 5, 9), self.holidays)
        self.assertIn(date(1945, 9, 3), self.holidays)
        self.assertIn(date(1981, 10, 7), self.holidays)
        self.assertIn(date(1937, 12, 5), self.holidays)
        self.assertIn(date(1918, 3, 18), self.holidays)

    def test_observed(self):
        for dt in [
            # New Year's Day
            date(2000, 1, 3),
            date(2005, 1, 3),
            date(2006, 1, 2),
            date(2011, 1, 3),
            date(2012, 1, 2),
            date(2017, 1, 2),
            date(2022, 1, 3),
            # Christmas Day (Julian calendar)
            date(1996, 1, 8),
            date(2001, 1, 8),
            date(2006, 1, 9),
            date(2007, 1, 8),
            date(2012, 1, 9),
            date(2017, 1, 9),
            date(2018, 1, 8),
            # Women's Day
            date(1997, 3, 10),
            date(2003, 3, 10),
            date(2008, 3, 10),
            date(2009, 3, 9),
            date(2014, 3, 10),
            date(2015, 3, 9),
            date(2020, 3, 9),
            # Easter
            date(1995, 4, 24),
            date(1996, 4, 15),
            date(1997, 4, 28),
            date(2000, 5, 3),
            date(2001, 4, 16),
            date(2002, 5, 6),
            date(2003, 4, 28),
            date(2004, 4, 12),
            date(2005, 5, 3),
            date(2006, 4, 24),
            date(2007, 4, 9),
            date(2008, 4, 28),
            date(2009, 4, 20),
            date(2010, 4, 5),
            date(2011, 4, 25),
            date(2012, 4, 16),
            date(2013, 5, 6),
            date(2014, 4, 21),
            date(2015, 4, 13),
            date(2016, 5, 3),
            date(2017, 4, 17),
            date(2018, 4, 9),
            date(2019, 4, 29),
            date(2020, 4, 20),
            date(2021, 5, 4),
            date(2022, 4, 25),
            date(2062, 5, 2),  # rare case
            # Holy trinity
            date(1995, 6, 12),
            date(1996, 6, 3),
            date(1997, 6, 16),
            date(1999, 5, 31),
            date(2000, 6, 19),
            date(2001, 6, 4),
            date(2002, 6, 24),
            date(2003, 6, 16),
            date(2004, 5, 31),
            date(2005, 6, 20),
            date(2006, 6, 12),
            date(2007, 5, 28),
            date(2008, 6, 16),
            date(2009, 6, 8),
            date(2010, 5, 24),
            date(2011, 6, 13),
            date(2012, 6, 4),
            date(2013, 6, 24),
            date(2014, 6, 9),
            date(2015, 6, 1),
            date(2016, 6, 20),
            date(2017, 6, 5),
            date(2018, 5, 28),
            date(2019, 6, 17),
            date(2020, 6, 8),
            date(2021, 6, 21),
            date(2022, 6, 13),
            # Labour Day
            date(1999, 5, 3),
            date(1999, 5, 4),
            date(2004, 5, 3),
            date(2004, 5, 4),
            date(2009, 5, 4),
            date(2010, 5, 3),
            date(2010, 5, 4),
            date(2011, 5, 3),
            date(2015, 5, 4),
            date(2021, 5, 3),
            date(2022, 5, 2),
            # Victory Day
            date(1999, 5, 10),
            date(2004, 5, 10),
            date(2009, 5, 11),
            date(2010, 5, 10),
            date(2015, 5, 11),
            date(2020, 5, 11),
            date(2021, 5, 10),
            # Constitution Day
            date(1997, 6, 30),
            date(2003, 6, 30),
            date(2008, 6, 30),
            date(2009, 6, 29),
            date(2014, 6, 30),
            date(2015, 6, 29),
            date(2020, 6, 29),
            # Independence Day
            date(1996, 8, 26),
            date(1997, 8, 25),
            date(2002, 8, 26),
            date(2003, 8, 25),
            date(2008, 8, 25),
            date(2013, 8, 26),
            date(2014, 8, 25),
            date(2019, 8, 26),
            # Day of the defender of Ukraine
            date(2017, 10, 16),
            date(2018, 10, 15),
            # October Revolution
            date(1997, 11, 10),
            date(1999, 11, 9),
            # Christmas Day (Gregorian calendar)
            date(2021, 12, 27),
            date(2022, 12, 26),
        ]:
            self.assertIn(dt, self.holidays_full)
            self.assertEqual(self.holidays_full.get(dt)[:11], "Вихідний за")

    def test_i18n_en(self):
        ua_en = holidays.Ukraine(language="en")

        self.assertEqual(ua_en["2022-01-01"], "New Year’s Day")
        self.assertEqual(ua_en["2022-01-07"], "Christmas (Julian calendar)")
        self.assertEqual(ua_en["2022-12-25"], "Christmas (Gregorian calendar)")
        self.assertEqual(ua_en["2023-01-02"], "New Year’s Day (Observed)")
