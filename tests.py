# -*- coding: utf-8 -*-

#  holidays.py
#  -----------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com>
#  Website: https://github.com/ryanss/holidays.py
#  License: MIT (see LICENSE file)
#  Version: 0.4 (October 4, 2015)


from datetime import date, datetime
from dateutil.relativedelta import relativedelta, MO
import unittest

import holidays


class TestBasics(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.US()

    def test_contains(self):
        self.assertTrue(date(2014, 1, 1) in self.holidays)
        self.assertFalse(date(2014, 1, 2) in self.holidays)

    def test_getitem(self):
        self.assertEqual(self.holidays[date(2014, 1, 1)], "New Year's Day")
        self.assertEqual(self.holidays.get(date(2014, 1, 1)), "New Year's Day")
        self.assertRaises(KeyError, lambda: self.holidays[date(2014, 1, 2)])
        self.assertEqual(self.holidays.get(date(2014, 1, 2)), None)

    def test_get(self):
        self.assertEqual(self.holidays.get('2014-01-01'), "New Year's Day")
        self.assertEqual(self.holidays.get('2014-01-02'), None)
        self.assertFalse(self.holidays.get('2014-01-02', False))
        self.assertTrue(self.holidays.get('2014-01-02', True))

    def test_pop(self):
        self.assertRaises(KeyError, lambda: self.holidays.pop('2014-01-02'))
        self.assertFalse(self.holidays.pop('2014-01-02', False))
        self.assertTrue(self.holidays.pop('2014-01-02', True))
        self.assertTrue(date(2014, 1, 1) in self.holidays)
        self.assertEqual(self.holidays.pop('2014-01-01'), "New Year's Day")
        self.assertFalse(date(2014, 1, 1) in self.holidays)
        self.assertTrue(date(2014, 7, 4) in self.holidays)

    def test_setitem(self):
        self.holidays = holidays.US(years=[2014])
        self.assertEqual(len(self.holidays), 10)
        self.holidays[date(2014, 1, 3)] = "Fake Holiday"
        self.assertEqual(len(self.holidays), 11)
        self.assertTrue(date(2014, 1, 3) in self.holidays)
        self.assertEqual(self.holidays.get(date(2014, 1, 3)), "Fake Holiday")

    def test_update(self):
        h = holidays.HolidayBase()
        h.update({
            date(2015, 1, 1): "New Year's Day",
            '2015-12-25': "Christmas Day",
        })
        self.assertTrue('2015-01-01' in h)
        self.assertTrue(date(2015, 12, 25) in h)

    def test_append(self):
        h = holidays.HolidayBase()
        h.update({
            date(2015, 1, 1): "New Year's Day",
            '2015-12-25': "Christmas Day",
        })
        h.append([date(2015, 4, 1), '2015-04-03'])
        h.append(date(2015, 4, 6))
        h.append('2015-04-07')
        self.assertTrue('2015-01-01' in h)
        self.assertTrue(date(2015, 12, 25) in h)
        self.assertTrue('2015-04-01' in h)
        self.assertFalse('2015-04-02' in h)
        self.assertTrue('2015-04-03' in h)
        self.assertFalse('2015-04-04' in h)
        self.assertFalse('2015-04-05' in h)
        self.assertTrue('2015-04-06' in h)
        self.assertTrue('2015-04-07' in h)

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
        self.assertTrue(us1 != us3)

    def test_add(self):
        ca = holidays.CA()
        us = holidays.US()
        mx = holidays.MX()
        na = ca + (us + mx)
        self.assertFalse('2014-07-01' in us)
        self.assertTrue('2014-07-01' in ca)
        self.assertFalse('2014-07-04' in ca)
        self.assertTrue('2014-07-04' in us)
        self.assertTrue('2014-07-04' in ca+us)
        self.assertTrue('2014-07-04' in us+ca)
        self.assertTrue('2015-07-04' in ca+us)
        self.assertTrue('2015-07-04' in us+ca)
        self.assertTrue('2015-07-01' in ca+us)
        self.assertTrue('2015-07-01' in us+ca)
        self.assertTrue('2014-07-04' in na)
        self.assertTrue('2015-07-04' in na)
        self.assertTrue('2015-07-01' in na)
        self.assertTrue('2000-02-05' in na)
        self.assertEqual((ca+us).prov, 'ON')
        self.assertEqual((us+ca).prov, 'ON')
        ca = holidays.CA(years=[2014], expand=False)
        us = holidays.US(years=[2014, 2015], expand=True)
        self.assertTrue((ca+us).expand)
        self.assertEqual((ca+us).years, set([2014, 2015]))
        self.assertEqual((us+ca).years, set([2014, 2015]))
        na = holidays.CA()
        na += holidays.US()
        na += holidays.MX()
        self.assertEqual(na.country, ['CA', 'US', 'MX'])
        self.assertTrue('2014-07-04' in na)
        self.assertTrue('2014-07-04' in na)
        self.assertTrue('2015-07-04' in na)
        self.assertTrue('2015-07-04' in na)
        self.assertTrue('2015-07-01' in na)
        self.assertTrue('2015-07-01' in na)
        self.assertTrue('2000-02-05' in na)
        self.assertEqual(na.prov, 'ON')
        na = holidays.CA() + holidays.US()
        na += holidays.MX()
        self.assertTrue('2014-07-04' in na)
        self.assertTrue('2014-07-04' in na)
        self.assertTrue('2015-07-04' in na)
        self.assertTrue('2015-07-04' in na)
        self.assertTrue('2015-07-01' in na)
        self.assertTrue('2015-07-01' in na)
        self.assertTrue('2000-02-05' in na)
        self.assertEqual(na.prov, 'ON')
        self.assertRaises(TypeError, lambda: holidays.US() + {})
        na = ca + (us + mx) + ca + (mx + us + holidays.CA(prov='BC'))
        self.assertTrue('2000-02-05' in na)
        self.assertTrue('2014-02-10' in na)
        self.assertTrue('2014-02-17' in na)
        self.assertTrue('2014-07-04' in na)
        provs = (holidays.CA(prov='ON', years=[2014]) +
                 holidays.CA(prov='BC', years=[2015]))
        self.assertTrue("2015-02-09" in provs)
        self.assertTrue("2015-02-16" in provs)
        self.assertEqual(provs.prov, ['ON', 'BC'])
        a = sum([holidays.CA(prov=x) for x in holidays.CA.PROVINCES])
        self.assertEqual(a.country, 'CA')
        self.assertEqual(a.prov, holidays.CA.PROVINCES)
        self.assertTrue("2015-02-09" in a)
        self.assertTrue("2015-02-16" in a)
        na = holidays.CA() + holidays.US() + holidays.MX()
        self.assertTrue(date(1969, 12, 25) in na)
        self.assertEqual(na.get(date(1969, 7, 1)), "Canada Day")
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
        self.assertTrue(date(1969, 12, 25) in na)
        self.assertEqual(na.get_list(date(1969, 12, 25)),
                         ["Christmas Day", "Navidad [Christmas]"])
        self.assertEqual(na.get_list(date(1969, 7, 1)), ["Canada Day"])
        self.assertEqual(na.get_list(date(1969, 1, 3)), [])

    def test_radd(self):
        self.assertRaises(TypeError, lambda: 1 + holidays.US())

    def test_inheritance(self):
        class NoColumbusHolidays(holidays.US):
            def _populate(self, year):
                holidays.US._populate(self, year)
                self.pop(date(year, 10, 1) + relativedelta(weekday=MO(+2)))
        hdays = NoColumbusHolidays()
        self.assertTrue(date(2014, 10, 13) in self.holidays)
        self.assertFalse(date(2014, 10, 13) in hdays)
        self.assertTrue(date(2014, 1, 1) in hdays)
        self.assertTrue(date(2020, 10, 12) in self.holidays)
        self.assertFalse(date(2020, 10, 12) in hdays)
        self.assertTrue(date(2020, 1, 1) in hdays)

        class NinjaTurtlesHolidays(holidays.US):
            def _populate(self, year):
                holidays.US._populate(self, year)
                self[date(year, 7, 13)] = "Ninja Turtle's Day"
        hdays = NinjaTurtlesHolidays()
        self.assertFalse(date(2014, 7, 13) in self.holidays)
        self.assertTrue(date(2014, 7, 13) in hdays)
        self.assertTrue(date(2014, 1, 1) in hdays)
        self.assertFalse(date(2020, 7, 13) in self.holidays)
        self.assertTrue(date(2020, 7, 13) in hdays)
        self.assertTrue(date(2020, 1, 1) in hdays)

        class NewCountry(holidays.HolidayBase):
            def _populate(self, year):
                self[date(year, 1, 2)] = "New New Year's"
        hdays = NewCountry()
        self.assertFalse(date(2014, 1, 1) in hdays)
        self.assertTrue(date(2014, 1, 2) in hdays)

        class Dec31Holiday(holidays.HolidayBase):
            def _populate(self, year):
                self[date(year, 12, 31)] = "New Year's Eve"
        self.assertTrue(date(2014, 12, 31) in Dec31Holiday())


class TestArgs(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.US()

    def test_country(self):
        self.assertEqual(self.holidays.country, 'US')
        self.assertTrue(date(2014, 7, 4) in self.holidays)
        self.assertFalse(date(2014, 7, 1) in self.holidays)
        self.holidays = holidays.UnitedStates()
        self.assertEqual(self.holidays.country, 'US')
        self.assertTrue(date(2014, 7, 4) in self.holidays)
        self.assertFalse(date(2014, 7, 1) in self.holidays)
        self.assertEqual(self.holidays.country, 'US')
        self.holidays = holidays.CA()
        self.assertEqual(self.holidays.country, 'CA')
        self.assertEqual(self.holidays.prov, 'ON')
        self.assertTrue(date(2014, 7, 1) in self.holidays)
        self.assertFalse(date(2014, 7, 4) in self.holidays)
        self.holidays = holidays.CA(prov='BC')
        self.assertEqual(self.holidays.country, 'CA')
        self.assertEqual(self.holidays.prov, 'BC')
        self.assertTrue(date(2014, 7, 1) in self.holidays)
        self.assertFalse(date(2014, 7, 4) in self.holidays)

    def test_years(self):
        self.assertEqual(len(self.holidays.years), 0)
        self.assertFalse(date(2014, 1, 2) in self.holidays)
        self.assertEqual(len(self.holidays.years), 1)
        self.assertTrue(2014 in self.holidays.years)
        self.assertFalse(date(2013, 1, 2) in self.holidays)
        self.assertFalse(date(2014, 1, 2) in self.holidays)
        self.assertFalse(date(2015, 1, 2) in self.holidays)
        self.assertEqual(len(self.holidays.years), 3)
        self.assertTrue(2013 in self.holidays.years)
        self.assertTrue(2015 in self.holidays.years)
        self.holidays = holidays.US(years=range(2010, 2015+1))
        self.assertEqual(len(self.holidays.years), 6)
        self.assertFalse(2009 in self.holidays.years)
        self.assertTrue(2010 in self.holidays.years)
        self.assertTrue(2015 in self.holidays.years)
        self.assertFalse(2016 in self.holidays.years)
        self.holidays = holidays.US(years=(2013, 2015, 2015))
        self.assertEqual(len(self.holidays.years), 2)
        self.assertTrue(2013 in self.holidays.years)
        self.assertFalse(2014 in self.holidays.years)
        self.assertTrue(2015 in self.holidays.years)
        self.assertTrue(date(2021, 12, 31) in holidays.US(years=[2022]).keys())
        self.holidays = holidays.US(years=2015)
        self.assertFalse(2014 in self.holidays.years)
        self.assertTrue(2015 in self.holidays.years)

    def test_expand(self):
        self.holidays = holidays.US(years=(2013, 2015), expand=False)
        self.assertEqual(len(self.holidays.years), 2)
        self.assertTrue(2013 in self.holidays.years)
        self.assertFalse(2014 in self.holidays.years)
        self.assertTrue(2015 in self.holidays.years)
        self.assertFalse(date(2014, 1, 1) in self.holidays)
        self.assertEqual(len(self.holidays.years), 2)
        self.assertFalse(2014 in self.holidays.years)

    def test_observed(self):
        self.holidays = holidays.US(observed=False)
        self.assertTrue(date(2000, 1, 1) in self.holidays)
        self.assertFalse(date(1999, 12, 31) in self.holidays)
        self.assertTrue(date(2012, 1, 1) in self.holidays)
        self.assertFalse(date(2012, 1, 2) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2000, 1, 1) in self.holidays)
        self.assertTrue(date(1999, 12, 31) in self.holidays)
        self.assertTrue(date(2012, 1, 1) in self.holidays)
        self.assertTrue(date(2012, 1, 2) in self.holidays)
        self.holidays.observed = False
        self.assertTrue(date(2000, 1, 1) in self.holidays)
        self.assertFalse(date(1999, 12, 31) in self.holidays)
        self.assertTrue(date(2012, 1, 1) in self.holidays)
        self.assertFalse(date(2012, 1, 2) in self.holidays)
        self.holidays = holidays.US(years=[2022], observed=False)
        self.assertFalse(date(2021, 12, 31) in self.holidays.keys())


class TestKeyTransforms(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.US()

    def test_dates(self):
        self.assertTrue(date(2014, 1, 1) in self.holidays)
        self.assertEqual(self.holidays[date(2014, 1, 1)], "New Year's Day")
        self.holidays[date(2014, 1, 3)] = "Fake Holiday"
        self.assertTrue(date(2014, 1, 3) in self.holidays)
        self.assertTrue(self.holidays.pop(date(2014, 1, 3)), "Fake Holiday")
        self.assertFalse(date(2014, 1, 3) in self.holidays)

    def test_datetimes(self):
        self.assertTrue(datetime(2014, 1, 1, 13, 45) in self.holidays)
        self.assertEqual(self.holidays[datetime(2014, 1, 1, 13, 45)],
                         "New Year's Day")
        self.holidays[datetime(2014, 1, 3, 1, 1)] = "Fake Holiday"
        self.assertTrue(datetime(2014, 1, 3, 2, 2) in self.holidays)
        self.assertTrue(self.holidays.pop(datetime(2014, 1, 3, 4, 4)),
                        "Fake Holiday")
        self.assertFalse(datetime(2014, 1, 3, 2, 2) in self.holidays)

    def test_timestamp(self):
        self.assertTrue(1388552400 in self.holidays)
        self.assertEqual(self.holidays[1388552400], "New Year's Day")
        self.assertTrue(1388552400.01 in self.holidays)
        self.assertEqual(self.holidays[1388552400.01], "New Year's Day")
        self.holidays[1388725200] = "Fake Holiday"
        self.assertTrue(1388725201 in self.holidays)
        self.assertTrue(self.holidays.pop(1388725202), "Fake Holiday")
        self.assertFalse(1388725201 in self.holidays)

    def test_strings(self):
        self.assertTrue("2014-01-01" in self.holidays)
        self.assertEqual(self.holidays["2014-01-01"], "New Year's Day")
        self.assertTrue("01/01/2014" in self.holidays)
        self.assertEqual(self.holidays["01/01/2014"], "New Year's Day")
        self.holidays["01/03/2014"] = "Fake Holiday"
        self.assertTrue("01/03/2014" in self.holidays)
        self.assertTrue(self.holidays.pop("01/03/2014"), "Fake Holiday")
        self.assertFalse("01/03/2014" in self.holidays)

    def test_exceptions(self):
        self.assertRaises(ValueError, lambda: "abc" in self.holidays)
        self.assertRaises(ValueError, lambda: self.holidays.get("abc123"))
        self.assertRaises(ValueError, self.holidays.__setitem__, "abc", "Test")
        self.assertRaises(TypeError, lambda: list() in self.holidays)


class TestCA(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.CA(observed=False)

    def test_new_years(self):
        self.assertFalse(date(2010, 12, 31) in self.holidays)
        self.assertFalse(date(2017,  1,  2) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2010, 12, 31) in self.holidays)
        self.assertTrue(date(2017,  1,  2) in self.holidays)
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

    def test_islander_day(self):
        pei_holidays = holidays.CA(prov="PE")
        for dt in [date(2009, 2,  9), date(2010, 2, 15), date(2011, 2, 21),
                   date(2012, 2, 20), date(2013, 2, 18), date(2014, 2, 17),
                   date(2015, 2, 16), date(2016, 2, 15), date(2020, 2, 17)]:
            if dt.year >= 2010:
                self.assertNotEqual(self.holidays[dt], "Islander Day")
            elif dt.year == 2009:
                self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in pei_holidays)
            self.assertFalse(dt + relativedelta(days=-1) in pei_holidays)
            self.assertFalse(dt + relativedelta(days=+1) in pei_holidays)

    def test_family_day(self):
        ab_holidays = holidays.CA(prov="AB")
        bc_holidays = holidays.CA(prov="BC")
        mb_holidays = holidays.CA(prov="MB")
        sk_holidays = holidays.CA(prov="SK")
        for dt in [date(1990, 2, 19), date(1999, 2, 15), date(2000, 2, 21),
                   date(2006, 2, 20)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in ab_holidays)
            self.assertFalse(dt in bc_holidays)
            self.assertFalse(dt in mb_holidays)
            self.assertFalse(dt in sk_holidays)
        dt = date(2007, 2, 19)
        self.assertFalse(dt in self.holidays)
        self.assertTrue(dt in ab_holidays)
        self.assertFalse(dt in bc_holidays)
        self.assertFalse(dt in mb_holidays)
        self.assertTrue(dt in sk_holidays)
        for dt in [date(2008, 2, 18), date(2012, 2, 20), date(2014, 2, 17),
                   date(2018, 2, 19), date(2019, 2, 18), date(2020, 2, 17)]:
            self.assertTrue(dt in self.holidays)
            self.assertTrue(dt in ab_holidays)
            self.assertFalse(dt in bc_holidays)
            self.assertTrue(dt in mb_holidays)
            self.assertTrue(dt in sk_holidays)
        for dt in [date(2013, 2, 11), date(2016, 2, 8), date(2020, 2, 10)]:
            self.assertFalse(dt in self.holidays)
            self.assertFalse(dt in ab_holidays)
            self.assertTrue(dt in bc_holidays)
            self.assertFalse(dt in mb_holidays)
            self.assertFalse(dt in sk_holidays)
        self.assertEqual(mb_holidays[date(2014, 2, 17)], "Louis Riel Day")

    def test_st_patricks_day(self):
        nl_holidays = holidays.CA(prov="NL", observed=False)
        for dt in [date(1900, 3, 19), date(1999, 3, 15), date(2000, 3, 20),
                   date(2012, 3, 19), date(2013, 3, 18), date(2014, 3, 17),
                   date(2015, 3, 16), date(2016, 3, 14), date(2020, 3, 16)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in nl_holidays)
            self.assertFalse(dt + relativedelta(days=-1) in nl_holidays)
            self.assertFalse(dt + relativedelta(days=+1) in nl_holidays)

    def test_good_friday(self):
        qc_holidays = holidays.CA(prov="QC")
        for dt in [date(1900, 4, 13), date(1901, 4,  5), date(1902, 3, 28),
                   date(1999, 4,  2), date(2000, 4, 21), date(2010, 4,  2),
                   date(2018, 3, 30), date(2019, 4, 19), date(2020, 4, 10)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)
            self.assertFalse(dt in qc_holidays)

    def test_easter_monday(self):
        qc_holidays = holidays.CA(prov="QC")
        for dt in [date(1900, 4, 16), date(1901, 4,  8), date(1902, 3, 31),
                   date(1999, 4,  5), date(2000, 4, 24), date(2010, 4,  5),
                   date(2018, 4,  2), date(2019, 4, 22), date(2020, 4, 13)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in qc_holidays)
            self.assertFalse(dt + relativedelta(days=-1) in qc_holidays)
            self.assertFalse(dt + relativedelta(days=+1) in qc_holidays)

    def test_st_georges_day(self):
        nl_holidays = holidays.CA(prov="NL")
        for dt in [date(1990, 4, 23), date(1999, 4, 26), date(2000, 4, 24),
                   date(2010, 4, 19), date(2016, 4, 25), date(2020, 4, 20)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in nl_holidays)
            self.assertFalse(dt + relativedelta(days=-1) in nl_holidays)
            self.assertFalse(dt + relativedelta(days=+1) in nl_holidays)

    def test_victoria_day(self):
        for dt in [date(1953, 5, 18), date(1999, 5, 24), date(2000, 5, 22),
                   date(2010, 5, 24), date(2015, 5, 18), date(2020, 5, 18)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

    def test_national_aboriginal_day(self):
        nt_holidays = holidays.CA(prov="NT")
        self.assertFalse(date(1995, 6, 21) in nt_holidays)
        for year in range(1996, 2100):
            dt = date(year, 6, 21)
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in nt_holidays)
            self.assertFalse(dt + relativedelta(days=-1) in nt_holidays)
            self.assertFalse(dt + relativedelta(days=+1) in nt_holidays)

    def test_st_jean_baptiste_day(self):
        qc_holidays = holidays.CA(prov="QC", observed=False)
        self.assertFalse(date(1924, 6, 24) in qc_holidays)
        for year in range(1925, 2100):
            dt = date(year, 6, 24)
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in qc_holidays)
            self.assertFalse(dt + relativedelta(days=-1) in qc_holidays)
            self.assertFalse(dt + relativedelta(days=+1) in qc_holidays)
        self.assertFalse(date(2001, 6, 25) in qc_holidays)
        qc_holidays.observed = True
        self.assertTrue(date(2001, 6, 25) in qc_holidays)

    def test_discovery_day(self):
        nl_holidays = holidays.CA(prov="NL")
        yu_holidays = holidays.CA(prov="YU")
        for dt in [date(1997, 6, 23), date(1999, 6, 21), date(2000, 6, 26),
                   date(2010, 6, 21), date(2016, 6, 27), date(2020, 6, 22)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in nl_holidays)
            self.assertFalse(dt in yu_holidays)
        for dt in [date(1912, 8, 19), date(1999, 8, 16), date(2000, 8, 21),
                   date(2006, 8, 21), date(2016, 8, 15), date(2020, 8, 17)]:
            self.assertFalse(dt in self.holidays)
            self.assertFalse(dt in nl_holidays)
            self.assertTrue(dt in yu_holidays)

    def test_canada_day(self):
        for year in range(1900, 2100):
            dt = date(year, 7, 1)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)
        self.assertFalse(date(2006, 7, 3) in self.holidays)
        self.assertFalse(date(2007, 7, 2) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2006, 7, 3) in self.holidays)
        self.assertTrue(date(2007, 7, 2) in self.holidays)

    def test_nunavut_day(self):
        nu_holidays = holidays.CA(prov="NU", observed=False)
        self.assertFalse(date(1999, 7, 9) in nu_holidays)
        self.assertFalse(date(2000, 7, 9) in nu_holidays)
        self.assertTrue(date(2000, 4, 1) in nu_holidays)
        for year in range(2001, 2100):
            dt = date(year, 7, 9)
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in nu_holidays)
            self.assertFalse(dt + relativedelta(days=-1) in nu_holidays)
            self.assertFalse(dt + relativedelta(days=+1) in nu_holidays)
        self.assertFalse(date(2017, 7, 10) in nu_holidays)
        nu_holidays.observed = True
        self.assertTrue(date(2017, 7, 10) in nu_holidays)

    def test_civic_holiday(self):
        bc_holidays = holidays.CA(prov="BC")
        for dt in [date(1900, 8, 6), date(1955, 8, 1), date(1973, 8, 6)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt in bc_holidays)
        for dt in [date(1974, 8, 5), date(1999, 8, 2), date(2000, 8, 7),
                   date(2010, 8, 2), date(2015, 8, 3), date(2020, 8, 3)]:
            self.assertTrue(dt in self.holidays)
            self.assertTrue(dt in bc_holidays)

    def test_labour_day(self):
        self.assertFalse(date(1893, 9, 4) in self.holidays)
        for dt in [date(1894, 9, 3), date(1900, 9, 3), date(1999, 9, 6),
                   date(2000, 9, 4), date(2014, 9, 1), date(2015, 9, 7)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

    def test_thanksgiving(self):
        ns_holidays = holidays.CA(prov="NB")
        for dt in [date(1931, 10, 12), date(1990, 10,  8), date(1999, 10, 11),
                   date(2000, 10,  9), date(2013, 10, 14), date(2020, 10, 12)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)
            self.assertFalse(dt in ns_holidays)

    def test_remembrance_day(self):
        ab_holidays = holidays.CA(prov="AB", observed=False)
        nl_holidays = holidays.CA(prov="NL", observed=False)
        self.assertFalse(date(1930, 11, 11) in ab_holidays)
        self.assertFalse(date(1930, 11, 11) in nl_holidays)
        for year in range(1931, 2100):
            dt = date(year, 11, 11)
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in ab_holidays)
            self.assertTrue(dt in nl_holidays)
            self.assertFalse(dt + relativedelta(days=-1) in nl_holidays)
            self.assertFalse(dt + relativedelta(days=+1) in nl_holidays)
        self.assertFalse(date(2007, 11, 12) in ab_holidays)
        self.assertFalse(date(2007, 11, 12) in nl_holidays)
        ab_holidays.observed = True
        nl_holidays.observed = True
        self.assertFalse(date(2007, 11, 12) in ab_holidays)
        self.assertTrue(date(2007, 11, 12) in nl_holidays)

    def test_christmas_day(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
        self.assertFalse(date(2010, 12, 24) in self.holidays)
        self.assertNotEqual(self.holidays[date(2011, 12, 26)],
                            "Christmas Day (Observed)")
        self.holidays.observed = True
        self.assertTrue(date(2010, 12, 24) in self.holidays)
        self.assertEqual(self.holidays[date(2011, 12, 26)],
                         "Christmas Day (Observed)")

    def test_boxing_day(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 26)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)
        self.assertFalse(date(2009, 12, 28) in self.holidays)
        self.assertFalse(date(2010, 12, 27) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2009, 12, 28) in self.holidays)
        self.assertTrue(date(2010, 12, 27) in self.holidays)


class TestMX(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.MX(observed=False)

    def test_new_years(self):
        self.assertFalse(date(2010, 12, 31) in self.holidays)
        self.assertFalse(date(2017,  1,  2) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2010, 12, 31) in self.holidays)
        self.assertTrue(date(2017,  1,  2) in self.holidays)
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

    def test_constitution_day(self):
        for dt in [date(2005, 2, 5), date(2006, 2, 5), date(2007, 2, 5),
                   date(2008, 2, 4), date(2009, 2, 2), date(2010, 2, 1),
                   date(2015, 2, 2), date(2016, 2, 1), date(2020, 2, 3)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

    def test_benito_juarez(self):
        for dt in [date(2005, 3, 21), date(2006, 3, 21), date(2007, 3, 19),
                   date(2008, 3, 17), date(2009, 3, 16), date(2010, 3, 15),
                   date(2015, 3, 16), date(2016, 3, 21), date(2020, 3, 16)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

    def test_labor_day(self):
        self.assertFalse(date(2010, 4, 30) in self.holidays)
        self.assertFalse(date(2011, 5,  2) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2010, 4, 30) in self.holidays)
        self.assertTrue(date(2011, 5,  2) in self.holidays)
        self.holidays.observed = False
        self.assertFalse(date(1922, 5, 1) in self.holidays)
        for year in range(1923, 2100):
            dt = date(year, 5, 1)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

    def test_independence_day(self):
        self.assertFalse(date(2006, 9, 15) in self.holidays)
        self.assertFalse(date(2007, 9, 17) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2006, 9, 15) in self.holidays)
        self.assertTrue(date(2007, 9, 17) in self.holidays)
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 9, 16)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

    def test_revolution_day(self):
        for dt in [date(2005, 11, 20), date(2006, 11, 20), date(2007, 11, 19),
                   date(2008, 11, 17), date(2009, 11, 16), date(2010, 11, 15),
                   date(2015, 11, 16), date(2016, 11, 21), date(2020, 11, 16)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

    def test_change_of_government(self):
        self.assertFalse(date(2012, 11, 30) in self.holidays)
        self.assertFalse(date(2024, 12,  2) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2012, 11, 30) in self.holidays)
        self.assertTrue(date(2024, 12,  2) in self.holidays)
        self.holidays.observed = False
        for year in range(1970, 2100):
            dt = date(year, 12, 1)
            if (2018 - year) % 6 == 0:
                self.assertTrue(dt in self.holidays)
                self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
                self.assertFalse(dt + relativedelta(days=+1) in self.holidays)
            else:
                self.assertFalse(dt in self.holidays)

    def test_christmas(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)
        self.assertFalse(date(2010, 12, 24) in self.holidays)
        self.assertFalse(date(2016, 12, 26) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2010, 12, 24) in self.holidays)
        self.assertTrue(date(2016, 12, 26) in self.holidays)


class TestUS(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.US(observed=False)

    def test_new_years(self):
        self.assertFalse(date(2010, 12, 31) in self.holidays)
        self.assertFalse(date(2017,  1,  2) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2010, 12, 31) in self.holidays)
        self.assertTrue(date(2017,  1,  2) in self.holidays)
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

    def test_epiphany(self):
        pr_holidays = holidays.US(state='PR')
        for year in range(2010, 2021):
            self.assertFalse(date(year, 1, 6) in self.holidays)
            self.assertTrue(date(year, 1, 6) in pr_holidays)

    def test_three_kings_day(self):
        vi_holidays = holidays.US(state='VI')
        for year in range(2010, 2021):
            self.assertFalse(date(year, 1, 6) in self.holidays)
            self.assertTrue(date(year, 1, 6) in vi_holidays)

    def test_lee_jackson_day(self):
        va_holidays = holidays.US(state='VA')
        self.assertFalse(date(1888, 1, 19) in va_holidays)
        self.assertFalse(date(1983, 1, 19) in va_holidays)
        self.assertFalse("Lee Jackson Day"
                         in va_holidays.get_list(date(2000, 1, 17)))
        for dt in [date(1889, 1, 19), date(1982, 1, 19), date(1983, 1, 17),
                   date(1999, 1, 18), date(2000, 1, 14), date(2001, 1, 12),
                   date(2013, 1, 18), date(2014, 1, 17), date(2018, 1, 12)]:
            self.assertFalse("Lee Jackson Day" in self.holidays.get_list(dt))
            self.assertTrue(dt in va_holidays)
            self.assertTrue("Lee Jackson Day" in va_holidays.get_list(dt))

    def test_inauguration_day(self):
        name = "Inauguration Day"
        dc_holidays = holidays.US(state='DC')
        la_holidays = holidays.US(state='LA')
        md_holidays = holidays.US(state='MD')
        va_holidays = holidays.US(state='VA')
        for year in (1789, 1793, 1877, 1929, 1933):
            self.assertFalse(name in self.holidays.get_list(date(year, 3, 4)))
            self.assertTrue(name in dc_holidays.get_list(date(year, 3, 4)))
            self.assertTrue(name in la_holidays.get_list(date(year, 3, 4)))
            self.assertTrue(name in md_holidays.get_list(date(year, 3, 4)))
            self.assertTrue(name in va_holidays.get_list(date(year, 3, 4)))
        for year in (1937, 1941, 1957, 2013, 2017):
            self.assertFalse(name in self.holidays.get_list(date(year, 1, 20)))
            self.assertTrue(name in dc_holidays.get_list(date(year, 1, 20)))
            self.assertTrue(name in la_holidays.get_list(date(year, 1, 20)))
            self.assertTrue(name in md_holidays.get_list(date(year, 1, 20)))
            self.assertTrue(name in va_holidays.get_list(date(year, 1, 20)))
        for year in (1785, 1788, 2010, 2011, 2012, 2014, 2015, 2016):
            self.assertFalse(name in dc_holidays.get_list(date(year, 3, 4)))
            self.assertFalse(name in la_holidays.get_list(date(year, 3, 4)))
            self.assertFalse(name in md_holidays.get_list(date(year, 3, 4)))
            self.assertFalse(name in va_holidays.get_list(date(year, 3, 4)))
            self.assertFalse(name in dc_holidays.get_list(date(year, 1, 20)))
            self.assertFalse(name in la_holidays.get_list(date(year, 1, 20)))
            self.assertFalse(name in md_holidays.get_list(date(year, 1, 20)))
            self.assertFalse(name in va_holidays.get_list(date(year, 1, 20)))

    def test_marthin_luther(self):
        for dt in [date(1986, 1, 20), date(1999, 1, 18), date(2000, 1, 17),
                   date(2012, 1, 16), date(2013, 1, 21), date(2014, 1, 20),
                   date(2015, 1, 19), date(2016, 1, 18), date(2020, 1, 20)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)
        self.assertFalse("Martin Luther King, Jr. Day"
                         in holidays.US(years=[1985]).values())
        self.assertTrue("Martin Luther King, Jr. Day"
                        in holidays.US(years=[1986]).values())
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
            self.assertFalse(date(year, 2, 12) in self.holidays)
            self.assertTrue(date(year, 2, 12) in ca_holidays)
            self.assertTrue(date(year, 2, 12) in ct_holidays)
            self.assertTrue(date(year, 2, 12) in il_holidays)
            self.assertTrue(date(year, 2, 12) in ia_holidays)
            self.assertTrue(date(year, 2, 12) in nj_holidays)
            self.assertTrue(date(year, 2, 12) in ny_holidays)
            if date(year, 2, 12).weekday() == 5:
                self.assertFalse(date(year, 2, 11) in self.holidays)
                self.assertTrue(date(year, 2, 11) in ca_holidays)
                self.assertTrue(date(year, 2, 11) in ct_holidays)
                self.assertTrue(date(year, 2, 11) in il_holidays)
                self.assertTrue(date(year, 2, 11) in ia_holidays)
                self.assertTrue(date(year, 2, 11) in nj_holidays)
                self.assertTrue(date(year, 2, 11) in ny_holidays)
            else:
                self.assertFalse(date(year, 2, 11) in ca_holidays)
                self.assertFalse(date(year, 2, 11) in ct_holidays)
                self.assertFalse(date(year, 2, 11) in il_holidays)
                self.assertFalse(date(year, 2, 11) in ia_holidays)
                self.assertFalse(date(year, 2, 11) in nj_holidays)
                self.assertFalse(date(year, 2, 11) in ny_holidays)
            if date(year, 2, 12).weekday() == 6:
                self.assertFalse(date(year, 2, 13) in self.holidays)
                self.assertTrue(date(year, 2, 13) in ca_holidays)
                self.assertTrue(date(year, 2, 13) in ct_holidays)
                self.assertTrue(date(year, 2, 13) in il_holidays)
                self.assertTrue(date(year, 2, 13) in ia_holidays)
                self.assertTrue(date(year, 2, 13) in nj_holidays)
                self.assertTrue(date(year, 2, 13) in ny_holidays)
            else:
                self.assertFalse(date(year, 2, 13) in ca_holidays)
                self.assertFalse(date(year, 2, 13) in ct_holidays)
                self.assertFalse(date(year, 2, 13) in il_holidays)
                self.assertFalse(date(year, 2, 13) in ia_holidays)
                self.assertFalse(date(year, 2, 13) in nj_holidays)
                self.assertFalse(date(year, 2, 13) in ny_holidays)
        for year in range(2010, 2050):
            self.assertFalse(date(year, 2, 12) in self.holidays)
            self.assertFalse(date(year, 2, 12) in ca_holidays)
            self.assertTrue(date(year, 2, 12) in ct_holidays)
            self.assertTrue(date(year, 2, 12) in il_holidays)
            self.assertTrue(date(year, 2, 12) in ia_holidays)
            self.assertTrue(date(year, 2, 12) in nj_holidays)
            self.assertTrue(date(year, 2, 12) in ny_holidays)
            if date(year, 2, 12).weekday() == 5:
                self.assertFalse(date(year, 2, 11) in self.holidays)
                self.assertFalse(date(year, 2, 11) in ca_holidays)
                self.assertTrue(date(year, 2, 11) in ct_holidays)
                self.assertTrue(date(year, 2, 11) in il_holidays)
                self.assertTrue(date(year, 2, 11) in ia_holidays)
                self.assertTrue(date(year, 2, 11) in nj_holidays)
                self.assertTrue(date(year, 2, 11) in ny_holidays)
            else:
                self.assertFalse(date(year, 2, 11) in ca_holidays)
                self.assertFalse(date(year, 2, 11) in ct_holidays)
                self.assertFalse(date(year, 2, 11) in il_holidays)
                self.assertFalse(date(year, 2, 11) in ia_holidays)
                self.assertFalse(date(year, 2, 11) in nj_holidays)
                self.assertFalse(date(year, 2, 11) in ny_holidays)
            if date(year, 2, 12).weekday() == 6:
                self.assertFalse(date(year, 2, 13) in self.holidays)
                self.assertFalse(date(year, 2, 13) in ca_holidays)
                self.assertTrue(date(year, 2, 13) in ct_holidays)
                self.assertTrue(date(year, 2, 13) in il_holidays)
                self.assertTrue(date(year, 2, 13) in ia_holidays)
                self.assertTrue(date(year, 2, 13) in nj_holidays)
                self.assertTrue(date(year, 2, 13) in ny_holidays)
            else:
                self.assertFalse(date(year, 2, 13) in ca_holidays)
                self.assertFalse(date(year, 2, 13) in ct_holidays)
                self.assertFalse(date(year, 2, 13) in il_holidays)
                self.assertFalse(date(year, 2, 13) in ia_holidays)
                self.assertFalse(date(year, 2, 13) in nj_holidays)
                self.assertFalse(date(year, 2, 13) in ny_holidays)

    def test_susan_b_anthony_day(self):
        ca_holidays = holidays.US(state='CA')
        fl_holidays = holidays.US(state='FL')
        ny_holidays = holidays.US(state='NY')
        wi_holidays = holidays.US(state='WI')
        self.assertFalse(date(1975, 2, 15) in wi_holidays)
        self.assertFalse(date(2000, 2, 15) in ca_holidays)
        self.assertFalse(date(2000, 2, 15) in fl_holidays)
        self.assertFalse(date(2000, 2, 15) in ny_holidays)
        self.assertTrue(date(2000, 2, 15) in wi_holidays)
        self.assertTrue(date(2004, 2, 15) in ny_holidays)
        self.assertFalse(date(2010, 2, 15) in fl_holidays)
        self.assertTrue(date(2010, 2, 15) in ny_holidays)
        self.assertFalse(date(2013, 2, 15) in self.holidays)
        self.assertFalse(date(2013, 2, 15) in ca_holidays)
        self.assertTrue(date(2013, 2, 15) in fl_holidays)
        self.assertTrue(date(2013, 2, 15) in ny_holidays)
        self.assertFalse(date(2014, 2, 15) in self.holidays)
        self.assertTrue(date(2014, 2, 15) in ca_holidays)
        self.assertTrue(date(2014, 2, 15) in fl_holidays)
        self.assertTrue(date(2014, 2, 15) in ny_holidays)
        self.assertTrue(date(2014, 2, 15) in wi_holidays)

    def test_washingtons_birthday(self):
        de_holidays = holidays.US(state='DE')
        fl_holidays = holidays.US(state='FL')
        ga_holidays = holidays.US(state='GA')
        nm_holidays = holidays.US(state='NM')
        for dt in [date(1969, 2, 22), date(1970, 2, 22), date(1971, 2, 15),
                   date(1997, 2, 17), date(1999, 2, 15), date(2000, 2, 21),
                   date(2012, 2, 20), date(2013, 2, 18), date(2014, 2, 17),
                   date(2015, 2, 16), date(2016, 2, 15), date(2020, 2, 17)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)
            self.assertFalse(dt in de_holidays)
            self.assertNotEqual(fl_holidays.get(dt), "Washington's Birthday")
            self.assertFalse(dt in ga_holidays)
            self.assertFalse(dt in nm_holidays)
        for dt in [date(2013, 12, 24), date(2014, 12, 26), date(2015, 12, 24)]:
            self.assertTrue(dt in ga_holidays)
            self.assertTrue("Washington's Birthday"
                            in ga_holidays.get_list(dt))
        self.assertTrue(holidays.US(state='AL').get('2015-02-16'),
                        "George Washington/Thomas Jefferson Birthday")
        self.assertTrue(holidays.US(state='AS').get('2015-02-16'),
                        ("George Washington's Birthday "
                         "and Daisy Gatson Bates Day"))
        self.assertTrue(holidays.US(state='PR').get('2015-02-16'),
                        ("Presidents' Day"))
        self.assertTrue(holidays.US(state='VI').get('2015-02-16'),
                        ("Presidents' Day"))

    def test_mardi_gras(self):
        la_holidays = holidays.US(state='LA')
        self.assertFalse(date(1856, 2, 5) in la_holidays)
        for dt in [date(1857, 2, 24), date(2008, 2, 5), date(2011, 3, 8),
                   date(2012, 2, 21), date(2014, 3, 4), date(2018, 2, 13)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in la_holidays)

    def test_guam_discovery_day(self):
        gu_holidays = holidays.US(state='GU')
        self.assertFalse(date(1969, 3, 1) in gu_holidays)
        for dt in [date(1970, 3, 2), date(1971, 3, 1), date(1977, 3, 7),
                   date(2014, 3, 3), date(2015, 3, 2), date(2016, 3, 7)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in gu_holidays)
            self.assertEqual(gu_holidays.get(dt), "Guam Discovery Day")

    def test_casimir_pulaski_day(self):
        il_holidays = holidays.US(state='IL')
        self.assertFalse(date(1977, 3, 7) in il_holidays)
        for dt in [date(1978, 3, 6), date(1982, 3, 1), date(1983, 3, 7),
                   date(2014, 3, 3), date(2015, 3, 2), date(2016, 3, 7)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in il_holidays)
            self.assertEqual(il_holidays.get(dt), "Casimir Pulaski Day")

    def test_texas_independence_day(self):
        tx_holidays = holidays.US(state='TX')
        self.assertFalse(date(1873, 3, 2) in tx_holidays)
        for year in range(1874, 2050):
            self.assertFalse(date(year, 3, 2) in self.holidays)
            self.assertTrue(date(year, 3, 2) in tx_holidays)

    def test_town_meeting_day(self):
        vt_holidays = holidays.US(state='VT')
        self.assertFalse(date(1799, 3, 5) in vt_holidays)
        for dt in [date(1800, 3, 4), date(1803, 3, 1), date(1804, 3, 6),
                   date(2011, 3, 1), date(2015, 3, 3), date(2017, 3, 7)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in vt_holidays)

    def test_evacuation_day(self):
        ma_holidays = holidays.US(state='MA')
        self.assertFalse(date(1900, 3, 17) in ma_holidays)
        for year in range(1901, 2050):
            self.assertFalse(date(year, 3, 17) in self.holidays)
            self.assertTrue(date(year, 3, 17) in ma_holidays)
        self.assertFalse(date(1995, 3, 20) in ma_holidays)
        for dt in [date(2012, 3, 19), date(2013, 3, 18), date(2018, 3, 19)]:
            self.assertTrue(dt in ma_holidays)
        ma_holidays.observed = False
        for dt in [date(2012, 3, 19), date(2013, 3, 18), date(2018, 3, 19)]:
            self.assertFalse(dt in ma_holidays)

    def test_emancipation_day_in_puerto_rico(self):
        pr_holidays = holidays.US(state='PR')
        for year in range(2010, 2021):
            self.assertFalse(date(year, 3, 22) in self.holidays)
            self.assertTrue(date(year, 3, 22) in pr_holidays)
        self.assertFalse(date(2014, 3, 21) in pr_holidays)
        self.assertFalse(date(2014, 3, 23) in pr_holidays)
        self.assertTrue(date(2015, 3, 23) in pr_holidays)

    def test_prince_jonah_kuhio_kalanianaole_day(self):
        hi_holidays = holidays.US(state='HI')
        self.assertFalse(date(1948, 3, 26) in hi_holidays)
        for year in range(1949, 2050):
            self.assertFalse(date(year, 3, 26) in self.holidays)
            self.assertTrue(date(year, 3, 26) in hi_holidays)
        for dt in [date(1949, 3, 25), date(2016, 3, 25), date(2017, 3, 27)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in hi_holidays)
            self.assertEqual(hi_holidays.get(dt),
                             "Prince Jonah Kuhio Kalanianaole Day (Observed)")
        hi_holidays.observed = False
        for dt in [date(1949, 3, 25), date(2016, 3, 25), date(2017, 3, 27)]:
            self.assertFalse(dt in hi_holidays)

    def test_stewards_day(self):
        ak_holidays = holidays.US(state='AK')
        self.assertFalse(date(1917, 3, 30) in ak_holidays)
        for dt in [date(1918, 3, 30), date(1954, 3, 30), date(1955, 3, 28),
                   date(2002, 3, 25), date(2014, 3, 31), date(2018, 3, 26)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in ak_holidays)

    def test_cesar_chavez_day(self):
        ca_holidays = holidays.US(state='CA')
        tx_holidays = holidays.US(state='TX')
        for year in range(1995, 2000):
            self.assertFalse(date(year, 3, 31) in self.holidays)
            self.assertTrue(date(year, 3, 31) in ca_holidays)
        for year in range(2000, 2020):
            self.assertFalse(date(year, 3, 31) in self.holidays)
            self.assertTrue(date(year, 3, 31) in ca_holidays)
            self.assertTrue(date(year, 3, 31) in tx_holidays)
        for year in (1996, 2002, 2013, 2019):
            self.assertFalse(date(year, 4, 1) in self.holidays)
            self.assertTrue(date(year, 4, 1) in ca_holidays)
            self.assertFalse(date(year, 4, 1) in tx_holidays)

    def test_transfer_day(self):
        vi_holidays = holidays.US(state='VI')
        for year in range(2010, 2021):
            self.assertFalse(date(year, 3, 31) in self.holidays)
            self.assertTrue(date(year, 3, 31) in vi_holidays)

    def test_emancipation_day(self):
        dc_holidays = holidays.US(state='DC')
        self.assertFalse(date(2004, 4, 16) in dc_holidays)
        for year in range(2005, 2020):
            self.assertFalse(date(year, 4, 16) in self.holidays)
            self.assertTrue(date(year, 4, 16) in dc_holidays)
        self.assertTrue(date(2005, 4, 15) in dc_holidays)
        self.assertTrue(date(2006, 4, 17) in dc_holidays)
        dc_holidays.observed = False
        self.assertFalse(date(2005, 4, 15) in dc_holidays)
        self.assertFalse(date(2006, 4, 17) in dc_holidays)

    def test_patriots_day(self):
        me_holidays = holidays.US(state='ME')
        ma_holidays = holidays.US(state='MA')
        self.assertFalse(date(1983, 4, 19) in me_holidays)
        self.assertFalse(date(1983, 4, 19) in ma_holidays)
        for year in range(1894, 1969):
            self.assertFalse(date(year, 4, 19) in self.holidays)
            self.assertTrue(date(year, 4, 19) in me_holidays)
            self.assertTrue(date(year, 4, 19) in ma_holidays)
        for dt in [date(1969, 4, 21), date(1974, 4, 15), date(1975, 4, 21),
                   date(2015, 4, 20), date(2016, 4, 18), date(2019, 4, 15)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in me_holidays)
            self.assertTrue(dt in ma_holidays)

    def test_holy_thursday(self):
        vi_holidays = holidays.US(state='VI')
        for dt in [date(2010, 4,  1), date(2011, 4, 21), date(2013, 3, 28),
                   date(2014, 4, 17), date(2015, 4,  2), date(2016, 3, 24)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in vi_holidays)

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
        for dt in [date(1900, 4, 13), date(1901, 4,  5), date(1902, 3, 28),
                   date(1999, 4,  2), date(2000, 4, 21), date(2010, 4,  2),
                   date(2018, 3, 30), date(2019, 4, 19), date(2020, 4, 10)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in ct_holidays)
            self.assertTrue(dt in de_holidays)
            self.assertTrue(dt in gu_holidays)
            self.assertTrue(dt in in_holidays)
            self.assertTrue(dt in ky_holidays)
            self.assertTrue(dt in la_holidays)
            self.assertTrue(dt in nj_holidays)
            self.assertTrue(dt in nc_holidays)
            self.assertTrue(dt in tn_holidays)
            self.assertTrue(dt in tx_holidays)
            self.assertTrue(dt in vi_holidays)

    def test_easter_monday(self):
        vi_holidays = holidays.US(state='VI')
        for dt in [date(1900, 4, 16), date(1901, 4,  8), date(1902, 3, 31),
                   date(1999, 4,  5), date(2010, 4,  5),
                   date(2018, 4,  2), date(2019, 4, 22), date(2020, 4, 13)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in vi_holidays)

    def test_confederate_memorial_day(self):
        al_holidays = holidays.US(state='AL')
        ga_holidays = holidays.US(state='GA')
        ms_holidays = holidays.US(state='MS')
        sc_holidays = holidays.US(state='SC')
        tx_holidays = holidays.US(state='TX')
        self.assertFalse(date(1865, 4, 24) in self.holidays)
        self.assertFalse(date(1865, 4, 24) in al_holidays)
        for dt in [date(1866, 4, 23), date(1878, 4, 22), date(1884, 4, 28),
                   date(2014, 4, 28), date(2015, 4, 27), date(2019, 4, 22)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in al_holidays)
            self.assertTrue(dt in ga_holidays)
            self.assertTrue(dt in ms_holidays)
            self.assertTrue(dt in sc_holidays)
        self.assertFalse(date(1930, 1, 19) in tx_holidays)
        self.assertFalse(date(1931, 1, 19) in self.holidays)
        self.assertTrue(date(1931, 1, 19) in tx_holidays)

    def test_san_jacinto_day(self):
        tx_holidays = holidays.US(state='TX')
        self.assertFalse(date(1874, 4, 21) in tx_holidays)
        for year in (1875, 2050):
            self.assertFalse(date(year, 4, 21) in self.holidays)
            self.assertTrue(date(year, 4, 21) in tx_holidays)

    def test_arbor_day(self):
        ne_holidays = holidays.US(state='NE')
        for dt in [date(1875, 4, 22), date(1988, 4, 22), date(1989, 4, 28),
                   date(2009, 4, 24), date(2010, 4, 30), date(2014, 4, 25)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in ne_holidays)

    def test_primary_election_day(self):
        in_holidays = holidays.US(state='IN')
        self.assertFalse(date(2004, 5, 4) in in_holidays)
        for dt in [date(2006, 5, 2), date(2008, 5, 6), date(2010, 5, 4),
                   date(2012, 5, 8), date(2014, 5, 6), date(2015, 5, 5),
                   date(2016, 5, 3)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in in_holidays)

    def test_truman_day(self):
        mo_holidays = holidays.US(state='MO', observed=False)
        self.assertFalse(date(1948, 5, 8) in self.holidays)
        self.assertFalse(date(1948, 5, 8) in mo_holidays)
        for year in range(1949, 2100):
            dt = date(year, 5, 8)
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in mo_holidays)
            self.assertFalse(dt + relativedelta(days=-1) in mo_holidays)
            self.assertFalse(dt + relativedelta(days=+1) in mo_holidays)
        self.assertFalse(date(2004, 5, 7) in mo_holidays)
        self.assertFalse(date(2005, 5, 10) in mo_holidays)
        mo_holidays.observed = True
        self.assertTrue(date(2004, 5, 7) in mo_holidays)
        self.assertTrue(date(2005, 5, 10) in mo_holidays)

    def test_memorial_day(self):
        for dt in [date(1969, 5, 30), date(1970, 5, 30), date(1971, 5, 31),
                   date(1997, 5, 26), date(1999, 5, 31), date(2000, 5, 29),
                   date(2012, 5, 28), date(2013, 5, 27), date(2014, 5, 26),
                   date(2015, 5, 25), date(2016, 5, 30), date(2020, 5, 25)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

    def test_jefferson_davis_birthday(self):
        al_holidays = holidays.US(state='AL')
        self.assertFalse(date(1889, 6, 3) in self.holidays)
        self.assertFalse(date(1889, 6, 3) in al_holidays)
        for dt in [date(1890, 6, 2), date(1891, 6, 1), date(1897, 6, 7),
                   date(2014, 6, 2), date(2015, 6, 1), date(2016, 6, 6)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in al_holidays)

    def test_kamehameha_day(self):
        hi_holidays = holidays.US(state='HI')
        self.assertFalse(date(1871, 6, 11) in hi_holidays)
        for year in range(1872, 2050):
            self.assertFalse(date(year, 6, 11) in self.holidays)
            self.assertTrue(date(year, 6, 11) in hi_holidays)
        self.assertFalse(date(2006, 6, 12) in hi_holidays)
        for dt in [date(2011, 6, 10), date(2016, 6, 10), date(2017, 6, 12)]:
            self.assertTrue(dt in hi_holidays)
            hi_holidays.get(dt) == "Kamehameha Day (Observed)"
        hi_holidays.observed = False
        for dt in [date(2011, 6, 10), date(2016, 6, 10), date(2017, 6, 12)]:
            self.assertFalse(dt in hi_holidays)

    def test_emancipation_day_in_texas(self):
        tx_holidays = holidays.US(state='TX')
        self.assertFalse(date(1979, 6, 19) in tx_holidays)
        for year in (1980, 2050):
            self.assertFalse(date(year, 6, 19) in self.holidays)
            self.assertTrue(date(year, 6, 19) in tx_holidays)

    def test_west_virginia_day(self):
        wv_holidays = holidays.US(state='WV')
        self.assertFalse(date(1926, 6, 20) in wv_holidays)
        for year in (1927, 2050):
            self.assertFalse(date(year, 6, 20) in self.holidays)
            self.assertTrue(date(year, 6, 20) in wv_holidays)
        self.assertTrue(date(2015, 6, 19) in wv_holidays)
        self.assertTrue(date(2010, 6, 21) in wv_holidays)
        wv_holidays.observed = False
        self.assertFalse(date(2015, 6, 19) in wv_holidays)
        self.assertFalse(date(2010, 6, 21) in wv_holidays)

    def test_emancipation_day_in_virgin_islands(self):
        vi_holidays = holidays.US(state='VI')
        for year in (2010, 2021):
            self.assertFalse(date(year, 7, 3) in self.holidays)
            self.assertTrue(date(year, 7, 3) in vi_holidays)

    def test_independence_day(self):
        for year in range(1900, 2100):
            dt = date(year, 7, 4)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)
        self.assertFalse(date(2010, 7, 5) in self.holidays)
        self.assertFalse(date(2020, 7, 3) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2010, 7, 5) in self.holidays)
        self.assertTrue(date(2020, 7, 3) in self.holidays)

    def test_liberation_day_guam(self):
        gu_holidays = holidays.US(state='GU')
        self.assertFalse(date(1944, 7, 21) in gu_holidays)
        for year in range(1945, 2100):
            self.assertFalse(date(year, 7, 21) in self.holidays)
            self.assertTrue(date(year, 7, 21) in gu_holidays)

    def test_pioneer_day(self):
        ut_holidays = holidays.US(state='UT')
        self.assertFalse(date(1848, 7, 24) in ut_holidays)
        for year in (1849, 2050):
            self.assertFalse(date(year, 7, 24) in self.holidays)
            self.assertTrue(date(year, 7, 24) in ut_holidays)
        self.assertTrue('2010-07-23' in ut_holidays)
        self.assertTrue('2011-07-25' in ut_holidays)
        ut_holidays.observed = False
        self.assertFalse('2010-07-23' in ut_holidays)
        self.assertFalse('2011-07-25' in ut_holidays)

    def test_constitution_day(self):
        pr_holidays = holidays.US(state='PR')
        for year in range(2010, 2021):
            self.assertFalse(date(year, 7, 25) in self.holidays)
            self.assertTrue(date(year, 7, 25) in pr_holidays)
        self.assertFalse(date(2015, 7, 24) in pr_holidays)
        self.assertFalse(date(2015, 7, 26) in pr_holidays)
        self.assertTrue(date(2021, 7, 26) in pr_holidays)

    def test_victory_day(self):
        ri_holidays = holidays.US(state='RI')
        self.assertFalse(date(1947, 8, 11) in ri_holidays)
        for dt in [date(1948, 8, 9), date(1995, 8, 14), date(2005, 8, 8),
                   date(2015, 8, 10), date(2016, 8, 8), date(2017, 8, 14)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in ri_holidays)

    def test_statehood_day(self):
        hi_holidays = holidays.US(state='HI')
        self.assertFalse(date(1958, 8, 15) in hi_holidays)
        for dt in [date(1959, 8, 21), date(1969, 8, 15), date(1999, 8, 20),
                   date(2014, 8, 15), date(2015, 8, 21), date(2016, 8, 19)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in hi_holidays)

    def test_bennington_battle_day(self):
        vt_holidays = holidays.US(state='VT')
        self.assertFalse(date(1777, 8, 16) in vt_holidays)
        for year in range(1778, 2050):
            self.assertFalse(date(year, 8, 16) in self.holidays)
            self.assertTrue(date(year, 8, 16) in vt_holidays)
        vt_holidays.observed = False
        self.assertFalse("Bennington Battle Day (Observed)" in
                         vt_holidays.get_list(date(1997, 8, 15)))
        vt_holidays.observed = True
        self.assertTrue("Bennington Battle Day (Observed)" in
                        vt_holidays.get_list(date(1997, 8, 15)))
        self.assertFalse("Bennington Battle Day (Observed)" in
                         vt_holidays.get_list(date(1997, 8, 17)))
        self.assertTrue("Bennington Battle Day (Observed)" in
                        vt_holidays.get_list(date(1998, 8, 17)))
        self.assertFalse("Bennington Battle Day (Observed)" in
                         vt_holidays.get_list(date(1999, 8, 15)))
        self.assertFalse("Bennington Battle Day (Observed)" in
                         vt_holidays.get_list(date(1999, 8, 17)))

    def test_lyndon_baines_johnson_day(self):
        tx_holidays = holidays.US(state='TX')
        self.assertFalse(date(1972, 8, 27) in tx_holidays)
        for year in (1973, 2050):
            self.assertFalse(date(year, 8, 27) in self.holidays)
            self.assertTrue(date(year, 8, 27) in tx_holidays)

    def test_labor_day(self):
        for dt in [date(1997, 9, 1), date(1999, 9, 6), date(2000, 9, 4),
                   date(2012, 9, 3), date(2013, 9, 2), date(2014, 9, 1),
                   date(2015, 9, 7), date(2016, 9, 5), date(2020, 9, 7)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

    def test_columbus_day(self):
        ak_holidays = holidays.US(state='AK')
        de_holidays = holidays.US(state='DE')
        fl_holidays = holidays.US(state='FL')
        hi_holidays = holidays.US(state='HI')
        sd_holidays = holidays.US(state='SD')
        vi_holidays = holidays.US(state='VI')
        for dt in [date(1937, 10, 12), date(1969, 10, 12), date(1970, 10, 12),
                   date(1999, 10, 11), date(2000, 10,  9), date(2001, 10,  8),
                   date(2013, 10, 14), date(2018, 10,  8), date(2019, 10, 14)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt in ak_holidays)
            self.assertFalse(dt in de_holidays)
            self.assertFalse(dt in fl_holidays)
            self.assertFalse(dt in hi_holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)
            self.assertEqual(sd_holidays.get(dt), "Native American Day")
            self.assertEqual(vi_holidays.get(dt),
                             "Columbus Day and Puerto Rico Friendship Day")
        self.assertFalse(date(1936, 10, 12) in self.holidays)

    def test_alaska_day(self):
        ak_holidays = holidays.US(state='AK', observed=False)
        self.assertFalse(date(1866, 10, 18) in ak_holidays)
        for year in range(1867, 2050):
            self.assertTrue(date(year, 10, 18) in ak_holidays)
            self.assertFalse(date(year, 10, 17) in ak_holidays)
            self.assertFalse(date(year, 10, 19) in ak_holidays)
            self.assertFalse(date(year, 10, 18) in self.holidays)
        ak_holidays.observed = True
        self.assertTrue(date(2014, 10, 17) in ak_holidays)
        self.assertTrue(date(2015, 10, 19) in ak_holidays)

    def test_nevada_day(self):
        nv_holidays = holidays.US(state='NV')
        self.assertFalse(date(1932, 10, 31) in nv_holidays)
        for dt in [date(1933, 10, 31), date(1999, 10, 31), date(2000, 10, 27),
                   date(2002, 10, 25), date(2014, 10, 31), date(2015, 10, 30)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in nv_holidays)
        self.assertTrue("Nevada Day (Observed)" in
                        nv_holidays.get_list(date(1998, 10, 30)))
        self.assertTrue("Nevada Day (Observed)" in
                        nv_holidays.get_list(date(1999, 11, 1)))
        nv_holidays.observed = False
        self.assertFalse("Nevada Day (Observed)" in
                         nv_holidays.get_list(date(1998, 10, 30)))
        self.assertFalse("Nevada Day (Observed)" in
                         nv_holidays.get_list(date(1999, 11, 1)))

    def test_liberty_day(self):
        vi_holidays = holidays.US(state='VI')
        for year in range(2010, 2021):
            self.assertFalse(date(year, 11, 1) in self.holidays)
            self.assertTrue(date(year, 11, 1) in vi_holidays)

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
        self.assertFalse(date(2004, 11, 2) in de_holidays)
        for dt in [date(2008, 11, 4), date(2010, 11, 2), date(2012, 11, 6),
                   date(2014, 11, 4), date(2016, 11, 8), date(2018, 11, 6)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in de_holidays)
            self.assertTrue(dt in hi_holidays)
            self.assertTrue(dt in il_holidays)
            self.assertTrue(dt in in_holidays)
            self.assertTrue(dt in la_holidays)
            self.assertTrue(dt in mt_holidays)
            self.assertTrue(dt in nh_holidays)
            self.assertTrue(dt in nj_holidays)
            self.assertTrue(dt in ny_holidays)
            self.assertTrue(dt in wv_holidays)
        self.assertFalse(date(2015, 11, 3) in self.holidays)
        self.assertFalse(date(2015, 11, 3) in de_holidays)
        self.assertFalse(date(2015, 11, 3) in hi_holidays)
        self.assertFalse(date(2015, 11, 3) in il_holidays)
        self.assertTrue(date(2015, 11, 3) in in_holidays)
        self.assertFalse(date(2015, 11, 3) in la_holidays)
        self.assertFalse(date(2015, 11, 3) in mt_holidays)
        self.assertFalse(date(2015, 11, 3) in nh_holidays)
        self.assertFalse(date(2015, 11, 3) in nj_holidays)
        self.assertTrue(date(2015, 11, 3) in ny_holidays)
        self.assertFalse(date(2015, 11, 3) in wv_holidays)

    def test_all_souls_day(self):
        gu_holidays = holidays.US(state='GU')
        for year in range(1945, 2100):
            self.assertFalse(date(year, 11, 2) in self.holidays)
            self.assertTrue(date(year, 11, 2) in gu_holidays)

    def test_veterans_day(self):
        for dt in [date(1938, 11, 11), date(1939, 11, 11), date(1970, 11, 11),
                   date(1971, 10, 25), date(1977, 10, 24), date(1978, 11, 11),
                   date(2012, 11, 11), date(2013, 11, 11), date(2014, 11, 11),
                   date(2015, 11, 11), date(2016, 11, 11), date(2020, 11, 11)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)
        self.assertFalse("Armistice Day" in holidays.US(years=[1937]).values())
        self.assertFalse("Armistice Day" in holidays.US(years=[1937]).values())
        self.assertTrue("Armistice Day" in holidays.US(years=[1938]).values())
        self.assertTrue("Armistice Day" in holidays.US(years=[1953]).values())
        self.assertTrue("Veterans Day" in holidays.US(years=[1954]).values())
        self.assertFalse(date(2012, 11, 12) in self.holidays)
        self.assertFalse(date(2017, 11, 10) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2012, 11, 12) in self.holidays)
        self.assertTrue(date(2017, 11, 10) in self.holidays)

    def test_discovery_day(self):
        pr_holidays = holidays.US(state='PR')
        for year in range(2010, 2021):
            self.assertFalse(date(year, 11, 19) in self.holidays)
            self.assertTrue(date(year, 11, 19) in pr_holidays)
        self.assertFalse(date(2016, 11, 18) in pr_holidays)
        self.assertFalse(date(2016, 11, 20) in pr_holidays)
        self.assertTrue(date(2017, 11, 20) in pr_holidays)

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
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)
            self.assertTrue(dt + relativedelta(days=+1) in de_holidays)
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
            self.assertTrue(dt + relativedelta(days=+1) in fl_holidays)
            self.assertEqual(fl_holidays.get(dt + relativedelta(days=+1)),
                             "Friday After Thanksgiving")
            self.assertTrue(dt + relativedelta(days=+1) in tx_holidays)
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
        self.assertFalse(date(2011, 11, 25) in ga_holidays)
        for dt in [date(2013, 11, 29), date(2014, 11, 28), date(2015, 11, 27),
                   date(2018, 11, 23), date(2019, 11, 29), date(2020, 11, 27)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in ga_holidays)

    def test_lady_of_camarin_day(self):
        gu_holidays = holidays.US(state='GU')
        for year in range(1945, 2100):
            self.assertFalse(date(year, 12, 8) in self.holidays)
            self.assertTrue(date(year, 12, 8) in gu_holidays)

    def test_christmass_eve(self):
        as_holidays = holidays.US(state='AS')
        ks_holidays = holidays.US(state='KS')
        mi_holidays = holidays.US(state='MI')
        nc_holidays = holidays.US(state='NC')
        tx_holidays = holidays.US(state='TX')
        wi_holidays = holidays.US(state='WI')
        self.holidays.observed = False
        for year in range(1900, 2050):
            self.assertFalse(date(year, 12, 24) in self.holidays)
            self.assertTrue(date(year, 12, 24) in as_holidays)
            if year >= 2013:
                f = ks_holidays.get(date(year, 12, 24)).find("Eve")
                self.assertTrue(f > 0)
                f = mi_holidays.get(date(year, 12, 24)).find("Eve")
                self.assertTrue(f > 0)
                f = nc_holidays.get(date(year, 12, 24)).find("Eve")
                self.assertTrue(f > 0)
            if year >= 2012:
                f = wi_holidays.get(date(year, 12, 24)).find("Eve")
                self.assertTrue(f > 0)
            if year >= 1981:
                f = tx_holidays.get(date(year, 12, 24)).find("Eve")
                self.assertTrue(f > 0)
            if year < 1981:
                f = ks_holidays.get(date(year, 12, 24), "").find("Eve")
                self.assertTrue(f < 0)
                f = mi_holidays.get(date(year, 12, 24), "").find("Eve")
                self.assertTrue(f < 0)
                f = nc_holidays.get(date(year, 12, 24), "").find("Eve")
                self.assertTrue(f < 0)
                f = tx_holidays.get(date(year, 12, 24), "").find("Eve")
                self.assertTrue(f < 0)
                f = wi_holidays.get(date(year, 12, 24), "").find("Eve")
                self.assertTrue(f < 0)
        self.assertTrue(date(2016, 12, 23) in as_holidays)
        self.assertTrue(date(2016, 12, 23) in ks_holidays)
        self.assertTrue(date(2016, 12, 23) in mi_holidays)
        self.assertTrue(date(2016, 12, 23) in nc_holidays)
        self.assertTrue(date(2016, 12, 23) in tx_holidays)
        self.assertTrue(date(2016, 12, 23) in wi_holidays)
        self.assertTrue("Christmas Eve (Observed)" in
                        as_holidays.get_list(date(2017, 12, 22)))
        self.assertTrue("Christmas Eve (Observed)" in
                        ks_holidays.get_list(date(2017, 12, 22)))
        self.assertTrue("Christmas Eve (Observed)" in
                        mi_holidays.get_list(date(2017, 12, 22)))
        self.assertTrue("Christmas Eve (Observed)" in
                        nc_holidays.get_list(date(2017, 12, 22)))
        self.assertTrue("Christmas Eve (Observed)" in
                        tx_holidays.get_list(date(2017, 12, 22)))
        self.assertTrue("Christmas Eve (Observed)" in
                        wi_holidays.get_list(date(2017, 12, 22)))

    def test_christmas_day(self):
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)
        self.assertFalse(date(2010, 12, 24) in self.holidays)
        self.assertFalse(date(2016, 12, 26) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2010, 12, 24) in self.holidays)
        self.assertTrue(date(2016, 12, 26) in self.holidays)

    def test_day_after_christmas(self):
        nc_holidays = holidays.US(state='NC', observed=False)
        tx_holidays = holidays.US(state='TX', observed=False)
        self.assertFalse(date(2015, 12, 28) in nc_holidays)
        self.assertFalse(date(2016, 12, 27) in nc_holidays)
        self.assertFalse(date(2015, 12, 28) in tx_holidays)
        self.assertFalse(date(2016, 12, 27) in tx_holidays)
        nc_holidays.observed = True
        self.assertTrue("Day After Christmas (Observed)" in
                        nc_holidays.get_list(date(2015, 12, 28)))
        self.assertTrue("Day After Christmas (Observed)" in
                        nc_holidays.get_list(date(2016, 12, 27)))
        tx_holidays.observed = True
        self.assertFalse("Day After Christmas (Observed)" in
                         tx_holidays.get_list(date(2015, 12, 28)))
        self.assertFalse("Day After Christmas (Observed)" in
                         tx_holidays.get_list(date(2016, 12, 27)))

    def test_new_years_eve(self):
        ky_holidays = holidays.US(state='KY')
        mi_holidays = holidays.US(state='MI')
        wi_holidays = holidays.US(state='WI')
        self.assertFalse(date(2012, 12, 31) in ky_holidays)
        self.assertFalse(date(2012, 12, 31) in mi_holidays)
        self.assertFalse(date(2011, 12, 31) in wi_holidays)
        self.assertTrue(date(2012, 12, 31) in wi_holidays)
        for dt in [date(2013, 12, 31), date(2016, 12, 30)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in ky_holidays)
            self.assertTrue(dt in mi_holidays)
            self.assertTrue(dt in wi_holidays)


class TestNZ(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.NZ(observed=True)

    def test_new_years(self):
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertTrue(dt in self.holidays)
        for year, day in enumerate([1, 1, 1, 1, 3,       # 2001-05
                                    3, 1, 1, 1, 1,       # 2006-10
                                    3, 3, 1, 1, 1,       # 2011-15
                                    1, 3, 1, 1, 1, 1],   # 2016-21
                                   2001):
            dt = date(year, 1, day)
            self.assertTrue(dt in self.holidays)
            self.assertEqual(self.holidays[dt][:10], "New Year's")
        self.assertFalse("1893-01-01" in self.holidays)
        self.assertTrue("1894-01-01" in self.holidays)

    def test_day_after_new_years(self):
        for year in range(1900, 2100):
            dt = date(year, 1, 2)
            self.assertTrue(dt in self.holidays)
        for year, day in enumerate([2, 2, 2, 2, 2,       # 2001-05
                                    2, 2, 2, 2, 4,       # 2006-10
                                    4, 2, 2, 2, 2,       # 2011-15
                                    4, 2, 2, 2, 2, 4],   # 2016-21
                                   2001):
            dt = date(year, 1, day)
            self.assertTrue(dt in self.holidays)
            self.assertEqual(self.holidays[dt][:10], "Day after ")
        self.assertFalse(date(2016, 1, 3) in self.holidays)

    def test_waitangi_day(self):
        ntl_holidays = holidays.NZ(prov='Northland')
        for year, day in enumerate([3, 8, 7, 6, 5], 1964):
            dt = date(year, 2, day)
            self.assertTrue(dt in ntl_holidays, dt)
            self.assertEqual(ntl_holidays[dt][:8], "Waitangi")
        for year in range(1900, 1974):
            dt = date(year, 2, 6)
            self.assertFalse(dt in self.holidays)
        for year in range(1974, 2100):
            dt = date(year, 2, 6)
            self.assertTrue(dt in self.holidays)
        for year, day in enumerate([6, 6, 6, 6, 6,       # 2001-05
                                    6, 6, 6, 6, 6,       # 2006-10
                                    6, 6, 6, 6, 6,       # 2011-15
                                    8, 6, 6, 6, 6, 8],   # 2016-21
                                   2001):
            dt = date(year, 2, day)
            self.assertTrue(dt in self.holidays)
            self.assertEqual(self.holidays[dt][:8], "Waitangi")
        self.assertFalse(date(2005, 2, 7) in self.holidays)
        self.assertFalse(date(2010, 2, 8) in self.holidays)
        self.assertFalse(date(2011, 2, 7) in self.holidays)

    def test_good_friday(self):
        for dt in [date(1900, 4, 13), date(1901, 4,  5), date(1902, 3, 28),
                   date(1999, 4,  2), date(2000, 4, 21), date(2010, 4,  2),
                   date(2018, 3, 30), date(2019, 4, 19), date(2020, 4, 10)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

    def test_easter_monday(self):
        for dt in [date(1900, 4, 16), date(1901, 4,  8), date(1902, 3, 31),
                   date(1999, 4,  5), date(2010, 4,  5),
                   date(2018, 4,  2), date(2019, 4, 22), date(2020, 4, 13)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

    def test_anzac_day(self):
        for year in range(1900, 1921):
            dt = date(year, 4, 25)
            self.assertFalse(dt in self.holidays)
        for year in range(1921, 2100):
            dt = date(year, 4, 25)
            self.assertTrue(dt in self.holidays)
        for year, day in enumerate([25, 25, 25, 25, 25,        # 2001-05
                                    25, 25, 25, 25, 25,        # 2006-10
                                    25, 25, 25, 25, 27,        # 2011-15
                                    25, 25, 25, 25, 27, 26],   # 2016-21
                                   2001):
            dt = date(year, 4, day)
            self.assertTrue(dt in self.holidays, dt)
            self.assertEqual(self.holidays[dt][:5], "Anzac")
        self.assertFalse(date(2009, 4, 27) in self.holidays)
        self.assertFalse(date(2010, 4, 26) in self.holidays)

    def test_sovereigns_birthday(self):
        self.assertTrue(date(1909, 11,  9) in self.holidays)
        self.assertTrue(date(1936,  6, 23) in self.holidays)
        self.assertTrue(date(1937,  6,  9) in self.holidays)
        self.assertTrue(date(1940,  6,  3) in self.holidays)
        self.assertTrue(date(1952,  6,  2) in self.holidays)
        for year in range(1912, 1936):
            dt = date(year, 6, 3)
            self.assertTrue(dt in self.holidays)
            self.assertEqual(self.holidays[dt], "King's Birthday")
        for year, day in enumerate([4, 3, 2, 7, 6,       # 2001-05
                                    5, 4, 2, 1, 7,       # 2006-10
                                    6, 4, 3, 2, 1,       # 2011-15
                                    6, 5, 4, 3, 1, 7],   # 2016-21
                                   2001):
            dt = date(year, 6, day)
            self.assertTrue(dt in self.holidays, dt)
            self.assertEqual(self.holidays[dt], "Queen's Birthday")

    def test_labour_day(self):
        for year, day in enumerate([22, 28, 27, 25, 24,        # 2001-05
                                    23, 22, 27, 26, 25,        # 2006-10
                                    24, 22, 28, 27, 26,        # 2011-15
                                    24, 23, 22, 28, 26, 25],   # 2016-21
                                   2001):
            dt = date(year, 10, day)
            self.assertTrue(dt in self.holidays, dt)
            self.assertEqual(self.holidays[dt], "Labour Day")

    def test_christmas_day(self):
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
        self.assertFalse(date(2010, 12, 24) in self.holidays)
        self.assertNotEqual(self.holidays[date(2011, 12, 26)],
                            "Christmas Day (Observed)")
        self.holidays.observed = True
        self.assertEqual(self.holidays[date(2011, 12, 27)],
                         "Christmas Day (Observed)")
        for year, day in enumerate([25, 25, 25, 27, 27,        # 2001-05
                                    25, 25, 25, 25, 27,        # 2006-10
                                    27, 25, 25, 25, 25,        # 2011-15
                                    27, 25, 25, 25, 25, 25],   # 2016-21
                                   2001):
            dt = date(year, 12, day)
            self.assertTrue(dt in self.holidays, dt)
            self.assertEqual(self.holidays[dt][:9], "Christmas")

    def test_boxing_day(self):
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 12, 26)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)
        self.assertFalse(date(2009, 12, 28) in self.holidays)
        self.assertFalse(date(2010, 12, 27) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2009, 12, 28) in self.holidays)
        self.assertTrue(date(2010, 12, 27) in self.holidays)
        for year, day in enumerate([26, 26, 26, 28, 26,        # 2001-05
                                    26, 26, 26, 28, 28,        # 2006-10
                                    26, 26, 26, 26, 28,        # 2011-15
                                    26, 26, 26, 26, 28, 28],   # 2016-21
                                   2001):
            dt = date(year, 12, day)
            self.assertTrue(dt in self.holidays, dt)
            self.assertEqual(self.holidays[dt][:6], "Boxing")

    def test_auckland_anniversary_day(self):
        auk_holidays = holidays.NZ(prov='Auckland')
        for year, day in enumerate([29, 28, 27, 26, 31,        # 2001-05
                                    30, 29, 28, 26,  1,        # 2006-10
                                    31, 30, 28, 27, 26,        # 2011-15
                                    1,  30, 29, 28, 27,  1],   # 2016-21
                                   2001):
            dt = date(year, 2 if day < 9 else 1, day)
            self.assertTrue(dt in auk_holidays, dt)
            self.assertEqual(auk_holidays[dt],
                             "Auckland Anniversary Day")

    def test_taranaki_anniversary_day(self):
        tki_holidays = holidays.NZ(prov='Taranaki')
        for year, day in enumerate([12, 11, 10,  8, 14,        # 2001-05
                                    13, 12, 10,  9,  8,        # 2006-10
                                    14, 12, 11, 10,  9,        # 2011-15
                                    14, 13, 12, 11,  9,  8],   # 2016-21
                                   2001):
            dt = date(year, 3, day)
            self.assertTrue(dt in tki_holidays, dt)
            self.assertEqual(tki_holidays[dt],
                             "Taranaki Anniversary Day")

    def test_hawkes_bay_anniversary_day(self):
        hkb_holidays = holidays.NZ(prov="Hawke's Bay")
        for year, day in enumerate([19, 25, 24, 22, 21,        # 2001-05
                                    20, 19, 24, 23, 22,        # 2006-10
                                    21, 19, 25, 24, 23,        # 2011-15
                                    21, 20, 19, 25, 23, 22],   # 2016-21
                                   2001):
            dt = date(year, 10, day)
            self.assertTrue(dt in hkb_holidays, dt)
            self.assertEqual(hkb_holidays[dt],
                             "Hawke's Bay Anniversary Day")

    def test_wellington_anniversary_day(self):
        wgn_holidays = holidays.NZ(prov='Wellington')
        for year, day in enumerate([22, 21, 20, 19, 24,        # 2001-05
                                    23, 22, 21, 19, 25,        # 2006-10
                                    24, 23, 21, 20, 19,        # 2011-15
                                    25, 23, 22, 21, 20, 25],   # 2016-21
                                   2001):
            dt = date(year, 1, day)
            self.assertTrue(dt in wgn_holidays, dt)
            self.assertEqual(wgn_holidays[dt],
                             "Wellington Anniversary Day", dt)

    def test_marlborough_anniversary_day(self):
        mbh_holidays = holidays.NZ(prov='Marlborough')
        for year, day in enumerate([29,  4,  3,  1, 31,        # 2001-05
                                    30, 29,  3,  2,  1,        # 2006-10
                                    31, 29,  4,  3,  2,        # 2011-15
                                    31, 30, 29,  4,  2,  1],   # 2016-21
                                   2001):
            dt = date(year, 11 if day < 9 else 10, day)
            self.assertTrue(dt in mbh_holidays, dt)
            self.assertEqual(mbh_holidays[dt],
                             "Marlborough Anniversary Day", dt)

    def test_nelson_anniversary_day(self):
        nsn_holidays = holidays.NZ(prov='Nelson')
        for year, day in enumerate([29,  4,  3,  2, 31,        # 2001-05
                                    30, 29,  4,  2,  1,        # 2006-10
                                    31, 30,  4,  3,  2,        # 2011-15
                                    1,  30, 29,  4,  3,  1],   # 2016-21
                                   2001):
            dt = date(year, 2 if day < 9 else 1, day)
            self.assertTrue(dt in nsn_holidays, dt)
            self.assertEqual(nsn_holidays[dt],
                             "Nelson Anniversary Day", dt)

    def test_canterbury_anniversary_day(self):
        can_holidays = holidays.NZ(prov='Canterbury')
        for year, day in enumerate([16, 15, 14, 12, 11,        # 2001-05
                                    17, 16, 14, 13, 12,        # 2006-10
                                    11, 16, 15, 14, 13,        # 2011-15
                                    11, 17, 16, 15, 13, 12],   # 2016-21
                                   2001):
            dt = date(year, 11, day)
            self.assertTrue(dt in can_holidays, dt)
            self.assertEqual(can_holidays[dt],
                             "Canterbury Anniversary Day", dt)

    def test_south_canterbury_anniversary_day(self):
        stc_holidays = holidays.NZ(prov='South Canterbury')
        for year, day in enumerate([24, 23, 22, 27, 26,        # 2001-05
                                    25, 24, 22, 28, 27,        # 2006-10
                                    26, 24, 23, 22, 28,        # 2011-15
                                    26, 25, 24, 23, 28, 27],   # 2016-21
                                   2001):
            dt = date(year, 9, day)
            self.assertTrue(dt in stc_holidays, dt)
            self.assertEqual(stc_holidays[dt],
                             "South Canterbury Anniversary Day", dt)

    def test_westland_anniversary_day(self):
        wtc_holidays = holidays.NZ(prov='Westland')
        for year, day in enumerate([3,   2,  1, 29,  5,        # 2001-05
                                    4,   3,  1, 30, 29,        # 2006-10
                                    28,  3,  2,  1, 30,        # 2011-15
                                    28,  4,  3,  2, 30, 29],   # 2016-21
                                   2001):
            dt = date(year, 12 if day < 9 else 11, day)
            self.assertTrue(dt in wtc_holidays, dt)
            self.assertEqual(wtc_holidays[dt],
                             "Westland Anniversary Day", dt)

    def test_otago_anniversary_day(self):
        ota_holidays = holidays.NZ(prov='Otago')
        for year, day in enumerate([26, 25, 24, 22, 21,        # 2001-05
                                    20, 26, 25, 23, 22,        # 2006-10
                                    21, 26, 25, 24, 23,        # 2011-15
                                    21, 20, 26, 25, 23, 22],   # 2016-21
                                   2001):
            dt = date(year, 3, day)
            self.assertTrue(dt in ota_holidays, dt)
            self.assertEqual(ota_holidays[dt],
                             "Otago Anniversary Day", dt)

    def test_southland_anniversary_day(self):
        stl_holidays = holidays.NZ(prov='Southland')
        for year, day in enumerate([15, 14, 20, 19, 17,        # 2001-05
                                    16, 15, 14, 19, 18, 17],   # 2006-11
                                   2001):
            dt = date(year, 1, day)
            self.assertTrue(dt in stl_holidays, dt)
            self.assertEqual(stl_holidays[dt],
                             "Southland Anniversary Day", dt)
            for year, (month, day) in enumerate([(4, 10), (4,  2), (4, 22),
                                                 (4,  7), (3, 29), (4, 18),
                                                 (4,  3), (4, 23), (4, 14),
                                                 (4,  6)], 2012):
                dt = date(year, month, day)
                self.assertTrue(dt in stl_holidays, dt)
                self.assertEqual(stl_holidays[dt],
                                 "Southland Anniversary Day", dt)

    def test_chatham_islands_anniversary_day(self):
        cit_holidays = holidays.NZ(prov='Chatham Islands')
        for year, day in enumerate([3,   2,  1, 29, 28,        # 2001-05
                                    27,  3,  1, 30, 29,        # 2006-10
                                    28,  3,  2,  1, 30,        # 2011-15
                                    28, 27,  3,  2, 30, 29],   # 2016-21
                                   2001):
            dt = date(year, 12 if day < 9 else 11, day)
            self.assertTrue(dt in cit_holidays, dt)
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
            self.assertTrue(holiday in holidays_in_1969, holiday)
            self.assertTrue(holiday in holidays_in_2015, holiday)
        all_holidays.remove("Waitangi Day")
        all_holidays.insert(2, "New Zealand Day")
        for holiday in all_holidays:
            self.assertTrue(holiday in holidays_in_1974, holiday)
        self.assertFalse("Waitangi Day" in holidays_in_1974, holiday)


class TestAU(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.AU(observed=True)
        self.state_hols = dict((state, holidays.AU(observed=True, prov=state))
                               for state in holidays.AU.PROVINCES)

    def test_new_years(self):
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertTrue(dt in self.holidays)
        for year, day in enumerate([3, 2, 1, 1, 1,       # 2011-15
                                    1, 2, 1, 1, 1, 1],   # 2016-21
                                   2011):
            dt = date(year, 1, day)
            for state, hols in self.state_hols.items():
                self.assertTrue(dt in hols, (state, dt))
                self.assertEqual(hols[dt][:10], "New Year's", state)

    def test_australia_day(self):
        for year, day in enumerate([26, 26, 28, 27, 26,       # 2011-15
                                    26, 26, 26, 28, 27, 26],  # 2016-21
                                   2011):
            jan26 = date(year, 1, 26)
            dt = date(year, 1, day)
            self.assertTrue(jan26 in self.holidays, dt)
            self.assertEqual(self.holidays[jan26], "Australia Day")
            self.assertTrue(dt in self.holidays, dt)
            self.assertEqual(self.holidays[dt][:10], "Australia ")
            for state in holidays.AU.PROVINCES:
                self.assertTrue(jan26 in self.state_hols[state], (state, dt))
                self.assertEqual(self.state_hols[state][jan26],
                                 "Australia Day")
                self.assertTrue(dt in self.state_hols[state], (state, dt))
                self.assertEqual(self.state_hols[state][dt][:10], "Australia ")
        self.assertFalse(date(2016, 1, 27) in self.holidays)
        self.assertFalse(date(1887, 1, 26) in self.holidays)
        self.assertFalse(date(1934, 1, 26) in self.state_hols['SA'])
        for dt in [date(1889, 1, 26), date(1936, 1, 26), date(1945, 1,  26)]:
                self.assertTrue(dt in self.state_hols['NSW'], dt)
                self.assertEqual(self.state_hols['NSW'][dt], "Anniversary Day")

    def test_good_friday(self):
        for dt in [date(1900, 4, 13), date(1901, 4,  5), date(1902, 3, 28),
                   date(1999, 4,  2), date(2000, 4, 21), date(2010, 4,  2),
                   date(2018, 3, 30), date(2019, 4, 19), date(2020, 4, 10)]:
            self.assertTrue(dt in self.holidays)
            self.assertEqual(self.holidays[dt], "Good Friday")

    def test_easter_saturday(self):
        for dt in [date(1900, 4, 14), date(1901, 4,  6), date(1902, 3, 29),
                   date(1999, 4,  3), date(2000, 4, 22), date(2010, 4,  3),
                   date(2018, 3, 31), date(2019, 4, 20), date(2020, 4, 11)]:
            for state in ['ACT', 'NSW', 'NT', 'QLD', 'SA', 'VIC']:
                self.assertTrue(dt in self.state_hols[state], (state, dt))
                self.assertEqual(self.state_hols[state][dt], "Easter Saturday")
            for state in ['TAS', 'WA']:
                self.assertFalse(dt in self.state_hols[state], (state, dt))

    def test_easter_sunday(self):
        for dt in [date(1900, 4, 15), date(1901, 4,  7), date(1902, 3, 30),
                   date(1999, 4,  4), date(2010, 4,  4),
                   date(2018, 4,  1), date(2019, 4, 21), date(2020, 4, 12)]:
            self.assertTrue(dt in self.state_hols['NSW'], dt)
            self.assertEqual(self.state_hols['NSW'][dt], "Easter Sunday")
            for state in ['ACT', 'NT', 'QLD', 'SA', 'VIC', 'TAS', 'WA']:
                self.assertFalse(dt in self.state_hols[state], (state, dt))

    def test_easter_monday(self):
        for dt in [date(1900, 4, 16), date(1901, 4,  8), date(1902, 3, 31),
                   date(1999, 4,  5), date(2010, 4,  5),
                   date(2018, 4,  2), date(2019, 4, 22), date(2020, 4, 13)]:
            self.assertTrue(dt in self.holidays)
            self.assertEqual(self.holidays[dt], "Easter Monday")
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

    def test_labour_day(self):
        for year, day in enumerate([7, 5, 4, 3, 2, 7, 6, ], 2011):
            dt = date(year, 3, day)
            self.assertTrue(dt in self.state_hols['WA'], dt)
            self.assertEqual(self.state_hols['WA'][dt], "Labour Day")
        for year, day in enumerate([10, 9, 14], 2014):
            dt = date(year, 3, day)
            self.assertFalse(dt in self.holidays, dt)
            self.assertTrue(dt in self.state_hols['VIC'], dt)
            self.assertEqual(self.state_hols['VIC'][dt], "Labour Day")

    def test_anzac_day(self):
        for year in range(1900, 1921):
            dt = date(year, 4, 25)
            self.assertFalse(dt in self.holidays)
        for year in range(1921, 2100):
            dt = date(year, 4, 25)
            self.assertTrue(dt in self.holidays)
        for dt in [date(2015, 4, 27), date(2020, 4, 27)]:
            self.assertFalse(dt in self.holidays, dt)
            for state in ['NT', 'WA']:
                self.assertTrue(dt in self.state_hols[state], (state, dt))
                self.assertEqual(self.state_hols[state][dt][:5], "Anzac")
            for state in ['ACT', 'QLD', 'SA', 'NSW', 'TAS', 'VIC']:
                self.assertFalse(dt in self.state_hols[state], (state, dt))
        dt = date(2021, 4, 26)
        for state in ['ACT', 'NT', 'QLD', 'SA', 'WA']:
            self.assertTrue(dt in self.state_hols[state], (state, dt))
            self.assertEqual(self.state_hols[state][dt][:5], "Anzac")
        for state in ['NSW', 'TAS', 'VIC']:
            self.assertFalse(dt in self.state_hols[state], (state, dt))

    def test_western_australia_day(self):
        for year, day in enumerate([4, 3, 2], 2012):
            dt = date(year, 6, day)
            self.assertTrue(dt in self.state_hols['WA'], dt)
            self.assertEqual(self.state_hols['WA'][dt], "Foundation Day")
        for year, day in enumerate([1, 6, 5], 2015):
            dt = date(year, 6, day)
            self.assertTrue(dt in self.state_hols['WA'], dt)
            self.assertEqual(self.state_hols['WA'][dt],
                             "Western Australia Day")

    def test_adelaide_cup(self):
        for dt in [date(2015, 3, 9), date(2016, 3, 14), date(2017, 3, 13)]:
            self.assertTrue(dt in self.state_hols['SA'], dt)
            self.assertEqual(self.state_hols['SA'][dt], "Adelaide Cup")

    def test_queens_birthday(self):
        for dt in [date(2012, 10,  1), date(2013,  6, 10), date(2014,  6,  9),
                   date(2015,  6,  8), date(2016,  6, 13)]:
            self.assertTrue(dt in self.state_hols['QLD'], dt)
            self.assertEqual(self.state_hols['QLD'][dt], "Queen's Birthday")
        self.assertTrue(date(2012, 6, 11) in self.state_hols['QLD'])
        for dt in [date(2012, 10,  1), date(2013, 9, 30), date(2014, 9, 29),
                   date(2015,  9, 28), date(2016, 9, 26), date(2017, 9, 25)]:
            self.assertTrue(dt in self.state_hols['WA'], dt)
            self.assertEqual(self.state_hols['WA'][dt], "Queen's Birthday")
        self.assertTrue(date(2015, 6, 8) in self.state_hols['VIC'])

    def test_picnic_day(self):
        for dt in [date(2015, 8,  3), date(2016,  8, 1)]:
            self.assertTrue(dt in self.state_hols['NT'], dt)
            self.assertEqual(self.state_hols['NT'][dt], "Picnic Day")

    def test_family_and_community_day(self):
        for dt in [date(2010, 9, 26), date(2011, 10, 10), date(2012, 10, 8),
                   date(2013, 9, 30), date(2014, 9, 29), date(2015, 9, 28),
                   date(2016, 9, 26)]:
            self.assertTrue(dt in self.state_hols['ACT'], dt)
            self.assertEqual(self.state_hols['ACT'][dt],
                             "Family & Community Day")

    def test_melbourne_cup(self):
        for dt in [date(2014, 11, 4), date(2015, 11, 3), date(2016, 11, 1)]:
            self.assertTrue(dt in self.state_hols['VIC'], dt)
            self.assertEqual(self.state_hols['VIC'][dt], "Melbourne Cup")

    def test_christmas_day(self):
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 12, 25)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
        self.assertFalse(date(2010, 12, 24) in self.holidays)
        self.assertNotEqual(self.holidays[date(2011, 12, 26)],
                            "Christmas Day (Observed)")
        self.holidays.observed = True
        self.assertEqual(self.holidays[date(2011, 12, 27)],
                         "Christmas Day (Observed)")
        for year, day in enumerate([25, 25, 25, 27, 27,        # 2001-05
                                    25, 25, 25, 25, 27,        # 2006-10
                                    27, 25, 25, 25, 25,        # 2011-15
                                    27, 25, 25, 25, 25, 25],   # 2016-21
                                   2001):
            dt = date(year, 12, day)
            self.assertTrue(dt in self.holidays, dt)
            self.assertEqual(self.holidays[dt][:9], "Christmas")

    def test_boxing_day(self):
        self.holidays.observed = False
        for year in range(1900, 2100):
            dt = date(year, 12, 26)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)
        self.assertFalse(date(2009, 12, 28) in self.holidays)
        self.assertFalse(date(2010, 12, 27) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2009, 12, 28) in self.holidays)
        self.assertTrue(date(2010, 12, 27) in self.holidays)
        for year, day in enumerate([26, 26, 26, 28, 26,        # 2001-05
                                    26, 26, 26, 28, 28,        # 2006-10
                                    26, 26, 26, 26, 28,        # 2011-15
                                    26, 26, 26, 26, 28, 28],   # 2016-21
                                   2001):
            dt = date(year, 12, day)
            self.assertTrue(dt in self.holidays, dt)
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
            self.assertTrue(holiday in holidays_in_2015, holiday)

if __name__ == "__main__":
    unittest.main()
