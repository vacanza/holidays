#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.democratic_republic_of_the_congo import (
    DemocraticRepublicOfTheCongo,
    CD,
    COD,
)
from tests.common import CommonCountryTests


class TestDemocraticRepublicOfTheCongo(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(DemocraticRepublicOfTheCongo, years=range(1960, 2050))

    def test_country_aliases(self):
        self.assertAliases(DemocraticRepublicOfTheCongo, CD, COD)

    def test_no_holidays(self):
        self.assertNoHolidays(DemocraticRepublicOfTheCongo(years=1959))

    def test_2006(self):
        self.assertHolidays(
            DemocraticRepublicOfTheCongo(years=2006),
            ("2006-01-01", "Jour de l'An"),
            ("2006-01-04", "Journée des Martyrs"),
            ("2006-01-16", "Assassinat de Laurent-Désiré Kabila"),
            ("2006-01-17", "Assassinat de Patrice Lumumba"),
            ("2006-05-01", "Fête du Travail"),
            ("2006-05-17", "Jour de la Libération"),
            ("2006-06-30", "Jour de l'indépendance"),
            ("2006-08-01", "Journée des parents"),
            ("2006-12-25", "Noël"),
        )

    def test_2010(self):
        self.assertHolidays(
            DemocraticRepublicOfTheCongo(years=2010),
            ("2010-01-01", "Jour de l'An"),
            ("2010-01-04", "Journée des Martyrs"),
            ("2010-01-16", "Assassinat de Laurent-Désiré Kabila"),
            ("2010-01-17", "Assassinat de Patrice Lumumba"),
            ("2010-05-01", "Fête du Travail"),
            ("2010-05-17", "Jour de la Libération"),
            ("2010-06-30", "Jour de l'indépendance"),
            ("2010-08-01", "Journée des parents"),
            ("2010-12-25", "Noël"),
        )

    def test_2015(self):
        self.assertHolidays(
            DemocraticRepublicOfTheCongo(years=2015),
            ("2015-01-01", "Jour de l'An"),
            ("2015-01-04", "Journée des Martyrs"),
            ("2015-01-16", "Assassinat de Laurent-Désiré Kabila"),
            ("2015-01-17", "Assassinat de Patrice Lumumba"),
            ("2015-05-01", "Fête du Travail"),
            ("2015-05-17", "Jour de la Libération"),
            ("2015-06-30", "Jour de l'indépendance"),
            ("2015-08-01", "Journée des parents"),
            ("2015-12-25", "Noël"),
        )

    def test_2016(self):
        self.assertHolidays(
            DemocraticRepublicOfTheCongo(years=2016),
            ("2016-01-01", "Jour de l'An"),
            ("2016-01-04", "Journée des Martyrs"),
            ("2016-01-16", "Assassinat de Laurent-Désiré Kabila"),
            ("2016-01-17", "Assassinat de Patrice Lumumba"),
            ("2016-05-01", "Fête du Travail"),
            ("2016-05-17", "Jour de la Libération"),
            ("2016-06-30", "Jour de l'indépendance"),
            ("2016-08-01", "Journée des parents"),
            ("2016-12-25", "Noël"),
        )

    def test_2017(self):
        self.assertHolidays(
            DemocraticRepublicOfTheCongo(years=2017),
            ("2017-01-01", "Jour de l'An"),
            ("2017-01-04", "Journée des Martyrs"),
            ("2017-01-16", "Assassinat de Laurent-Désiré Kabila"),
            ("2017-01-17", "Assassinat de Patrice Lumumba"),
            ("2017-05-01", "Fête du Travail"),
            ("2017-05-17", "Jour de la Libération"),
            ("2017-06-30", "Jour de l'indépendance"),
            ("2017-08-01", "Journée des parents"),
            ("2017-12-25", "Noël"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Jour de l'An"),
            ("2024-01-04", "Journée des Martyrs"),
            ("2024-01-16", "Assassinat de Laurent-Désiré Kabila"),
            ("2024-01-17", "Assassinat de Patrice Lumumba"),
            ("2024-04-06", "Journée de Kimbangu"),
            ("2024-05-01", "Fête du Travail"),
            ("2024-05-17", "Journée des forces armées"),
            ("2024-06-30", "Jour de l'indépendance"),
            ("2024-08-01", "Journée des parents"),
            ("2024-08-02", "Journée du génocide congolais"),
            ("2024-12-25", "Noël"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-04", "Martyrs' Day"),
            ("2024-01-16", "Laurent-Désiré Kabila Assassination"),
            ("2024-01-17", "Patrice Lumumba Assassination"),
            ("2024-04-06", "Kimbangu's Day"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-17", "Armed Forces Day"),
            ("2024-06-30", "Independence Day"),
            ("2024-08-01", "Parents' Day"),
            ("2024-08-02", "Congolese Genocide Day"),
            ("2024-12-25", "Christmas Day"),
        )
