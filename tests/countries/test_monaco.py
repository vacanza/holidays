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

from holidays.countries.monaco import Monaco
from tests.common import CommonCountryTests


class TestMonaco(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Monaco)

    def test_special_holidays(self):
        self.assertHoliday("2015-01-07")

    def test_new_years_day(self):
        name = "Le jour de l'An"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (reporté)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_saint_devotes_day(self):
        self.assertHolidayName(
            "Le jour de la Sainte-Dévote", (f"{year}-01-27" for year in self.full_range)
        )

    def test_easter_monday(self):
        name = "Le Lundi de Pâques"
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
        name = "Le jour de la Fête du Travail"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        obs_dts = (
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (reporté)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_ascension_day(self):
        name = "Le jour de l'Ascension"
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

    def test_pentecost_monday(self):
        name = "Le Lundi de Pentecôte"
        self.assertHolidayName(
            name,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.full_range)

    def test_corpus_christi(self):
        name = "Le jour de la Fête Dieu"
        self.assertHolidayName(
            name,
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
            "2025-06-19",
        )
        self.assertHolidayName(name, self.full_range)

    def test_assumption_day(self):
        name = "Le jour de l'Assomption"
        self.assertHolidayName(name, (f"{year}-08-15" for year in self.full_range))
        obs_dts = (
            "2004-08-16",
            "2010-08-16",
            "2021-08-16",
        )
        self.assertHolidayName(f"{name} (reporté)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_all_saints_day(self):
        name = "Le jour de la Toussaint"
        self.assertHolidayName(name, (f"{year}-11-01" for year in self.full_range))
        obs_dts = (
            "2009-11-02",
            "2015-11-02",
            "2020-11-02",
        )
        self.assertHolidayName(f"{name} (reporté)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_princes_day(self):
        name = "Le jour de la Fête de S.A.S. le Prince Souverain"
        self.assertHolidayName(name, (f"{year}-11-19" for year in self.full_range))
        obs_dts = (
            "2006-11-20",
            "2017-11-20",
            "2023-11-20",
        )
        self.assertHolidayName(f"{name} (reporté)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_immaculate_conception(self):
        name = "Le jour de l'Immaculée Conception"
        name_observed = f"{name} (reporté)"
        self.assertHolidayName(name, (f"{year}-12-08" for year in self.full_range))
        obs_dts = (
            "2019-12-09",
            "2024-12-09",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)
        self.assertNoHolidayName(name_observed, range(self.start_year, 2019))

    def test_christmas_day(self):
        name = "Le jour de Noël"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2005-12-26",
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (reporté)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_2023(self):
        self.assertHolidaysInYear(
            2023,
            ("2023-01-01", "Le jour de l'An"),
            ("2023-01-02", "Le jour de l'An (reporté)"),
            ("2023-01-27", "Le jour de la Sainte-Dévote"),
            ("2023-04-10", "Le Lundi de Pâques"),
            ("2023-05-01", "Le jour de la Fête du Travail"),
            ("2023-05-18", "Le jour de l'Ascension"),
            ("2023-05-29", "Le Lundi de Pentecôte"),
            ("2023-06-08", "Le jour de la Fête Dieu"),
            ("2023-08-15", "Le jour de l'Assomption"),
            ("2023-11-01", "Le jour de la Toussaint"),
            ("2023-11-19", "Le jour de la Fête de S.A.S. le Prince Souverain"),
            ("2023-11-20", "Le jour de la Fête de S.A.S. le Prince Souverain (reporté)"),
            ("2023-12-08", "Le jour de l'Immaculée Conception"),
            ("2023-12-25", "Le jour de Noël"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Le jour de l'An"),
            ("2022-01-27", "Le jour de la Sainte-Dévote"),
            ("2022-04-18", "Le Lundi de Pâques"),
            ("2022-05-01", "Le jour de la Fête du Travail"),
            ("2022-05-02", "Le jour de la Fête du Travail (reporté)"),
            ("2022-05-26", "Le jour de l'Ascension"),
            ("2022-06-06", "Le Lundi de Pentecôte"),
            ("2022-06-16", "Le jour de la Fête Dieu"),
            ("2022-08-15", "Le jour de l'Assomption"),
            ("2022-11-01", "Le jour de la Toussaint"),
            ("2022-11-19", "Le jour de la Fête de S.A.S. le Prince Souverain"),
            ("2022-12-08", "Le jour de l'Immaculée Conception"),
            ("2022-12-25", "Le jour de Noël"),
            ("2022-12-26", "Le jour de Noël (reporté)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-27", "Saint Devote's Day"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Labor Day (observed)"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-06", "Pentecost Monday"),
            ("2022-06-16", "Corpus Christi"),
            ("2022-08-15", "Assumption Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-19", "Prince's Day"),
            ("2022-12-08", "Immaculate Conception"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-27", "День Святої Девоти"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-02", "День праці (вихідний)"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-06", "Другий день Пʼятидесятниці"),
            ("2022-06-16", "Свято Тіла і Крові Христових"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-19", "День Князя"),
            ("2022-12-08", "Непорочне зачаття Діви Марії"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Різдво Христове (вихідний)"),
        )
