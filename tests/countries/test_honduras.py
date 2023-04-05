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

from holidays.countries.honduras import Honduras, HN, HND
from tests.common import TestCase


class TestHonduras(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Honduras)

    def test_country_aliases(self):
        self.assertCountryAliases(Honduras, HN, HND)

    def test_2014(self):
        self.assertHolidayDates(
            "2014-01-01",
            "2014-04-14",
            "2014-04-17",
            "2014-04-18",
            "2014-04-19",
            "2014-05-01",
            "2014-09-15",
            "2014-10-03",
            "2014-10-12",
            "2014-10-21",
            "2014-12-25",
        )

    def test_2016(self):
        # https://www.officeholidays.com/countries/honduras/2016
        self.assertHolidayDates(
            "2016-01-01",
            "2016-03-24",
            "2016-03-25",
            "2016-03-26",
            "2016-04-14",
            "2016-05-01",
            "2016-09-15",
            "2016-10-05",
            "2016-10-06",
            "2016-10-07",
            "2016-12-25",
        )

    def test_2021(self):
        # https://www.officeholidays.com/countries/honduras/2021
        self.assertHolidayDates(
            "2021-01-01",
            "2021-04-01",
            "2021-04-02",
            "2021-04-03",
            "2021-04-14",
            "2021-05-01",
            "2021-09-15",
            "2021-10-06",
            "2021-10-07",
            "2021-10-08",
            "2021-12-25",
        )

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-04-14", "Día de las Américas; Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-04-16", "Sábado de Gloria"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-09-15", "Día de la Independencia"),
            ("2022-10-05", "Semana Morazánica"),
            ("2022-10-06", "Semana Morazánica"),
            ("2022-10-07", "Semana Morazánica"),
            ("2022-12-25", "Navidad"),
        )

    def test_2025(self):
        self.assertHolidayDates(
            "2025-01-01",
            "2025-04-14",
            "2025-04-17",
            "2025-04-18",
            "2025-04-19",
            "2025-05-01",
            "2025-09-15",
            "2025-10-01",
            "2025-10-02",
            "2025-10-03",
            "2025-12-25",
        )

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                hn = Honduras(language=language)
                self.assertEqual(hn["2022-01-01"], "Año Nuevo")
                self.assertEqual(hn["2022-12-25"], "Navidad")

        run_tests((Honduras.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Honduras.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        hn = Honduras(language=en_us)
        self.assertEqual(hn["2022-01-01"], "New Year's Day")
        self.assertEqual(hn["2022-12-25"], "Christmas")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            hn = Honduras(language=language)
            self.assertEqual(hn["2022-01-01"], "New Year's Day")
            self.assertEqual(hn["2022-12-25"], "Christmas")

    def test_l10n_uk(self):
        uk = "uk"

        hn = Honduras(language=uk)
        self.assertEqual(hn["2022-01-01"], "Новий рік")
        self.assertEqual(hn["2022-12-25"], "Різдво Христове")

        self.set_language(uk)
        for language in (None, uk, "invalid"):
            hn = Honduras(language=language)
            self.assertEqual(hn["2022-01-01"], "Новий рік")
            self.assertEqual(hn["2022-12-25"], "Різдво Христове")
