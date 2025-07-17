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
        super().setUpClass(DRCongo, years=range(1980, 2050))

    def test_country_aliases(self):
        self.assertAliases(DRCongo, CD, COD)

    def test_no_holidays(self):
        self.assertNoHolidays(DRCongo(years=1979))

    def test_new_years_day(self):
        self.assertHolidayName("Nouvel an", (f"{year}-01-01" for year in range(1980, 2050)))

    def test_martyrs_day(self):
        name = "Martyrs de l'indépendance"
        self.assertHolidayName(name, (f"{year}-01-04" for year in range(2015, 2050)))
        self.assertNoHolidayName(name, range(1980, 2015))

    def test_national_hero_laurent_desire_kabila_day(self):
        name = "Journée du héros national Laurent Désiré Kabila"
        self.assertHolidayName(name, (f"{year}-01-16" for year in range(2015, 2050)))
        self.assertNoHolidayName(name, range(1980, 2015))

    def test_national_hero_patrice_emery_lumumba_day(self):
        name = "Journée du héros national Patrice Emery Lumumba"
        self.assertHolidayName(name, (f"{year}-01-17" for year in range(2015, 2050)))
        self.assertNoHolidayName(name, range(1980, 2015))

    def test_day_of_the_struggle_of_simon_kimbangu_and_african_consciousness(self):
        name = "Journée du combat de Simon Kimbangu et de la conscience africaine"
        self.assertHolidayName(name, (f"{year}-04-06" for year in range(2023, 2050)))
        self.assertNoHolidayName(name, range(1980, 2023))

    def test_labor_day(self):
        self.assertHolidayName("Fête du travail", (f"{year}-05-01" for year in range(1980, 2050)))

    def test_anniversary_of_the_popular_movement_of_the_revolution(self):
        name = "Anniversaire du Mouvement populaire de la révolution"
        self.assertHolidayName(name, (f"{year}-05-20" for year in range(1980, 2015)))
        self.assertNoHolidayName(name, range(2015, 2050))

    def test_anniversary_of_the_new_revolutionary_constitution(self):
        name = "Anniversaire de la nouvelle Constitution révolutionnaire"
        self.assertHolidayName(name, (f"{year}-06-24" for year in range(1980, 2015)))
        self.assertNoHolidayName(name, range(2015, 2050))

    def test_independence_day(self):
        name = "Journée de l'indépendance"
        self.assertHolidayName(name, (f"{year}-06-30" for year in range(1980, 2050)))

    def test_parents_day(self):
        name = "Fête des parents"
        self.assertHolidayName(name, (f"{year}-08-01" for year in range(1980, 2050)))

    def test_congolese_genocide_memorial_day(self):
        name = "Journée commémorative du génocide Congolais"
        self.assertHolidayName(name, (f"{year}-08-02" for year in range(2024, 2050)))
        self.assertNoHolidayName(name, range(1980, 2024))

    def test_youth_day(self):
        name = "Journée de la Jeunesse"
        self.assertHolidayName(name, (f"{year}-10-14" for year in range(1980, 2015)))
        self.assertNoHolidayName(name, range(2015, 2050))

    def test_anniversary_of_the_new_regime(self):
        name = "Anniversaire du nouveau régime"
        self.assertHolidayName(name, (f"{year}-11-24" for year in range(1980, 2015)))
        self.assertNoHolidayName(name, range(2015, 2050))

    def test_christmas_day(self):
        name = "Noël"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1980, 2050)))

    def test_2006(self):
        self.assertHolidays(
            DRCongo(years=2006),
            ("2006-01-01", "Nouvel an"),
            ("2006-05-01", "Fête du travail"),
            ("2006-05-20", "Anniversaire du Mouvement populaire de la révolution"),
            ("2006-06-24", "Anniversaire de la nouvelle Constitution révolutionnaire"),
            ("2006-06-30", "Journée de l'indépendance"),
            ("2006-08-01", "Fête des parents"),
            ("2006-10-14", "Journée de la Jeunesse"),
            ("2006-10-27", "Anniversaire du changement du nom de notre Pays"),
            ("2006-11-17", "Fête des Forces armées zaïroises"),
            ("2006-11-24", "Anniversaire du nouveau régime"),
            ("2006-12-25", "Noël"),
        )

    def test_2010(self):
        self.assertHolidays(
            DRCongo(years=2010),
            ("2010-01-01", "Nouvel an"),
            ("2010-05-01", "Fête du travail"),
            ("2010-05-20", "Anniversaire du Mouvement populaire de la révolution"),
            ("2010-06-24", "Anniversaire de la nouvelle Constitution révolutionnaire"),
            ("2010-06-30", "Journée de l'indépendance"),
            ("2010-07-31", "Fête des parents (observé)"),
            ("2010-08-01", "Fête des parents"),
            ("2010-10-14", "Journée de la Jeunesse"),
            ("2010-10-27", "Anniversaire du changement du nom de notre Pays"),
            ("2010-11-17", "Fête des Forces armées zaïroises"),
            ("2010-11-24", "Anniversaire du nouveau régime"),
            ("2010-12-25", "Noël"),
        )

    def test_2015(self):
        self.assertHolidays(
            DRCongo(years=2015),
            ("2015-01-01", "Nouvel an"),
            ("2015-01-04", "Martyrs de l'indépendance"),
            ("2015-01-03", "Martyrs de l'indépendance (observé)"),
            ("2015-01-16", "Journée du héros national Laurent Désiré Kabila"),
            ("2015-01-17", "Journée du héros national Patrice Emery Lumumba"),
            ("2015-05-01", "Fête du travail"),
            ("2015-05-17", "Journée de la Révolution et des Forces Armées"),
            ("2015-05-16", "Journée de la Révolution et des Forces Armées (observé)"),
            ("2015-06-30", "Journée de l'indépendance"),
            ("2015-08-01", "Fête des parents"),
            ("2015-12-25", "Noël"),
        )

    def test_2016(self):
        self.assertHolidays(
            DRCongo(years=2016),
            ("2016-01-01", "Nouvel an"),
            ("2016-01-04", "Martyrs de l'indépendance"),
            (
                "2016-01-16",
                "Journée du héros national Laurent Désiré Kabila; "
                "Journée du héros national Patrice Emery Lumumba (observé)",
            ),
            ("2016-01-17", "Journée du héros national Patrice Emery Lumumba"),
            ("2016-04-30", "Fête du travail (observé)"),
            ("2016-05-01", "Fête du travail"),
            ("2016-05-17", "Journée de la Révolution et des Forces Armées"),
            ("2016-06-30", "Journée de l'indépendance"),
            ("2016-08-01", "Fête des parents"),
            ("2016-12-24", "Noël (observé)"),
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
            ("2017-05-17", "Journée de la Révolution et des Forces Armées"),
            ("2017-06-30", "Journée de l'indépendance"),
            ("2017-08-01", "Fête des parents"),
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
            ("2024-05-17", "Journée de la Révolution et des Forces Armées"),
            ("2024-06-29", "Journée de l'indépendance (observé)"),
            ("2024-06-30", "Journée de l'indépendance"),
            ("2024-08-01", "Fête des parents"),
            ("2024-08-02", "Journée commémorative du génocide Congolais"),
            ("2024-12-25", "Noël"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-01-04", "Martyrs' Day"),
            ("2024-01-16", "National Hero Laurent Désiré Kabila Day"),
            ("2024-01-17", "National Hero Patrice Emery Lumumba Day"),
            ("2024-04-06", "Day of the Struggle of Simon Kimbangu and African Consciousness"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-17", "Revolution and Armed Forces Day"),
            ("2024-06-29", "Independence Day (observed)"),
            ("2024-06-30", "Independence Day"),
            ("2024-08-01", "Parents' Day"),
            ("2024-08-02", "Congolese Genocide Memorial Day"),
            ("2024-12-25", "Christmas Day"),
        )
