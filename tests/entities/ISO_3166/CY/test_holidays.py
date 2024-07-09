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

from holidays.constants import BANK, OPTIONAL, PUBLIC
from holidays.entities.ISO_3166.CY import CyHolidays
from tests.common import CommonCountryTests


class TestCyHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CyHolidays, years=range(2000, 2025))

    def test_no_holidays(self):
        self.assertNoHolidays(CyHolidays(categories=(BANK, OPTIONAL, PUBLIC), years=1960))

    def test_fixed_holidays(self):
        fdays = (
            (1, 1, "Πρωτοχρονιά"),
            (1, 6, "Ημέρα των Θεοφανίων"),
            (3, 25, "Ημέρα της Ελληνικής Ανεξαρτησίας"),
            (4, 1, "Εθνική Ημέρα Κύπρου"),
            (5, 1, "Πρωτομαγιά"),
            (8, 15, "Κοίμηση της Θεοτόκου"),
            (10, 1, "Ημέρα της Κυπριακής Ανεξαρτησίας"),
            (10, 28, "Ημέρα του Όχι"),
            (12, 25, "Χριστούγεννα"),
            (12, 26, "Επομένη Χριστουγέννων"),
        )
        for y in range(2000, 2025):
            for m, d, name in fdays:
                self.assertHolidayName(name, f"{y}-{m}-{d}")

    def test_green_monday(self):
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

    def test_easter_sunday(self):
        self.assertHolidayName(
            "Κυριακή του Πάσχα",
            "2018-04-08",
            "2019-04-28",
            "2020-04-19",
            "2021-05-02",
            "2022-04-24",
            "2023-04-16",
            "2024-05-05",
        )

    def test_easter_monday(self):
        self.assertHolidayName(
            "Δευτέρα της Διακαινησίμου",
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

    def test_cyprus_independence_day(self):
        name = "Ημέρα της Κυπριακής Ανεξαρτησίας"
        self.assertHolidayName(name, (f"{year}-10-01" for year in range(1979, 2025)))
        self.assertNoHolidayName(name, CyHolidays(years=range(1961, 1979)))

    def test_bank_2023(self):
        self.assertHolidays(
            CyHolidays(categories=BANK, years=2023),
            ("2023-04-18", "Τρίτη της Διακαινησίμου"),
        )

    def test_optional_2023(self):
        self.assertHolidays(
            CyHolidays(categories=OPTIONAL, years=2023),
            ("2023-04-15", "Μεγάλο Σάββατο"),
            ("2023-12-24", "Παραμονή Χριστουγέννων"),
        )
