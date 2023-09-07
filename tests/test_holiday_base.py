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

import pickle
import unittest
from datetime import date, datetime
from datetime import timedelta as td

from holidays.calendars.gregorian import JAN, FEB, OCT, DEC, MON, TUE, SAT, SUN
from holidays.constants import HOLIDAY_NAME_DELIMITER, PUBLIC
from holidays.holiday_base import HolidayBase


class EntityStub(HolidayBase):
    special_holidays = {
        1111: (JAN, 1, "Test holiday"),
        2222: (FEB, 2, "Test holiday"),
        3333: ((FEB, 2, "Test holiday")),
        4444: (),
    }

    substituted_holidays = {
        1991: (
            (JAN, 12, JAN, 7),
            (1991, JAN, 13, JAN, 8),
        ),
    }
    substituted_date_format = "%d/%m/%Y"
    substituted_label = "From %s"
    supported_categories = {PUBLIC}

    def _add_observed(self, dt: date, before: bool = True, after: bool = True) -> None:
        if not self.observed:
            return None

        if self._is_saturday(dt) and before:
            self._add_holiday("%s (Observed)" % self[dt], dt + td(days=-1))
        elif self._is_sunday(dt) and after:
            self._add_holiday("%s (Observed)" % self[dt], dt + td(days=+1))

    def _populate(self, year: int) -> None:
        super()._populate(year)

        name = "New Year's Day"
        self._add_observed(self._add_holiday_jan_1(name), before=False)
        if self.observed and self._is_friday(DEC, 31):
            self._add_holiday_dec_31("%s (Observed)" % name)

        self._add_observed(self._add_holiday_jun_19("Juneteenth National Independence Day"))
        self._add_observed(self._add_holiday_jul_4("Independence Day"))
        self._add_holiday_4th_thu_of_nov("Thanksgiving")
        self._add_observed(self._add_holiday_dec_25("Christmas Day"))


class CountryStub1(EntityStub):
    country = "CS1"
    subdivisions = ("Subdiv1", "Subdiv2")

    def _add_subdiv_subdiv1_holidays(self):
        self._add_holiday_aug_10("Subdiv1 Custom Holiday")

    def _add_subdiv_subdiv2_holidays(self):
        self._add_holiday_aug_10("Subdiv2 Custom Holiday")


class CountryStub2(EntityStub):
    country = "CS2"
    subdivisions = ("Subdiv3", "Subdiv4")

    def _populate(self, year: int) -> None:
        super()._populate(year)
        self._add_holiday_mar_1("Custom March 1st Holiday")


class CountryStub3(HolidayBase):
    country = "CS3"

    def _populate(self, year: int) -> None:
        super()._populate(year)
        self._add_holiday_may_1("Custom May 1st Holiday")
        self._add_holiday_may_2("Custom May 2nd Holiday")


class MarketStub1(EntityStub):
    market = "MS1"


class MarketStub2(EntityStub):
    market = "MS2"


class TestArgs(unittest.TestCase):
    def test_categories(self):
        self.assertRaises(NotImplementedError, lambda: CountryStub1(categories=("HOME",)))

    def test_country(self):
        self.assertEqual(CountryStub1().country, "CS1")

    def test_expand(self):
        hb = CountryStub1(years=(2013, 2015), expand=False)
        self.assertFalse(hb.expand)
        self.assertSetEqual(hb.years, {2013, 2015})

        self.assertNotIn("2014-01-01", hb)
        self.assertSetEqual(hb.years, {2013, 2015})

    def test_observed(self):
        hb = CountryStub1(observed=False)
        self.assertFalse(hb.observed)
        self.assertIn("2000-01-01", hb)
        self.assertNotIn("1999-12-31", hb)
        self.assertIn("2012-01-01", hb)
        self.assertNotIn("2012-01-02", hb)

        hb.observed = True
        self.assertIn("2000-01-01", hb)
        self.assertIn("1999-12-31", hb)
        self.assertIn("2012-01-01", hb)
        self.assertIn("2012-01-02", hb)

        hb.observed = False
        self.assertIn("2000-01-01", hb)
        self.assertNotIn("1999-12-31", hb)
        self.assertIn("2012-01-01", hb)
        self.assertNotIn("2012-01-02", hb)

    def test_subdiv(self):
        self.assertEqual(CountryStub1(subdiv="Subdiv1").subdiv, "Subdiv1")

    def test_years(self):
        hb = HolidayBase()
        self.assertSetEqual(hb.years, set())

        self.assertNotIn("2014-01-02", hb)
        self.assertSetEqual(hb.years, {2014})

        self.assertNotIn("2013-01-02", hb)
        self.assertNotIn("2014-01-02", hb)
        self.assertNotIn("2015-01-02", hb)
        self.assertSetEqual(hb.years, {2013, 2014, 2015})

        self.assertSetEqual(
            HolidayBase(years=range(2010, 2016)).years, {2010, 2011, 2012, 2013, 2014, 2015}
        )
        self.assertSetEqual(HolidayBase(years=(2013, 2015, 2015)).years, {2013, 2015})
        self.assertSetEqual(HolidayBase(years=2015).years, {2015})


class TestDeprecationWarnings(unittest.TestCase):
    def test_prov_deprecation(self):
        with self.assertWarns(Warning):
            CountryStub1(prov="Subdiv1")

    def test_state_deprecation(self):
        with self.assertWarns(Warning):
            CountryStub1(state="Subdiv1")


class TestEqualityInequality(unittest.TestCase):
    def test_eq(self):
        hb_1 = CountryStub1()
        hb_2 = CountryStub2()
        hb_3 = CountryStub1(subdiv="Subdiv1")

        self.assertEqual(hb_1, hb_1)
        self.assertEqual(hb_2, hb_2)
        self.assertEqual(hb_3, hb_3)

        hb_4 = CountryStub1(years=2014)
        hb_5 = CountryStub1(years=2014)
        self.assertEqual(hb_4, hb_5)
        self.assertEqual(hb_5, hb_4)

        hb_6 = CountryStub2(years=(2014, 2015))
        hb_7 = CountryStub2(years=(2014, 2015))
        self.assertEqual(hb_6, hb_7)
        self.assertEqual(hb_7, hb_6)

        hb_8 = CountryStub3(language="fr")
        hb_9 = CountryStub3(language="fr")
        self.assertEqual(hb_8, hb_9)
        self.assertEqual(hb_9, hb_8)

        # Use assertFalse instead of assertNotEqual as we want to check "==" explicitly.
        self.assertFalse(hb_1 == {})
        self.assertFalse(hb_2 == {})
        self.assertFalse(hb_3 == {})
        self.assertFalse(hb_1 == hb_2)
        self.assertFalse(hb_2 == hb_1)
        self.assertFalse(hb_1 == hb_3)
        self.assertFalse(hb_3 == hb_1)
        self.assertFalse(hb_2 == hb_3)
        self.assertFalse(hb_3 == hb_2)

    def test_ne(self):
        hb_1 = CountryStub1()
        hb_2 = CountryStub2()
        hb_3 = CountryStub1(subdiv="Subdiv1")

        self.assertNotEqual(hb_1, {})
        self.assertNotEqual(hb_2, {})
        self.assertNotEqual(hb_3, {})
        self.assertNotEqual(hb_1, hb_2)
        self.assertNotEqual(hb_2, hb_1)
        self.assertNotEqual(hb_1, hb_3)
        self.assertNotEqual(hb_3, hb_1)
        self.assertNotEqual(hb_2, hb_3)
        self.assertNotEqual(hb_3, hb_2)

        hb_4 = CountryStub1(years=2014)
        hb_5 = CountryStub2(years=2015)
        self.assertNotEqual(hb_1, hb_4)
        self.assertNotEqual(hb_4, hb_1)
        self.assertNotEqual(hb_2, hb_5)
        self.assertNotEqual(hb_5, hb_2)
        self.assertNotEqual(hb_4, hb_5)
        self.assertNotEqual(hb_5, hb_4)

        hb_6 = CountryStub1(years=2014, subdiv="Subdiv1")
        hb_7 = CountryStub1(years=2014, subdiv="Subdiv2")
        self.assertNotEqual(hb_6, hb_7)
        self.assertNotEqual(hb_7, hb_6)

        hb_8 = CountryStub1(years=2014)
        hb_9 = CountryStub1(years=2014, language="fr")
        self.assertNotEqual(hb_8, hb_9)
        self.assertNotEqual(hb_9, hb_8)

        # Use assertFalse instead of assertEqual in order to check "!=" explicitly.
        self.assertFalse(hb_1 != hb_1)
        self.assertFalse(hb_2 != hb_2)
        self.assertFalse(hb_3 != hb_3)


class TestGetList(unittest.TestCase):
    def test_get_list_multiple_countries(self):
        hb_country_1 = CountryStub1(years=2021)
        hb_country_2 = CountryStub1(years=2021)
        hb_country_1._add_holiday_dec_20("Custom Holiday 1")
        hb_country_2._add_holiday_dec_20("Custom Holiday 2")

        self.assertEqual(hb_country_1["2021-12-20"], "Custom Holiday 1")
        self.assertEqual(hb_country_2["2021-12-20"], "Custom Holiday 2")
        self.assertListEqual(hb_country_1.get_list("2021-12-20"), ["Custom Holiday 1"])
        self.assertListEqual(hb_country_2.get_list("2021-12-20"), ["Custom Holiday 2"])

        hb_combined = hb_country_1 + hb_country_2
        self.assertEqual(hb_combined["2021-12-20"], "Custom Holiday 1; Custom Holiday 2")
        self.assertListEqual(
            hb_combined.get_list("2021-12-20"), ["Custom Holiday 1", "Custom Holiday 2"]
        )

    def test_get_list_multiple_subdivisions(self):
        hb_subdiv_1 = CountryStub1(subdiv="Subdiv1", years=2021)
        hb_subdiv_2 = CountryStub1(subdiv="Subdiv2", years=2021)
        self.assertEqual(hb_subdiv_1["2021-08-10"], "Subdiv1 Custom Holiday")
        self.assertEqual(hb_subdiv_2["2021-08-10"], "Subdiv2 Custom Holiday")
        self.assertListEqual(hb_subdiv_1.get_list("2021-08-10"), ["Subdiv1 Custom Holiday"])
        self.assertListEqual(hb_subdiv_2.get_list("2021-08-10"), ["Subdiv2 Custom Holiday"])

        hb_combined = hb_subdiv_1 + hb_subdiv_2
        self.assertEqual(
            hb_combined["2021-08-10"], "Subdiv1 Custom Holiday; Subdiv2 Custom Holiday"
        )
        self.assertListEqual(
            hb_combined.get_list("2021-08-10"),
            ["Subdiv1 Custom Holiday", "Subdiv2 Custom Holiday"],
        )


class TestGetNamed(unittest.TestCase):
    def test_contains(self):
        hb = CountryStub1(years=2022)
        for name in ("New", "Year"):
            self.assertListEqual(hb.get_named(name, lookup="contains"), [date(2022, 1, 1)])
        self.assertListEqual(
            hb.get_named("Independence Day", lookup="contains"),
            [date(2022, 6, 19), date(2022, 6, 20), date(2022, 7, 4)],
        )
        self.assertListEqual(hb.get_named("independence day", lookup="contains"), [])
        self.assertListEqual(hb.get_named("Thanksgiving", lookup="contains"), [date(2022, 11, 24)])
        self.assertListEqual(hb.get_named("Thanksgivi", lookup="contains"), [date(2022, 11, 24)])
        self.assertListEqual(hb.get_named("thanks", lookup="contains"), [])
        self.assertSetEqual(hb.years, {2022})

        hb = CountryStub1(observed=False, years=2022)
        self.assertListEqual(
            hb.get_named("Independence Day", lookup="contains"),
            [date(2022, 6, 19), date(2022, 7, 4)],
        )
        self.assertListEqual(hb.get_named("independence day", lookup="contains"), [])
        self.assertSetEqual(hb.years, {2022})

    def test_exact(self):
        hb = CountryStub1(years=2022)
        for name in ("New", "Day"):
            self.assertListEqual(hb.get_named(name, lookup="exact"), [])
        self.assertListEqual(hb.get_named("Independence Day", lookup="exact"), [date(2022, 7, 4)])
        self.assertListEqual(hb.get_named("Thanksgiving", lookup="exact"), [date(2022, 11, 24)])
        self.assertListEqual(hb.get_named("thanksgiving", lookup="exact"), [])
        self.assertSetEqual(hb.years, {2022})

        hb = CountryStub1(observed=False, years=2022)
        self.assertListEqual(hb.get_named("Independence Day", lookup="exact"), [date(2022, 7, 4)])
        self.assertSetEqual(hb.years, {2022})

    def test_icontains(self):
        hb = CountryStub1(years=2022)
        for name in ("Thanksgiving", "thanksgiving", "Thanksgivi"):
            self.assertListEqual(hb.get_named(name, lookup="icontains"), [date(2022, 11, 24)])
        self.assertListEqual(
            hb.get_named("Independence Day", lookup="icontains"),
            [date(2022, 6, 19), date(2022, 6, 20), date(2022, 7, 4)],
        )
        self.assertSetEqual(hb.years, {2022})

        hb = CountryStub1(observed=False, years=2022)
        self.assertListEqual(
            hb.get_named("Independence Day", lookup="icontains"),
            [date(2022, 6, 19), date(2022, 7, 4)],
        )
        self.assertSetEqual(hb.years, {2022})

    def test_iexact(self):
        hb = CountryStub1(years=2022)
        for name in ("new year's day", "New Year's Day"):
            self.assertListEqual(hb.get_named(name, lookup="iexact"), [date(2022, 1, 1)])
        for name in ("New Year Day", "New Year", "year", "NEW Year"):
            self.assertListEqual(hb.get_named(name, lookup="iexact"), [])
        self.assertListEqual(hb.get_named("independence day", lookup="iexact"), [date(2022, 7, 4)])
        self.assertListEqual(hb.get_named("thanksgiving", lookup="iexact"), [date(2022, 11, 24)])
        self.assertListEqual(hb.get_named("Thanksgivin", lookup="iexact"), [])
        self.assertSetEqual(hb.years, {2022})

        hb = CountryStub1(observed=False, years=2022)
        self.assertListEqual(hb.get_named("independence day", lookup="iexact"), [date(2022, 7, 4)])
        self.assertSetEqual(hb.years, {2022})

    def test_invalid(self):
        hb = CountryStub1(years=2022)
        self.assertRaises(
            AttributeError, lambda: hb.get_named("Independence Day", lookup="invalid")
        )

    def test_istartswith(self):
        hb = CountryStub1(years=2022)
        for name in ("new year's", "New Year's", "New Year's day"):
            self.assertListEqual(hb.get_named(name, lookup="istartswith"), [date(2022, 1, 1)])
        for name in ("New Year Day", "New Year holiday", "New Year's Day Holiday", "year"):
            self.assertListEqual(hb.get_named(name, lookup="istartswith"), [])
        self.assertListEqual(
            hb.get_named("independence day", lookup="istartswith"), [date(2022, 7, 4)]
        )
        self.assertSetEqual(hb.years, {2022})

        hb = CountryStub1(observed=False, years=2022)
        self.assertListEqual(
            hb.get_named("independence day", lookup="istartswith"), [date(2022, 7, 4)]
        )
        self.assertSetEqual(hb.years, {2022})

    def test_startswith(self):
        hb = CountryStub1(years=2022)
        for name in ("New Year's", "New Year"):
            self.assertListEqual(hb.get_named(name, lookup="startswith"), [date(2022, 1, 1)])
        for name in ("New Year Day", "New Year Holiday", "New Year's Day Holiday", "year"):
            self.assertListEqual(hb.get_named(name, lookup="startswith"), [])
        self.assertListEqual(
            hb.get_named("Independence Day", lookup="startswith"), [date(2022, 7, 4)]
        )
        self.assertListEqual(
            hb.get_named("Christmas", lookup="startswith"),
            [date(2022, 12, 25), date(2022, 12, 26)],
        )
        self.assertSetEqual(hb.years, {2022})

        hb = CountryStub1(observed=False, years=2022)
        self.assertListEqual(
            hb.get_named("Independence Day", lookup="startswith"), [date(2022, 7, 4)]
        )
        self.assertListEqual(hb.get_named("Christmas", lookup="startswith"), [date(2022, 12, 25)])
        self.assertSetEqual(hb.years, {2022})


class TestHelperMethods(unittest.TestCase):
    def setUp(self):
        self.hb = CountryStub1()

    def test_add_holiday(self):
        self.hb._populate(2023)
        self.hb._add_holiday("Test 1", date(2023, JAN, 5))
        self.hb._add_holiday("Test 2", (JAN, 6))
        self.hb._add_holiday_jan_7("Test 3")

        self.assertIn("2023-01-05", self.hb)
        self.assertIn("2023-01-06", self.hb)
        self.assertIn("2023-01-07", self.hb)

        for args in (
            (date(2020, JAN, 5),),
            (JAN, 5, "Test 1", True),
            ("Test", "Test"),
        ):
            self.assertRaises(TypeError, lambda: self.hb._add_holiday(*args))

    def test_is_leap_year(self):
        self.hb._populate(1999)
        self.assertFalse(self.hb._is_leap_year())

        self.hb._populate(2000)
        self.assertTrue(self.hb._is_leap_year())

        self.hb._populate(2004)
        self.assertTrue(self.hb._is_leap_year())

        self.hb._populate(2200)
        self.assertFalse(self.hb._is_leap_year())

    def test_is_weekend(self):
        self.hb._populate(2022)
        dts = (date(2022, 10, 3), date(2022, 10, 4), (OCT, 3), (OCT, 4))

        self.hb.weekend = {MON, TUE}
        for dt in dts:
            self.assertTrue(self.hb._is_weekend(dt))

        self.hb.weekend = {}
        for dt in dts:
            self.assertFalse(self.hb._is_weekend(dt))

        self.hb.weekend = {SAT, SUN}
        for dt in (date(2022, 10, 1), date(2022, 10, 2)):
            self.assertTrue(self.hb._is_weekend(dt))
        for dt in ((OCT, 1), (OCT, 2)):
            self.assertTrue(self.hb._is_weekend(dt))
            self.assertTrue(self.hb._is_weekend(*dt))

        for dt in (date(2022, 10, 3), date(2022, 10, 4)):
            self.assertFalse(self.hb._is_weekend(dt))
        for dt in ((OCT, 3), (OCT, 4)):
            self.assertFalse(self.hb._is_weekend(dt))
            self.assertFalse(self.hb._is_weekend(*dt))


class TestHolidaySum(unittest.TestCase):
    def setUp(self) -> None:
        self.hb_1 = CountryStub1(years=2014)
        self.hb_2 = CountryStub2(years=2015)
        self.hb_3 = CountryStub3()
        self.hb_combined = self.hb_1 + self.hb_2 + self.hb_3

    def assertAdded(self):
        self.assertNotIn("2014-03-01", self.hb_1)
        self.assertNotIn("2014-05-01", self.hb_1)
        self.assertNotIn("2014-05-02", self.hb_1)
        self.assertIn("2014-03-01", self.hb_2)
        self.assertIn("2014-05-01", self.hb_3)
        self.assertIn("2014-05-02", self.hb_3)

        self.assertIn("2014-07-04", self.hb_1)
        self.assertIn("2014-07-04", self.hb_1 + self.hb_2)
        self.assertIn("2014-07-04", self.hb_2 + self.hb_1)
        self.assertIn("2015-07-04", self.hb_1 + self.hb_2)
        self.assertIn("2015-07-04", self.hb_2 + self.hb_1)

        self.assertIn("2000-03-01", self.hb_combined)
        self.assertIn("2000-05-01", self.hb_combined)
        self.assertIn("2000-05-02", self.hb_combined)
        self.assertIn("2000-07-04", self.hb_combined)
        self.assertIn("2000-07-04", self.hb_combined)

    def test_add_country(self):
        self.assertAdded()

        self.hb_combined = CountryStub1(years=2014)
        self.hb_combined += CountryStub2(years=2015)
        self.hb_combined += CountryStub3()
        self.assertAdded()

        self.hb_combined = (
            self.hb_1
            + (self.hb_2 + self.hb_3)
            + self.hb_1
            + (self.hb_3 + self.hb_2 + CountryStub2(subdiv="Subdiv4"))
        )
        self.assertAdded()

        self.hb_combined = CountryStub1(years=2014, subdiv="Subdiv1")
        self.hb_combined += CountryStub1(years=2014, subdiv="Subdiv2")
        self.assertEqual(
            self.hb_combined["2014-08-10"], "Subdiv1 Custom Holiday; Subdiv2 Custom Holiday"
        )

        self.assertRaises(TypeError, lambda: self.hb_1 + {})

    def test_add_financial(self):
        hb_1 = MarketStub1(years=2013)
        hb_2 = MarketStub2(years=(2014, 2015))
        hb_combined = hb_1 + hb_2

        self.assertIn("2013-01-01", hb_1)
        self.assertIn("2014-01-01", hb_2)
        self.assertIn("2015-01-01", hb_2)
        self.assertIn("2013-01-01", hb_combined)
        self.assertIn("2014-01-01", hb_combined)
        self.assertIn("2015-01-01", hb_combined)
        self.assertListEqual(hb_combined.market, ["MS1", "MS2"])

    def test_args(self):
        self.hb_1 = CountryStub1(years=2014, subdiv="Subdiv1")
        self.hb_2 = CountryStub2(years=2015, subdiv="Subdiv3")
        self.assertListEqual(self.hb_combined.country, ["CS1", "CS2", "CS3"])
        self.assertListEqual((self.hb_1 + self.hb_2).subdiv, ["Subdiv1", "Subdiv3"])
        self.assertListEqual((self.hb_2 + self.hb_1).subdiv, ["Subdiv3", "Subdiv1"])
        self.assertEqual((self.hb_1 + self.hb_3).subdiv, "Subdiv1")

        self.assertTrue((self.hb_2 + self.hb_3).expand)
        self.assertSetEqual((self.hb_2 + self.hb_3).years, {2014, 2015})
        self.assertSetEqual((self.hb_3 + self.hb_2).years, {2014, 2015})

        self.hb_combined = sum(CountryStub1(subdiv=subdiv) for subdiv in CountryStub1.subdivisions)
        self.assertEqual(self.hb_combined.country, CountryStub1.country)
        self.assertEqual(self.hb_combined.subdiv, list(CountryStub1.subdivisions))


class TestInheritance(unittest.TestCase):
    def setUp(self):
        self.hb = CountryStub1()

    def test_custom_holidays(self):
        class CustomHolidays(CountryStub1):
            def _populate(self, year):
                super()._populate(year)
                self._add_holiday_jul_13("Ninja Turtle's Day")
                self._add_holiday_dec_31("New Year's Eve")
                del self[date(year, JAN, 1)]

        hb = CustomHolidays(years=(2014, 2020))
        self.assertIn("2014-01-01", self.hb)
        self.assertNotIn("2014-01-01", hb)
        self.assertIn("2014-12-31", hb)
        self.assertNotIn("2014-12-31", self.hb)

        self.assertIn("2020-01-01", self.hb)
        self.assertNotIn("2020-01-01", hb)
        self.assertIn("2020-12-31", hb)
        self.assertNotIn("2020-12-31", self.hb)

        self.assertNotIn("2014-07-13", self.hb)
        self.assertIn("2014-07-13", hb)
        self.assertNotIn("2020-07-13", self.hb)
        self.assertIn("2020-07-13", hb)


class TestKeyTransforms(unittest.TestCase):
    def setUp(self):
        self.hb = CountryStub1()

    def test_date(self):
        dt = date(2014, 1, 1)
        self.assertIn(dt, self.hb)
        self.assertEqual(self.hb[dt], "New Year's Day")

        dt = date(2014, 1, 3)
        self.hb[dt] = "Fake Holiday"
        self.assertIn(dt, self.hb)
        self.assertEqual(self.hb.pop(dt), "Fake Holiday")
        self.assertNotIn(dt, self.hb)

    def test_date_subclass(self):
        class CustomDateType(date):
            pass

        self.assertTrue(issubclass(CustomDateType, date))
        self.assertIn(CustomDateType(2014, 1, 1), self.hb)
        self.assertNotIn(CustomDateType(2014, 1, 3), self.hb)

    def test_datetime(self):
        self.assertIn(datetime(2014, 1, 1, 13, 45), self.hb)
        self.assertEqual(self.hb[datetime(2014, 1, 1, 13, 45)], "New Year's Day")

        self.hb[datetime(2014, 1, 3, 1, 1)] = "Fake Holiday"
        self.assertIn(datetime(2014, 1, 3, 2, 2), self.hb)
        self.assertEqual(self.hb.pop(datetime(2014, 1, 3, 4, 4)), "Fake Holiday")
        self.assertNotIn(datetime(2014, 1, 3, 2, 2), self.hb)

    def test_exception(self):
        self.assertRaises((TypeError, ValueError), lambda: "abc" in self.hb)
        self.assertRaises((TypeError, ValueError), lambda: self.hb.get("abc123"))
        self.assertRaises(TypeError, lambda: self.hb.get({"123"}))
        self.assertRaises((TypeError, ValueError), self.hb.__setitem__, "abc", "Test")
        self.assertRaises((TypeError, ValueError), lambda: {} in self.hb)

    def test_string(self):
        self.assertIn("2014-01-01", self.hb)
        self.assertEqual(self.hb["2014-01-01"], "New Year's Day")
        self.assertIn("01/01/2014", self.hb)
        self.assertEqual(self.hb["01/01/2014"], "New Year's Day")

        self.hb["01/03/2014"] = "Fake Holiday"
        self.assertIn("01/03/2014", self.hb)
        self.assertNotIn("03/01/2014", self.hb)
        self.assertIn("2014-01-03", self.hb)
        self.assertNotIn("2014-03-01", self.hb)
        self.assertEqual(self.hb.pop("01/03/2014"), "Fake Holiday")

    def test_timestamp(self):
        self.assertIn(1388552400, self.hb)
        self.assertEqual(self.hb[1388552400], "New Year's Day")
        self.assertIn(1388552400.01, self.hb)
        self.assertEqual(self.hb[1388552400.01], "New Year's Day")

        self.hb[1388725200] = "Fake Holiday"
        self.assertIn(1388725201, self.hb)
        self.assertEqual(self.hb.pop(1388725202), "Fake Holiday")
        self.assertNotIn(1388725201, self.hb)


class TestPop(unittest.TestCase):
    def setUp(self):
        self.hb = CountryStub1()

    def test_exception(self):
        self.assertRaises(KeyError, lambda: self.hb.pop("2014-01-02"))

        self.hb.pop("2014-01-01")
        self.assertRaises(KeyError, lambda: self.hb.pop("2014-01-01"))

    def test_success(self):
        self.assertFalse(self.hb.pop("2014-01-02", False))
        self.assertTrue(self.hb.pop("2014-01-02", True))
        self.assertIn("2014-01-01", self.hb)
        self.assertEqual(self.hb.pop("2014-01-01"), "New Year's Day")
        self.assertNotIn("2014-01-01", self.hb)


class TestPopNamed(unittest.TestCase):
    def setUp(self):
        self.hb = CountryStub1()

    def test_exception(self):
        self.assertRaises(KeyError, lambda: self.hb.pop_named("New Year's Dayz"))

        self.assertIn("2014-01-01", self.hb)
        self.hb.pop_named("New Year's Day")
        self.assertRaises(KeyError, lambda: self.hb.pop_named("New Year's Day"))

    def test_single(self):
        self.assertIn("2014-01-01", self.hb)
        for dt in self.hb.pop_named("New Year's Day"):
            self.assertNotIn(dt, self.hb)

    def test_multiple(self):
        dt = date(2022, 2, 22)
        holiday_name_1 = "Holiday Name 1"
        holiday_name_2 = "Holiday Name 2"
        holiday_name_3 = "Holiday Name 3"
        combined_name = HOLIDAY_NAME_DELIMITER.join(
            (holiday_name_1, holiday_name_2, holiday_name_3)
        )
        self.hb[dt] = holiday_name_1
        self.hb[dt] = holiday_name_2
        self.hb[dt] = holiday_name_3
        self.assertEqual(self.hb[dt], combined_name)

        # Pop the entire date by multiple holidays exact name.
        self.hb.pop_named(combined_name)
        self.assertNotIn(dt, self.hb)

        # Pop only one holiday by a single name.
        self.hb[dt] = holiday_name_1
        self.hb[dt] = holiday_name_2
        self.hb[dt] = holiday_name_3

        # 3 holidays names.
        self.assertEqual(self.hb[dt], combined_name)

        self.hb.pop_named(holiday_name_1)
        # 2 holiday names.
        self.assertEqual(
            self.hb[dt], HOLIDAY_NAME_DELIMITER.join((holiday_name_2, holiday_name_3))
        )

        self.hb.pop_named(holiday_name_3)
        # 1 holiday name.
        self.assertEqual(self.hb[dt], holiday_name_2)

        self.hb.pop_named(holiday_name_2)
        # 0 holiday names.
        self.assertNotIn(dt, self.hb)

    def test_partial(self):
        self.assertIn("2014-01-01", self.hb)
        for dt in self.hb.pop_named("N"):
            self.assertNotIn(dt, self.hb)
        self.assertRaises(KeyError, lambda: self.hb.pop_named("New Year"))


class TestRepr(unittest.TestCase):
    def test_country(self):
        hb = CountryStub1()
        self.assertEqual(repr(hb), "holidays.country_holidays('CS1')")

        hb = CountryStub1(subdiv="Subdiv1")
        self.assertEqual(repr(hb), "holidays.country_holidays('CS1', subdiv='Subdiv1')")

    def test_market(self):
        self.assertEqual(repr(MarketStub1()), "holidays.financial_holidays('MS1')")


class TestSerialization(unittest.TestCase):
    def setUp(self):
        self.hb = CountryStub1()

    def test_pickle(self):
        dt = "2020-01-01"
        self.assertIn(dt, self.hb)

        loaded_holidays = pickle.loads(pickle.dumps(self.hb))
        self.assertEqual(loaded_holidays, self.hb)
        self.assertIn(dt, self.hb)


class TestSpecialHolidays(unittest.TestCase):
    def setUp(self):
        self.hb = CountryStub1()

    def test_populate_special_holidays(self):
        self.assertSetEqual(self.hb.years, set())

        self.hb._populate(1111)
        self.assertSetEqual(self.hb.years, {1111})
        self.assertIn("1111-01-01", self.hb)
        self.assertIn("2222-02-02", self.hb)
        self.assertIn("3333-02-02", self.hb)
        self.assertSetEqual(self.hb.years, {1111, 2222, 3333})


class TestStandardMethods(unittest.TestCase):
    def setUp(self):
        self.hb = CountryStub1()

    def test_append(self):
        self.hb.append([date(2015, 4, 1), "2015-04-03"])
        self.hb.append(date(2015, 4, 6))
        self.hb.append("2015-04-07")

        for dt in (
            "2015-01-01",
            "2015-04-01",
            "2015-04-03",
            "2015-04-06",
            "2015-04-07",
            "2015-12-25",
        ):
            self.assertIn(dt, self.hb)

        for dt in (
            "2015-04-04",
            "2015-04-05",
            "2015-04-02",
        ):
            self.assertNotIn(dt, self.hb)

    def test_bool(self):
        self.assertFalse(self.hb)
        self.assertEqual(bool(self.hb), False)
        self.assertEqual(len(self.hb), 0)

        self.assertIn("2014-01-01", self.hb)
        self.assertTrue(self.hb)
        self.assertEqual(bool(self.hb), True)
        self.assertNotEqual(len(self.hb), 0)

    def test_contains(self):
        self.assertIn("2014-01-01", self.hb)
        self.assertNotIn("2014-01-03", self.hb)

    def test_copy(self):
        hb = CountryStub1()
        self.assertEqual(hb, hb.copy())

        hb_fr = CountryStub1(language="fr")
        hb_xx = CountryStub1(language="xx")
        self.assertNotEqual(hb, hb_fr)
        self.assertNotEqual(hb.copy(), hb_fr.copy())

        self.assertNotEqual(hb, hb_xx)
        self.assertNotEqual(hb.copy(), hb_xx.copy())

    def test_get(self):
        self.assertEqual(self.hb.get("2014-01-01"), "New Year's Day")
        self.assertIsNone(self.hb.get("2014-01-03"))
        self.assertFalse(self.hb.get("2014-01-03", False))
        self.assertTrue(self.hb.get("2014-01-03", True))

    def test_getattr(self):
        self.hb._populate(2023)

        name = "Test"
        self.assertEqual(self.hb._add_holiday_3rd_mon_of_jun(name), date(2023, 6, 19))
        self.assertEqual(self.hb._add_holiday_4th_fri_of_aug(name), date(2023, 8, 25))
        self.assertEqual(self.hb._add_holiday_1st_wed_of_aug(name), date(2023, 8, 2))
        self.assertEqual(self.hb._add_holiday_1st_mon_before_may_24(name), date(2023, 5, 22))
        self.assertEqual(self.hb._add_holiday_1st_sun_from_aug_31(name), date(2023, 9, 3))

        self.assertRaises(ValueError, lambda: self.hb._add_holiday_5th_fri_of_aug(name))
        self.assertRaises(AttributeError, lambda: self.hb._add_holiday_4th_nam_of_aug(name))
        self.assertRaises(AttributeError, lambda: self.hb._add_holiday_nam_12(name))
        self.assertRaises(AttributeError, lambda: self.hb._add_holiday_1st_fri_before_nam_29(name))
        self.assertRaises(AttributeError, lambda: self.hb._add_holiday_1st_fri_random_jan_29(name))

    def test_getitem(self):
        self.assertEqual(self.hb["2014-01-01"], "New Year's Day")
        self.assertEqual(self.hb.get("2014-01-01"), "New Year's Day")
        self.assertIsNone(self.hb.get("2014-01-03"))
        self.assertRaises(KeyError, lambda: self.hb["2014-01-03"])

        self.assertListEqual(self.hb["2013-12-31":"2014-01-02"], [date(2014, 1, 1)])
        self.assertListEqual(
            self.hb["2013-12-24":"2014-01-02"], [date(2013, 12, 25), date(2014, 1, 1)]
        )
        self.assertListEqual(self.hb["2013-12-25":"2014-01-02":3], [date(2013, 12, 25)])
        self.assertListEqual(
            self.hb["2013-12-25":"2014-01-02":7], [date(2013, 12, 25), date(2014, 1, 1)]
        )
        self.assertListEqual(self.hb["2014-01-02":"2013-12-30"], [date(2014, 1, 1)])
        self.assertListEqual(self.hb["2014-01-02":"2013-12-25"], [date(2014, 1, 1)])
        self.assertListEqual(
            self.hb["2014-01-02":"2013-12-24"], [date(2014, 1, 1), date(2013, 12, 25)]
        )
        self.assertListEqual(self.hb["2014-01-01":"2013-12-24":3], [date(2014, 1, 1)])
        self.assertListEqual(
            self.hb["2014-01-01":"2013-12-24":7],
            [date(2014, 1, 1), date(2013, 12, 25)],
        )
        self.assertListEqual(self.hb["2013-12-31":"2014-01-02":-3], [])
        self.assertListEqual(self.hb["2014-01-01" : "2013-12-24" : td(days=3)], [date(2014, 1, 1)])
        self.assertListEqual(
            self.hb["2014-01-01" : "2013-12-24" : td(days=7)],
            [date(2014, 1, 1), date(2013, 12, 25)],
        )
        self.assertListEqual(self.hb["2013-12-31" : "2014-01-02" : td(days=3)], [])

        self.assertRaises(ValueError, lambda: self.hb["2014-01-01":])
        self.assertRaises(ValueError, lambda: self.hb[:"2014-01-01"])
        self.assertRaises(TypeError, lambda: self.hb["2014-01-01":"2014-01-02":""])
        self.assertRaises(ValueError, lambda: self.hb["2014-01-01":"2014-01-02":0])

    def test_radd(self):
        self.assertRaises(TypeError, lambda: 1 + CountryStub1())

    def test_setitem(self):
        self.assertEqual(len(self.hb), 0)
        self.hb["2014-01-03"] = "Custom Holiday"
        self.assertGreater(len(self.hb), 0)
        self.assertIn("2014-01-03", self.hb)
        self.assertEqual(self.hb["2014-01-03"], "Custom Holiday")

    def test_update(self):
        self.hb.update(
            {
                "2015-01-10": "Custom Holiday",
                "2015-01-11": "Custom Holiday",
            }
        )
        self.assertIn("2015-01-10", self.hb)
        self.assertIn("2015-01-11", self.hb)
        self.assertEqual(self.hb["2015-01-10"], "Custom Holiday")
        self.assertEqual(self.hb["2015-01-11"], "Custom Holiday")

        self.hb.update(
            {
                date(2015, 1, 10): "New Holiday",
                date(2015, 1, 11): "New Holiday",
            }
        )
        self.assertIn(date(2015, 1, 10), self.hb)
        self.assertIn(date(2015, 1, 11), self.hb)
        self.assertEqual(self.hb["2015-01-10"], "Custom Holiday; New Holiday")
        self.assertEqual(self.hb["2015-01-11"], "Custom Holiday; New Holiday")


class TestStr(unittest.TestCase):
    def test_country(self):
        hb = CountryStub1()

        self.assertEqual(
            str(hb),
            "{'country': CS1, 'expand': True, 'language': None, "
            "'market': None, 'observed': True, 'subdiv': None, "
            "'years': set()}",
        )

        hb._populate(2013)
        self.assertEqual(
            str(hb),
            '{datetime.date(2013, 1, 1): "New Year\'s Day", '
            "datetime.date(2013, 6, 19): 'Juneteenth National Independence Day', "
            "datetime.date(2013, 7, 4): 'Independence Day', "
            "datetime.date(2013, 11, 28): 'Thanksgiving', "
            "datetime.date(2013, 12, 25): 'Christmas Day'}",
        )

    def test_market(self):
        self.assertEqual(
            str(MarketStub1()),
            "{'country': None, 'expand': True, 'language': None, "
            "'market': MS1, 'observed': True, 'subdiv': None, "
            "'years': set()}",
        )


class TestSubstitutedHolidays(unittest.TestCase):
    class SubstitutedHolidays(HolidayBase):
        country = "HB"
        substituted_holidays = {
            1991: (
                (JAN, 12, JAN, 7),
                (1991, JAN, 13, JAN, 8),
            ),
        }

    def test_populate_substituted_holidays(self):
        hb = CountryStub1(years=1991)
        self.assertIn("1991-01-07", hb)
        self.assertIn("1991-01-08", hb)
        self.assertIn("12/01/1991", hb["1991-01-07"])
        self.assertIn("13/01/1991", hb["1991-01-08"])

    def test_no_substituted_date_format(self):
        hb = self.SubstitutedHolidays()
        hb.substituted_date_format = "%d/%m/%Y"
        self.assertRaises(ValueError, lambda: hb._populate(1991))

    def test_no_substituted_holidays(self):
        hb = CountryStub1()
        hb.substituted_holidays = {}
        hb._populate(1991)
        self.assertNotIn("1991-01-07", hb)
        self.assertNotIn("1991-01-08", hb)

    def test_no_substituted_label(self):
        hb = self.SubstitutedHolidays()
        hb.substituted_label = "From %s"
        self.assertRaises(ValueError, lambda: hb._populate(1991))
