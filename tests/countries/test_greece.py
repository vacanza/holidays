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

from holidays.countries.greece import Greece, GR, GRC
from tests.common import TestCase


class TestGreece(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Greece, years=range(2000, 2025))

    def test_country_aliases(self):
        self.assertCountryAliases(Greece, GR, GRC)

    def test_fixed_holidays(self):
        years = range(2000, 2025)
        for m, d, name in (
            (1, 1, "Πρωτοχρονιά"),
            (1, 6, "Θεοφάνεια"),
            (3, 25, "Εικοστή Πέμπτη Μαρτίου"),
            (5, 1, "Εργατική Πρωτομαγιά"),
            (8, 15, "Κοίμηση της Θεοτόκου"),
            (10, 28, "Ημέρα του Όχι"),
            (12, 25, "Χριστούγεννα"),
            (12, 26, "Επόμενη ημέρα των Χριστουγέννων"),
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

    def test_monday_of_the_holy_spirit(self):
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

    def test_labour_day_observed(self):
        name_observed = "Εργατική Πρωτομαγιά (παρατηρήθηκε)"
        dt = (
            "2011-05-02",
            "2016-05-03",
            "2021-05-04",
            "2022-05-02",
        )
        self.assertHolidayName(name_observed, dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNoHolidayName(name_observed, 2017, 2018, 2019, 2020, 2023)

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
            ("2022-12-25", "Χριστούγεννα"),
            ("2022-12-26", "Επόμενη ημέρα των Χριστουγέννων"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year’s Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-03-07", "Clean Monday"),
            ("2022-03-25", "Independence Day"),
            ("2022-04-22", "Good Friday"),
            ("2022-04-25", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Labor Day (Observed)"),
            ("2022-06-13", "Easter Monday"),
            ("2022-08-15", "Assumption of Mary Day"),
            ("2022-10-28", "Ochi Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Day After Christmas"),
        )
