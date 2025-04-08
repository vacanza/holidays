#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.french_southern_territories import (
    HolidaysTF,
    FrenchSouthernTerritories,
    TF,
    ATF,
)
from tests.common import CommonCountryTests


class TestTF(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HolidaysTF)

    def test_country_aliases(self):
        self.assertAliases(HolidaysTF, FrenchSouthernTerritories, TF, ATF)

    def test_pre_1802(self):
        self.assertNoHoliday("1801-08-15", "1801-11-01", "1801-12-25")

    def test_2017(self):
        self.assertHolidayDates(
            HolidaysTF(years=2017),
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
            HolidaysTF(years=2022),
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
        self.assertNoHolidayName("Jour de l'an", HolidaysTF(years=1810))

    def test_fete_du_travail(self):
        name_old = "Fête du Travail et de la Concorde sociale"
        name_new = "Fête du Travail"

        self.assertHoliday("1919-05-01")
        self.assertNoHoliday("1918-05-01")
        self.assertNoHolidayName(name_old, HolidaysTF(years=1918))
        self.assertNoHolidayName(name_new, HolidaysTF(years=range(1919, 1948)))
        self.assertNoHolidayName(name_old, HolidaysTF(years=1948))
        self.assertHolidayName(name_old, "1919-05-01", "1947-05-01")
        self.assertHolidayName(name_new, "1948-05-01")

    def test_fete_de_la_victoire(self):
        self.assertHoliday(*[f"{year}-05-08" for year in range(1953, 1960)])
        self.assertHoliday("1982-05-08")
        self.assertNoHoliday("1960-05-08", "1981-05-08")
        self.assertNoHolidayName("Fête de la Victoire", HolidaysTF(years=range(1960, 1982)))

    def test_fete_nationale(self):
        self.assertHoliday("1880-07-14")
        self.assertNoHoliday("1879-07-14")
        self.assertNoHolidayName("Fête nationale", HolidaysTF(years=1879))

    def test_armistice(self):
        self.assertHoliday("1918-11-11")
        self.assertNoHoliday("1917-11-11")
        self.assertNoHolidayName("Armistice", HolidaysTF(years=1917))

    def test_lundi_de_pentecote(self):
        self.assertNoHoliday(
            "2005-05-12",
            "2006-05-12",
            "2007-05-28",
        )
        self.assertHoliday("2004-05-31", "2008-05-12")

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Jour de l'an"),
            ("2022-04-18", "Lundi de Pâques"),
            ("2022-05-01", "Fête du Travail"),
            ("2022-05-08", "Fête de la Victoire"),
            ("2022-05-26", "Ascension"),
            ("2022-06-06", "Lundi de Pentecôte"),
            ("2022-07-14", "Fête nationale"),
            ("2022-08-15", "Assomption"),
            ("2022-11-01", "Toussaint"),
            ("2022-11-11", "Armistice"),
            ("2022-12-25", "Noël"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-08", "Victory Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-06", "Whit Monday"),
            ("2022-07-14", "National Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-11", "Armistice Day"),
            ("2022-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-08", "День Перемоги"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-07-14", "Національне свято"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-11", "День перемирʼя"),
            ("2022-12-25", "Різдво Христове"),
        )
