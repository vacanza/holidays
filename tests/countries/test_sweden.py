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

from holidays.countries.sweden import Sweden, SE, SWE
from tests.common import SundayHolidays


class TestSweden(SundayHolidays):
    def setUp(self):
        self.holidays = Sweden(include_sundays=False)

    def test_country_aliases(self):
        self.assertCountryAliases(Sweden, SE, SWE)

    def test_new_years(self):
        self.assertHoliday(
            "1900-01-01",
            "2017-01-01",
            "2023-01-01",
        )

    def test_annunciation(self):
        self.assertHoliday(
            "1950-03-25",
            "1951-03-25",
            "1952-03-25",
            "1953-03-25",
        )
        self.assertNoHoliday("1954-03-25")
        self.assertNoHolidayName(
            "Jungfru Marie bebådelsedag", Sweden(years=1954)
        )

    def test_easter(self):
        self.assertHoliday(
            "2000-04-21",
            "2000-04-23",
            "2000-04-24",
            "2010-04-02",
            "2010-04-04",
            "2010-04-05",
            "2021-04-02",
            "2021-04-04",
            "2021-04-05",
            "2024-03-29",
            "2024-03-31",
            "2024-04-01",
        )
        self.assertNoHoliday(
            "2000-04-20",
            "2010-04-01",
            "2021-04-01",
            "2024-03-28",
        )

    def test_may_day(self):
        self.assertHoliday(
            "1939-05-01",
            "2017-05-01",
            "2023-05-01",
        )
        self.assertNoHoliday("1938-05-01")
        self.assertNoHolidayName("Första maj", Sweden(years=1938))

    def test_constitution_day(self):
        self.assertHoliday(
            "2005-06-06",
            "2017-06-06",
            "2999-06-06",
        )
        self.assertNoHoliday("2004-06-06")
        self.assertNoHolidayName("Sveriges nationaldag", Sweden(years=2004))

    def test_pentecost(self):
        self.assertHoliday(
            "2000-06-11",
            "2000-06-12",
            "2010-05-23",
            "2021-05-23",
            "2003-06-09",
            "2024-05-19",
        )
        self.assertNoHoliday(
            "2010-05-24",
            "2021-05-24",
            "2024-05-20",
        )
        self.assertNoHolidayName("Annandag pingst", Sweden(years=2005))

    def test_midsommar(self):
        self.assertHoliday(
            "1950-06-23",
            "1950-06-24",
            "1951-06-23",
            "1951-06-24",
            "1952-06-23",
            "1952-06-24",
            "1953-06-19",
            "1953-06-20",
            "1954-06-25",
            "1954-06-26",
            "2019-06-21",
            "2019-06-22",
            "2020-06-19",
            "2020-06-20",
            "2021-06-25",
            "2021-06-26",
            "2022-06-24",
            "2022-06-25",
        )
        self.assertNoHoliday(
            "1952-06-20",
            "1952-06-21",
            "1953-06-23",
            "1953-06-24",
            "1954-06-23",
            "1954-06-24",
        )

    def test_christmas(self):
        self.assertHoliday(
            "1901-12-25",
            "1901-12-26",
            "2016-12-25",
            "2016-12-26",
        )

    def test_sundays(self):
        self.assertSundays(
            Sweden
        )  # Sundays are considered holidays in Sweden.

    def test_not_holiday(self):
        # Sundays in Sweden are considered holidays,
        # so make sure none of these are actually Sundays.
        self.assertNoHoliday(
            "2017-02-06",
            "2017-02-07",
            "2017-02-08",
            "2017-02-09",
            "2017-02-10",
            "2016-12-27",
            "2016-12-28",
        )

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "Nyårsdagen"),
            ("2022-01-06", "Trettondedag jul"),
            ("2022-04-15", "Långfredagen"),
            ("2022-04-17", "Påskdagen"),
            ("2022-04-18", "Annandag påsk"),
            ("2022-05-01", "Första maj"),
            ("2022-05-26", "Kristi himmelsfärdsdag"),
            ("2022-06-05", "Pingstdagen"),
            ("2022-06-06", "Sveriges nationaldag"),
            ("2022-06-24", "Midsommarafton"),
            ("2022-06-25", "Midsommardagen"),
            ("2022-11-05", "Alla helgons dag"),
            ("2022-12-24", "Julafton"),
            ("2022-12-25", "Juldagen"),
            ("2022-12-26", "Annandag jul"),
            ("2022-12-31", "Nyårsafton"),
        )

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                cnt = SE(language=language)
                self.assertEqual(cnt["2021-01-01"], "Nyårsdagen")
                self.assertEqual(cnt["2021-12-25"], "Juldagen")

        run_tests((SE.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((SE.default_language,))

    def test_l10n_en_us(self):
        lang = "en_US"

        cnt = SE(language=lang)
        self.assertEqual(cnt["2021-01-01"], "New Year's Day")
        self.assertEqual(cnt["2021-12-25"], "Christmas Day")

        self.set_language(lang)
        for language in (None, lang, "invalid"):
            cnt = SE(language=language)
            self.assertEqual(cnt["2021-01-01"], "New Year's Day")
            self.assertEqual(cnt["2021-12-25"], "Christmas Day")

    def test_l10n_uk(self):
        lang = "uk"

        cnt = SE(language=lang)
        self.assertEqual(cnt["2021-01-01"], "Новий рік")
        self.assertEqual(cnt["2021-12-25"], "Різдво Христове")

        self.set_language(lang)
        for language in (None, lang, "invalid"):
            cnt = SE(language=language)
            self.assertEqual(cnt["2021-01-01"], "Новий рік")
            self.assertEqual(cnt["2021-12-25"], "Різдво Христове")
