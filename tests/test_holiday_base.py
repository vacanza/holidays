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

import os
import pathlib
import pickle
import unittest
import warnings
from datetime import date, datetime
from datetime import timedelta as td

from dateutil.relativedelta import MO
from dateutil.relativedelta import relativedelta as rd

import holidays
from holidays.constants import JAN, FEB, MON, TUE, SAT, SUN


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
            self.holidays[date(2013, 12, 31) : date(2014, 1, 2) : -3],
            [],
        )
        self.assertListEqual(
            self.holidays[date(2014, 1, 1) : date(2013, 12, 24) : td(days=3)],
            [date(2014, 1, 1)],
        )
        self.assertListEqual(
            self.holidays[date(2014, 1, 1) : date(2013, 12, 24) : td(days=7)],
            [date(2014, 1, 1), date(2013, 12, 25)],
        )
        self.assertListEqual(
            self.holidays[date(2013, 12, 31) : date(2014, 1, 2) : td(days=3)],
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
            KeyError,
            lambda: self.holidays.pop_named("New Year's Dayz"),
        )

    def test_setitem(self):
        self.holidays = holidays.US(years=[2014])
        self.assertEqual(len(self.holidays), 10)
        self.holidays[date(2014, 1, 3)] = "Fake Holiday"
        self.assertEqual(len(self.holidays), 11)
        self.assertIn(date(2014, 1, 3), self.holidays)
        self.assertEqual(self.holidays.get(date(2014, 1, 3)), "Fake Holiday")

    def test_repr_country(self):
        self.assertEqual(
            repr(holidays.US()),
            "holidays.country_holidays('US')",
        )
        self.assertEqual(
            repr(holidays.US(subdiv="CA")),
            "holidays.country_holidays('US', subdiv='CA')",
        )

    def test_repr_market(self):
        self.assertEqual(
            repr(holidays.NYSE()),
            "holidays.financial_holidays('NYSE')",
        )

    def test_str_country(self):
        self.assertEqual(
            str(holidays.US()),
            "{'country': US, 'expand': True, 'language': None, "
            "'market': None, 'observed': True, 'subdiv': None, "
            "'years': set()}",
        )
        self.assertEqual(
            str(holidays.US(years=1900)),
            '{datetime.date(1900, 1, 1): "New Year\'s Day", '
            'datetime.date(1900, 2, 22): "Washington\'s Birthday", '
            "datetime.date(1900, 5, 30): 'Memorial Day', "
            "datetime.date(1900, 7, 4): 'Independence Day', "
            "datetime.date(1900, 9, 3): 'Labor Day', "
            "datetime.date(1900, 11, 22): 'Thanksgiving', "
            "datetime.date(1900, 12, 25): 'Christmas Day'}",
        )

    def test_str_market(self):
        self.assertEqual(
            str(holidays.NYSE()),
            "{'country': None, 'expand': True, 'language': None, "
            "'market': NYSE, 'observed': True, 'subdiv': None, "
            "'years': set()}",
        )
        self.assertEqual(
            str(holidays.NYSE(years=1900)),
            "{datetime.date(1900, 12, 24): 'Christmas Eve', "
            'datetime.date(1900, 1, 1): "New Year\'s Day", '
            'datetime.date(1900, 2, 12): "Lincoln\'s Birthday", '
            'datetime.date(1900, 2, 22): "Washington\'s Birthday", '
            "datetime.date(1900, 4, 13): 'Good Friday', "
            "datetime.date(1900, 5, 30): 'Memorial Day', "
            "datetime.date(1900, 7, 4): 'Independence Day', "
            "datetime.date(1900, 9, 3): 'Labor Day', "
            "datetime.date(1900, 11, 6): 'Election Day', "
            "datetime.date(1900, 11, 22): 'Thanksgiving Day', "
            "datetime.date(1900, 12, 25): 'Christmas Day'}",
        )

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

    def test_is_leap_year(self):
        self.assertTrue(holidays.HolidayBase._is_leap_year(2000))
        self.assertFalse(holidays.HolidayBase._is_leap_year(2100))

    def test_is_weekend(self):
        h = holidays.HolidayBase()
        h._populate(2022)

        h.weekend = {MON, TUE}
        for dt in (date(2022, 10, 3), date(2022, 10, 4)):
            self.assertTrue(h._is_weekend(dt))

        h.weekend = {}
        for dt in (date(2022, 10, 3), date(2022, 10, 4)):
            self.assertFalse(h._is_weekend(dt))

        h.weekend = {SAT, SUN}
        for dt in (date(2022, 10, 1), date(2022, 10, 2)):
            self.assertTrue(h._is_weekend(dt))
        for dt in ((10, 1), (10, 2)):
            self.assertTrue(h._is_weekend(*dt))

        for dt in (date(2022, 10, 3), date(2022, 10, 4)):
            self.assertFalse(h._is_weekend(dt))
        for dt in ((10, 3), (10, 4)):
            self.assertFalse(h._is_weekend(*dt))

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

    def test_eq_(self):
        canada = holidays.Canada()
        united_states = holidays.UnitedStates()
        self.assertEqual(united_states, holidays.US())
        self.assertEqual(
            holidays.UnitedStates(years=2014), holidays.US(years=2014)
        )
        self.assertEqual(canada, holidays.CA())
        self.assertEqual(
            holidays.Canada(years=[2014]), holidays.CA(years=[2014])
        )
        self.assertEqual(
            holidays.Canada(language="fr"), holidays.CA(language="fr")
        )
        self.assertFalse(united_states == {})
        self.assertFalse(united_states == holidays.UnitedStates(subdiv="WA"))

    def test_ne(self):
        canada = holidays.Canada()
        united_states = holidays.UnitedStates()
        self.assertNotEqual(united_states, holidays.UnitedStates(years=2014))
        self.assertNotEqual(united_states, canada)
        self.assertNotEqual(
            holidays.UnitedStates(years=2014), holidays.Canada(years=2014)
        )
        self.assertNotEqual(united_states, holidays.UnitedStates(years=[2014]))
        self.assertNotEqual(canada, holidays.Canada(language="fr"))

        self.assertNotEqual(united_states, {})
        self.assertTrue(united_states != {})
        self.assertTrue(united_states != holidays.UnitedStates(subdiv="WA"))

        united_states.append("2023-01-01")
        self.assertNotEqual(united_states, holidays.UnitedStates(years=2023))

    def test_copy(self):
        us = holidays.UnitedStates()
        self.assertEqual(us, us.copy())
        self.assertTrue(us == us.copy())

        ca = holidays.Canada()
        ca_fr = holidays.Canada(language="fr")
        ca_xx = holidays.Canada(language="xx")
        self.assertNotEqual(ca, ca_fr)
        self.assertNotEqual(ca.copy(), ca_fr.copy())

        self.assertNotEqual(ca, ca_xx)
        self.assertNotEqual(ca.copy(), ca_xx.copy())

    def test_add_countries(self):
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
        na = holidays.CA() + holidays.US() + holidays.MX(language="es")
        self.assertIn(date(1969, 12, 25), na)
        self.assertEqual(na.get(date(1969, 7, 1)), "Dominion Day")
        self.assertEqual(na.get(date(1983, 7, 1)), "Canada Day")
        self.assertEqual(
            na.get(date(1969, 12, 25)),
            "Christmas Day; Navidad",
        )
        na = holidays.MX(language="es") + holidays.CA() + holidays.US()
        self.assertEqual(
            na.get(date(1969, 12, 25)),
            "Christmas Day; Navidad",
        )
        self.assertEqual(na, na.copy())

    def test_add_financial(self):
        ecb = holidays.ECB()
        nyse = holidays.NYSE()
        ecb_nyse = ecb + nyse
        self.assertEqual(len(ecb) + len(nyse), len(ecb_nyse))
        self.assertEqual(ecb_nyse.market, ["ECB", "NYSE"])
        self.assertEqual(ecb_nyse, ecb_nyse.copy())
        self.assertNotEqual(ecb_nyse, {})

    def test_add_holiday(self):
        us = holidays.UnitedStates()
        us._populate(2023)
        us._add_holiday("Test 1", date(2023, JAN, 5))
        us._add_holiday("Test 2", JAN, 6)

        self.assertIn("2023-01-05", us)
        self.assertIn("2023-01-06", us)

        for args in (
            (date(2020, JAN, 5),),
            (JAN, 5, "Test 1", True),
            ("Test", "Test"),
        ):
            self.assertRaises(TypeError, lambda: us._add_holiday(*args))

    def test_get_list(self):
        westland = holidays.NZ(subdiv="WTL")
        chathams = holidays.NZ(subdiv="CIT")
        wild = westland + chathams
        self.assertEqual(
            wild[date(1969, 12, 1)],
            ("Chatham Islands Anniversary Day; West Coast Anniversary Day"),
        )

        self.assertEqual(
            wild.get_list(date(1969, 12, 1)),
            ["Chatham Islands Anniversary Day", "West Coast Anniversary Day"],
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
        mx = holidays.MX(language="es")
        na = ca + us + mx
        self.assertIn(date(1969, 12, 25), na)
        self.assertEqual(
            na.get_list(date(1969, 12, 25)),
            ["Christmas Day", "Navidad"],
        )
        self.assertEqual(na.get_list(date(1969, 7, 1)), ["Dominion Day"])
        self.assertEqual(na.get_list(date(1969, 1, 3)), [])

    def test_list_supported_countries(self):
        supported_countries = holidays.list_supported_countries(unique=True)

        countries_files = [
            path
            for path in pathlib.Path("holidays/countries").glob("*.py")
            if not str(path).endswith("__init__.py")
        ]
        self.assertEqual(
            len(countries_files),
            len(supported_countries),
        )

        self.assertIn("AR", supported_countries)
        self.assertIn("CA", supported_countries["US"])
        self.assertIn("IM", supported_countries)
        self.assertIn("ZA", supported_countries)

    def test_list_supported_financial(self):
        supported_financial = holidays.list_supported_financial(unique=True)

        financial_files = [
            path
            for path in pathlib.Path("holidays/financial").glob("*.py")
            if not str(path).endswith("__init__.py")
        ]
        self.assertEqual(
            len(financial_files),
            len(supported_financial),
        )

        self.assertIn("ECB", supported_financial)
        self.assertIn("NYSE", supported_financial)

    def test_radd(self):
        self.assertRaises(TypeError, lambda: 1 + holidays.US())

    def test_inheritance(self):
        class NoColumbusHolidays(holidays.US):
            def _populate(self, year):
                holidays.US._populate(self, year)
                self.pop(date(year, 10, 1) + rd(weekday=MO(+2)))

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

    def test_get_named_contains(self):
        us = holidays.UnitedStates(years=2020)

        holidays_count = len(us.keys())
        for name in ("New", "Year"):
            self.assertIn(date(2020, 1, 1), us.get_named(name))
        for name in ("new", "year", "NEW Year"):
            self.assertNotIn(
                date(2020, 1, 1), us.get_named(name, lookup="contains")
            )
        self.assertEqual(holidays_count, len(us.keys()))

        us = holidays.UnitedStates(years=2022)
        self.assertEqual(
            1, len(us.get_named("Thanksgiving", lookup="contains"))
        )
        self.assertEqual(1, len(us.get_named("Thanksgivi", lookup="contains")))
        self.assertEqual(0, len(us.get_named("thanks", lookup="contains")))
        self.assertEqual([2022], list(us.years))

        us = holidays.UnitedStates(observed=False, years=2022)
        self.assertEqual(
            2, len(us.get_named("Independence Day", lookup="contains"))
        )
        self.assertEqual(
            0, len(us.get_named("independence day", lookup="contains"))
        )

    def test_get_named_exact(self):
        us = holidays.UnitedStates(years=2020)
        holidays_count = len(us.keys())
        for name in ("New Year's Day", "Christmas Day"):
            self.assertEqual(1, len(us.get_named(name)))
        for name in ("New", "Day"):
            self.assertEqual(0, len(us.get_named(name, lookup="exact")))
        self.assertEqual(holidays_count, len(us.keys()))

        us = holidays.UnitedStates(years=2022)
        self.assertEqual(1, len(us.get_named("Thanksgiving", lookup="exact")))
        self.assertEqual(0, len(us.get_named("thanksgiving", lookup="exact")))
        self.assertEqual([2022], list(us.years))

        us = holidays.UnitedStates(observed=False, years=2022)
        self.assertEqual(
            1, len(us.get_named("Independence Day", lookup="exact"))
        )

    def test_get_named_icontains(self):
        us = holidays.UnitedStates(years=2020)
        holidays_count = len(us.keys())
        self.assertEqual(holidays_count, len(us.keys()))
        for name in ("New", "Year", "new", "year", "NEW Year"):
            self.assertIn(date(2020, 1, 1), us.get_named(name))

        us = holidays.UnitedStates(years=2022)
        for name in ("Thanksgiving", "thanksgiving", "Thanksgivi"):
            self.assertEqual(1, len(us.get_named(name, lookup="icontains")))
        self.assertEqual([2022], list(us.years))

        us = holidays.UnitedStates(observed=False, years=2022)
        self.assertEqual(
            2, len(us.get_named("Independence Day", lookup="icontains"))
        )

    def test_get_named_iexact(self):
        us = holidays.UnitedStates(years=2020)
        holidays_count = len(us.keys())
        self.assertEqual(holidays_count, len(us.keys()))

        for name in ("new year's day", "New Year's Day"):
            self.assertIn(
                date(2020, 1, 1), us.get_named(name, lookup="iexact")
            )
        for name in ("New Year Day", "New Year", "year", "NEW Year"):
            self.assertNotIn(
                date(2020, 1, 1), us.get_named(name, lookup="iexact")
            )

        us = holidays.UnitedStates(years=2022)
        self.assertEqual(1, len(us.get_named("thanksgiving", lookup="iexact")))
        self.assertEqual(0, len(us.get_named("Thanksgivin", lookup="iexact")))
        self.assertEqual([2022], list(us.years))

        us = holidays.UnitedStates(years=2022)
        self.assertEqual(
            1, len(us.get_named("independence day", lookup="iexact"))
        )

    def test_get_named_istartswith(self):
        us = holidays.UnitedStates(years=2020)
        holidays_count = len(us.keys())
        self.assertEqual(holidays_count, len(us.keys()))

        for name in ("new year's", "New Year's", "New Year's day"):
            self.assertIn(
                date(2020, 1, 1), us.get_named(name, lookup="istartswith")
            )
        for name in (
            "New Year Day",
            "New Year holiday",
            "New Year's Day Holiday",
            "year",
        ):
            self.assertNotIn(
                date(2020, 1, 1), us.get_named(name, lookup="istartswith")
            )

        us = holidays.UnitedStates(years=2022)
        self.assertEqual(
            1, len(us.get_named("independence day", lookup="istartswith"))
        )

    def test_get_named_startswith(self):
        us = holidays.UnitedStates(years=2020)
        holidays_count = len(us.keys())
        self.assertEqual(holidays_count, len(us.keys()))

        for name in ("New Year's", "New Year"):
            self.assertIn(
                date(2020, 1, 1), us.get_named(name, lookup="startswith")
            )
        for name in (
            "New Year Day",
            "New Year Holiday",
            "New Year's Day Holiday",
            "year",
        ):
            self.assertNotIn(
                date(2020, 1, 1), us.get_named(name, lookup="startswith")
            )

        us = holidays.UnitedStates(years=2022)
        self.assertEqual(
            2, len(us.get_named("Christmas", lookup="startswith"))
        )
        self.assertEqual(
            1, len(us.get_named("Independence Day", lookup="startswith"))
        )

    def test_get_named_lookup_invalid(self):
        us = holidays.UnitedStates(years=2020)
        self.assertRaises(
            AttributeError,
            lambda: us.get_named("Holiday name", lookup="invalid"),
        )


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
        dt = datetime(2020, 1, 1)
        self.assertIn(dt, self.holidays)

        loaded_holidays = pickle.loads(pickle.dumps(self.holidays))
        self.assertEqual(loaded_holidays, self.holidays)
        self.assertIn(dt, self.holidays)

    def test_deprecation_warnings(self):
        with self.assertWarns(Warning):
            holidays.US(prov="AL")

        with self.assertWarns(Warning):
            holidays.US(state="WY")


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
            self.holidays[datetime(2014, 1, 1, 13, 45)],
            "New Year's Day",
        )
        self.holidays[datetime(2014, 1, 3, 1, 1)] = "Fake Holiday"
        self.assertIn(datetime(2014, 1, 3, 2, 2), self.holidays)
        self.assertEqual(
            self.holidays.pop(datetime(2014, 1, 3, 4, 4)),
            "Fake Holiday",
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
            (TypeError, ValueError),
            lambda: self.holidays.get("abc123"),
        )
        self.assertRaises(TypeError, lambda: self.holidays.get({"123"}))
        self.assertRaises(
            (TypeError, ValueError),
            self.holidays.__setitem__,
            "abc",
            "Test",
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


class TestCountrySpecialHolidays(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.country_holidays("US")

    def test_populate_special_holidays(self):
        self.holidays._populate(1111)  # special_holidays is empty.
        self.assertEqual(0, len(self.holidays))

        self.holidays.special_holidays = {
            1111: ((JAN, 1, "Test holiday"),),
            2222: ((FEB, 2, "Test holiday"),),
            3333: (),
        }

        self.assertNotIn(3333, self.holidays.years)

        self.assertIn("1111-01-01", self.holidays)
        self.assertIn("2222-02-02", self.holidays)
        self.assertEqual(13, len(self.holidays))

        self.holidays._populate(1111)
        self.holidays._populate(2222)
        self.assertIn("1111-01-01", self.holidays)
        self.assertIn("2222-02-02", self.holidays)
        self.assertEqual(13, len(self.holidays))


class TestHolidaysTranslation(unittest.TestCase):
    def test_language_unavailable(self):
        os.environ["LANGUAGE"] = "en_US"
        us_xx = holidays.country_holidays("CA", language="xx")
        self.assertEqual(us_xx["2022-01-01"], "New Year's Day")

        os.environ["LANGUAGE"] = "pl"
        pl_xx = holidays.country_holidays("PL", language="xx")
        self.assertEqual(pl_xx["2022-01-01"], "Nowy Rok")
