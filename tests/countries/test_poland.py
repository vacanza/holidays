#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.poland import Poland, PL, POL
from tests.common import CommonCountryTests


class TestPoland(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Poland, years=range(1925, 2050))

    def test_country_aliases(self):
        self.assertAliases(Poland, PL, POL)

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
        self.assertNoHolidayName("Święto Trzech Króli", range(1961, 2011))

    def test_oczyszczenie_nmp(self):
        self.assertHoliday(f"{year}-02-02" for year in range(1925, 1951))
        self.assertNoHoliday(f"{year}-02-02" for year in range(1951, 2050))
        self.assertNoHolidayName("Oczyszczenie Najświętszej Marii Panny", range(1951, 2050))

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
        self.assertNoHolidayName("Święto Państwowe", range(1925, 1950))

    def test_swieto_narodowe_trzeciego_maja(self):
        self.assertHoliday(f"{year}-05-03" for year in range(1925, 1951))
        self.assertHoliday(f"{year}-05-03" for year in range(1990, 2050))
        self.assertNoHoliday(f"{year}-05-03" for year in range(1951, 1990))
        self.assertNoHolidayName("Święto Narodowe Trzeciego Maja", range(1951, 1990))

    def test_narodowe_swieto_zwyciestwa_i_wolnosci(self):
        self.assertHoliday(f"{year}-05-09" for year in range(1946, 1951))
        self.assertNoHoliday(
            f"{year}-05-09" for year in set(range(1925, 1946)).difference({1929})
        )  # Exclude Ascension day on 09/05/1929
        self.assertNoHoliday(f"{year}-05-09" for year in range(1951, 2050))
        self.assertNoHolidayName(
            "Narodowe Święto Zwycięstwa i Wolności", range(1925, 1946), range(1951, 2050)
        )

    def test_wniebowstapienie_panskie(self):
        self.assertHoliday(
            "1930-05-29",
            "1934-05-10",
            "1939-05-18",
            "1945-05-10",
            "1950-05-18",
        )
        self.assertNoHolidayName("Wniebowstąpienie Pańskie", range(1951, 2050))

    def test_drugi_dzien_zielonych_swiatek(self):
        self.assertHoliday(
            "1930-06-09",
            "1934-05-21",
            "1939-05-29",
            "1945-05-21",
            "1950-05-29",
        )
        self.assertNoHolidayName("Drugi dzień Zielonych Świątek", range(1951, 2050))

    def test_swietych_apostolow_piotra_i_pawla(self):
        self.assertHoliday(f"{year}-06-29" for year in range(1925, 1951))
        self.assertNoHoliday(f"{year}-06-29" for year in range(1951, 2050))
        self.assertNoHolidayName(
            "Uroczystość Świętych Apostołów Piotra i Pawła", range(1951, 2050)
        )

    def test_narodowe_swieto_odrodzenia_polski(self):
        self.assertHoliday(f"{year}-07-22" for year in range(1945, 1990))
        self.assertNoHoliday(f"{year}-07-22" for year in range(1925, 1945))
        self.assertNoHoliday(f"{year}-07-22" for year in range(1990, 2050))
        self.assertNoHolidayName(
            "Narodowe Święto Odrodzenia Polski", range(1925, 1945), range(1990, 2050)
        )

    def test_wniebowziecie_nmp(self):
        self.assertHoliday(f"{year}-08-15" for year in range(1925, 1961))
        self.assertHoliday(f"{year}-08-15" for year in range(1989, 2050))
        self.assertNoHoliday(f"{year}-08-15" for year in range(1961, 1989))
        self.assertNoHolidayName("Wniebowzięcie Najświętszej Marii Panny", range(1961, 1989))

    def test_wszystkich_swietych(self):
        self.assertHoliday(f"{year}-11-01" for year in range(1925, 2050))

    def test_narodowe_swieto_niepodleglosci(self):
        self.assertHoliday(f"{year}-11-11" for year in range(1937, 1945))
        self.assertHoliday(f"{year}-11-11" for year in range(1989, 2050))
        self.assertNoHoliday(f"{year}-11-11" for year in range(1925, 1937))
        self.assertNoHoliday(f"{year}-11-11" for year in range(1945, 1989))
        self.assertNoHolidayName(
            "Narodowe Święto Niepodległości", range(1925, 1937), range(1945, 1989)
        )

    def test_niepokalane_poczecie_nmp(self):
        self.assertHoliday(f"{year}-12-08" for year in range(1925, 1951))
        self.assertNoHoliday(f"{year}-12-08" for year in range(1951, 2050))
        self.assertNoHolidayName(
            "Niepokalane Poczęcie Najświętszej Marii Panny", range(1951, 2050)
        )

    def test_boze_narodzenie(self):
        self.assertHoliday(f"{year}-12-25" for year in range(1925, 2050))
        self.assertHoliday(f"{year}-12-26" for year in range(1925, 2050))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "Nowy Rok"),
            ("2018-01-06", "Święto Trzech Króli"),
            ("2018-04-01", "Niedziela Wielkanocna"),
            ("2018-04-02", "Poniedziałek Wielkanocny"),
            ("2018-05-01", "Święto Państwowe"),
            ("2018-05-03", "Święto Narodowe Trzeciego Maja"),
            ("2018-05-20", "Zielone Świątki"),
            ("2018-05-31", "Dzień Bożego Ciała"),
            ("2018-08-15", "Wniebowzięcie Najświętszej Marii Panny"),
            ("2018-11-01", "Uroczystość Wszystkich Świętych"),
            ("2018-11-11", "Narodowe Święto Niepodległości"),
            ("2018-11-12", "Narodowe Święto Niepodległości - 100-lecie"),
            ("2018-12-25", "Boże Narodzenie (pierwszy dzień)"),
            ("2018-12-26", "Boże Narodzenie (drugi dzień)"),
        )

        self.assertLocalizedHolidays(
            ("2022-01-01", "Nowy Rok"),
            ("2022-01-06", "Święto Trzech Króli"),
            ("2022-04-17", "Niedziela Wielkanocna"),
            ("2022-04-18", "Poniedziałek Wielkanocny"),
            ("2022-05-01", "Święto Państwowe"),
            ("2022-05-03", "Święto Narodowe Trzeciego Maja"),
            ("2022-06-05", "Zielone Świątki"),
            ("2022-06-16", "Dzień Bożego Ciała"),
            ("2022-08-15", "Wniebowzięcie Najświętszej Marii Panny"),
            ("2022-11-01", "Uroczystość Wszystkich Świętych"),
            ("2022-11-11", "Narodowe Święto Niepodległości"),
            ("2022-12-25", "Boże Narodzenie (pierwszy dzień)"),
            ("2022-12-26", "Boże Narodzenie (drugi dzień)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2018-01-01", "New Year's Day"),
            ("2018-01-06", "Epiphany"),
            ("2018-04-01", "Easter Sunday"),
            ("2018-04-02", "Easter Monday"),
            ("2018-05-01", "National Day"),
            ("2018-05-03", "National Day of the Third of May"),
            ("2018-05-20", "Pentecost"),
            ("2018-05-31", "Corpus Christi"),
            ("2018-08-15", "Assumption Day"),
            ("2018-11-01", "All Saints' Day"),
            ("2018-11-11", "National Independence Day"),
            ("2018-11-12", "National Independence Day - 100th anniversary"),
            ("2018-12-25", "Christmas Day"),
            ("2018-12-26", "Second Day of Christmas"),
        )
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "National Day"),
            ("2022-05-03", "National Day of the Third of May"),
            ("2022-06-05", "Pentecost"),
            ("2022-06-16", "Corpus Christi"),
            ("2022-08-15", "Assumption Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-11", "National Independence Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2018-01-01", "Новий рік"),
            ("2018-01-06", "Богоявлення"),
            ("2018-04-01", "Великдень"),
            ("2018-04-02", "Великодній понеділок"),
            ("2018-05-01", "Національне свято"),
            ("2018-05-03", "Національне свято Третього Травня"),
            ("2018-05-20", "День Святої Трійці"),
            ("2018-05-31", "Свято Тіла і Крові Христових"),
            ("2018-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2018-11-01", "День усіх святих"),
            ("2018-11-11", "День Незалежності"),
            ("2018-11-12", "100-а річниця Дня Незалежності"),
            ("2018-12-25", "Різдво Христове"),
            ("2018-12-26", "Другий день Різдва"),
        )
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-06", "Богоявлення"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "Національне свято"),
            ("2022-05-03", "Національне свято Третього Травня"),
            ("2022-06-05", "День Святої Трійці"),
            ("2022-06-16", "Свято Тіла і Крові Христових"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-11", "День Незалежності"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )
