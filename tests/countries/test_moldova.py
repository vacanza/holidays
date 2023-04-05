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

from holidays.countries.moldova import Moldova, MD, MDA
from tests.common import TestCase


class TestMoldova(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Moldova)

    def test_country_aliases(self):
        self.assertCountryAliases(Moldova, MD, MDA)

    def test_no_holidays(self):
        self.assertNoHolidays(Moldova(years=1990))

    def test_christmas(self):
        name_old1 = "Naşterea lui Iisus Hristos (Crăciunul)"
        name_old2 = "Naşterea lui Iisus Hristos (Crăciunul pe stil vechi)"
        name_new = "Naşterea lui Iisus Hristos (Crăciunul pe stil nou)"
        self.assertHolidaysName(
            name_old1, (f"{year}-01-07" for year in range(1991, 2014))
        )
        self.assertNoHolidayName(name_old1, Moldova(years=2014))
        self.assertHolidaysName(
            name_old2, (f"{year}-01-07" for year in range(2014, 2031))
        )
        self.assertNoHolidayName(name_old2, Moldova(years=2013))

        self.assertHolidaysName(
            name_new, (f"{year}-12-25" for year in range(2013, 2031))
        )
        self.assertNoHolidayName(name_new, Moldova(years=2012))

    def test_europe_day(self):
        name = "Ziua Europei"
        self.assertHolidaysName(
            name, (f"{year}-05-09" for year in range(2017, 2031))
        )
        self.assertNoHolidayName(name, Moldova(years=2016))

    def test_childrens_day(self):
        name = "Ziua Ocrotirii Copilului"
        self.assertHolidaysName(
            name, (f"{year}-06-01" for year in range(2016, 2031))
        )
        self.assertNoHolidayName(name, Moldova(years=2015))

    def test_2022(self):
        self.assertHolidayDates(
            Moldova(years=2022),
            "2022-01-01",
            "2022-01-07",
            "2022-01-08",
            "2022-03-08",
            "2022-04-24",
            "2022-04-25",
            "2022-05-01",
            "2022-05-02",
            "2022-05-09",
            "2022-06-01",
            "2022-08-27",
            "2022-08-31",
            "2022-12-25",
        )

    def test_2023(self):
        self.assertHolidayDates(
            Moldova(years=2023),
            "2023-01-01",
            "2023-01-07",
            "2023-01-08",
            "2023-03-08",
            "2023-04-16",
            "2023-04-17",
            "2023-04-24",
            "2023-05-01",
            "2023-05-09",
            "2023-06-01",
            "2023-08-27",
            "2023-08-31",
            "2023-12-25",
        )

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                md = Moldova(language=language)
                self.assertEqual(md["2022-01-01"], "Anul Nou")
                self.assertEqual(md["2022-08-31"], "Limba noastră")

        run_tests((Moldova.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Moldova.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        md = Moldova(language=en_us)
        self.assertEqual(md["2022-01-01"], "New Year's Day")
        self.assertEqual(md["2022-08-31"], "National Language Day")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            md = Moldova(language=language)
            self.assertEqual(md["2022-01-01"], "New Year's Day")
            self.assertEqual(md["2022-08-31"], "National Language Day")

    def test_l10n_uk(self):
        uk = "uk"

        do = Moldova(language=uk)
        self.assertEqual(do["2022-01-01"], "Новий рік")
        self.assertEqual(do["2022-08-31"], "День рідної мови")

        self.set_language(uk)
        for language in (None, uk, "invalid"):
            do = Moldova(language=language)
            self.assertEqual(do["2022-01-01"], "Новий рік")
            self.assertEqual(do["2022-08-31"], "День рідної мови")
