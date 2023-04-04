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
#  Copyright: Kateryna Golovanova <kate@kgthreads.com>, 2022

from holidays.countries.liechtenstein import Liechtenstein, LI, LIE
from tests.common import TestCase


class TestLI(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Liechtenstein, years=range(1900, 2100))

    def test_country_aliases(self):
        self.assertCountryAliases(Liechtenstein, LI, LIE)

    def test_new_years(self):
        self.assertHolidaysName(
            "Neujahr", (f"{year}-01-01" for year in range(1900, 2100))
        )

    def test_saint_berchtolds_day(self):
        self.assertHolidaysName(
            "Berchtoldstag", (f"{year}-01-02" for year in range(1900, 2100))
        )

    def test_epiphany(self):
        self.assertHolidaysName(
            "Heilige Drei Könige",
            (f"{year}-01-06" for year in range(1900, 2100)),
        )

    def test_candlemas(self):
        self.assertHolidaysName(
            "Mariä Lichtmess", (f"{year}-02-02" for year in range(1900, 2100))
        )

    def test_shrove_tuesday(self):
        self.assertHolidaysName(
            "Fasnachtsdienstag",
            "1900-02-27",
            "1901-02-19",
            "1902-02-11",
            "1999-02-16",
            "2000-03-07",
            "2018-02-13",
            "2019-03-05",
            "2020-02-25",
            "2021-02-16",
            "2022-03-01",
        )

    def test_saint_josephs_day(self):
        self.assertHolidaysName(
            "Josefstag", (f"{year}-03-19" for year in range(1900, 2100))
        )

    def test_good_friday(self):
        self.assertHolidaysName(
            "Karfreitag",
            "1900-04-13",
            "1901-04-05",
            "1902-03-28",
            "1999-04-02",
            "2000-04-21",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
        )

    def test_easter(self):
        self.assertHolidaysName(
            "Ostersonntag",
            "1900-04-15",
            "1901-04-07",
            "1902-03-30",
            "1999-04-04",
            "2000-04-23",
            "2018-04-01",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
        )

    def test_easter_monday(self):
        self.assertHolidaysName(
            "Ostermontag",
            "1900-04-16",
            "1901-04-08",
            "1902-03-31",
            "1999-04-05",
            "2000-04-24",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
        )

    def test_labor_day(self):
        self.assertHolidaysName(
            "Tag der Arbeit", (f"{year}-05-01" for year in range(1900, 2100))
        )

    def test_ascension_day(self):
        self.assertHolidaysName(
            "Auffahrt",
            "1900-05-24",
            "1901-05-16",
            "1902-05-08",
            "1999-05-13",
            "2000-06-01",
            "2018-05-10",
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
        )

    def test_whit_sunday(self):
        self.assertHolidaysName(
            "Pfingstsonntag",
            "1900-06-03",
            "1901-05-26",
            "1902-05-18",
            "1999-05-23",
            "2000-06-11",
            "2018-05-20",
            "2019-06-09",
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
        )

    def test_whit_monday(self):
        self.assertHolidaysName(
            "Pfingstmontag",
            "1900-06-04",
            "1901-05-27",
            "1902-05-19",
            "1999-05-24",
            "2000-06-12",
            "2018-05-21",
            "2019-06-10",
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
        )

    def test_corpus_christi(self):
        self.assertHolidaysName(
            "Fronleichnam",
            "1900-06-14",
            "1901-06-06",
            "1902-05-29",
            "1999-06-03",
            "2000-06-22",
            "2018-05-31",
            "2019-06-20",
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
        )

    def test_national_day(self):
        self.assertHolidaysName(
            "Staatsfeiertag",
            (f"{year}-08-15" for year in range(1900, 2100)),
        )

    def test_nativity_of_mary(self):
        self.assertHolidaysName(
            "Mariä Geburt",
            (f"{year}-09-08" for year in range(1900, 2100)),
        )

    def test_all_saints_day(self):
        self.assertHolidaysName(
            "Allerheiligen",
            (f"{year}-11-01" for year in range(1900, 2100)),
        )

    def test_immaculate_conception(self):
        self.assertHolidaysName(
            "Mariä Empfängnis",
            (f"{year}-12-08" for year in range(1900, 2100)),
        )

    def test_christmas_eve(self):
        self.assertHolidaysName(
            "Heiligabend",
            (f"{year}-12-24" for year in range(1900, 2100)),
        )

    def test_christmas_day(self):
        self.assertHolidaysName(
            "Weihnachten",
            (f"{year}-12-25" for year in range(1900, 2100)),
        )

    def test_st_stephens_day(self):
        self.assertHolidaysName(
            "Stefanstag",
            (f"{year}-12-26" for year in range(1900, 2100)),
        )

    def test_new_years_eve(self):
        self.assertHolidaysName(
            "Silvester",
            (f"{year}-12-31" for year in range(1900, 2100)),
        )

    def test_2022(self):
        self.assertHolidays(
            Liechtenstein(years=2022),
            ("2022-01-01", "Neujahr"),
            ("2022-01-02", "Berchtoldstag"),
            ("2022-01-06", "Heilige Drei Könige"),
            ("2022-02-02", "Mariä Lichtmess"),
            ("2022-03-01", "Fasnachtsdienstag"),
            ("2022-03-19", "Josefstag"),
            ("2022-04-15", "Karfreitag"),
            ("2022-04-17", "Ostersonntag"),
            ("2022-04-18", "Ostermontag"),
            ("2022-05-01", "Tag der Arbeit"),
            ("2022-05-26", "Auffahrt"),
            ("2022-06-05", "Pfingstsonntag"),
            ("2022-06-06", "Pfingstmontag"),
            ("2022-06-16", "Fronleichnam"),
            ("2022-08-15", "Staatsfeiertag"),
            ("2022-09-08", "Mariä Geburt"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-12-08", "Mariä Empfängnis"),
            ("2022-12-24", "Heiligabend"),
            ("2022-12-25", "Weihnachten"),
            ("2022-12-26", "Stefanstag"),
            ("2022-12-31", "Silvester"),
        )

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                cnt = LI(language=language)
                self.assertEqual(cnt["2022-01-01"], "Neujahr")
                self.assertEqual(cnt["2022-12-25"], "Weihnachten")

        run_tests((LI.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((LI.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        cnt = LI(language=en_us)
        self.assertEqual(cnt["2022-01-01"], "New Year's Day")
        self.assertEqual(cnt["2022-12-25"], "Christmas Day")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            cnt = LI(language=language)
            self.assertEqual(cnt["2022-01-01"], "New Year's Day")
            self.assertEqual(cnt["2022-12-25"], "Christmas Day")

    def test_l10n_uk(self):
        uk = "uk"

        cnt = LI(language=uk)
        self.assertEqual(cnt["2022-01-01"], "Новий рік")
        self.assertEqual(cnt["2022-12-25"], "Різдво Христове")

        self.set_language(uk)
        for language in (None, uk, "invalid"):
            cnt = LI(language=language)
            self.assertEqual(cnt["2022-01-01"], "Новий рік")
            self.assertEqual(cnt["2022-12-25"], "Різдво Христове")
