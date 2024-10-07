#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.andorra import Andorra, AD, AND
from tests.common import CommonCountryTests


class TestAndorra(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Andorra)

    def test_country_aliases(self):
        self.assertAliases(Andorra, AD, AND)

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-03-01", "Carnival"),
            ("2022-03-14", "Constitution Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-06-06", "Whit Monday"),
            ("2022-08-15", "Assumption Day"),
            ("2022-09-08", "National Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-08", "Immaculate Conception Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Saint Stephen's Day"),
        )

        # AD-02, Canillo.
        self.assertHoliday(Andorra(subdiv="02"), "2022-07-16", "2022-07-17", "2022-07-18")

        # AD-03, Encamp.
        self.assertHoliday(Andorra(subdiv="03"), "2022-08-15", "2022-08-16")

        # AD-04, La Massana.
        self.assertHoliday(Andorra(subdiv="04"), "2022-08-15", "2022-08-16")

        # AD-05, Ordino.
        self.assertHoliday(Andorra(subdiv="05"), "2022-08-15", "2022-08-16")

        # AD-06, Sant Julià de Lòria.
        self.assertHoliday(
            Andorra(subdiv="06"),
            "2022-07-29",
            "2022-07-30",
            "2022-07-31",
            "2022-08-01",
        )

        # AD-07, Andorra la Vella.
        self.assertHoliday(Andorra(subdiv="07"), "2022-08-06", "2022-08-07", "2022-08-08")

        # AD-08, Escaldes-Engordany.
        self.assertHoliday(Andorra(subdiv="08"), "2022-07-25", "2022-07-26")

    def test_2023(self):
        self.assertHolidays(
            ("2023-01-01", "New Year's Day"),
            ("2023-01-06", "Epiphany"),
            ("2023-02-21", "Carnival"),
            ("2023-03-14", "Constitution Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-05-01", "Labor Day"),
            ("2023-05-29", "Whit Monday"),
            ("2023-08-15", "Assumption Day"),
            ("2023-09-08", "National Day"),
            ("2023-11-01", "All Saints' Day"),
            ("2023-12-08", "Immaculate Conception Day"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Saint Stephen's Day"),
        )

        # AD-02, Canillo.
        self.assertHoliday(Andorra(subdiv="02"), "2023-07-15", "2023-07-16", "2023-07-17")

        # AD-03, Encamp.
        self.assertHoliday(Andorra(subdiv="03"), "2023-08-15", "2023-08-16")

        # AD-04, La Massana.
        self.assertHoliday(Andorra(subdiv="04"), "2023-08-15", "2023-08-16")

        # AD-05, Ordino.
        self.assertHoliday(Andorra(subdiv="05"), "2023-08-15", "2023-08-16")

        # AD-06, Sant Julià de Lòria.
        self.assertHoliday(
            Andorra(subdiv="06"),
            "2023-07-28",
            "2023-07-29",
            "2023-07-30",
            "2023-07-31",
        )

        # AD-07, Andorra la Vella.
        self.assertHoliday(Andorra(subdiv="07"), "2023-08-05", "2023-08-06", "2023-08-07")

        # AD-08, Escaldes-Engordany.
        self.assertHoliday(Andorra(subdiv="08"), "2023-07-25", "2023-07-26")
