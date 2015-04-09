# -*- coding: utf-8 -*-

#  holidays.py
#  -----------
#  A fast, efficient Python library for generating country-specific sets of
#  holidays on the fly. It aims to make determining whether a specific date is
#  a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com>
#  Website: https://github.com/ryanss/holidays.py
#  License: MIT (see LICENSE file)


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
        self.assertFalse((ca+us).expand)
        self.assertTrue((us+ca).expand)
        self.assertEqual((ca+us).years, set([2014, 2015]))
        self.assertEqual((us+ca).years, set([2014, 2015]))
        na = holidays.CA()
        na += holidays.US()
        na += holidays.MX()
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

    def test_washingtons_birthday(self):
        for dt in [date(1969, 2, 22), date(1970, 2, 22), date(1971, 2, 15),
                   date(1997, 2, 17), date(1999, 2, 15), date(2000, 2, 21),
                   date(2012, 2, 20), date(2013, 2, 18), date(2014, 2, 17),
                   date(2015, 2, 16), date(2016, 2, 15), date(2020, 2, 17)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

    def test_memorial_day(self):
        for dt in [date(1969, 5, 30), date(1970, 5, 30), date(1971, 5, 31),
                   date(1997, 5, 26), date(1999, 5, 31), date(2000, 5, 29),
                   date(2012, 5, 28), date(2013, 5, 27), date(2014, 5, 26),
                   date(2015, 5, 25), date(2016, 5, 30), date(2020, 5, 25)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

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

    def test_labor_day(self):
        for dt in [date(1997, 9, 1), date(1999, 9, 6), date(2000, 9, 4),
                   date(2012, 9, 3), date(2013, 9, 2), date(2014, 9, 1),
                   date(2015, 9, 7), date(2016, 9, 5), date(2020, 9, 7)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

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

    def test_columbus_day(self):
        for dt in [date(1937, 10, 12), date(1969, 10, 12), date(1970, 10, 12),
                   date(1999, 11, 11), date(2000, 10,  9), date(2001, 10,  8),
                   date(2013, 10, 14), date(2018, 10,  8), date(2019, 10, 14)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)
        self.assertFalse(date(1936, 10, 12) in self.holidays)

    def test_thanksgiving_day(self):
        for dt in [date(1997, 11, 27), date(1999, 11, 25), date(2000, 11, 23),
                   date(2012, 11, 22), date(2013, 11, 28), date(2014, 11, 27),
                   date(2015, 11, 26), date(2016, 11, 24), date(2020, 11, 26)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt + relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt + relativedelta(days=+1) in self.holidays)

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


class TestNZ(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.NZ(observed=True)

    def test_new_years(self):
        for year in range(1900, 2100):
            dt = date(year, 1, 1)
            self.assertTrue(dt in self.holidays)
        for year, day in enumerate([1, 1, 1, 1, 3,     # 2001-05
                                    3, 1, 1, 1, 1,     # 2006-10
                                    3, 3, 1, 1, 1,     # 2011-15
                                    1, 3, 1, 1, 1, 1], # 2016-21
                                   2001):
            dt = date(year, 1, day)
            self.assertTrue(dt in self.holidays)
            self.assertEqual(self.holidays[dt][:10], "New Year's")

    def test_day_after_new_years(self):
        for year in range(1900, 2100):
            dt = date(year, 1, 2)
            self.assertTrue(dt in self.holidays)
        for year, day in enumerate([2, 2, 2, 2, 2,     # 2001-05
                                    2, 2, 2, 2, 4,     # 2006-10
                                    4, 2, 2, 2, 2,     # 2011-15
                                    4, 2, 2, 2, 2, 4], # 2016-21
                                   2001):
            dt = date(year, 1, day)
            self.assertTrue(dt in self.holidays)
            self.assertEqual(self.holidays[dt][:10], "Day after ")
        self.assertFalse(date(2016, 1, 3) in self.holidays)

    def test_waitangi_day(self):
        ntl_holidays = holidays.NZ(prov='Northland')
        for year in range(1964, 1974):
            dt = date(year, 2, 6)
            self.assertTrue(dt in ntl_holidays, dt)
            self.assertEqual(ntl_holidays[dt][:8], "Waitangi")
        for year in range(1900, 1974):
            dt = date(year, 2, 6)
            self.assertFalse(dt in self.holidays)
        for year in range(1974, 2100):
            dt = date(year, 2, 6)
            self.assertTrue(dt in self.holidays)
        for year, day in enumerate([6, 6, 6, 6, 6,     # 2001-05
                                    6, 6, 6, 6, 6,     # 2006-10
                                    6, 6, 6, 6, 6,     # 2011-15
                                    8, 6, 6, 6, 6, 8], # 2016-21
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
        for year, day in enumerate([25, 25, 25, 25, 25,      # 2001-05
                                    25, 25, 25, 25, 25,      # 2006-10
                                    25, 25, 25, 25, 27,      # 2011-15
                                    25, 25, 25, 25, 27, 26], # 2016-21
                                   2001):
            dt = date(year, 4, day)
            self.assertTrue(dt in self.holidays, dt)
            self.assertEqual(self.holidays[dt][:5], "Anzac")
        self.assertFalse(date(2009, 4, 27) in self.holidays)
        self.assertFalse(date(2010, 4, 26) in self.holidays)

    def test_sovereigns_birthday(self):
        self.assertTrue(date(1909, 11, 9) in self.holidays)
        for year in range(1912, 1936):
            dt = date(year, 6, 3)
            self.assertTrue(dt in self.holidays)
            self.assertEqual(self.holidays[dt], "King's Birthday")
        for year, day in enumerate([4, 3, 2, 7, 6,     # 2001-05
                                    5, 4, 2, 1, 7,     # 2006-10
                                    6, 4, 3, 2, 1,     # 2011-15
                                    6, 5, 4, 3, 1, 7], # 2016-21
                                   2001):
            dt = date(year, 6, day)
            self.assertTrue(dt in self.holidays, dt)
            self.assertEqual(self.holidays[dt], "Queen's Birthday")

    def test_labour_day(self):
        for year, day in enumerate([22, 28, 27, 25, 24,      # 2001-05
                                    23, 22, 27, 26, 25,      # 2006-10
                                    24, 22, 28, 27, 26,      # 2011-15
                                    24, 23, 22, 28, 26, 25], # 2016-21
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
        for year, day in enumerate([25, 25, 25, 27, 27,      # 2001-05
                                    25, 25, 25, 25, 27,      # 2006-10
                                    27, 25, 25, 25, 25,      # 2011-15
                                    27, 25, 25, 25, 25, 25], # 2016-21
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
        for year, day in enumerate([26, 26, 26, 28, 26,      # 2001-05
                                    26, 26, 26, 28, 28,      # 2006-10
                                    26, 26, 26, 26, 28,      # 2011-15
                                    26, 26, 26, 26, 28, 28], # 2016-21
                                   2001):
            dt = date(year, 12, day)
            self.assertTrue(dt in self.holidays, dt)
            self.assertEqual(self.holidays[dt][:6], "Boxing")

    def test_auckland_anniversary_day(self):
        auk_holidays = holidays.NZ(prov='Auckland')
        for year in range(1900, 2100):
            dt = date(year, 1, 29)
            self.assertTrue(dt in auk_holidays)
            self.assertEqual(auk_holidays[dt][:8], "Auckland")
        for year, day in enumerate([29, 28, 27, 26, 31,      # 2001-05
                                    30, 29, 28, 26,  1,      # 2006-10
                                    31, 30, 28, 27, 26,      # 2011-15
                                     1, 30, 29, 28, 27,  1], # 2016-21
                                   2001):
            dt = date(year, 2 if day < 9 else 1, day)
            self.assertTrue(dt in auk_holidays, dt)
            self.assertEqual(auk_holidays[dt],
                             "Auckland Anniversary Day (Observed)")

    def test_taranaki_anniversary_day(self):
        tki_holidays = holidays.NZ(prov='Taranaki')
        for year in range(1900, 2100):
            dt = date(year, 3, 31)
            self.assertTrue(dt in tki_holidays)
            self.assertEqual(tki_holidays[dt][:8], "Taranaki")
        for year, day in enumerate([12, 11, 10,  8, 14,      # 2001-05
                                    13, 12, 10,  9,  8,      # 2006-10
                                    14, 12, 11, 10,  9,      # 2011-15
                                    14, 13, 12, 11,  9,  8], # 2016-21
                                   2001):
            dt = date(year, 3, day)
            self.assertTrue(dt in tki_holidays, dt)
            self.assertEqual(tki_holidays[dt],
                             "Taranaki Anniversary Day (Observed)")

    def test_hawkes_bay_anniversary_day(self):
        hkb_holidays = holidays.NZ(prov='Hawkes Bay')
        for year in range(1940, 2100):
            dt = date(year, 11, 1)
            self.assertTrue(dt in hkb_holidays)
            self.assertEqual(hkb_holidays[dt][:10], "Hawkes Bay")
        for year, day in enumerate([19, 25, 24, 22, 21,      # 2001-05
                                    20, 19, 24, 23, 22,      # 2006-10
                                    21, 19, 25, 24, 23,      # 2011-15
                                    21, 20, 19, 25, 23, 22], # 2016-21
                                   2001):
            dt = date(year, 10, day)
            self.assertTrue(dt in hkb_holidays, dt)
            self.assertEqual(hkb_holidays[dt],
                             "Hawkes Bay Anniversary Day (Observed)")

    def test_wellington_anniversary_day(self):
        wgn_holidays = holidays.NZ(prov='Wellington')
        for year in range(1900, 2100):
            dt = date(year, 1, 22)
            self.assertTrue(dt in wgn_holidays)
            self.assertEqual(wgn_holidays[dt][:10], "Wellington")
        for year, day in enumerate([22, 21, 20, 19, 24,      # 2001-05
                                    23, 22, 21, 19, 25,      # 2006-10
                                    24, 23, 21, 20, 19,      # 2011-15
                                    25, 23, 22, 21, 20, 25], # 2016-21
                                   2001):
            dt = date(year, 1, day)
            self.assertTrue(dt in wgn_holidays, dt)
            self.assertEqual(wgn_holidays[dt],
                             "Wellington Anniversary Day (Observed)", dt)

    def test_marlborough_anniversary_day(self):
        mbh_holidays = holidays.NZ(prov='Marlborough')
        for year in range(1900, 2100):
            dt = date(year, 11, 1)
            self.assertTrue(dt in mbh_holidays)
            self.assertEqual(mbh_holidays[dt][:11], "Marlborough")
        for year, day in enumerate([29,  4,  3,  1, 31,      # 2001-05
                                    30, 29,  3,  2,  1,      # 2006-10
                                    31, 29,  4,  3,  2,      # 2011-15
                                    31, 30, 29,  4,  2,  1], # 2016-21
                                   2001):
            dt = date(year, 11 if day < 9 else 10 , day)
            self.assertTrue(dt in mbh_holidays, dt)
            self.assertEqual(mbh_holidays[dt],
                             "Marlborough Anniversary Day (Observed)", dt)

    def test_nelson_anniversary_day(self):
        nsn_holidays = holidays.NZ(prov='Nelson')
        for year in range(1900, 2100):
            dt = date(year, 2, 1)
            self.assertTrue(dt in nsn_holidays)
            self.assertEqual(nsn_holidays[dt][:6], "Nelson")
        for year, day in enumerate([29,  4,  3,  2, 31,      # 2001-05
                                    30, 29,  4,  2,  1,      # 2006-10
                                    31, 30,  4,  3,  2,      # 2011-15
                                     1, 30, 29,  4,  3,  1], # 2016-21
                                   2001):
            dt = date(year, 2 if day < 9 else 1 , day)
            self.assertTrue(dt in nsn_holidays, dt)
            self.assertEqual(nsn_holidays[dt],
                             "Nelson Anniversary Day (Observed)", dt)

    def test_canterbury_anniversary_day(self):
        can_holidays = holidays.NZ(prov='Canterbury')
        for year in range(1900, 2100):
            dt = date(year, 12, 16)
            self.assertTrue(dt in can_holidays)
            self.assertEqual(can_holidays[dt][:10], "Canterbury")
        for year, day in enumerate([16, 15, 14, 12, 11,      # 2001-05
                                    17, 16, 14, 13, 12,      # 2006-10
                                    11, 16, 15, 14, 13,      # 2011-15
                                    11, 17, 16, 15, 13, 12], # 2016-21
                                   2001):
            dt = date(year, 11, day)
            self.assertTrue(dt in can_holidays, dt)
            self.assertEqual(can_holidays[dt],
                             "Canterbury Anniversary Day (Observed)", dt)

    def test_south_canterbury_anniversary_day(self):
        stc_holidays = holidays.NZ(prov='South Canterbury')
        for year in range(1940, 2100):
            dt = date(year, 12, 16)
            self.assertTrue(dt in stc_holidays)
            self.assertEqual(stc_holidays[dt][:10], "Canterbury")
        for year, day in enumerate([24, 23, 22, 27, 26,      # 2001-05
                                    25, 24, 22, 28, 27,      # 2006-10
                                    26, 24, 23, 22, 28,      # 2011-15
                                    26, 25, 24, 23, 28, 27], # 2016-21
                                   2001):
            dt = date(year, 9, day)
            self.assertTrue(dt in stc_holidays, dt)
            self.assertEqual(stc_holidays[dt],
                             "Canterbury Anniversary Day (Observed)", dt)

    def test_westland_anniversary_day(self):
        wtc_holidays = holidays.NZ(prov='Westland')
        for year in range(1940, 2100):
            dt = date(year, 12, 1)
            self.assertTrue(dt in wtc_holidays)
            self.assertEqual(wtc_holidays[dt][:8], "Westland")
        for year, day in enumerate([ 3,  2,  1, 29,  5,      # 2001-05
                                     4,  3,  1, 30, 29,      # 2006-10
                                    28,  3,  2,  1, 30,      # 2011-15
                                    28,  4,  3,  2, 30, 29], # 2016-21
                                   2001):
            dt = date(year, 12 if day < 9 else 11, day)
            self.assertTrue(dt in wtc_holidays, dt)
            self.assertEqual(wtc_holidays[dt],
                             "Westland Anniversary Day (Observed)", dt)

    def test_otago_anniversary_day(self):
        ota_holidays = holidays.NZ(prov='Otago')
        for year in range(1900, 2100):
            dt = date(year, 3, 23)
            self.assertTrue(dt in ota_holidays)
            self.assertEqual(ota_holidays[dt][:5], "Otago")
        for year, day in enumerate([26, 25, 24, 22, 21,      # 2001-05
                                    20, 26, 25, 23, 22,      # 2006-10
                                    21, 26, 25, 24, 23,      # 2011-15
                                    21, 20, 26, 25, 23, 22], # 2016-21
                                   2001):
            dt = date(year, 3, day)
            self.assertTrue(dt in ota_holidays, dt)
            self.assertEqual(ota_holidays[dt],
                             "Otago Anniversary Day (Observed)", dt)

    def test_southland_anniversary_day(self):
        stl_holidays = holidays.NZ(prov='Southland')
        for year in range(1940, 2100):
            dt = date(year, 1, 17)
            self.assertTrue(dt in stl_holidays)
            self.assertEqual(stl_holidays[dt][:9], "Southland")
        for year, day in enumerate([15, 14, 20, 19, 17,      # 2001-05
                                    16, 15, 14, 19, 18, 17], # 2006-11
                                   2001):
            dt = date(year, 1, day)
            self.assertTrue(dt in stl_holidays, dt)
            self.assertEqual(stl_holidays[dt],
                             "Southland Anniversary Day (Observed)", dt)
            for year, (month, day) in enumerate([(4, 10), (4,  2), (4, 22),
                                                 (4,  7), (3, 29), (4, 18),
                                                 (4,  3), (4, 23), (4, 14),
                                                 (4,  6)], 2012):
                dt = date(year, month, day)
                self.assertTrue(dt in stl_holidays, dt)
                self.assertEqual(stl_holidays[dt],
                                 "Southland Anniversary Day (Observed)", dt)

    def test_chatham_islands_anniversary_day(self):
        cit_holidays = holidays.NZ(prov='Chatham Islands')
        for year in range(1940, 2100):
            dt = date(year, 11, 30)
            self.assertTrue(dt in cit_holidays)
            self.assertEqual(cit_holidays[dt][:7], "Chatham")
        for year, day in enumerate([ 3,  2,  1, 29, 28,      # 2001-05
                                    27,  3,  1, 30, 29,      # 2006-10
                                    28,  3,  2,  1, 30,      # 2011-15
                                    28, 27,  3,  2, 30, 29], # 2016-21
                                   2001):
            dt = date(year, 12 if day < 9 else 11, day)
            self.assertTrue(dt in cit_holidays, dt)
            self.assertEqual(cit_holidays[dt],
                             "Chatham Islands Anniversary Day (Observed)", dt)


if __name__ == "__main__":
    unittest.main()

