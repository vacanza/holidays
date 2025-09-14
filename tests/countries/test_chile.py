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

from holidays.countries.chile import Chile, CL, CHL
from tests.common import CommonCountryTests


class TestChile(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Chile)

    def test_country_aliases(self):
        self.assertAliases(Chile, CL, CHL)

    def test_special_holidays(self):
        self.assertHoliday(
            "1999-12-31",
            "2002-04-24",
            "2004-09-17",
            "2010-09-17",
            "2010-09-20",
            "2017-04-19",
            "2022-09-16",
        )

    def test_no_holidays(self):
        self.assertNoHolidays(
            Chile(categories=Chile.supported_categories, years=self.start_year - 1)
        )

    def test_new_years_day(self):
        name_jan_2 = "Feriado nacional"
        self.assertHolidayName("Año Nuevo", (f"{year}-01-01" for year in self.full_range))
        self.assertHolidayName(
            name_jan_2,
            "2017-01-02",
            "2023-01-02",
        )
        self.assertNoHolidayName(
            name_jan_2, (f"{year}-01-02" for year in range(self.start_year, 2017))
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
        self.assertHolidayName(name, self.full_range)

    def test_holy_saturday(self):
        name = "Sábado Santo"
        self.assertHolidayName(
            name,
            "2020-04-11",
            "2021-04-03",
            "2022-04-16",
            "2023-04-08",
            "2024-03-30",
            "2025-04-19",
        )
        self.assertHolidayName(name, self.full_range)

    def test_ascension(self):
        name = "Ascensión del Señor"
        self.assertHolidayName(
            name,
            "1915-05-13",
            "1930-05-29",
            "1950-05-18",
            "1967-05-04",
        )
        self.assertHolidayName(name, range(self.start_year, 1968))
        self.assertNoHolidayName(name, range(1968, self.end_year))

    def test_corpus_christi(self):
        name = "Corpus Christi"
        self.assertHolidayName(
            name,
            "1915-06-03",
            "1940-05-23",
            "1950-06-08",
            "1967-05-25",
            "1987-06-18",
            "1998-06-11",
            "2000-06-19",
            "2006-06-12",
        )
        self.assertHolidayName(name, range(self.start_year, 1968), range(1987, 2007))
        self.assertNoHolidayName(name, range(1968, 1987), range(2007, self.end_year))

    def test_labor_day(self):
        name = "Día Nacional del Trabajo"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1932, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1932))

    def test_naval_glories_day(self):
        self.assertHolidayName(
            "Día de las Glorias Navales", (f"{year}-05-21" for year in self.full_range)
        )

    def test_indigenous_peoples_day(self):
        name = "Día Nacional de los Pueblos Indígenas"
        self.assertHolidayName(
            name,
            "2021-06-21",
            "2022-06-21",
            "2023-06-21",
            "2024-06-20",
            "2025-06-20",
            "2026-06-21",
            "2027-06-21",
            "2028-06-20",
            "2029-06-20",
            "2030-06-21",
            "2031-06-21",
            "2032-06-20",
            "2033-06-20",
            "2034-06-21",
            "2035-06-21",
            "2036-06-20",
            "2037-06-20",
            "2038-06-21",
            "2039-06-21",
            "2040-06-20",
            "2041-06-20",
            "2042-06-21",
            "2043-06-21",
            "2044-06-20",
            "2045-06-20",
            "2046-06-21",
            "2047-06-21",
            "2048-06-20",
            "2049-06-20",
        )
        self.assertNoHolidayName(name, range(self.start_year, 2021))

    def test_saint_peter_and_paul(self):
        name = "San Pedro y San Pablo"
        self.assertNonObservedHolidayName(
            name,
            (
                f"{year}-06-29"
                for year in (*range(self.start_year, 1968), *range(1986, self.end_year))
            ),
        )
        self.assertHolidayName(
            name,
            "2000-06-26",
            "2001-07-02",
            "2002-06-29",
            "2003-06-29",
            "2004-06-28",
            "2005-06-27",
            "2006-06-26",
            "2007-07-02",
            "2008-06-29",
            "2009-06-29",
            "2010-06-28",
            "2011-06-27",
            "2012-07-02",
            "2013-06-29",
            "2014-06-29",
            "2015-06-29",
            "2016-06-27",
            "2017-06-26",
            "2018-07-02",
            "2019-06-29",
            "2020-06-29",
            "2021-06-28",
            "2022-06-27",
            "2023-06-26",
            "2024-06-29",
        )
        self.assertNoHolidayName(name, range(1968, 1986))

    def test_virgin_of_carmen(self):
        name = "Virgen del Carmen"
        self.assertHolidayName(name, (f"{year}-07-16" for year in range(2007, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2007))

    def test_assumption_of_mary(self):
        self.assertHolidayName(
            "Asunción de la Virgen", (f"{year}-08-15" for year in self.full_range)
        )

    def test_day_of_national_liberation(self):
        name = "Día de la Liberación Nacional"
        self.assertHolidayName(name, (f"{year}-09-11" for year in range(1981, 1999)))
        self.assertNoHolidayName(name, range(self.start_year, 1981), range(1999, self.end_year))

    def test_day_of_national_unity(self):
        name = "Día de la Unidad Nacional"
        self.assertHolidayName(
            name,
            "1999-09-06",
            "2000-09-04",
            "2001-09-03",
        )
        self.assertNoHolidayName(name, range(self.start_year, 1999), range(2002, self.end_year))

    def test_national_holidays(self):
        name = "Fiestas Patrias"
        self.assertHolidayName(
            name,
            "2007-09-17",
            "2012-09-17",
            "2013-09-20",
            "2018-09-17",
            "2019-09-20",
            "2021-09-17",
            "2024-09-20",
        )
        self.assertHolidayName(name, (f"{year}-09-20" for year in range(1932, 1945)))
        self.assertNoHolidayName(name, range(self.start_year, 1932), range(1945, 2007))

    def test_independence_day(self):
        self.assertHolidayName(
            "Día de la Independencia", (f"{year}-09-18" for year in self.full_range)
        )

    def test_army_day(self):
        self.assertHolidayName(
            "Día de las Glorias del Ejército", (f"{year}-09-19" for year in self.full_range)
        )

    def test_columbus_day(self):
        name_1922 = "Día de la Raza"
        name_2000 = "Día del Encuentro de dos Mundos"
        self.assertHolidayName(
            name_1922, (f"{year}-10-12" for year in (*range(1922, 1973), *range(1974, 2000)))
        )
        self.assertNoHolidayName(name_1922, 1973, range(2000, self.end_year))

        self.assertHolidayName(
            name_2000,
            "2000-10-09",
            "2005-10-10",
            "2010-10-11",
            "2015-10-12",
            "2019-10-12",
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-09",
        )
        self.assertHolidayName(name_2000, range(2000, self.end_year))

    def test_national_day_of_evangelical_and_protestant_churches(self):
        name = "Día Nacional de las Iglesias Evangélicas y Protestantes"
        self.assertHolidayName(
            name,
            "2008-10-31",
            "2009-10-31",
            "2010-10-31",
            "2011-10-31",
            "2012-11-02",
            "2013-10-31",
            "2014-10-31",
            "2015-10-31",
            "2016-10-31",
            "2017-10-27",
            "2018-11-02",
            "2019-10-31",
            "2020-10-31",
            "2021-10-31",
            "2022-10-31",
            "2023-10-27",
        )
        self.assertNoHolidayName(name, range(self.start_year, 2008))

    def test_all_saints_day(self):
        self.assertHoliday(f"{year}-11-01" for year in self.full_range)

    def test_immaculate_conception(self):
        self.assertHoliday(f"{year}-12-08" for year in self.full_range)

    def test_christmas_eve(self):
        name = "Víspera de Navidad"
        self.assertHolidayName(name, (f"{year}-12-24" for year in range(1944, 1989)))
        self.assertNoHolidayName(name, range(self.start_year, 1944), range(1989, self.end_year))

    def test_christmas_day(self):
        self.assertHolidayName("Navidad", (f"{year}-12-25" for year in self.full_range))

    def test_bank_holidays(self):
        name = "Feriado bancario"
        self.assertBankHolidayName(name, (f"{year}-06-30" for year in range(1957, 1976)))
        self.assertBankHolidayName(
            name, (f"{year}-12-31" for year in (*range(1956, 1997), *range(1998, 2025)))
        )
        self.assertNoBankHolidayName(
            name, range(self.start_year, 1956), 1997, range(2025, self.end_year)
        )
        self.assertNoHolidayName(name)

    def test_2019(self):
        self.assertHolidayDates(
            Chile(years=2019),
            "2019-01-01",
            "2019-04-19",
            "2019-04-20",
            "2019-05-01",
            "2019-05-21",
            "2019-06-29",
            "2019-07-16",
            "2019-08-15",
            "2019-09-18",
            "2019-09-19",
            "2019-09-20",
            "2019-10-12",
            "2019-10-31",
            "2019-11-01",
            "2019-12-08",
            "2019-12-25",
        )

    def test_2020(self):
        # from https://feriados.cl/2020.htm
        self.assertHolidayDates(
            Chile(years=2020),
            "2020-01-01",
            "2020-04-10",
            "2020-04-11",
            "2020-05-01",
            "2020-05-21",
            "2020-06-29",
            "2020-07-16",
            "2020-08-15",
            "2020-09-18",
            "2020-09-19",
            "2020-10-12",
            "2020-10-31",
            "2020-11-01",
            "2020-12-08",
            "2020-12-25",
        )

    def test_2021(self):
        # from https://feriados.cl/2021.htm
        self.assertHolidayDates(
            Chile(years=2021),
            "2021-01-01",
            "2021-04-02",
            "2021-04-03",
            "2021-05-01",
            "2021-05-21",
            "2021-06-21",
            "2021-06-28",
            "2021-07-16",
            "2021-08-15",
            "2021-09-17",
            "2021-09-18",
            "2021-09-19",
            "2021-10-11",
            "2021-10-31",
            "2021-11-01",
            "2021-12-08",
            "2021-12-25",
        )

    def test_provinces(self):
        self.assertSubdivApHoliday(
            "2020-06-07",
            "2021-06-07",
        )
        self.assertNoSubdivApHoliday("2012-06-07")
        self.assertSubdivNbHoliday(
            "2020-08-20",
            "2021-08-20",
        )
        self.assertNoSubdivNbHoliday("2013-08-20")

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-04-16", "Sábado Santo"),
            ("2022-05-01", "Día Nacional del Trabajo"),
            ("2022-05-21", "Día de las Glorias Navales"),
            ("2022-06-07", "Asalto y Toma del Morro de Arica"),
            ("2022-06-21", "Día Nacional de los Pueblos Indígenas"),
            ("2022-06-27", "San Pedro y San Pablo"),
            ("2022-07-16", "Virgen del Carmen"),
            ("2022-08-15", "Asunción de la Virgen"),
            ("2022-08-20", "Nacimiento del Prócer de la Independencia (Chillán y Chillán Viejo)"),
            ("2022-09-16", "Feriado nacional"),
            ("2022-09-18", "Día de la Independencia"),
            ("2022-09-19", "Día de las Glorias del Ejército"),
            ("2022-10-10", "Día del Encuentro de dos Mundos"),
            ("2022-10-31", "Día Nacional de las Iglesias Evangélicas y Protestantes"),
            ("2022-11-01", "Día de Todos los Santos"),
            ("2022-12-08", "La Inmaculada Concepción"),
            ("2022-12-25", "Navidad"),
            ("2022-12-31", "Feriado bancario"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-16", "Holy Saturday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-21", "Navy Day"),
            ("2022-06-07", "Assault and Capture of Cape Arica"),
            ("2022-06-21", "National Day of Indigenous Peoples"),
            ("2022-06-27", "Saint Peter and Saint Paul's Day"),
            ("2022-07-16", "Our Lady of Mount Carmel"),
            ("2022-08-15", "Assumption Day"),
            ("2022-08-20", "Nativity of Bernardo O'Higgins (Chillán and Chillán Viejo communes)"),
            ("2022-09-16", "National Holiday"),
            ("2022-09-18", "Independence Day"),
            ("2022-09-19", "Army Day"),
            ("2022-10-10", "Meeting of Two Worlds' Day"),
            ("2022-10-31", "Reformation Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-08", "Immaculate Conception"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-31", "Bank Holiday"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-16", "Велика субота"),
            ("2022-05-01", "День праці"),
            ("2022-05-21", "День військово-морської слави"),
            ("2022-06-07", "Штурм і захоплення Морро-де-Аріка"),
            ("2022-06-21", "Національний день корінних народів"),
            ("2022-06-27", "День Святих Петра і Павла"),
            ("2022-07-16", "Матір Божа Кармельська"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-08-20", "Річниця Бернардо ОʼГіґґінса (свято комун Чіллан і Чіллан Вʼєхо)"),
            ("2022-09-16", "Національне свято"),
            ("2022-09-18", "День незалежності"),
            ("2022-09-19", "День військової слави"),
            ("2022-10-10", "День зустрічі двох світів"),
            ("2022-10-31", "День Реформації"),
            ("2022-11-01", "День усіх святих"),
            ("2022-12-08", "Непорочне зачаття Діви Марії"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-31", "Банківський вихідний"),
        )
