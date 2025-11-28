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

from holidays.countries.burundi import Burundi
from tests.common import CommonCountryTests


class TestBurundi(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Burundi)

    def test_new_year_day(self):
        name = "Jour de l'an"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_unity_day(self):
        name = "Fête de l'Unité"
        self.assertHolidayName(name, (f"{year}-02-05" for year in range(1992, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1992))
        obs_dts = (
            "2012-02-06",
            "2017-02-06",
            "2023-02-06",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_commemoration_of_the_assassination_of_president_cyprien_ntaryamira(self):
        name = "Commémoration de l'Assassinat du Président Cyprien Ntaryamira"
        self.assertHolidayName(name, (f"{year}-04-06" for year in range(1995, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1995))
        obs_dts = (
            "2008-04-07",
            "2014-04-07",
            "2025-04-07",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_international_labor_day(self):
        name = "Fête Internationale du Travail"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        obs_dts = (
            "2011-05-02",
            "2016-05-02",
            "2033-05-02",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_ascension_day(self):
        name = "Jour de l'Ascension"
        self.assertHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, self.full_range)

    def test_commemoration_of_the_death_of_president_pierre_nkurunziza(self):
        name = (
            "Journée Nationale du Patriotisme et Commémoration de la Mort "
            "du Président Pierre Nkurunziza"
        )
        self.assertHolidayName(name, (f"{year}-06-08" for year in range(2022, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2022))
        obs_dts = (
            "2025-06-09",
            "2031-06-09",
            "2036-06-09",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_independence_day(self):
        name = "Anniversaire de l'Indépendance"
        self.assertHolidayName(name, (f"{year}-07-01" for year in self.full_range))
        obs_dts = (
            "2012-07-02",
            "2018-07-02",
            "2029-07-02",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_assumption_day(self):
        name = "Assomption"
        self.assertHolidayName(name, (f"{year}-08-15" for year in self.full_range))
        obs_dts = (
            "2010-08-16",
            "2021-08-16",
            "2027-08-16",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_commemoration_of_the_assassination_of_national_hero_prince_louis_rwagasore(self):
        name = "Commémoration de l'Assassinat du Héros National, le Prince Louis Rwagasore"
        self.assertHolidayName(name, (f"{year}-10-13" for year in self.full_range))
        obs_dts = (
            "2013-10-14",
            "2019-10-14",
            "2024-10-14",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_commemoration_of_the_assassination_of_president_melchior_ndadaye(self):
        name = "Commémoration de l'Assassinat du Président Melchior Ndadaye"
        self.assertHolidayName(name, (f"{year}-10-21" for year in range(1994, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1994))
        obs_dts = (
            "2012-10-22",
            "2018-10-22",
            "2029-10-22",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_all_saints_day(self):
        name = "Toussaint"
        self.assertHolidayName(name, (f"{year}-11-01" for year in self.full_range))
        obs_dts = (
            "2015-11-02",
            "2020-11-02",
            "2026-11-02",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_christmas_day(self):
        name = "Noël"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2016-12-26",
            "2022-12-26",
            "2033-12-26",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_eid_al_fitr(self):
        name = "Aid-El-Fithr"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2020-05-25",
            "2025-03-31",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_eid_al_adha(self):
        name = "Aid-El-Adha"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)
        obs_dts = (
            "2019-08-12",
            "2024-06-17",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_2024(self):
        self.assertHolidaysInYear(
            2024,
            ("2024-01-01", "Jour de l'an"),
            ("2024-02-05", "Fête de l'Unité"),
            ("2024-04-06", "Commémoration de l'Assassinat du Président Cyprien Ntaryamira"),
            ("2024-04-10", "Aid-El-Fithr"),
            ("2024-05-01", "Fête Internationale du Travail"),
            ("2024-05-09", "Jour de l'Ascension"),
            (
                "2024-06-08",
                (
                    "Journée Nationale du Patriotisme et Commémoration de la Mort "
                    "du Président Pierre Nkurunziza"
                ),
            ),
            ("2024-06-16", "Aid-El-Adha"),
            ("2024-06-17", "Aid-El-Adha (observé)"),
            ("2024-07-01", "Anniversaire de l'Indépendance"),
            ("2024-08-15", "Assomption"),
            (
                "2024-10-13",
                "Commémoration de l'Assassinat du Héros National, le Prince Louis Rwagasore",
            ),
            (
                "2024-10-14",
                (
                    "Commémoration de l'Assassinat du Héros National, "
                    "le Prince Louis Rwagasore (observé)"
                ),
            ),
            ("2024-10-21", "Commémoration de l'Assassinat du Président Melchior Ndadaye"),
            ("2024-11-01", "Toussaint"),
            ("2024-12-25", "Noël"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Jour de l'an"),
            ("2025-02-05", "Fête de l'Unité"),
            ("2025-03-30", "Aid-El-Fithr"),
            ("2025-03-31", "Aid-El-Fithr (observé)"),
            ("2025-04-06", "Commémoration de l'Assassinat du Président Cyprien Ntaryamira"),
            (
                "2025-04-07",
                "Commémoration de l'Assassinat du Président Cyprien Ntaryamira (observé)",
            ),
            ("2025-05-01", "Fête Internationale du Travail"),
            ("2025-05-29", "Jour de l'Ascension"),
            ("2025-06-06", "Aid-El-Adha"),
            (
                "2025-06-08",
                (
                    "Journée Nationale du Patriotisme et Commémoration de la Mort "
                    "du Président Pierre Nkurunziza"
                ),
            ),
            (
                "2025-06-09",
                (
                    "Journée Nationale du Patriotisme et Commémoration de la Mort "
                    "du Président Pierre Nkurunziza (observé)"
                ),
            ),
            ("2025-07-01", "Anniversaire de l'Indépendance"),
            ("2025-08-15", "Assomption"),
            (
                "2025-10-13",
                "Commémoration de l'Assassinat du Héros National, le Prince Louis Rwagasore",
            ),
            ("2025-10-21", "Commémoration de l'Assassinat du Président Melchior Ndadaye"),
            ("2025-11-01", "Toussaint"),
            ("2025-12-25", "Noël"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-02-05", "Unity Day"),
            ("2025-03-30", "Eid al-Fitr"),
            ("2025-03-31", "Eid al-Fitr (observed)"),
            ("2025-04-06", "Commemoration of the Assassination of President Cyprien Ntaryamira"),
            (
                "2025-04-07",
                "Commemoration of the Assassination of President Cyprien Ntaryamira (observed)",
            ),
            ("2025-05-01", "International Labor Day"),
            ("2025-05-29", "Ascension Day"),
            ("2025-06-06", "Eid al-Adha"),
            (
                "2025-06-08",
                (
                    "National Day of Patriotism and Commemoration of the Death of "
                    "President Pierre Nkurunziza"
                ),
            ),
            (
                "2025-06-09",
                (
                    "National Day of Patriotism and Commemoration of the Death of "
                    "President Pierre Nkurunziza (observed)"
                ),
            ),
            ("2025-07-01", "Independence Day"),
            ("2025-08-15", "Assumption Day"),
            (
                "2025-10-13",
                "Commemoration of the Assassination of National Hero, Prince Louis Rwagasore",
            ),
            ("2025-10-21", "Commemoration of the Assassination of President Melchior Ndadaye"),
            ("2025-11-01", "All Saints' Day"),
            ("2025-12-25", "Christmas Day"),
        )
