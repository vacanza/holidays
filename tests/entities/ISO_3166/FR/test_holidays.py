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

from holidays.entities.ISO_3166.FR import FrHolidays
from tests.common import CommonCountryTests


class TestFrHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(FrHolidays)

    def test_pre_1802(self):
        self.assertNoHoliday("1801-08-15", "1801-11-01", "1801-12-25")

    def test_2017(self):
        self.assertHolidayDates(
            FrHolidays(years=2017),
            "2017-01-01",
            "2017-04-17",
            "2017-05-01",
            "2017-05-08",
            "2017-05-25",
            "2017-06-05",
            "2017-07-14",
            "2017-08-15",
            "2017-11-01",
            "2017-11-11",
            "2017-12-25",
        )

    def test_2022(self):
        self.assertHolidayDates(
            FrHolidays(years=2022),
            "2022-01-01",
            "2022-04-18",
            "2022-05-01",
            "2022-05-08",
            "2022-05-26",
            "2022-06-06",
            "2022-07-14",
            "2022-08-15",
            "2022-11-01",
            "2022-11-11",
            "2022-12-25",
        )

    def test_jour_de_lan(self):
        self.assertHoliday("1811-01-01")
        self.assertNoHoliday("1810-01-01")
        self.assertNoHolidayName("Jour de l'an", FrHolidays(years=1810))

    def test_fete_du_travail(self):
        name_old = "Fête du Travail et de la Concorde sociale"
        name_new = "Fête du Travail"

        self.assertHoliday("1919-05-01")
        self.assertNoHoliday("1918-05-01")
        self.assertNoHolidayName(name_old, FrHolidays(years=1918))
        self.assertNoHolidayName(name_new, FrHolidays(years=range(1919, 1948)))
        self.assertNoHolidayName(name_old, FrHolidays(years=1948))
        self.assertHolidayName(name_old, "1919-05-01", "1947-05-01")
        self.assertHolidayName(name_new, "1948-05-01")

    def test_fete_de_la_victoire(self):
        self.assertHoliday(f"{year}-05-08" for year in range(1953, 1960))
        self.assertHoliday("1982-05-08")
        self.assertNoHoliday("1960-05-08", "1981-05-08")
        self.assertNoHolidayName("Fête de la Victoire", FrHolidays(years=range(1960, 1982)))

    def test_fete_nationale(self):
        self.assertHoliday("1880-07-14")
        self.assertNoHoliday("1879-07-14")
        self.assertNoHolidayName("Fête nationale", FrHolidays(years=1879))

    def test_armistice(self):
        self.assertHoliday("1918-11-11")
        self.assertNoHoliday("1917-11-11")
        self.assertNoHolidayName("Armistice", FrHolidays(years=1917))

    def test_lundi_de_pentecote(self):
        self.assertNoHoliday(
            "2005-05-16",
            "2006-06-05",
            "2007-05-28",
        )
        self.assertHoliday("2004-05-31", "2008-05-12")

    def test_ges(self):
        self.assertHoliday(
            FrHolidays(subdiv="GES"),
            "2017-04-14",
            "2017-12-26",
        )

    def test_yt(self):
        self.assertHoliday(
            FrHolidays(subdiv="YT"),
            "2017-04-27",
        )

    def test_wf(self):
        self.assertHoliday(
            FrHolidays(subdiv="WF"),
            "2017-04-28",
            "2017-07-29",
        )

    def test_martinique(self):
        self.assertHoliday(
            FrHolidays(subdiv="MQ"),
            "2017-04-14",
            "2017-05-22",
            "2017-07-21",
        )

    def test_guadeloupe(self):
        self.assertHoliday(
            FrHolidays(subdiv="GP"),
            "2017-04-14",
            "2017-05-27",
            "2017-07-21",
        )

    def test_saint_martin(self):
        self.assertHoliday(
            FrHolidays(subdiv="MF"),
            "2018-05-28",
        )
        self.assertNoHoliday(
            FrHolidays(subdiv="MF"),
            "2017-05-28",
        )

        self.assertNoHolidayName("Abolition de l'esclavage", FrHolidays(subdiv="MF", years=2017))

    def test_guyane(self):
        self.assertHoliday(
            FrHolidays(subdiv="GY"),
            "2017-06-10",
        )

    def test_polynesie_francaise(self):
        self.assertHoliday(
            FrHolidays(subdiv="PF"),
            "2017-03-05",
            "2017-04-14",
            "2017-06-29",
        )

    def test_nouvelle_caledonie(self):
        self.assertHoliday(
            FrHolidays(subdiv="NC"),
            "2017-09-24",
        )

    def test_saint_barthelemy(self):
        self.assertHoliday(FrHolidays(subdiv="BL"), "2017-10-09")

    def test_la_reunion(self):
        self.assertHoliday(
            FrHolidays(subdiv="RE"),
            "2017-12-20",
        )
        self.assertNoHoliday(
            FrHolidays(subdiv="RE"),
            "1980-12-20",
        )
        self.assertNoHolidayName("Abolition de l'esclavage", FrHolidays(subdiv="RE", years=1980))
