#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.countries.argentina import Argentina, AR, ARG
from tests.common import TestCase


class TestArgentina(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            Argentina, years=range(1950, 2050), years_non_observed=range(1950, 2050)
        )

    def test_country_aliases(self):
        self.assertCountryAliases(Argentina, AR, ARG)

    def test_new_years_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1950, 2050))

    def test_carnival_day(self):
        name = "Día de Carnaval"
        self.assertNoHolidayName(name, 1955, range(1976, 2011))
        self.assertHolidayName(name, range(1956, 1976), range(2011, 2050))

        self.assertHoliday(
            "2016-02-08",
            "2016-02-09",
            "2017-02-27",
            "2017-02-28",
            "2018-02-12",
            "2018-02-13",
            "2019-03-04",
            "2019-03-05",
            "2020-02-24",
            "2020-02-25",
            "2021-02-15",
            "2021-02-16",
            "2022-02-28",
            "2022-03-01",
            "2023-02-20",
            "2023-02-21",
        )

    def test_memory_national_day(self):
        self.assertHoliday(f"{year}-03-24" for year in range(2006, 2050))
        self.assertNoHolidayName(
            "Día Nacional de la Memoria por la Verdad y la Justicia", range(1950, 2006)
        )

    def test_good_friday(self):
        self.assertHoliday(
            "2016-03-25",
            "2017-04-14",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )

    def test_malvinas_war_day(self):
        name_veterans = "Día del Veterano de Guerra"
        name_malvinas = "Día del Veterano y de los Caidos en la Guerra de Malvinas"

        self.assertNoHolidayName(name_veterans, 1992)
        self.assertNoHolidayName(name_malvinas, range(1950, 2001))
        self.assertHolidayName(name_veterans, range(1993, 2001))
        self.assertHolidayName(name_malvinas, range(2001, 2050))
        self.assertHoliday(f"{year}-04-02" for year in range(1993, 2020))
        self.assertHoliday("2020-03-31")
        self.assertHoliday(f"{year}-04-02" for year in range(2021, 2050))

    def test_labor_day(self):
        self.assertNoHolidayName("Día del Trabajo", Argentina(years=1929))
        self.assertHoliday(f"{year}-05-01" for year in range(1930, 2050))

    def test_may_revolution_day(self):
        self.assertNoHolidayName("Día de la Revolución de Mayo", Argentina(years=1812))
        self.assertHoliday(f"{year}-05-25" for year in range(1813, 2050))

    def test_sovereignty_over_malvinas_day(self):
        name = (
            "Día de los Derechos Argentinos sobre las Islas Malvinas, "
            "Sandwich y del Atlántico Sur"
        )

        self.assertNoHolidayName(name, 1982, range(2001, 2050))
        self.assertHoliday("1983-04-02")
        self.assertHoliday(f"{year}-06-10" for year in range(1984, 2001))
        self.assertNoHoliday(f"{year}-06-10" for year in range(2001, 2050))

    def test_guemes_day(self):
        self.assertNonObservedHoliday(f"{year}-06-17" for year in range(2016, 2050))
        self.assertNoHolidayName(
            "Paso a la Inmortalidad del General Don Martín Miguel de Güemes", range(1950, 2016)
        )
        self.assertHoliday(
            "2016-06-17",
            "2017-06-17",
            "2018-06-17",
            "2019-06-17",
            "2020-06-15",
            "2021-06-21",
            "2022-06-17",
            "2023-06-17",
        )

    def test_belgrano_day(self):
        self.assertHoliday(f"{year}-06-20" for year in range(1938, 1995))
        self.assertHoliday(f"{year}-06-20" for year in range(2011, 2050))
        self.assertHoliday(
            "2001-06-18",
            "2002-06-17",
            "2003-06-16",
            "2004-06-21",
            "2005-06-20",
            "2006-06-19",
            "2007-06-18",
            "2008-06-16",
            "2009-06-15",
            "2010-06-21",
        )

    def test_independence_day(self):
        self.assertNoHolidayName("Día de la Independencia", Argentina(years=1815))
        self.assertHoliday("1816-07-09")
        self.assertHoliday(f"{year}-07-09" for year in range(1950, 2050))

    def test_san_martin_day(self):
        self.assertNoHolidayName(
            "Paso a la Inmortalidad del General Don José de San Martin", Argentina(years=1937)
        )
        self.assertNonObservedHoliday(f"{year}-08-17" for year in range(1938, 1995))
        self.assertHoliday(
            "2011-08-22",
            "2015-08-17",
            "2016-08-15",
            "2017-08-21",
            "2018-08-20",
            "2019-08-17",
            "2020-08-17",
            "2021-08-16",
            "2022-08-15",
            "2023-08-21",
        )

    def test_cultural_day(self):
        name_raza = "Día de la Raza"
        name_cultural = "Día del Respeto a la Diversidad Cultural"

        self.assertNoHolidayName(name_raza, Argentina(years=1916))
        self.assertNoHolidayName(name_cultural, Argentina(years=(1917, 2009)))
        self.assertNoHolidayName(name_raza, range(2010, 2050))

        self.assertNonObservedHoliday("1917-10-12")
        self.assertNonObservedHoliday(f"{year}-10-12" for year in range(1950, 2050))
        self.assertHoliday(
            "2015-10-12",
            "2016-10-10",
            "2017-10-16",
            "2018-10-15",
            "2019-10-12",
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-16",
        )

    def test_national_sovereignty_day(self):
        self.assertNoHoliday(f"{year}-11-20" for year in range(1950, 2010))
        self.assertNonObservedHoliday(f"{year}-11-20" for year in range(2010, 2015))
        self.assertHoliday(
            "2015-11-27",
            "2016-11-28",
            "2017-11-20",
            "2018-11-19",
            "2019-11-18",
            "2020-11-23",
            "2021-11-22",
            "2022-11-20",
            "2023-11-20",
        )

    def test_immaculate_conception_day(self):
        self.assertHoliday(f"{year}-12-08" for year in range(1950, 2050))

    def test_christmas(self):
        self.assertHoliday(f"{year}-12-25" for year in range(1950, 2050))

    def test_2022(self):
        self.assertHolidays(
            Argentina(years=2022),
            (
                "2022-01-01",
                "Año Nuevo",
            ),
            (
                "2022-02-28",
                "Día de Carnaval",
            ),
            (
                "2022-03-01",
                "Día de Carnaval",
            ),
            (
                "2022-03-24",
                "Día Nacional de la Memoria por la Verdad y la Justicia",
            ),
            (
                "2022-04-02",
                "Día del Veterano y de los Caidos en la Guerra de Malvinas",
            ),
            (
                "2022-04-15",
                "Viernes Santo",
            ),
            (
                "2022-05-01",
                "Día del Trabajo",
            ),
            (
                "2022-05-18",
                "Censo nacional 2022",
            ),
            (
                "2022-05-25",
                "Día de la Revolución de Mayo",
            ),
            (
                "2022-06-17",
                "Paso a la Inmortalidad del General Don Martín Miguel de Güemes",
            ),
            (
                "2022-06-20",
                "Paso a la Inmortalidad del General Don Manuel Belgrano",
            ),
            (
                "2022-07-09",
                "Día de la Independencia",
            ),
            (
                "2022-08-15",
                "Paso a la Inmortalidad del General Don José de San Martin (Observado)",
            ),
            (
                "2022-10-07",
                "Feriado con fines turísticos",
            ),
            (
                "2022-10-10",
                "Día del Respeto a la Diversidad Cultural (Observado)",
            ),
            (
                "2022-11-20",
                "Día de la Soberanía Nacional",
            ),
            (
                "2022-11-21",
                "Feriado con fines turísticos",
            ),
            (
                "2022-12-08",
                "Inmaculada Concepción de María",
            ),
            (
                "2022-12-09",
                "Feriado con fines turísticos",
            ),
            (
                "2022-12-25",
                "Navidad",
            ),
        )

    def test_2023(self):
        self.assertHolidays(
            Argentina(years=2023),
            (
                "2023-01-01",
                "Año Nuevo",
            ),
            (
                "2023-02-20",
                "Día de Carnaval",
            ),
            (
                "2023-02-21",
                "Día de Carnaval",
            ),
            (
                "2023-03-24",
                "Día Nacional de la Memoria por la Verdad y la Justicia",
            ),
            (
                "2023-04-02",
                "Día del Veterano y de los Caidos en la Guerra de Malvinas",
            ),
            (
                "2023-04-07",
                "Viernes Santo",
            ),
            (
                "2023-05-01",
                "Día del Trabajo",
            ),
            (
                "2023-05-25",
                "Día de la Revolución de Mayo",
            ),
            (
                "2023-05-26",
                "Feriado con fines turísticos",
            ),
            (
                "2023-06-17",
                "Paso a la Inmortalidad del General Don Martín Miguel de Güemes",
            ),
            (
                "2023-06-19",
                "Feriado con fines turísticos",
            ),
            (
                "2023-06-20",
                "Paso a la Inmortalidad del General Don Manuel Belgrano",
            ),
            (
                "2023-07-09",
                "Día de la Independencia",
            ),
            (
                "2023-08-21",
                "Paso a la Inmortalidad del General Don José de San Martin (Observado)",
            ),
            (
                "2023-10-13",
                "Feriado con fines turísticos",
            ),
            (
                "2023-10-16",
                "Día del Respeto a la Diversidad Cultural (Observado)",
            ),
            (
                "2023-11-20",
                "Día de la Soberanía Nacional",
            ),
            (
                "2023-12-08",
                "Inmaculada Concepción de María",
            ),
            (
                "2023-12-25",
                "Navidad",
            ),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-02-28", "Día de Carnaval"),
            ("2022-03-01", "Día de Carnaval"),
            (
                "2022-03-24",
                "Día Nacional de la Memoria por la Verdad y la Justicia",
            ),
            (
                "2022-04-02",
                "Día del Veterano y de los Caidos en la Guerra de Malvinas",
            ),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-05-18", "Censo nacional 2022"),
            ("2022-05-25", "Día de la Revolución de Mayo"),
            (
                "2022-06-17",
                "Paso a la Inmortalidad del General Don Martín Miguel de Güemes",
            ),
            (
                "2022-06-20",
                "Paso a la Inmortalidad del General Don Manuel Belgrano",
            ),
            ("2022-07-09", "Día de la Independencia"),
            (
                "2022-08-15",
                "Paso a la Inmortalidad del General Don José de San Martin (Observado)",
            ),
            ("2022-10-07", "Feriado con fines turísticos"),
            (
                "2022-10-10",
                "Día del Respeto a la Diversidad Cultural (Observado)",
            ),
            ("2022-11-20", "Día de la Soberanía Nacional"),
            ("2022-11-21", "Feriado con fines turísticos"),
            ("2022-12-08", "Inmaculada Concepción de María"),
            ("2022-12-09", "Feriado con fines turísticos"),
            ("2022-12-25", "Navidad"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-02-28", "Carnival"),
            ("2022-03-01", "Carnival"),
            (
                "2022-03-24",
                "Memory's National Day for the Truth and Justice",
            ),
            (
                "2022-04-02",
                "Veterans Day and the Fallen in the Malvinas War",
            ),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-18", "National Census Day 2022"),
            ("2022-05-25", "May Revolution Day"),
            (
                "2022-06-17",
                "Pass to the Immortality of General Don Martín Miguel de Güemes",
            ),
            (
                "2022-06-20",
                "Pass to the Immortality of General Don Manuel Belgrano",
            ),
            ("2022-07-09", "Independence Day"),
            (
                "2022-08-15",
                "Pass to the Immortality of General Don José de San Martin (Observed)",
            ),
            ("2022-10-07", "Bridge Public Holiday"),
            (
                "2022-10-10",
                "Respect for Cultural Diversity Day (Observed)",
            ),
            ("2022-11-20", "National Sovereignty Day"),
            ("2022-11-21", "Bridge Public Holiday"),
            ("2022-12-08", "Immaculate Conception"),
            ("2022-12-09", "Bridge Public Holiday"),
            ("2022-12-25", "Christmas"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-02-28", "Карнавал"),
            ("2022-03-01", "Карнавал"),
            ("2022-03-24", "День памʼяті заради правди та правосуддя"),
            (
                "2022-04-02",
                "День ветеранів та загиблих на Мальвінській війні",
            ),
            ("2022-04-15", "Страсна п'ятниця"),
            ("2022-05-01", "День праці"),
            ("2022-05-18", "День національного перепису 2022"),
            ("2022-05-25", "День Травневої революції"),
            (
                "2022-06-17",
                "День пам'яті генерала Мартіна Мігеля де Гуемеса",
            ),
            ("2022-06-20", "День пам’яті генерала Мануеля Бельграно"),
            ("2022-07-09", "День незалежності"),
            (
                "2022-08-15",
                "День пам'яті генерала Хосе де Сан-Мартіна (вихідний)",
            ),
            ("2022-10-07", "Додатковий вихідний"),
            (
                "2022-10-10",
                "День поваги до культурного різноманіття (вихідний)",
            ),
            ("2022-11-20", "День національного суверенітету"),
            ("2022-11-21", "Додатковий вихідний"),
            ("2022-12-08", "Непорочне зачаття Діви Марії"),
            ("2022-12-09", "Додатковий вихідний"),
            ("2022-12-25", "Різдво Христове"),
        )
