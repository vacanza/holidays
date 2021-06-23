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

import pickle
import unittest

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta, MO

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

        self.assertListEqual(
            self.holidays[date(2013, 12, 31) : date(2014, 1, 2)],
            [date(2014, 1, 1)],
        )
        self.assertListEqual(
            self.holidays[date(2013, 12, 24) : date(2014, 1, 2)],
            [date(2013, 12, 25), date(2014, 1, 1)],
        )
        self.assertListEqual(
            self.holidays[date(2013, 12, 25) : date(2014, 1, 2) : 3],
            [date(2013, 12, 25)],
        )
        self.assertListEqual(
            self.holidays[date(2013, 12, 25) : date(2014, 1, 2) : 7],
            [date(2013, 12, 25), date(2014, 1, 1)],
        )
        self.assertListEqual(
            self.holidays[date(2014, 1, 2) : date(2013, 12, 30)],
            [date(2014, 1, 1)],
        )
        self.assertListEqual(
            self.holidays[date(2014, 1, 2) : date(2013, 12, 25)],
            [date(2014, 1, 1)],
        )
        self.assertListEqual(
            self.holidays[date(2014, 1, 2) : date(2013, 12, 24)],
            [date(2014, 1, 1), date(2013, 12, 25)],
        )
        self.assertListEqual(
            self.holidays[date(2014, 1, 1) : date(2013, 12, 24) : 3],
            [date(2014, 1, 1)],
        )
        self.assertListEqual(
            self.holidays[date(2014, 1, 1) : date(2013, 12, 24) : 7],
            [date(2014, 1, 1), date(2013, 12, 25)],
        )
        self.assertListEqual(
            self.holidays[date(2013, 12, 31) : date(2014, 1, 2) : -3], []
        )
        self.assertListEqual(
            self.holidays[
                date(2014, 1, 1) : date(2013, 12, 24) : timedelta(days=3)
            ],
            [date(2014, 1, 1)],
        )
        self.assertListEqual(
            self.holidays[
                date(2014, 1, 1) : date(2013, 12, 24) : timedelta(days=7)
            ],
            [date(2014, 1, 1), date(2013, 12, 25)],
        )
        self.assertListEqual(
            self.holidays[
                date(2013, 12, 31) : date(2014, 1, 2) : timedelta(days=3)
            ],
            [],
        )
        self.assertRaises(
            ValueError, lambda: self.holidays[date(2014, 1, 1) :]
        )
        self.assertRaises(
            ValueError, lambda: self.holidays[: date(2014, 1, 1)]
        )
        self.assertRaises(
            TypeError,
            lambda: self.holidays[date(2014, 1, 1) : date(2014, 1, 2) : ""],
        )
        self.assertRaises(
            ValueError,
            lambda: self.holidays[date(2014, 1, 1) : date(2014, 1, 2) : 0],
        )

    def test_get(self):
        self.assertEqual(self.holidays.get("2014-01-01"), "New Year's Day")
        self.assertIsNone(self.holidays.get("2014-01-02"))
        self.assertFalse(self.holidays.get("2014-01-02", False))
        self.assertTrue(self.holidays.get("2014-01-02", True))

    def test_pop(self):
        self.assertRaises(KeyError, lambda: self.holidays.pop("2014-01-02"))
        self.assertFalse(self.holidays.pop("2014-01-02", False))
        self.assertTrue(self.holidays.pop("2014-01-02", True))
        self.assertIn(date(2014, 1, 1), self.holidays)
        self.assertEqual(self.holidays.pop("2014-01-01"), "New Year's Day")
        self.assertNotIn(date(2014, 1, 1), self.holidays)
        self.assertIn(date(2014, 7, 4), self.holidays)

    def test_pop_named(self):
        self.assertIn(date(2014, 1, 1), self.holidays)
        self.holidays.pop_named("New Year's Day")
        self.assertNotIn(date(2014, 1, 1), self.holidays)
        self.assertRaises(
            KeyError, lambda: self.holidays.pop_named("New Year's Dayz")
        )

    def test_setitem(self):
        self.holidays = holidays.US(years=[2014])
        self.assertEqual(len(self.holidays), 10)
        self.holidays[date(2014, 1, 3)] = "Fake Holiday"
        self.assertEqual(len(self.holidays), 11)
        self.assertIn(date(2014, 1, 3), self.holidays)
        self.assertEqual(self.holidays.get(date(2014, 1, 3)), "Fake Holiday")

    def test_update(self):
        h = holidays.HolidayBase()
        h.update(
            {
                date(2015, 1, 1): "New Year's Day",
                "2015-12-25": "Christmas Day",
            }
        )
        self.assertIn("2015-01-01", h)
        self.assertIn(date(2015, 12, 25), h)

    def test_append(self):
        h = holidays.HolidayBase()
        h.update(
            {
                date(2015, 1, 1): "New Year's Day",
                "2015-12-25": "Christmas Day",
            }
        )
        h.append([date(2015, 4, 1), "2015-04-03"])
        h.append(date(2015, 4, 6))
        h.append("2015-04-07")
        self.assertIn("2015-01-01", h)
        self.assertIn(date(2015, 12, 25), h)
        self.assertIn("2015-04-01", h)
        self.assertNotIn("2015-04-02", h)
        self.assertIn("2015-04-03", h)
        self.assertNotIn("2015-04-04", h)
        self.assertNotIn("2015-04-05", h)
        self.assertIn("2015-04-06", h)
        self.assertIn("2015-04-07", h)

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
        self.assertNotIn("2014-07-01", us)
        self.assertIn("2014-07-01", ca)
        self.assertNotIn("2014-07-04", ca)
        self.assertIn("2014-07-04", us)
        self.assertIn("2014-07-04", ca + us)
        self.assertIn("2014-07-04", us + ca)
        self.assertIn("2015-07-04", ca + us)
        self.assertIn("2015-07-04", us + ca)
        self.assertIn("2015-07-01", ca + us)
        self.assertIn("2015-07-01", us + ca)
        self.assertIn("2014-07-04", na)
        self.assertIn("2015-07-04", na)
        self.assertIn("2015-07-01", na)
        self.assertIn("2000-02-05", na)
        self.assertEqual((ca + us).prov, "ON")
        self.assertEqual((us + ca).prov, "ON")
        ca = holidays.CA(years=[2014], expand=False)
        us = holidays.US(years=[2014, 2015], expand=True)
        self.assertTrue((ca + us).expand)
        self.assertEqual((ca + us).years, {2014, 2015})
        self.assertEqual((us + ca).years, {2014, 2015})
        na = holidays.CA()
        na += holidays.US()
        na += holidays.MX()
        self.assertEqual(na.country, ["CA", "US", "MX"])
        self.assertIn("2014-07-04", na)
        self.assertIn("2014-07-04", na)
        self.assertIn("2015-07-04", na)
        self.assertIn("2015-07-04", na)
        self.assertIn("2015-07-01", na)
        self.assertIn("2015-07-01", na)
        self.assertIn("2000-02-05", na)
        self.assertEqual(na.prov, "ON")
        na = holidays.CA() + holidays.US()
        na += holidays.MX()
        self.assertIn("2014-07-04", na)
        self.assertIn("2014-07-04", na)
        self.assertIn("2015-07-04", na)
        self.assertIn("2015-07-04", na)
        self.assertIn("2015-07-01", na)
        self.assertIn("2015-07-01", na)
        self.assertIn("2000-02-05", na)
        self.assertEqual(na.prov, "ON")
        self.assertRaises(TypeError, lambda: holidays.US() + {})
        na = ca + (us + mx) + ca + (mx + us + holidays.CA(prov="BC"))
        self.assertIn("2000-02-05", na)
        self.assertIn("2014-02-10", na)
        self.assertIn("2014-02-17", na)
        self.assertIn("2014-07-04", na)
        provs = holidays.CA(prov="ON", years=[2014]) + holidays.CA(
            prov="BC", years=[2015]
        )
        self.assertIn("2015-02-09", provs)
        self.assertIn("2015-02-16", provs)
        self.assertEqual(provs.prov, ["ON", "BC"])
        a = sum(holidays.CA(prov=x) for x in holidays.CA.PROVINCES)
        self.assertEqual(a.country, "CA")
        self.assertEqual(a.prov, holidays.CA.PROVINCES)
        self.assertIn("2015-02-09", a)
        self.assertIn("2015-02-16", a)
        na = holidays.CA() + holidays.US() + holidays.MX()
        self.assertIn(date(1969, 12, 25), na)
        self.assertEqual(na.get(date(1969, 7, 1)), "Dominion Day")
        self.assertEqual(na.get(date(1983, 7, 1)), "Canada Day")
        self.assertEqual(
            na.get(date(1969, 12, 25)), "Christmas Day, Navidad [Christmas]"
        )
        na = holidays.MX() + holidays.CA() + holidays.US()
        self.assertEqual(
            na.get(date(1969, 12, 25)), "Navidad [Christmas], Christmas Day"
        )

    def test_get_list(self):
        westland = holidays.NZ(prov="WTL")
        chathams = holidays.NZ(prov="CIT")
        wild = westland + chathams
        self.assertEqual(
            wild[date(1969, 12, 1)],
            ("Westland Anniversary Day, " + "Chatham Islands Anniversary Day"),
        )

        self.assertEqual(
            wild.get_list(date(1969, 12, 1)),
            ["Westland Anniversary Day", "Chatham Islands Anniversary Day"],
        )
        self.assertEqual(wild.get_list(date(1969, 1, 1)), ["New Year's Day"])
        self.assertEqual(
            westland.get_list(date(1969, 12, 1)), ["Westland Anniversary Day"]
        )
        self.assertEqual(
            westland.get_list(date(1969, 1, 1)), ["New Year's Day"]
        )
        self.assertEqual(
            chathams.get_list(date(1969, 12, 1)),
            ["Chatham Islands Anniversary Day"],
        )
        self.assertEqual(
            chathams.get_list(date(1969, 1, 1)), ["New Year's Day"]
        )
        ca = holidays.CA()
        us = holidays.US()
        mx = holidays.MX()
        na = ca + us + mx
        self.assertIn(date(1969, 12, 25), na)
        self.assertEqual(
            na.get_list(date(1969, 12, 25)),
            ["Christmas Day", "Navidad [Christmas]"],
        )
        self.assertEqual(na.get_list(date(1969, 7, 1)), ["Dominion Day"])
        self.assertEqual(na.get_list(date(1969, 1, 3)), [])

    def test_list_supported_countries(self):
        self.assertIn("AR", holidays.list_supported_countries())
        self.assertIn("ZA", holidays.list_supported_countries())

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

    def test_get_named(self):
        us = holidays.UnitedStates(years=[2020])
        # check for "New Year's Day" presence in get_named("new")
        self.assertIn(date(2020, 1, 1), us.get_named("new"))

        # check for searching holiday in US when the observed holiday is on
        # a different year than input one
        us = holidays.US(years=[2022])
        us.get_named("Thanksgiving")
        self.assertEqual([2022], list(us.years))


class TestArgs(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.US()

    def test_country(self):
        self.assertEqual(self.holidays.country, "US")
        self.assertIn(date(2014, 7, 4), self.holidays)
        self.assertNotIn(date(2014, 7, 1), self.holidays)
        self.holidays = holidays.UnitedStates()
        self.assertEqual(self.holidays.country, "US")
        self.assertIn(date(2014, 7, 4), self.holidays)
        self.assertNotIn(date(2014, 7, 1), self.holidays)
        self.assertEqual(self.holidays.country, "US")
        self.holidays = holidays.CA()
        self.assertEqual(self.holidays.country, "CA")
        self.assertEqual(self.holidays.prov, "ON")
        self.assertIn(date(2014, 7, 1), self.holidays)
        self.assertNotIn(date(2014, 7, 4), self.holidays)
        self.holidays = holidays.CA(prov="BC")
        self.assertEqual(self.holidays.country, "CA")
        self.assertEqual(self.holidays.prov, "BC")
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

    def test_serialization(self):
        loaded_holidays = pickle.loads(pickle.dumps(self.holidays))
        assert loaded_holidays == self.holidays

        dt = datetime(2020, 1, 1)
        res = dt in self.holidays
        loaded_holidays = pickle.loads(pickle.dumps(self.holidays))
        assert loaded_holidays == self.holidays
        assert (dt in loaded_holidays) == res


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
        self.assertEqual(
            self.holidays[datetime(2014, 1, 1, 13, 45)], "New Year's Day"
        )
        self.holidays[datetime(2014, 1, 3, 1, 1)] = "Fake Holiday"
        self.assertIn(datetime(2014, 1, 3, 2, 2), self.holidays)
        self.assertEqual(
            self.holidays.pop(datetime(2014, 1, 3, 4, 4)), "Fake Holiday"
        )
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
            (TypeError, ValueError), lambda: "abc" in self.holidays
        )
        self.assertRaises(
            (TypeError, ValueError), lambda: self.holidays.get("abc123")
        )
        self.assertRaises(
            (TypeError, ValueError), self.holidays.__setitem__, "abc", "Test"
        )
        self.assertRaises((TypeError, ValueError), lambda: {} in self.holidays)


class TestCountryHoliday(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.CountryHoliday("US")

    def test_country(self):
        self.assertEqual(self.holidays.country, "US")

    def test_country_years(self):
        h = holidays.CountryHoliday("US", years=[2015, 2016])
        self.assertEqual(h.years, {2015, 2016})

    def test_country_state(self):
        h = holidays.CountryHoliday("US", state="NY")
        self.assertEqual(h.state, "NY")

    def test_country_province(self):
        h = holidays.CountryHoliday("AU", prov="NT")
        self.assertEqual(h.prov, "NT")

    def test_exceptions(self):
        self.assertRaises((KeyError), lambda: holidays.CountryHoliday("XXXX"))
