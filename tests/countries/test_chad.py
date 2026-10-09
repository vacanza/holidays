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

from holidays.countries.chad import Chad
from tests.common import CommonCountryTests


class TestChad(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Chad)

    def test_special_holidays(self):
        self.assertHoliday("2021-04-23")

    def test_new_years_day(self):
        name = "Jour de l'An"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_international_womens_day(self):
        name = "Journée internationale de la femme"
        self.assertHolidayName(name, (f"{year}-03-08" for year in range(2019, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2019))
        obs_dts = (
            "2020-03-09",
            "2026-03-09",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_easter_monday(self):
        name = "Lundi de Pâques"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        name = "Fête du Travail"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        obs_dts = (
            "2011-05-02",
            "2016-05-02",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_independence_day(self):
        name = "Anniversaire de la Proclamation de l'Indépendance"
        self.assertHolidayName(name, (f"{year}-08-11" for year in self.full_range))
        obs_dts = (
            "2013-08-12",
            "2019-08-12",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_all_saints_day(self):
        self.assertHolidayName(
            "Fête de la Toussaint", (f"{year}-11-01" for year in self.full_range)
        )

    def test_republic_day(self):
        name = "Anniversaire de la Proclamation de la République"
        self.assertHolidayName(name, (f"{year}-11-28" for year in self.full_range))
        obs_dts = (
            "2010-11-29",
            "2021-11-29",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_freedom_and_democracy_day(self):
        name = "Journée de la Liberté et de la Démocratie"
        self.assertHolidayName(name, (f"{year}-12-01" for year in range(1991, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1991))
        obs_dts = (
            "2013-12-02",
            "2019-12-02",
        )
        self.assertHolidayName(f"{name} (observé)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_christmas_day(self):
        self.assertHolidayName("Fête de Noël", (f"{year}-12-25" for year in self.full_range))

    def test_eid_al_fitr(self):
        name = "Aïd El Fitir"
        self.assertHolidayName(
            name,
            "2018-06-15",
            "2019-06-04",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_adha(self):
        name = "Aïd El Adha"
        self.assertHolidayName(
            name,
            "2018-08-22",
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_prophets_birthday(self):
        name = "Maouloud El Nebi"
        self.assertHolidayName(
            name,
            "2018-11-21",
            "2019-11-09",
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "Jour de l'An"),
            ("2022-03-08", "Journée internationale de la femme"),
            ("2022-04-18", "Lundi de Pâques"),
            ("2022-05-01", "Fête du Travail"),
            ("2022-05-02", "Aïd El Fitir; Fête du Travail (observé)"),
            ("2022-07-09", "Aïd El Adha"),
            ("2022-08-11", "Anniversaire de la Proclamation de l'Indépendance"),
            ("2022-10-08", "Maouloud El Nebi"),
            ("2022-11-01", "Fête de la Toussaint"),
            ("2022-11-28", "Anniversaire de la Proclamation de la République"),
            ("2022-12-01", "Journée de la Liberté et de la Démocratie"),
            ("2022-12-25", "Fête de Noël"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Jour de l'An"),
            ("2024-03-08", "Journée internationale de la femme"),
            ("2024-04-01", "Lundi de Pâques"),
            ("2024-04-10", "Aïd El Fitir"),
            ("2024-05-01", "Fête du Travail"),
            ("2024-06-16", "Aïd El Adha (estimé)"),
            ("2024-08-11", "Anniversaire de la Proclamation de l'Indépendance"),
            ("2024-08-12", "Anniversaire de la Proclamation de l'Indépendance (observé)"),
            ("2024-09-15", "Maouloud El Nebi (estimé)"),
            ("2024-11-01", "Fête de la Toussaint"),
            ("2024-11-28", "Anniversaire de la Proclamation de la République"),
            ("2024-12-01", "Journée de la Liberté et de la Démocratie"),
            ("2024-12-02", "Journée de la Liberté et de la Démocratie (observé)"),
            ("2024-12-25", "Fête de Noël"),
        )

    def test_l10n_ar(self):
        self.assertLocalizedHolidays(
            "ar",
            ("2024-01-01", "رأس السنة الميلادية"),
            ("2024-03-08", "اليوم العالمي للمرأة"),
            ("2024-04-01", "إثنين الفصح"),
            ("2024-04-10", "عيد الفطر"),
            ("2024-05-01", "عيد العمال"),
            ("2024-06-16", "عيد الأضحى (تقديري)"),
            ("2024-08-11", "ذكرى إعلان الاستقلال"),
            ("2024-08-12", "ذكرى إعلان الاستقلال (يوم تعويضي)"),
            ("2024-09-15", "المولد النبوي الشريف (تقديري)"),
            ("2024-11-01", "عيد جميع القديسين"),
            ("2024-11-28", "ذكرى إعلان الجمهورية"),
            ("2024-12-01", "يوم الحرية والديمقراطية"),
            ("2024-12-02", "يوم الحرية والديمقراطية (يوم تعويضي)"),
            ("2024-12-25", "عيد الميلاد"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-08", "International Women's Day"),
            ("2024-04-01", "Easter Monday"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-05-01", "Labor Day"),
            ("2024-06-16", "Eid al-Adha (estimated)"),
            ("2024-08-11", "Independence Day"),
            ("2024-08-12", "Independence Day (observed)"),
            ("2024-09-15", "Prophet's Birthday (estimated)"),
            ("2024-11-01", "All Saints' Day"),
            ("2024-11-28", "Republic Day"),
            ("2024-12-01", "Freedom and Democracy Day"),
            ("2024-12-02", "Freedom and Democracy Day (observed)"),
            ("2024-12-25", "Christmas Day"),
        )
