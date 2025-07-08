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
            ("2006-01-01", "Jour de l'An"),
            ("2006-01-04", "Martyrs de l’indépendance"),
            ("2006-01-16", "Journée du Héro National Laurent Désiré KABILA"),
            ("2006-01-17", "Journée du Héro National Patrice Emery LUMUMBA"),
            ("2006-05-01", "Fête du Travail"),
            ("2006-05-17", "Jour de la Libération"),
            ("2006-06-30", "Jour de l'indépendance"),
            ("2006-08-01", "Fête des parents"),
            ("2006-12-25", "Noël"),
        )

    def test_2010(self):
        self.assertHolidays(
            DRCongo(years=2010),
            ("2010-01-01", "Jour de l'An"),
            ("2010-01-04", "Martyrs de l’indépendance"),
            ("2010-01-16", "Journée du Héro National Laurent Désiré KABILA"),
            ("2010-01-17", "Journée du Héro National Patrice Emery LUMUMBA"),
            ("2010-05-01", "Fête du Travail"),
            ("2010-05-17", "Jour de la Libération"),
            ("2010-06-30", "Jour de l'indépendance"),
            ("2010-08-01", "Fête des parents"),
            ("2010-12-25", "Noël"),
        )

    def test_2015(self):
        self.assertHolidays(
            DRCongo(years=2015),
            ("2015-01-01", "Jour de l'An"),
            ("2015-01-04", "Martyrs de l’indépendance"),
            ("2015-01-16", "Journée du Héro National Laurent Désiré KABILA"),
            ("2015-01-17", "Journée du Héro National Patrice Emery LUMUMBA"),
            ("2015-05-01", "Fête du Travail"),
            ("2015-05-17", "Jour de la Libération"),
            ("2015-06-30", "Jour de l'indépendance"),
            ("2015-08-01", "Fête des parents"),
            ("2015-12-25", "Noël"),
        )

    def test_2016(self):
        self.assertHolidays(
            DRCongo(years=2016),
            ("2016-01-01", "Jour de l'An"),
            ("2016-01-04", "Martyrs de l’indépendance"),
            ("2016-01-16", "Journée du Héro National Laurent Désiré KABILA"),
            ("2016-01-17", "Journée du Héro National Patrice Emery LUMUMBA"),
            ("2016-05-01", "Fête du Travail"),
            ("2016-05-17", "Jour de la Libération"),
            ("2016-06-30", "Jour de l'indépendance"),
            ("2016-08-01", "Fête des parents"),
            ("2016-12-25", "Noël"),
        )

    def test_2017(self):
        self.assertHolidays(
            DRCongo(years=2017),
            ("2017-01-01", "Jour de l'An"),
            ("2017-01-04", "Martyrs de l’indépendance"),
            ("2017-01-16", "Journée du Héro National Laurent Désiré KABILA"),
            ("2017-01-17", "Journée du Héro National Patrice Emery LUMUMBA"),
            ("2017-05-01", "Fête du Travail"),
            ("2017-05-17", "Jour de la Libération"),
            ("2017-06-30", "Jour de l'indépendance"),
            ("2017-08-01", "Fête des parents"),
            ("2017-12-25", "Noël"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Jour de l'An"),
            ("2024-01-04", "Martyrs de l’indépendance"),
            ("2024-01-16", "Journée du Héro National Laurent Désiré KABILA"),
            ("2024-01-17", "Journée du Héro National Patrice Emery LUMUMBA"),
            ("2024-04-06", "Journée du combat de Simon Kimbangu et de la conscience africaine"),
            ("2024-05-01", "Fête du Travail"),
            ("2024-05-17", "Journée de la Révolution et des Forces Armées"),
            ("2024-06-30", "Jour de l'indépendance"),
            ("2024-08-01", "Fête des parents"),
            ("2024-08-02", "Journée commémorative du génocide Congolais"),
            ("2024-12-25", "Noël"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-04", "Martyrs of Independence"),
            ("2024-01-16", "National Hero Laurent Désiré KABILA Day"),
            ("2024-01-17", "National Hero Patrice Emery LUMUMBA Day"),
            ("2024-04-06", "Day of the Struggle of Simon Kimbangu and African Consciousness"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-17", "Revolution and Armed Forces Day"),
            ("2024-06-30", "Independence Day"),
            ("2024-08-01", "Parents' Day"),
            ("2024-08-02", "Congolese Genocide Memorial Day"),
            ("2024-12-25", "Christmas Day"),
        )
