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

import unittest
from datetime import date

import holidays


class TestCyprus(unittest.TestCase):
    def setUp(self):
        self.cy_holidays = holidays.CY()

    def test_fixed_holidays(self):
        years = range(2000, 2025)
        for y in years:
            fdays = (
                (date(y, 1, 1), "Πρωτοχρονιά [New Year's Day]"),
                (date(y, 1, 6), "Θεοφάνεια [Epiphany]"),
                (
                    date(y, 3, 25),
                    "Εικοστή Πέμπτη Μαρτίου [Greek Independence Day]",
                ),
                (date(y, 4, 1), "1η Απριλίου [Cyprus National Day]"),
                (date(y, 5, 1), "Εργατική Πρωτομαγιά [Labour day]"),
                (
                    date(y, 8, 15),
                    "Κοίμηση της Θεοτόκου [Assumption of Mary]",
                ),
                (date(y, 10, 28), "Ημέρα του Όχι [Ochi Day]"),
                (date(y, 12, 25), "Χριστούγεννα [Christmas]"),
                (
                    date(y, 12, 26),
                    "Δεύτερη μέρα Χριστουγέννων [Day after Christmas]",
                ),
            )

        for d, dstr in fdays:
            self.assertIn(d, self.cy_holidays)
            self.assertIn(dstr, self.cy_holidays[d])

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
            self.assertIn(d, self.cy_holidays)
            self.assertIn("Καθαρά Δευτέρα [Clean Monday]", self.cy_holidays[d])

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
            self.assertIn(d, self.cy_holidays)
            self.assertIn(
                "Μεγάλη Παρασκευή [Good Friday]", self.cy_holidays[d]
            )

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
            self.assertIn(d, self.cy_holidays)
            self.assertIn(
                "Κυριακή του Πάσχα [Easter Sunday]", self.cy_holidays[d]
            )

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
            self.assertIn(d, self.cy_holidays)
            self.assertIn(
                "Δευτέρα του Πάσχα [Easter Monday]", self.cy_holidays[d]
            )

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
            self.assertIn(d, self.cy_holidays)
            self.assertIn(
                "Δευτέρα του Αγίου Πνεύματος " + "[Monday of the Holy Spirit]",
                self.cy_holidays[d],
            )
