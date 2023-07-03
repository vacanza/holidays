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
#  Copyright: Kateryna Golovanova <kate@kgthreads.com>, 2022

from holidays.countries.bolivia import Bolivia, BO, BOL
from tests.common import TestCase


class TestBO(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Bolivia, years=range(2000, 2050))

    def test_country_aliases(self):
        self.assertCountryAliases(Bolivia, BO, BOL)

    def test_new_years(self):
        self.assertNoHoliday("1824-01-01")
        self.assertHolidayName("Año Nuevo", (f"{year}-01-01" for year in range(2000, 2050)))
        dt = (
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
            "2034-01-02",
        )
        self.assertHolidayName("Año Nuevo (Observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_plurinational_state_foundation_day(self):
        name = "Nacimiento del Estado Plurinacional de Bolivia"
        self.assertHoliday(f"{year}-01-22" for year in range(2010, 2050))
        self.assertNoHoliday(f"{year}-01-22" for year in range(2000, 2010))
        self.assertNoHolidayName(name, range(2000, 2010))

    def test_la_tablada(self):
        name = "La Tablada"
        t_holidays = Bolivia(subdiv="T")

        for year in range(2000, 2050):
            self.assertNoHolidayName(name, Bolivia(years=year))
            if year not in {2022, 2033, 2044}:
                self.assertNoHoliday(f"{year}-04-15")
                self.assertHolidayName(name, t_holidays, f"{year}-04-15")
            else:
                self.assertHolidayName("La Tablada", t_holidays, f"{year}-04-15")
                self.assertHolidayName("Viernes Santo", t_holidays, f"{year}-04-15")

    def test_carnival_in_oruro(self):
        name = "Carnaval de Oruro"
        self.assertNoHolidayName(name, range(2000, 2050))

        for dt in (
            "2015-02-13",
            "2016-02-05",
            "2017-02-24",
            "2018-02-09",
            "2019-03-01",
            "2020-02-21",
            "2021-02-12",
            "2022-02-25",
            "2023-02-17",
            "2024-02-09",
        ):
            self.assertNoHoliday(dt)
            self.assertHolidayName(name, Bolivia(subdiv="O"), dt)

    def test_carnival(self):
        self.assertHolidayName(
            "Feriado por Carnaval",
            "2010-02-15",
            "2010-02-16",
            "2015-02-16",
            "2015-02-17",
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
            "2024-02-12",
            "2024-02-13",
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
            "2024-03-29",
        )

    def test_labor_day(self):
        self.assertHolidayName("Día del trabajo", (f"{year}-05-01" for year in range(2000, 2050)))
        name = "Día del trabajo (Observed)"
        dt = (
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
            "2033-05-02",
        )
        self.assertHolidayName(name, dt)
        self.assertNoNonObservedHoliday(dt)

    def test_chuquisaca_day(self):
        name = "Día del departamento de Chuquisaca"
        self.assertNoHolidayName(name, range(2000, 2050))
        self.assertNoHoliday(f"{year}-05-25" for year in range(2000, 2050))
        self.assertHolidayName(
            name, Bolivia(subdiv="H"), (f"{year}-05-25" for year in range(2000, 2050))
        )

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
            "2024-05-30",
        )

    def test_andean_new_year(self):
        self.assertHoliday(f"{year}-06-21" for year in range(2010, 2050))
        self.assertNoHoliday(f"{year}-06-21" for year in range(2000, 2010))
        self.assertNoHolidayName("Año Nuevo Andino", range(2000, 2010))
        dt = (
            "2015-06-22",
            "2020-06-22",
            "2026-06-22",
            "2037-06-22",
            "2043-06-22",
        )
        self.assertHolidayName("Año Nuevo Andino (Observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_la_paz_day(self):
        name = "Día del departamento de La Paz"
        self.assertNoHolidayName(name, range(2000, 2050))
        self.assertNoHoliday(f"{year}-07-16" for year in range(2000, 2050))
        self.assertHolidayName(
            name, Bolivia(subdiv="L"), (f"{year}-07-16" for year in range(2000, 2050))
        )

    def test_independence_day(self):
        self.assertNoHoliday("1824-08-06")
        self.assertHolidayName("Día de la Patria", (f"{year}-08-06" for year in range(2000, 2050)))
        dt = (
            "2000-08-07",
            "2006-08-07",
            "2017-08-07",
            "2023-08-07",
            "2028-08-07",
        )
        self.assertHolidayName("Día de la Patria (Observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_cochabamba_day(self):
        name = "Día del departamento de Cochabamba"
        self.assertNoHolidayName(name, range(2000, 2050))
        self.assertNoHoliday(f"{year}-09-14" for year in range(2000, 2050))
        self.assertHolidayName(
            name, Bolivia(subdiv="C"), (f"{year}-09-14" for year in range(2000, 2050))
        )

    def test_santa_cruz_day(self):
        name = "Día del departamento de Santa Cruz"
        self.assertNoHolidayName(name, range(2000, 2050))
        self.assertNoHoliday(f"{year}-09-24" for year in range(2000, 2050))
        self.assertHolidayName(
            name, Bolivia(subdiv="S"), (f"{year}-09-24" for year in range(2000, 2050))
        )

    def test_pando_day(self):
        name = "Día del departamento de Pando"
        self.assertNoHolidayName(name, range(2000, 2050))
        self.assertNoHoliday(f"{year}-09-24" for year in range(2000, 2050))
        self.assertHolidayName(
            name, Bolivia(subdiv="N"), (f"{year}-09-24" for year in range(2000, 2050))
        )

    def test_all_souls_day(self):
        self.assertHolidayName("Todos Santos", (f"{year}-11-02" for year in range(2000, 2050)))
        dt = (
            "2008-11-03",
            "2014-11-03",
            "2025-11-03",
            "2031-11-03",
            "2036-11-03",
        )
        self.assertHolidayName("Todos Santos (Observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_potosi_day(self):
        name = "Día del departamento de Potosí"
        self.assertNoHolidayName(name, range(2000, 2050))
        self.assertNoHoliday(f"{year}-11-10" for year in range(2000, 2050))
        self.assertHolidayName(
            name, Bolivia(subdiv="P"), (f"{year}-11-10" for year in range(2000, 2050))
        )

    def test_beni_day(self):
        name = "Día del departamento de Beni"
        self.assertNoHolidayName(name, range(2000, 2050))
        self.assertNoHoliday(f"{year}-11-18" for year in range(2000, 2050))
        self.assertHolidayName(
            name, Bolivia(subdiv="B"), (f"{year}-11-18" for year in range(2000, 2050))
        )

    def test_christmas_day(self):
        self.assertHolidayName("Navidad", (f"{year}-12-25" for year in range(2000, 2050)))
        dt = (
            "2005-12-26",
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
            "2033-12-26",
        )
        self.assertHolidayName("Navidad (Observed)", dt)
        self.assertNoNonObservedHoliday(dt)
