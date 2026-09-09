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

from holidays.countries.burkina_faso import BurkinaFaso
from tests.common import CommonCountryTests


class TestBurkinaFaso(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BurkinaFaso)

    def test_new_years_day(self):
        name = "New Year's Day"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_revolution_day(self):
        name = "Revolution Day"
        self.assertHolidayName(name, (f"{year}-01-03" for year in range(1967, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1967))
        obs_dts = (
            "2010-01-04",
            "2016-01-04",
            "2021-01-04",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_international_womens_day(self):
        name = "International Women's Day"
        self.assertHolidayName(name, (f"{year}-03-08" for year in self.full_range))
        obs_dts = (
            "2015-03-09",
            "2020-03-09",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_labor_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        obs_dts = (
            "2011-05-02",
            "2016-05-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_independence_day(self):
        name = "Independence Day"
        self.assertHolidayName(name, (f"{year}-08-05" for year in self.full_range))
        obs_dts = (
            "2012-08-06",
            "2018-08-06",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_assumption_day(self):
        name = "Assumption Day"
        self.assertHolidayName(name, (f"{year}-08-15" for year in self.full_range))
        obs_dts = (
            "2010-08-16",
            "2021-08-16",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_martyrs_day(self):
        name = "Martyrs' Day"
        name_observed = f"{name} (observed)"
        self.assertHolidayName(name, (f"{year}-10-31" for year in range(2016, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2016))
        obs_dts = ("2021-11-01",)
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoNonObservedHolidayName(name_observed, obs_dts)

    def test_all_saints_day(self):
        name = "All Saints' Day"
        self.assertHolidayName(name, (f"{year}-11-01" for year in self.full_range))
        obs_dts = (
            "2015-11-02",
            "2020-11-02",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_proclamation_of_independence_day(self):
        name = "Proclamation of Independence Day"
        self.assertHolidayName(name, (f"{year}-12-11" for year in self.full_range))
        obs_dts = (
            "2011-12-12",
            "2022-12-12",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in self.full_range))
        obs_dts = (
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (observed)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_eid_al_fitr(self):
        name = "Eid al-Fitr"
        self.assertHolidayName(
            name,
            "2014-07-29",
            "2015-07-18",
            "2016-07-07",
            "2017-06-26",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_adha(self):
        name = "Eid al-Adha"
        self.assertHolidayName(
            name,
            "2014-10-05",
            "2015-09-24",
            "2016-09-13",
            "2017-09-02",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_prophets_birthday(self):
        name = "Mawlid"
        self.assertHolidayName(
            name,
            "2014-01-14",
            "2015-01-03",
            "2015-12-24",
            "2016-12-12",
            "2017-12-01",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "Revolution Day"),
            ("2022-03-08", "International Women's Day"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Eid al-Fitr; Labour Day (observed)"),
            ("2022-05-26", "Ascension Day"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-08-05", "Independence Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-10-09", "Mawlid"),
            ("2022-10-31", "Martyrs' Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-11", "Proclamation of Independence Day"),
            ("2022-12-12", "Proclamation of Independence Day (observed)"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "Revolution Day"),
            ("2022-03-08", "International Women's Day"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Eid al-Fitr; Labor Day (observed)"),
            ("2022-05-26", "Ascension Day"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-08-05", "Independence Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-10-09", "Prophet's Birthday"),
            ("2022-10-31", "Martyrs' Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-11", "Proclamation of Independence Day"),
            ("2022-12-12", "Proclamation of Independence Day (observed)"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2022-01-01", "Jour de l'An"),
            ("2022-01-03", "Soulèvement populaire"),
            ("2022-03-08", "Journée internationale de la femme"),
            ("2022-04-18", "Lundi de Pâques"),
            ("2022-05-01", "Fête du travail"),
            ("2022-05-02", "Fête du travail (observé); Jour de Ramadan"),
            ("2022-05-26", "Ascension"),
            ("2022-07-09", "Jour de Tabaski"),
            ("2022-08-05", "Fête nationale"),
            ("2022-08-15", "Assomption"),
            ("2022-10-09", "Mouloud"),
            ("2022-10-31", "Journée nationale des martyrs"),
            ("2022-11-01", "Toussaint"),
            ("2022-12-11", "Proclamation de l'Indépendance"),
            ("2022-12-12", "Proclamation de l'Indépendance (observé)"),
            ("2022-12-25", "Jour de Noël"),
            ("2022-12-26", "Jour de Noël (observé)"),
        )
