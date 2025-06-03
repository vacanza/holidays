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

from holidays import OPTIONAL
from holidays.countries.niger import Niger, NE, NER
from tests.common import CommonCountryTests


class TestNiger(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1960, 2050)
        super().setUpClass(Niger, years=years, years_non_observed=years)
        cls.no_estimated_holidays = Niger(years=years, islamic_show_estimated=False)
        cls.optional_holidays = Niger(categories=OPTIONAL, years=years)
        cls.optional_holidays_non_observed = Niger(
            categories=OPTIONAL, years=years, observed=False
        )

    def test_country_aliases(self):
        self.assertAliases(Niger, NE, NER)

    def test_no_holidays(self):
        self.assertNoHolidays(Niger(years=1959))

    def test_new_years_day(self):
        name = "Jour de l'An"
        name_observed = f"{name} (observé)"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1960, 2050)))
        obs_dt = (
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(name_observed, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        self.assertNoHolidayName(name_observed, range(1960, 1998))

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
        self.assertHolidayName(name, range(1960, 2050))

    def test_concord_day(self):
        name = "Fête nationale de la Concorde"
        name_observed = f"{name} (observé)"
        self.assertHolidayName(name, (f"{year}-04-24" for year in range(1995, 2050)))
        self.assertNoHolidayName(name, range(1960, 1995))
        obs_dt = (
            "2011-04-25",
            "2016-04-25",
            "2022-04-25",
        )
        self.assertHolidayName(name_observed, obs_dt)
        self.assertNoNonObservedHolidayName(name, obs_dt)
        self.assertNoHolidayName(name_observed, range(1960, 1998))

    def test_international_labor_day(self):
        name = "Journée internationale du travail"
        name_observed = f"{name} (observé)"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1960, 2050)))
        obs_dt = (
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(name_observed, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        self.assertNoHolidayName(name_observed, range(1960, 1998))

    def test_ascension_day(self):
        name = "Ascension"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            self.optional_holidays,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, self.optional_holidays, range(1960, 2050))

    def test_whit_monday(self):
        name = "Lundi de Pentecôte"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            self.optional_holidays,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.optional_holidays, range(1960, 2050))

    def test_cnsp_coup_anniversary(self):
        name = "Anniversaire du coup d'État du CNSP"
        name_observed = f"{name} (observé)"
        self.assertHolidayName(name, (f"{year}-07-26" for year in range(2024, 2050)))
        self.assertNoHolidayName(name, range(1960, 2024))
        obs_dt = (
            "2026-07-27",
            "2037-07-27",
        )
        self.assertHolidayName(name_observed, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        self.assertNoHolidayName(name_observed, range(1960, 2024))

    def test_independence_day(self):
        name_1 = "Jour de l'indépendance"
        name_2 = "L'anniversaire de la proclamation de l'indépendance"
        name_observed = f"{name_2} (observé)"
        self.assertHolidayName(name_1, "1960-08-03")
        self.assertNoHolidayName(name_1, range(1961, 2050))
        self.assertHolidayName(name_2, (f"{year}-08-03" for year in range(1961, 2050)))
        self.assertNoHolidayName(name_2, 1960)
        obs_dt = (
            "2008-08-04",
            "2014-08-04",
            "2025-08-04",
        )
        self.assertHolidayName(name_observed, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        self.assertNoHolidayName(name_observed, range(1960, 1998))

    def test_assumption_day(self):
        name = "Assomption"
        name_observed = f"{name} (observé)"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-08-15" for year in range(1960, 2050))
        )
        obs_dt = (
            "2010-08-16",
            "2021-08-16",
        )
        self.assertHolidayName(name_observed, self.optional_holidays, obs_dt)
        self.assertNoNonObservedHoliday(self.optional_holidays_non_observed, obs_dt)
        self.assertNoHolidayName(name_observed, self.optional_holidays, range(1960, 1998))

    def test_all_saints_day(self):
        name = "Toussaint"
        name_observed = f"{name} (observé)"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name, self.optional_holidays, (f"{year}-11-01" for year in range(1960, 2050))
        )
        obs_dt = (
            "2009-11-02",
            "2015-11-02",
            "2020-11-02",
        )
        self.assertHolidayName(name_observed, self.optional_holidays, obs_dt)
        self.assertNoNonObservedHoliday(self.optional_holidays_non_observed, obs_dt)
        self.assertNoHolidayName(name_observed, self.optional_holidays, range(1960, 1998))

    def test_national_day(self):
        name = "Fête nationale"
        name_observed = f"{name} (observé)"
        self.assertHolidayName(name, (f"{year}-12-18" for year in range(1960, 2050)))
        obs_dt = (
            "2011-12-19",
            "2016-12-19",
            "2022-12-19",
        )
        self.assertHolidayName(name_observed, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        self.assertNoHolidayName(name_observed, range(1960, 1998))

    def test_christmas_day(self):
        name = "Noël"
        name_observed = f"{name} (observé)"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1960, 2050)))
        obs_dt = (
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
        )
        self.assertHolidayName(name_observed, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        self.assertNoHolidayName(name_observed, range(1960, 1998))

    def test_islamic_new_year(self):
        name = "Jour de l'An musulman"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-08-21",
            "2021-08-10",
            "2022-07-30",
            "2023-07-19",
            "2024-07-06",
            "2025-06-27",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1960, 2050))
        obs_dt = (
            "2004-02-23",
            "2011-11-28",
        )
        self.assertHolidayName(f"{name} (observé)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_prophets_birthday(self):
        name = "Mouloud"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-16",
            "2025-09-05",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1960, 2050))
        obs_dt = (
            "2004-05-03",
            "2012-02-06",
            "2019-11-11",
        )
        self.assertHolidayName(f"{name} (observé)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_laylat_al_qadr(self):
        name = "Laylat al-Qadr"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-05-20",
            "2021-05-09",
            "2022-04-28",
            "2023-04-18",
            "2024-04-06",
            "2025-03-27",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1960, 2050))
        obs_dt = (
            "2000-12-25",
            "2008-09-29",
            "2013-08-05",
            "2021-05-10",
        )
        self.assertHolidayName(f"{name} (observé)", self.no_estimated_holidays, obs_dt)

    def test_eid_al_fitr(self):
        name = "Korité"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-05-23",
            "2021-05-12",
            "2022-05-01",
            "2023-04-21",
            "2024-04-09",
            "2025-03-30",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1960, 2050))
        obs_dt = (
            "2004-11-15",
            "2012-08-20",
            "2022-05-02",
            "2025-03-31",
        )
        self.assertHolidayName(f"{name} (observé)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_eid_al_adha(self):
        name = "Tabaski"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-07-31",
            "2021-07-20",
            "2022-07-10",
            "2023-06-28",
            "2024-06-16",
            "2025-06-07",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1960, 2050))

    def test_day_after_eid_al_adha(self):
        name = "Lendemain de la Tabaski"
        self.assertHolidayName(
            name,
            self.no_estimated_holidays,
            "2020-08-01",
            "2021-07-21",
            "2022-07-11",
            "2023-06-29",
            "2024-06-17",
            "2025-06-08",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1960, 2050))
        obs_dt = (
            "2009-11-30",
            "2017-09-04",
            "2025-06-09",
        )
        self.assertHolidayName(f"{name} (observé)", self.no_estimated_holidays, obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Jour de l'An"),
            ("2025-03-27", "Laylat al-Qadr"),
            ("2025-03-30", "Korité"),
            ("2025-03-31", "Korité (observé)"),
            ("2025-04-21", "Lundi de Pâques"),
            ("2025-04-24", "Fête nationale de la Concorde"),
            ("2025-05-01", "Journée internationale du travail"),
            ("2025-05-29", "Ascension"),
            ("2025-06-07", "Tabaski"),
            ("2025-06-08", "Lendemain de la Tabaski"),
            ("2025-06-09", "Lendemain de la Tabaski (observé); Lundi de Pentecôte"),
            ("2025-06-27", "Jour de l'An musulman"),
            ("2025-07-26", "Anniversaire du coup d'État du CNSP"),
            ("2025-08-03", "L'anniversaire de la proclamation de l'indépendance"),
            ("2025-08-04", "L'anniversaire de la proclamation de l'indépendance (observé)"),
            ("2025-08-15", "Assomption"),
            ("2025-09-05", "Mouloud"),
            ("2025-11-01", "Toussaint"),
            ("2025-12-18", "Fête nationale"),
            ("2025-12-25", "Noël"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-03-27", "Laylat al-Qadr"),
            ("2025-03-30", "Eid al-Fitr"),
            ("2025-03-31", "Eid al-Fitr (observed)"),
            ("2025-04-21", "Easter Monday"),
            ("2025-04-24", "National Concord Day"),
            ("2025-05-01", "International Labor Day"),
            ("2025-05-29", "Ascension"),
            ("2025-06-07", "Eid al-Adha"),
            ("2025-06-08", "Day after Eid al-Adha"),
            ("2025-06-09", "Day after Eid al-Adha (observed); Whit Monday"),
            ("2025-06-27", "Islamic New Year"),
            ("2025-07-26", "Anniversary of the CNSP Coup"),
            ("2025-08-03", "Anniversary of the Proclamation of Independence"),
            ("2025-08-04", "Anniversary of the Proclamation of Independence (observed)"),
            ("2025-08-15", "Assumption Day"),
            ("2025-09-05", "Prophet's Birthday"),
            ("2025-11-01", "All Saints' Day"),
            ("2025-12-18", "National Day"),
            ("2025-12-25", "Christmas Day"),
        )
