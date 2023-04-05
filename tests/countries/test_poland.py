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

from holidays.countries.poland import Poland, PL, POL
from tests.common import TestCase


class TestPoland(TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1925, 2050)
        super().setUpClass(Poland, years=years)

    def test_country_aliases(self):
        self.assertCountryAliases(Poland, PL, POL)

    def test_no_holidays(self):
        self.assertNoHolidays(Poland(years=1924))

    def test_2017(self):
        # http://www.officeholidays.com/countries/poland/2017.php
        self.assertHolidayDates(
            Poland(years=2017),
            "2017-01-01",
            "2017-01-06",
            "2017-04-16",
            "2017-04-17",
            "2017-05-01",
            "2017-05-03",
            "2017-06-04",
            "2017-06-15",
            "2017-08-15",
            "2017-11-01",
            "2017-11-11",
            "2017-12-25",
            "2017-12-26",
        )

    def test_2022(self):
        self.assertHolidayDates(
            Poland(years=2022),
            "2022-01-01",
            "2022-01-06",
            "2022-04-17",
            "2022-04-18",
            "2022-05-01",
            "2022-05-03",
            "2022-06-05",
            "2022-06-16",
            "2022-08-15",
            "2022-11-01",
            "2022-11-11",
            "2022-12-25",
            "2022-12-26",
        )

    def test_special_holidays(self):
        self.assertHoliday("2018-11-12")

    def test_nowy_rok(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1925, 2050))

    def test_swieto_trzech_kroli(self):
        self.assertHoliday(f"{year}-01-06" for year in range(1925, 1960))
        self.assertHoliday(f"{year}-01-06" for year in range(2011, 2050))
        self.assertNoHoliday(f"{year}-01-06" for year in range(1961, 2011))
        self.assertNoHolidayNameInYears(
            "Święto Trzech Króli", range(1961, 2011)
        )

    def test_oczyszczenie_nmp(self):
        self.assertHoliday(f"{year}-02-02" for year in range(1925, 1951))
        self.assertNoHoliday(f"{year}-02-02" for year in range(1951, 2050))
        self.assertNoHolidayNameInYears(
            "Oczyszczenie Najświętszej Marii Panny",
            range(1951, 2050),
        )

    def test_easter_related(self):
        self.assertHoliday(
            # Niedziela Wielkanocna
            "2015-04-05",
            "2016-03-27",
            "2017-04-16",
            "2018-04-01",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            # Poniedziałek Wielkanocny
            "2015-04-06",
            "2016-03-28",
            "2017-04-17",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            # Zielone Świątki
            "2015-05-24",
            "2016-05-15",
            "2017-06-04",
            "2018-05-20",
            "2019-06-09",
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            # Dzień Bożego Ciała
            "2015-06-04",
            "2016-05-26",
            "2017-06-15",
            "2018-05-31",
            "2019-06-20",
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
        )

    def test_swieto_panstwowe(self):
        self.assertHoliday(f"{year}-05-01" for year in range(1950, 2050))
        self.assertNoHoliday(f"{year}-05-01" for year in range(1925, 1950))
        self.assertNoHolidayNameInYears("Święto Państwowe", range(1925, 1950))

    def test_swieto_narodowe_trzeciego_maja(self):
        self.assertHoliday(f"{year}-05-03" for year in range(1925, 1951))
        self.assertHoliday(f"{year}-05-03" for year in range(1990, 2050))
        self.assertNoHoliday(f"{year}-05-03" for year in range(1951, 1990))
        self.assertNoHolidayNameInYears(
            "Święto Narodowe Trzeciego Maja", range(1951, 1990)
        )

    def test_narodowe_swieto_zwyciestwa_i_wolnosci(self):
        self.assertHoliday(f"{year}-05-09" for year in range(1946, 1951))
        self.assertNoHoliday(f"{year}-05-09" for year in range(1925, 1946))
        self.assertNoHoliday(f"{year}-05-09" for year in range(1951, 2050))
        self.assertNoHolidayNameInYears(
            "Narodowe Święto Zwycięstwa i Wolności",
            range(1925, 1946),
        )
        self.assertNoHolidayNameInYears(
            "Narodowe Święto Zwycięstwa i Wolności",
            range(1951, 2050),
        )

    def test_wniebowstapienie_panskie(self):
        self.assertHoliday(
            "1930-05-30",
            "1934-05-11",
            "1939-05-19",
            "1945-05-11",
            "1950-05-19",
        )
        self.assertNoHolidayNameInYears(
            "Wniebowstąpienie Pańskie", range(1951, 2050)
        )

    def test_drugi_dzien_zielonych_swiatek(self):
        self.assertHoliday(
            "1930-06-09",
            "1934-05-21",
            "1939-05-29",
            "1945-05-21",
            "1950-05-29",
        )
        self.assertNoHolidayNameInYears(
            "Drugi dzień Zielonych Świątek", range(1951, 2050)
        )

    def test_swietych_apostolow_piotra_i_pawla(self):
        self.assertHoliday(f"{year}-06-29" for year in range(1925, 1951))
        self.assertNoHoliday(f"{year}-06-29" for year in range(1951, 2050))
        self.assertNoHolidayNameInYears(
            "Uroczystość Świętych Apostołów Piotra i Pawła",
            range(1951, 2050),
        )

    def test_narodowe_swieto_odrodzenia_polski(self):
        self.assertHoliday(f"{year}-07-22" for year in range(1945, 1990))
        self.assertNoHoliday(f"{year}-07-22" for year in range(1925, 1945))
        self.assertNoHoliday(f"{year}-07-22" for year in range(1990, 2050))
        self.assertNoHolidayNameInYears(
            "Narodowe Święto Odrodzenia Polski",
            range(1925, 1945),
        )
        self.assertNoHolidayNameInYears(
            "Narodowe Święto Odrodzenia Polski",
            range(1990, 2050),
        )

    def test_wniebowziecie_nmp(self):
        self.assertHoliday(f"{year}-08-15" for year in range(1925, 1961))
        self.assertHoliday(f"{year}-08-15" for year in range(1989, 2050))
        self.assertNoHoliday(f"{year}-08-15" for year in range(1961, 1989))
        self.assertNoHolidayNameInYears(
            "Wniebowzięcie Najświętszej Marii Panny",
            range(1961, 1989),
        )

    def test_wszystkich_swietych(self):
        self.assertHoliday(f"{year}-11-01" for year in range(1925, 2050))

    def test_narodowe_swieto_niepodleglosci(self):
        self.assertHoliday(f"{year}-11-11" for year in range(1937, 1945))
        self.assertHoliday(f"{year}-11-11" for year in range(1989, 2050))
        self.assertNoHoliday(f"{year}-11-11" for year in range(1925, 1937))
        self.assertNoHoliday(f"{year}-11-11" for year in range(1945, 1989))
        self.assertNoHolidayNameInYears(
            "Narodowe Święto Niepodległości", range(1925, 1937)
        )
        self.assertNoHolidayNameInYears(
            "Narodowe Święto Niepodległości", range(1945, 1989)
        )

    def test_niepokalane_poczecie_nmp(self):
        self.assertHoliday(f"{year}-12-08" for year in range(1925, 1951))
        self.assertNoHoliday(f"{year}-12-08" for year in range(1951, 2050))
        self.assertNoHolidayNameInYears(
            "Niepokalane Poczęcie Najświętszej Marii Panny",
            range(1951, 2050),
        )

    def test_boze_narodzenie(self):
        self.assertHoliday(f"{year}-12-25" for year in range(1925, 2050))
        self.assertHoliday(f"{year}-12-26" for year in range(1925, 2050))

    def test_l10n_default(self):
        def run_tests(languages):
            for language in languages:
                pl = Poland(language=language)
                self.assertEqual(pl["2022-01-01"], "Nowy Rok")
                self.assertEqual(
                    pl["2022-12-25"], "Boże Narodzenie (pierwszy dzień)"
                )

        run_tests((Poland.default_language, None, "invalid"))

        self.set_language("en_US")
        run_tests((Poland.default_language,))

    def test_l10n_en_us(self):
        en_us = "en_US"

        pl = Poland(language=en_us)
        self.assertEqual(
            pl["2018-11-12"],
            "National Independence Day - 100th anniversary",
        )
        self.assertEqual(pl["2022-01-01"], "New Year's Day")
        self.assertEqual(pl["2022-12-25"], "Christmas (Day 1)")

        self.set_language(en_us)
        for language in (None, en_us, "invalid"):
            pl = Poland(language=language)
            self.assertEqual(pl["2022-01-01"], "New Year's Day")
            self.assertEqual(pl["2022-12-25"], "Christmas (Day 1)")

    def test_l10n_uk(self):
        uk = "uk"

        pl = Poland(language=uk)
        self.assertEqual(
            pl["2018-11-12"],
            "100-а річниця Дня Незалежності",
        )
        self.assertEqual(pl["2022-01-01"], "Новий рік")
        self.assertEqual(pl["2022-12-25"], "Перший день Різдва")

        self.set_language(uk)
        for language in (None, uk, "invalid"):
            pl = Poland(language=language)
            self.assertEqual(pl["2022-01-01"], "Новий рік")
            self.assertEqual(pl["2022-12-25"], "Перший день Різдва")
