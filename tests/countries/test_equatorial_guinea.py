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

from holidays.countries.equatorial_guinea import EquatorialGuinea, GQ, GNQ
from tests.common import CommonCountryTests


class TestEquatorialGuinea(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2007, 2050)
        super().setUpClass(EquatorialGuinea, years=years, years_non_observed=years)

    def test_country_aliases(self):
        self.assertAliases(EquatorialGuinea, GQ, GNQ)

    def test_no_holidays(self):
        self.assertNoHolidays(EquatorialGuinea(years=2006))

    def test_new_years_day(self):
        name = "Año Nuevo"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(2007, 2050)))

        obs_dt = (
            "2011-01-03",
            "2012-01-02",
            "2017-01-02",
            "2022-01-03",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_international_womens_day(self):
        self.assertHolidayName(
            "Día Internacional de la Mujer", (f"{year}-03-08" for year in range(2007, 2050))
        )

    def test_maundy_thursday(self):
        self.assertHolidayName(
            "Jueves Santo",
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
        )

    def test_good_friday(self):
        name = "Viernes Santo"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )

        self.assertHolidayName(name, range(2007, 2050))

    def test_international_labor_day(self):
        name = "Día Internacional del Trabajo"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(2007, 2050)))

        obs_dt = (
            "2010-05-03",
            "2011-05-02",
            "2016-05-02",
            "2021-05-03",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_african_liberation_day(self):
        self.assertHolidayName(
            "Día de la liberación Africana", (f"{year}-05-25" for year in range(2007, 2050))
        )

    def test_presidents_day(self):
        name = "Natalicio de Su Excelencia el Presidente de la República"
        self.assertHolidayName(name, (f"{year}-06-05" for year in range(2007, 2050)))

        obs_dt = (
            "2010-06-07",
            "2011-06-06",
            "2016-06-06",
            "2021-06-07",
            "2022-06-06",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_corpus_christi(self):
        name = "Corpus Christi"
        self.assertHolidayName(
            name,
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
            "2025-06-19",
        )

        self.assertHolidayName(name, range(2007, 2050))

    def test_armed_forces_day(self):
        name = "Día de las Fuerzas Armadas"
        self.assertHolidayName(name, (f"{year}-08-03" for year in range(2007, 2050)))
        self.assertNoHolidayName(name, range(1969, 1979))

        obs_dt = (
            "2008-08-04",
            "2013-08-05",
            "2014-08-04",
            "2019-08-05",
            "2024-08-05",
            "2025-08-04",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_constitution_day(self):
        name = "Día de la Constitución"
        self.assertHolidayName(name, (f"{year}-08-15" for year in range(2007, 2050)))

        obs_dt = (
            "2009-08-17",
            "2010-08-16",
            "2015-08-17",
            "2020-08-17",
            "2021-08-16",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_independence_day(self):
        name = "Día de la Independencia Nacional"
        self.assertHolidayName(name, (f"{year}-10-12" for year in range(2007, 2050)))

        obs_dt = (
            "2008-10-13",
            "2013-10-14",
            "2014-10-13",
            "2019-10-14",
            "2024-10-14",
            "2025-10-13",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_immaculate_conception(self):
        name = "Festividad de la Inmaculada Concepción de María"
        self.assertHolidayName(name, (f"{year}-12-08" for year in range(2007, 2050)))

        obs_dt = (
            "2007-12-10",
            "2012-12-10",
            "2013-12-09",
            "2018-12-10",
            "2019-12-09",
            "2024-12-09",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_christmas_day(self):
        name = "Día de Navidad"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(2007, 2050)))

        obs_dt = (
            "2010-12-27",
            "2011-12-26",
            "2016-12-26",
            "2021-12-27",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_subdivision_holidays(self):
        subdiv_holidays_mapping = {
            "AN": ("2025-06-13",),
            "Akurenam": ("2025-12-04",),
            "Akonibe": ("2025-08-21",),
            "Anisok": ("2025-06-29",),
            "Ayene": ("2025-08-15",),
            "Baney": ("2025-07-25",),
            "Bata": ("2025-07-25",),
            "Bidja-Bidjan": ("2025-09-14",),
            "Bikurga": ("2025-08-15",),
            "Bitika": ("2025-10-15",),
            "Ebebiyin": ("2025-09-09",),
            "Kogo": ("2025-07-15",),
            "Luba": ("2025-04-27",),
            "Machinda": ("2025-12-30",),
            "Malabo": ("2025-11-17",),
            "Mbini": ("2025-08-22",),
            "Mikomeseng": ("2025-08-05",),
            "Mongomeyen": ("2025-12-30",),
            "Mongomo": ("2025-12-12",),
            "Niefang": ("2025-08-22",),
            "Nkimi": ("2025-07-25",),
            "Nkue": ("2025-12-03",),
            "Nsok-Nsomo": ("2025-09-09",),
            "Nsork": ("2025-06-29",),
            "Rebola": ("2025-04-27",),
        }

        for subdiv, holidays in subdiv_holidays_mapping.items():
            self.assertHoliday(EquatorialGuinea(subdiv=subdiv), holidays)

    def test_afcon_victory(self):
        name = "Victoria de la AFCON contra Costa de Marfil"
        self.assertHolidayName(name, "2024-01-23")
        self.assertNoHoliday("2023-01-23", "2025-01-23")

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Año Nuevo"),
            ("2025-03-08", "Día Internacional de la Mujer"),
            ("2025-04-17", "Jueves Santo"),
            ("2025-04-18", "Viernes Santo"),
            ("2025-04-27", "Nuestra Señora de Montserrat"),
            ("2025-05-01", "Día Internacional del Trabajo"),
            ("2025-05-25", "Día de la liberación Africana"),
            ("2025-06-05", "Natalicio de Su Excelencia el Presidente de la República"),
            ("2025-06-13", "Fiesta Patronal de Annobón"),
            ("2025-06-19", "Corpus Christi"),
            ("2025-06-29", "Santos Pablo; Santos Pedro y Pablo"),
            ("2025-07-15", "Nuestra Señora del Carmen"),
            ("2025-07-25", "Santiago Apóstol"),
            ("2025-08-03", "Día de las Fuerzas Armadas"),
            ("2025-08-04", "Día de las Fuerzas Armadas (observado)"),
            ("2025-08-05", "Virgen de Africa"),
            ("2025-08-15", "Asunción de Nuestra Señora; Día de la Constitución"),
            ("2025-08-21", "Santo Pío X"),
            ("2025-08-22", "Inmaculada Corazón de Maria; Maria Reina"),
            ("2025-09-09", "San Pedro Claver"),
            ("2025-09-14", "Exaltación de la Santa Cruz"),
            ("2025-10-12", "Día de la Independencia Nacional"),
            ("2025-10-13", "Día de la Independencia Nacional (observado)"),
            ("2025-10-15", "Santa Teresa de Jesús"),
            ("2025-11-17", "Fiesta de Santa Isabel"),
            ("2025-12-03", "San Francisco Javier"),
            ("2025-12-04", "Santa Bárbara"),
            ("2025-12-08", "Festividad de la Inmaculada Concepción de María"),
            ("2025-12-12", "Virgen de Guadalupe"),
            ("2025-12-25", "Día de Navidad"),
            ("2025-12-30", "Sagrada Familia"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-03-08", "International Women's Day"),
            ("2025-04-17", "Maundy Thursday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-27", "Our Lady of Montserrat"),
            ("2025-05-01", "International Labor Day"),
            ("2025-05-25", "African Liberation Day"),
            ("2025-06-05", "President's Day"),
            ("2025-06-13", "Patron Saint Festival of Annobón"),
            ("2025-06-19", "Corpus Christi"),
            ("2025-06-29", "Saints Paul; Saints Peter and Paul"),
            ("2025-07-15", "Our Lady of Carmen"),
            ("2025-07-25", "Santiago Apóstol"),
            ("2025-08-03", "Armed Forces Day"),
            ("2025-08-04", "Armed Forces Day (observed)"),
            ("2025-08-05", "Virgin of Africa"),
            (
                "2025-08-15",
                "Assumption of Our Lady; Constitution Day",
            ),
            ("2025-08-21", "Saint Pius X"),
            ("2025-08-22", "Immaculate Heart of Mary; Maria Reina"),
            ("2025-09-09", "Saint Peter Claver"),
            ("2025-09-14", "Exaltation of the Holy Cross"),
            ("2025-10-12", "Independence Day"),
            ("2025-10-13", "Independence Day (observed)"),
            ("2025-10-15", "Saint Teresa of Jesus"),
            ("2025-11-17", "Feast of Santa Isabel"),
            ("2025-12-03", "Saint Francis Xavier"),
            ("2025-12-04", "Saint Barbara"),
            ("2025-12-08", "Immaculate Conception"),
            ("2025-12-12", "Virgin of Guadalupe"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-30", "Holy Family"),
        )
