#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.poland import Poland
from tests.common import CommonCountryTests


class TestPoland(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Poland, years=range(1925, 2050))

    def test_special_holidays(self):
        self.assertHoliday("2018-11-12")

    def test_new_years_day(self):
        self.assertHolidayName("Nowy Rok", (f"{year}-01-01" for year in range(1925, 2050)))

    def test_epiphany(self):
        name = "Święto Trzech Króli"
        self.assertHolidayName(
            name, (f"{year}-01-06" for year in (*range(1925, 1960), *range(2011, 2050)))
        )
        self.assertNoHoliday(f"{year}-01-06" for year in range(1961, 2011))
        self.assertNoHolidayName(name, range(1961, 2011))

    def test_candlemas(self):
        name = "Oczyszczenie Najświętszej Marii Panny"
        self.assertHolidayName(name, (f"{year}-02-02" for year in range(1925, 1951)))
        self.assertNoHoliday(f"{year}-02-02" for year in range(1951, 2050))
        self.assertNoHolidayName(name, range(1951, 2050))

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

    def test_national_day(self):
        name = "Święto Państwowe"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1950, 2050)))
        self.assertNoHoliday(f"{year}-05-01" for year in range(1925, 1950))
        self.assertNoHolidayName(name, range(1925, 1950))

    def test_national_day_of_third_of_may(self):
        name = "Święto Narodowe Trzeciego Maja"
        self.assertHolidayName(
            name, (f"{year}-05-03" for year in (*range(1925, 1951), *range(1990, 2050)))
        )
        self.assertNoHoliday(f"{year}-05-03" for year in range(1951, 1990))
        self.assertNoHolidayName(name, range(1951, 1990))

    def test_national_victory_and_freedom_day(self):
        name = "Narodowe Święto Zwycięstwa i Wolności"
        self.assertHolidayName(name, (f"{year}-05-09" for year in range(1946, 1951)))
        # Exclude Ascension day on 1929-05-09
        self.assertNoHoliday(
            f"{year}-05-09"
            for year in (*range(1925, 1929), *range(1930, 1946), *range(1951, 2050))
        )
        self.assertNoHolidayName(name, range(1925, 1946), range(1951, 2050))

    def test_ascension_day(self):
        name = "Wniebowstąpienie Pańskie"
        self.assertHolidayName(
            name,
            "1930-05-29",
            "1934-05-10",
            "1939-05-18",
            "1945-05-10",
            "1950-05-18",
        )
        self.assertHolidayName(name, range(1925, 1951))
        self.assertNoHolidayName(name, range(1951, 2050))

    def test_whit_monday(self):
        name = "Drugi dzień Zielonych Świątek"
        self.assertHolidayName(
            name,
            "1930-06-09",
            "1934-05-21",
            "1939-05-29",
            "1945-05-21",
            "1950-05-29",
        )
        self.assertHolidayName(name, range(1925, 1951))
        self.assertNoHolidayName(name, range(1951, 2050))

    def test_saints_peter_and_paul_day(self):
        name = "Uroczystość Świętych Apostołów Piotra i Pawła"
        self.assertHolidayName(name, (f"{year}-06-29" for year in range(1925, 1951)))
        self.assertNoHoliday(f"{year}-06-29" for year in range(1951, 2050))
        self.assertNoHolidayName(name, range(1951, 2050))

    def test_national_day_of_rebirth_of_poland(self):
        name = "Narodowe Święto Odrodzenia Polski"
        self.assertHolidayName(name, (f"{year}-07-22" for year in range(1945, 1990)))
        self.assertNoHoliday(f"{year}-07-22" for year in (*range(1925, 1945), *range(1990, 2050)))
        self.assertNoHolidayName(name, range(1925, 1945), range(1990, 2050))

    def test_assumption_day(self):
        name = "Wniebowzięcie Najświętszej Marii Panny"
        self.assertHolidayName(
            name, (f"{year}-08-15" for year in (*range(1925, 1961), *range(1989, 2050)))
        )
        self.assertNoHoliday(f"{year}-08-15" for year in range(1961, 1989))
        self.assertNoHolidayName(name, range(1961, 1989))

    def test_all_saints_day(self):
        self.assertHolidayName(
            "Uroczystość Wszystkich Świętych", (f"{year}-11-01" for year in range(1925, 2050))
        )

    def test_national_independence_day(self):
        name = "Narodowe Święto Niepodległości"
        self.assertHolidayName(
            name, (f"{year}-11-11" for year in (*range(1937, 1945), *range(1989, 2050)))
        )
        self.assertNoHoliday(f"{year}-11-11" for year in (*range(1925, 1937), *range(1945, 1989)))
        self.assertNoHolidayName(name, range(1925, 1937), range(1945, 1989))

    def test_immaculate_conception_day(self):
        name = "Niepokalane Poczęcie Najświętszej Marii Panny"
        self.assertHolidayName(name, (f"{year}-12-08" for year in range(1925, 1951)))
        self.assertNoHoliday(f"{year}-12-08" for year in range(1951, 2050))
        self.assertNoHolidayName(name, range(1951, 2050))

    def test_christmas_eve(self):
        name = "Wigilia Bożego Narodzenia"
        self.assertHolidayName(name, (f"{year}-12-24" for year in range(2025, 2050)))
        self.assertNoHoliday(f"{year}-12-24" for year in range(1925, 2025))
        self.assertNoHolidayName(name, range(1925, 2025))

    def test_christmas(self):
        self.assertHolidayName(
            "Boże Narodzenie (pierwszy dzień)", (f"{year}-12-25" for year in range(1925, 2050))
        )
        self.assertHolidayName(
            "Boże Narodzenie (drugi dzień)", (f"{year}-12-26" for year in range(1925, 2050))
        )

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

    def test_2025(self):
        self.assertHolidayDates(
            Poland(years=2025),
            "2025-01-01",
            "2025-01-06",
            "2025-04-20",
            "2025-04-21",
            "2025-05-01",
            "2025-05-03",
            "2025-06-08",
            "2025-06-19",
            "2025-08-15",
            "2025-11-01",
            "2025-11-11",
            "2025-12-24",
            "2025-12-25",
            "2025-12-26",
        )

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

    def test_l10n_de(self):
        self.assertLocalizedHolidays(
            "de",
            ("2018-01-01", "Neujahr"),
            ("2018-01-06", "Heilige Drei Könige"),
            ("2018-04-01", "Ostersonntag"),
            ("2018-04-02", "Ostermontag"),
            ("2018-05-01", "Tag der Arbeit"),
            ("2018-05-03", "Nationalfeiertag am 3. Mai"),
            ("2018-05-20", "Pfingsten"),
            ("2018-05-31", "Fronleichnam"),
            ("2018-08-15", "Mariä Himmelfahrt"),
            ("2018-11-01", "Allerheiligen"),
            ("2018-11-11", "Nationalfeiertag der Unabhängigkeit"),
            ("2018-11-12", "Nationalfeiertag der Unabhängigkeit - 100. Jahrestag"),
            ("2018-12-25", "Erster Weihnachtstag"),
            ("2018-12-26", "Zweiter Weihnachtstag"),
        )
        self.assertLocalizedHolidays(
            "de",
            ("2022-01-01", "Neujahr"),
            ("2022-01-06", "Heilige Drei Könige"),
            ("2022-04-17", "Ostersonntag"),
            ("2022-04-18", "Ostermontag"),
            ("2022-05-01", "Tag der Arbeit"),
            ("2022-05-03", "Nationalfeiertag am 3. Mai"),
            ("2022-06-05", "Pfingsten"),
            ("2022-06-16", "Fronleichnam"),
            ("2022-08-15", "Mariä Himmelfahrt"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-11-11", "Nationalfeiertag der Unabhängigkeit"),
            ("2022-12-25", "Erster Weihnachtstag"),
            ("2022-12-26", "Zweiter Weihnachtstag"),
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
            ("2018-11-11", "День незалежності"),
            ("2018-11-12", "100-а річниця Дня незалежності"),
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
            ("2022-11-11", "День незалежності"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )
