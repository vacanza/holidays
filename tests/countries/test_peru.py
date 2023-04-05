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

from holidays.countries.peru import Peru, PE, PER
from tests.common import TestCase


class TestPeru(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Peru)

    def test_country_aliases(self):
        self.assertCountryAliases(Peru, PE, PER)

    def test_2019(self):
        self.assertHolidayDates(
            "2019-01-01",
            "2019-04-18",
            "2019-04-19",
            "2019-04-21",
            "2019-05-01",
            "2019-06-29",
            "2019-07-28",
            "2019-07-29",
            "2019-08-30",
            "2019-10-08",
            "2019-11-01",
            "2019-12-08",
            "2019-12-25",
        )

    def test_2022(self):
        self.assertHolidayDates(
            "2022-01-01",
            "2022-04-14",
            "2022-04-15",
            "2022-04-17",
            "2022-05-01",
            "2022-06-29",
            "2022-07-28",
            "2022-07-29",
            "2022-08-06",
            "2022-08-30",
            "2022-10-08",
            "2022-11-01",
            "2022-12-08",
            "2022-12-09",
            "2022-12-25",
        )

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                pe = Peru(language=language)
                self.assertEqual(pe["2022-01-01"], "Año Nuevo")
                self.assertEqual(pe["2022-12-25"], "Navidad del Señor")

        run_tests((Peru.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Peru.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        pe = Peru(language=en_us)
        self.assertEqual(pe["2018-01-01"], "New Year's Day")
        self.assertEqual(pe["2022-12-25"], "Christmas Day")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            pe = Peru(language=language)
            self.assertEqual(pe["2018-01-01"], "New Year's Day")
            self.assertEqual(pe["2022-12-25"], "Christmas Day")

    def test_l10n_uk(self):
        uk = "uk"

        pe = Peru(language=uk)
        self.assertEqual(pe["2022-01-01"], "Новий рік")
        self.assertEqual(pe["2022-12-25"], "Різдво Христове")

        self.set_language(uk)
        for language in (None, uk, "invalid"):
            pe = Peru(language=language)
            self.assertEqual(pe["2022-01-01"], "Новий рік")
            self.assertEqual(pe["2022-12-25"], "Різдво Христове")
