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

from holidays.countries.denmark import Denmark
from test.common import TestCase


class TestDK(TestCase):
    def setUp(self):
        super().setUp(Denmark)

    @classmethod
    def setUpClass(cls):
        super().setUpClass(Denmark)

    def test_2016(self):
        # http://www.officeholidays.com/countries/denmark/2016.php
        self.assertIn(date(2016, 1, 1), self.holidays)
        self.assertIn(date(2016, 3, 24), self.holidays)
        self.assertIn(date(2016, 3, 25), self.holidays)
        self.assertIn(date(2016, 3, 28), self.holidays)
        self.assertIn(date(2016, 4, 22), self.holidays)
        self.assertIn(date(2016, 5, 5), self.holidays)
        self.assertIn(date(2016, 5, 16), self.holidays)
        self.assertIn(date(2016, 12, 25), self.holidays)

    def test_i18n_default(self):
        def run_tests(languages):
            for language in languages:
                dk = Denmark(language=language)
                self.assertEqual(dk["2022-01-01"], "Nytårsdag")
                self.assertEqual(dk["2022-12-25"], "Juledag")

        run_tests((Denmark.default_language, None, "invalid"))

        self.set_locale("en")
        run_tests((Denmark.default_language,))

    def test_i18n_en(self):
        language = "en"

        dk_en = Denmark(language=language)
        self.assertEqual(dk_en["2022-01-01"], "New Year's Day")
        self.assertEqual(dk_en["2022-12-25"], "Christmas Day")

        self.set_locale(language)
        for language in (None, language, "invalid"):
            dk_en = Denmark(language=language)
            self.assertEqual(dk_en["2022-01-01"], "New Year's Day")
            self.assertEqual(dk_en["2022-12-25"], "Christmas Day")
