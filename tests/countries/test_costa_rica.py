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

from holidays.countries.costa_rica import CostaRica, CR, CRI
from tests.common import TestCase


class TestCostaRica(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CostaRica)

    def test_country_aliases(self):
        self.assertCountryAliases(CostaRica, CR, CRI)

    def test_new_year_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1980, 2041))

    def test_easter(self):
        self.assertHoliday(
            # Maundy Thursday
            "2016-03-24",
            "2017-04-13",
            "2018-03-29",
            "2019-04-18",
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            # Good Friday
            "2016-03-25",
            "2017-04-14",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )

    def test_juan_santamaria_day(self):
        years_with_obs = {2006, 2007, 2008, 2023, 2024}
        years = set(range(1980, 2041)).difference(years_with_obs)
        self.assertHoliday(f"{year}-04-11" for year in years)

        dt = (
            "2006-04-17",
            "2007-04-16",
            "2008-04-14",
            "2023-04-10",
            "2024-04-15",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNonObservedHoliday(
            f"{year}-04-11" for year in years_with_obs
        )

    def test_labor_day(self):
        years_with_obs = {2021}
        years = set(range(1980, 2041)).difference(years_with_obs)
        self.assertHoliday(f"{year}-05-01" for year in years)

        dt = "2021-05-03"
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNonObservedHoliday("2021-05-01")

    def test_annexation(self):
        years_with_obs = {2006, 2007, 2008, 2020, 2021, 2023, 2024}
        years = set(range(1980, 2041)).difference(years_with_obs)
        self.assertHoliday(f"{year}-07-25" for year in years)

        dt = (
            "2006-07-31",
            "2007-07-30",
            "2008-07-28",
            "2020-07-27",
            "2021-07-26",
            "2023-07-24",
            "2024-07-29",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNonObservedHoliday(
            f"{year}-07-25" for year in years_with_obs
        )

    def test_feast_our_lady_of_angels(self):
        self.assertHoliday(f"{year}-08-02" for year in range(1980, 2041))

    def test_mothers_day(self):
        years_with_obs = {2006, 2007, 2020, 2023, 2024}
        years = set(range(1980, 2041)).difference(years_with_obs)
        self.assertHoliday(f"{year}-08-15" for year in years)

        dt = (
            "2006-08-21",
            "2007-08-20",
            "2020-08-17",
            "2023-08-14",
            "2024-08-19",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNonObservedHoliday(
            f"{year}-08-15" for year in years_with_obs
        )

    def test_black_person_day(self):
        self.assertHoliday(f"{year}-08-31" for year in range(2024, 2041))
        self.assertNoHoliday("2021-08-31")
        self.assertNoHolidayName(
            "Día de la Persona Negra y la Cultura Afrocostarricense",
            CostaRica(years=2021),
        )

        dt = (
            "2022-09-04",
            "2023-09-03",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNonObservedHoliday("2022-08-31", "2023-08-31")

    def test_independence_day(self):
        years_with_obs = {2020, 2021, 2022, 2024}
        years = set(range(1980, 2041)).difference(years_with_obs)
        self.assertHoliday(f"{year}-09-15" for year in years)

        dt = (
            "2020-09-14",
            "2021-09-13",
            "2022-09-19",
            "2024-09-16",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNonObservedHoliday(
            f"{year}-09-15" for year in years_with_obs
        )

    def test_cultures_day(self):
        self.assertHoliday(
            "2008-10-12",
            "2009-10-12",
            "2013-10-12",
            "2014-10-12",
            "2015-10-12",
            "2019-10-12",
        )
        self.assertNoHoliday("2020-10-12")
        self.assertNoHolidayName(
            "Día de las Culturas",
            CostaRica(years=2020),
        )

        dt = (
            "2010-10-18",
            "2011-10-17",
            "2012-10-15",
            "2016-10-17",
            "2017-10-16",
            "2018-10-15",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNonObservedHoliday(
            "2010-10-12",
            "2011-10-12",
            "2012-10-12",
            "2016-10-12",
            "2017-10-12",
            "2018-10-12",
        )

    def test_army_abolition_day(self):
        self.assertHoliday(f"{year}-12-01" for year in range(2023, 2041))
        self.assertNoHoliday("2019-12-31")
        self.assertNoHolidayName(
            "Día de la Abolición del Ejército",
            CostaRica(years=2019),
        )

        dt = (
            "2020-11-30",
            "2021-11-29",
            "2022-12-05",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNonObservedHoliday("2020-12-01", "2021-12-01", "2022-12-01")

    def test_christmas_day(self):
        self.assertHoliday(f"{year}-12-25" for year in range(1980, 2041))

    def test_2022(self):
        self.assertHolidayDates(
            CostaRica(years=2022),
            "2022-01-01",
            "2022-04-11",
            "2022-04-14",
            "2022-04-15",
            "2022-05-01",
            "2022-07-25",
            "2022-08-02",
            "2022-08-15",
            "2022-09-04",
            "2022-09-19",
            "2022-12-05",
            "2022-12-25",
        )

        self.assertNonObservedHolidayDates(
            CostaRica(observed=False, years=2022),
            "2022-01-01",
            "2022-04-11",
            "2022-04-14",
            "2022-04-15",
            "2022-05-01",
            "2022-07-25",
            "2022-08-02",
            "2022-08-15",
            "2022-08-31",
            "2022-09-15",
            "2022-12-01",
            "2022-12-25",
        )

    def test_2023(self):
        self.assertHolidayDates(
            CostaRica(years=2023),
            "2023-01-01",
            "2023-04-06",
            "2023-04-07",
            "2023-04-10",
            "2023-05-01",
            "2023-07-24",
            "2023-08-02",
            "2023-08-14",
            "2023-09-03",
            "2023-09-15",
            "2023-12-01",
            "2023-12-25",
        )

        self.assertNonObservedHolidayDates(
            CostaRica(observed=False, years=2023),
            "2023-01-01",
            "2023-04-06",
            "2023-04-07",
            "2023-04-11",
            "2023-05-01",
            "2023-07-25",
            "2023-08-02",
            "2023-08-15",
            "2023-08-31",
            "2023-09-15",
            "2023-12-01",
            "2023-12-25",
        )

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                cr = CostaRica(language=language)
                self.assertEqual(cr["2022-01-01"], "Año Nuevo")
                self.assertEqual(cr["2022-12-25"], "Navidad")

        run_tests((CostaRica.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((CostaRica.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        cr = CostaRica(language=en_us)
        self.assertEqual(cr["2022-01-01"], "New Year's Day")
        self.assertEqual(cr["2022-12-25"], "Christmas Day")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            cr = CostaRica(language=language)
            self.assertEqual(cr["2022-01-01"], "New Year's Day")
            self.assertEqual(cr["2022-12-25"], "Christmas Day")

    def test_l10n_uk(self):
        uk = "uk"

        cr = CostaRica(language=uk)
        self.assertEqual(cr["2022-01-01"], "Новий рік")
        self.assertEqual(cr["2022-12-25"], "Різдво Христове")

        self.set_language(uk)
        for language in (None, uk, "invalid"):
            cr = CostaRica(language=language)
            self.assertEqual(cr["2022-01-01"], "Новий рік")
            self.assertEqual(cr["2022-12-25"], "Різдво Христове")
