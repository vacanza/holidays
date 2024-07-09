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

from holidays.entities.ISO_3166.CY import CyHolidays
from tests.common import CommonCountryTests


class TestCyHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CyHolidays)

    def test_el(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Πρωτοχρονιά"),
            ("2023-01-06", "Ημέρα των Θεοφανίων"),
            ("2023-02-27", "Καθαρά Δευτέρα"),
            ("2023-03-25", "Ημέρα της Ελληνικής Ανεξαρτησίας"),
            ("2023-04-01", "Εθνική Ημέρα Κύπρου"),
            ("2023-04-14", "Μεγάλη Παρασκευή"),
            ("2023-04-15", "Μεγάλο Σάββατο"),
            ("2023-04-16", "Κυριακή του Πάσχα"),
            ("2023-04-17", "Δευτέρα της Διακαινησίμου"),
            ("2023-04-18", "Τρίτη της Διακαινησίμου"),
            ("2023-05-01", "Πρωτομαγιά"),
            ("2023-06-05", "Δευτέρα του Αγίου Πνεύματος"),
            ("2023-08-15", "Κοίμηση της Θεοτόκου"),
            ("2023-10-01", "Ημέρα της Κυπριακής Ανεξαρτησίας"),
            ("2023-10-28", "Ημέρα του Όχι"),
            ("2023-12-24", "Παραμονή Χριστουγέννων"),
            ("2023-12-25", "Χριστούγεννα"),
            ("2023-12-26", "Επομένη Χριστουγέννων"),
        )
