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

from holidays.countries.nicaragua import Nicaragua, NI, NIC
from tests.common import TestCase


class TestNicaragua(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Nicaragua)

    def setUp(self):
        super().setUp()
        self.holidays_an = Nicaragua(subdiv="AN")

    def test_country_aliases(self):
        self.assertCountryAliases(Nicaragua, NI, NIC)

    def test_2020(self):
        self.assertHoliday(
            "2020-01-01",
            "2020-04-09",
            "2020-04-10",
            "2020-05-01",
            "2020-07-19",
            "2020-08-01",
            "2020-08-10",
            "2020-09-14",
            "2020-09-15",
            "2020-12-08",
            "2020-12-25",
        )
        self.assertNoHoliday(self.holidays_an, "2020-08-01", "2020-08-10")

    def test_ni_holidays_1979(self):
        self.assertHoliday(
            "1979-01-01",
            "1979-04-12",
            "1979-04-13",
            "1979-05-01",
            "1979-07-19",
            "1979-09-14",
            "1979-09-15",
            "1979-12-08",
            "1979-12-25",
        )

    def test_pre_1979(self):
        self.assertNoHoliday("1978-07-19")

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                ni = Nicaragua(language=language)
                self.assertEqual(ni["2022-01-01"], "Año Nuevo")
                self.assertEqual(ni["2022-12-25"], "Navidad")

        run_tests((Nicaragua.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Nicaragua.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        ni = Nicaragua(language=en_us)
        self.assertEqual(ni["2022-01-01"], "New Year's Day")
        self.assertEqual(ni["2022-12-25"], "Christmas")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            ni = Nicaragua(language=language)
            self.assertEqual(ni["2022-01-01"], "New Year's Day")
            self.assertEqual(ni["2022-12-25"], "Christmas")

    def test_l10n_uk(self):
        uk = "uk"

        ni = Nicaragua(language=uk)
        self.assertEqual(ni["2022-01-01"], "Новий рік")
        self.assertEqual(ni["2022-12-25"], "Різдво Христове")

        self.set_language(uk)
        for language in (None, uk, "invalid"):
            ni = Nicaragua(language=language)
            self.assertEqual(ni["2022-01-01"], "Новий рік")
            self.assertEqual(ni["2022-12-25"], "Різдво Христове")
