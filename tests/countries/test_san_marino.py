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

from holidays.countries.san_marino import SanMarino
from tests.common import CommonCountryTests


class TestSanMarino(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SanMarino)

    def test_new_years_day(self):
        self.assertHolidayName("Capodanno", (f"{year}-01-01" for year in self.full_range))

    def test_epiphany(self):
        self.assertHolidayName("Epifania", (f"{year}-01-06" for year in self.full_range))

    def test_anniversary_of_liberation_of_republic(self):
        self.assertHolidayName(
            "Anniversario della Liberazione della Repubblica e Festa di Sant'Agata",
            (f"{year}-02-05" for year in self.full_range),
        )

    def test_anniversary_of_arengo(self):
        self.assertHolidayName(
            "Anniversario dell'Arengo", (f"{year}-03-25" for year in self.full_range)
        )

    def test_easter_sunday(self):
        name = "Pasqua"
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
        name = "Lunedì dell'angelo"
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

    def test_investiture_of_captains_regent(self):
        self.assertHolidayName(
            "Investitura Capitani Reggenti",
            (f"{year}-04-01" for year in self.full_range),
            (f"{year}-10-01" for year in self.full_range),
        )

    def test_workers_day(self):
        self.assertHolidayName(
            "Festa dei lavoratori", (f"{year}-05-01" for year in self.full_range)
        )

    def test_corpus_christi(self):
        name = "Corpus Domini"
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

    def test_anniversary_of_fall_of_fascism(self):
        self.assertHolidayName(
            "Anniversario della Caduta del Fascismo e Festa della Libertà",
            (f"{year}-07-28" for year in self.full_range),
        )

    def test_assumption_day(self):
        self.assertHolidayName(
            "Assunzione della B.V. Maria", (f"{year}-08-15" for year in self.full_range)
        )

    def test_saint_marinus_day(self):
        self.assertHolidayName(
            "San Marino, Anniversario di Fondazione della Repubblica",
            (f"{year}-09-03" for year in self.full_range),
        )

    def test_all_saints_day(self):
        self.assertHolidayName("Tutti i Santi", (f"{year}-11-01" for year in self.full_range))

    def test_commemoration_of_the_dead(self):
        self.assertHolidayName(
            "Commemorazione dei defunti", (f"{year}-11-02" for year in self.full_range)
        )

    def test_immaculate_conception(self):
        self.assertHolidayName(
            "Immacolata Concezione", (f"{year}-12-08" for year in self.full_range)
        )

    def test_christmas_day(self):
        self.assertHolidayName("Natale", (f"{year}-12-25" for year in self.full_range))

    def test_saint_stephens_day(self):
        self.assertHolidayName("Santo Stefano", (f"{year}-12-26" for year in self.full_range))

    def test_christmas_eve(self):
        name = "Vigilia di Natale"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-12-24" for year in self.full_range))

    def test_new_years_eve(self):
        name = "Ultimo dell'anno"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-12-31" for year in self.full_range))

    def test_2023(self):
        self.assertHolidaysInYear(
            2023,
            ("2023-01-01", "Capodanno"),
            ("2023-01-06", "Epifania"),
            (
                "2023-02-05",
                "Anniversario della Liberazione della Repubblica e Festa di Sant'Agata",
            ),
            ("2023-03-25", "Anniversario dell'Arengo"),
            ("2023-04-01", "Investitura Capitani Reggenti"),
            ("2023-04-09", "Pasqua"),
            ("2023-04-10", "Lunedì dell'angelo"),
            ("2023-05-01", "Festa dei lavoratori"),
            ("2023-06-08", "Corpus Domini"),
            ("2023-07-28", "Anniversario della Caduta del Fascismo e Festa della Libertà"),
            ("2023-08-15", "Assunzione della B.V. Maria"),
            ("2023-09-03", "San Marino, Anniversario di Fondazione della Repubblica"),
            ("2023-10-01", "Investitura Capitani Reggenti"),
            ("2023-11-01", "Tutti i Santi"),
            ("2023-11-02", "Commemorazione dei defunti"),
            ("2023-12-08", "Immacolata Concezione"),
            ("2023-12-25", "Natale"),
            ("2023-12-26", "Santo Stefano"),
        )

    def test_2023_bank(self):
        self.assertBankHolidaysInYear(
            2023,
            ("2023-12-24", "Vigilia di Natale"),
            ("2023-12-31", "Ultimo dell'anno"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Capodanno"),
            ("2024-01-06", "Epifania"),
            (
                "2024-02-05",
                "Anniversario della Liberazione della Repubblica e Festa di Sant'Agata",
            ),
            ("2024-03-25", "Anniversario dell'Arengo"),
            ("2024-03-31", "Pasqua"),
            ("2024-04-01", "Investitura Capitani Reggenti; Lunedì dell'angelo"),
            ("2024-05-01", "Festa dei lavoratori"),
            ("2024-05-30", "Corpus Domini"),
            ("2024-07-28", "Anniversario della Caduta del Fascismo e Festa della Libertà"),
            ("2024-08-15", "Assunzione della B.V. Maria"),
            ("2024-09-03", "San Marino, Anniversario di Fondazione della Repubblica"),
            ("2024-10-01", "Investitura Capitani Reggenti"),
            ("2024-11-01", "Tutti i Santi"),
            ("2024-11-02", "Commemorazione dei defunti"),
            ("2024-12-08", "Immacolata Concezione"),
            ("2024-12-24", "Vigilia di Natale"),
            ("2024-12-25", "Natale"),
            ("2024-12-26", "Santo Stefano"),
            ("2024-12-31", "Ultimo dell'anno"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-06", "Epiphany"),
            (
                "2024-02-05",
                "Anniversary of the Liberation of the Republic and Feast of Saint Agatha",
            ),
            ("2024-03-25", "Anniversary of the Arengo"),
            ("2024-03-31", "Easter Sunday"),
            ("2024-04-01", "Easter Monday; Investiture of Captains Regent"),
            ("2024-05-01", "Workers' Day"),
            ("2024-05-30", "Corpus Christi"),
            ("2024-07-28", "Anniversary of the Fall of Fascism and Freedom Day"),
            ("2024-08-15", "Assumption Day"),
            ("2024-09-03", "Saint Marinus' Day, Anniversary of the Founding of the Republic"),
            ("2024-10-01", "Investiture of Captains Regent"),
            ("2024-11-01", "All Saints' Day"),
            ("2024-11-02", "Commemoration of the Dead"),
            ("2024-12-08", "Immaculate Conception"),
            ("2024-12-24", "Christmas Eve"),
            ("2024-12-25", "Christmas Day"),
            ("2024-12-26", "Saint Stephen's Day"),
            ("2024-12-31", "New Year's Eve"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2024-01-01", "Новий рік"),
            ("2024-01-06", "Богоявлення"),
            ("2024-02-05", "Річниця визволення Республіки та День Святої Агати"),
            ("2024-03-25", "Річниця Аренго"),
            ("2024-03-31", "Великдень"),
            ("2024-04-01", "Інвеститура капітанів-регентів; Великодній понеділок"),
            ("2024-05-01", "День трудящих"),
            ("2024-05-30", "Свято Тіла і Крові Христових"),
            ("2024-07-28", "Річниця падіння фашизму та День свободи"),
            ("2024-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2024-09-03", "Річниця заснування Республіки та День Святого Марина"),
            ("2024-10-01", "Інвеститура капітанів-регентів"),
            ("2024-11-01", "День усіх святих"),
            ("2024-11-02", "День вшанування померлих"),
            ("2024-12-08", "Непорочне зачаття Діви Марії"),
            ("2024-12-24", "Святий вечір"),
            ("2024-12-25", "Різдво Христове"),
            ("2024-12-26", "День Святого Стефана"),
            ("2024-12-31", "Переддень Нового року"),
        )
