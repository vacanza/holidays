# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest

from datetime import date
from dateutil.relativedelta import relativedelta

import holidays


class TestUS(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.US(observed=False)

    def test_new_years(self):
        self.assertNotIn(date(2010, 12, 31), self.holidays)
        self.assertNotIn(date(2017, 1, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2010, 12, 31), self.holidays)
        self.assertIn(date(2017, 1, 2), self.holidays)
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_epiphany(self):
        pr_holidays = holidays.US(state="PR")
        for year in range(2010, 2021):
            self.assertNotIn(date(year, 1, 6), self.holidays)
            self.assertIn(date(year, 1, 6), pr_holidays)

    def test_three_kings_day(self):
        vi_holidays = holidays.US(state="VI")
        for year in range(2010, 2021):
            self.assertNotIn(date(year, 1, 6), self.holidays)
            self.assertIn(date(year, 1, 6), vi_holidays)

    def test_lee_jackson_day(self):
        va_holidays = holidays.US(state="VA")
        self.assertNotIn(date(1888, 1, 19), va_holidays)
        self.assertNotIn(date(1983, 1, 19), va_holidays)
        self.assertNotIn(
            "Lee Jackson Day", va_holidays.get_list(date(2000, 1, 17))
        )
        for dt in [
            date(1889, 1, 19),
            date(1982, 1, 19),
            date(1983, 1, 17),
            date(1999, 1, 18),
            date(2000, 1, 14),
            date(2001, 1, 12),
            date(2013, 1, 18),
            date(2014, 1, 17),
            date(2018, 1, 12),
        ]:
            self.assertNotIn("Lee Jackson Day", self.holidays.get_list(dt))
            self.assertIn(dt, va_holidays)
            self.assertIn("Lee Jackson Day", va_holidays.get_list(dt))

    def test_inauguration_day(self):
        name = "Inauguration Day"
        dc_holidays = holidays.US(state="DC")
        la_holidays = holidays.US(state="LA")
        md_holidays = holidays.US(state="MD")
        va_holidays = holidays.US(state="VA")
        for year in (1789, 1793, 1877, 1929, 1933):
            self.assertNotIn(name, self.holidays.get_list(date(year, 3, 4)))
            self.assertIn(name, dc_holidays.get_list(date(year, 3, 4)))
            self.assertIn(name, la_holidays.get_list(date(year, 3, 4)))
            self.assertIn(name, md_holidays.get_list(date(year, 3, 4)))
            self.assertIn(name, va_holidays.get_list(date(year, 3, 4)))
        for year in (1937, 1941, 1957, 2013, 2017):
            self.assertNotIn(name, self.holidays.get_list(date(year, 1, 20)))
            self.assertIn(name, dc_holidays.get_list(date(year, 1, 20)))
            self.assertIn(name, la_holidays.get_list(date(year, 1, 20)))
            self.assertIn(name, md_holidays.get_list(date(year, 1, 20)))
            self.assertIn(name, va_holidays.get_list(date(year, 1, 20)))
        for year in (1785, 1788, 2010, 2011, 2012, 2014, 2015, 2016):
            self.assertNotIn(name, dc_holidays.get_list(date(year, 3, 4)))
            self.assertNotIn(name, la_holidays.get_list(date(year, 3, 4)))
            self.assertNotIn(name, md_holidays.get_list(date(year, 3, 4)))
            self.assertNotIn(name, va_holidays.get_list(date(year, 3, 4)))
            self.assertNotIn(name, dc_holidays.get_list(date(year, 1, 20)))
            self.assertNotIn(name, la_holidays.get_list(date(year, 1, 20)))
            self.assertNotIn(name, md_holidays.get_list(date(year, 1, 20)))
            self.assertNotIn(name, va_holidays.get_list(date(year, 1, 20)))

    def test_martin_luther(self):
        for dt in [
            date(1986, 1, 20),
            date(1999, 1, 18),
            date(2000, 1, 17),
            date(2012, 1, 16),
            date(2013, 1, 21),
            date(2014, 1, 20),
            date(2015, 1, 19),
            date(2016, 1, 18),
            date(2020, 1, 20),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.assertNotIn(
            "Martin Luther King Jr. Day", holidays.US(years=[1985]).values()
        )
        self.assertIn(
            "Martin Luther King Jr. Day", holidays.US(years=[1986]).values()
        )
        self.assertEqual(
            holidays.US(state="AL").get("2015-01-19"),
            "Robert E. Lee/Martin Luther King Birthday",
        )
        self.assertEqual(
            holidays.US(state="AR").get("2015-01-19"),
            ("Dr. Martin Luther King Jr. " "and Robert E. Lee's Birthdays"),
        )
        self.assertEqual(
            holidays.US(state="MS").get("2015-01-19"),
            ("Dr. Martin Luther King Jr. " "and Robert E. Lee's Birthdays"),
        )
        self.assertEqual(
            holidays.US(state="AZ").get("2015-01-19"),
            "Dr. Martin Luther King Jr./Civil Rights Day",
        )
        self.assertEqual(
            holidays.US(state="NH").get("2015-01-19"),
            "Dr. Martin Luther King Jr./Civil Rights Day",
        )
        self.assertEqual(
            holidays.US(state="ID").get("2015-01-19"),
            "Martin Luther King Jr. - Idaho Human Rights Day",
        )
        self.assertNotEqual(
            holidays.US(state="ID").get("2000-01-17"),
            "Martin Luther King Jr. - Idaho Human Rights Day",
        )
        self.assertEqual(
            holidays.US(state="GA").get("2011-01-17"),
            "Robert E. Lee's Birthday",
        )

    def test_lincolns_birthday(self):
        ca_holidays = holidays.US(state="CA")
        ct_holidays = holidays.US(state="CT")
        il_holidays = holidays.US(state="IL")
        ia_holidays = holidays.US(state="IA")
        nj_holidays = holidays.US(state="NJ")
        ny_holidays = holidays.US(state="NY")
        for year in range(1971, 2010):
            self.assertNotIn(date(year, 2, 12), self.holidays)
            self.assertIn(date(year, 2, 12), ca_holidays)
            self.assertIn(date(year, 2, 12), ct_holidays)
            self.assertIn(date(year, 2, 12), il_holidays)
            self.assertIn(date(year, 2, 12), ia_holidays)
            self.assertIn(date(year, 2, 12), nj_holidays)
            self.assertIn(date(year, 2, 12), ny_holidays)
            if date(year, 2, 12).weekday() == 5:
                self.assertNotIn(date(year, 2, 11), self.holidays)
                self.assertIn(date(year, 2, 11), ca_holidays)
                self.assertIn(date(year, 2, 11), ct_holidays)
                self.assertIn(date(year, 2, 11), il_holidays)
                self.assertIn(date(year, 2, 11), ia_holidays)
                self.assertIn(date(year, 2, 11), nj_holidays)
                self.assertIn(date(year, 2, 11), ny_holidays)
            else:
                self.assertNotIn(date(year, 2, 11), ca_holidays)
                self.assertNotIn(date(year, 2, 11), ct_holidays)
                self.assertNotIn(date(year, 2, 11), il_holidays)
                self.assertNotIn(date(year, 2, 11), ia_holidays)
                self.assertNotIn(date(year, 2, 11), nj_holidays)
                self.assertNotIn(date(year, 2, 11), ny_holidays)
            if date(year, 2, 12).weekday() == 6:
                self.assertNotIn(date(year, 2, 13), self.holidays)
                self.assertIn(date(year, 2, 13), ca_holidays)
                self.assertIn(date(year, 2, 13), ct_holidays)
                self.assertIn(date(year, 2, 13), il_holidays)
                self.assertIn(date(year, 2, 13), ia_holidays)
                self.assertIn(date(year, 2, 13), nj_holidays)
                self.assertIn(date(year, 2, 13), ny_holidays)
            else:
                self.assertNotIn(date(year, 2, 13), ca_holidays)
                self.assertNotIn(date(year, 2, 13), ct_holidays)
                self.assertNotIn(date(year, 2, 13), il_holidays)
                self.assertNotIn(date(year, 2, 13), ia_holidays)
                self.assertNotIn(date(year, 2, 13), nj_holidays)
                self.assertNotIn(date(year, 2, 13), ny_holidays)
        for year in range(2010, 2050):
            self.assertNotIn(date(year, 2, 12), self.holidays)
            self.assertNotIn(date(year, 2, 12), ca_holidays)
            self.assertIn(date(year, 2, 12), ct_holidays)
            self.assertIn(date(year, 2, 12), il_holidays)
            self.assertIn(date(year, 2, 12), ia_holidays)
            self.assertIn(date(year, 2, 12), nj_holidays)
            self.assertIn(date(year, 2, 12), ny_holidays)
            if date(year, 2, 12).weekday() == 5:
                self.assertNotIn(date(year, 2, 11), self.holidays)
                self.assertNotIn(date(year, 2, 11), ca_holidays)
                self.assertIn(date(year, 2, 11), ct_holidays)
                self.assertIn(date(year, 2, 11), il_holidays)
                self.assertIn(date(year, 2, 11), ia_holidays)
                self.assertIn(date(year, 2, 11), nj_holidays)
                self.assertIn(date(year, 2, 11), ny_holidays)
            else:
                self.assertNotIn(date(year, 2, 11), ca_holidays)
                self.assertNotIn(date(year, 2, 11), ct_holidays)
                self.assertNotIn(date(year, 2, 11), il_holidays)
                self.assertNotIn(date(year, 2, 11), ia_holidays)
                self.assertNotIn(date(year, 2, 11), nj_holidays)
                self.assertNotIn(date(year, 2, 11), ny_holidays)
            if date(year, 2, 12).weekday() == 6:
                self.assertNotIn(date(year, 2, 13), self.holidays)
                self.assertNotIn(date(year, 2, 13), ca_holidays)
                self.assertIn(date(year, 2, 13), ct_holidays)
                self.assertIn(date(year, 2, 13), il_holidays)
                self.assertIn(date(year, 2, 13), ia_holidays)
                self.assertIn(date(year, 2, 13), nj_holidays)
                self.assertIn(date(year, 2, 13), ny_holidays)
            else:
                self.assertNotIn(date(year, 2, 13), ca_holidays)
                self.assertNotIn(date(year, 2, 13), ct_holidays)
                self.assertNotIn(date(year, 2, 13), il_holidays)
                self.assertNotIn(date(year, 2, 13), ia_holidays)
                self.assertNotIn(date(year, 2, 13), nj_holidays)
                self.assertNotIn(date(year, 2, 13), ny_holidays)

    def test_susan_b_anthony_day(self):
        ca_holidays = holidays.US(state="CA")
        fl_holidays = holidays.US(state="FL")
        ny_holidays = holidays.US(state="NY")
        wi_holidays = holidays.US(state="WI")
        self.assertNotIn(date(1975, 2, 15), wi_holidays)
        self.assertNotIn(date(2000, 2, 15), ca_holidays)
        self.assertNotIn(date(2000, 2, 15), fl_holidays)
        self.assertNotIn(date(2000, 2, 15), ny_holidays)
        self.assertIn(date(2000, 2, 15), wi_holidays)
        self.assertIn(date(2004, 2, 15), ny_holidays)
        self.assertNotIn(date(2010, 2, 15), fl_holidays)
        self.assertIn(date(2010, 2, 15), ny_holidays)
        self.assertNotIn(date(2013, 2, 15), self.holidays)
        self.assertNotIn(date(2013, 2, 15), ca_holidays)
        self.assertIn(date(2013, 2, 15), fl_holidays)
        self.assertIn(date(2013, 2, 15), ny_holidays)
        self.assertNotIn(date(2014, 2, 15), self.holidays)
        self.assertIn(date(2014, 2, 15), ca_holidays)
        self.assertIn(date(2014, 2, 15), fl_holidays)
        self.assertIn(date(2014, 2, 15), ny_holidays)
        self.assertIn(date(2014, 2, 15), wi_holidays)

    def test_washingtons_birthday(self):
        de_holidays = holidays.US(state="DE")
        fl_holidays = holidays.US(state="FL")
        ga_holidays = holidays.US(state="GA")
        nm_holidays = holidays.US(state="NM")
        for dt in [
            date(1969, 2, 22),
            date(1970, 2, 22),
            date(1971, 2, 15),
            date(1997, 2, 17),
            date(1999, 2, 15),
            date(2000, 2, 21),
            date(2012, 2, 20),
            date(2013, 2, 18),
            date(2014, 2, 17),
            date(2015, 2, 16),
            date(2016, 2, 15),
            date(2020, 2, 17),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt, de_holidays)
            self.assertNotEqual(fl_holidays.get(dt), "Washington's Birthday")
            self.assertNotIn(dt, ga_holidays)
            self.assertNotIn(dt, nm_holidays)
        for dt in [date(2013, 12, 24), date(2014, 12, 26), date(2015, 12, 24)]:
            self.assertIn(dt, ga_holidays)
            self.assertIn("Washington's Birthday", ga_holidays.get_list(dt))
        self.assertEqual(
            holidays.US(state="AL").get("2015-02-16"),
            "George Washington/Thomas Jefferson Birthday",
        )
        self.assertEqual(
            holidays.US(state="AR").get("2015-02-16"),
            ("George Washington's Birthday " "and Daisy Gatson Bates Day"),
        )
        self.assertEqual(
            holidays.US(state="PR").get("2015-02-16"), "Presidents' Day"
        )
        self.assertEqual(
            holidays.US(state="VI").get("2015-02-16"), "Presidents' Day"
        )

    def test_mardi_gras(self):
        la_holidays = holidays.US(state="LA")
        self.assertNotIn(date(1856, 2, 5), la_holidays)
        for dt in [
            date(1857, 2, 24),
            date(2008, 2, 5),
            date(2011, 3, 8),
            date(2012, 2, 21),
            date(2014, 3, 4),
            date(2018, 2, 13),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, la_holidays)

    def test_guam_discovery_day(self):
        gu_holidays = holidays.US(state="GU")
        self.assertNotIn(date(1969, 3, 1), gu_holidays)
        for dt in [
            date(1970, 3, 2),
            date(1971, 3, 1),
            date(1977, 3, 7),
            date(2014, 3, 3),
            date(2015, 3, 2),
            date(2016, 3, 7),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, gu_holidays)
            self.assertEqual(gu_holidays.get(dt), "Guam Discovery Day")

    def test_casimir_pulaski_day(self):
        il_holidays = holidays.US(state="IL")
        self.assertNotIn(date(1977, 3, 7), il_holidays)
        for dt in [
            date(1978, 3, 6),
            date(1982, 3, 1),
            date(1983, 3, 7),
            date(2014, 3, 3),
            date(2015, 3, 2),
            date(2016, 3, 7),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, il_holidays)
            self.assertEqual(il_holidays.get(dt), "Casimir Pulaski Day")

    def test_texas_independence_day(self):
        tx_holidays = holidays.US(state="TX")
        self.assertNotIn(date(1873, 3, 2), tx_holidays)
        for year in range(1874, 2050):
            self.assertNotIn(date(year, 3, 2), self.holidays)
            self.assertIn(date(year, 3, 2), tx_holidays)

    def test_town_meeting_day(self):
        vt_holidays = holidays.US(state="VT")
        self.assertNotIn(date(1799, 3, 5), vt_holidays)
        for dt in [
            date(1800, 3, 4),
            date(1803, 3, 1),
            date(1804, 3, 6),
            date(2011, 3, 1),
            date(2015, 3, 3),
            date(2017, 3, 7),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, vt_holidays)

    def test_evacuation_day(self):
        ma_holidays = holidays.US(state="MA")
        self.assertNotIn(date(1900, 3, 17), ma_holidays)
        for year in range(1901, 2050):
            self.assertNotIn(date(year, 3, 17), self.holidays)
            self.assertIn(date(year, 3, 17), ma_holidays)
        self.assertNotIn(date(1995, 3, 20), ma_holidays)
        for dt in [date(2012, 3, 19), date(2013, 3, 18), date(2018, 3, 19)]:
            self.assertIn(dt, ma_holidays)
        ma_holidays.observed = False
        for dt in [date(2012, 3, 19), date(2013, 3, 18), date(2018, 3, 19)]:
            self.assertNotIn(dt, ma_holidays)

    def test_emancipation_day_in_puerto_rico(self):
        pr_holidays = holidays.US(state="PR")
        for year in range(2010, 2021):
            self.assertNotIn(date(year, 3, 22), self.holidays)
            self.assertIn(date(year, 3, 22), pr_holidays)
        self.assertNotIn(date(2014, 3, 21), pr_holidays)
        self.assertNotIn(date(2014, 3, 23), pr_holidays)
        self.assertIn(date(2015, 3, 23), pr_holidays)

    def test_prince_jonah_kuhio_kalanianaole_day(self):
        hi_holidays = holidays.US(state="HI")
        self.assertNotIn(date(1948, 3, 26), hi_holidays)
        for year in range(1949, 2050):
            self.assertNotIn(date(year, 3, 26), self.holidays)
            self.assertIn(date(year, 3, 26), hi_holidays)
        for dt in [date(1949, 3, 25), date(2016, 3, 25), date(2017, 3, 27)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, hi_holidays)
            self.assertEqual(
                hi_holidays.get(dt),
                "Prince Jonah Kuhio Kalanianaole Day (Observed)",
            )
        hi_holidays.observed = False
        for dt in [date(1949, 3, 25), date(2016, 3, 25), date(2017, 3, 27)]:
            self.assertNotIn(dt, hi_holidays)

    def test_stewards_day(self):
        ak_holidays = holidays.US(state="AK")
        self.assertNotIn(date(1917, 3, 30), ak_holidays)
        for dt in [
            date(1918, 3, 30),
            date(1954, 3, 30),
            date(1955, 3, 28),
            date(2002, 3, 25),
            date(2014, 3, 31),
            date(2018, 3, 26),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, ak_holidays)

    def test_cesar_chavez_day(self):
        ca_holidays = holidays.US(state="CA")
        tx_holidays = holidays.US(state="TX")
        for year in range(1995, 2000):
            self.assertNotIn(date(year, 3, 31), self.holidays)
            self.assertIn(date(year, 3, 31), ca_holidays)
        for year in range(2000, 2020):
            self.assertNotIn(date(year, 3, 31), self.holidays)
            self.assertIn(date(year, 3, 31), ca_holidays)
            self.assertIn(date(year, 3, 31), tx_holidays)
        for year in (1996, 2002, 2013, 2019):
            self.assertNotIn(date(year, 4, 1), self.holidays)
            self.assertIn(date(year, 4, 1), ca_holidays)
            self.assertNotIn(date(year, 4, 1), tx_holidays)

    def test_transfer_day(self):
        vi_holidays = holidays.US(state="VI")
        for year in range(2010, 2021):
            self.assertNotIn(date(year, 3, 31), self.holidays)
            self.assertIn(date(year, 3, 31), vi_holidays)

    def test_emancipation_day(self):
        dc_holidays = holidays.US(state="DC")
        self.assertNotIn(date(2004, 4, 16), dc_holidays)
        for year in range(2005, 2020):
            self.assertNotIn(date(year, 4, 16), self.holidays)
            self.assertIn(date(year, 4, 16), dc_holidays)
        self.assertIn(date(2005, 4, 15), dc_holidays)
        self.assertIn(date(2006, 4, 17), dc_holidays)
        dc_holidays.observed = False
        self.assertNotIn(date(2005, 4, 15), dc_holidays)
        self.assertNotIn(date(2006, 4, 17), dc_holidays)

    def test_patriots_day(self):
        me_holidays = holidays.US(state="ME")
        ma_holidays = holidays.US(state="MA")
        self.assertNotIn(date(1983, 4, 19), me_holidays)
        self.assertNotIn(date(1983, 4, 19), ma_holidays)
        for year in range(1894, 1969):
            self.assertNotIn(date(year, 4, 19), self.holidays)
            self.assertIn(date(year, 4, 19), me_holidays)
            self.assertIn(date(year, 4, 19), ma_holidays)
        for dt in [
            date(1969, 4, 21),
            date(1974, 4, 15),
            date(1975, 4, 21),
            date(2015, 4, 20),
            date(2016, 4, 18),
            date(2019, 4, 15),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, me_holidays)
            self.assertIn(dt, ma_holidays)

    def test_holy_thursday(self):
        vi_holidays = holidays.US(state="VI")
        for dt in [
            date(2010, 4, 1),
            date(2011, 4, 21),
            date(2013, 3, 28),
            date(2014, 4, 17),
            date(2015, 4, 2),
            date(2016, 3, 24),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, vi_holidays)

    def test_good_friday(self):
        ct_holidays = holidays.US(state="CT")
        de_holidays = holidays.US(state="DE")
        gu_holidays = holidays.US(state="GU")
        in_holidays = holidays.US(state="IN")
        ky_holidays = holidays.US(state="IN")
        la_holidays = holidays.US(state="LA")
        nj_holidays = holidays.US(state="NJ")
        nc_holidays = holidays.US(state="NC")
        tn_holidays = holidays.US(state="TN")
        tx_holidays = holidays.US(state="TX")
        vi_holidays = holidays.US(state="VI")
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
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, ct_holidays)
            self.assertIn(dt, de_holidays)
            self.assertIn(dt, gu_holidays)
            self.assertIn(dt, in_holidays)
            self.assertIn(dt, ky_holidays)
            self.assertIn(dt, la_holidays)
            self.assertIn(dt, nj_holidays)
            self.assertIn(dt, nc_holidays)
            self.assertIn(dt, tn_holidays)
            self.assertIn(dt, tx_holidays)
            self.assertIn(dt, vi_holidays)

    def test_easter_monday(self):
        vi_holidays = holidays.US(state="VI")
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
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, vi_holidays)

    def test_confederate_memorial_day(self):
        al_holidays = holidays.US(state="AL")
        ga_holidays = holidays.US(state="GA")
        ms_holidays = holidays.US(state="MS")
        sc_holidays = holidays.US(state="SC")
        tx_holidays = holidays.US(state="TX")
        self.assertNotIn(date(1865, 4, 24), self.holidays)
        self.assertNotIn(date(1865, 4, 24), al_holidays)
        for dt in [
            date(1866, 4, 23),
            date(1878, 4, 22),
            date(1884, 4, 28),
            date(2014, 4, 28),
            date(2015, 4, 27),
            date(2019, 4, 22),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, al_holidays)
            self.assertIn(dt, ga_holidays)
            self.assertIn(dt, ms_holidays)
            self.assertIn(dt, sc_holidays)
        self.assertNotIn(date(1930, 1, 19), tx_holidays)
        self.assertNotIn(date(1931, 1, 19), self.holidays)
        self.assertIn(date(1931, 1, 19), tx_holidays)
        self.assertIn(date(2020, 4, 10), ga_holidays)

    def test_san_jacinto_day(self):
        tx_holidays = holidays.US(state="TX")
        self.assertNotIn(date(1874, 4, 21), tx_holidays)
        for year in (1875, 2050):
            self.assertNotIn(date(year, 4, 21), self.holidays)
            self.assertIn(date(year, 4, 21), tx_holidays)

    def test_arbor_day(self):
        ne_holidays = holidays.US(state="NE")
        for dt in [
            date(1875, 4, 22),
            date(1988, 4, 22),
            date(1989, 4, 28),
            date(2009, 4, 24),
            date(2010, 4, 30),
            date(2014, 4, 25),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, ne_holidays)

    def test_primary_election_day(self):
        in_holidays = holidays.US(state="IN")
        self.assertNotIn(date(2004, 5, 4), in_holidays)
        for dt in [
            date(2006, 5, 2),
            date(2008, 5, 6),
            date(2010, 5, 4),
            date(2012, 5, 8),
            date(2014, 5, 6),
            date(2015, 5, 5),
            date(2016, 5, 3),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, in_holidays)

    def test_truman_day(self):
        mo_holidays = holidays.US(state="MO", observed=False)
        self.assertNotIn(date(1948, 5, 8), self.holidays)
        self.assertNotIn(date(1948, 5, 8), mo_holidays)
        for year in range(1949, 2100):
            dt = date(year, 5, 8)
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, mo_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), mo_holidays)
            self.assertNotIn(dt + relativedelta(days=+1), mo_holidays)
        self.assertNotIn(date(2004, 5, 7), mo_holidays)
        self.assertNotIn(date(2005, 5, 10), mo_holidays)
        mo_holidays.observed = True
        self.assertIn(date(2004, 5, 7), mo_holidays)
        self.assertIn(date(2005, 5, 10), mo_holidays)

    def test_memorial_day(self):
        for dt in [
            date(1969, 5, 30),
            date(1970, 5, 30),
            date(1971, 5, 31),
            date(1997, 5, 26),
            date(1999, 5, 31),
            date(2000, 5, 29),
            date(2012, 5, 28),
            date(2013, 5, 27),
            date(2014, 5, 26),
            date(2015, 5, 25),
            date(2016, 5, 30),
            date(2020, 5, 25),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_jefferson_davis_birthday(self):
        al_holidays = holidays.US(state="AL")
        self.assertNotIn(date(1889, 6, 3), self.holidays)
        self.assertNotIn(date(1889, 6, 3), al_holidays)
        for dt in [
            date(1890, 6, 2),
            date(1891, 6, 1),
            date(1897, 6, 7),
            date(2014, 6, 2),
            date(2015, 6, 1),
            date(2016, 6, 6),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, al_holidays)

    def test_kamehameha_day(self):
        hi_holidays = holidays.US(state="HI")
        self.assertNotIn(date(1871, 6, 11), hi_holidays)
        for year in range(1872, 2050):
            self.assertNotIn(date(year, 6, 11), self.holidays)
            self.assertIn(date(year, 6, 11), hi_holidays)
        self.assertNotIn(date(2006, 6, 12), hi_holidays)
        for dt in [date(2011, 6, 10), date(2016, 6, 10), date(2017, 6, 12)]:
            self.assertIn(dt, hi_holidays)
            self.assertEqual(hi_holidays.get(dt), "Kamehameha Day (Observed)")
        hi_holidays.observed = False
        for dt in [date(2011, 6, 10), date(2016, 6, 10), date(2017, 6, 12)]:
            self.assertNotIn(dt, hi_holidays)

    def test_emancipation_day_in_texas(self):
        tx_holidays = holidays.US(state="TX")
        self.assertNotIn(date(1979, 6, 19), tx_holidays)
        for year in (1980, 2020):
            self.assertNotIn(date(year, 6, 19), self.holidays)
            self.assertIn(date(year, 6, 19), tx_holidays)
        for year in (2021, 2050):
            self.assertIn(date(year, 6, 19), tx_holidays)

    def test_juneteenth(self):
        self.assertNotIn(date(2020, 6, 19), self.holidays)
        self.assertIn(date(2021, 6, 19), self.holidays)

    def test_west_virginia_day(self):
        wv_holidays = holidays.US(state="WV")
        self.assertNotIn(date(1926, 6, 20), wv_holidays)
        for year in (1927, 2050):
            self.assertNotIn(date(year, 6, 20), self.holidays)
            self.assertIn(date(year, 6, 20), wv_holidays)
        self.assertIn(date(2015, 6, 19), wv_holidays)
        self.assertIn(date(2010, 6, 21), wv_holidays)
        wv_holidays.observed = False
        self.assertNotIn(date(2015, 6, 19), wv_holidays)
        self.assertNotIn(date(2010, 6, 21), wv_holidays)

    def test_emancipation_day_in_virgin_islands(self):
        vi_holidays = holidays.US(state="VI")
        for year in (2010, 2021):
            self.assertNotIn(date(year, 7, 3), self.holidays)
            self.assertIn(date(year, 7, 3), vi_holidays)

    def test_independence_day(self):
        for year in range(1900, 2100):
            dt = date(year, 7, 4)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.assertNotIn(date(2010, 7, 5), self.holidays)
        self.assertNotIn(date(2020, 7, 3), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2010, 7, 5), self.holidays)
        self.assertIn(date(2020, 7, 3), self.holidays)

    def test_liberation_day_guam(self):
        gu_holidays = holidays.US(state="GU")
        self.assertNotIn(date(1944, 7, 21), gu_holidays)
        for year in range(1945, 2100):
            self.assertNotIn(date(year, 7, 21), self.holidays)
            self.assertIn(date(year, 7, 21), gu_holidays)

    def test_pioneer_day(self):
        ut_holidays = holidays.US(state="UT")
        self.assertNotIn(date(1848, 7, 24), ut_holidays)
        for year in (1849, 2050):
            self.assertNotIn(date(year, 7, 24), self.holidays)
            self.assertIn(date(year, 7, 24), ut_holidays)
        self.assertIn("2010-07-23", ut_holidays)
        self.assertIn("2011-07-25", ut_holidays)
        ut_holidays.observed = False
        self.assertNotIn("2010-07-23", ut_holidays)
        self.assertNotIn("2011-07-25", ut_holidays)

    def test_constitution_day(self):
        pr_holidays = holidays.US(state="PR")
        for year in range(2010, 2021):
            self.assertNotIn(date(year, 7, 25), self.holidays)
            self.assertIn(date(year, 7, 25), pr_holidays)
        self.assertNotIn(date(2015, 7, 24), pr_holidays)
        self.assertNotIn(date(2015, 7, 26), pr_holidays)
        self.assertIn(date(2021, 7, 26), pr_holidays)

    def test_victory_day(self):
        ri_holidays = holidays.US(state="RI")
        self.assertNotIn(date(1947, 8, 11), ri_holidays)
        for dt in [
            date(1948, 8, 9),
            date(1995, 8, 14),
            date(2005, 8, 8),
            date(2015, 8, 10),
            date(2016, 8, 8),
            date(2017, 8, 14),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, ri_holidays)

    def test_statehood_day(self):
        hi_holidays = holidays.US(state="HI")
        self.assertNotIn(date(1958, 8, 15), hi_holidays)
        for dt in [
            date(1959, 8, 21),
            date(1969, 8, 15),
            date(1999, 8, 20),
            date(2014, 8, 15),
            date(2015, 8, 21),
            date(2016, 8, 19),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, hi_holidays)

    def test_bennington_battle_day(self):
        vt_holidays = holidays.US(state="VT")
        self.assertNotIn(date(1777, 8, 16), vt_holidays)
        for year in range(1778, 2050):
            self.assertNotIn(date(year, 8, 16), self.holidays)
            self.assertIn(date(year, 8, 16), vt_holidays)
        vt_holidays.observed = False
        self.assertNotIn(
            "Bennington Battle Day (Observed)",
            vt_holidays.get_list(date(1997, 8, 15)),
        )
        vt_holidays.observed = True
        self.assertIn(
            "Bennington Battle Day (Observed)",
            vt_holidays.get_list(date(1997, 8, 15)),
        )
        self.assertNotIn(
            "Bennington Battle Day (Observed)",
            vt_holidays.get_list(date(1997, 8, 17)),
        )
        self.assertIn(
            "Bennington Battle Day (Observed)",
            vt_holidays.get_list(date(1998, 8, 17)),
        )
        self.assertNotIn(
            "Bennington Battle Day (Observed)",
            vt_holidays.get_list(date(1999, 8, 15)),
        )
        self.assertNotIn(
            "Bennington Battle Day (Observed)",
            vt_holidays.get_list(date(1999, 8, 17)),
        )

    def test_lyndon_baines_johnson_day(self):
        tx_holidays = holidays.US(state="TX")
        self.assertNotIn(date(1972, 8, 27), tx_holidays)
        for year in (1973, 2050):
            self.assertNotIn(date(year, 8, 27), self.holidays)
            self.assertIn(date(year, 8, 27), tx_holidays)

    def test_labor_day(self):
        for dt in [
            date(1997, 9, 1),
            date(1999, 9, 6),
            date(2000, 9, 4),
            date(2012, 9, 3),
            date(2013, 9, 2),
            date(2014, 9, 1),
            date(2015, 9, 7),
            date(2016, 9, 5),
            date(2020, 9, 7),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_columbus_day(self):
        ak_holidays = holidays.US(state="AK")
        de_holidays = holidays.US(state="DE")
        fl_holidays = holidays.US(state="FL")
        hi_holidays = holidays.US(state="HI")
        sd_holidays = holidays.US(state="SD")
        vi_holidays = holidays.US(state="VI")
        for dt in [
            date(1937, 10, 12),
            date(1969, 10, 12),
            date(1970, 10, 12),
            date(1999, 10, 11),
            date(2000, 10, 9),
            date(2001, 10, 8),
            date(2013, 10, 14),
            date(2018, 10, 8),
            date(2019, 10, 14),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt, ak_holidays)
            self.assertNotIn(dt, de_holidays)
            self.assertNotIn(dt, fl_holidays)
            self.assertNotIn(dt, hi_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertEqual(sd_holidays.get(dt), "Native American Day")
            self.assertEqual(
                vi_holidays.get(dt),
                "Columbus Day and Puerto Rico Friendship Day",
            )
        self.assertNotIn(date(1936, 10, 12), self.holidays)

    def test_alaska_day(self):
        ak_holidays = holidays.US(state="AK", observed=False)
        self.assertNotIn(date(1866, 10, 18), ak_holidays)
        for year in range(1867, 2050):
            self.assertIn(date(year, 10, 18), ak_holidays)
            self.assertNotIn(date(year, 10, 17), ak_holidays)
            self.assertNotIn(date(year, 10, 19), ak_holidays)
            self.assertNotIn(date(year, 10, 18), self.holidays)
        ak_holidays.observed = True
        self.assertIn(date(2014, 10, 17), ak_holidays)
        self.assertIn(date(2015, 10, 19), ak_holidays)

    def test_nevada_day(self):
        nv_holidays = holidays.US(state="NV")
        self.assertNotIn(date(1932, 10, 31), nv_holidays)
        for dt in [
            date(1933, 10, 31),
            date(1999, 10, 31),
            date(2000, 10, 27),
            date(2002, 10, 25),
            date(2014, 10, 31),
            date(2015, 10, 30),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, nv_holidays)
        self.assertIn(
            "Nevada Day (Observed)", nv_holidays.get_list(date(1998, 10, 30))
        )
        self.assertIn(
            "Nevada Day (Observed)", nv_holidays.get_list(date(1999, 11, 1))
        )
        nv_holidays.observed = False
        self.assertNotIn(
            "Nevada Day (Observed)", nv_holidays.get_list(date(1998, 10, 30))
        )
        self.assertNotIn(
            "Nevada Day (Observed)", nv_holidays.get_list(date(1999, 11, 1))
        )

    def test_liberty_day(self):
        vi_holidays = holidays.US(state="VI")
        for year in range(2010, 2021):
            self.assertNotIn(date(year, 11, 1), self.holidays)
            self.assertIn(date(year, 11, 1), vi_holidays)

    def test_election_day(self):
        de_holidays = holidays.US(state="DE")
        hi_holidays = holidays.US(state="HI")
        il_holidays = holidays.US(state="IL")
        in_holidays = holidays.US(state="IN")
        la_holidays = holidays.US(state="LA")
        mt_holidays = holidays.US(state="MT")
        nh_holidays = holidays.US(state="NH")
        nj_holidays = holidays.US(state="NJ")
        ny_holidays = holidays.US(state="NY")
        wv_holidays = holidays.US(state="WV")
        self.assertNotIn(date(2004, 11, 2), de_holidays)
        for dt in [
            date(2008, 11, 4),
            date(2010, 11, 2),
            date(2012, 11, 6),
            date(2014, 11, 4),
            date(2016, 11, 8),
            date(2018, 11, 6),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, de_holidays)
            self.assertIn(dt, hi_holidays)
            self.assertIn(dt, il_holidays)
            self.assertIn(dt, in_holidays)
            self.assertIn(dt, la_holidays)
            self.assertIn(dt, mt_holidays)
            self.assertIn(dt, nh_holidays)
            self.assertIn(dt, nj_holidays)
            self.assertIn(dt, ny_holidays)
            self.assertIn(dt, wv_holidays)
        self.assertNotIn(date(2015, 11, 3), self.holidays)
        self.assertNotIn(date(2015, 11, 3), de_holidays)
        self.assertNotIn(date(2015, 11, 3), hi_holidays)
        self.assertNotIn(date(2015, 11, 3), il_holidays)
        self.assertIn(date(2015, 11, 3), in_holidays)
        self.assertNotIn(date(2015, 11, 3), la_holidays)
        self.assertNotIn(date(2015, 11, 3), mt_holidays)
        self.assertNotIn(date(2015, 11, 3), nh_holidays)
        self.assertNotIn(date(2015, 11, 3), nj_holidays)
        self.assertIn(date(2015, 11, 3), ny_holidays)
        self.assertNotIn(date(2015, 11, 3), wv_holidays)

    def test_all_souls_day(self):
        gu_holidays = holidays.US(state="GU")
        for year in range(1945, 2100):
            self.assertNotIn(date(year, 11, 2), self.holidays)
            self.assertIn(date(year, 11, 2), gu_holidays)

    def test_veterans_day(self):
        for dt in [
            date(1938, 11, 11),
            date(1939, 11, 11),
            date(1970, 11, 11),
            date(1971, 10, 25),
            date(1977, 10, 24),
            date(1978, 11, 11),
            date(2012, 11, 11),
            date(2013, 11, 11),
            date(2014, 11, 11),
            date(2015, 11, 11),
            date(2016, 11, 11),
            date(2020, 11, 11),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.assertNotIn("Armistice Day", holidays.US(years=[1937]).values())
        self.assertNotIn("Armistice Day", holidays.US(years=[1937]).values())
        self.assertIn("Armistice Day", holidays.US(years=[1938]).values())
        self.assertIn("Armistice Day", holidays.US(years=[1953]).values())
        self.assertIn("Veterans Day", holidays.US(years=[1954]).values())
        self.assertNotIn(date(2012, 11, 12), self.holidays)
        self.assertNotIn(date(2017, 11, 10), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2012, 11, 12), self.holidays)
        self.assertIn(date(2017, 11, 10), self.holidays)

    def test_discovery_day(self):
        pr_holidays = holidays.US(state="PR")
        for year in range(2010, 2021):
            self.assertNotIn(date(year, 11, 19), self.holidays)
            self.assertIn(date(year, 11, 19), pr_holidays)
        self.assertNotIn(date(2016, 11, 18), pr_holidays)
        self.assertNotIn(date(2016, 11, 20), pr_holidays)
        self.assertIn(date(2017, 11, 20), pr_holidays)

    def test_thanksgiving_day(self):
        ca_holidays = holidays.US(state="CA")
        de_holidays = holidays.US(state="DE")
        fl_holidays = holidays.US(state="FL")
        in_holidays = holidays.US(state="IN")
        md_holidays = holidays.US(state="MD")
        nv_holidays = holidays.US(state="NV")
        nh_holidays = holidays.US(state="NH")
        nm_holidays = holidays.US(state="NM")
        nc_holidays = holidays.US(state="NC")
        ok_holidays = holidays.US(state="OK")
        tx_holidays = holidays.US(state="TX")
        wv_holidays = holidays.US(state="WV")
        for dt in [
            date(1997, 11, 27),
            date(1999, 11, 25),
            date(2000, 11, 23),
            date(2012, 11, 22),
            date(2013, 11, 28),
            date(2014, 11, 27),
            date(2015, 11, 26),
            date(2016, 11, 24),
            date(2020, 11, 26),
        ]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertIn(dt + relativedelta(days=+1), de_holidays)
            self.assertEqual(
                ca_holidays.get(dt + relativedelta(days=+1)),
                "Day After Thanksgiving",
            )
            self.assertEqual(
                de_holidays.get(dt + relativedelta(days=+1)),
                "Day After Thanksgiving",
            )
            self.assertEqual(
                nh_holidays.get(dt + relativedelta(days=+1)),
                "Day After Thanksgiving",
            )
            self.assertEqual(
                nc_holidays.get(dt + relativedelta(days=+1)),
                "Day After Thanksgiving",
            )
            self.assertEqual(
                ok_holidays.get(dt + relativedelta(days=+1)),
                "Day After Thanksgiving",
            )
            self.assertEqual(
                wv_holidays.get(dt + relativedelta(days=+1)),
                "Day After Thanksgiving",
            )
            self.assertIn(dt + relativedelta(days=+1), fl_holidays)
            self.assertEqual(
                fl_holidays.get(dt + relativedelta(days=+1)),
                "Friday After Thanksgiving",
            )
            self.assertIn(dt + relativedelta(days=+1), tx_holidays)
            self.assertEqual(
                tx_holidays.get(dt + relativedelta(days=+1)),
                "Friday After Thanksgiving",
            )
            self.assertEqual(
                nv_holidays.get(dt + relativedelta(days=+1)), "Family Day"
            )
            self.assertEqual(
                nm_holidays.get(dt + relativedelta(days=+1)), "Presidents' Day"
            )
            if dt.year >= 2008:
                self.assertEqual(
                    md_holidays.get(dt + relativedelta(days=1)),
                    "American Indian Heritage Day",
                )
            if dt.year >= 2010:
                self.assertEqual(
                    in_holidays.get(dt + relativedelta(days=1)),
                    "Lincoln's Birthday",
                )
            else:
                self.assertNotEqual(
                    in_holidays.get(dt + relativedelta(days=1)),
                    "Lincoln's Birthday",
                )

    def test_robert_lee_birthday(self):
        ga_holidays = holidays.US(state="GA")
        self.assertNotIn(date(1985, 11, 25), ga_holidays)
        for dt in [
            date(2007, 11, 23),
            date(2008, 11, 28),
            date(2010, 11, 26),
            date(2013, 11, 29),
            date(2014, 11, 28),
            date(2015, 11, 27),
            date(2018, 11, 23),
            date(2019, 11, 29),
            date(2020, 11, 27),
        ]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, ga_holidays)

    def test_lady_of_camarin_day(self):
        gu_holidays = holidays.US(state="GU")
        for year in range(1945, 2100):
            self.assertNotIn(date(year, 12, 8), self.holidays)
            self.assertIn(date(year, 12, 8), gu_holidays)

    def test_christmas_eve(self):
        as_holidays = holidays.US(state="AS")
        ks_holidays = holidays.US(state="KS")
        mi_holidays = holidays.US(state="MI")
        nc_holidays = holidays.US(state="NC")
        tx_holidays = holidays.US(state="TX")
        wi_holidays = holidays.US(state="WI")
        self.holidays.observed = False
        for year in range(1900, 2050):
            self.assertNotIn(date(year, 12, 24), self.holidays)
            self.assertIn(date(year, 12, 24), as_holidays)
            if year >= 2013:
                f = ks_holidays.get(date(year, 12, 24)).find("Eve")
                self.assertGreater(f, 0)
                f = mi_holidays.get(date(year, 12, 24)).find("Eve")
                self.assertGreater(f, 0)
                f = nc_holidays.get(date(year, 12, 24)).find("Eve")
                self.assertGreater(f, 0)
            if year >= 2012:
                f = wi_holidays.get(date(year, 12, 24)).find("Eve")
                self.assertGreater(f, 0)
            if year >= 1981:
                f = tx_holidays.get(date(year, 12, 24)).find("Eve")
                self.assertGreater(f, 0)
            if year < 1981:
                f = ks_holidays.get(date(year, 12, 24), "").find("Eve")
                self.assertLess(f, 0)
                f = mi_holidays.get(date(year, 12, 24), "").find("Eve")
                self.assertLess(f, 0)
                f = nc_holidays.get(date(year, 12, 24), "").find("Eve")
                self.assertLess(f, 0)
                f = tx_holidays.get(date(year, 12, 24), "").find("Eve")
                self.assertLess(f, 0)
                f = wi_holidays.get(date(year, 12, 24), "").find("Eve")
                self.assertLess(f, 0)
        self.assertIn(date(2016, 12, 23), as_holidays)
        self.assertIn(date(2016, 12, 23), ks_holidays)
        self.assertIn(date(2016, 12, 23), mi_holidays)
        self.assertIn(date(2016, 12, 23), nc_holidays)
        self.assertIn(date(2016, 12, 23), tx_holidays)
        self.assertIn(date(2016, 12, 23), wi_holidays)
        self.assertIn(
            "Christmas Eve (Observed)",
            as_holidays.get_list(date(2017, 12, 22)),
        )
        self.assertIn(
            "Christmas Eve (Observed)",
            ks_holidays.get_list(date(2017, 12, 22)),
        )
        self.assertIn(
            "Christmas Eve (Observed)",
            mi_holidays.get_list(date(2017, 12, 22)),
        )
        self.assertIn(
            "Christmas Eve (Observed)",
            nc_holidays.get_list(date(2017, 12, 22)),
        )
        self.assertIn(
            "Christmas Eve (Observed)",
            tx_holidays.get_list(date(2017, 12, 22)),
        )
        self.assertIn(
            "Christmas Eve (Observed)",
            wi_holidays.get_list(date(2017, 12, 22)),
        )

    def test_christmas_day(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.assertNotIn(date(2010, 12, 24), self.holidays)
        self.assertNotIn(date(2016, 12, 26), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2010, 12, 24), self.holidays)
        self.assertIn(date(2016, 12, 26), self.holidays)

    def test_day_after_christmas(self):
        nc_holidays = holidays.US(state="NC", observed=False)
        tx_holidays = holidays.US(state="TX", observed=False)
        self.assertNotIn(date(2015, 12, 28), nc_holidays)
        self.assertNotIn(date(2016, 12, 27), nc_holidays)
        self.assertNotIn(date(2015, 12, 28), tx_holidays)
        self.assertNotIn(date(2016, 12, 27), tx_holidays)
        nc_holidays.observed = True
        self.assertIn(
            "Day After Christmas (Observed)",
            nc_holidays.get_list(date(2015, 12, 28)),
        )
        self.assertIn(
            "Day After Christmas (Observed)",
            nc_holidays.get_list(date(2016, 12, 27)),
        )
        tx_holidays.observed = True
        self.assertNotIn(
            "Day After Christmas (Observed)",
            tx_holidays.get_list(date(2015, 12, 28)),
        )
        self.assertNotIn(
            "Day After Christmas (Observed)",
            tx_holidays.get_list(date(2016, 12, 27)),
        )

    def test_new_years_eve(self):
        ky_holidays = holidays.US(state="KY")
        mi_holidays = holidays.US(state="MI")
        wi_holidays = holidays.US(state="WI")
        self.assertNotIn(date(2012, 12, 31), ky_holidays)
        self.assertNotIn(date(2012, 12, 31), mi_holidays)
        self.assertNotIn(date(2011, 12, 31), wi_holidays)
        self.assertIn(date(2012, 12, 31), wi_holidays)
        for dt in [date(2013, 12, 31), date(2016, 12, 30)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, ky_holidays)
            self.assertIn(dt, mi_holidays)
            self.assertIn(dt, wi_holidays)
