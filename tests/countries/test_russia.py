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

from holidays.countries.russia import Russia, RU, RUS
from tests.common import TestCase


class TestRussia(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Russia)

    def test_country_aliases(self):
        self.assertCountryAliases(Russia, RU, RUS)

    def test_pre_2005(self):
        self.assertHoliday("2004-11-07")
        self.assertNoHoliday("2004-11-04")

    def test_2018(self):
        self.assertHoliday(
            "2018-01-01",
            "2018-01-02",
            "2018-01-03",
            "2018-01-04",
            "2018-01-05",
            "2018-01-06",
            "2018-01-07",
            "2018-01-08",
            "2018-02-23",
            "2018-03-08",
            "2018-05-01",
            "2018-05-09",
            "2018-06-12",
            "2018-11-04",
        )

        self.assertNoHoliday(
            "2018-11-07",
            "2018-12-31",
        )

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                ru = Russia(language=language)
                self.assertEqual(ru["2022-01-01"], "Новогодние каникулы")
                self.assertEqual(ru["2022-01-07"], "Рождество Христово")

        run_tests((Russia.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Russia.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        ru = Russia(language=en_us)
        self.assertEqual(ru["2022-01-01"], "New Year Holidays")
        self.assertEqual(ru["2022-01-07"], "Orthodox Christmas Day")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            ru = Russia(language=language)
            self.assertEqual(ru["2022-01-01"], "New Year Holidays")
            self.assertEqual(ru["2022-01-07"], "Orthodox Christmas Day")
