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

from holidays.countries.dr_congo import DRCongo, CD, COD
from tests.common import CommonCountryTests


class TestDRCongo(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1980, 2050)
        super().setUpClass(DRCongo, years=years, years_non_observed=years)

    def test_country_aliases(self):
        self.assertAliases(DRCongo, CD, COD)

    def test_no_holidays(self):
        self.assertNoHolidays(DRCongo(years=1979))

    def test_new_years_day(self):
        name = "Nouvel an"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1980, 2050)))

        obs_dt = (
            "2005-12-31",
            "2011-12-31",
            "2016-12-31",
            "2022-12-31",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_martyrs_day(self):
        name = "Martyrs de l'indépendance"
        self.assertHolidayName(name, (f"{year}-01-04" for year in range(2015, 2050)))
        self.assertNoHolidayName(name, range(1980, 2015))

        obs_dt = ("2015-01-03",)
        self.assertHolidayName(f"{name} (observé)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_national_hero_laurent_desire_kabila_day(self):
        name = "Journée du héros national Laurent Désiré Kabila"
        self.assertHolidayName(name, (f"{year}-01-16" for year in range(2015, 2050)))
        self.assertNoHolidayName(name, range(1980, 2015))

        obs_dt = ("2022-01-15",)
        self.assertHolidayName(f"{name} (observé)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_national_hero_patrice_emery_lumumba_day(self):
        name = "Journée du héros national Patrice Emery Lumumba"
        self.assertHolidayName(name, (f"{year}-01-17" for year in range(2015, 2050)))
        self.assertNoHolidayName(name, range(1980, 2015))

        obs_dt = (
            "2016-01-16",
            "2021-01-16",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dt)

    def test_day_of_the_struggle_of_simon_kimbangu_and_african_consciousness(self):
        name = "Journée du combat de Simon Kimbangu et de la conscience africaine"
        self.assertHolidayName(name, (f"{year}-04-06" for year in range(2023, 2050)))
        self.assertNoHolidayName(name, range(1980, 2023))

        obs_dt = ("2025-04-05",)
        self.assertHolidayName(f"{name} (observé)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_armed_forces_day(self):
        name_1 = "Fête des Forces armées zaïroises"
        self.assertHolidayName(name_1, (f"{year}-11-17" for year in range(1980, 2014)))
        self.assertNoHolidayName(name_1, range(2014, 2050))

        obs_dt = (
            "2002-11-16",
            "2013-11-16",
        )
        self.assertHolidayName(f"{name_1} (observé)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

        name_2 = "Journée de la Révolution et des Forces Armées"
        self.assertHolidayName(name_2, (f"{year}-05-17" for year in range(2014, 2050)))
        self.assertNoHolidayName(name_2, range(1980, 2014))

        obs_dt = (
            "2015-05-16",
            "2020-05-16",
        )
        self.assertHolidayName(f"{name_2} (observé)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_labor_day(self):
        name = "Fête du travail"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1980, 2050)))

        obs_dt = (
            "2005-04-30",
            "2011-04-30",
            "2016-04-30",
            "2022-04-30",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_anniversary_of_the_popular_movement_of_the_revolution(self):
        name = "Anniversaire du Mouvement populaire de la révolution"
        self.assertHolidayName(name, (f"{year}-05-20" for year in range(1980, 2014)))
        self.assertNoHolidayName(name, range(2014, 2050))

        obs_dt = (
            "2001-05-19",
            "2007-05-19",
            "2012-05-19",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_anniversary_of_the_new_revolutionary_constitution(self):
        name = "Anniversaire de la nouvelle Constitution révolutionnaire"
        self.assertHolidayName(name, (f"{year}-06-24" for year in range(1980, 2014)))
        self.assertNoHolidayName(name, range(2014, 2050))

        obs_dt = (
            "2001-06-23",
            "2007-06-23",
            "2012-06-23",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_independence_day(self):
        name = "Journée de l'indépendance"
        self.assertHolidayName(name, (f"{year}-06-30" for year in range(1980, 2050)))

        obs_dt = (
            "2002-06-29",
            "2013-06-29",
            "2019-06-29",
            "2024-06-29",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_parents_day(self):
        name = "Fête des parents"
        self.assertHolidayName(name, (f"{year}-08-01" for year in range(1980, 2050)))

        obs_dt = (
            "2004-07-31",
            "2010-07-31",
            "2021-07-31",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_congolese_genocide_memorial_day(self):
        name = "Journée commémorative du génocide Congolais"
        self.assertHolidayName(name, (f"{year}-08-02" for year in range(2024, 2050)))
        self.assertNoHolidayName(name, range(1980, 2024))

        obs_dt = ("2026-08-01",)
        self.assertHolidayName(f"{name} (observé)", obs_dt)

    def test_youth_day(self):
        name = "Journée de la Jeunesse"
        self.assertHolidayName(name, (f"{year}-10-14" for year in range(1980, 2014)))
        self.assertNoHolidayName(name, range(2014, 2050))

        obs_dt = (
            "2001-10-13",
            "2007-10-13",
            "2012-10-13",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_anniversary_of_the_new_regime(self):
        name = "Anniversaire du nouveau régime"
        self.assertHolidayName(name, (f"{year}-11-24" for year in range(1980, 2014)))
        self.assertNoHolidayName(name, range(2014, 2050))

        obs_dt = (
            "2002-11-23",
            "2013-11-23",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_christmas_day(self):
        name = "Noël"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1980, 2050)))

        obs_dt = (
            "2005-12-24",
            "2011-12-24",
            "2016-12-24",
            "2022-12-24",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

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
