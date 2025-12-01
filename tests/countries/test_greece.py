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

from holidays.countries.greece import Greece
from tests.common import CommonCountryTests


class TestGreece(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Greece)

    def test_new_years_day(self):
        self.assertHolidayName("Πρωτοχρονιά", (f"{year}-01-01" for year in self.full_range))

    def test_epiphany(self):
        self.assertHolidayName("Θεοφάνεια", (f"{year}-01-06" for year in self.full_range))

    def test_clean_monday(self):
        name = "Καθαρά Δευτέρα"
        self.assertHolidayName(
            name,
            "2020-03-02",
            "2021-03-15",
            "2022-03-07",
            "2023-02-27",
            "2024-03-18",
            "2025-03-03",
        )
        self.assertHolidayName(name, self.full_range)

    def test_independence_day(self):
        self.assertHolidayName(
            "Εικοστή Πέμπτη Μαρτίου", (f"{year}-03-25" for year in self.full_range)
        )

    def test_good_friday(self):
        name = "Μεγάλη Παρασκευή"
        self.assertHolidayName(
            name,
            "2020-04-17",
            "2021-04-30",
            "2022-04-22",
            "2023-04-14",
            "2024-05-03",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_easter_monday(self):
        name = "Δευτέρα του Πάσχα"
        self.assertHolidayName(
            name,
            "2020-04-20",
            "2021-05-03",
            "2022-04-25",
            "2023-04-17",
            "2024-05-06",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        name = "Εργατική Πρωτομαγιά"
        self.assertHolidayName(
            name,
            "2024-05-07",
            (
                f"{year}-05-01"
                for year in (*range(self.start_year, 2024), *range(2025, self.end_year))
            ),
        )
        obs_dt = (
            "2021-05-04",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (παρατηρήθηκε)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_whit_monday(self):
        name = "Δευτέρα του Αγίου Πνεύματος"
        self.assertHolidayName(
            name,
            "2020-06-08",
            "2021-06-21",
            "2022-06-13",
            "2023-06-05",
            "2024-06-24",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.full_range)

    def test_assumption_day(self):
        self.assertHolidayName(
            "Κοίμηση της Θεοτόκου", (f"{year}-08-15" for year in self.full_range)
        )

    def test_ochi_day(self):
        self.assertHolidayName("Ημέρα του Όχι", (f"{year}-10-28" for year in self.full_range))

    def test_christmas_eve(self):
        name = "Παραμονή Χριστουγέννων"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(name, (f"{year}-12-24" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName("Χριστούγεννα", (f"{year}-12-25" for year in self.full_range))

    def test_boxing_day(self):
        self.assertHolidayName(
            "Σύναξη της Υπεραγίας Θεοτόκου", (f"{year}-12-26" for year in self.full_range)
        )

    def test_new_years_eve(self):
        name = "Παραμονή Πρωτοχρονιάς"
        self.assertNoHolidayName(name)
        self.assertHalfDayHolidayName(name, (f"{year}-12-31" for year in self.full_range))

    def test_2024(self):
        self.assertHolidays(
            Greece(years=2024),
            ("2024-01-01", "Πρωτοχρονιά"),
            ("2024-01-06", "Θεοφάνεια"),
            ("2024-03-18", "Καθαρά Δευτέρα"),
            ("2024-03-25", "Εικοστή Πέμπτη Μαρτίου"),
            ("2024-05-03", "Μεγάλη Παρασκευή"),
            ("2024-05-06", "Δευτέρα του Πάσχα"),
            ("2024-05-07", "Εργατική Πρωτομαγιά"),
            ("2024-06-24", "Δευτέρα του Αγίου Πνεύματος"),
            ("2024-08-15", "Κοίμηση της Θεοτόκου"),
            ("2024-10-28", "Ημέρα του Όχι"),
            ("2024-12-25", "Χριστούγεννα"),
            ("2024-12-26", "Σύναξη της Υπεραγίας Θεοτόκου"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Πρωτοχρονιά"),
            ("2022-01-06", "Θεοφάνεια"),
            ("2022-03-07", "Καθαρά Δευτέρα"),
            ("2022-03-25", "Εικοστή Πέμπτη Μαρτίου"),
            ("2022-04-22", "Μεγάλη Παρασκευή"),
            ("2022-04-25", "Δευτέρα του Πάσχα"),
            ("2022-05-01", "Εργατική Πρωτομαγιά"),
            ("2022-05-02", "Εργατική Πρωτομαγιά (παρατηρήθηκε)"),
            ("2022-06-13", "Δευτέρα του Αγίου Πνεύματος"),
            ("2022-08-15", "Κοίμηση της Θεοτόκου"),
            ("2022-10-28", "Ημέρα του Όχι"),
            ("2022-12-24", "Παραμονή Χριστουγέννων"),
            ("2022-12-25", "Χριστούγεννα"),
            ("2022-12-26", "Σύναξη της Υπεραγίας Θεοτόκου"),
            ("2022-12-31", "Παραμονή Πρωτοχρονιάς"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-03-07", "Green Monday"),
            ("2022-03-25", "Independence Day"),
            ("2022-04-22", "Good Friday"),
            ("2022-04-25", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Labor Day (observed)"),
            ("2022-06-13", "Whit Monday"),
            ("2022-08-15", "Dormition of the Mother of God"),
            ("2022-10-28", "Ochi Day"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Glorifying Mother of God"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-06", "Богоявлення"),
            ("2022-03-07", "Чистий понеділок"),
            ("2022-03-25", "День незалежності"),
            ("2022-04-22", "Страсна пʼятниця"),
            ("2022-04-25", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-02", "День праці (вихідний)"),
            ("2022-06-13", "День Святого Духа"),
            ("2022-08-15", "Успіння Пресвятої Богородиці"),
            ("2022-10-28", "День Охі"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Собор Пресвятої Богородиці"),
            ("2022-12-31", "Переддень Нового року"),
        )
