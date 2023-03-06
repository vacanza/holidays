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

from holidays.countries.greece import Greece, GR, GRC
from tests.common import TestCase


class TestGreece(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Greece)

    def test_country_aliases(self):
        self.assertCountryAliases(Greece, GR, GRC)

    def test_fixed_holidays(self):
        years = range(2000, 2025)
        for y in years:
            fdays = (
                (date(y, 1, 1), "Πρωτοχρονιά"),
                (date(y, 1, 6), "Θεοφάνεια"),
                (date(y, 3, 25), "Εικοστή Πέμπτη Μαρτίου"),
                (date(y, 5, 1), "Εργατική Πρωτομαγιά"),
                (date(y, 8, 15), "Κοίμηση της Θεοτόκου"),
                (date(y, 10, 28), "Ημέρα του Όχι"),
                (date(y, 12, 25), "Χριστούγεννα"),
                (date(y, 12, 26), "Επόμενη ημέρα των Χριστουγέννων"),
            )

            for d, dstr in fdays:
                self.assertIn(d, self.holidays)
                self.assertIn(dstr, self.holidays[d])

    def test_gr_clean_monday(self):
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

    def test_gr_easter_monday(self):
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

    def test_gr_monday_of_the_holy_spirit(self):
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

    def test_gr_labour_day_observed(self):
        # Dates when labour day was observed on a different date
        checkdates = (
            date(2016, 5, 3),
            date(2021, 5, 4),
            date(2022, 5, 2),
            date(2033, 5, 2),
        )
        # Years when labour date was observed on May 1st
        checkyears = (2017, 2018, 2019, 2020, 2023)

        for d in checkdates:
            self.assertIn(d, self.holidays)
            self.assertIn("Εργατική Πρωτομαγιά", self.holidays[d])

        # Check that there is no observed day created for years
        # when Labour Day was on May 1st
        for year in checkyears:
            for day in (2, 3, 4):
                d = date(year, 5, day)
                if d in self.holidays:
                    self.assertNotIn("Εργατική Πρωτομαγιά", self.holidays[d])
