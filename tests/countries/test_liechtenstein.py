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

from holidays.countries.liechtenstein import Liechtenstein
from tests.common import CommonCountryTests


class TestLiechtenstein(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Liechtenstein)

    def test_new_years_day(self):
        self.assertHolidayName("Neujahr", (f"{year}-01-01" for year in self.full_range))

    def test_saint_berchtolds_day(self):
        name = "Berchtoldstag"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-01-02" for year in self.full_range))

    def test_epiphany(self):
        self.assertHolidayName(
            "Heilige Drei Könige", (f"{year}-01-06" for year in self.full_range)
        )

    def test_candlemas(self):
        self.assertHolidayName("Mariä Lichtmess", (f"{year}-02-02" for year in self.full_range))

    def test_shrove_tuesday(self):
        name = "Fasnachtsdienstag"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(
            name,
            "2020-02-25",
            "2021-02-16",
            "2022-03-01",
            "2023-02-21",
            "2024-02-13",
            "2025-03-04",
        )
        self.assertBankHolidayName(name, self.full_range)

    def test_saint_josephs_day(self):
        self.assertHolidayName("Josefstag", (f"{year}-03-19" for year in self.full_range))

    def test_good_friday(self):
        name = "Karfreitag"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertBankHolidayName(name, self.full_range)

    def test_easter_sunday(self):
        name = "Ostersonntag"
        self.assertHolidayName(
            name,
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Ostermontag"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        self.assertHolidayName("Tag der Arbeit", (f"{year}-05-01" for year in self.full_range))

    def test_ascension_day(self):
        name = "Auffahrt"
        self.assertHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, self.full_range)

    def test_whit_sunday(self):
        name = "Pfingstsonntag"
        self.assertHolidayName(
            name,
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
            "2025-06-08",
        )
        self.assertHolidayName(name, self.full_range)

    def test_whit_monday(self):
        name = "Pfingstmontag"
        self.assertHolidayName(
            name,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.full_range)

    def test_corpus_christi(self):
        name = "Fronleichnam"
        self.assertHolidayName(
            name,
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
            "2025-06-19",
        )
        self.assertHolidayName(name, self.full_range)

    def test_national_day(self):
        self.assertHolidayName("Staatsfeiertag", (f"{year}-08-15" for year in self.full_range))

    def test_nativity_of_mary(self):
        self.assertHolidayName("Mariä Geburt", (f"{year}-09-08" for year in self.full_range))

    def test_all_saints_day(self):
        self.assertHolidayName("Allerheiligen", (f"{year}-11-01" for year in self.full_range))

    def test_immaculate_conception(self):
        self.assertHolidayName("Mariä Empfängnis", (f"{year}-12-08" for year in self.full_range))

    def test_christmas_eve(self):
        name = "Heiligabend"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-12-24" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName("Weihnachten", (f"{year}-12-25" for year in self.full_range))

    def test_st_stephens_day(self):
        self.assertHolidayName("Stephanstag", (f"{year}-12-26" for year in self.full_range))

    def test_new_years_eve(self):
        name = "Silvester"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-12-31" for year in self.full_range))

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "Neujahr"),
            ("2022-01-06", "Heilige Drei Könige"),
            ("2022-02-02", "Mariä Lichtmess"),
            ("2022-03-19", "Josefstag"),
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
            ("2022-12-25", "Weihnachten"),
            ("2022-12-26", "Stephanstag"),
        )

    def test_2022_bank(self):
        self.assertBankHolidaysInYear(
            2022,
            ("2022-01-02", "Berchtoldstag"),
            ("2022-03-01", "Fasnachtsdienstag"),
            ("2022-04-15", "Karfreitag"),
            ("2022-12-24", "Heiligabend"),
            ("2022-12-31", "Silvester"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
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
            ("2022-12-26", "Stephanstag"),
            ("2022-12-31", "Silvester"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-02", "Saint Berchtold's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-02-02", "Candlemas"),
            ("2022-03-01", "Shrove Tuesday"),
            ("2022-03-19", "Saint Joseph's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-06", "Whit Monday"),
            ("2022-06-16", "Corpus Christi"),
            ("2022-08-15", "National Day"),
            ("2022-09-08", "Nativity of Mary"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-08", "Immaculate Conception"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Saint Stephen's Day"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-02", "День Святого Бертольда"),
            ("2022-01-06", "Богоявлення"),
            ("2022-02-02", "Стрітення"),
            ("2022-03-01", "Масний вівторок"),
            ("2022-03-19", "День Святого Йосипа"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-05", "Трійця"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-06-16", "Свято Тіла і Крові Христових"),
            ("2022-08-15", "Національне свято"),
            ("2022-09-08", "Різдво Пресвятої Богородиці"),
            ("2022-11-01", "День усіх святих"),
            ("2022-12-08", "Непорочне зачаття Діви Марії"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "День Святого Стефана"),
            ("2022-12-31", "Переддень Нового року"),
        )
