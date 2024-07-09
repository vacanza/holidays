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

from holidays.constants import HALF_DAY
from holidays.entities.ISO_3166.GR import GrHolidays
from tests.common import CommonCountryTests


class TestGrHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(GrHolidays, years=range(2000, 2025))

    def test_fixed_holidays(self):
        years = range(2000, 2024)
        for m, d, name in (
            (1, 1, "Πρωτοχρονιά"),
            (1, 6, "Θεοφάνεια"),
            (3, 25, "Εικοστή Πέμπτη Μαρτίου"),
            (5, 1, "Εργατική Πρωτομαγιά"),
            (8, 15, "Κοίμηση της Θεοτόκου"),
            (10, 28, "Ημέρα του Όχι"),
            (12, 25, "Χριστούγεννα"),
            (12, 26, "Σύναξη της Υπεραγίας Θεοτόκου"),
        ):
            self.assertHolidayName(name, (f"{year}-{m}-{d}" for year in years))

    def test_clean_monday(self):
        self.assertHolidayName(
            "Καθαρά Δευτέρα",
            "2018-02-19",
            "2019-03-11",
            "2020-03-02",
            "2021-03-15",
            "2022-03-07",
            "2023-02-27",
            "2024-03-18",
        )

    def test_good_friday(self):
        self.assertHolidayName(
            "Μεγάλη Παρασκευή",
            "2018-04-06",
            "2019-04-26",
            "2020-04-17",
            "2021-04-30",
            "2022-04-22",
            "2023-04-14",
            "2024-05-03",
        )

    def test_easter_monday(self):
        self.assertHolidayName(
            "Δευτέρα του Πάσχα",
            "2018-04-09",
            "2019-04-29",
            "2020-04-20",
            "2021-05-03",
            "2022-04-25",
            "2023-04-17",
            "2024-05-06",
        )

    def test_whit_monday(self):
        self.assertHolidayName(
            "Δευτέρα του Αγίου Πνεύματος",
            "2018-05-28",
            "2019-06-17",
            "2020-06-08",
            "2021-06-21",
            "2022-06-13",
            "2023-06-05",
            "2024-06-24",
        )

    def test_labor_day_observed(self):
        name_observed = "Εργατική Πρωτομαγιά (παρατηρήθηκε)"
        dt = (
            "2021-05-04",
            "2022-05-02",
        )
        self.assertHolidayName(name_observed, dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNoHolidayName(name_observed, range(2000, 2021), 2023)

    def test_half_day_2022(self):
        self.assertHolidays(
            GrHolidays(categories=HALF_DAY, years=2022),
            ("2022-12-24", "Παραμονή Χριστουγέννων"),
            ("2022-12-31", "Παραμονή Πρωτοχρονιάς"),
        )
        self.assertNoHoliday(
            "2022-12-24",
            "2022-12-31",
        )

    def test_2024(self):
        self.assertHolidays(
            GrHolidays(years=2024),
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
