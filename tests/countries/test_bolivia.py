#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.bolivia import Bolivia, BO, BOL
from tests.common import CommonCountryTests


class TestBolivia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Bolivia, years=range(1980, 2050), years_non_observed=range(2000, 2024))

    def test_country_aliases(self):
        self.assertAliases(Bolivia, BO, BOL)

    def test_no_holidays(self):
        self.assertNoHolidays(Bolivia(years=1824))

    def test_new_years(self):
        name = "Año Nuevo"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1980, 2050)))
        dt = (
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (observado)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_plurinational_state_foundation_day(self):
        name = "Día de la Creación del Estado Plurinacional de Bolivia"
        self.assertHolidayName(name, (f"{year}-01-22" for year in range(2010, 2050)))
        self.assertNoHoliday(f"{year}-01-22" for year in range(1980, 2010))
        self.assertNoHolidayName(name, range(1980, 2010))
        dt = (
            "2012-01-23",
            "2017-01-23",
            "2023-01-23",
        )
        self.assertHolidayName(f"{name} (observado)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_carnival(self):
        self.assertHolidayName(
            "Carnaval",
            "2015-02-16",
            "2015-02-17",
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

    def test_good_friday(self):
        self.assertHolidayName(
            "Viernes Santo",
            "2015-04-03",
            "2016-03-25",
            "2017-04-14",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )

    def test_labor_day(self):
        name = "Día del Trabajo"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1980, 2050)))
        dt = (
            "2005-05-02",
            "2011-05-02",
            "2012-04-30",
            "2014-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (observado)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_corpus_christi(self):
        self.assertHolidayName(
            "Corpus Christi",
            "2015-06-04",
            "2016-05-26",
            "2017-06-15",
            "2018-05-31",
            "2019-06-20",
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
        )

    def test_andean_new_year(self):
        name = "Año Nuevo Aymara Amazónico"
        self.assertHolidayName(name, (f"{year}-06-21" for year in range(2009, 2050)))
        self.assertNoHoliday(f"{year}-06-21" for year in range(1985, 2009))
        self.assertNoHolidayName(name, range(1980, 2009))
        dt = (
            "2009-06-22",
            "2015-06-22",
            "2020-06-22",
        )
        self.assertHolidayName(f"{name} (observado)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_independence_day(self):
        name = "Día de la Independencia de Bolivia"
        self.assertHolidayName(name, (f"{year}-08-06" for year in range(1980, 2050)))
        dt = (
            "2000-08-07",
            "2006-08-07",
            "2017-08-07",
            "2023-08-07",
        )
        self.assertHolidayName(f"{name} (observado)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_national_dignity_day(self):
        name = "Día de la Dignidad Nacional"
        self.assertHolidayName(name, (f"{year}-10-17" for year in range(2020, 2050)))
        self.assertNoHoliday(f"{year}-10-17" for year in range(1980, 2020))
        self.assertNoHolidayName(name, range(1980, 2020))

    def test_all_saints_day(self):
        name = "Día de Todos los Santos"
        self.assertHolidayName(name, (f"{year}-11-01" for year in range(1985, 1989)))
        self.assertNoHoliday(f"{year}-11-01" for year in range(1980, 1985))
        self.assertNoHoliday(f"{year}-11-01" for year in range(1989, 2050))
        self.assertNoHolidayName(name, range(1980, 1985), range(1989, 2050))

    def test_all_souls_day(self):
        name = "Día de Todos los Difuntos"
        self.assertHolidayName(name, (f"{year}-11-02" for year in range(1989, 2050)))
        self.assertNoHoliday(f"{year}-11-02" for year in range(1980, 1989))
        self.assertNoHolidayName(name, range(1980, 1989))
        dt = (
            "2003-11-03",
            "2008-11-03",
            "2014-11-03",
        )
        self.assertHolidayName(f"{name} (observado)", dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNoHolidayName(f"{name} (observado)", range(2016, 2050))

    def test_christmas_day(self):
        name = "Navidad"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1980, 2050)))
        dt = (
            "2005-12-26",
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (observado)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_beni_day(self):
        name = "Día del departamento de Beni"
        self.assertNoHolidayName(name, range(1980, 2050))
        self.assertNoHoliday(f"{year}-11-18" for year in range(1980, 2050))
        self.assertHolidayName(
            name, Bolivia(subdiv="B"), (f"{year}-11-18" for year in range(1980, 2050))
        )

    def test_cochabamba_day(self):
        name = "Día del departamento de Cochabamba"
        self.assertNoHolidayName(name, range(1980, 2050))
        self.assertNoHoliday(f"{year}-09-14" for year in range(1980, 2050))
        self.assertHolidayName(
            name, Bolivia(subdiv="C"), (f"{year}-09-14" for year in range(1980, 2050))
        )

    def test_chuquisaca_day(self):
        name = "Día del departamento de Chuquisaca"
        self.assertNoHolidayName(name, range(1980, 2050))
        self.assertNoHoliday(f"{year}-05-25" for year in set(range(1980, 2050)).difference({1989}))
        self.assertHolidayName(
            name, Bolivia(subdiv="H"), (f"{year}-05-25" for year in range(1980, 2050))
        )

    def test_la_paz_day(self):
        name = "Día del departamento de La Paz"
        self.assertNoHolidayName(name, range(1980, 2050))
        self.assertNoHoliday(f"{year}-07-16" for year in range(1980, 2050))
        self.assertHolidayName(
            name, Bolivia(subdiv="L"), (f"{year}-07-16" for year in range(1980, 2050))
        )

    def test_pando_day(self):
        name = "Día del departamento de Pando"
        self.assertNoHolidayName(name, range(1980, 2050))
        self.assertNoHoliday(f"{year}-10-11" for year in range(1980, 2050))
        self.assertHolidayName(
            name, Bolivia(subdiv="N"), (f"{year}-10-11" for year in range(1980, 2050))
        )

    def test_potosi_day(self):
        name = "Día del departamento de Potosí"
        self.assertNoHolidayName(name, range(1980, 2050))
        self.assertNoHoliday(f"{year}-11-10" for year in range(1980, 2050))
        self.assertHolidayName(
            name, Bolivia(subdiv="P"), (f"{year}-11-10" for year in range(1980, 2050))
        )

    def test_carnival_in_oruro(self):
        name = "Carnaval de Oruro"
        self.assertNoHolidayName(name, range(1980, 2050))
        dt = (
            "2015-02-13",
            "2016-02-05",
            "2017-02-24",
            "2018-02-09",
            "2019-03-01",
            "2020-02-21",
            "2021-02-12",
            "2022-02-25",
            "2023-02-17",
        )
        self.assertNoHoliday(dt)
        self.assertHolidayName(name, Bolivia(subdiv="O"), dt)

    def test_santa_cruz_day(self):
        name = "Día del departamento de Santa Cruz"
        self.assertNoHolidayName(name, range(1980, 2050))
        self.assertNoHoliday(f"{year}-09-24" for year in range(1980, 2050))
        self.assertHolidayName(
            name, Bolivia(subdiv="S"), (f"{year}-09-24" for year in range(1980, 2050))
        )

    def test_la_tablada(self):
        name = "La Tablada"
        self.assertNoHolidayName(name, range(1980, 2050))
        self.assertNoHoliday(
            f"{year}-04-15" for year in set(range(1980, 2050)).difference({2022, 2033, 2044})
        )
        self.assertHolidayName(
            name, Bolivia(subdiv="T"), (f"{year}-04-15" for year in range(1980, 2050))
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Año Nuevo"),
            ("2023-01-02", "Año Nuevo (observado)"),
            ("2023-01-22", "Día de la Creación del Estado Plurinacional de Bolivia"),
            ("2023-01-23", "Día de la Creación del Estado Plurinacional de Bolivia (observado)"),
            ("2023-02-20", "Carnaval"),
            ("2023-02-21", "Carnaval"),
            ("2023-04-07", "Viernes Santo"),
            ("2023-05-01", "Día del Trabajo"),
            ("2023-06-08", "Corpus Christi"),
            ("2023-06-21", "Año Nuevo Aymara Amazónico"),
            ("2023-08-06", "Día de la Independencia de Bolivia"),
            ("2023-08-07", "Día de la Independencia de Bolivia (observado)"),
            ("2023-10-17", "Día de la Dignidad Nacional"),
            ("2023-11-02", "Día de Todos los Difuntos"),
            ("2023-12-25", "Navidad"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "New Year's Day (observed)"),
            ("2023-01-22", "Plurinational State Foundation Day"),
            ("2023-01-23", "Plurinational State Foundation Day (observed)"),
            ("2023-02-20", "Carnival"),
            ("2023-02-21", "Carnival"),
            ("2023-04-07", "Good Friday"),
            ("2023-05-01", "Labor Day"),
            ("2023-06-08", "Corpus Christi"),
            ("2023-06-21", "Aymara New Year"),
            ("2023-08-06", "Independence Day"),
            ("2023-08-07", "Independence Day (observed)"),
            ("2023-10-17", "National Dignity Day"),
            ("2023-11-02", "All Souls' Day"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2023-01-01", "Новий рік"),
            ("2023-01-02", "Новий рік (вихідний)"),
            ("2023-01-22", "День створення Багатонаціональної Держави Болівія"),
            ("2023-01-23", "День створення Багатонаціональної Держави Болівія (вихідний)"),
            ("2023-02-20", "Карнавал"),
            ("2023-02-21", "Карнавал"),
            ("2023-04-07", "Страсна пʼятниця"),
            ("2023-05-01", "День праці"),
            ("2023-06-08", "Свято Тіла і Крові Христових"),
            ("2023-06-21", "Новий рік Аймара"),
            ("2023-08-06", "День незалежності Болівії"),
            ("2023-08-07", "День незалежності Болівії (вихідний)"),
            ("2023-10-17", "День національної гідності"),
            ("2023-11-02", "День усіх померлих"),
            ("2023-12-25", "Різдво Христове"),
        )
