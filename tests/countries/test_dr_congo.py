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

from holidays.countries.dr_congo import (
    DRCongo,
    CD,
    COD,
)
from tests.common import CommonCountryTests


class TestDRCongo(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(DRCongo, years=range(1960, 2050))

    def test_country_aliases(self):
        self.assertAliases(DRCongo, CD, COD)

    def test_no_holidays(self):
        self.assertNoHolidays(DRCongo(years=1959))

    def test_2006(self):
        self.assertHolidays(
            DRCongo(years=2006),
            ("2006-01-01", "Nouvel an"),
            ("2006-05-01", "Fête du travail"),
            ("2006-05-20", "Anniversaire du Mouvement populaire de la révolution"),
            (
                "2006-06-24",
                "Anniversaire de la nouvelle Constitution révolutionnaire; "
                "Du Zaïre monnaie; Journée du Poisson",
            ),
            ("2006-06-30", "Journée de l’indépendance"),
            ("2006-08-01", "Fête des parents"),
            ("2006-10-14", "Journée de la Jeunesse"),
            ("2006-10-27", "Anniversaire du changement du nom de notre Pays"),
            ("2006-11-17", "Jour de la Libération"),
            ("2006-11-24", "Anniversaire du nouveau régime"),
            ("2006-12-25", "Noël"),
        )

    def test_2010(self):
        self.assertHolidays(
            DRCongo(years=2010),
            ("2010-01-01", "Nouvel an"),
            ("2010-05-01", "Fête du travail"),
            ("2010-05-20", "Anniversaire du Mouvement populaire de la révolution"),
            (
                "2010-06-24",
                "Anniversaire de la nouvelle Constitution révolutionnaire; "
                "Du Zaïre monnaie; Journée du Poisson",
            ),
            ("2010-06-30", "Journée de l’indépendance"),
            ("2010-08-01", "Fête des parents"),
            ("2010-10-14", "Journée de la Jeunesse"),
            ("2010-10-27", "Anniversaire du changement du nom de notre Pays"),
            ("2010-11-17", "Jour de la Libération"),
            ("2010-11-24", "Anniversaire du nouveau régime"),
            ("2010-12-25", "Noël"),
        )

    def test_2015(self):
        self.assertHolidays(
            DRCongo(years=2015),
            ("2015-01-01", "Nouvel an"),
            ("2015-01-04", "Martyrs de l'indépendance"),
            ("2015-01-16", "Journée du héros national Laurent Désiré Kabila"),
            ("2015-01-17", "Journée du héros national Patrice Emery Lumumba"),
            ("2015-05-01", "Fête du travail"),
            ("2015-05-20", "Anniversaire du Mouvement populaire de la révolution"),
            (
                "2015-06-24",
                "Anniversaire de la nouvelle Constitution révolutionnaire; "
                "Du Zaïre monnaie; Journée du Poisson",
            ),
            ("2015-06-30", "Journée de l’indépendance"),
            ("2015-08-01", "Fête des parents"),
            ("2015-10-14", "Journée de la Jeunesse"),
            ("2015-10-27", "Anniversaire du changement du nom de notre Pays"),
            ("2015-11-17", "Jour de la Libération"),
            ("2015-11-24", "Anniversaire du nouveau régime"),
            ("2015-12-25", "Noël"),
        )

    def test_2016(self):
        self.assertHolidays(
            DRCongo(years=2016),
            ("2016-01-01", "Nouvel an"),
            ("2016-01-04", "Martyrs de l'indépendance"),
            ("2016-01-16", "Journée du héros national Laurent Désiré Kabila"),
            ("2016-01-17", "Journée du héros national Patrice Emery Lumumba"),
            ("2016-05-01", "Fête du travail"),
            ("2016-05-20", "Anniversaire du Mouvement populaire de la révolution"),
            (
                "2016-06-24",
                "Anniversaire de la nouvelle Constitution révolutionnaire; "
                "Du Zaïre monnaie; Journée du Poisson",
            ),
            ("2016-06-30", "Journée de l’indépendance"),
            ("2016-08-01", "Fête des parents"),
            ("2016-10-14", "Journée de la Jeunesse"),
            ("2016-10-27", "Anniversaire du changement du nom de notre Pays"),
            ("2016-11-17", "Jour de la Libération"),
            ("2016-11-24", "Anniversaire du nouveau régime"),
            ("2016-12-25", "Noël"),
        )

    def test_2017(self):
        self.assertHolidays(
            DRCongo(years=2017),
            ("2017-01-01", "Nouvel an"),
            ("2017-01-04", "Martyrs de l'indépendance"),
            ("2017-01-16", "Journée du héros national Laurent Désiré Kabila"),
            ("2017-01-17", "Journée du héros national Patrice Emery Lumumba"),
            ("2017-05-01", "Fête du travail"),
            ("2017-05-20", "Anniversaire du Mouvement populaire de la révolution"),
            (
                "2017-06-24",
                "Anniversaire de la nouvelle Constitution révolutionnaire; "
                "Du Zaïre monnaie; Journée du Poisson",
            ),
            ("2017-06-30", "Journée de l’indépendance"),
            ("2017-08-01", "Fête des parents"),
            ("2017-10-14", "Journée de la Jeunesse"),
            ("2017-10-27", "Anniversaire du changement du nom de notre Pays"),
            ("2017-11-17", "Jour de la Libération"),
            ("2017-11-24", "Anniversaire du nouveau régime"),
            ("2017-12-25", "Noël"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Nouvel an"),
            ("2024-01-04", "Martyrs de l'indépendance"),
            ("2024-01-16", "Journée du héros national Laurent Désiré Kabila"),
            ("2024-01-17", "Journée du héros national Patrice Emery Lumumba"),
            ("2024-04-06", "Journée du combat de Simon Kimbangu et de la conscience africaine"),
            ("2024-05-01", "Fête du travail"),
            ("2024-05-20", "Anniversaire du Mouvement populaire de la révolution"),
            (
                "2024-06-24",
                "Anniversaire de la nouvelle Constitution révolutionnaire; "
                "Du Zaïre monnaie; Journée du Poisson",
            ),
            ("2024-06-30", "Journée de l’indépendance"),
            ("2024-08-01", "Fête des parents"),
            ("2024-08-02", "Journée commémorative du génocide Congolais"),
            ("2024-10-14", "Journée de la Jeunesse"),
            ("2024-10-27", "Anniversaire du changement du nom de notre Pays"),
            ("2024-11-17", "Journée des Forces armées"),
            ("2024-11-24", "Anniversaire du nouveau régime"),
            ("2024-12-25", "Noël"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-04", "Martyrs of Independence"),
            ("2024-01-16", "National Hero Laurent Désiré Kabila Day"),
            ("2024-01-17", "National Hero Patrice Emery Lumumba Day"),
            ("2024-04-06", "Day of the Struggle of Simon Kimbangu and African Consciousness"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-20", "Anniversary of the Popular Movement of the Revolution"),
            (
                "2024-06-24",
                "Anniversary of the New Revolutionary Constitution; Currency zaire; Fish Day",
            ),
            ("2024-06-30", "Independence Day"),
            ("2024-08-01", "Parents' Day"),
            ("2024-08-02", "Congolese Genocide Memorial Day"),
            ("2024-10-14", "Youth Day"),
            ("2024-10-27", "Anniversary of the Country's Name Change"),
            ("2024-11-17", "Armed Forces Day"),
            ("2024-11-24", "Anniversary of the New Regime"),
            ("2024-12-25", "Christmas Day"),
        )
