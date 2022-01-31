# -*- coding: utf-8 -*-

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

import pickle
import sys
import unittest
import warnings

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
        self.assertEqual((ca + us).subdiv, "ON")
        self.assertEqual((us + ca).subdiv, "ON")
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
        self.assertEqual(na.subdiv, "ON")
        na = holidays.CA() + holidays.US()
        na += holidays.MX()
        self.assertIn("2014-07-04", na)
        self.assertIn("2014-07-04", na)
        self.assertIn("2015-07-04", na)
        self.assertIn("2015-07-04", na)
        self.assertIn("2015-07-01", na)
        self.assertIn("2015-07-01", na)
        self.assertIn("2000-02-05", na)
        self.assertEqual(na.subdiv, "ON")
        self.assertRaises(TypeError, lambda: holidays.US() + {})
        na = ca + (us + mx) + ca + (mx + us + holidays.CA(subdiv="BC"))
        self.assertIn("2000-02-05", na)
        self.assertIn("2014-02-10", na)
        self.assertIn("2014-02-17", na)
        self.assertIn("2014-07-04", na)
        provs = holidays.CA(subdiv="ON", years=[2014]) + holidays.CA(
            subdiv="BC", years=[2015]
        )
        self.assertIn("2015-02-09", provs)
        self.assertIn("2015-02-16", provs)
        self.assertEqual(provs.subdiv, ["ON", "BC"])
        a = sum(holidays.CA(subdiv=x) for x in holidays.CA.subdivisions)
        self.assertEqual(a.country, "CA")
        self.assertEqual(a.subdiv, holidays.CA.subdivisions)
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
        westland = holidays.NZ(subdiv="WTL")
        chathams = holidays.NZ(subdiv="CIT")
        wild = westland + chathams
        self.assertEqual(
            wild[date(1969, 12, 1)],
            ("West Coast Anniversary Day, Chatham Islands Anniversary Day"),
        )

        self.assertEqual(
            wild.get_list(date(1969, 12, 1)),
            ["West Coast Anniversary Day", "Chatham Islands Anniversary Day"],
        )
        self.assertEqual(wild.get_list(date(1969, 1, 1)), ["New Year's Day"])
        self.assertEqual(
            westland.get_list(date(1969, 12, 1)),
            ["West Coast Anniversary Day"],
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
        self.assertIn("CA", holidays.list_supported_countries()["US"])

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
        self.assertEqual(self.holidays.subdiv, "ON")
        self.assertIn(date(2014, 7, 1), self.holidays)
        self.assertNotIn(date(2014, 7, 4), self.holidays)
        self.holidays = holidays.CA(subdiv="BC")
        self.assertEqual(self.holidays.country, "CA")
        self.assertEqual(self.holidays.subdiv, "BC")
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
        self.assertIn(date(2021, 12, 31), holidays.US(years=[2021]).keys())
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


class TestCountryHolidayDeprecation(unittest.TestCase):
    def test_deprecation(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            h = holidays.CountryHoliday("IT")
            self.assertIsInstance(h, holidays.HolidayBase)
            self.assertEqual(1, len(w))
            self.assertTrue(issubclass(w[-1].category, DeprecationWarning))


class TestCountryHolidays(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.country_holidays("US")

    def test_country(self):
        self.assertEqual(self.holidays.country, "US")

    def test_country_single_year(self):
        h = holidays.country_holidays("US", years=2021)
        self.assertEqual(h.years, {2021})

    def test_country_years(self):
        h = holidays.country_holidays("US", years=[2015, 2016])
        self.assertEqual(h.years, {2015, 2016})

    def test_country_state(self):
        h = holidays.country_holidays("US", subdiv="NY")
        self.assertEqual(h.subdiv, "NY")

    def test_country_province(self):
        h = holidays.country_holidays("AU", subdiv="NT")
        self.assertEqual(h.subdiv, "NT")

    def test_exceptions(self):
        self.assertRaises(
            NotImplementedError, lambda: holidays.country_holidays("XXXX")
        )
        self.assertRaises(
            NotImplementedError, lambda: holidays.country_holidays("XXXX")
        )
        self.assertRaises(
            NotImplementedError,
            lambda: holidays.country_holidays("US", subdiv="XXXX"),
        )
        self.assertRaises(
            NotImplementedError, lambda: holidays.US(subdiv="XXXX")
        )


class TestAllInSameYear(unittest.TestCase):
    """Test that only holidays in the year(s) requested are returned."""

    country: str
    hol: datetime
    year: int

    def setUp(self):
        self.countries = holidays.list_supported_countries()

    def tearDown(self):
        """https://stackoverflow.com/questions/4414234/"""

        def list2reason(exc_list):
            if exc_list and exc_list[-1][0] is self:
                return exc_list[-1][1]

        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = list2reason(result.errors)
        failure = list2reason(result.failures)
        text = error if error else failure
        if text:
            print(
                f"{text.splitlines()[-1]} in country {self.country}: "
                f"holiday {self.hol} returned for year {self.year}"
            )
            print(
                holidays.country_holidays(
                    self.country, subdiv=None, years=[self.year]
                ).get_list(self.hol)
            )

    def test_all_countries(self):
        """
        Only holidays in the year(s) requested should be returned. This
        ensures that we avoid triggering a "RuntimeError: dictionary changed
        size during iteration" error.

        Here we test all countries for the 12-year period starting ten years
        ago and ending 2 years from now.

        This is logic test and not a code compatibility test, so for expediency
        we only run it once on the latest Python version.
        """
        for self.country in self.countries:
            for self.year in range(
                date.today().year - 10, date.today().year + 3
            ):
                hols = holidays.country_holidays(
                    self.country, years=[self.year]
                )
                for self.hol in hols:
                    assert self.hol.year == self.year
