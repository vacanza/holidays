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

from datetime import date

from holidays.countries.cyprus import Cyprus, CY, CYP
from tests.common import TestCase


class TestCyprus(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Cyprus)

    def test_country_aliases(self):
        self.assertCountryAliases(Cyprus, CY, CYP)

    def test_fixed_holidays(self):
        years = range(2000, 2025)
        for y in years:
            fdays = (
                (date(y, 1, 1), "Πρωτοχρονιά"),
                (date(y, 1, 6), "Θεοφάνεια"),
                (date(y, 3, 25), "Εικοστή Πέμπτη Μαρτίου"),
                (date(y, 4, 1), "1η Απριλίου"),
                (date(y, 5, 1), "Εργατική Πρωτομαγιά"),
                (date(y, 8, 15), "Κοίμηση της Θεοτόκου"),
                (date(y, 10, 28), "Ημέρα του Όχι"),
                (date(y, 12, 25), "Χριστούγεννα"),
                (date(y, 12, 26), "Δεύτερη μέρα Χριστουγέννων"),
            )

        for d, dstr in fdays:
            self.assertIn(d, self.holidays)
            self.assertIn(dstr, self.holidays[d])

    def test_cy_clean_monday(self):
        checkdates = (
            date(2018, 2, 19),
            date(2019, 3, 11),
            date(2020, 3, 2),
            date(2021, 3, 15),
            date(2022, 3, 7),
            date(2023, 2, 27),
            date(2024, 3, 18),
        )

        for d in checkdates:
            self.assertIn(d, self.holidays)
            self.assertIn("Καθαρά Δευτέρα", self.holidays[d])

    def test_cy_good_friday(self):
        checkdates = (
            date(2018, 4, 6),
            date(2019, 4, 26),
            date(2020, 4, 17),
            date(2021, 4, 30),
            date(2022, 4, 22),
            date(2023, 4, 14),
            date(2024, 5, 3),
        )

        for d in checkdates:
            self.assertIn(d, self.holidays)
            self.assertIn("Μεγάλη Παρασκευή", self.holidays[d])

    def test_cy_easter_sunday(self):
        checkdates = (
            date(2018, 4, 8),
            date(2019, 4, 28),
            date(2020, 4, 19),
            date(2021, 5, 2),
            date(2022, 4, 24),
            date(2023, 4, 16),
            date(2024, 5, 5),
        )

        for d in checkdates:
            self.assertIn(d, self.holidays)
            self.assertIn("Κυριακή του Πάσχα", self.holidays[d])

    def test_cy_easter_monday(self):
        checkdates = (
            date(2018, 4, 9),
            date(2019, 4, 29),
            date(2020, 4, 20),
            date(2021, 5, 3),
            date(2022, 4, 25),
            date(2023, 4, 17),
            date(2024, 5, 6),
        )

        for d in checkdates:
            self.assertIn(d, self.holidays)
            self.assertIn("Δευτέρα του Πάσχα", self.holidays[d])

    def test_cy_monday_of_the_holy_spirit(self):
        checkdates = (
            date(2018, 5, 28),
            date(2019, 6, 17),
            date(2020, 6, 8),
            date(2021, 6, 21),
            date(2022, 6, 13),
            date(2023, 6, 5),
            date(2024, 6, 24),
        )

        for d in checkdates:
            self.assertIn(d, self.holidays)
            self.assertIn("Δευτέρα του Αγίου Πνεύματος", self.holidays[d])

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Πρωτοχρονιά"),
            ("2022-01-06", "Θεοφάνεια"),
            ("2022-03-07", "Καθαρά Δευτέρα"),
            ("2022-03-25", "Εικοστή Πέμπτη Μαρτίου"),
            ("2022-04-01", "1η Απριλίου"),
            ("2022-04-22", "Μεγάλη Παρασκευή"),
            ("2022-04-24", "Κυριακή του Πάσχα"),
            ("2022-04-25", "Δευτέρα του Πάσχα"),
            ("2022-05-01", "Εργατική Πρωτομαγιά"),
            ("2022-06-13", "Δευτέρα του Αγίου Πνεύματος"),
            ("2022-08-15", "Κοίμηση της Θεοτόκου"),
            ("2022-10-01", "Ημέρα Ανεξαρτησίας της Κύπρου"),
            ("2022-10-28", "Ημέρα του Όχι"),
            ("2022-12-24", "Παραμονή Χριστουγέννων"),
            ("2022-12-25", "Χριστούγεννα"),
            ("2022-12-26", "Δεύτερη μέρα Χριστουγέννων"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-03-07", "Clean Monday"),
            ("2022-03-25", "Greek Independence Day"),
            ("2022-04-01", "Cyprus National Day"),
            ("2022-04-22", "Good Friday"),
            ("2022-04-24", "Easter Sunday"),
            ("2022-04-25", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-06-13", "Monday of the Holy Spirit"),
            ("2022-08-15", "Assumption of Mary"),
            ("2022-10-01", "Cyprus Independence Day"),
            ("2022-10-28", "Ochi Day"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Day After Christmas"),
        )
