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

from holidays.countries.denmark import Denmark, DK, DNK
from tests.common import TestCase


class TestDenmark(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Denmark)

    def test_country_aliases(self):
        self.assertCountryAliases(Denmark, DK, DNK)

    def test_2016(self):
        # http://www.officeholidays.com/countries/denmark/2016.php
        self.assertHolidays(
            ("2016-01-01", "Nytårsdag"),
            ("2016-03-24", "Skærtorsdag"),
            ("2016-03-25", "Langfredag"),
            ("2016-03-27", "Påskedag"),
            ("2016-03-28", "Anden påskedag"),
            ("2016-04-22", "Store bededag"),
            ("2016-05-05", "Kristi himmelfartsdag"),
            ("2016-05-15", "Pinsedag"),
            ("2016-05-16", "Anden pinsedag"),
            ("2016-12-25", "Juledag"),
            ("2016-12-26", "Anden juledag"),
        )

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "Nytårsdag"),
            ("2022-04-14", "Skærtorsdag"),
            ("2022-04-15", "Langfredag"),
            ("2022-04-17", "Påskedag"),
            ("2022-04-18", "Anden påskedag"),
            ("2022-05-13", "Store bededag"),
            ("2022-05-26", "Kristi himmelfartsdag"),
            ("2022-06-05", "Pinsedag"),
            ("2022-06-06", "Anden pinsedag"),
            ("2022-12-25", "Juledag"),
            ("2022-12-26", "Anden juledag"),
        )

    def test_2024(self):
        # https://www.officeholidays.com/countries/denmark/2024
        self.assertNoHoliday("2024-04-26")
        self.assertNoHolidayName("Store bededag", Denmark(years=2024))

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                dk = Denmark(language=language)
                self.assertEqual(dk["2022-01-01"], "Nytårsdag")
                self.assertEqual(dk["2022-12-25"], "Juledag")

        run_tests((Denmark.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Denmark.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        dk = Denmark(language=en_us)
        self.assertEqual(dk["2022-01-01"], "New Year's Day")
        self.assertEqual(dk["2022-12-25"], "Christmas Day")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            dk = Denmark(language=language)
            self.assertEqual(dk["2022-01-01"], "New Year's Day")
            self.assertEqual(dk["2022-12-25"], "Christmas Day")

    def test_l10n_uk(self):
        lang = "uk"

        dk = Denmark(language=lang)
        self.assertEqual(dk["2022-01-01"], "Новий рік")
        self.assertEqual(dk["2022-12-25"], "Різдво Христове")

        self.set_language(lang)
        for language in (None, lang, "invalid"):
            dk = Denmark(language=language)
            self.assertEqual(dk["2022-01-01"], "Новий рік")
            self.assertEqual(dk["2022-12-25"], "Різдво Христове")
