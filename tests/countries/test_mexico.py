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

from holidays.countries.mexico import Mexico, MX, MEX
from tests.common import TestCase


class TestMexico(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Mexico, years=range(1900, 2050))

    def test_country_aliases(self):
        self.assertCountryAliases(Mexico, MX, MEX)

    def test_new_years_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1900, 2050))

    def test_constitution_day(self):
        self.assertHoliday(f"{year}-02-05" for year in range(1917, 2006))
        self.assertNoHoliday(f"{year}-02-05" for year in range(1900, 1917))
        self.assertNoHolidayNameInYears(
            "Día de la Constitución", range(1900, 1917)
        )
        self.assertHoliday(
            "2006-02-06",
            "2007-02-05",
            "2008-02-04",
            "2009-02-02",
            "2010-02-01",
            "2011-02-07",
            "2012-02-06",
            "2013-02-04",
            "2014-02-03",
            "2015-02-02",
            "2016-02-01",
            "2017-02-06",
            "2018-02-05",
            "2019-02-04",
            "2020-02-03",
            "2021-02-01",
            "2022-02-07",
            "2023-02-06",
        )

    def test_benito_juarez(self):
        self.assertHoliday(f"{year}-03-21" for year in range(1917, 2007))
        self.assertNoHoliday(f"{year}-03-21" for year in range(1900, 1917))
        self.assertNoHolidayNameInYears(
            "Natalicio de Benito Juárez", range(1900, 1917)
        )
        self.assertHoliday(
            "2007-03-19",
            "2008-03-17",
            "2009-03-16",
            "2010-03-15",
            "2011-03-21",
            "2012-03-19",
            "2013-03-18",
            "2014-03-17",
            "2015-03-16",
            "2016-03-21",
            "2017-03-20",
            "2018-03-19",
            "2019-03-18",
            "2020-03-16",
            "2021-03-15",
            "2022-03-21",
            "2023-03-20",
        )

    def test_labour_day(self):
        self.assertHoliday(f"{year}-05-01" for year in range(1923, 2050))
        self.assertNoHoliday(f"{year}-05-01" for year in range(1900, 1923))
        self.assertNoHolidayNameInYears("Día del Trabajo", range(1900, 1923))

    def test_independence_day(self):
        self.assertHoliday(f"{year}-09-16" for year in range(1900, 2050))

    def test_revolution_day(self):
        self.assertHoliday(f"{year}-11-20" for year in range(1917, 2006))
        self.assertNoHoliday(f"{year}-11-20" for year in range(1900, 1917))
        self.assertNoHolidayNameInYears(
            "Día de la Revolución", range(1900, 1917)
        )
        self.assertHoliday(
            "2006-11-20",
            "2007-11-19",
            "2008-11-17",
            "2009-11-16",
            "2010-11-15",
            "2011-11-21",
            "2012-11-19",
            "2013-11-18",
            "2014-11-17",
            "2015-11-16",
            "2016-11-21",
            "2017-11-20",
            "2018-11-19",
            "2019-11-18",
            "2020-11-16",
            "2021-11-15",
            "2022-11-21",
            "2023-11-20",
        )

    def test_change_of_government(self):
        self.assertHoliday(
            "1970-12-01",
            "1976-12-01",
            "1982-12-01",
            "1988-12-01",
            "1994-12-01",
            "2000-12-01",
            "2006-12-01",
            "2012-12-01",
            "2018-12-01",
            "2024-12-01",
        )
        self.assertNoHoliday(
            f"{year}-12-01"
            for year in range(1970, 2050)
            if (year - 1970) % 6 > 0
        )
        name = "Transmisión del Poder Ejecutivo Federal"
        self.assertNoHolidayNameInYears(name, range(1900, 1970))
        self.assertNoHolidayNameInYears(
            name, (year for year in range(1970, 2050) if (year - 1970) % 6 > 0)
        )

    def test_christmas_day(self):
        self.assertHoliday(f"{year}-12-25" for year in range(1900, 2050))

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                mx = Mexico(language=language)
                self.assertEqual(mx["2022-01-01"], "Año Nuevo")
                self.assertEqual(mx["2022-12-25"], "Navidad")

        run_tests((Mexico.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Mexico.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        mx = Mexico(language=en_us)
        self.assertEqual(mx["2022-01-01"], "New Year's Day")
        self.assertEqual(mx["2022-12-25"], "Christmas Day")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            mx = Mexico(language=language)
            self.assertEqual(mx["2022-01-01"], "New Year's Day")
            self.assertEqual(mx["2022-12-25"], "Christmas Day")

    def test_l10n_uk(self):
        uk = "uk"

        mx = Mexico(language=uk)
        self.assertEqual(mx["2022-01-01"], "Новий рік")
        self.assertEqual(mx["2022-12-25"], "Різдво Христове")

        self.set_language(uk)
        for language in (None, uk, "invalid"):
            mx = Mexico(language=language)
            self.assertEqual(mx["2022-01-01"], "Новий рік")
            self.assertEqual(mx["2022-12-25"], "Різдво Христове")
