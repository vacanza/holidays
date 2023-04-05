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

from holidays.countries.romania import Romania, RO, ROU
from tests.common import TestCase


class TestRomania(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Romania)

    def test_country_aliases(self):
        self.assertCountryAliases(Romania, RO, ROU)

    def test_from_2024(self):
        self.assertHoliday("2024-01-06", "2024-01-07")
        self.assertNoHoliday("2023-01-06", "2023-01-07")
        self.assertNoHolidayName("Bobotează", Romania(years=2023))
        self.assertNoHolidayName("Sfântul Ion", Romania(years=2023))

    def test_unification_day(self):
        self.assertHoliday("2016-01-24")
        self.assertNoHoliday("2015-01-24")
        self.assertNoHolidayName(
            "Ziua Unirii Principatelor Române", Romania(years=2015)
        )

    def test_easter(self):
        self.assertHoliday(
            "2017-04-16",
            "2017-04-17",
            "2018-04-06",
            "2018-04-08",
            "2018-04-09",
        )
        self.assertNoHoliday("2016-04-29", "2017-04-14")

    def test_childrens_day(self):
        self.assertHoliday("2017-06-01")
        self.assertNoHoliday("2016-06-01")
        self.assertNoHolidayName("Ziua Copilului", Romania(years=2016))

    def test_assumption_day(self):
        self.assertHoliday("2009-08-15")
        self.assertNoHoliday("2008-08-15")
        self.assertNoHolidayName(
            "Adormirea Maicii Domnului", Romania(years=2008)
        )

    def test_saint_andrews_day(self):
        self.assertHoliday("2012-11-30")
        self.assertNoHoliday("2011-11-30")
        self.assertNoHolidayName(
            "Sfantul Apostol Andrei cel Intai chemat", Romania(years=2011)
        )

    def test_2020(self):
        # https://publicholidays.ro/2020-dates/
        self.assertHolidayDates(
            Romania(years=2020),
            "2020-01-01",
            "2020-01-02",
            "2020-01-24",
            "2020-04-17",
            "2020-04-19",
            "2020-04-20",
            "2020-05-01",
            "2020-06-01",
            "2020-06-07",
            "2020-06-08",
            "2020-08-15",
            "2020-11-30",
            "2020-12-01",
            "2020-12-25",
            "2020-12-26",
        )

    def test_2022(self):
        # https://publicholidays.ro/2022-dates/
        self.assertHolidayDates(
            Romania(years=2022),
            "2022-01-01",
            "2022-01-02",
            "2022-01-24",
            "2022-04-22",
            "2022-04-24",
            "2022-04-25",
            "2022-05-01",
            "2022-06-01",
            "2022-06-12",
            "2022-06-13",
            "2022-08-15",
            "2022-11-30",
            "2022-12-01",
            "2022-12-25",
            "2022-12-26",
        )

    def test_2023(self):
        # https://publicholidays.ro/2023-dates/
        self.assertHolidayDates(
            Romania(years=2023),
            "2023-01-01",
            "2023-01-02",
            "2023-01-24",
            "2023-04-14",
            "2023-04-16",
            "2023-04-17",
            "2023-05-01",
            "2023-06-01",
            "2023-06-04",
            "2023-06-05",
            "2023-08-15",
            "2023-11-30",
            "2023-12-01",
            "2023-12-25",
            "2023-12-26",
        )

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                ro = Romania(language=language)
                self.assertEqual(ro["2022-01-01"], "Anul Nou")
                self.assertEqual(ro["2022-12-25"], "Crăciunul")

        run_tests((Romania.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Romania.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        ro = Romania(language=en_us)
        self.assertEqual(ro["2022-01-01"], "New Year's Day")
        self.assertEqual(ro["2022-12-25"], "Christmas Day")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            ro = Romania(language=language)
            self.assertEqual(ro["2022-01-01"], "New Year's Day")
            self.assertEqual(ro["2022-12-25"], "Christmas Day")

    def test_l10n_uk(self):
        uk = "uk"

        ro = Romania(language=uk)
        self.assertEqual(ro["2022-01-01"], "Новий рік")
        self.assertEqual(ro["2022-12-25"], "Різдво Христове")

        self.set_language(uk)
        for language in (None, uk, "invalid"):
            ro = Romania(language=language)
            self.assertEqual(ro["2022-01-01"], "Новий рік")
            self.assertEqual(ro["2022-12-25"], "Різдво Христове")
