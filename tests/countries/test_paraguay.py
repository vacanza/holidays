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

from datetime import date
from datetime import timedelta as td

from holidays.countries.paraguay import Paraguay, PY, PRY
from tests.common import TestCase


class TestParaguay(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Paraguay)

    def test_country_aliases(self):
        self.assertCountryAliases(Paraguay, PY, PRY)

    def test_fixed_holidays(self):
        for year, month, day in (
            (2016, 1, 1),
            (2020, 1, 1),
            (2020, 3, 1),
            (2020, 4, 8),
            (2020, 4, 9),
            (2020, 4, 10),
            (2020, 4, 12),
            (2020, 5, 1),
            (2020, 5, 14),
            (2020, 5, 15),
            (2020, 6, 12),
            (2020, 8, 15),
            (2020, 9, 29),
            (2020, 12, 8),
            (2020, 12, 25),
        ):
            self.assertIn(date(year, month, day), self.holidays)

    def test_non_observed(self):
        # no observed dates
        for year, month, day in (
            (2017, 1, 1),
            (2014, 3, 2),
            (2020, 4, 12),
            (2016, 5, 1),
            (2016, 5, 15),
            (2016, 6, 12),
            (2015, 8, 15),
            (2018, 9, 29),
            (2018, 12, 8),
        ):
            self.assertNoNonObservedHoliday(date(year, month, day))

    def test_moveable(self):
        for year, month, day in (
            # Patriots day
            (2013, 3, 4),
            (2016, 2, 29),
            (2018, 2, 26),
            (2022, 2, 28),
            (2014, 3, 1),
            (2015, 3, 1),
            (2017, 3, 1),
            (2019, 3, 1),
            (2020, 3, 1),
            (2021, 3, 1),
            # Peace in Chaco Day
            (2014, 6, 16),
            (2018, 6, 11),
            (2013, 6, 12),
            (2015, 6, 12),
            (2016, 6, 12),
            (2017, 6, 12),
            (2019, 6, 12),
            (2020, 6, 12),
            (2021, 6, 12),
            (2022, 6, 12),
            # Boqueron's Battle
            (2015, 9, 28),
            (2016, 10, 3),
            (2017, 10, 2),
            (2021, 9, 27),
            (2022, 10, 3),
            (2013, 9, 29),
            (2014, 9, 29),
            (2018, 9, 29),
            (2019, 9, 29),
            (2020, 9, 29),
        ):
            self.assertIn(date(year, month, day), self.holidays)

        for year, month, day in (
            # Patriots day
            (2013, 3, 1),
            (2016, 3, 1),
            (2018, 3, 1),
            (2022, 3, 1),
            # Peace in Chaco Day
            (2014, 6, 12),
            (2018, 6, 12),
            # Boqueron's Battle
            (1999, 9, 29),
            (2015, 9, 29),
            (2016, 9, 29),
            (2017, 9, 29),
            (2021, 9, 29),
            (2022, 9, 29),
        ):
            self.assertNotIn(date(year, month, day), self.holidays)

    def test_independence_day(self):
        for year, month, day in (
            (2010, 5, 15),
            (2011, 5, 15),
            (2012, 5, 14),
            (2012, 5, 15),
            (2013, 5, 14),
            (2013, 5, 15),
            (2018, 5, 14),
            (2018, 5, 15),
            (2021, 5, 14),
            (2021, 5, 15),
        ):
            self.assertIn(date(year, month, day), self.holidays)

    def test_easter(self):
        for year, month, day in [
            (2002, 3, 31),
            (2003, 4, 20),
            (2004, 4, 11),
            (2005, 3, 27),
            (2006, 4, 16),
            (2007, 4, 8),
            (2008, 3, 23),
            (2009, 4, 12),
            (2010, 4, 4),
            (2011, 4, 24),
            (2012, 4, 8),
            (2013, 3, 31),
            (2014, 4, 20),
            (2015, 4, 5),
            (2016, 3, 27),
            (2017, 4, 16),
            (2018, 4, 1),
            (2019, 4, 21),
            (2020, 4, 12),
            (2021, 4, 4),
            (2022, 4, 17),
        ]:
            easter = date(year, month, day)
            easter_thursday = easter + td(days=-3)
            easter_friday = easter + td(days=-2)
            for holiday in [easter_thursday, easter_friday, easter]:
                self.assertIn(holiday, self.holidays)

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                py = Paraguay(language=language)
                self.assertEqual(py["2022-01-01"], "Año Nuevo")
                self.assertEqual(py["2022-12-25"], "Navidad")

        run_tests((Paraguay.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Paraguay.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        py = Paraguay(language=en_us)
        self.assertEqual(py["2022-01-01"], "New Year's Day")
        self.assertEqual(py["2022-12-25"], "Christmas")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            py = Paraguay(language=language)
            self.assertEqual(py["2022-01-01"], "New Year's Day")
            self.assertEqual(py["2022-12-25"], "Christmas")

    def test_l10n_uk(self):
        uk = "uk"

        py = Paraguay(language=uk)
        self.assertEqual(py["2022-01-01"], "Новий рік")
        self.assertEqual(py["2022-12-25"], "Різдво Христове")

        self.set_language(uk)
        for language in (None, uk, "invalid"):
            py = Paraguay(language=language)
            self.assertEqual(py["2022-01-01"], "Новий рік")
            self.assertEqual(py["2022-12-25"], "Різдво Христове")
