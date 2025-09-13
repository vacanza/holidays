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

from holidays.constants import OPTIONAL
from holidays.countries.costa_rica import CostaRica, CR, CRI
from tests.common import CommonCountryTests


class TestCostaRica(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full_range = range(1980, 2050)
        super().setUpClass(CostaRica)

    def test_country_aliases(self):
        self.assertAliases(CostaRica, CR, CRI)

    def test_new_year_day(self):
        self.assertHolidayName("Año Nuevo", (f"{year}-01-01" for year in self.full_range))

    def test_maundy_thursday(self):
        name = "Jueves Santo"
        self.assertHolidayName(
            name,
            "2016-03-24",
            "2017-04-13",
            "2018-03-29",
            "2019-04-18",
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
        )
        self.assertHolidayName(name, self.full_range)

    def test_good_friday(self):
        name = "Viernes Santo"
        self.assertHolidayName(
            name,
            "2016-03-25",
            "2017-04-14",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )
        self.assertHolidayName(name, self.full_range)

    def test_juan_santamaria_day(self):
        name = "Día de Juan Santamaría"
        years_observed = {2006, 2007, 2008, 2023, 2024}
        self.assertHolidayName(
            name, (f"{year}-04-11" for year in self.full_range if year not in years_observed)
        )

        dt = (
            "2006-04-17",
            "2007-04-16",
            "2008-04-14",
            "2023-04-10",
            "2024-04-15",
        )
        self.assertHolidayName(f"{name} (observado)", dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNonObservedHolidayName(name, (f"{year}-04-11" for year in years_observed))

    def test_labor_day(self):
        name = "Día Internacional del Trabajo"
        years_observed = {2021}
        self.assertHolidayName(
            name, (f"{year}-05-01" for year in self.full_range if year not in years_observed)
        )

        dt = "2021-05-03"
        self.assertHolidayName(f"{name} (observado)", dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNonObservedHolidayName(name, "2021-05-01")

    def test_annexation(self):
        name = "Anexión del Partido de Nicoya a Costa Rica"
        years_observed = {2006, 2007, 2008, 2020, 2021, 2023, 2024}
        self.assertHolidayName(
            name, (f"{year}-07-25" for year in self.full_range if year not in years_observed)
        )

        dt = (
            "2006-07-31",
            "2007-07-30",
            "2008-07-28",
            "2020-07-27",
            "2021-07-26",
            "2023-07-24",
            "2024-07-29",
        )
        self.assertHolidayName(f"{name} (observado)", dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNonObservedHolidayName(name, (f"{year}-07-25" for year in years_observed))

    def test_feast_our_lady_of_angels(self):
        name = "Fiesta de Nuestra Señora de los Ángeles"
        self.assertOptionalHolidayName(name, (f"{year}-08-02" for year in self.full_range))
        self.assertNoHolidayName(name)

    def test_mothers_day(self):
        name = "Día de la Madre"
        years_observed = {2006, 2007, 2020, 2023, 2024}
        self.assertHolidayName(
            name, (f"{year}-08-15" for year in self.full_range if year not in years_observed)
        )

        dt = (
            "2006-08-21",
            "2007-08-20",
            "2020-08-17",
            "2023-08-14",
            "2024-08-19",
        )
        self.assertHolidayName(f"{name} (observado)", dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNonObservedHolidayName(name, (f"{year}-08-15" for year in years_observed))

    def test_black_person_day(self):
        name = "Día de la Persona Negra y la Cultura Afrocostarricense"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(name, (f"{year}-08-31" for year in range(2024, 2050)))
        self.assertNoOptionalHoliday(f"{year}-08-31" for year in range(1980, 2021))
        self.assertNoOptionalHolidayName(name, range(1980, 2021))

        dt = (
            "2021-09-05",
            "2022-09-04",
            "2023-09-03",
        )
        self.assertOptionalHolidayName(f"{name} (observado)", dt)
        self.assertNoOptionalNonObservedHoliday(dt)
        self.assertOptionalNonObservedHolidayName(
            name,
            "2021-08-31",
            "2022-08-31",
            "2023-08-31",
        )

    def test_independence_day(self):
        name = "Día de la Independencia"
        years_observed = {2020, 2021, 2022}
        self.assertHolidayName(
            name, (f"{year}-09-15" for year in self.full_range if year not in years_observed)
        )

        dt = (
            "2020-09-14",
            "2021-09-13",
            "2022-09-19",
        )
        self.assertHolidayName(f"{name} (observado)", dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNonObservedHolidayName(name, (f"{year}-09-15" for year in years_observed))

    def test_cultures_day(self):
        name = "Día de las Culturas"
        self.assertHolidayName(
            name,
            "2008-10-12",
            "2009-10-12",
            "2013-10-12",
            "2014-10-12",
            "2015-10-12",
            "2019-10-12",
        )
        self.assertNoHolidayName(name, range(2020, 2050))

        dt = (
            "2010-10-18",
            "2011-10-17",
            "2012-10-15",
            "2016-10-17",
            "2017-10-16",
            "2018-10-15",
        )
        self.assertHolidayName(f"{name} (observado)", dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNonObservedHolidayName(
            name,
            "2010-10-12",
            "2011-10-12",
            "2012-10-12",
            "2016-10-12",
            "2017-10-12",
            "2018-10-12",
        )

    def test_army_abolition_day(self):
        name = "Día de la Abolición del Ejército"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(name, (f"{year}-12-01" for year in range(2023, 2050)))
        self.assertNoOptionalHoliday("2019-12-01")
        self.assertNoOptionalHolidayName(name, range(1980, 2020))

        dt = (
            "2020-11-30",
            "2021-11-29",
            "2022-12-05",
        )
        self.assertOptionalHolidayName(f"{name} (observado)", dt)
        self.assertNoOptionalNonObservedHoliday(dt)
        self.assertOptionalNonObservedHolidayName(
            name,
            "2020-12-01",
            "2021-12-01",
            "2022-12-01",
        )

    def test_christmas_day(self):
        self.assertHolidayName("Navidad", (f"{year}-12-25" for year in self.full_range))

    def test_2022(self):
        self.assertHolidays(
            CostaRica(years=2022),
            ("2022-01-01", "Año Nuevo"),
            ("2022-04-11", "Día de Juan Santamaría"),
            ("2022-04-14", "Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-01", "Día Internacional del Trabajo"),
            ("2022-07-25", "Anexión del Partido de Nicoya a Costa Rica"),
            ("2022-08-15", "Día de la Madre"),
            ("2022-09-19", "Día de la Independencia (observado)"),
            ("2022-12-25", "Navidad"),
        )

        self.assertNonObservedHolidays(
            CostaRica(years=2022, observed=False),
            ("2022-01-01", "Año Nuevo"),
            ("2022-04-11", "Día de Juan Santamaría"),
            ("2022-04-14", "Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-01", "Día Internacional del Trabajo"),
            ("2022-07-25", "Anexión del Partido de Nicoya a Costa Rica"),
            ("2022-08-15", "Día de la Madre"),
            ("2022-09-15", "Día de la Independencia"),
            ("2022-12-25", "Navidad"),
        )

    def test_optional_2022(self):
        self.assertHolidays(
            CostaRica(categories=OPTIONAL, years=2022),
            ("2022-08-02", "Fiesta de Nuestra Señora de los Ángeles"),
            ("2022-09-04", "Día de la Persona Negra y la Cultura Afrocostarricense (observado)"),
            ("2022-12-05", "Día de la Abolición del Ejército (observado)"),
        )

    def test_2023(self):
        self.assertHolidays(
            CostaRica(years=2023),
            ("2023-01-01", "Año Nuevo"),
            ("2023-04-06", "Jueves Santo"),
            ("2023-04-07", "Viernes Santo"),
            ("2023-04-10", "Día de Juan Santamaría (observado)"),
            ("2023-05-01", "Día Internacional del Trabajo"),
            ("2023-07-24", "Anexión del Partido de Nicoya a Costa Rica (observado)"),
            ("2023-08-14", "Día de la Madre (observado)"),
            ("2023-09-15", "Día de la Independencia"),
            ("2023-12-25", "Navidad"),
        )

    def test_optional_2023(self):
        self.assertHolidays(
            CostaRica(categories=OPTIONAL, years=2023),
            ("2023-08-02", "Fiesta de Nuestra Señora de los Ángeles"),
            ("2023-09-03", "Día de la Persona Negra y la Cultura Afrocostarricense (observado)"),
            ("2023-12-01", "Día de la Abolición del Ejército"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-04-11", "Día de Juan Santamaría"),
            ("2022-04-14", "Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-01", "Día Internacional del Trabajo"),
            ("2022-07-25", "Anexión del Partido de Nicoya a Costa Rica"),
            ("2022-08-02", "Fiesta de Nuestra Señora de los Ángeles"),
            ("2022-08-15", "Día de la Madre"),
            ("2022-09-04", "Día de la Persona Negra y la Cultura Afrocostarricense (observado)"),
            ("2022-09-19", "Día de la Independencia (observado)"),
            ("2022-12-05", "Día de la Abolición del Ejército (observado)"),
            ("2022-12-25", "Navidad"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-11", "Juan Santamaría Day"),
            ("2022-04-14", "Maundy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "International Labor Day"),
            ("2022-07-25", "Annexation of the Party of Nicoya to Costa Rica"),
            ("2022-08-02", "Feast of Our Lady of the Angels"),
            ("2022-08-15", "Mother's Day"),
            ("2022-09-04", "Day of the Black Person and Afro-Costa Rican Culture (observed)"),
            ("2022-09-19", "Independence Day (observed)"),
            ("2022-12-05", "Army Abolition Day (observed)"),
            ("2022-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-11", "День Хуана Сантамарії"),
            ("2022-04-14", "Великий четвер"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-05-01", "Міжнародний день праці"),
            ("2022-07-25", "День приєднання Нікої"),
            ("2022-08-02", "Свято Богоматері Ангелів"),
            ("2022-08-15", "День матері"),
            ("2022-09-04", "День чорношкірої людини та афро-костариканської культури (вихідний)"),
            ("2022-09-19", "День незалежності (вихідний)"),
            ("2022-12-05", "День ліквідації армії (вихідний)"),
            ("2022-12-25", "Різдво Христове"),
        )
