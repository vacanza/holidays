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

from holidays.countries.cuba import Cuba
from tests.common import CommonCountryTests


class TestCuba(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Cuba)

    def test_liberation_day(self):
        name = "Triunfo de la Revolución"
        name_observed = f"{name} (observado)"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "1989-01-02",
            "1995-01-02",
            "2006-01-02",
        )
        self.assertHolidayName(name_observed, obs_dts)
        self.assertNoHolidayName(name_observed, range(2014, self.end_year))
        self.assertNoNonObservedHoliday(obs_dts)

    def test_victory_day(self):
        name = "Día de la Victoria"
        self.assertHolidayName(name, (f"{year}-01-02" for year in range(2008, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2008))

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
        self.assertHolidayName(name, range(2012, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2012))

    def test_christmas_day(self):
        name = "Día de Navidad"
        self.assertHolidayName(
            name,
            (
                f"{year}-12-25"
                for year in (*range(self.start_year, 1969), *range(1997, self.end_year))
            ),
        )
        self.assertNoHolidayName(name, range(1969, 1997))

    def test_new_years_eve(self):
        name = "Fiesta de Fin de Año"
        self.assertHolidayName(name, (f"{year}-12-31" for year in range(2007, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2007))

    def test_international_workers_day(self):
        name = "Día Internacional de los Trabajadores"
        self.assertHolidayName(name, (f"{year}-05-01" for year in self.full_range))
        obs_dts = (
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_assault_moncada_day(self):
        self.assertHolidayName(
            "Conmemoración del asalto a Moncada",
            (f"{year}-07-25" for year in self.full_range),
            (f"{year}-07-27" for year in self.full_range),
        )

    def test_national_rebellion_day(self):
        self.assertHolidayName(
            "Día de la Rebeldía Nacional", (f"{year}-07-26" for year in self.full_range)
        )

    def test_independence_day(self):
        name = "Inicio de las Guerras de Independencia"
        self.assertHolidayName(name, (f"{year}-10-10" for year in self.full_range))
        obs_dts = (
            "2004-10-11",
            "2010-10-11",
            "2021-10-11",
        )
        self.assertHolidayName(f"{name} (observado)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_2018(self):
        # https://www.officeholidays.com/countries/cuba/2018
        self.assertHolidayDates(
            Cuba(years=2018),
            "2018-01-01",
            "2018-01-02",
            "2018-03-30",
            "2018-05-01",
            "2018-07-25",
            "2018-07-26",
            "2018-07-27",
            "2018-10-10",
            "2018-12-25",
            "2018-12-31",
        )

    def test_2019(self):
        # https://www.officeholidays.com/countries/cuba/2019
        self.assertHolidayDates(
            Cuba(years=2019),
            "2019-01-01",
            "2019-01-02",
            "2019-04-19",
            "2019-05-01",
            "2019-07-25",
            "2019-07-26",
            "2019-07-27",
            "2019-10-10",
            "2019-12-25",
            "2019-12-31",
        )

    def test_2020(self):
        # https://www.officeholidays.com/countries/cuba/2020
        self.assertHolidayDates(
            Cuba(years=2020),
            "2020-01-01",
            "2020-01-02",
            "2020-04-10",
            "2020-05-01",
            "2020-07-25",
            "2020-07-26",
            "2020-07-27",
            "2020-10-10",
            "2020-12-25",
            "2020-12-31",
        )

    def test_2021(self):
        # https://www.officeholidays.com/countries/cuba/2021
        self.assertHolidayDates(
            Cuba(years=2021),
            "2021-01-01",
            "2021-01-02",
            "2021-04-02",
            "2021-05-01",
            "2021-07-25",
            "2021-07-26",
            "2021-07-27",
            "2021-10-10",
            "2021-10-11",
            "2021-12-25",
            "2021-12-31",
        )

    def test_2022(self):
        # https://www.officeholidays.com/countries/cuba/2022
        self.assertHolidayDates(
            Cuba(years=2022),
            "2022-01-01",
            "2022-01-02",
            "2022-04-15",
            "2022-05-01",
            "2022-05-02",
            "2022-07-25",
            "2022-07-26",
            "2022-07-27",
            "2022-10-10",
            "2022-12-25",
            "2022-12-31",
        )

    def test_2023(self):
        # https://www.officeholidays.com/countries/cuba/2023
        self.assertHolidayDates(
            Cuba(years=2023),
            "2023-01-01",
            "2023-01-02",
            "2023-04-07",
            "2023-05-01",
            "2023-07-25",
            "2023-07-26",
            "2023-07-27",
            "2023-10-10",
            "2023-12-25",
            "2023-12-31",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Triunfo de la Revolución"),
            ("2022-01-02", "Día de la Victoria"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-01", "Día Internacional de los Trabajadores"),
            ("2022-05-02", "Día Internacional de los Trabajadores (observado)"),
            ("2022-07-25", "Conmemoración del asalto a Moncada"),
            ("2022-07-26", "Día de la Rebeldía Nacional"),
            ("2022-07-27", "Conmemoración del asalto a Moncada"),
            ("2022-10-10", "Inicio de las Guerras de Independencia"),
            ("2022-12-25", "Día de Navidad"),
            ("2022-12-31", "Fiesta de Fin de Año"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "Liberation Day"),
            ("2022-01-02", "Victory Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "International Workers' Day"),
            ("2022-05-02", "International Workers' Day (observed)"),
            ("2022-07-25", "Commemoration of the Assault of the Moncada garrison"),
            ("2022-07-26", "Day of the National Rebellion"),
            ("2022-07-27", "Commemoration of the Assault of the Moncada garrison"),
            ("2022-10-10", "Independence Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-31", "New Year's Eve"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Тріумф революції"),
            ("2022-01-02", "День Перемоги"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-05-01", "Міжнародний день трудящих"),
            ("2022-05-02", "Міжнародний день трудящих (вихідний)"),
            ("2022-07-25", "Вшанування памʼяті штурму Монкади"),
            ("2022-07-26", "День національного повстання"),
            ("2022-07-27", "Вшанування памʼяті штурму Монкади"),
            ("2022-10-10", "Початок війни за незалежність"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-31", "Переддень Нового року"),
        )
