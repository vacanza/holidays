# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-1017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2018
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from itertools import product
from datetime import date, datetime
from dateutil.relativedelta import relativedelta, MO
import unittest

import holidays


class TestBasics(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.US()

    def test_contains(self):
        self.assertIn(date(2014, 1, 1), self.holidays)
        self.assertNotIn(date(2014, 1, 2), self.holidays)

    def test_getitem(self):
        self.assertEqual(self.holidays[date(2014, 1, 1)], "New Year's Day")
        self.assertEqual(self.holidays.get(date(2014, 1, 1)), "New Year's Day")
        self.assertRaises(KeyError, lambda: self.holidays[date(2014, 1, 2)])
        self.assertIsNone(self.holidays.get(date(2014, 1, 2)))

    def test_get(self):
        self.assertEqual(self.holidays.get('2014-01-01'), "New Year's Day")
        self.assertIsNone(self.holidays.get('2014-01-02'))
        self.assertFalse(self.holidays.get('2014-01-02', False))
        self.assertTrue(self.holidays.get('2014-01-02', True))

    def test_pop(self):
        self.assertRaises(KeyError, lambda: self.holidays.pop('2014-01-02'))
        self.assertFalse(self.holidays.pop('2014-01-02', False))
        self.assertTrue(self.holidays.pop('2014-01-02', True))
        self.assertIn(date(2014, 1, 1), self.holidays)
        self.assertEqual(self.holidays.pop('2014-01-01'), "New Year's Day")
        self.assertNotIn(date(2014, 1, 1), self.holidays)
        self.assertIn(date(2014, 7, 4), self.holidays)

    def test_setitem(self):
        self.holidays = holidays.US(years=[2014])
        self.assertEqual(len(self.holidays), 10)
        self.holidays[date(2014, 1, 3)] = "Fake Holiday"
        self.assertEqual(len(self.holidays), 11)
        self.assertIn(date(2014, 1, 3), self.holidays)
        self.assertEqual(self.holidays.get(date(2014, 1, 3)), "Fake Holiday")

    def test_update(self):
        h = holidays.HolidayBase()
        h.update({
            date(2015, 1, 1): "New Year's Day",
            '2015-12-25': "Christmas Day",
        })
        self.assertIn('2015-01-01', h)
        self.assertIn(date(2015, 12, 25), h)

    def test_append(self):
        h = holidays.HolidayBase()
        h.update({
            date(2015, 1, 1): "New Year's Day",
            '2015-12-25': "Christmas Day",
        })
        h.append([date(2015, 4, 1), '2015-04-03'])
        h.append(date(2015, 4, 6))
        h.append('2015-04-07')
        self.assertIn('2015-01-01', h)
        self.assertIn(date(2015, 12, 25), h)
        self.assertIn('2015-04-01', h)
        self.assertNotIn('2015-04-02', h)
        self.assertIn('2015-04-03', h)
        self.assertNotIn('2015-04-04', h)
        self.assertNotIn('2015-04-05', h)
        self.assertIn('2015-04-06', h)
        self.assertIn('2015-04-07', h)

    def test_eq_ne(self):
        us1 = holidays.UnitedStates()
        us2 = holidays.US()
        us3 = holidays.UnitedStates(years=[2014])
        us4 = holidays.US(years=[2014])
        ca1 = holidays.Canada()
        ca2 = holidays.CA()
        ca3 = holidays.Canada(years=[2014])
        ca4 = holidays.CA(years=[2014])
        self.assertEqual(us1, us2)
        self.assertEqual(us3, us4)
        self.assertEqual(ca1, ca2)
        self.assertEqual(ca3, ca4)
        self.assertNotEqual(us1, us3)
        self.assertNotEqual(us1, ca1)
        self.assertNotEqual(us3, ca3)
        self.assertNotEqual(us1, us3)

    def test_add(self):
        ca = holidays.CA()
        us = holidays.US()
        mx = holidays.MX()
        na = ca + (us + mx)
        self.assertNotIn('2014-07-01', us)
        self.assertIn('2014-07-01', ca)
        self.assertNotIn('2014-07-04', ca)
        self.assertIn('2014-07-04', us)
        self.assertIn('2014-07-04', ca + us)
        self.assertIn('2014-07-04', us + ca)
        self.assertIn('2015-07-04', ca + us)
        self.assertIn('2015-07-04', us + ca)
        self.assertIn('2015-07-01', ca + us)
        self.assertIn('2015-07-01', us + ca)
        self.assertIn('2014-07-04', na)
        self.assertIn('2015-07-04', na)
        self.assertIn('2015-07-01', na)
        self.assertIn('2000-02-05', na)
        self.assertEqual((ca + us).prov, 'ON')
        self.assertEqual((us + ca).prov, 'ON')
        ca = holidays.CA(years=[2014], expand=False)
        us = holidays.US(years=[2014, 2015], expand=True)
        self.assertTrue((ca + us).expand)
        self.assertEqual((ca + us).years, {2014, 2015})
        self.assertEqual((us + ca).years, {2014, 2015})
        na = holidays.CA()
        na += holidays.US()
        na += holidays.MX()
        self.assertEqual(na.country, ['CA', 'US', 'MX'])
        self.assertIn('2014-07-04', na)
        self.assertIn('2014-07-04', na)
        self.assertIn('2015-07-04', na)
        self.assertIn('2015-07-04', na)
        self.assertIn('2015-07-01', na)
        self.assertIn('2015-07-01', na)
        self.assertIn('2000-02-05', na)
        self.assertEqual(na.prov, 'ON')
        na = holidays.CA() + holidays.US()
        na += holidays.MX()
        self.assertIn('2014-07-04', na)
        self.assertIn('2014-07-04', na)
        self.assertIn('2015-07-04', na)
        self.assertIn('2015-07-04', na)
        self.assertIn('2015-07-01', na)
        self.assertIn('2015-07-01', na)
        self.assertIn('2000-02-05', na)
        self.assertEqual(na.prov, 'ON')
        self.assertRaises(TypeError, lambda: holidays.US() + {})
        na = ca + (us + mx) + ca + (mx + us + holidays.CA(prov='BC'))
        self.assertIn('2000-02-05', na)
        self.assertIn('2014-02-10', na)
        self.assertIn('2014-02-17', na)
        self.assertIn('2014-07-04', na)
        provs = (holidays.CA(prov='ON', years=[2014]) +
                 holidays.CA(prov='BC', years=[2015]))
        self.assertIn("2015-02-09", provs)
        self.assertIn("2015-02-16", provs)
        self.assertEqual(provs.prov, ['ON', 'BC'])
        a = sum(holidays.CA(prov=x) for x in holidays.CA.PROVINCES)
        self.assertEqual(a.country, 'CA')
        self.assertEqual(a.prov, holidays.CA.PROVINCES)
        self.assertIn("2015-02-09", a)
        self.assertIn("2015-02-16", a)
        na = holidays.CA() + holidays.US() + holidays.MX()
        self.assertIn(date(1969, 12, 25), na)
        self.assertEqual(na.get(date(1969, 7, 1)), "Dominion Day")
        self.assertEqual(na.get(date(1983, 7, 1)), "Canada Day")
        self.assertEqual(na.get(date(1969, 12, 25)),
                         "Christmas Day, Navidad [Christmas]")
        na = holidays.MX() + holidays.CA() + holidays.US()
        self.assertEqual(na.get(date(1969, 12, 25)),
                         "Navidad [Christmas], Christmas Day")

    def test_get_list(self):
        westland = holidays.NZ(prov='WTL')
        chathams = holidays.NZ(prov='CIT')
        wild = westland + chathams
        self.assertEqual(wild[date(1969, 12, 1)],
                         ("Westland Anniversary Day, " +
                          "Chatham Islands Anniversary Day"))

        self.assertEqual(wild.get_list(date(1969, 12, 1)),
                         ["Westland Anniversary Day",
                          "Chatham Islands Anniversary Day"])
        self.assertEqual(wild.get_list(date(1969, 1, 1)),
                         ["New Year's Day"])
        self.assertEqual(westland.get_list(date(1969, 12, 1)),
                         ["Westland Anniversary Day"])
        self.assertEqual(westland.get_list(date(1969, 1, 1)),
                         ["New Year's Day"])
        self.assertEqual(chathams.get_list(date(1969, 12, 1)),
                         ["Chatham Islands Anniversary Day"])
        self.assertEqual(chathams.get_list(date(1969, 1, 1)),
                         ["New Year's Day"])
        ca = holidays.CA()
        us = holidays.US()
        mx = holidays.MX()
        na = ca + us + mx
        self.assertIn(date(1969, 12, 25), na)
        self.assertEqual(na.get_list(date(1969, 12, 25)),
                         ["Christmas Day", "Navidad [Christmas]"])
        self.assertEqual(na.get_list(date(1969, 7, 1)), ["Dominion Day"])
        self.assertEqual(na.get_list(date(1969, 1, 3)), [])

    def test_radd(self):
        self.assertRaises(TypeError, lambda: 1 + holidays.US())

    def test_inheritance(self):
        class NoColumbusHolidays(holidays.US):
            def _populate(self, year):
                holidays.US._populate(self, year)
                self.pop(date(year, 10, 1) + relativedelta(weekday=MO(+2)))

        hdays = NoColumbusHolidays()
        self.assertIn(date(2014, 10, 13), self.holidays)
        self.assertNotIn(date(2014, 10, 13), hdays)
        self.assertIn(date(2014, 1, 1), hdays)
        self.assertIn(date(2020, 10, 12), self.holidays)
        self.assertNotIn(date(2020, 10, 12), hdays)
        self.assertIn(date(2020, 1, 1), hdays)

        class NinjaTurtlesHolidays(holidays.US):
            def _populate(self, year):
                holidays.US._populate(self, year)
                self[date(year, 7, 13)] = "Ninja Turtle's Day"

        hdays = NinjaTurtlesHolidays()
        self.assertNotIn(date(2014, 7, 13), self.holidays)
        self.assertIn(date(2014, 7, 13), hdays)
        self.assertIn(date(2014, 1, 1), hdays)
        self.assertNotIn(date(2020, 7, 13), self.holidays)
        self.assertIn(date(2020, 7, 13), hdays)
        self.assertIn(date(2020, 1, 1), hdays)

        class NewCountry(holidays.HolidayBase):
            def _populate(self, year):
                self[date(year, 1, 2)] = "New New Year's"

        hdays = NewCountry()
        self.assertNotIn(date(2014, 1, 1), hdays)
        self.assertIn(date(2014, 1, 2), hdays)

        class Dec31Holiday(holidays.HolidayBase):
            def _populate(self, year):
                self[date(year, 12, 31)] = "New Year's Eve"

        self.assertIn(date(2014, 12, 31), Dec31Holiday())


class TestArgs(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.US()

    def test_country(self):
        self.assertEqual(self.holidays.country, 'US')
        self.assertIn(date(2014, 7, 4), self.holidays)
        self.assertNotIn(date(2014, 7, 1), self.holidays)
        self.holidays = holidays.UnitedStates()
        self.assertEqual(self.holidays.country, 'US')
        self.assertIn(date(2014, 7, 4), self.holidays)
        self.assertNotIn(date(2014, 7, 1), self.holidays)
        self.assertEqual(self.holidays.country, 'US')
        self.holidays = holidays.CA()
        self.assertEqual(self.holidays.country, 'CA')
        self.assertEqual(self.holidays.prov, 'ON')
        self.assertIn(date(2014, 7, 1), self.holidays)
        self.assertNotIn(date(2014, 7, 4), self.holidays)
        self.holidays = holidays.CA(prov='BC')
        self.assertEqual(self.holidays.country, 'CA')
        self.assertEqual(self.holidays.prov, 'BC')
        self.assertIn(date(2014, 7, 1), self.holidays)
        self.assertNotIn(date(2014, 7, 4), self.holidays)

    def test_years(self):
        self.assertEqual(len(self.holidays.years), 0)
        self.assertNotIn(date(2014, 1, 2), self.holidays)
        self.assertEqual(len(self.holidays.years), 1)
        self.assertIn(2014, self.holidays.years)
        self.assertNotIn(date(2013, 1, 2), self.holidays)
        self.assertNotIn(date(2014, 1, 2), self.holidays)
        self.assertNotIn(date(2015, 1, 2), self.holidays)
        self.assertEqual(len(self.holidays.years), 3)
        self.assertIn(2013, self.holidays.years)
        self.assertIn(2015, self.holidays.years)
        self.holidays = holidays.US(years=range(2010, 2015 + 1))
        self.assertEqual(len(self.holidays.years), 6)
        self.assertNotIn(2009, self.holidays.years)
        self.assertIn(2010, self.holidays.years)
        self.assertIn(2015, self.holidays.years)
        self.assertNotIn(2016, self.holidays.years)
        self.holidays = holidays.US(years=(2013, 2015, 2015))
        self.assertEqual(len(self.holidays.years), 2)
        self.assertIn(2013, self.holidays.years)
        self.assertNotIn(2014, self.holidays.years)
        self.assertIn(2015, self.holidays.years)
        self.assertIn(date(2021, 12, 31), holidays.US(years=[2022]).keys())
        self.holidays = holidays.US(years=2015)
        self.assertNotIn(2014, self.holidays.years)
        self.assertIn(2015, self.holidays.years)

    def test_expand(self):
        self.holidays = holidays.US(years=(2013, 2015), expand=False)
        self.assertEqual(len(self.holidays.years), 2)
        self.assertIn(2013, self.holidays.years)
        self.assertNotIn(2014, self.holidays.years)
        self.assertIn(2015, self.holidays.years)
        self.assertNotIn(date(2014, 1, 1), self.holidays)
        self.assertEqual(len(self.holidays.years), 2)
        self.assertNotIn(2014, self.holidays.years)

    def test_observed(self):
        self.holidays = holidays.US(observed=False)
        self.assertIn(date(2000, 1, 1), self.holidays)
        self.assertNotIn(date(1999, 12, 31), self.holidays)
        self.assertIn(date(2012, 1, 1), self.holidays)
        self.assertNotIn(date(2012, 1, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2000, 1, 1), self.holidays)
        self.assertIn(date(1999, 12, 31), self.holidays)
        self.assertIn(date(2012, 1, 1), self.holidays)
        self.assertIn(date(2012, 1, 2), self.holidays)
        self.holidays.observed = False
        self.assertIn(date(2000, 1, 1), self.holidays)
        self.assertNotIn(date(1999, 12, 31), self.holidays)
        self.assertIn(date(2012, 1, 1), self.holidays)
        self.assertNotIn(date(2012, 1, 2), self.holidays)
        self.holidays = holidays.US(years=[2022], observed=False)
        self.assertNotIn(date(2021, 12, 31), self.holidays.keys())

        self.holidays = holidays.CA(observed=False)
        self.assertNotIn(date(1878, 7, 3), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2018, 7, 2), self.holidays)


class TestKeyTransforms(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.US()

    def test_dates(self):
        self.assertIn(date(2014, 1, 1), self.holidays)
        self.assertEqual(self.holidays[date(2014, 1, 1)], "New Year's Day")
        self.holidays[date(2014, 1, 3)] = "Fake Holiday"
        self.assertIn(date(2014, 1, 3), self.holidays)
        self.assertEqual(self.holidays.pop(date(2014, 1, 3)), "Fake Holiday")
        self.assertNotIn(date(2014, 1, 3), self.holidays)

    def test_datetimes(self):
        self.assertIn(datetime(2014, 1, 1, 13, 45), self.holidays)
        self.assertEqual(self.holidays[datetime(2014, 1, 1, 13, 45)],
                         "New Year's Day")
        self.holidays[datetime(2014, 1, 3, 1, 1)] = "Fake Holiday"
        self.assertIn(datetime(2014, 1, 3, 2, 2), self.holidays)
        self.assertEqual(self.holidays.pop(datetime(2014, 1, 3, 4, 4)),
                         "Fake Holiday")
        self.assertNotIn(datetime(2014, 1, 3, 2, 2), self.holidays)

    def test_timestamp(self):
        self.assertIn(1388552400, self.holidays)
        self.assertEqual(self.holidays[1388552400], "New Year's Day")
        self.assertIn(1388552400.01, self.holidays)
        self.assertEqual(self.holidays[1388552400.01], "New Year's Day")
        self.holidays[1388725200] = "Fake Holiday"
        self.assertIn(1388725201, self.holidays)
        self.assertEqual(self.holidays.pop(1388725202), "Fake Holiday")
        self.assertNotIn(1388725201, self.holidays)

    def test_strings(self):
        self.assertIn("2014-01-01", self.holidays)
        self.assertEqual(self.holidays["2014-01-01"], "New Year's Day")
        self.assertIn("01/01/2014", self.holidays)
        self.assertEqual(self.holidays["01/01/2014"], "New Year's Day")
        self.holidays["01/03/2014"] = "Fake Holiday"
        self.assertIn("01/03/2014", self.holidays)
        self.assertEqual(self.holidays.pop("01/03/2014"), "Fake Holiday")
        self.assertNotIn("01/03/2014", self.holidays)

    def test_exceptions(self):
        self.assertRaises(
            (TypeError, ValueError), lambda: "abc" in self.holidays)
        self.assertRaises(
            (TypeError, ValueError), lambda: self.holidays.get("abc123"))
        self.assertRaises(
            (TypeError, ValueError), self.holidays.__setitem__, "abc", "Test")
        self.assertRaises(
            (TypeError, ValueError), lambda: {} in self.holidays)


class TestCountryHoliday(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.CountryHoliday('US')

    def test_country(self):
        self.assertEqual(self.holidays.country, 'US')

    def test_country_state(self):
        h = holidays.CountryHoliday('US', state='NY')
        self.assertEqual(h.state, 'NY')

    def test_country_province(self):
        h = holidays.CountryHoliday('AU', prov='NT')
        self.assertEqual(h.prov, 'NT')

    def test_exceptions(self):
        self.assertRaises((KeyError), lambda: holidays.CountryHoliday('XXXX'))


class TestCA(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.CA(observed=False)

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

    def test_islander_day(self):
        pei_holidays = holidays.CA(prov="PE")
        for dt in [date(2009, 2, 9), date(2010, 2, 15), date(2011, 2, 21),
                   date(2012, 2, 20), date(2013, 2, 18), date(2014, 2, 17),
                   date(2015, 2, 16), date(2016, 2, 15), date(2020, 2, 17)]:
            if dt.year >= 2010:
                self.assertNotEqual(self.holidays[dt], "Islander Day")
            elif dt.year == 2009:
                self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, pei_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), pei_holidays)
            self.assertNotIn(dt + relativedelta(days=+1), pei_holidays)

    def test_family_day(self):
        ab_holidays = holidays.CA(prov="AB")
        bc_holidays = holidays.CA(prov="BC")
        mb_holidays = holidays.CA(prov="MB")
        sk_holidays = holidays.CA(prov="SK")
        for dt in [date(1990, 2, 19), date(1999, 2, 15), date(2000, 2, 21),
                   date(2006, 2, 20)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, ab_holidays)
            self.assertNotIn(dt, bc_holidays)
            self.assertNotIn(dt, mb_holidays)
            self.assertNotIn(dt, sk_holidays)
        dt = date(2007, 2, 19)
        self.assertNotIn(dt, self.holidays)
        self.assertIn(dt, ab_holidays)
        self.assertNotIn(dt, bc_holidays)
        self.assertNotIn(dt, mb_holidays)
        self.assertIn(dt, sk_holidays)
        for dt in [date(2008, 2, 18), date(2012, 2, 20), date(2014, 2, 17),
                   date(2018, 2, 19)]:
            self.assertIn(dt, self.holidays)
            self.assertIn(dt, ab_holidays)
            self.assertNotIn(dt, bc_holidays)
            self.assertIn(dt, mb_holidays)
            self.assertIn(dt, sk_holidays)
        for dt in [date(2019, 2, 18), date(2020, 2, 17)]:
            self.assertIn(dt, self.holidays)
            self.assertIn(dt, ab_holidays)
            self.assertIn(dt, bc_holidays)
            self.assertIn(dt, mb_holidays)
            self.assertIn(dt, sk_holidays)
        for dt in [date(2013, 2, 11), date(2016, 2, 8)]:
            self.assertNotIn(dt, self.holidays)
            self.assertNotIn(dt, ab_holidays)
            self.assertIn(dt, bc_holidays)
            self.assertNotIn(dt, mb_holidays)
            self.assertNotIn(dt, sk_holidays)
        self.assertEqual(mb_holidays[date(2014, 2, 17)], "Louis Riel Day")

    def test_st_patricks_day(self):
        nl_holidays = holidays.CA(prov="NL", observed=False)
        for dt in [date(1900, 3, 19), date(1999, 3, 15), date(2000, 3, 20),
                   date(2012, 3, 19), date(2013, 3, 18), date(2014, 3, 17),
                   date(2015, 3, 16), date(2016, 3, 14), date(2020, 3, 16)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, nl_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), nl_holidays)
            self.assertNotIn(dt + relativedelta(days=+1), nl_holidays)

    def test_good_friday(self):
        qc_holidays = holidays.CA(prov="QC")
        for dt in [date(1900, 4, 13), date(1901, 4, 5), date(1902, 3, 28),
                   date(1999, 4, 2), date(2000, 4, 21), date(2010, 4, 2),
                   date(2018, 3, 30), date(2019, 4, 19), date(2020, 4, 10)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt, qc_holidays)

    def test_easter_monday(self):
        qc_holidays = holidays.CA(prov="QC")
        for dt in [date(1900, 4, 16), date(1901, 4, 8), date(1902, 3, 31),
                   date(1999, 4, 5), date(2000, 4, 24), date(2010, 4, 5),
                   date(2018, 4, 2), date(2019, 4, 22), date(2020, 4, 13)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, qc_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), qc_holidays)
            self.assertNotIn(dt + relativedelta(days=+1), qc_holidays)

    def test_st_georges_day(self):
        nl_holidays = holidays.CA(prov="NL")
        for dt in [date(1990, 4, 23), date(1999, 4, 26), date(2000, 4, 24),
                   date(2010, 4, 19), date(2016, 4, 25), date(2020, 4, 20)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, nl_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), nl_holidays)
            self.assertNotIn(dt + relativedelta(days=+1), nl_holidays)

    def test_victoria_day(self):
        for dt in [date(1953, 5, 18), date(1999, 5, 24), date(2000, 5, 22),
                   date(2010, 5, 24), date(2015, 5, 18), date(2020, 5, 18)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_national_aboriginal_day(self):
        nt_holidays = holidays.CA(prov="NT")
        self.assertNotIn(date(1995, 6, 21), nt_holidays)
        for year in range(1996, 2100):
            dt = date(year, 6, 21)
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, nt_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), nt_holidays)
            self.assertNotIn(dt + relativedelta(days=+1), nt_holidays)

    def test_st_jean_baptiste_day(self):
        qc_holidays = holidays.CA(prov="QC", observed=False)
        self.assertNotIn(date(1924, 6, 24), qc_holidays)
        for year in range(1925, 2100):
            dt = date(year, 6, 24)
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, qc_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), qc_holidays)
            self.assertNotIn(dt + relativedelta(days=+1), qc_holidays)
        self.assertNotIn(date(2001, 6, 25), qc_holidays)
        qc_holidays.observed = True
        self.assertIn(date(2001, 6, 25), qc_holidays)

    def test_discovery_day(self):
        nl_holidays = holidays.CA(prov="NL")
        yu_holidays = holidays.CA(prov="YU")
        for dt in [date(1997, 6, 23), date(1999, 6, 21), date(2000, 6, 26),
                   date(2010, 6, 21), date(2016, 6, 27), date(2020, 6, 22)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, nl_holidays)
            self.assertNotIn(dt, yu_holidays)
        for dt in [date(1912, 8, 19), date(1999, 8, 16), date(2000, 8, 21),
                   date(2006, 8, 21), date(2016, 8, 15), date(2020, 8, 17)]:
            self.assertNotIn(dt, self.holidays)
            self.assertNotIn(dt, nl_holidays)
            self.assertIn(dt, yu_holidays)

    def test_canada_day(self):
        for year in range(1900, 2100):
            dt = date(year, 7, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.assertNotIn(date(2006, 7, 3), self.holidays)
        self.assertNotIn(date(2007, 7, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2006, 7, 3), self.holidays)
        self.assertIn(date(2007, 7, 2), self.holidays)

    def test_nunavut_day(self):
        nu_holidays = holidays.CA(prov="NU", observed=False)
        self.assertNotIn(date(1999, 7, 9), nu_holidays)
        self.assertNotIn(date(2000, 7, 9), nu_holidays)
        self.assertIn(date(2000, 4, 1), nu_holidays)
        for year in range(2001, 2100):
            dt = date(year, 7, 9)
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, nu_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), nu_holidays)
            self.assertNotIn(dt + relativedelta(days=+1), nu_holidays)
        self.assertNotIn(date(2017, 7, 10), nu_holidays)
        nu_holidays.observed = True
        self.assertIn(date(2017, 7, 10), nu_holidays)

    def test_civic_holiday(self):
        bc_holidays = holidays.CA(prov="BC")
        for dt in [date(1900, 8, 6), date(1955, 8, 1), date(1973, 8, 6)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt, bc_holidays)
        for dt in [date(1974, 8, 5), date(1999, 8, 2), date(2000, 8, 7),
                   date(2010, 8, 2), date(2015, 8, 3), date(2020, 8, 3)]:
            self.assertIn(dt, self.holidays)
            self.assertIn(dt, bc_holidays)

    def test_labour_day(self):
        self.assertNotIn(date(1893, 9, 4), self.holidays)
        for dt in [date(1894, 9, 3), date(1900, 9, 3), date(1999, 9, 6),
                   date(2000, 9, 4), date(2014, 9, 1), date(2015, 9, 7)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_thanksgiving(self):
        ns_holidays = holidays.CA(prov="NB")
        for dt in [date(1931, 10, 12), date(1990, 10, 8), date(1999, 10, 11),
                   date(2000, 10, 9), date(2013, 10, 14), date(2020, 10, 12)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt, ns_holidays)

    def test_remembrance_day(self):
        ab_holidays = holidays.CA(prov="AB", observed=False)
        nl_holidays = holidays.CA(prov="NL", observed=False)
        self.assertNotIn(date(1930, 11, 11), ab_holidays)
        self.assertNotIn(date(1930, 11, 11), nl_holidays)
        for year in range(1931, 2100):
            dt = date(year, 11, 11)
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, ab_holidays)
            self.assertIn(dt, nl_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), nl_holidays)
            self.assertNotIn(dt + relativedelta(days=+1), nl_holidays)
        self.assertNotIn(date(2007, 11, 12), ab_holidays)
        self.assertNotIn(date(2007, 11, 12), nl_holidays)
        ab_holidays.observed = True
        nl_holidays.observed = True
        self.assertNotIn(date(2007, 11, 12), ab_holidays)
        self.assertIn(date(2007, 11, 12), nl_holidays)

    def test_christmas_day(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
        self.assertNotIn(date(2010, 12, 24), self.holidays)
        self.assertNotEqual(self.holidays[date(2011, 12, 26)],
                            "Christmas Day (Observed)")
        self.holidays.observed = True
        self.assertIn(date(2010, 12, 24), self.holidays)
        self.assertEqual(self.holidays[date(2011, 12, 26)],
                         "Christmas Day (Observed)")

    def test_boxing_day(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 26)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.assertNotIn(date(2009, 12, 28), self.holidays)
        self.assertNotIn(date(2010, 12, 27), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2009, 12, 28), self.holidays)
        self.assertIn(date(2010, 12, 27), self.holidays)


class TestCO(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.CO(observed=True)

    def test_2016(self):
        # http://www.officeholidays.com/countries/colombia/
        self.assertIn(date(2016, 1, 1), self.holidays)
        self.assertIn(date(2016, 1, 11), self.holidays)
        self.assertIn(date(2016, 3, 21), self.holidays)
        self.assertIn(date(2016, 3, 24), self.holidays)
        self.assertIn(date(2016, 3, 25), self.holidays)
        self.assertIn(date(2016, 5, 1), self.holidays)
        self.assertIn(date(2016, 5, 9), self.holidays)
        self.assertIn(date(2016, 5, 30), self.holidays)
        self.assertIn(date(2016, 6, 6), self.holidays)
        self.assertIn(date(2016, 7, 4), self.holidays)
        self.assertIn(date(2016, 7, 20), self.holidays)
        self.assertIn(date(2016, 8, 7), self.holidays)
        self.assertIn(date(2016, 8, 15), self.holidays)
        self.assertIn(date(2016, 10, 17), self.holidays)
        self.assertIn(date(2016, 11, 7), self.holidays)
        self.assertIn(date(2016, 11, 14), self.holidays)
        self.assertIn(date(2016, 12, 8), self.holidays)
        self.assertIn(date(2016, 12, 25), self.holidays)

    def test_others(self):
        # holidays falling on weekend
        self.assertNotIn(date(2017, 1, 1), self.holidays)
        self.assertNotIn(date(2014, 7, 20), self.holidays)
        self.assertNotIn(date(2018, 8, 12), self.holidays)

        self.assertIn(date(2014, 1, 6), self.holidays)
        self.assertIn(date(2012, 3, 19), self.holidays)
        self.assertIn(date(2015, 6, 29), self.holidays)
        self.assertIn(date(2010, 8, 16), self.holidays)
        self.assertIn(date(2015, 10, 12), self.holidays)
        self.assertIn(date(2010, 11, 1), self.holidays)
        self.assertIn(date(2013, 11, 11), self.holidays)
        self.holidays.observed = False
        self.assertIn(date(2016, 5, 5), self.holidays)
        self.assertIn(date(2016, 5, 26), self.holidays)


class TestMX(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.MX(observed=False)

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

    def test_constitution_day(self):
        for dt in [date(2005, 2, 5), date(2006, 2, 5), date(2007, 2, 5),
                   date(2008, 2, 4), date(2009, 2, 2), date(2010, 2, 1),
                   date(2015, 2, 2), date(2016, 2, 1), date(2020, 2, 3)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_benito_juarez(self):
        for dt in [date(2005, 3, 21), date(2006, 3, 21), date(2007, 3, 19),
                   date(2008, 3, 17), date(2009, 3, 16), date(2010, 3, 15),
                   date(2015, 3, 16), date(2016, 3, 21), date(2020, 3, 16)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_labor_day(self):
        self.assertNotIn(date(2010, 4, 30), self.holidays)
        self.assertNotIn(date(2011, 5, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2010, 4, 30), self.holidays)
        self.assertIn(date(2011, 5, 2), self.holidays)
        self.holidays.observed = False
        self.assertNotIn(date(1922, 5, 1), self.holidays)
        for year in range(1923, 2100):
            dt = date(year, 5, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_independence_day(self):
        self.assertNotIn(date(2006, 9, 15), self.holidays)
        self.assertNotIn(date(2007, 9, 17), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2006, 9, 15), self.holidays)
        self.assertIn(date(2007, 9, 17), self.holidays)
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 9, 16)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_revolution_day(self):
        for dt in [date(2005, 11, 20), date(2006, 11, 20), date(2007, 11, 19),
                   date(2008, 11, 17), date(2009, 11, 16), date(2010, 11, 15),
                   date(2015, 11, 16), date(2016, 11, 21), date(2020, 11, 16)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_change_of_government(self):
        self.assertNotIn(date(2012, 11, 30), self.holidays)
        self.assertNotIn(date(2024, 12, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2012, 11, 30), self.holidays)
        self.assertIn(date(2024, 12, 2), self.holidays)
        self.holidays.observed = False
        for year in range(1970, 2100):
            dt = date(year, 12, 1)
            if (2018 - year) % 6 == 0:
                self.assertIn(dt, self.holidays)
                self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
                self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            else:
                self.assertNotIn(dt, self.holidays)

    def test_christmas(self):
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


class TestNetherlands(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.NL()

    def test_2017(self):
        # http://www.iamsterdam.com/en/plan-your-trip/practical-info/public-holidays
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 4, 16), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 4, 27), self.holidays)
        self.assertIn(date(2017, 5, 25), self.holidays)
        self.assertIn(date(2017, 6, 4), self.holidays)
        self.assertIn(date(2017, 6, 5), self.holidays)
        self.assertIn(date(2017, 12, 25), self.holidays)
        self.assertIn(date(2017, 12, 26), self.holidays)

    def test_new_years(self):
        self.assertIn(date(2017, 1, 1), self.holidays)

    def test_easter(self):
        self.assertIn(date(2017, 4, 16), self.holidays)

    def test_easter_monday(self):
        self.assertIn(date(2017, 4, 17), self.holidays)

    def test_queens_day_between_1891_and_1948(self):
        # Between 1891 and 1948 Queens Day was celebrated on 8-31
        self.holidays = holidays.NL(years=[1901])
        self.assertIn(date(1901, 8, 31), self.holidays)

    def test_queens_day_between_1891_and_1948_substituted_later(self):
        # Between 1891 and 1948 Queens Day was celebrated on 9-1
        #  (one day later) when Queens Day falls on a Sunday
        self.holidays = holidays.NL(years=[1947])
        self.assertIn(date(1947, 9, 1), self.holidays)

    def test_queens_day_between_1949_and_2013(self):
        self.holidays = holidays.NL(years=[1965])
        self.assertIn(date(1965, 4, 30), self.holidays)

    def test_queens_day_between_1949_and_1980_substituted_later(self):
        self.holidays = holidays.NL(years=[1967])
        self.assertIn(date(1967, 5, 1), self.holidays)

    def test_queens_day_between_1980_and_2013_substituted_earlier(self):
        self.holidays = holidays.NL(years=[2006])
        self.assertIn(date(2006, 4, 29), self.holidays)

    def test_kings_day_after_2014(self):
        self.holidays = holidays.NL(years=[2013])
        self.assertNotIn(date(2013, 4, 27), self.holidays)

        self.holidays = holidays.NL(years=[2017])
        self.assertIn(date(2017, 4, 27), self.holidays)

    def test_kings_day_after_2014_substituted_earlier(self):
        self.holidays = holidays.NL(years=[2188])
        self.assertIn(date(2188, 4, 26), self.holidays)

    def test_liberation_day(self):
        self.holidays = holidays.NL(years=1900)
        self.assertNotIn(date(1900, 5, 5), self.holidays)

    def test_liberation_day_after_1990_non_lustrum_year(self):
        self.holidays = holidays.NL(years=2017)
        self.assertNotIn(date(2017, 5, 5), self.holidays)

    def test_liberation_day_after_1990_in_lustrum_year(self):
        self.holidays = holidays.NL(years=2020)
        self.assertIn(date(2020, 5, 5), self.holidays)

    def test_ascension_day(self):
        self.holidays = holidays.NL(years=2017)
        self.assertIn(date(2017, 5, 25), self.holidays)

    def test_whit_sunday(self):
        self.holidays = holidays.NL(years=2017)
        self.assertIn(date(2017, 6, 4), self.holidays)

    def test_whit_monday(self):
        self.holidays = holidays.NL(years=2017)
        self.assertIn(date(2017, 6, 5), self.holidays)

    def test_first_christmas(self):
        self.holidays = holidays.NL(years=2017)
        self.assertIn(date(2017, 12, 25), self.holidays)

    def test_second_christmas(self):
        self.holidays = holidays.NL(years=2017)
        self.assertIn(date(2017, 12, 26), self.holidays)


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
        pr_holidays = holidays.US(state='PR')
        for year in range(2010, 2021):
            self.assertNotIn(date(year, 1, 6), self.holidays)
            self.assertIn(date(year, 1, 6), pr_holidays)

    def test_three_kings_day(self):
        vi_holidays = holidays.US(state='VI')
        for year in range(2010, 2021):
            self.assertNotIn(date(year, 1, 6), self.holidays)
            self.assertIn(date(year, 1, 6), vi_holidays)

    def test_lee_jackson_day(self):
        va_holidays = holidays.US(state='VA')
        self.assertNotIn(date(1888, 1, 19), va_holidays)
        self.assertNotIn(date(1983, 1, 19), va_holidays)
        self.assertNotIn("Lee Jackson Day",
                         va_holidays.get_list(date(2000, 1, 17)))
        for dt in [date(1889, 1, 19), date(1982, 1, 19), date(1983, 1, 17),
                   date(1999, 1, 18), date(2000, 1, 14), date(2001, 1, 12),
                   date(2013, 1, 18), date(2014, 1, 17), date(2018, 1, 12)]:
            self.assertNotIn("Lee Jackson Day", self.holidays.get_list(dt))
            self.assertIn(dt, va_holidays)
            self.assertIn("Lee Jackson Day", va_holidays.get_list(dt))

    def test_inauguration_day(self):
        name = "Inauguration Day"
        dc_holidays = holidays.US(state='DC')
        la_holidays = holidays.US(state='LA')
        md_holidays = holidays.US(state='MD')
        va_holidays = holidays.US(state='VA')
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

    def test_marthin_luther(self):
        for dt in [date(1986, 1, 20), date(1999, 1, 18), date(2000, 1, 17),
                   date(2012, 1, 16), date(2013, 1, 21), date(2014, 1, 20),
                   date(2015, 1, 19), date(2016, 1, 18), date(2020, 1, 20)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        self.assertNotIn("Martin Luther King, Jr. Day",
                         holidays.US(years=[1985]).values())
        self.assertIn("Martin Luther King, Jr. Day",
                      holidays.US(years=[1986]).values())
        self.assertEqual(holidays.US(state='AL').get('2015-01-19'),
                         "Robert E. Lee/Martin Luther King Birthday")
        self.assertEqual(holidays.US(state='AS').get('2015-01-19'),
                         ("Dr. Martin Luther King Jr. "
                          "and Robert E. Lee's Birthdays"))
        self.assertEqual(holidays.US(state='MS').get('2015-01-19'),
                         ("Dr. Martin Luther King Jr. "
                          "and Robert E. Lee's Birthdays"))
        self.assertEqual(holidays.US(state='AZ').get('2015-01-19'),
                         "Dr. Martin Luther King Jr./Civil Rights Day")
        self.assertEqual(holidays.US(state='NH').get('2015-01-19'),
                         "Dr. Martin Luther King Jr./Civil Rights Day")
        self.assertEqual(holidays.US(state='ID').get('2015-01-19'),
                         "Martin Luther King, Jr. - Idaho Human Rights Day")
        self.assertNotEqual(holidays.US(state='ID').get('2000-01-17'),
                            "Martin Luther King, Jr. - Idaho Human Rights Day")
        self.assertEqual(holidays.US(state='GA').get('2011-01-17'),
                         "Robert E. Lee's Birthday")

    def test_lincolns_birthday(self):
        ca_holidays = holidays.US(state='CA')
        ct_holidays = holidays.US(state='CT')
        il_holidays = holidays.US(state='IL')
        ia_holidays = holidays.US(state='IA')
        nj_holidays = holidays.US(state='NJ')
        ny_holidays = holidays.US(state='NY')
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
        ca_holidays = holidays.US(state='CA')
        fl_holidays = holidays.US(state='FL')
        ny_holidays = holidays.US(state='NY')
        wi_holidays = holidays.US(state='WI')
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
        de_holidays = holidays.US(state='DE')
        fl_holidays = holidays.US(state='FL')
        ga_holidays = holidays.US(state='GA')
        nm_holidays = holidays.US(state='NM')
        for dt in [date(1969, 2, 22), date(1970, 2, 22), date(1971, 2, 15),
                   date(1997, 2, 17), date(1999, 2, 15), date(2000, 2, 21),
                   date(2012, 2, 20), date(2013, 2, 18), date(2014, 2, 17),
                   date(2015, 2, 16), date(2016, 2, 15), date(2020, 2, 17)]:
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
        self.assertEqual(holidays.US(state='AL').get('2015-02-16'),
                         "George Washington/Thomas Jefferson Birthday")
        self.assertEqual(holidays.US(state='AS').get('2015-02-16'),
                         ("George Washington's Birthday "
                          "and Daisy Gatson Bates Day"))
        self.assertEqual(holidays.US(state='PR').get('2015-02-16'),
                         "Presidents' Day")
        self.assertEqual(holidays.US(state='VI').get('2015-02-16'),
                         "Presidents' Day")

    def test_mardi_gras(self):
        la_holidays = holidays.US(state='LA')
        self.assertNotIn(date(1856, 2, 5), la_holidays)
        for dt in [date(1857, 2, 24), date(2008, 2, 5), date(2011, 3, 8),
                   date(2012, 2, 21), date(2014, 3, 4), date(2018, 2, 13)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, la_holidays)

    def test_guam_discovery_day(self):
        gu_holidays = holidays.US(state='GU')
        self.assertNotIn(date(1969, 3, 1), gu_holidays)
        for dt in [date(1970, 3, 2), date(1971, 3, 1), date(1977, 3, 7),
                   date(2014, 3, 3), date(2015, 3, 2), date(2016, 3, 7)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, gu_holidays)
            self.assertEqual(gu_holidays.get(dt), "Guam Discovery Day")

    def test_casimir_pulaski_day(self):
        il_holidays = holidays.US(state='IL')
        self.assertNotIn(date(1977, 3, 7), il_holidays)
        for dt in [date(1978, 3, 6), date(1982, 3, 1), date(1983, 3, 7),
                   date(2014, 3, 3), date(2015, 3, 2), date(2016, 3, 7)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, il_holidays)
            self.assertEqual(il_holidays.get(dt), "Casimir Pulaski Day")

    def test_texas_independence_day(self):
        tx_holidays = holidays.US(state='TX')
        self.assertNotIn(date(1873, 3, 2), tx_holidays)
        for year in range(1874, 2050):
            self.assertNotIn(date(year, 3, 2), self.holidays)
            self.assertIn(date(year, 3, 2), tx_holidays)

    def test_town_meeting_day(self):
        vt_holidays = holidays.US(state='VT')
        self.assertNotIn(date(1799, 3, 5), vt_holidays)
        for dt in [date(1800, 3, 4), date(1803, 3, 1), date(1804, 3, 6),
                   date(2011, 3, 1), date(2015, 3, 3), date(2017, 3, 7)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, vt_holidays)

    def test_evacuation_day(self):
        ma_holidays = holidays.US(state='MA')
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
        pr_holidays = holidays.US(state='PR')
        for year in range(2010, 2021):
            self.assertNotIn(date(year, 3, 22), self.holidays)
            self.assertIn(date(year, 3, 22), pr_holidays)
        self.assertNotIn(date(2014, 3, 21), pr_holidays)
        self.assertNotIn(date(2014, 3, 23), pr_holidays)
        self.assertIn(date(2015, 3, 23), pr_holidays)

    def test_prince_jonah_kuhio_kalanianaole_day(self):
        hi_holidays = holidays.US(state='HI')
        self.assertNotIn(date(1948, 3, 26), hi_holidays)
        for year in range(1949, 2050):
            self.assertNotIn(date(year, 3, 26), self.holidays)
            self.assertIn(date(year, 3, 26), hi_holidays)
        for dt in [date(1949, 3, 25), date(2016, 3, 25), date(2017, 3, 27)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, hi_holidays)
            self.assertEqual(hi_holidays.get(dt),
                             "Prince Jonah Kuhio Kalanianaole Day (Observed)")
        hi_holidays.observed = False
        for dt in [date(1949, 3, 25), date(2016, 3, 25), date(2017, 3, 27)]:
            self.assertNotIn(dt, hi_holidays)

    def test_stewards_day(self):
        ak_holidays = holidays.US(state='AK')
        self.assertNotIn(date(1917, 3, 30), ak_holidays)
        for dt in [date(1918, 3, 30), date(1954, 3, 30), date(1955, 3, 28),
                   date(2002, 3, 25), date(2014, 3, 31), date(2018, 3, 26)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, ak_holidays)

    def test_cesar_chavez_day(self):
        ca_holidays = holidays.US(state='CA')
        tx_holidays = holidays.US(state='TX')
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
        vi_holidays = holidays.US(state='VI')
        for year in range(2010, 2021):
            self.assertNotIn(date(year, 3, 31), self.holidays)
            self.assertIn(date(year, 3, 31), vi_holidays)

    def test_emancipation_day(self):
        dc_holidays = holidays.US(state='DC')
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
        me_holidays = holidays.US(state='ME')
        ma_holidays = holidays.US(state='MA')
        self.assertNotIn(date(1983, 4, 19), me_holidays)
        self.assertNotIn(date(1983, 4, 19), ma_holidays)
        for year in range(1894, 1969):
            self.assertNotIn(date(year, 4, 19), self.holidays)
            self.assertIn(date(year, 4, 19), me_holidays)
            self.assertIn(date(year, 4, 19), ma_holidays)
        for dt in [date(1969, 4, 21), date(1974, 4, 15), date(1975, 4, 21),
                   date(2015, 4, 20), date(2016, 4, 18), date(2019, 4, 15)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, me_holidays)
            self.assertIn(dt, ma_holidays)

    def test_holy_thursday(self):
        vi_holidays = holidays.US(state='VI')
        for dt in [date(2010, 4, 1), date(2011, 4, 21), date(2013, 3, 28),
                   date(2014, 4, 17), date(2015, 4, 2), date(2016, 3, 24)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, vi_holidays)

    def test_good_friday(self):
        ct_holidays = holidays.US(state='CT')
        de_holidays = holidays.US(state='DE')
        gu_holidays = holidays.US(state='GU')
        in_holidays = holidays.US(state='IN')
        ky_holidays = holidays.US(state='IN')
        la_holidays = holidays.US(state='LA')
        nj_holidays = holidays.US(state='NJ')
        nc_holidays = holidays.US(state='NC')
        tn_holidays = holidays.US(state='TN')
        tx_holidays = holidays.US(state='TX')
        vi_holidays = holidays.US(state='VI')
        for dt in [date(1900, 4, 13), date(1901, 4, 5), date(1902, 3, 28),
                   date(1999, 4, 2), date(2000, 4, 21), date(2010, 4, 2),
                   date(2018, 3, 30), date(2019, 4, 19), date(2020, 4, 10)]:
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
        vi_holidays = holidays.US(state='VI')
        for dt in [date(1900, 4, 16), date(1901, 4, 8), date(1902, 3, 31),
                   date(1999, 4, 5), date(2010, 4, 5),
                   date(2018, 4, 2), date(2019, 4, 22), date(2020, 4, 13)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, vi_holidays)

    def test_confederate_memorial_day(self):
        al_holidays = holidays.US(state='AL')
        ga_holidays = holidays.US(state='GA')
        ms_holidays = holidays.US(state='MS')
        sc_holidays = holidays.US(state='SC')
        tx_holidays = holidays.US(state='TX')
        self.assertNotIn(date(1865, 4, 24), self.holidays)
        self.assertNotIn(date(1865, 4, 24), al_holidays)
        for dt in [date(1866, 4, 23), date(1878, 4, 22), date(1884, 4, 28),
                   date(2014, 4, 28), date(2015, 4, 27), date(2019, 4, 22)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, al_holidays)
            self.assertIn(dt, ga_holidays)
            self.assertIn(dt, ms_holidays)
            self.assertIn(dt, sc_holidays)
        self.assertNotIn(date(1930, 1, 19), tx_holidays)
        self.assertNotIn(date(1931, 1, 19), self.holidays)
        self.assertIn(date(1931, 1, 19), tx_holidays)

    def test_san_jacinto_day(self):
        tx_holidays = holidays.US(state='TX')
        self.assertNotIn(date(1874, 4, 21), tx_holidays)
        for year in (1875, 2050):
            self.assertNotIn(date(year, 4, 21), self.holidays)
            self.assertIn(date(year, 4, 21), tx_holidays)

    def test_arbor_day(self):
        ne_holidays = holidays.US(state='NE')
        for dt in [date(1875, 4, 22), date(1988, 4, 22), date(1989, 4, 28),
                   date(2009, 4, 24), date(2010, 4, 30), date(2014, 4, 25)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, ne_holidays)

    def test_primary_election_day(self):
        in_holidays = holidays.US(state='IN')
        self.assertNotIn(date(2004, 5, 4), in_holidays)
        for dt in [date(2006, 5, 2), date(2008, 5, 6), date(2010, 5, 4),
                   date(2012, 5, 8), date(2014, 5, 6), date(2015, 5, 5),
                   date(2016, 5, 3)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, in_holidays)

    def test_truman_day(self):
        mo_holidays = holidays.US(state='MO', observed=False)
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
        for dt in [date(1969, 5, 30), date(1970, 5, 30), date(1971, 5, 31),
                   date(1997, 5, 26), date(1999, 5, 31), date(2000, 5, 29),
                   date(2012, 5, 28), date(2013, 5, 27), date(2014, 5, 26),
                   date(2015, 5, 25), date(2016, 5, 30), date(2020, 5, 25)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_jefferson_davis_birthday(self):
        al_holidays = holidays.US(state='AL')
        self.assertNotIn(date(1889, 6, 3), self.holidays)
        self.assertNotIn(date(1889, 6, 3), al_holidays)
        for dt in [date(1890, 6, 2), date(1891, 6, 1), date(1897, 6, 7),
                   date(2014, 6, 2), date(2015, 6, 1), date(2016, 6, 6)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, al_holidays)

    def test_kamehameha_day(self):
        hi_holidays = holidays.US(state='HI')
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
        tx_holidays = holidays.US(state='TX')
        self.assertNotIn(date(1979, 6, 19), tx_holidays)
        for year in (1980, 2050):
            self.assertNotIn(date(year, 6, 19), self.holidays)
            self.assertIn(date(year, 6, 19), tx_holidays)

    def test_west_virginia_day(self):
        wv_holidays = holidays.US(state='WV')
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
        vi_holidays = holidays.US(state='VI')
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
        gu_holidays = holidays.US(state='GU')
        self.assertNotIn(date(1944, 7, 21), gu_holidays)
        for year in range(1945, 2100):
            self.assertNotIn(date(year, 7, 21), self.holidays)
            self.assertIn(date(year, 7, 21), gu_holidays)

    def test_pioneer_day(self):
        ut_holidays = holidays.US(state='UT')
        self.assertNotIn(date(1848, 7, 24), ut_holidays)
        for year in (1849, 2050):
            self.assertNotIn(date(year, 7, 24), self.holidays)
            self.assertIn(date(year, 7, 24), ut_holidays)
        self.assertIn('2010-07-23', ut_holidays)
        self.assertIn('2011-07-25', ut_holidays)
        ut_holidays.observed = False
        self.assertNotIn('2010-07-23', ut_holidays)
        self.assertNotIn('2011-07-25', ut_holidays)

    def test_constitution_day(self):
        pr_holidays = holidays.US(state='PR')
        for year in range(2010, 2021):
            self.assertNotIn(date(year, 7, 25), self.holidays)
            self.assertIn(date(year, 7, 25), pr_holidays)
        self.assertNotIn(date(2015, 7, 24), pr_holidays)
        self.assertNotIn(date(2015, 7, 26), pr_holidays)
        self.assertIn(date(2021, 7, 26), pr_holidays)

    def test_victory_day(self):
        ri_holidays = holidays.US(state='RI')
        self.assertNotIn(date(1947, 8, 11), ri_holidays)
        for dt in [date(1948, 8, 9), date(1995, 8, 14), date(2005, 8, 8),
                   date(2015, 8, 10), date(2016, 8, 8), date(2017, 8, 14)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, ri_holidays)

    def test_statehood_day(self):
        hi_holidays = holidays.US(state='HI')
        self.assertNotIn(date(1958, 8, 15), hi_holidays)
        for dt in [date(1959, 8, 21), date(1969, 8, 15), date(1999, 8, 20),
                   date(2014, 8, 15), date(2015, 8, 21), date(2016, 8, 19)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, hi_holidays)

    def test_bennington_battle_day(self):
        vt_holidays = holidays.US(state='VT')
        self.assertNotIn(date(1777, 8, 16), vt_holidays)
        for year in range(1778, 2050):
            self.assertNotIn(date(year, 8, 16), self.holidays)
            self.assertIn(date(year, 8, 16), vt_holidays)
        vt_holidays.observed = False
        self.assertNotIn("Bennington Battle Day (Observed)",
                         vt_holidays.get_list(date(1997, 8, 15)))
        vt_holidays.observed = True
        self.assertIn("Bennington Battle Day (Observed)",
                      vt_holidays.get_list(date(1997, 8, 15)))
        self.assertNotIn("Bennington Battle Day (Observed)",
                         vt_holidays.get_list(date(1997, 8, 17)))
        self.assertIn("Bennington Battle Day (Observed)",
                      vt_holidays.get_list(date(1998, 8, 17)))
        self.assertNotIn("Bennington Battle Day (Observed)",
                         vt_holidays.get_list(date(1999, 8, 15)))
        self.assertNotIn("Bennington Battle Day (Observed)",
                         vt_holidays.get_list(date(1999, 8, 17)))

    def test_lyndon_baines_johnson_day(self):
        tx_holidays = holidays.US(state='TX')
        self.assertNotIn(date(1972, 8, 27), tx_holidays)
        for year in (1973, 2050):
            self.assertNotIn(date(year, 8, 27), self.holidays)
            self.assertIn(date(year, 8, 27), tx_holidays)

    def test_labor_day(self):
        for dt in [date(1997, 9, 1), date(1999, 9, 6), date(2000, 9, 4),
                   date(2012, 9, 3), date(2013, 9, 2), date(2014, 9, 1),
                   date(2015, 9, 7), date(2016, 9, 5), date(2020, 9, 7)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_columbus_day(self):
        ak_holidays = holidays.US(state='AK')
        de_holidays = holidays.US(state='DE')
        fl_holidays = holidays.US(state='FL')
        hi_holidays = holidays.US(state='HI')
        sd_holidays = holidays.US(state='SD')
        vi_holidays = holidays.US(state='VI')
        for dt in [date(1937, 10, 12), date(1969, 10, 12), date(1970, 10, 12),
                   date(1999, 10, 11), date(2000, 10, 9), date(2001, 10, 8),
                   date(2013, 10, 14), date(2018, 10, 8), date(2019, 10, 14)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt, ak_holidays)
            self.assertNotIn(dt, de_holidays)
            self.assertNotIn(dt, fl_holidays)
            self.assertNotIn(dt, hi_holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertEqual(sd_holidays.get(dt), "Native American Day")
            self.assertEqual(vi_holidays.get(dt),
                             "Columbus Day and Puerto Rico Friendship Day")
        self.assertNotIn(date(1936, 10, 12), self.holidays)

    def test_alaska_day(self):
        ak_holidays = holidays.US(state='AK', observed=False)
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
        nv_holidays = holidays.US(state='NV')
        self.assertNotIn(date(1932, 10, 31), nv_holidays)
        for dt in [date(1933, 10, 31), date(1999, 10, 31), date(2000, 10, 27),
                   date(2002, 10, 25), date(2014, 10, 31), date(2015, 10, 30)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, nv_holidays)
        self.assertIn("Nevada Day (Observed)",
                      nv_holidays.get_list(date(1998, 10, 30)))
        self.assertIn("Nevada Day (Observed)",
                      nv_holidays.get_list(date(1999, 11, 1)))
        nv_holidays.observed = False
        self.assertNotIn("Nevada Day (Observed)",
                         nv_holidays.get_list(date(1998, 10, 30)))
        self.assertNotIn("Nevada Day (Observed)",
                         nv_holidays.get_list(date(1999, 11, 1)))

    def test_liberty_day(self):
        vi_holidays = holidays.US(state='VI')
        for year in range(2010, 2021):
            self.assertNotIn(date(year, 11, 1), self.holidays)
            self.assertIn(date(year, 11, 1), vi_holidays)

    def test_election_day(self):
        de_holidays = holidays.US(state='DE')
        hi_holidays = holidays.US(state='HI')
        il_holidays = holidays.US(state='IL')
        in_holidays = holidays.US(state='IN')
        la_holidays = holidays.US(state='LA')
        mt_holidays = holidays.US(state='MT')
        nh_holidays = holidays.US(state='NH')
        nj_holidays = holidays.US(state='NJ')
        ny_holidays = holidays.US(state='NY')
        wv_holidays = holidays.US(state='WV')
        self.assertNotIn(date(2004, 11, 2), de_holidays)
        for dt in [date(2008, 11, 4), date(2010, 11, 2), date(2012, 11, 6),
                   date(2014, 11, 4), date(2016, 11, 8), date(2018, 11, 6)]:
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
        gu_holidays = holidays.US(state='GU')
        for year in range(1945, 2100):
            self.assertNotIn(date(year, 11, 2), self.holidays)
            self.assertIn(date(year, 11, 2), gu_holidays)

    def test_veterans_day(self):
        for dt in [date(1938, 11, 11), date(1939, 11, 11), date(1970, 11, 11),
                   date(1971, 10, 25), date(1977, 10, 24), date(1978, 11, 11),
                   date(2012, 11, 11), date(2013, 11, 11), date(2014, 11, 11),
                   date(2015, 11, 11), date(2016, 11, 11), date(2020, 11, 11)]:
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
        pr_holidays = holidays.US(state='PR')
        for year in range(2010, 2021):
            self.assertNotIn(date(year, 11, 19), self.holidays)
            self.assertIn(date(year, 11, 19), pr_holidays)
        self.assertNotIn(date(2016, 11, 18), pr_holidays)
        self.assertNotIn(date(2016, 11, 20), pr_holidays)
        self.assertIn(date(2017, 11, 20), pr_holidays)

    def test_thanksgiving_day(self):
        de_holidays = holidays.US(state='DE')
        fl_holidays = holidays.US(state='FL')
        in_holidays = holidays.US(state='IN')
        md_holidays = holidays.US(state='MD')
        nv_holidays = holidays.US(state='NV')
        nh_holidays = holidays.US(state='NH')
        nm_holidays = holidays.US(state='NM')
        nc_holidays = holidays.US(state='NC')
        ok_holidays = holidays.US(state='OK')
        tx_holidays = holidays.US(state='TX')
        wv_holidays = holidays.US(state='WV')
        for dt in [date(1997, 11, 27), date(1999, 11, 25), date(2000, 11, 23),
                   date(2012, 11, 22), date(2013, 11, 28), date(2014, 11, 27),
                   date(2015, 11, 26), date(2016, 11, 24), date(2020, 11, 26)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
            self.assertIn(dt + relativedelta(days=+1), de_holidays)
            self.assertEqual(de_holidays.get(dt + relativedelta(days=+1)),
                             "Day After Thanksgiving")
            self.assertEqual(nh_holidays.get(dt + relativedelta(days=+1)),
                             "Day After Thanksgiving")
            self.assertEqual(nc_holidays.get(dt + relativedelta(days=+1)),
                             "Day After Thanksgiving")
            self.assertEqual(ok_holidays.get(dt + relativedelta(days=+1)),
                             "Day After Thanksgiving")
            self.assertEqual(wv_holidays.get(dt + relativedelta(days=+1)),
                             "Day After Thanksgiving")
            self.assertIn(dt + relativedelta(days=+1), fl_holidays)
            self.assertEqual(fl_holidays.get(dt + relativedelta(days=+1)),
                             "Friday After Thanksgiving")
            self.assertIn(dt + relativedelta(days=+1), tx_holidays)
            self.assertEqual(tx_holidays.get(dt + relativedelta(days=+1)),
                             "Friday After Thanksgiving")
            self.assertEqual(nv_holidays.get(dt + relativedelta(days=+1)),
                             "Family Day")
            self.assertEqual(nm_holidays.get(dt + relativedelta(days=+1)),
                             "Presidents' Day")
            if dt.year >= 2008:
                self.assertEqual(md_holidays.get(dt + relativedelta(days=1)),
                                 "American Indian Heritage Day")
            if dt.year >= 2010:
                self.assertEqual(in_holidays.get(dt + relativedelta(days=1)),
                                 "Lincoln's Birthday")
            else:
                self.assertNotEqual(
                    in_holidays.get(dt + relativedelta(days=1)),
                    "Lincoln's Birthday")

    def test_robert_lee_birthday(self):
        ga_holidays = holidays.US(state='GA')
        self.assertNotIn(date(1985, 11, 25), ga_holidays)
        for dt in [date(2007, 11, 23), date(2008, 11, 28), date(2010, 11, 26),
                   date(2013, 11, 29), date(2014, 11, 28), date(2015, 11, 27),
                   date(2018, 11, 23), date(2019, 11, 29), date(2020, 11, 27)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, ga_holidays)

    def test_lady_of_camarin_day(self):
        gu_holidays = holidays.US(state='GU')
        for year in range(1945, 2100):
            self.assertNotIn(date(year, 12, 8), self.holidays)
            self.assertIn(date(year, 12, 8), gu_holidays)

    def test_christmas_eve(self):
        as_holidays = holidays.US(state='AS')
        ks_holidays = holidays.US(state='KS')
        mi_holidays = holidays.US(state='MI')
        nc_holidays = holidays.US(state='NC')
        tx_holidays = holidays.US(state='TX')
        wi_holidays = holidays.US(state='WI')
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
        self.assertIn("Christmas Eve (Observed)",
                      as_holidays.get_list(date(2017, 12, 22)))
        self.assertIn("Christmas Eve (Observed)",
                      ks_holidays.get_list(date(2017, 12, 22)))
        self.assertIn("Christmas Eve (Observed)",
                      mi_holidays.get_list(date(2017, 12, 22)))
        self.assertIn("Christmas Eve (Observed)",
                      nc_holidays.get_list(date(2017, 12, 22)))
        self.assertIn("Christmas Eve (Observed)",
                      tx_holidays.get_list(date(2017, 12, 22)))
        self.assertIn("Christmas Eve (Observed)",
                      wi_holidays.get_list(date(2017, 12, 22)))

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
        nc_holidays = holidays.US(state='NC', observed=False)
        tx_holidays = holidays.US(state='TX', observed=False)
        self.assertNotIn(date(2015, 12, 28), nc_holidays)
        self.assertNotIn(date(2016, 12, 27), nc_holidays)
        self.assertNotIn(date(2015, 12, 28), tx_holidays)
        self.assertNotIn(date(2016, 12, 27), tx_holidays)
        nc_holidays.observed = True
        self.assertIn("Day After Christmas (Observed)",
                      nc_holidays.get_list(date(2015, 12, 28)))
        self.assertIn("Day After Christmas (Observed)",
                      nc_holidays.get_list(date(2016, 12, 27)))
        tx_holidays.observed = True
        self.assertNotIn("Day After Christmas (Observed)",
                         tx_holidays.get_list(date(2015, 12, 28)))
        self.assertNotIn("Day After Christmas (Observed)",
                         tx_holidays.get_list(date(2016, 12, 27)))

    def test_new_years_eve(self):
        ky_holidays = holidays.US(state='KY')
        mi_holidays = holidays.US(state='MI')
        wi_holidays = holidays.US(state='WI')
        self.assertNotIn(date(2012, 12, 31), ky_holidays)
        self.assertNotIn(date(2012, 12, 31), mi_holidays)
        self.assertNotIn(date(2011, 12, 31), wi_holidays)
        self.assertIn(date(2012, 12, 31), wi_holidays)
        for dt in [date(2013, 12, 31), date(2016, 12, 30)]:
            self.assertNotIn(dt, self.holidays)
            self.assertIn(dt, ky_holidays)
            self.assertIn(dt, mi_holidays)
            self.assertIn(dt, wi_holidays)


class TestNZ(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.NZ(observed=True)

    def test_new_years(self):
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
        for year, day in enumerate([1, 1, 1, 1, 3,  # 2001-05
                                    3, 1, 1, 1, 1,  # 2006-10
                                    3, 3, 1, 1, 1,  # 2011-15
                                    1, 3, 1, 1, 1, 1],  # 2016-21
                                   2001):
            dt = date(year, 1, day)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt][:10], "New Year's")
        self.assertNotIn("1893-01-01", self.holidays)
        self.assertIn("1894-01-01", self.holidays)

    def test_day_after_new_years(self):
        for year in range(1900, 2100):
            dt = date(year, 1, 2)
            self.assertIn(dt, self.holidays)
        for year, day in enumerate([2, 2, 2, 2, 2,  # 2001-05
                                    2, 2, 2, 2, 4,  # 2006-10
                                    4, 2, 2, 2, 2,  # 2011-15
                                    4, 2, 2, 2, 2, 4],  # 2016-21
                                   2001):
            dt = date(year, 1, day)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt][:10], "Day after ")
        self.assertNotIn(date(2016, 1, 3), self.holidays)

    def test_waitangi_day(self):
        ntl_holidays = holidays.NZ(prov='Northland')
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
        for year, day in enumerate([6, 6, 6, 6, 6,  # 2001-05
                                    6, 6, 6, 6, 6,  # 2006-10
                                    6, 6, 6, 6, 6,  # 2011-15
                                    8, 6, 6, 6, 6, 8],  # 2016-21
                                   2001):
            dt = date(year, 2, day)
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt][:8], "Waitangi")
        self.assertNotIn(date(2005, 2, 7), self.holidays)
        self.assertNotIn(date(2010, 2, 8), self.holidays)
        self.assertNotIn(date(2011, 2, 7), self.holidays)

    def test_good_friday(self):
        for dt in [date(1900, 4, 13), date(1901, 4, 5), date(1902, 3, 28),
                   date(1999, 4, 2), date(2000, 4, 21), date(2010, 4, 2),
                   date(2018, 3, 30), date(2019, 4, 19), date(2020, 4, 10)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_easter_monday(self):
        for dt in [date(1900, 4, 16), date(1901, 4, 8), date(1902, 3, 31),
                   date(1999, 4, 5), date(2010, 4, 5),
                   date(2018, 4, 2), date(2019, 4, 22), date(2020, 4, 13)]:
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
        for year, day in enumerate([25, 25, 25, 25, 25,  # 2001-05
                                    25, 25, 25, 25, 25,  # 2006-10
                                    25, 25, 25, 25, 27,  # 2011-15
                                    25, 25, 25, 25, 27, 26],  # 2016-21
                                   2001):
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
        for year, day in enumerate([4, 3, 2, 7, 6,  # 2001-05
                                    5, 4, 2, 1, 7,  # 2006-10
                                    6, 4, 3, 2, 1,  # 2011-15
                                    6, 5, 4, 3, 1, 7],  # 2016-21
                                   2001):
            dt = date(year, 6, day)
            self.assertIn(dt, self.holidays, dt)
            self.assertEqual(self.holidays[dt], "Queen's Birthday")

    def test_labour_day(self):
        for year, day in enumerate([22, 28, 27, 25, 24,  # 2001-05
                                    23, 22, 27, 26, 25,  # 2006-10
                                    24, 22, 28, 27, 26,  # 2011-15
                                    24, 23, 22, 28, 26, 25],  # 2016-21
                                   2001):
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
        self.assertNotEqual(self.holidays[date(2011, 12, 26)],
                            "Christmas Day (Observed)")
        self.holidays.observed = True
        self.assertEqual(self.holidays[date(2011, 12, 27)],
                         "Christmas Day (Observed)")
        for year, day in enumerate([25, 25, 25, 27, 27,  # 2001-05
                                    25, 25, 25, 25, 27,  # 2006-10
                                    27, 25, 25, 25, 25,  # 2011-15
                                    27, 25, 25, 25, 25, 25],  # 2016-21
                                   2001):
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
        for year, day in enumerate([26, 26, 26, 28, 26,  # 2001-05
                                    26, 26, 26, 28, 28,  # 2006-10
                                    26, 26, 26, 26, 28,  # 2011-15
                                    26, 26, 26, 26, 28, 28],  # 2016-21
                                   2001):
            dt = date(year, 12, day)
            self.assertIn(dt, self.holidays, dt)
            self.assertEqual(self.holidays[dt][:6], "Boxing")

    def test_auckland_anniversary_day(self):
        auk_holidays = holidays.NZ(prov='Auckland')
        for year, day in enumerate([29, 28, 27, 26, 31,  # 2001-05
                                    30, 29, 28, 26, 1,  # 2006-10
                                    31, 30, 28, 27, 26,  # 2011-15
                                    1, 30, 29, 28, 27, 1],  # 2016-21
                                   2001):
            dt = date(year, 2 if day < 9 else 1, day)
            self.assertIn(dt, auk_holidays, dt)
            self.assertEqual(auk_holidays[dt],
                             "Auckland Anniversary Day")

    def test_taranaki_anniversary_day(self):
        tki_holidays = holidays.NZ(prov='Taranaki')
        for year, day in enumerate([12, 11, 10, 8, 14,  # 2001-05
                                    13, 12, 10, 9, 8,  # 2006-10
                                    14, 12, 11, 10, 9,  # 2011-15
                                    14, 13, 12, 11, 9, 8],  # 2016-21
                                   2001):
            dt = date(year, 3, day)
            self.assertIn(dt, tki_holidays, dt)
            self.assertEqual(tki_holidays[dt],
                             "Taranaki Anniversary Day")

    def test_hawkes_bay_anniversary_day(self):
        hkb_holidays = holidays.NZ(prov="Hawke's Bay")
        for year, day in enumerate([19, 25, 24, 22, 21,  # 2001-05
                                    20, 19, 24, 23, 22,  # 2006-10
                                    21, 19, 25, 24, 23,  # 2011-15
                                    21, 20, 19, 25, 23, 22],  # 2016-21
                                   2001):
            dt = date(year, 10, day)
            self.assertIn(dt, hkb_holidays, dt)
            self.assertEqual(hkb_holidays[dt],
                             "Hawke's Bay Anniversary Day")

    def test_wellington_anniversary_day(self):
        wgn_holidays = holidays.NZ(prov='Wellington')
        for year, day in enumerate([22, 21, 20, 19, 24,  # 2001-05
                                    23, 22, 21, 19, 25,  # 2006-10
                                    24, 23, 21, 20, 19,  # 2011-15
                                    25, 23, 22, 21, 20, 25],  # 2016-21
                                   2001):
            dt = date(year, 1, day)
            self.assertIn(dt, wgn_holidays, dt)
            self.assertEqual(wgn_holidays[dt],
                             "Wellington Anniversary Day", dt)

    def test_marlborough_anniversary_day(self):
        mbh_holidays = holidays.NZ(prov='Marlborough')
        for year, day in enumerate([29, 4, 3, 1, 31,  # 2001-05
                                    30, 29, 3, 2, 1,  # 2006-10
                                    31, 29, 4, 3, 2,  # 2011-15
                                    31, 30, 29, 4, 2, 1],  # 2016-21
                                   2001):
            dt = date(year, 11 if day < 9 else 10, day)
            self.assertIn(dt, mbh_holidays, dt)
            self.assertEqual(mbh_holidays[dt],
                             "Marlborough Anniversary Day", dt)

    def test_nelson_anniversary_day(self):
        nsn_holidays = holidays.NZ(prov='Nelson')
        for year, day in enumerate([29, 4, 3, 2, 31,  # 2001-05
                                    30, 29, 4, 2, 1,  # 2006-10
                                    31, 30, 4, 3, 2,  # 2011-15
                                    1, 30, 29, 4, 3, 1],  # 2016-21
                                   2001):
            dt = date(year, 2 if day < 9 else 1, day)
            self.assertIn(dt, nsn_holidays, dt)
            self.assertEqual(nsn_holidays[dt],
                             "Nelson Anniversary Day", dt)

    def test_canterbury_anniversary_day(self):
        can_holidays = holidays.NZ(prov='Canterbury')
        for year, day in enumerate([16, 15, 14, 12, 11,  # 2001-05
                                    17, 16, 14, 13, 12,  # 2006-10
                                    11, 16, 15, 14, 13,  # 2011-15
                                    11, 17, 16, 15, 13, 12],  # 2016-21
                                   2001):
            dt = date(year, 11, day)
            self.assertIn(dt, can_holidays, dt)
            self.assertEqual(can_holidays[dt],
                             "Canterbury Anniversary Day", dt)

    def test_south_canterbury_anniversary_day(self):
        stc_holidays = holidays.NZ(prov='South Canterbury')
        for year, day in enumerate([24, 23, 22, 27, 26,  # 2001-05
                                    25, 24, 22, 28, 27,  # 2006-10
                                    26, 24, 23, 22, 28,  # 2011-15
                                    26, 25, 24, 23, 28, 27],  # 2016-21
                                   2001):
            dt = date(year, 9, day)
            self.assertIn(dt, stc_holidays, dt)
            self.assertEqual(stc_holidays[dt],
                             "South Canterbury Anniversary Day", dt)

    def test_westland_anniversary_day(self):
        wtc_holidays = holidays.NZ(prov='Westland')
        for year, day in enumerate([3, 2, 1, 29, 5,  # 2001-05
                                    4, 3, 1, 30, 29,  # 2006-10
                                    28, 3, 2, 1, 30,  # 2011-15
                                    28, 4, 3, 2, 30, 29],  # 2016-21
                                   2001):
            dt = date(year, 12 if day < 9 else 11, day)
            self.assertIn(dt, wtc_holidays, dt)
            self.assertEqual(wtc_holidays[dt],
                             "Westland Anniversary Day", dt)

    def test_otago_anniversary_day(self):
        ota_holidays = holidays.NZ(prov='Otago')
        for year, day in enumerate([26, 25, 24, 22, 21,  # 2001-05
                                    20, 26, 25, 23, 22,  # 2006-10
                                    21, 26, 25, 24, 23,  # 2011-15
                                    21, 20, 26, 25, 23, 22],  # 2016-21
                                   2001):
            dt = date(year, 3, day)
            self.assertIn(dt, ota_holidays, dt)
            self.assertEqual(ota_holidays[dt],
                             "Otago Anniversary Day", dt)

    def test_southland_anniversary_day(self):
        stl_holidays = holidays.NZ(prov='Southland')
        for year, day in enumerate([15, 14, 20, 19, 17,  # 2001-05
                                    16, 15, 14, 19, 18, 17],  # 2006-11
                                   2001):
            dt = date(year, 1, day)
            self.assertIn(dt, stl_holidays, dt)
            self.assertEqual(stl_holidays[dt],
                             "Southland Anniversary Day", dt)
            for year, (month, day) in enumerate([(4, 10), (4, 2), (4, 22),
                                                 (4, 7), (3, 29), (4, 18),
                                                 (4, 3), (4, 23), (4, 14),
                                                 (4, 6)], 2012):
                dt = date(year, month, day)
                self.assertIn(dt, stl_holidays, dt)
                self.assertEqual(stl_holidays[dt],
                                 "Southland Anniversary Day", dt)

    def test_chatham_islands_anniversary_day(self):
        cit_holidays = holidays.NZ(prov='Chatham Islands')
        for year, day in enumerate([3, 2, 1, 29, 28,  # 2001-05
                                    27, 3, 1, 30, 29,  # 2006-10
                                    28, 3, 2, 1, 30,  # 2011-15
                                    28, 27, 3, 2, 30, 29],  # 2016-21
                                   2001):
            dt = date(year, 12 if day < 9 else 11, day)
            self.assertIn(dt, cit_holidays, dt)
            self.assertEqual(cit_holidays[dt],
                             "Chatham Islands Anniversary Day", dt)

    def test_all_holidays_present(self):
        nz_1969 = sum(holidays.NZ(years=[1969], prov=p)
                      for p in holidays.NZ.PROVINCES)
        holidays_in_1969 = sum((nz_1969.get_list(key) for key in nz_1969), [])
        nz_2015 = sum(holidays.NZ(years=[2015], prov=p)
                      for p in holidays.NZ.PROVINCES)
        holidays_in_2015 = sum((nz_2015.get_list(key) for key in nz_2015), [])
        nz_1974 = sum(holidays.NZ(years=[1974], prov=p)
                      for p in holidays.NZ.PROVINCES)
        holidays_in_1974 = sum((nz_1974.get_list(key) for key in nz_1974), [])
        all_holidays = ["New Year's Day",
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
                        "Boxing Day"]
        for holiday in all_holidays:
            self.assertIn(holiday, holidays_in_1969, holiday)
            self.assertIn(holiday, holidays_in_2015, holiday)
        all_holidays.remove("Waitangi Day")
        all_holidays.insert(2, "New Zealand Day")
        for holiday in all_holidays:
            self.assertIn(holiday, holidays_in_1974, holiday)
        self.assertNotIn("Waitangi Day", holidays_in_1974)


class TestAU(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.AU(observed=True)
        self.state_hols = {state: holidays.AU(observed=True, prov=state)
                           for state in holidays.AU.PROVINCES}

    def test_new_years(self):
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
        for year, day in enumerate([3, 2, 1, 1, 1,  # 2011-15
                                    1, 2, 1, 1, 1, 1],  # 2016-21
                                   2011):
            dt = date(year, 1, day)
            for state, hols in self.state_hols.items():
                self.assertIn(dt, hols, (state, dt))
                self.assertEqual(hols[dt][:10], "New Year's", state)

    def test_australia_day(self):
        for year, day in enumerate([26, 26, 28, 27, 26,  # 2011-15
                                    26, 26, 26, 28, 27, 26],  # 2016-21
                                   2011):
            jan26 = date(year, 1, 26)
            dt = date(year, 1, day)
            self.assertIn(jan26, self.holidays, dt)
            self.assertEqual(self.holidays[jan26], "Australia Day")
            self.assertIn(dt, self.holidays, dt)
            self.assertEqual(self.holidays[dt][:10], "Australia ")
            for state in holidays.AU.PROVINCES:
                self.assertIn(jan26, self.state_hols[state], (state, dt))
                self.assertEqual(self.state_hols[state][jan26],
                                 "Australia Day")
                self.assertIn(dt, self.state_hols[state], (state, dt))
                self.assertEqual(self.state_hols[state][dt][:10], "Australia ")
        self.assertNotIn(date(2016, 1, 27), self.holidays)
        self.assertNotIn(date(1887, 1, 26), self.holidays)
        self.assertNotIn(date(1934, 1, 26), self.state_hols['SA'])
        for dt in [date(1889, 1, 26), date(1936, 1, 26), date(1945, 1, 26)]:
            self.assertIn(dt, self.state_hols['NSW'], dt)
            self.assertEqual(self.state_hols['NSW'][dt], "Anniversary Day")

    def test_good_friday(self):
        for dt in [date(1900, 4, 13), date(1901, 4, 5), date(1902, 3, 28),
                   date(1999, 4, 2), date(2000, 4, 21), date(2010, 4, 2),
                   date(2018, 3, 30), date(2019, 4, 19), date(2020, 4, 10)]:
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Good Friday")

    def test_easter_saturday(self):
        for dt in [date(1900, 4, 14), date(1901, 4, 6), date(1902, 3, 29),
                   date(1999, 4, 3), date(2000, 4, 22), date(2010, 4, 3),
                   date(2018, 3, 31), date(2019, 4, 20), date(2020, 4, 11)]:
            for state in ['ACT', 'NSW', 'NT', 'QLD', 'SA', 'VIC']:
                self.assertIn(dt, self.state_hols[state], (state, dt))
                self.assertEqual(self.state_hols[state][dt], "Easter Saturday")
            for state in ['TAS', 'WA']:
                self.assertNotIn(dt, self.state_hols[state], (state, dt))

    def test_easter_sunday(self):
        for dt in [date(1900, 4, 15), date(1901, 4, 7), date(1902, 3, 30),
                   date(1999, 4, 4), date(2010, 4, 4),
                   date(2018, 4, 1), date(2019, 4, 21), date(2020, 4, 12)]:
            self.assertIn(dt, self.state_hols['NSW'], dt)
            self.assertEqual(self.state_hols['NSW'][dt], "Easter Sunday")
            for state in ['ACT', 'NT', 'QLD', 'SA', 'VIC', 'TAS', 'WA']:
                self.assertNotIn(dt, self.state_hols[state], (state, dt))

    def test_easter_monday(self):
        for dt in [date(1900, 4, 16), date(1901, 4, 8), date(1902, 3, 31),
                   date(1999, 4, 5), date(2010, 4, 5),
                   date(2018, 4, 2), date(2019, 4, 22), date(2020, 4, 13)]:
            self.assertIn(dt, self.holidays)
            self.assertEqual(self.holidays[dt], "Easter Monday")
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_labour_day(self):
        for year, day in enumerate([7, 5, 4, 3, 2, 7, 6, ], 2011):
            dt = date(year, 3, day)
            self.assertIn(dt, self.state_hols['WA'], dt)
            self.assertEqual(self.state_hols['WA'][dt], "Labour Day")
        for year, day in enumerate([10, 9, 14], 2014):
            dt = date(year, 3, day)
            self.assertNotIn(dt, self.holidays, dt)
            self.assertIn(dt, self.state_hols['VIC'], dt)
            self.assertEqual(self.state_hols['VIC'][dt], "Labour Day")

    def test_anzac_day(self):
        for year in range(1900, 1921):
            dt = date(year, 4, 25)
            self.assertNotIn(dt, self.holidays)
        for year in range(1921, 2100):
            dt = date(year, 4, 25)
            self.assertIn(dt, self.holidays)
        for dt in [date(2015, 4, 27), date(2020, 4, 27)]:
            self.assertNotIn(dt, self.holidays, dt)
            for state in ['NT', 'WA']:
                self.assertIn(dt, self.state_hols[state], (state, dt))
                self.assertEqual(self.state_hols[state][dt][:5], "Anzac")
            for state in ['ACT', 'QLD', 'SA', 'NSW', 'TAS', 'VIC']:
                self.assertNotIn(dt, self.state_hols[state], (state, dt))
        dt = date(2021, 4, 26)
        for state in ['ACT', 'NT', 'QLD', 'SA', 'WA']:
            self.assertIn(dt, self.state_hols[state], (state, dt))
            self.assertEqual(self.state_hols[state][dt][:5], "Anzac")
        for state in ['NSW', 'TAS', 'VIC']:
            self.assertNotIn(dt, self.state_hols[state], (state, dt))

    def test_western_australia_day(self):
        for year, day in enumerate([4, 3, 2], 2012):
            dt = date(year, 6, day)
            self.assertIn(dt, self.state_hols['WA'], dt)
            self.assertEqual(self.state_hols['WA'][dt], "Foundation Day")
        for year, day in enumerate([1, 6, 5], 2015):
            dt = date(year, 6, day)
            self.assertIn(dt, self.state_hols['WA'], dt)
            self.assertEqual(self.state_hols['WA'][dt],
                             "Western Australia Day")

    def test_adelaide_cup(self):
        for dt in [date(2015, 3, 9), date(2016, 3, 14), date(2017, 3, 13)]:
            self.assertIn(dt, self.state_hols['SA'], dt)
            self.assertEqual(self.state_hols['SA'][dt], "Adelaide Cup")

    def test_queens_birthday(self):
        # Western Australia
        for dt in [date(2012, 10, 1), date(2013, 9, 30), date(2014, 9, 29),
                   date(2015, 9, 28), date(2016, 9, 26), date(2017, 9, 25)]:
            self.assertIn(dt, self.state_hols['WA'], dt)
            self.assertEqual(self.state_hols['WA'][dt], "Queen's Birthday")
        # Other states except Queensland
        other_states = [
            date(2010, 6, 14), date(2011, 6, 13), date(2012, 6, 11),
            date(2013, 6, 10), date(2014, 6, 9), date(2015, 6, 8),
            date(2016, 6, 13), date(2017, 6, 12), date(2018, 6, 11)]
        for dt in other_states:
            self.assertIn(dt, self.state_hols['NSW'], dt)
            self.assertIn(dt, self.state_hols['VIC'], dt)
            self.assertIn(dt, self.state_hols['ACT'], dt)
        # Queensland
        qld_dates = other_states[:-3]
        qld_dates.remove(date(2012, 6, 11))
        qld_dates.extend([date(2012, 10, 1), date(2016, 10, 3),
                          date(2017, 10, 2), date(2018, 10, 1)])
        for dt in qld_dates:
            self.assertIn(dt, self.state_hols['QLD'], dt)
            self.assertEqual(self.state_hols['QLD'][dt], "Queen's Birthday")
        self.assertIn(date(2012, 6, 11), self.state_hols['QLD'])

    def test_picnic_day(self):
        for dt in [date(2015, 8, 3), date(2016, 8, 1)]:
            self.assertIn(dt, self.state_hols['NT'], dt)
            self.assertEqual(self.state_hols['NT'][dt], "Picnic Day")

    def test_family_and_community_day(self):
        for dt in [date(2010, 9, 26), date(2011, 10, 10), date(2012, 10, 8),
                   date(2013, 9, 30), date(2014, 9, 29), date(2015, 9, 28),
                   date(2016, 9, 26)]:
            self.assertIn(dt, self.state_hols['ACT'], dt)
            self.assertEqual(self.state_hols['ACT'][dt],
                             "Family & Community Day")

    def test_melbourne_cup(self):
        for dt in [date(2014, 11, 4), date(2015, 11, 3), date(2016, 11, 1)]:
            self.assertIn(dt, self.state_hols['VIC'], dt)
            self.assertEqual(self.state_hols['VIC'][dt], "Melbourne Cup")

    def test_royal_queensland_show(self):
        for year, day in enumerate([15, 14, 12, 11, 10, 16], 2018):
            dt = date(year, 8, day)
            self.assertIn(dt, self.state_hols['QLD'], dt)
            self.assertEqual(self.state_hols['QLD'][dt],
                             "The Royal Queensland Show")

    def test_christmas_day(self):
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
        self.assertNotIn(date(2010, 12, 24), self.holidays)
        self.assertNotEqual(self.holidays[date(2011, 12, 26)],
                            "Christmas Day (Observed)")
        self.holidays.observed = True
        self.assertEqual(self.holidays[date(2011, 12, 27)],
                         "Christmas Day (Observed)")
        for year, day in enumerate([25, 25, 25, 27, 27,  # 2001-05
                                    25, 25, 25, 25, 27,  # 2006-10
                                    27, 25, 25, 25, 25,  # 2011-15
                                    27, 25, 25, 25, 25, 25],  # 2016-21
                                   2001):
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
        for year, day in enumerate([26, 26, 26, 28, 26,  # 2001-05
                                    26, 26, 26, 28, 28,  # 2006-10
                                    26, 26, 26, 26, 28,  # 2011-15
                                    26, 26, 26, 26, 28, 28],  # 2016-21
                                   2001):
            dt = date(year, 12, day)
            self.assertIn(dt, self.holidays, dt)
            self.assertEqual(self.holidays[dt][:6], "Boxing")

    def test_all_holidays_present(self):
        au_2015 = sum(holidays.AU(years=[2015], prov=p)
                      for p in holidays.AU.PROVINCES)
        holidays_in_2015 = sum((au_2015.get_list(key) for key in au_2015), [])
        all_holidays = ["New Year's Day",
                        "Australia Day",
                        "Adelaide Cup",
                        "Canberra Day",
                        "Good Friday",
                        "Easter Saturday",
                        "Easter Sunday",
                        "Easter Monday",
                        "Anzac Day",
                        "Queen's Birthday",
                        "Western Australia Day",
                        "Family & Community Day",
                        "Labour Day",
                        "Eight Hours Day",
                        "May Day",
                        "Picnic Day",
                        "Melbourne Cup",
                        "Christmas Day",
                        "Proclamation Day",
                        "Boxing Day"]
        for holiday in all_holidays:
            self.assertIn(holiday, holidays_in_2015, holiday)


class TestDE(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.DE()
        self.prov_hols = {prov: holidays.DE(prov=prov)
                          for prov in holidays.DE.PROVINCES}

    def test_no_data_before_1990(self):
        de_1989 = sum(holidays.DE(years=[1989], prov=p)
                      for p in holidays.DE.PROVINCES)
        self.assertEqual(len(de_1989), 0)

    def test_all_holidays_present(self):
        de_2015 = sum(holidays.DE(years=[2015], prov=p)
                      for p in holidays.DE.PROVINCES)
        in_2015 = sum((de_2015.get_list(key) for key in de_2015), [])
        all_de = ["Neujahr",
                  "Heilige Drei Könige",
                  "Karfreitag",
                  "Ostersonntag",
                  "Ostermontag",
                  "Erster Mai",
                  "Christi Himmelfahrt",
                  "Pfingstsonntag",
                  "Pfingstmontag",
                  "Fronleichnam",
                  "Mariä Himmelfahrt",
                  "Tag der Deutschen Einheit",
                  "Reformationstag",
                  "Allerheiligen",
                  "Buß- und Bettag",
                  "Erster Weihnachtstag",
                  "Zweiter Weihnachtstag"]

        for holiday in all_de:
            self.assertIn(holiday, in_2015, "missing: {}".format(holiday))
        for holiday in in_2015:
            self.assertIn(holiday, all_de, "extra: {}".format(holiday))

    def test_fixed_holidays(self):
        fixed_days_whole_country = (
            (1, 1),  # Neujahr
            (5, 1),  # Maifeiertag
            (10, 3),  # Tag der Deutschen Einheit
            (12, 25),  # Erster Weihnachtstag
            (12, 26),  # Zweiter Weihnachtstag
        )

        for y, (m, d) in product(range(1991, 2050), fixed_days_whole_country):
            self.assertIn(date(y, m, d), self.holidays)

    def test_heilige_drei_koenige(self):
        provinces_that_have = {'BW', 'BY', 'ST'}
        provinces_that_dont = set(holidays.DE.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1991, 2050)):
            self.assertIn(date(year, 1, 6), self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1991, 2050)):
            self.assertNotIn(date(year, 1, 6), self.prov_hols[province])

    def test_karfreitag(self):
        known_good = [(2014, 4, 18), (2015, 4, 3), (2016, 3, 25),
                      (2017, 4, 14), (2018, 3, 30), (2019, 4, 19),
                      (2020, 4, 10), (2021, 4, 2), (2022, 4, 15),
                      (2023, 4, 7), (2024, 3, 29)]

        for province, (y, m, d) in product(holidays.DE.PROVINCES, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])

    def test_ostersonntag(self):
        known_good = [(2014, 4, 20), (2015, 4, 5), (2016, 3, 27),
                      (2017, 4, 16), (2018, 4, 1), (2019, 4, 21),
                      (2020, 4, 12), (2021, 4, 4), (2022, 4, 17),
                      (2023, 4, 9), (2024, 3, 31)]

        for province, (y, m, d) in product(holidays.DE.PROVINCES, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])

    def test_ostermontag(self):
        known_good = [(2014, 4, 21), (2015, 4, 6), (2016, 3, 28),
                      (2017, 4, 17), (2018, 4, 2), (2019, 4, 22),
                      (2020, 4, 13), (2021, 4, 5), (2022, 4, 18),
                      (2023, 4, 10), (2024, 4, 1)]

        for province, (y, m, d) in product(holidays.DE.PROVINCES, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])

    def test_christi_himmelfahrt(self):
        known_good = [(2014, 5, 29), (2015, 5, 14), (2016, 5, 5),
                      (2017, 5, 25), (2018, 5, 10), (2019, 5, 30),
                      (2020, 5, 21), (2021, 5, 13), (2022, 5, 26),
                      (2023, 5, 18), (2024, 5, 9)]

        for province, (y, m, d) in product(holidays.DE.PROVINCES, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])

    def test_pfingstsonntag(self):
        known_good = [(2014, 6, 8), (2015, 5, 24), (2016, 5, 15),
                      (2017, 6, 4), (2018, 5, 20), (2019, 6, 9),
                      (2020, 5, 31), (2021, 5, 23), (2022, 6, 5),
                      (2023, 5, 28), (2024, 5, 19)]

        for province, (y, m, d) in product(holidays.DE.PROVINCES, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])

    def test_pfingstmontag(self):
        known_good = [(2014, 6, 9), (2015, 5, 25), (2016, 5, 16),
                      (2017, 6, 5), (2018, 5, 21), (2019, 6, 10),
                      (2020, 6, 1), (2021, 5, 24), (2022, 6, 6),
                      (2023, 5, 29), (2024, 5, 20)]

        for province, (y, m, d) in product(holidays.DE.PROVINCES, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])

    def test_fronleichnam(self):
        known_good = [(2014, 6, 19), (2015, 6, 4), (2016, 5, 26),
                      (2017, 6, 15), (2018, 5, 31), (2019, 6, 20),
                      (2020, 6, 11), (2021, 6, 3), (2022, 6, 16),
                      (2023, 6, 8), (2024, 5, 30)]
        provinces_that_have = {'BW', 'BY', 'HE', 'NW', 'RP', 'SL'}
        provinces_that_dont = set(holidays.DE.PROVINCES) - provinces_that_have

        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertNotIn(date(y, m, d), self.prov_hols[province])

    def test_mariae_himmelfahrt(self):
        provinces_that_have = {'BY', 'SL'}
        provinces_that_dont = set(holidays.DE.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1991, 2050)):
            self.assertIn(date(year, 8, 15), self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1991, 2050)):
            self.assertNotIn(date(year, 8, 15), self.prov_hols[province])

    def test_reformationstag(self):
        prov_that_have = {'BB', 'MV', 'SN', 'ST', 'TH'}
        prov_yes_since_2018 = prov_that_have.union({'HB', 'HH', 'NI', 'SH'})
        prov_that_dont = set(holidays.DE.PROVINCES) - prov_that_have
        prov_not_since_2018 = set(holidays.DE.PROVINCES) - prov_yes_since_2018

        for province, year in product(prov_that_have, range(1991, 2050)):
            # in 2017 all states got the reformationstag for that year
            if year == 2017:
                continue
            self.assertIn(date(year, 10, 31), self.prov_hols[province])
        # additional provinces got this holiday 2018
        for province, year in product(prov_yes_since_2018, range(2018, 2050)):
            self.assertIn(date(year, 10, 31), self.prov_hols[province])
        for province, year in product(prov_that_dont, range(1991, 2017)):
            self.assertNotIn(date(year, 10, 31), self.prov_hols[province])
        for province, year in product(prov_not_since_2018, range(2018, 2050)):
            self.assertNotIn(date(year, 10, 31), self.prov_hols[province])
        # check the 2017 case where all states have the reformationstag
        for province in holidays.DE.PROVINCES:
            self.assertIn(date(2017, 10, 31), self.prov_hols[province])

    def test_allerheiligen(self):
        provinces_that_have = {'BW', 'BY', 'NW', 'RP', 'SL'}
        provinces_that_dont = set(holidays.DE.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1991, 2050)):
            self.assertIn(date(year, 11, 1), self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1991, 2050)):
            self.assertNotIn(date(year, 11, 1), self.prov_hols[province])

    def test_buss_und_bettag(self):
        known_good = [(2014, 11, 19), (2015, 11, 18), (2016, 11, 16),
                      (2017, 11, 22), (2018, 11, 21), (2019, 11, 20),
                      (2020, 11, 18), (2021, 11, 17), (2022, 11, 16),
                      (2023, 11, 22), (2024, 11, 20)]
        provinces_that_have = {'SN'}
        provinces_that_dont = set(holidays.DE.PROVINCES) - provinces_that_have

        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertNotIn(date(y, m, d), self.prov_hols[province])

    def test_tag_der_deutschen_einheit(self):
        known_good = [(1990, 6, 17)]

        for province, (y, m, d) in product(holidays.DE.PROVINCES, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])


class TestAT(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.AT()

    def test_new_years(self):
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_christmas(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertIn(dt + relativedelta(days=+1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+2), self.holidays)

    def test_easter_monday(self):
        for dt in [date(1900, 4, 16), date(1901, 4, 8), date(1902, 3, 31),
                   date(1999, 4, 5), date(2000, 4, 24), date(2010, 4, 5),
                   date(2018, 4, 2), date(2019, 4, 22), date(2020, 4, 13)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_national_day(self):
        for year in range(1919, 1934):
            dt = date(year, 11, 12)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)
        for year in range(1967, 2100):
            dt = date(year, 10, 26)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_all_holidays_present(self):
        at_2015 = holidays.AT(years=[2015])
        all_holidays = ["Neujahr",
                        "Heilige Drei Könige",
                        "Ostermontag",
                        "Staatsfeiertag",
                        "Christi Himmelfahrt",
                        "Pfingstmontag",
                        "Fronleichnam",
                        "Maria Himmelfahrt",
                        "Nationalfeiertag",
                        "Allerheiligen",
                        "Maria Empfängnis",
                        "Christtag",
                        "Stefanitag"]
        for holiday in all_holidays:
            self.assertIn(holiday, at_2015.values())


class TestDK(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.DK()

    def test_2016(self):
        # http://www.officeholidays.com/countries/denmark/2016.php
        self.assertIn(date(2016, 1, 1), self.holidays)
        self.assertIn(date(2016, 3, 24), self.holidays)
        self.assertIn(date(2016, 3, 25), self.holidays)
        self.assertIn(date(2016, 3, 28), self.holidays)
        self.assertIn(date(2016, 4, 22), self.holidays)
        self.assertIn(date(2016, 5, 5), self.holidays)
        self.assertIn(date(2016, 5, 16), self.holidays)
        self.assertIn(date(2016, 12, 25), self.holidays)


class TestUK(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.England()
        self.holidays = holidays.Wales()
        self.holidays = holidays.Scotland()
        self.holidays = holidays.IsleOfMan()
        self.holidays = holidays.NorthernIreland()
        self.holidays = holidays.UK()

    def test_new_years(self):
        for year in range(1974, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            if year == 2000:
                self.assertIn(dt + relativedelta(days=-1), self.holidays)
            else:
                self.assertNotIn(dt + relativedelta(days=-1), self.holidays)

    def test_good_friday(self):
        for dt in [date(1900, 4, 13), date(1901, 4, 5), date(1902, 3, 28),
                   date(1999, 4, 2), date(2000, 4, 21), date(2010, 4, 2),
                   date(2018, 3, 30), date(2019, 4, 19), date(2020, 4, 10)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_easter_monday(self):
        for dt in [date(1900, 4, 16), date(1901, 4, 8), date(1902, 3, 31),
                   date(1999, 4, 5), date(2000, 4, 24), date(2010, 4, 5),
                   date(2018, 4, 2), date(2019, 4, 22), date(2020, 4, 13)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_royal_wedding(self):
        self.assertIn('2011-04-29', self.holidays)
        self.assertNotIn('2010-04-29', self.holidays)
        self.assertNotIn('2012-04-29', self.holidays)

    def test_may_day(self):
        for dt in [date(1978, 5, 1), date(1979, 5, 7), date(1980, 5, 5),
                   date(1999, 5, 3), date(2000, 5, 1), date(2010, 5, 3),
                   date(2018, 5, 7), date(2019, 5, 6), date(2020, 5, 4)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_spring_bank_holiday(self):
        for dt in [date(1978, 5, 29), date(1979, 5, 28), date(1980, 5, 26),
                   date(1999, 5, 31), date(2000, 5, 29), date(2010, 5, 31),
                   date(2018, 5, 28), date(2019, 5, 27), date(2020, 5, 25)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_christmas_day(self):
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
        self.assertNotIn(date(2010, 12, 24), self.holidays)
        self.assertNotEqual(self.holidays[date(2011, 12, 26)],
                            "Christmas Day (Observed)")
        self.holidays.observed = True
        self.assertEqual(self.holidays[date(2011, 12, 27)],
                         "Christmas Day (Observed)")
        for year, day in enumerate([25, 25, 25, 27, 27,  # 2001-05
                                    25, 25, 25, 25, 27,  # 2006-10
                                    27, 25, 25, 25, 25,  # 2011-15
                                    27, 25, 25, 25, 25, 25],  # 2016-21
                                   2001):
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
        self.assertIn(date(2004, 12, 28), self.holidays)
        self.assertIn(date(2010, 12, 28), self.holidays)
        for year, day in enumerate([26, 26, 26, 28, 26,
                                    26, 26, 26, 28, 28,
                                    26, 26, 26, 26, 26,
                                    26, 26, 26, 26, 26, 28],
                                   2001):
            dt = date(year, 12, day)
            self.assertIn(dt, self.holidays, dt)
            self.assertEqual(self.holidays[dt][:6], "Boxing")

    def test_all_holidays_present(self):
        uk_2015 = holidays.UK(years=[2015])
        all_holidays = ["New Year's Day",
                        "Good Friday",
                        "Easter Monday [England, Wales, Northern Ireland]",
                        "May Day",
                        "Spring Bank Holiday",
                        "Christmas Day",
                        "Boxing Day"]
        for holiday in all_holidays:
            self.assertIn(holiday, uk_2015.values())


class TestScotland(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.Scotland()

    def test_2017(self):
        self.assertIn('2017-01-01', self.holidays)
        self.assertIn('2017-01-02', self.holidays)
        self.assertIn('2017-01-03', self.holidays)
        self.assertIn('2017-04-14', self.holidays)
        self.assertIn('2017-05-01', self.holidays)
        self.assertIn('2017-05-29', self.holidays)
        self.assertIn('2017-08-07', self.holidays)
        self.assertIn('2017-11-30', self.holidays)
        self.assertIn('2017-12-25', self.holidays)
        self.assertIn('2017-12-26', self.holidays)


class TestIsleOfMan(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.IsleOfMan()

    def test_2018(self):
        self.assertIn('2018-06-01', self.holidays)
        self.assertIn('2018-07-05', self.holidays)


class TestES(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.ES()
        self.prov_holidays = {prov: holidays.ES(prov=prov)
                              for prov in holidays.ES.PROVINCES}

    def test_fixed_holidays(self):
        fixed_days_whole_country = (
            (1, 1),
            (1, 6),
            (5, 1),
            (8, 15),
            (10, 12),
            (11, 1),
            (12, 6),
            (12, 8),
            (12, 25),
        )
        for y, (m, d) in product(range(1950, 2050), fixed_days_whole_country):
            self.assertIn(date(y, m, d), self.holidays)

    def test_variable_days_in_2016(self):
        self.assertIn(date(2016, 3, 25), self.holidays)
        for prov, prov_holidays in self.prov_holidays.items():
            self.assertEqual(
                date(2016, 3, 24) in prov_holidays, prov != 'CAT')
            self.assertEqual(
                date(2016, 3, 28) in prov_holidays,
                prov in ['CAT', 'PVA', 'NAV', 'CVA', 'IBA'])

    def test_province_specific_days(self):
        province_days = {
            (2, 28): ['AND', 'CAN', 'CAM'],
            (3, 1): ['IBA'],
            (3, 8): ['AST'],
            (4, 23): ['ARG', 'CAL'],
            (5, 30): ['ICA'],
            (5, 2): ['MAD'],
            (6, 9): ['MUR', 'RIO'],
            (7, 25): ['GAL'],
            (9, 8): ['EXT'],
            (9, 11): ['CAT'],
            (9, 27): ['NAV'],
            (10, 9): ['CVA'],
            (10, 25): ['PVA'],
        }
        for prov, prov_holidays in self.prov_holidays.items():
            for year in range(2010, 2020):
                self.assertEqual(
                    date(year, 12, 26) in prov_holidays,
                    prov in ['CAT', 'IBA'])
                self.assertEqual(
                    date(year, 3, 19) in prov_holidays,
                    prov in ['CVA', 'MUR', 'MAD', 'NAV', 'PVA'])
                self.assertEqual(
                    date(year, 6, 24) in prov_holidays,
                    prov in ['CAT', 'GAL'])
                for fest_day, fest_prov in province_days.items():
                    self.assertEqual(
                        date(year, *fest_day) in prov_holidays,
                        prov in fest_prov)


class TestTAR(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.TAR()

    def test_new_years(self):
        for year in range(1974, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)

    def test_good_friday(self):
        for dt in [date(1900, 4, 13), date(1901, 4, 5), date(1902, 3, 28),
                   date(1999, 4, 2), date(2000, 4, 21), date(2010, 4, 2),
                   date(2018, 3, 30), date(2019, 4, 19), date(2020, 4, 10)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_easter_monday(self):
        for dt in [date(1900, 4, 16), date(1901, 4, 8), date(1902, 3, 31),
                   date(1999, 4, 5), date(2000, 4, 24), date(2010, 4, 5),
                   date(2018, 4, 2), date(2019, 4, 22), date(2020, 4, 13)]:
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_labour_day(self):
        for year in range(1900, 2100):
            dt = date(year, 5, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_christmas_day(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)

    def test_26_december_day(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 26)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_all_holidays_present(self):
        tar_2015 = holidays.TAR(years=[2015])
        all_holidays = ["New Year's Day",
                        "Good Friday",
                        "Easter Monday",
                        "1 May (Labour Day)",
                        "Christmas Day",
                        "26 December"]
        for holiday in all_holidays:
            self.assertIn(holiday, tar_2015.values())


class TestECB(unittest.TestCase):

    def setUp(self):
        self.holidays_ecb = holidays.ECB()
        self.holidays_tar = holidays.TAR()

    def test_new_years(self):
        for year in range(1974, 2100):
            self.holidays_ecb._populate(year)
            self.holidays_tar._populate(year)
        for holiday in self.holidays_tar:
            self.assertIn(holiday, self.holidays_ecb)


class TestCZ(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.CZ()

    def test_2017(self):
        # http://www.officeholidays.com/countries/czech_republic/2017.php
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 5, 1), self.holidays)
        self.assertIn(date(2017, 5, 8), self.holidays)
        self.assertIn(date(2017, 7, 5), self.holidays)
        self.assertIn(date(2017, 7, 6), self.holidays)
        self.assertIn(date(2017, 9, 28), self.holidays)
        self.assertIn(date(2017, 10, 28), self.holidays)
        self.assertIn(date(2017, 11, 17), self.holidays)
        self.assertIn(date(2017, 12, 24), self.holidays)
        self.assertIn(date(2017, 12, 25), self.holidays)
        self.assertIn(date(2017, 12, 26), self.holidays)

    def test_others(self):
        self.assertIn(date(1991, 5, 9), self.holidays)


class TestSK(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.SK()

    def test_2018(self):
        # https://www.officeholidays.com/countries/slovakia/2018.php
        self.assertIn(date(2018, 1, 1), self.holidays)
        self.assertIn(date(2018, 1, 6), self.holidays)
        self.assertIn(date(2018, 3, 30), self.holidays)
        self.assertIn(date(2018, 5, 1), self.holidays)
        self.assertIn(date(2018, 5, 8), self.holidays)
        self.assertIn(date(2018, 4, 2), self.holidays)
        self.assertIn(date(2018, 7, 5), self.holidays)
        self.assertIn(date(2018, 8, 29), self.holidays)
        self.assertIn(date(2018, 9, 1), self.holidays)
        self.assertIn(date(2018, 9, 15), self.holidays)
        self.assertIn(date(2018, 10, 30), self.holidays)
        self.assertIn(date(2018, 11, 1), self.holidays)
        self.assertIn(date(2018, 11, 17), self.holidays)
        self.assertIn(date(2018, 12, 24), self.holidays)
        self.assertIn(date(2018, 12, 25), self.holidays)
        self.assertIn(date(2018, 12, 26), self.holidays)


class TestPL(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.PL()

    def test_2017(self):
        # http://www.officeholidays.com/countries/poland/2017.php
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 1, 6), self.holidays)
        self.assertIn(date(2017, 4, 16), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 5, 1), self.holidays)
        self.assertIn(date(2017, 5, 3), self.holidays)
        self.assertIn(date(2017, 6, 4), self.holidays)
        self.assertIn(date(2017, 6, 15), self.holidays)
        self.assertIn(date(2017, 8, 15), self.holidays)
        self.assertIn(date(2017, 11, 1), self.holidays)
        self.assertIn(date(2017, 11, 11), self.holidays)
        self.assertIn(date(2017, 12, 25), self.holidays)
        self.assertIn(date(2017, 12, 26), self.holidays)


class TestPT(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.PT()

    def test_2017(self):
        # http://www.officeholidays.com/countries/portugal/2017.php
        self.assertIn(date(2017, 1, 1), self.holidays)  # New Year
        self.assertIn(date(2017, 4, 14), self.holidays)  # Good Friday
        self.assertIn(date(2017, 4, 16), self.holidays)  # Easter
        self.assertIn(date(2017, 4, 25), self.holidays)  # Liberation Day
        self.assertIn(date(2017, 5, 1), self.holidays)  # Labour Day
        self.assertIn(date(2017, 6, 10), self.holidays)  # Portugal Day
        self.assertIn(date(2017, 6, 15), self.holidays)  # Corpus Christi
        self.assertIn(date(2017, 8, 15), self.holidays)  # Assumption Day
        self.assertIn(date(2017, 10, 5), self.holidays)  # Republic Day
        self.assertIn(date(2017, 11, 1), self.holidays)  # All Saints Day
        self.assertIn(date(2017, 12, 1), self.holidays)  # Independence
        self.assertIn(date(2017, 12, 8), self.holidays)  # Immaculate
        self.assertIn(date(2017, 12, 25), self.holidays)  # Christmas


class TestPortugalExt(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.PortugalExt()

    def test_2017(self):
        self.assertIn(date(2017, 12, 24), self.holidays)  # Christmas' Eve
        self.assertIn(date(2017, 12, 26), self.holidays)  # S.Stephan
        self.assertIn(date(2017, 12, 26), self.holidays)  # New Year's Eve


class TestNorway(unittest.TestCase):

    def setUp(self):
        self.holidays_without_sundays = holidays.Norway(include_sundays=False)
        self.holidays_with_sundays = holidays.Norway()

    def test_new_years(self):
        self.assertIn('1900-01-01', self.holidays_without_sundays)
        self.assertIn('2017-01-01', self.holidays_without_sundays)
        self.assertIn('2999-01-01', self.holidays_without_sundays)

    def test_easter(self):
        self.assertIn('2000-04-20', self.holidays_without_sundays)
        self.assertIn('2000-04-21', self.holidays_without_sundays)
        self.assertIn('2000-04-23', self.holidays_without_sundays)
        self.assertIn('2000-04-24', self.holidays_without_sundays)

        self.assertIn('2010-04-01', self.holidays_without_sundays)
        self.assertIn('2010-04-02', self.holidays_without_sundays)
        self.assertIn('2010-04-04', self.holidays_without_sundays)
        self.assertIn('2010-04-05', self.holidays_without_sundays)

        self.assertIn('2021-04-01', self.holidays_without_sundays)
        self.assertIn('2021-04-02', self.holidays_without_sundays)
        self.assertIn('2021-04-04', self.holidays_without_sundays)
        self.assertIn('2021-04-05', self.holidays_without_sundays)

        self.assertIn('2024-03-28', self.holidays_without_sundays)
        self.assertIn('2024-03-29', self.holidays_without_sundays)
        self.assertIn('2024-03-31', self.holidays_without_sundays)
        self.assertIn('2024-04-01', self.holidays_without_sundays)

    def test_workers_day(self):
        self.assertNotIn('1900-05-01', self.holidays_without_sundays)
        self.assertNotIn('1946-05-01', self.holidays_without_sundays)
        self.assertIn('1947-05-01', self.holidays_without_sundays)
        self.assertIn('2017-05-01', self.holidays_without_sundays)
        self.assertIn('2999-05-01', self.holidays_without_sundays)

    def test_constitution_day(self):
        self.assertNotIn('1900-05-17', self.holidays_without_sundays)
        self.assertNotIn('1946-05-17', self.holidays_without_sundays)
        self.assertIn('1947-05-17', self.holidays_without_sundays)
        self.assertIn('2017-05-17', self.holidays_without_sundays)
        self.assertIn('2999-05-17', self.holidays_without_sundays)

    def test_pentecost(self):
        self.assertIn('2000-06-11', self.holidays_without_sundays)
        self.assertIn('2000-06-12', self.holidays_without_sundays)

        self.assertIn('2010-05-23', self.holidays_without_sundays)
        self.assertIn('2010-05-24', self.holidays_without_sundays)

        self.assertIn('2021-05-23', self.holidays_without_sundays)
        self.assertIn('2021-05-24', self.holidays_without_sundays)

        self.assertIn('2024-05-19', self.holidays_without_sundays)
        self.assertIn('2024-05-20', self.holidays_without_sundays)

    def test_christmas(self):
        self.assertIn('1901-12-25', self.holidays_without_sundays)
        self.assertIn('1901-12-26', self.holidays_without_sundays)

        self.assertIn('2016-12-25', self.holidays_without_sundays)
        self.assertIn('2016-12-26', self.holidays_without_sundays)

        self.assertIn('2500-12-25', self.holidays_without_sundays)
        self.assertIn('2500-12-26', self.holidays_without_sundays)

    def test_sundays(self):
        """
        Sundays are considered holidays in Norway
        :return:
        """
        self.assertIn('1989-12-31', self.holidays_with_sundays)
        self.assertIn('2017-02-05', self.holidays_with_sundays)
        self.assertIn('2017-02-12', self.holidays_with_sundays)
        self.assertIn('2032-02-29', self.holidays_with_sundays)

    def test_not_holiday(self):
        """
        Note: Sundays in Norway are considered holidays,
        so make sure none of these are actually Sundays

        TODO: Should add more dates that are often confused for being a holiday
        :return:
        """
        self.assertNotIn('2017-02-06', self.holidays_without_sundays)
        self.assertNotIn('2017-02-07', self.holidays_without_sundays)
        self.assertNotIn('2017-02-08', self.holidays_without_sundays)
        self.assertNotIn('2017-02-09', self.holidays_without_sundays)
        self.assertNotIn('2017-02-10', self.holidays_without_sundays)

        self.assertNotIn('2001-12-24', self.holidays_without_sundays)
        self.assertNotIn('2001-05-16', self.holidays_without_sundays)
        self.assertNotIn('2001-05-18', self.holidays_without_sundays)
        self.assertNotIn('1999-12-31', self.holidays_without_sundays)
        self.assertNotIn('2016-12-31', self.holidays_without_sundays)
        self.assertNotIn('2016-12-27', self.holidays_without_sundays)
        self.assertNotIn('2016-12-28', self.holidays_without_sundays)

        self.assertNotIn('2017-02-06', self.holidays_with_sundays)
        self.assertNotIn('2017-02-07', self.holidays_with_sundays)
        self.assertNotIn('2017-02-08', self.holidays_with_sundays)
        self.assertNotIn('2017-02-09', self.holidays_with_sundays)
        self.assertNotIn('2017-02-10', self.holidays_with_sundays)

        self.assertNotIn('2001-12-24', self.holidays_with_sundays)
        self.assertNotIn('2001-05-16', self.holidays_with_sundays)
        self.assertNotIn('2001-05-18', self.holidays_with_sundays)
        self.assertNotIn('1999-12-31', self.holidays_with_sundays)
        self.assertNotIn('2016-12-31', self.holidays_with_sundays)
        self.assertNotIn('2016-12-27', self.holidays_with_sundays)
        self.assertNotIn('2016-12-28', self.holidays_with_sundays)


class TestItaly(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.IT()

    def test_2017(self):
        # https://www.giorni-festivi.it/
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 1, 6), self.holidays)
        self.assertIn(date(2017, 4, 16), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 4, 25), self.holidays)
        self.assertIn(date(2017, 5, 1), self.holidays)
        self.assertIn(date(2017, 6, 2), self.holidays)
        self.assertIn(date(2017, 8, 15), self.holidays)
        self.assertIn(date(2017, 11, 1), self.holidays)
        self.assertIn(date(2017, 12, 8), self.holidays)
        self.assertIn(date(2017, 12, 25), self.holidays)
        self.assertIn(date(2017, 12, 26), self.holidays)

    def test_new_years(self):
        for year in range(1974, 2100):
            self.assertIn(date(year, 1, 1), self.holidays)

    def test_easter(self):
        self.assertIn(date(2017, 4, 16), self.holidays)

    def test_easter_monday(self):
        self.assertIn(date(2017, 4, 17), self.holidays)

    def test_republic_day_before_1948(self):
        self.holidays = holidays.IT(years=[1947])
        self.assertNotIn(date(1947, 6, 2), self.holidays)

    def test_republic_day_after_1948(self):
        self.holidays = holidays.IT(years=[1948])
        self.assertIn(date(1948, 6, 2), self.holidays)

    def test_liberation_day_before_1946(self):
        self.holidays = holidays.IT(years=1945)
        self.assertNotIn(date(1945, 4, 25), self.holidays)

    def test_liberation_day_after_1946(self):
        self.holidays = holidays.IT(years=1946)
        self.assertIn(date(1946, 4, 25), self.holidays)

    def test_christmas(self):
        self.holidays = holidays.IT(years=2017)
        self.assertIn(date(2017, 12, 25), self.holidays)

    def test_saint_stephan(self):
        self.holidays = holidays.IT(years=2017)
        self.assertIn(date(2017, 12, 26), self.holidays)

    def test_province_specific_days(self):
        prov_mi = (holidays.IT(prov='MI', years=[2017]))
        prov_rm = (holidays.IT(prov='RM', years=[2017]))
        self.assertIn("2017-12-08", prov_mi)
        self.assertIn("2017-06-29", prov_rm)


class TestSweden(unittest.TestCase):

    def setUp(self):
        self.holidays_without_sundays = holidays.Sweden(include_sundays=False)
        self.holidays_with_sundays = holidays.Sweden()

    def test_new_years(self):
        self.assertIn('1900-01-01', self.holidays_without_sundays)
        self.assertIn('2017-01-01', self.holidays_without_sundays)
        self.assertIn('2999-01-01', self.holidays_without_sundays)

    def test_easter(self):
        self.assertNotIn('2000-04-20', self.holidays_without_sundays)
        self.assertIn('2000-04-21', self.holidays_without_sundays)
        self.assertIn('2000-04-23', self.holidays_without_sundays)
        self.assertIn('2000-04-24', self.holidays_without_sundays)

        self.assertNotIn('2010-04-01', self.holidays_without_sundays)
        self.assertIn('2010-04-02', self.holidays_without_sundays)
        self.assertIn('2010-04-04', self.holidays_without_sundays)
        self.assertIn('2010-04-05', self.holidays_without_sundays)

        self.assertNotIn('2021-04-01', self.holidays_without_sundays)
        self.assertIn('2021-04-02', self.holidays_without_sundays)
        self.assertIn('2021-04-04', self.holidays_without_sundays)
        self.assertIn('2021-04-05', self.holidays_without_sundays)

        self.assertNotIn('2024-03-28', self.holidays_without_sundays)
        self.assertIn('2024-03-29', self.holidays_without_sundays)
        self.assertIn('2024-03-31', self.holidays_without_sundays)
        self.assertIn('2024-04-01', self.holidays_without_sundays)

    def test_workers_day(self):
        self.assertNotIn('1800-05-01', self.holidays_without_sundays)
        self.assertNotIn('1879-05-01', self.holidays_without_sundays)
        self.assertIn('1939-05-01', self.holidays_without_sundays)
        self.assertIn('2017-05-01', self.holidays_without_sundays)
        self.assertIn('2999-05-01', self.holidays_without_sundays)

    def test_constitution_day(self):
        self.assertNotIn('1900-06-06', self.holidays_without_sundays)
        self.assertNotIn('2004-06-06', self.holidays_without_sundays)
        self.assertIn('2005-06-06', self.holidays_without_sundays)
        self.assertIn('2017-06-06', self.holidays_without_sundays)
        self.assertIn('2999-06-06', self.holidays_without_sundays)

    def test_pentecost(self):
        self.assertIn('2000-06-11', self.holidays_without_sundays)
        self.assertIn('2000-06-12', self.holidays_without_sundays)

        self.assertIn('2010-05-23', self.holidays_without_sundays)
        self.assertNotIn('2010-05-24', self.holidays_without_sundays)

        self.assertIn('2021-05-23', self.holidays_without_sundays)
        self.assertNotIn('2021-05-24', self.holidays_without_sundays)

        self.assertIn('2003-06-09', self.holidays_without_sundays)

        self.assertIn('2024-05-19', self.holidays_without_sundays)
        self.assertNotIn('2024-05-20', self.holidays_without_sundays)

    def test_christmas(self):
        self.assertIn('1901-12-25', self.holidays_without_sundays)
        self.assertIn('1901-12-26', self.holidays_without_sundays)

        self.assertIn('2016-12-25', self.holidays_without_sundays)
        self.assertIn('2016-12-26', self.holidays_without_sundays)

        self.assertIn('2500-12-25', self.holidays_without_sundays)
        self.assertIn('2500-12-26', self.holidays_without_sundays)

    def test_sundays(self):
        """
        Sundays are considered holidays in Sweden
        :return:
        """
        self.assertIn('1989-12-31', self.holidays_with_sundays)
        self.assertIn('2017-02-05', self.holidays_with_sundays)
        self.assertIn('2017-02-12', self.holidays_with_sundays)
        self.assertIn('2032-02-29', self.holidays_with_sundays)

    def test_not_holiday(self):
        """
        Note: Sundays in Sweden are considered holidays,
        so make sure none of these are actually Sundays
        :return:
        """
        self.assertNotIn('2017-02-06', self.holidays_without_sundays)
        self.assertNotIn('2017-02-07', self.holidays_without_sundays)
        self.assertNotIn('2017-02-08', self.holidays_without_sundays)
        self.assertNotIn('2017-02-09', self.holidays_without_sundays)
        self.assertNotIn('2017-02-10', self.holidays_without_sundays)
        self.assertNotIn('2016-12-27', self.holidays_without_sundays)
        self.assertNotIn('2016-12-28', self.holidays_without_sundays)

        self.assertNotIn('2017-02-06', self.holidays_with_sundays)
        self.assertNotIn('2017-02-07', self.holidays_with_sundays)
        self.assertNotIn('2017-02-08', self.holidays_with_sundays)
        self.assertNotIn('2017-02-09', self.holidays_with_sundays)
        self.assertNotIn('2017-02-10', self.holidays_with_sundays)
        self.assertNotIn('2016-12-27', self.holidays_with_sundays)
        self.assertNotIn('2016-12-28', self.holidays_with_sundays)


class TestJapan(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.Japan(observed=False)

    def test_new_years_day(self):
        self.assertIn(date(1949, 1, 1), self.holidays)
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2050, 1, 1), self.holidays)

    def test_coming_of_age(self):
        self.assertIn(date(1999, 1, 15), self.holidays)
        self.assertIn(date(2000, 1, 10), self.holidays)
        self.assertIn(date(2017, 1, 9), self.holidays)
        self.assertIn(date(2030, 1, 14), self.holidays)
        self.assertIn(date(2050, 1, 10), self.holidays)

        self.assertNotIn(date(2000, 1, 15), self.holidays)
        self.assertNotIn(date(2017, 1, 15), self.holidays)
        self.assertNotIn(date(2030, 1, 15), self.holidays)

    def test_foundation_day(self):
        self.assertIn(date(1949, 2, 11), self.holidays)
        self.assertIn(date(2017, 2, 11), self.holidays)
        self.assertIn(date(2050, 2, 11), self.holidays)

    def test_vernal_equinox_day(self):
        self.assertIn(date(1956, 3, 21), self.holidays)
        self.assertIn(date(1960, 3, 20), self.holidays)
        self.assertIn(date(1970, 3, 21), self.holidays)
        self.assertIn(date(1980, 3, 20), self.holidays)
        self.assertIn(date(1990, 3, 21), self.holidays)
        self.assertIn(date(2000, 3, 20), self.holidays)
        self.assertIn(date(2010, 3, 21), self.holidays)
        self.assertIn(date(2017, 3, 20), self.holidays)
        self.assertIn(date(2020, 3, 20), self.holidays)
        self.assertIn(date(2030, 3, 20), self.holidays)
        self.assertIn(date(2040, 3, 20), self.holidays)
        self.assertIn(date(2092, 3, 19), self.holidays)

    def test_showa_day(self):
        self.assertIn(date(1950, 4, 29), self.holidays)
        self.assertIn(date(1990, 4, 29), self.holidays)
        self.assertIn(date(2010, 4, 29), self.holidays)

    def test_constitution_memorial_day(self):
        self.assertIn(date(1950, 5, 3), self.holidays)
        self.assertIn(date(2000, 5, 3), self.holidays)
        self.assertIn(date(2050, 5, 3), self.holidays)

    def test_greenery_day(self):
        self.assertNotIn(date(1950, 5, 4), self.holidays)
        self.assertIn(date(2007, 5, 4), self.holidays)
        self.assertIn(date(2050, 5, 4), self.holidays)

    def test_childrens_day(self):
        self.assertIn(date(1950, 5, 5), self.holidays)
        self.assertIn(date(2000, 5, 5), self.holidays)
        self.assertIn(date(2050, 5, 5), self.holidays)

    def test_marine_day(self):
        self.assertNotIn(date(1950, 7, 20), self.holidays)
        self.assertIn(date(2000, 7, 20), self.holidays)
        self.assertIn(date(2003, 7, 21), self.holidays)
        self.assertIn(date(2017, 7, 17), self.holidays)
        self.assertIn(date(2050, 7, 18), self.holidays)

    def test_mountain_day(self):
        self.assertNotIn(date(1950, 8, 11), self.holidays)
        self.assertNotIn(date(2015, 8, 11), self.holidays)
        self.assertIn(date(2016, 8, 11), self.holidays)
        self.assertIn(date(2017, 8, 11), self.holidays)
        self.assertIn(date(2050, 8, 11), self.holidays)

    def test_respect_for_the_aged_day(self):
        self.assertNotIn(date(1965, 9, 15), self.holidays)
        self.assertIn(date(1966, 9, 15), self.holidays)
        self.assertIn(date(2002, 9, 15), self.holidays)
        self.assertIn(date(2003, 9, 15), self.holidays)
        self.assertNotIn(date(2004, 9, 15), self.holidays)
        self.assertIn(date(2004, 9, 20), self.holidays)
        self.assertIn(date(2017, 9, 18), self.holidays)
        self.assertIn(date(2050, 9, 19), self.holidays)

    def test_autumnal_equinox_day(self):
        self.assertIn(date(2000, 9, 23), self.holidays)
        self.assertIn(date(2010, 9, 23), self.holidays)
        self.assertIn(date(2017, 9, 23), self.holidays)
        self.assertIn(date(2020, 9, 22), self.holidays)
        self.assertIn(date(2030, 9, 23), self.holidays)
        self.assertIn(date(1979, 9, 24), self.holidays)
        self.assertIn(date(2032, 9, 21), self.holidays)

    def test_health_and_sports_day(self):
        self.assertNotIn(date(1965, 10, 10), self.holidays)
        self.assertIn(date(1966, 10, 10), self.holidays)
        self.assertIn(date(1999, 10, 10), self.holidays)
        self.assertNotIn(date(2000, 10, 10), self.holidays)
        self.assertIn(date(2000, 10, 9), self.holidays)
        self.assertIn(date(2017, 10, 9), self.holidays)
        self.assertIn(date(2050, 10, 10), self.holidays)

    def test_culture_day(self):
        self.assertIn(date(1950, 11, 3), self.holidays)
        self.assertIn(date(2000, 11, 3), self.holidays)
        self.assertIn(date(2050, 11, 3), self.holidays)

    def test_labour_thanks_giving_day(self):
        self.assertIn(date(1950, 11, 23), self.holidays)
        self.assertIn(date(2000, 11, 23), self.holidays)
        self.assertIn(date(2050, 11, 23), self.holidays)

    def test_emperors_birthday(self):
        self.assertIn(date(1989, 12, 23), self.holidays)
        self.assertIn(date(2017, 12, 23), self.holidays)
        self.assertIn(date(2050, 12, 23), self.holidays)

    def test_invalid_years(self):
        self.assertRaises(NotImplementedError,
                          lambda: date(1948, 1, 1) in self.holidays)
        self.assertRaises(NotImplementedError,
                          lambda: date(2100, 1, 1) in self.holidays)


class TestFrance(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.France()
        self.prov_holidays = {prov: holidays.France(prov=prov)
                              for prov in holidays.France.PROVINCES}

    def test_2017(self):
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 5, 1), self.holidays)
        self.assertIn(date(2017, 5, 8), self.holidays)
        self.assertIn(date(2017, 5, 25), self.holidays)
        self.assertIn(date(2017, 6, 5), self.holidays)
        self.assertIn(date(2017, 7, 14), self.holidays)

    def test_others(self):
        self.assertEqual(self.holidays[date(1948, 5, 1)],
                         'Fête du Travail et de la Concorde sociale')

    def test_alsace_moselle(self):
        am_holidays = self.prov_holidays['Alsace-Moselle']
        self.assertIn(date(2017, 4, 14), am_holidays)
        self.assertIn(date(2017, 12, 26), am_holidays)

    def test_mayotte(self):
        am_holidays = self.prov_holidays['Mayotte']
        self.assertIn(date(2017, 4, 27), am_holidays)

    def test_wallis_et_futuna(self):
        am_holidays = self.prov_holidays['Wallis-et-Futuna']
        self.assertIn(date(2017, 4, 28), am_holidays)
        self.assertIn(date(2017, 7, 29), am_holidays)

    def test_martinique(self):
        am_holidays = self.prov_holidays['Martinique']
        self.assertIn(date(2017, 5, 22), am_holidays)

    def test_guadeloupe(self):
        am_holidays = self.prov_holidays['Guadeloupe']
        self.assertIn(date(2017, 5, 27), am_holidays)
        self.assertIn(date(2017, 7, 21), am_holidays)

    def test_guyane(self):
        am_holidays = self.prov_holidays['Guyane']
        self.assertIn(date(2017, 6, 10), am_holidays)

    def test_polynesie_francaise(self):
        am_holidays = self.prov_holidays['Polynésie Française']
        self.assertIn(date(2017, 6, 29), am_holidays)

    def test_nouvelle_caledonie(self):
        am_holidays = self.prov_holidays['Nouvelle-Calédonie']
        self.assertIn(date(2017, 9, 24), am_holidays)

    def test_saint_barthelemy(self):
        am_holidays = self.prov_holidays['Saint-Barthélémy']
        self.assertIn(date(2017, 10, 9), am_holidays)

    def test_la_reunion(self):
        am_holidays = self.prov_holidays['La Réunion']
        self.assertIn(date(2017, 12, 20), am_holidays)


class TestBelgium(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.BE()

    def test_2017(self):
        # https://www.belgium.be/nl/over_belgie/land/belgie_in_een_notendop/feestdagen
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 4, 16), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(2017, 5, 1), self.holidays)
        self.assertIn(date(2017, 5, 25), self.holidays)
        self.assertIn(date(2017, 6, 4), self.holidays)
        self.assertIn(date(2017, 6, 5), self.holidays)
        self.assertIn(date(2017, 7, 21), self.holidays)
        self.assertIn(date(2017, 8, 15), self.holidays)
        self.assertIn(date(2017, 11, 1), self.holidays)
        self.assertIn(date(2017, 11, 11), self.holidays)
        self.assertIn(date(2017, 12, 25), self.holidays)


class TestSouthAfrica(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.ZA()

    def test_new_years(self):
        self.assertIn('1900-01-01', self.holidays)
        self.assertIn('2017-01-01', self.holidays)
        self.assertIn('2999-01-01', self.holidays)
        self.assertIn('2017-01-02', self.holidays)  # sunday

    def test_easter(self):
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertIn(date(1994, 4, 1), self.holidays)

    def test_static(self):
        self.assertIn('2004-08-09', self.holidays)

    def test_not_holiday(self):
        self.assertNotIn('2016-12-28', self.holidays)
        self.assertNotIn('2015-03-02', self.holidays)


class TestSI(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.SI()

    def test_holidays(self):
        """
        Test all expected holiday dates
        :return:
        """
        # New Year
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertIn(date(2017, 1, 2), self.holidays)
        # Prešeren's day
        self.assertIn(date(2017, 2, 8), self.holidays)
        # Easter monday - 2016 and 2017
        self.assertIn(date(2016, 3, 28), self.holidays)
        self.assertIn(date(2017, 4, 17), self.holidays)
        # Day of uprising against occupation
        self.assertIn(date(2017, 4, 27), self.holidays)
        # Labour day
        self.assertIn(date(2017, 5, 1), self.holidays)
        # Labour day
        self.assertIn(date(2017, 5, 2), self.holidays)
        # Statehood day
        self.assertIn(date(2017, 6, 25), self.holidays)
        # Assumption day
        self.assertIn(date(2017, 8, 15), self.holidays)
        # Reformation day
        self.assertIn(date(2017, 10, 31), self.holidays)
        # Remembrance day
        self.assertIn(date(2017, 11, 1), self.holidays)
        # Christmas
        self.assertIn(date(2017, 12, 25), self.holidays)
        # Day of independence and unity
        self.assertIn(date(2017, 12, 26), self.holidays)

    def test_non_holidays(self):
        """
        Test dates that should be excluded from holidays list
        :return:
        """
        # January 2nd was not public holiday between 2012 and 2017
        self.assertNotIn(date(2013, 1, 2), self.holidays)
        self.assertNotIn(date(2014, 1, 2), self.holidays)
        self.assertNotIn(date(2015, 1, 2), self.holidays)
        self.assertNotIn(date(2016, 1, 2), self.holidays)

    def test_missing_years(self):
        self.assertNotIn(date(1990, 1, 1), self.holidays)


class TestIE(unittest.TestCase):

    def setUp(self):
        self.irish_holidays = holidays.IE()

    def test_new_year_day(self):
        self.assertIn('2017-01-02', self.irish_holidays)
        self.assertIn('2018-01-01', self.irish_holidays)

    def test_st_patricks_day(self):
        self.assertIn('2017-03-17', self.irish_holidays)
        self.assertIn('2018-03-17', self.irish_holidays)

    def test_easter_monday(self):
        self.assertIn('2017-04-17', self.irish_holidays)
        self.assertIn('2018-04-02', self.irish_holidays)

    def test_may_bank_holiday(self):
        self.assertIn('2017-05-01', self.irish_holidays)
        self.assertIn('2018-05-07', self.irish_holidays)

    def test_june_bank_holiday(self):
        self.assertIn('2017-06-05', self.irish_holidays)
        self.assertIn('2018-06-04', self.irish_holidays)

    def test_august_bank_holiday(self):
        self.assertIn('2017-08-07', self.irish_holidays)
        self.assertIn('2018-08-06', self.irish_holidays)

    def test_october_bank_holiday(self):
        self.assertIn('2017-10-30', self.irish_holidays)
        self.assertIn('2018-10-29', self.irish_holidays)

    def test_christmas_period(self):
        self.assertIn('2015-12-25', self.irish_holidays)
        self.assertIn('2015-12-28', self.irish_holidays)
        self.assertIn('2016-12-26', self.irish_holidays)
        self.assertIn('2016-12-27', self.irish_holidays)
        self.assertIn('2017-12-25', self.irish_holidays)
        self.assertIn('2017-12-26', self.irish_holidays)
        self.assertIn('2018-12-25', self.irish_holidays)
        self.assertIn('2018-12-26', self.irish_holidays)


class TestFinland(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.FI()

    def test_fixed_holidays(self):
        self.assertIn(date(2017, 1, 1), self.holidays)
        self.assertEqual(self.holidays[date(2017, 1, 1)],
                         "Uudenvuodenpäivä")

        self.assertIn(date(2017, 1, 6), self.holidays)
        self.assertEqual(self.holidays[date(2017, 1, 6)],
                         "Loppiainen")

        self.assertIn(date(2017, 5, 1), self.holidays)
        self.assertEqual(self.holidays[date(2017, 5, 1)],
                         "Vappu")

        self.assertIn(date(2017, 12, 6), self.holidays)
        self.assertEqual(self.holidays[date(2017, 12, 6)],
                         "Itsenäisyyspäivä")

        self.assertIn(date(2017, 12, 25), self.holidays)
        self.assertEqual(self.holidays[date(2017, 12, 25)],
                         "Joulupäivä")

        self.assertIn(date(2017, 12, 26), self.holidays)
        self.assertEqual(self.holidays[date(2017, 12, 26)],
                         "Tapaninpäivä")

    def test_relative_holidays(self):
        self.assertIn(date(2017, 4, 14), self.holidays)
        self.assertEqual(self.holidays[date(2017, 4, 14)],
                         "Pitkäperjantai")

        self.assertIn(date(2017, 4, 16), self.holidays)
        self.assertEqual(self.holidays[date(2017, 4, 16)],
                         "Pääsiäispäivä")

        self.assertIn(date(2017, 4, 17), self.holidays)
        self.assertEqual(self.holidays[date(2017, 4, 17)],
                         "2. pääsiäispäivä")

        self.assertIn(date(2017, 5, 25), self.holidays)
        self.assertEqual(self.holidays[date(2017, 5, 25)],
                         "Helatorstai")

        self.assertIn(date(2017, 11, 4), self.holidays)
        self.assertEqual(self.holidays[date(2017, 11, 4)],
                         "Pyhäinpäivä")

    def test_Juhannus(self):
        self.assertIn(date(2017, 6, 24), self.holidays)
        self.assertNotIn(date(2017, 6, 20), self.holidays)
        self.assertIn(date(2020, 6, 20), self.holidays)
        self.assertIn(date(2021, 6, 26), self.holidays)
        self.assertIn(date(2018, 6, 22), self.holidays)
        self.assertEqual(self.holidays[date(2018, 6, 22)],
                         "Juhannusaatto")
        self.assertEqual(self.holidays[date(2018, 6, 23)],
                         "Juhannuspäivä")


class TestHungary(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.HU()

    def test_2018(self):
        self.assertIn(date(2018, 1, 1), self.holidays)  # newyear
        self.assertIn(date(2018, 3, 15), self.holidays)  # national holiday
        self.assertIn(date(2018, 3, 30), self.holidays)  # good friday
        self.assertIn(date(2018, 4, 1), self.holidays)  # easter 1.
        self.assertIn(date(2018, 4, 2), self.holidays)  # easter 2.
        self.assertIn(date(2018, 5, 1), self.holidays)  # Workers' Day
        self.assertIn(date(2018, 5, 20), self.holidays)  # Pentecost
        self.assertIn(date(2018, 5, 21), self.holidays)  # Pentecost monday
        self.assertIn(date(2018, 8, 20), self.holidays)  # State Foundation Day
        self.assertIn(date(2018, 10, 23), self.holidays)  # National Day
        self.assertIn(date(2018, 11, 1), self.holidays)  # All Saints' Day
        self.assertIn(date(2018, 12, 25), self.holidays)  # First christmas
        self.assertIn(date(2018, 12, 26), self.holidays)  # Second christmas


class TestSwitzerland(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.CH()
        self.prov_hols = dict((prov, holidays.CH(prov=prov))
                              for prov in holidays.CH.PROVINCES)

    def test_all_holidays_present(self):
        ch_2018 = sum(holidays.CH(years=[2018], prov=p)
                      for p in holidays.CH.PROVINCES)
        in_2018 = sum((ch_2018.get_list(key) for key in ch_2018), [])
        all_ch = ['Neujahrestag',
                  'Berchtoldstag',
                  'Heilige Drei Könige',
                  'Jahrestag der Ausrufung der Republik',
                  'Josefstag',
                  'Näfelser Fahrt',
                  'Karfreitag',
                  'Ostern',
                  'Ostermontag',
                  'Tag der Arbeit',
                  'Auffahrt',
                  'Pfingsten',
                  'Pfingstmontag',
                  'Fronleichnam',
                  'Fest der Unabhängigkeit',
                  'Peter und Paul',
                  'Nationalfeiertag',
                  'Maria Himmelfahrt',
                  'Bruder Klaus',
                  'Allerheiligen',
                  'Maria Empfängnis',
                  'Escalade de Genève',
                  'Weihnachten',
                  'Stephanstag',
                  'Wiederherstellung der Republik']

        for holiday in all_ch:
            self.assertTrue(holiday in in_2018, "missing: {}".format(holiday))
        for holiday in in_2018:
            self.assertTrue(holiday in all_ch, "extra: {}".format(holiday))

    def test_fixed_holidays(self):
        fixed_days_whole_country = (
            (1, 1),  # Neujahrestag
            (8, 1),  # Nationalfeiertag
            (12, 25),  # Weihnachten
        )
        for y, (m, d) in product(range(1291, 2050), fixed_days_whole_country):
            self.assertTrue(date(y, m, d) in self.holidays)

    def test_berchtoldstag(self):
        provinces_that_have = {'AG', 'BE', 'FR', 'GE', 'GL', 'GR', 'JU', 'LU',
                               'NE', 'OW', 'SH', 'SO', 'TG', 'VD', 'ZG', 'ZH'}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 1, 2) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 1, 2) not in self.prov_hols[province])

    def test_heilige_drei_koenige(self):
        provinces_that_have = {'SZ', 'TI', 'UR'}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 1, 6) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 1, 6) not in self.prov_hols[province])

    def test_jahrestag_der_ausrufung_der_republik(self):
        provinces_that_have = {'NE'}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 3, 1) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 3, 1) not in self.prov_hols[province])

    def test_josefstag(self):
        provinces_that_have = {'NW', 'SZ', 'TI', 'UR', 'VS'}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 3, 19) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 3, 19) not in self.prov_hols[province])

    def test_naefelser_fahrt(self):
        known_good = [(2018, 4, 5), (2019, 4, 4), (2020, 4, 2),
                      (2021, 4, 8), (2022, 4, 7), (2023, 4, 13),
                      (2024, 4, 4), (2025, 4, 3), (2026, 4, 9),
                      (2027, 4, 1), (2028, 4, 6), (2029, 4, 5),
                      (2030, 4, 4), (2031, 4, 3), (2032, 4, 1),
                      (2033, 4, 7), (2034, 4, 13), (2035, 4, 5)]
        provinces_that_have = {'GL'}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertTrue(date(y, m, d) in self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertTrue(date(y, m, d) not in self.prov_hols[province])

    def test_karfreitag(self):
        known_good = [(2018, 3, 30), (2019, 4, 19), (2020, 4, 10),
                      (2021, 4, 2), (2022, 4, 15), (2023, 4, 7),
                      (2024, 3, 29), (2025, 4, 18), (2026, 4, 3),
                      (2027, 3, 26), (2028, 4, 14), (2029, 3, 30),
                      (2030, 4, 19), (2031, 4, 11), (2032, 3, 26),
                      (2033, 4, 15), (2034, 4, 7), (2035, 3, 23)]
        provinces_that_dont = {'VS'}
        provinces_that_have = set(holidays.CH.PROVINCES) - provinces_that_dont
        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertTrue(date(y, m, d) in self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertTrue(date(y, m, d) not in self.prov_hols[province])

    def test_ostern(self):
        known_good = [(2018, 4, 1), (2019, 4, 21), (2020, 4, 12),
                      (2021, 4, 4), (2022, 4, 17), (2023, 4, 9),
                      (2024, 3, 31), (2025, 4, 20), (2026, 4, 5),
                      (2027, 3, 28), (2028, 4, 16), (2029, 4, 1),
                      (2030, 4, 21), (2031, 4, 13), (2032, 3, 28),
                      (2033, 4, 17), (2034, 4, 9), (2035, 3, 25)]

        for province, (y, m, d) in product(holidays.CH.PROVINCES, known_good):
            self.assertTrue(date(y, m, d) in self.prov_hols[province])

    def test_ostermontag(self):
        known_good = [(2018, 4, 2), (2019, 4, 22), (2020, 4, 13),
                      (2021, 4, 5), (2022, 4, 18), (2023, 4, 10),
                      (2024, 4, 1), (2025, 4, 21), (2026, 4, 6),
                      (2027, 3, 29), (2028, 4, 17), (2029, 4, 2),
                      (2030, 4, 22), (2031, 4, 14), (2032, 3, 29),
                      (2033, 4, 18), (2034, 4, 10), (2035, 3, 26)]
        provinces_that_dont = {'VS'}
        provinces_that_have = set(holidays.CH.PROVINCES) - provinces_that_dont
        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertTrue(date(y, m, d) in self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertTrue(date(y, m, d) not in self.prov_hols[province])

    def test_auffahrt(self):
        known_good = [(2018, 5, 10), (2019, 5, 30), (2020, 5, 21),
                      (2021, 5, 13), (2022, 5, 26), (2023, 5, 18),
                      (2024, 5, 9), (2025, 5, 29), (2026, 5, 14),
                      (2027, 5, 6), (2028, 5, 25), (2029, 5, 10),
                      (2030, 5, 30), (2031, 5, 22), (2032, 5, 6),
                      (2033, 5, 26), (2034, 5, 18), (2035, 5, 3)]

        for province, (y, m, d) in product(holidays.CH.PROVINCES, known_good):
            self.assertTrue(date(y, m, d) in self.prov_hols[province])

    def test_pfingsten(self):
        known_good = [(2018, 5, 20), (2019, 6, 9), (2020, 5, 31),
                      (2021, 5, 23), (2022, 6, 5), (2023, 5, 28),
                      (2024, 5, 19), (2025, 6, 8), (2026, 5, 24),
                      (2027, 5, 16), (2028, 6, 4), (2029, 5, 20),
                      (2030, 6, 9), (2031, 6, 1), (2032, 5, 16),
                      (2033, 6, 5), (2034, 5, 28), (2035, 5, 13)]

        for province, (y, m, d) in product(holidays.CH.PROVINCES, known_good):
            self.assertTrue(date(y, m, d) in self.prov_hols[province])

    def test_pfingstmontag(self):
        known_good = [(2018, 5, 21), (2019, 6, 10), (2020, 6, 1),
                      (2021, 5, 24), (2022, 6, 6), (2023, 5, 29),
                      (2024, 5, 20), (2025, 6, 9), (2026, 5, 25),
                      (2027, 5, 17), (2028, 6, 5), (2029, 5, 21),
                      (2030, 6, 10), (2031, 6, 2), (2032, 5, 17),
                      (2033, 6, 6), (2034, 5, 29), (2035, 5, 14)]

        for province, (y, m, d) in product(holidays.CH.PROVINCES, known_good):
            self.assertTrue(date(y, m, d) in self.prov_hols[province])

    def test_fronleichnam(self):
        known_good = [(2014, 6, 19), (2015, 6, 4), (2016, 5, 26),
                      (2017, 6, 15), (2018, 5, 31), (2019, 6, 20),
                      (2020, 6, 11), (2021, 6, 3), (2022, 6, 16),
                      (2023, 6, 8), (2024, 5, 30)]
        provinces_that_have = {'AI', 'JU', 'LU', 'NW', 'OW', 'SZ', 'TI', 'UR',
                               'VS', 'ZG'}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertTrue(date(y, m, d) in self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertTrue(date(y, m, d) not in self.prov_hols[province])

    def test_fest_der_unabhaengikeit(self):
        provinces_that_have = {'JU'}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 6, 23) in self.prov_hols[province])
        # 2011 is "Fronleichnam" on the same date, we don't test this year
        for province, year in product(provinces_that_dont, range(1970, 2010)):
            self.assertTrue(date(year, 6, 23) not in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(2012, 2050)):
            self.assertTrue(date(year, 6, 23) not in self.prov_hols[province])

    def test_peter_und_paul(self):
        provinces_that_have = {'TI'}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 6, 29) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 6, 29) not in self.prov_hols[province])

    def test_mariae_himmelfahrt(self):
        provinces_that_have = {'AI', 'JU', 'LU', 'NW', 'OW', 'SZ', 'TI', 'UR',
                               'VS', 'ZG'}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 8, 15) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 8, 15) not in self.prov_hols[province])

    def test_bruder_chlaus(self):
        provinces_that_have = {'OW'}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 9, 25) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 9, 25) not in self.prov_hols[province])

    def test_allerheiligen(self):
        provinces_that_have = {'AI', 'GL', 'JU', 'LU', 'NW', 'OW', 'SG', 'SZ',
                               'TI', 'UR', 'VS', 'ZG'}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 11, 1) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 11, 1) not in self.prov_hols[province])

    def test_escalade_de_geneve(self):
        provinces_that_have = {'GE'}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 12, 12) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 12, 12) not in self.prov_hols[province])

    def test_stephanstag(self):
        provinces_that_have = {'AG', 'AR', 'AI', 'BL', 'BS', 'BE', 'FR', 'GL',
                               'GR', 'LU', 'NE', 'NW', 'OW', 'SG', 'SH', 'SZ',
                               'SO', 'TG', 'TI', 'UR', 'ZG', 'ZH'}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 12, 26) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 12, 26) not in self.prov_hols[province])

    def test_wiedererstellung_der_republik(self):
        provinces_that_have = {'GE'}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 12, 31) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 12, 31) not in self.prov_hols[province])


class TestAR(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.AR(observed=True)

    def test_new_years(self):
        self.holidays.observed = False
        self.assertNotIn(date(2010, 12, 31), self.holidays)
        self.assertNotIn(date(2017, 1, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2017, 1, 1), self.holidays)
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_carnival_day(self):
        for dt in [date(2018, 2, 12), date(2018, 2, 13), date(2017, 2, 27),
                   date(2017, 2, 28), date(2016, 2, 8), date(2016, 2, 9)]:
            self.assertIn(dt, self.holidays)

    def test_memory_national_day(self):
        self.holidays.observed = False
        self.assertNotIn(date(1907, 3, 24), self.holidays)
        self.assertNotIn(date(2002, 3, 24), self.holidays)
        self.holidays.observed = True
        for dt in [date(2018, 3, 24), date(2017, 3, 24),
                   date(2016, 3, 24)]:
            self.assertIn(dt, self.holidays)

    def test_holy_week_day(self):
        for dt in [date(2018, 3, 29), date(2018, 3, 30), date(2017, 4, 13),
                   date(2017, 4, 14), date(2016, 3, 24), date(2016, 3, 25)]:
            self.assertIn(dt, self.holidays)

    def test_malvinas_war_day(self):
        for year in range(1900, 2100):
            dt = date(year, 4, 2)
            self.assertIn(dt, self.holidays)

    def test_labor_day(self):
        self.holidays.observerd = False
        self.assertNotIn(date(2010, 4, 30), self.holidays)
        self.assertNotIn(date(2011, 5, 2), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(1922, 5, 1), self.holidays)
        for year in range(1900, 2100):
            dt = date(year, 5, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_may_revolution_day(self):
        self.holidays.observed = False
        self.assertNotIn(date(1930, 5, 25), self.holidays)
        self.assertNotIn(date(2014, 5, 25), self.holidays)
        self.holidays.observed = True
        for year in range(1900, 2100):
            dt = date(year, 5, 1)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_guemes_day(self):
        for year in range(1900, 2100):
            dt = date(year, 6, 17)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_belgrano_day(self):
        for year in range(1900, 2100):
            dt = date(year, 6, 20)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_independence_day(self):
        self.holidays.observed = False
        self.assertNotIn(date(2017, 7, 9), self.holidays)
        self.assertNotIn(date(2011, 7, 9), self.holidays)
        self.holidays.observed = True
        self.assertIn(date(2017, 7, 9), self.holidays)
        self.assertIn(date(2011, 7, 9), self.holidays)
        for year in range(1900, 2100):
            dt = date(year, 7, 9)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_san_martin_day(self):
        self.holidays.observed = False
        self.assertNotIn(date(1930, 8, 10), self.holidays)
        self.assertNotIn(date(2008, 8, 10), self.holidays)
        self.holidays.observed = True
        for year in range(1900, 2100):
            dt = date(year, 8, 17)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_cultural_day(self):
        self.holidays.observed = False
        self.assertNotIn(date(2014, 10, 12), self.holidays)
        self.assertNotIn(date(1913, 10, 12), self.holidays)
        self.holidays.observed = True
        for year in range(1900, 2100):
            dt = date(year, 10, 12)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_national_sovereignty_day(self):
        for year in range(1900, 2100):
            dt = date(year, 11, 20)
            if year < 2010:
                self.assertNotIn(dt, self.holidays)
            else:
                self.assertIn(dt, self.holidays)
                self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
                self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_inmaculate_conception_day(self):
        self.holidays.observed = False
        self.assertNotIn(date(1940, 12, 8), self.holidays)
        self.assertNotIn(date(2013, 12, 8), self.holidays)
        self.holidays.observed = True
        for year in range(1900, 2100):
            dt = date(year, 12, 8)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)

    def test_christmas(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertIn(dt, self.holidays)
            self.assertNotIn(dt + relativedelta(days=-1), self.holidays)
            self.assertNotIn(dt + relativedelta(days=+1), self.holidays)


class TestIND(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.IND()

    def test_2018(self):
        self.assertIn(date(2018, 1, 1), self.holidays)
        self.assertIn(date(2018, 10, 2), self.holidays)
        self.assertIn(date(2018, 8, 15), self.holidays)
        self.assertIn(date(2018, 1, 26), self.holidays)
        self.assertIn(date(2018, 12, 25), self.holidays)
        self.assertIn(date(2018, 5, 1), self.holidays)
        self.assertIn(date(2018, 1, 14), self.holidays)

        gj_holidays = holidays.IND(prov="GJ")
        as_holidays = holidays.IND(prov="AS")
        tn_holidays = holidays.IND(prov="TN")
        wb_holidays = holidays.IND(prov="WB")
        cg_holidays = holidays.IND(prov="CG")
        sk_holidays = holidays.IND(prov="SK")
        ka_holidays = holidays.IND(prov="KA")
        br_holidays = holidays.IND(prov="BR")
        rj_holidays = holidays.IND(prov="RJ")
        od_holidays = holidays.IND(prov="OD")
        ap_holidays = holidays.IND(prov="AP")
        kl_holidays = holidays.IND(prov="KL")
        hr_holidays = holidays.IND(prov="HR")
        mh_holidays = holidays.IND(prov="MH")
        mp_holidays = holidays.IND(prov="MP")
        up_holidays = holidays.IND(prov="UP")
        uk_holidays = holidays.IND(prov="UK")

        for dt in ([date(2018, 1, 14), date(2018, 5, 1), date(2018, 10, 31)]):
            self.assertIn(dt, gj_holidays)
        for dt in [date(2018, 4, 15), date(2018, 4, 14)]:
            self.assertIn(dt, tn_holidays)
            self.assertIn(dt, wb_holidays)
        for dt in ([date(2018, 1, 14), date(2018, 5, 1), date(2018, 10, 31)]):
            self.assertIn(dt, gj_holidays)
        self.assertIn(date(2018, 3, 22), br_holidays)
        self.assertIn(date(2018, 3, 30), rj_holidays)
        self.assertIn(date(2018, 6, 15), rj_holidays)
        self.assertIn(date(2018, 4, 1), od_holidays)
        self.assertIn(date(2018, 4, 15), od_holidays)
        self.assertIn(date(2018, 4, 14), od_holidays)
        self.assertIn(date(2018, 4, 14), br_holidays)
        self.assertIn(date(2018, 4, 14), kl_holidays)
        self.assertIn(date(2018, 4, 14), up_holidays)
        self.assertIn(date(2018, 4, 14), uk_holidays)
        self.assertIn(date(2018, 4, 14), hr_holidays)
        self.assertIn(date(2018, 4, 14), mh_holidays)
        self.assertIn(date(2018, 4, 14), wb_holidays)
        self.assertIn(date(2018, 5, 9), wb_holidays)
        self.assertIn(date(2018, 4, 15), as_holidays)
        self.assertIn(date(2018, 5, 1), mh_holidays)
        self.assertIn(date(2018, 5, 16), sk_holidays)
        self.assertIn(date(2018, 11, 1), ka_holidays)
        self.assertIn(date(2018, 11, 1), ap_holidays)
        self.assertIn(date(2018, 11, 1), hr_holidays)
        self.assertIn(date(2018, 11, 1), mp_holidays)
        self.assertIn(date(2018, 11, 1), kl_holidays)
        self.assertIn(date(2018, 11, 1), cg_holidays)


class TestBelarus(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.BY()

    def test_2018(self):
        # http://calendar.by/procal.php?year=2018
        # https://www.officeholidays.com/countries/belarus/index.php
        self.assertIn(date(2018, 1, 1), self.holidays)
        self.assertIn(date(2018, 1, 7), self.holidays)
        self.assertIn(date(2018, 3, 8), self.holidays)
        self.assertIn(date(2018, 4, 17), self.holidays)
        self.assertIn(date(2018, 5, 1), self.holidays)
        self.assertIn(date(2018, 5, 9), self.holidays)
        self.assertIn(date(2018, 7, 3), self.holidays)
        self.assertIn(date(2018, 11, 7), self.holidays)
        self.assertIn(date(2018, 12, 25), self.holidays)

    def test_radunitsa(self):
        # http://calendar.by/content.php?id=20
        self.assertIn(date(2012, 4, 24), self.holidays)
        self.assertIn(date(2013, 5, 14), self.holidays)
        self.assertIn(date(2014, 4, 29), self.holidays)
        self.assertIn(date(2015, 4, 21), self.holidays)
        self.assertIn(date(2016, 5, 10), self.holidays)
        self.assertIn(date(2017, 4, 25), self.holidays)
        self.assertIn(date(2018, 4, 17), self.holidays)
        self.assertIn(date(2019, 5, 7), self.holidays)
        self.assertIn(date(2020, 4, 28), self.holidays)
        self.assertIn(date(2021, 5, 11), self.holidays)
        self.assertIn(date(2022, 5, 3), self.holidays)
        self.assertIn(date(2023, 4, 25), self.holidays)
        self.assertIn(date(2024, 5, 14), self.holidays)
        self.assertIn(date(2025, 4, 29), self.holidays)
        self.assertIn(date(2026, 4, 21), self.holidays)
        self.assertIn(date(2027, 5, 11), self.holidays)
        self.assertIn(date(2028, 4, 25), self.holidays)
        self.assertIn(date(2029, 4, 17), self.holidays)
        self.assertIn(date(2030, 5, 7), self.holidays)

    def test_before_1998(self):
        self.assertNotIn(date(1997, 7, 3), self.holidays)


class TestCroatia(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.HR()

    def test_2018(self):
        self.assertIn(date(2018, 1, 1), self.holidays)
        self.assertIn(date(2018, 1, 6), self.holidays)
        self.assertIn(date(2018, 4, 1), self.holidays)
        self.assertIn(date(2018, 4, 2), self.holidays)
        self.assertIn(date(2018, 5, 1), self.holidays)
        self.assertIn(date(2018, 8, 15), self.holidays)
        self.assertIn(date(2018, 10, 8), self.holidays)
        self.assertIn(date(2018, 11, 1), self.holidays)
        self.assertIn(date(2018, 12, 25), self.holidays)
        self.assertIn(date(2018, 12, 26), self.holidays)


class TestUkraine(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.UA()

    def test_before_1918(self):
        self.assertNotIn(date(1917, 12, 31), self.holidays)

    def test_2018(self):
        # http://www.buhoblik.org.ua/kadry-zarplata/vremya/1676-1676-kalendar.html
        self.assertIn(date(2018, 1, 1), self.holidays)
        self.assertIn(date(2018, 1, 7), self.holidays)
        self.assertIn(date(2018, 12, 25), self.holidays)
        self.assertIn(date(2018, 4, 8), self.holidays)
        self.assertIn(date(2018, 5, 27), self.holidays)
        self.assertIn(date(2018, 5, 9), self.holidays)
        self.assertIn(date(2018, 6, 28), self.holidays)
        self.assertIn(date(2018, 8, 24), self.holidays)
        self.assertIn(date(2018, 10, 14), self.holidays)

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


class TestBrazil(unittest.TestCase):

    def test_BR_holidays(self):
        self.holidays = holidays.BR(years=2018)
        self.assertIn("2018-01-01", self.holidays)
        self.assertEqual(self.holidays[date(2018, 1, 1)], "Ano novo")
        self.assertIn("2018-02-14", self.holidays)
        self.assertEqual(self.holidays[date(2018, 2, 14)],
                         "Quarta-feira de cinzas (Início da Quaresma)")
        self.assertIn("2018-02-20", self.holidays)
        self.assertEqual(self.holidays[date(2018, 2, 20)], "Carnaval")
        self.assertIn("2018-04-01", self.holidays)
        self.assertEqual(self.holidays[date(2018, 4, 1)], "Páscoa")
        self.assertIn("2018-04-21", self.holidays)
        self.assertEqual(self.holidays[date(2018, 4, 21)], "Tiradentes")
        self.assertIn("2018-05-01", self.holidays)
        self.assertEqual(self.holidays[date(2018, 5, 1)],
                         "Dia Mundial do Trabalho")
        self.assertIn("2018-05-31", self.holidays)
        self.assertEqual(self.holidays[date(2018, 5, 31)], "Corpus Christi")
        self.assertIn("2018-09-07", self.holidays)
        self.assertEqual(self.holidays[date(2018, 9, 7)],
                         "Independência do Brasil")
        self.assertIn("2018-10-12", self.holidays)
        self.assertEqual(self.holidays[date(2018, 10, 12)],
                         "Nossa Senhora Aparecida")
        self.assertIn("2018-11-02", self.holidays)
        self.assertEqual(self.holidays[date(2018, 11, 2)], "Finados")
        self.assertIn("2018-11-15", self.holidays)
        self.assertEqual(self.holidays[date(2018, 11, 15)],
                         "Proclamação da República")
        self.assertIn("2018-12-25", self.holidays)
        self.assertEqual(self.holidays[date(2018, 12, 25)], "Natal")

    def test_AC_holidays(self):
        ac_holidays = holidays.BR(state="AC")
        self.assertIn("2018-01-23", ac_holidays)
        self.assertEqual(ac_holidays[date(2018, 1, 23)], "Dia do evangélico")
        self.assertIn("2018-06-15", ac_holidays)
        self.assertEqual(ac_holidays[date(2018, 6, 15)], "Aniversário do Acre")
        self.assertIn("2018-09-05", ac_holidays)
        self.assertEqual(ac_holidays[date(2018, 9, 5)], "Dia da Amazônia")
        self.assertIn("2018-11-17", ac_holidays)
        self.assertEqual(ac_holidays[date(2018, 11, 17)],
                         "Assinatura do Tratado de Petrópolis")

    def test_AL_holidays(self):
        al_holidays = holidays.BR(state="AL")
        self.assertIn("2018-06-24", al_holidays)
        self.assertEqual(al_holidays[date(2018, 6, 24)], "São João")
        self.assertIn("2018-06-29", al_holidays)
        self.assertEqual(al_holidays[date(2018, 6, 29)], "São Pedro")
        self.assertIn("2018-09-16", al_holidays)
        self.assertEqual(al_holidays[date(2018, 9, 16)],
                         "Emancipação política de Alagoas")
        self.assertIn("2018-11-20", al_holidays)
        self.assertEqual(al_holidays[date(2018, 11, 20)], "Consciência Negra")

    def test_AP_holidays(self):
        ap_holidays = holidays.BR(state="AP")
        self.assertIn("2018-03-19", ap_holidays)
        self.assertEqual(ap_holidays[date(2018, 3, 19)], "Dia de São José")
        self.assertIn("2018-07-25", ap_holidays)
        self.assertEqual(ap_holidays[date(2018, 7, 25)], "São Tiago")
        self.assertIn("2018-10-05", ap_holidays)
        self.assertEqual(ap_holidays[date(2018, 10, 5)], "Criação do estado")
        self.assertIn("2018-11-20", ap_holidays)
        self.assertEqual(ap_holidays[date(2018, 11, 20)], "Consciência Negra")

    def test_AM_holidays(self):
        am_holidays = holidays.BR(state="AM")
        self.assertIn("2018-09-05", am_holidays)
        self.assertEqual(am_holidays[date(2018, 9, 5)],
                         "Elevação do Amazonas à categoria de província")
        self.assertIn("2018-11-20", am_holidays)
        self.assertEqual(am_holidays[date(2018, 11, 20)], "Consciência Negra")
        self.assertIn("2018-12-08", am_holidays)
        self.assertEqual(am_holidays[date(2018, 12, 8)],
                         "Dia de Nossa Senhora da Conceição")

    def test_BA_holidays(self):
        ba_holidays = holidays.BR(state="BA")
        self.assertIn("2018-07-02", ba_holidays)
        self.assertEqual(ba_holidays[date(2018, 7, 2)],
                         "Independência da Bahia")

    def test_CE_holidays(self):
        ce_holidays = holidays.BR(state="CE")
        self.assertIn("2018-03-19", ce_holidays)
        self.assertEqual(ce_holidays[date(2018, 3, 19)], "São José")
        self.assertIn("2018-03-25", ce_holidays)
        self.assertEqual(ce_holidays[date(2018, 3, 25)], "Data Magna do Ceará")

    def test_DF_holidays(self):
        df_holidays = holidays.BR(state="DF")
        self.assertIn("2018-04-21", df_holidays)
        self.assertEqual(df_holidays[date(2018, 4, 21)],
                         "Fundação de Brasília, Tiradentes")
        self.assertIn("2018-11-30", df_holidays)
        self.assertEqual(df_holidays[date(2018, 11, 30)], "Dia do Evangélico")

    def test_ES_holidays(self):
        es_holidays = holidays.BR(state="ES")
        self.assertIn("2018-10-28", es_holidays)
        self.assertEqual(
            es_holidays[date(2018, 10, 28)], "Dia do Servidor Público")

    def test_GO_holidays(self):
        go_holidays = holidays.BR(state="GO")
        self.assertIn("2018-10-28", go_holidays)
        self.assertEqual(
            go_holidays[date(2018, 10, 28)], "Dia do Servidor Público")

    def test_MA_holidays(self):
        ma_holidays = holidays.BR(state="MA")
        self.assertIn("2018-07-28", ma_holidays)
        self.assertEqual(ma_holidays[date(2018, 7, 28)],
                         "Adesão do Maranhão à independência do Brasil")
        self.assertIn("2018-12-08", ma_holidays)
        self.assertEqual(ma_holidays[date(2018, 12, 8)],
                         "Dia de Nossa Senhora da Conceição")

    def test_MT_holidays(self):
        mt_holidays = holidays.BR(state="MT")
        self.assertIn("2018-11-20", mt_holidays)
        self.assertEqual(mt_holidays[date(2018, 11, 20)], "Consciência Negra")

    def test_MS_holidays(self):
        ms_holidays = holidays.BR(state="MS")
        self.assertIn("2018-10-11", ms_holidays)
        self.assertEqual(ms_holidays[date(2018, 10, 11)], "Criação do estado")

    def test_MG_holidays(self):
        mg_holidays = holidays.BR(state="MG")
        self.assertIn("2018-04-21", mg_holidays)
        self.assertEqual(mg_holidays[date(2018, 4, 21)],
                         "Data Magna de MG, Tiradentes")

    def test_PA_holidays(self):
        pa_holidays = holidays.BR(state="PA")
        self.assertIn("2018-08-15", pa_holidays)
        self.assertEqual(pa_holidays[date(2018, 8, 15)],
                         "Adesão do Grão-Pará à independência do Brasil")

    def test_PB_holidays(self):
        pb_holidays = holidays.BR(state="PB")
        self.assertIn("2018-08-05", pb_holidays)
        self.assertEqual(pb_holidays[date(2018, 8, 5)], "Fundação do Estado")

    def test_PE_holidays(self):
        pe_holidays = holidays.BR(state="PE")
        self.assertIn("2018-03-06", pe_holidays)
        self.assertEqual(pe_holidays[date(2018, 3, 6)],
                         "Revolução Pernambucana (Data Magna)")
        self.assertIn("2018-06-24", pe_holidays)
        self.assertEqual(pe_holidays[date(2018, 6, 24)], "São João")

    def test_PI_holidays(self):
        pi_holidays = holidays.BR(state="PI")
        self.assertIn("2018-03-13", pi_holidays)
        self.assertEqual(pi_holidays[date(2018, 3, 13)],
                         "Dia da Batalha do Jenipapo")
        self.assertIn("2018-10-19", pi_holidays)
        self.assertEqual(pi_holidays[date(2018, 10, 19)], "Dia do Piauí")

    def test_RJ_holidays(self):
        rj_holidays = holidays.BR(state="RJ")
        self.assertIn("2018-04-23", rj_holidays)
        self.assertEqual(rj_holidays[date(2018, 4, 23)], "Dia de São Jorge")
        self.assertIn("2018-10-28", rj_holidays)
        self.assertEqual(rj_holidays[date(2018, 10, 28)],
                         "Dia do Funcionário Público")
        self.assertIn("2018-11-20", rj_holidays)
        self.assertEqual(rj_holidays[date(2018, 11, 20)], "Zumbi dos Palmares")

    def test_RN_holidays(self):
        rn_holidays = holidays.BR(state="RN")
        self.assertIn("2018-06-29", rn_holidays)
        self.assertEqual(rn_holidays[date(2018, 6, 29)], "Dia de São Pedro")
        self.assertIn("2018-10-03", rn_holidays)
        self.assertEqual(rn_holidays[date(2018, 10, 3)],
                         "Mártires de Cunhaú e Uruaçuu")

    def test_RS_holidays(self):
        rs_holidays = holidays.BR(state="RS")
        self.assertIn("2018-09-20", rs_holidays)
        self.assertEqual(
            rs_holidays[date(2018, 9, 20)], "Revolução Farroupilha")

    def test_RO_holidays(self):
        ro_holidays = holidays.BR(state="RO")
        self.assertIn("2018-01-04", ro_holidays)
        self.assertEqual(ro_holidays[date(2018, 1, 4)], "Criação do estado")
        self.assertIn("2018-06-18", ro_holidays)
        self.assertEqual(ro_holidays[date(2018, 6, 18)], "Dia do Evangélico")

    def test_RR_holidays(self):
        rr_holidays = holidays.BR(state="RR")
        self.assertIn("2018-10-05", rr_holidays)
        self.assertEqual(rr_holidays[date(2018, 10, 5)], "Criação de Roraima")

    def test_SC_holidays(self):
        sc_holidays = holidays.BR(state="SC")
        self.assertIn("2018-08-11", sc_holidays)
        self.assertEqual(sc_holidays[date(2018, 8, 11)],
                         "Criação da capitania, separando-se de SP")

    def test_SP_holidays(self):
        sp_holidays = holidays.BR(state="SP")
        self.assertIn("2018-07-09", sp_holidays)
        self.assertEqual(sp_holidays[date(2018, 7, 9)],
                         "Revolução Constitucionalista de 1932")

    def test_SE_holidays(self):
        se_holidays = holidays.BR(state="SE")
        self.assertIn("2018-07-08", se_holidays)
        self.assertEqual(se_holidays[date(2018, 7, 8)],
                         "Autonomia política de Sergipe")

    def test_TO_holidays(self):
        to_holidays = holidays.BR(state="TO")
        self.assertIn("2018-01-01", to_holidays)
        self.assertEqual(to_holidays[date(2018, 1, 1)],
                         "Instalação de Tocantins, Ano novo")
        self.assertIn("2018-09-08", to_holidays)
        self.assertEqual(to_holidays[date(2018, 9, 8)],
                         "Nossa Senhora da Natividade")
        self.assertIn("2018-10-05", to_holidays)
        self.assertEqual(to_holidays[date(2018, 10, 5)],
                         "Criação de Tocantins")


if __name__ == "__main__":
    unittest.main()
