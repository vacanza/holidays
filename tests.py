#  holidays.py
#  -----------
#  A fast, efficient Python library for generating country-specific lists of
#  holidays on the fly which aims to make determining whether a specific date
#  is a hoiday as fast and flexible as possible.
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
        self.assertTrue(date(2014,1,1) in self.holidays)
        self.assertFalse(date(2014,1,2) in self.holidays)

    def test_getitem(self):
        self.assertEqual(self.holidays[date(2014,1,1)], "New Year's Day")
        self.assertEqual(self.holidays.get(date(2014,1,1)), "New Year's Day")
        self.assertRaises(KeyError, lambda: self.holidays[date(2014,1,2)])
        self.assertEqual(self.holidays.get(date(2014,1,2)), None)

    def test_get(self):
        self.assertEqual(self.holidays.get('2014-01-01'), "New Year's Day")
        self.assertEqual(self.holidays.get('2014-01-02'), None)

    def test_pop(self):
        self.assertRaises(KeyError, lambda: self.holidays.pop('2014-01-02'))
        self.assertFalse(self.holidays.pop('2014-01-02', False))
        self.assertTrue(date(2014,1,1) in self.holidays)
        self.assertEqual(self.holidays.pop('2014-01-01'), "New Year's Day")
        self.assertFalse(date(2014,1,1) in self.holidays)
        self.assertTrue(date(2014,7,4) in self.holidays)

    def test_setitem(self):
        self.holidays = holidays.US(years=[2014])
        self.assertEqual(len(self.holidays), 10)
        self.holidays[date(2014,1,3)] = "Fake Holiday"
        self.assertEqual(len(self.holidays), 11)
        self.assertTrue(date(2014,1,3) in self.holidays)
        self.assertEqual(self.holidays.get(date(2014,1,3)), "Fake Holiday")

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

    def test_inheritance(self):
        class NoColumbusHolidays(holidays.US):
            def _populate(self, year):
                holidays.US._populate(self, year)
                self.pop(date(year,10, 1)+relativedelta(weekday=MO(+2)), None)
        hdays = NoColumbusHolidays()
        self.assertTrue(date(2014,10,13) in self.holidays)
        self.assertFalse(date(2014,10,13) in hdays)
        self.assertTrue(date(2014,1,1) in hdays)
        self.assertTrue(date(2020,10,12) in self.holidays)
        self.assertFalse(date(2020,10,12) in hdays)
        self.assertTrue(date(2020,1,1) in hdays)

        class NinjaTurtlesHolidays(holidays.US):
            def _populate(self, year):
                holidays.US._populate(self, year)
                self[date(year,7,13)] = "Ninja Turtle's Day"
        hdays = NinjaTurtlesHolidays()
        self.assertFalse(date(2014,7,13) in self.holidays)
        self.assertTrue(date(2014,7,13) in hdays)
        self.assertTrue(date(2014,1,1) in hdays)
        self.assertFalse(date(2020,7,13) in self.holidays)
        self.assertTrue(date(2020,7,13) in hdays)
        self.assertTrue(date(2020,1,1) in hdays)

        class NewCountry(holidays.HolidayBase):
            def _populate(self, year):
                self[date(year,1,2)] = "New New Year's"
        hdays = NewCountry()
        self.assertFalse(date(2014,1,1) in hdays)
        self.assertTrue(date(2014,1,2) in hdays)


class TestArgs(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.US()

    def test_country(self):
        self.assertEqual(self.holidays.country, 'US')
        self.assertTrue(date(2014,7,4) in self.holidays)
        self.assertFalse(date(2014,7,1) in self.holidays)
        self.holidays = holidays.UnitedStates()
        self.assertEqual(self.holidays.country, 'US')
        self.assertTrue(date(2014,7,4) in self.holidays)
        self.assertFalse(date(2014,7,1) in self.holidays)
        self.assertEqual(self.holidays.country, 'US')
        self.holidays = holidays.CA()
        self.assertEqual(self.holidays.country, 'CA')
        self.assertEqual(self.holidays.prov, 'ON')
        self.assertTrue(date(2014,7,1) in self.holidays)
        self.assertFalse(date(2014,7,4) in self.holidays)
        self.holidays = holidays.CA(prov='BC')
        self.assertEqual(self.holidays.country, 'CA')
        self.assertEqual(self.holidays.prov, 'BC')
        self.assertTrue(date(2014,7,1) in self.holidays)
        self.assertFalse(date(2014,7,4) in self.holidays)

    def test_years(self):
        self.assertEqual(len(self.holidays.years), 0)
        self.assertFalse(date(2014,1,2) in self.holidays)
        self.assertEqual(len(self.holidays.years), 1)
        self.assertTrue(2014 in self.holidays.years)
        self.assertFalse(date(2013,1,2) in self.holidays)
        self.assertFalse(date(2014,1,2) in self.holidays)
        self.assertFalse(date(2015,1,2) in self.holidays)
        self.assertEqual(len(self.holidays.years), 3)
        self.assertTrue(2013 in self.holidays.years)
        self.assertTrue(2015 in self.holidays.years)
        self.holidays = holidays.US(years=range(2010,2015+1))
        self.assertEqual(len(self.holidays.years), 6)
        self.assertFalse(2009 in self.holidays.years)
        self.assertTrue(2010 in self.holidays.years)
        self.assertTrue(2015 in self.holidays.years)
        self.assertFalse(2016 in self.holidays.years)
        self.holidays = holidays.US(years=(2013,2015,2015))
        self.assertEqual(len(self.holidays.years), 2)
        self.assertTrue(2013 in self.holidays.years)
        self.assertFalse(2014 in self.holidays.years)
        self.assertTrue(2015 in self.holidays.years)

    def test_expand(self):
        self.holidays = holidays.US(years=(2013,2015), expand=False)
        self.assertEqual(len(self.holidays.years), 2)
        self.assertTrue(2013 in self.holidays.years)
        self.assertFalse(2014 in self.holidays.years)
        self.assertTrue(2015 in self.holidays.years)
        self.assertFalse(date(2014,1,1) in self.holidays)
        self.assertEqual(len(self.holidays.years), 2)
        self.assertFalse(2014 in self.holidays.years)

    def test_observed(self):
        self.holidays = holidays.US(observed=False)
        self.assertTrue(date(2000,1,1) in self.holidays)
        self.assertFalse(date(1999,12,31) in self.holidays)
        self.assertTrue(date(2012,1,1) in self.holidays)
        self.assertFalse(date(2012,1,2) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2000,1,1) in self.holidays)
        self.assertTrue(date(1999,12,31) in self.holidays)
        self.assertTrue(date(2012,1,1) in self.holidays)
        self.assertTrue(date(2012,1,2) in self.holidays)
        self.holidays.observed = False
        self.assertTrue(date(2000,1,1) in self.holidays)
        self.assertFalse(date(1999,12,31) in self.holidays)
        self.assertTrue(date(2012,1,1) in self.holidays)
        self.assertFalse(date(2012,1,2) in self.holidays)


class TestKeyTransforms(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.US()

    def test_dates(self):
        self.assertTrue(date(2014,1,1) in self.holidays)
        self.assertEqual(self.holidays[date(2014,1,1)], "New Year's Day")
        self.holidays[date(2014,1,3)] = "Fake Holiday"
        self.assertTrue(date(2014,1,3) in self.holidays)
        self.assertTrue(self.holidays.pop(date(2014,1,3)), "Fake Holiday")
        self.assertFalse(date(2014,1,3) in self.holidays)

    def test_datetimes(self):
        self.assertTrue(datetime(2014,1,1,13,45) in self.holidays)
        self.assertEqual(self.holidays[datetime(2014,1,1,13,45)], "New Year's Day")
        self.holidays[datetime(2014,1,3,1,1)] = "Fake Holiday"
        self.assertTrue(datetime(2014,1,3,2,2) in self.holidays)
        self.assertTrue(self.holidays.pop(datetime(2014,1,3,4,4)), "Fake Holiday")
        self.assertFalse(datetime(2014,1,3,2,2) in self.holidays)

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

    def test_unicode(self):
        self.assertTrue(u"01/01/2014" in self.holidays)
        self.assertEqual(self.holidays[u"01/01/2014"], "New Year's Day")
        self.holidays[u"01/03/2014"] = "Fake Holiday"
        self.assertTrue(u"01/03/2014" in self.holidays)
        self.assertTrue(self.holidays.pop(u"01/03/2014"), "Fake Holiday")
        self.assertFalse(u"01/03/2014" in self.holidays)

    def test_exceptions(self):
        self.assertRaises(ValueError, lambda: "abc" in self.holidays)
        self.assertRaises(ValueError, lambda: self.holidays.get("abc123"))
        self.assertRaises(ValueError, self.holidays.__setitem__, "abc", "Test")
        self.assertRaises(TypeError, lambda: list() in self.holidays)


class TestUS(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.US(observed=False)

    def test_new_years(self):
        for year in range(1900, 2100):
            dt = date(year,1,1)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt+relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt+relativedelta(days=+1) in self.holidays)
        self.assertFalse(date(2010,12,31) in self.holidays)
        self.assertFalse(date(2017,1,2) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2010,12,31) in self.holidays)
        self.assertTrue(date(2017,1,2) in self.holidays)
        self.holidays.observed = False

    def test_marthin_luther(self):
        for dt in [date(1986,1,20), date(1999,1,18), date(2000,1,17),
                   date(2012,1,16), date(2013,1,21), date(2014,1,20),
                   date(2015,1,19), date(2016,1,18), date(2020,1,20)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt+relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt+relativedelta(days=+1) in self.holidays)
        self.assertFalse("Martin Luther King, Jr. Day" \
                         in holidays.US(years=[1985]).values())
        self.assertTrue("Martin Luther King, Jr. Day" \
                         in holidays.US(years=[1986]).values())

    def test_washingtons_birthday(self):
        for dt in [date(1969,2,22), date(1970,2,22), date(1971,2,15),
                   date(1997,2,17), date(1999,2,15), date(2000,2,21),
                   date(2012,2,20), date(2013,2,18), date(2014,2,17),
                   date(2015,2,16), date(2016,2,15), date(2020,2,17)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt+relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt+relativedelta(days=+1) in self.holidays)

    def test_memorial_day(self):
        for dt in [date(1969,5,30), date(1970,5,30), date(1971,5,31),
                   date(1997,5,26), date(1999,5,31), date(2000,5,29),
                   date(2012,5,28), date(2013,5,27), date(2014,5,26),
                   date(2015,5,25), date(2016,5,30), date(2020,5,25)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt+relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt+relativedelta(days=+1) in self.holidays)

    def test_independence_day(self):
        for year in range(1900, 2100):
            dt = date(year,7,4)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt+relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt+relativedelta(days=+1) in self.holidays)
        self.assertFalse(date(2010,7,5) in self.holidays)
        self.assertFalse(date(2020,7,3) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2010,7,5) in self.holidays)
        self.assertTrue(date(2020,7,3) in self.holidays)
        self.holidays.observed = False

    def test_labor_day(self):
        for dt in [date(1997,9,1), date(1999,9,6), date(2000,9,4),
                   date(2012,9,3), date(2013,9,2), date(2014,9,1),
                   date(2015,9,7), date(2016,9,5), date(2020,9,7)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt+relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt+relativedelta(days=+1) in self.holidays)

    def test_veterans_day(self):
        for dt in [date(1938,11,11), date(1939,11,11), date(1970,11,11),
                   date(1971,10,25), date(1977,10,24), date(1978,11,11),
                   date(2012,11,11), date(2013,11,11), date(2014,11,11),
                   date(2015,11,11), date(2016,11,11), date(2020,11,11)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt+relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt+relativedelta(days=+1) in self.holidays)
        self.assertFalse("Armistice Day" in holidays.US(years=[1937]).values())
        self.assertFalse("Armistice Day" in holidays.US(years=[1937]).values())
        self.assertTrue("Armistice Day" in holidays.US(years=[1938]).values())
        self.assertTrue("Armistice Day" in holidays.US(years=[1953]).values())
        self.assertTrue("Veterans Day" in holidays.US(years=[1954]).values())
        self.assertFalse(date(2012,11,12) in self.holidays)
        self.assertFalse(date(2017,11,10) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2012,11,12) in self.holidays)
        self.assertTrue(date(2017,11,10) in self.holidays)
        self.holidays.observed = False

    def test_columbus_day(self):
        for dt in [date(1937,10,12), date(1969,10,12), date(1970,10,12),
                   date(1999,11,11), date(2000,10, 9), date(2001,10, 8),
                   date(2013,10,14), date(2018,10, 8), date(2019,10, 14)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt+relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt+relativedelta(days=+1) in self.holidays)
        self.assertFalse(date(1936,10,12) in self.holidays)

    def test_thanksgiving_day(self):
        for dt in [date(1997,11,27), date(1999,11,25), date(2000,11,23),
                   date(2012,11,22), date(2013,11,28), date(2014,11,27),
                   date(2015,11,26), date(2016,11,24), date(2020,11,26)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt+relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt+relativedelta(days=+1) in self.holidays)

    def test_christmas_day(self):
        for year in range(1900, 2100):
            dt = date(year,12,25)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt+relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt+relativedelta(days=+1) in self.holidays)
        self.assertFalse(date(2010,12,24) in self.holidays)
        self.assertFalse(date(2016,12,26) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2010,12,24) in self.holidays)
        self.assertTrue(date(2016,12,26) in self.holidays)
        self.holidays.observed = False


class TestCA(unittest.TestCase):

    def setUp(self):
        self.holidays = holidays.CA(observed=False)

    def test_new_years(self):
        for year in range(1900, 2100):
            dt = date(year,1,1)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt+relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt+relativedelta(days=+1) in self.holidays)
        self.assertFalse(date(2010,12,31) in self.holidays)
        self.assertFalse(date(2017,1,2) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2010,12,31) in self.holidays)
        self.assertTrue(date(2017,1,2) in self.holidays)
        self.holidays.observed = False

    def test_islander_day(self):
        pei_holidays = holidays.CA(prov="PE")
        for dt in [date(2009,2,9), date(2010,2,15), date(2011,2,21),
                   date(2012,2,20), date(2013,2,18), date(2014,2,17),
                   date(2015,2,16), date(2016,2,15), date(2020,2,17)]:
            if dt.year >= 2010:
                self.assertNotEqual(self.holidays[dt], "Islander Day")
            elif dt.year == 2009:
                self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in pei_holidays)
            self.assertFalse(dt+relativedelta(days=-1) in pei_holidays)
            self.assertFalse(dt+relativedelta(days=+1) in pei_holidays)

    def test_family_day(self):
        ab_holidays = holidays.CA(prov="AB")
        bc_holidays = holidays.CA(prov="BC")
        mb_holidays = holidays.CA(prov="MB")
        sk_holidays = holidays.CA(prov="SK")
        for dt in [date(1990,2,19), date(1999,2,15), date(2000,2,21),
                   date(2006,2,20)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in ab_holidays)
            self.assertFalse(dt in bc_holidays)
            self.assertFalse(dt in mb_holidays)
            self.assertFalse(dt in sk_holidays)
        dt = date(2007,2,19)
        self.assertFalse(dt in self.holidays)
        self.assertTrue(dt in ab_holidays)
        self.assertFalse(dt in bc_holidays)
        self.assertFalse(dt in mb_holidays)
        self.assertTrue(dt in sk_holidays)
        for dt in [date(2008,2,18), date(2012,2,20), date(2014,2,17),
                   date(2018,2,19), date(2019,2,18), date(2020,2,17)]:
            self.assertTrue(dt in self.holidays)
            self.assertTrue(dt in ab_holidays)
            self.assertFalse(dt in bc_holidays)
            self.assertTrue(dt in mb_holidays)
            self.assertTrue(dt in sk_holidays)
        for dt in [date(2013,2,11), date(2016,2,8), date(2020,2,10)]:
            self.assertFalse(dt in self.holidays)
            self.assertFalse(dt in ab_holidays)
            self.assertTrue(dt in bc_holidays)
            self.assertFalse(dt in mb_holidays)
            self.assertFalse(dt in sk_holidays)
        self.assertEqual(mb_holidays[date(2014,2,17)], "Louis Riel Day")


    def test_st_patricks_day(self):
        nl_holidays = holidays.CA(prov="NL", observed=False)
        for dt in [date(1900,3,19), date(1999,3,15), date(2000,3,20),
                   date(2012,3,19), date(2013,3,18), date(2014,3,17),
                   date(2015,3,16), date(2016,3,14), date(2020,3,16)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in nl_holidays)
            self.assertFalse(dt+relativedelta(days=-1) in nl_holidays)
            self.assertFalse(dt+relativedelta(days=+1) in nl_holidays)

    def test_good_friday(self):
        qc_holidays = holidays.CA(prov="QC")
        for dt in [date(1900,4,13), date(1901,4, 5), date(1902,3,28),
                   date(1999,4, 2), date(2000,4,21), date(2010,4, 2),
                   date(2018,3,30), date(2019,4,19), date(2020,4,10)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt+relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt+relativedelta(days=+1) in self.holidays)
            self.assertFalse(dt in qc_holidays)

    def test_easter_monday(self):
        qc_holidays = holidays.CA(prov="QC")
        for dt in [date(1900,4,16), date(1901,4, 8), date(1902,3,31),
                   date(1999,4, 5), date(2000,4,24), date(2010,4, 5),
                   date(2018,4, 2), date(2019,4,22), date(2020,4,13)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in qc_holidays)
            self.assertFalse(dt+relativedelta(days=-1) in qc_holidays)
            self.assertFalse(dt+relativedelta(days=+1) in qc_holidays)

    def test_st_georges_day(self):
        nl_holidays = holidays.CA(prov="NL")
        for dt in [date(1990,4,23), date(1999,4,26), date(2000,4,24),
                   date(2010,4,19), date(2016,4,25), date(2020,4,20)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in nl_holidays)
            self.assertFalse(dt+relativedelta(days=-1) in nl_holidays)
            self.assertFalse(dt+relativedelta(days=+1) in nl_holidays)

    def test_victoria_day(self):
        for dt in [date(1953,5,18), date(1999,5,24), date(2000,5,22),
                   date(2010,5,24), date(2015,5,18), date(2020,5,18)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt+relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt+relativedelta(days=+1) in self.holidays)

    def test_national_aboriginal_day(self):
        nt_holidays = holidays.CA(prov="NT")
        self.assertFalse(date(1995,6,21) in nt_holidays)
        for year in range(1996, 2100):
            dt = date(year,6,21)
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in nt_holidays)
            self.assertFalse(dt+relativedelta(days=-1) in nt_holidays)
            self.assertFalse(dt+relativedelta(days=+1) in nt_holidays)

    def test_st_jean_baptiste_day(self):
        qc_holidays = holidays.CA(prov="QC", observed=False)
        self.assertFalse(date(1924,6,24) in qc_holidays)
        for year in range(1925, 2100):
            dt = date(year,6,24)
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in qc_holidays)
            self.assertFalse(dt+relativedelta(days=-1) in qc_holidays)
            self.assertFalse(dt+relativedelta(days=+1) in qc_holidays)
        self.assertFalse(date(2001,6,25) in qc_holidays)
        qc_holidays.observed = True
        self.assertTrue(date(2001,6,25) in qc_holidays)

    def test_discovery_day(self):
        nl_holidays = holidays.CA(prov="NL")
        yu_holidays = holidays.CA(prov="YU")
        for dt in [date(1997,6,23), date(1999,6,21), date(2000,6,26),
                   date(2010,6,21), date(2016,6,27), date(2020,6,22)]:
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in nl_holidays)
            self.assertFalse(dt in yu_holidays)
        for dt in [date(1912,8,19), date(1999,8,16), date(2000,8,21),
                   date(2006,8,21), date(2016,8,15), date(2020,8,17)]:
            self.assertFalse(dt in self.holidays)
            self.assertFalse(dt in nl_holidays)
            self.assertTrue(dt in yu_holidays)

    def test_canada_day(self):
        for year in range(1900, 2100):
            dt = date(year,7,1)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt+relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt+relativedelta(days=+1) in self.holidays)
        self.assertFalse(date(2006,7,3) in self.holidays)
        self.assertFalse(date(2007,7,2) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2006,7,3) in self.holidays)
        self.assertTrue(date(2007,7,2) in self.holidays)
        self.holidays.observed = False

    def test_nunavut_day(self):
        nu_holidays = holidays.CA(prov="NU", observed=False)
        self.assertFalse(date(1999,7,9) in nu_holidays)
        self.assertFalse(date(2000,7,9) in nu_holidays)
        self.assertTrue(date(2000,4,1) in nu_holidays)
        for year in range(2001, 2100):
            dt = date(year,7,9)
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in nu_holidays)
            self.assertFalse(dt+relativedelta(days=-1) in nu_holidays)
            self.assertFalse(dt+relativedelta(days=+1) in nu_holidays)
        self.assertFalse(date(2017,7,10) in nu_holidays)
        nu_holidays.observed = True
        self.assertTrue(date(2017,7,10) in nu_holidays)

    def test_civic_holiday(self):
        bc_holidays = holidays.CA(prov="BC")
        for dt in [date(1900,8,6), date(1955,8,1), date(1973,8,6)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt in bc_holidays)
        for dt in [date(1974,8,5), date(1999,8,2), date(2000,8,7),
                   date(2010,8,2), date(2015,8,3), date(2020,8,3)]:
            self.assertTrue(dt in self.holidays)
            self.assertTrue(dt in bc_holidays)

    def test_labour_day(self):
        self.assertFalse(date(1893,9,4) in self.holidays)
        for dt in [date(1894,9,3), date(1900,9,3), date(1999,9,6),
                   date(2000,9,4), date(2014,9,1), date(2015,9,7)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt+relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt+relativedelta(days=+1) in self.holidays)

    def test_thanksgiving(self):
        ns_holidays = holidays.CA(prov="NB")
        for dt in [date(1931,10,12), date(1990,10, 8), date(1999,10,11),
                   date(2000,10, 9), date(2013,10,14), date(2020,10,12)]:
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt+relativedelta(days=-1) in self.holidays)
            self.assertFalse(dt+relativedelta(days=+1) in self.holidays)
            self.assertFalse(dt in ns_holidays)

    def test_remembrance_day(self):
        ab_holidays = holidays.CA(prov="AB", observed=False)
        nl_holidays = holidays.CA(prov="NL", observed=False)
        self.assertFalse(date(1930,11,11) in ab_holidays)
        self.assertFalse(date(1930,11,11) in nl_holidays)
        for year in range(1931, 2100):
            dt = date(year,11,11)
            self.assertFalse(dt in self.holidays)
            self.assertTrue(dt in ab_holidays)
            self.assertTrue(dt in nl_holidays)
            self.assertFalse(dt+relativedelta(days=-1) in nl_holidays)
            self.assertFalse(dt+relativedelta(days=+1) in nl_holidays)
        self.assertFalse(date(2007,11,12) in ab_holidays)
        self.assertFalse(date(2007,11,12) in nl_holidays)
        ab_holidays.observed = True
        nl_holidays.observed = True
        self.assertFalse(date(2007,11,12) in ab_holidays)
        self.assertTrue(date(2007,11,12) in nl_holidays)

    def test_christmas_day(self):
        for year in range(1900, 2100):
            dt = date(year,12,25)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt+relativedelta(days=-1) in self.holidays)
        self.assertFalse(date(2010,12,24) in self.holidays)
        self.assertNotEqual(self.holidays[date(2011,12,26)],
                            "Christmas Day (Observed)")
        self.holidays.observed = True
        self.assertTrue(date(2010,12,24) in self.holidays)
        self.assertEqual(self.holidays[date(2011,12,26)],
                            "Christmas Day (Observed)")
        self.holidays.observed = False

    def test_boxing_day(self):
        for year in range(1900, 2100):
            dt = date(year,12,26)
            self.assertTrue(dt in self.holidays)
            self.assertFalse(dt+relativedelta(days=+1) in self.holidays)
        self.assertFalse(date(2009,12,28) in self.holidays)
        self.assertFalse(date(2010,12,27) in self.holidays)
        self.holidays.observed = True
        self.assertTrue(date(2009,12,28) in self.holidays)
        self.assertTrue(date(2010,12,27) in self.holidays)
        self.holidays.observed = False


if __name__ == "__main__":
    unittest.main()
