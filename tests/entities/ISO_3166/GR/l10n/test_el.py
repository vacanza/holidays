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

from holidays.entities.ISO_3166.GR import GrHolidays
from tests.common import CommonCountryTests


class TestGrHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(GrHolidays)

    def test_el(self):
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
