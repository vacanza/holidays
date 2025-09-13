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

from holidays.constants import ARMENIAN, BANK, GOVERNMENT, HEBREW, ISLAMIC
from holidays.countries.argentina import Argentina, AR, ARG
from tests.common import CommonCountryTests


class TestArgentina(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            Argentina,
            years_armenian=range(2007, 2050),
            years_bank=range(1975, 2050),
            years_government=range(2014, 2050),
            years_hebrew=range(1996, 2050),
            years_islamic=range(1997, 2050),
        )

    def test_country_aliases(self):
        self.assertAliases(Argentina, AR, ARG)

    def test_no_holidays(self):
        self.assertNoHolidays(Argentina(categories=ARMENIAN, years=2006))
        self.assertNoHolidays(Argentina(categories=BANK, years=1974))
        self.assertNoHolidays(Argentina(categories=GOVERNMENT, years=2013))
        self.assertNoHolidays(Argentina(categories=HEBREW, years=1995))
        self.assertNoHolidays(Argentina(categories=ISLAMIC, years=1996))
        self.assertNoHolidays(Argentina(years=AR.start_year - 1))

    def test_special_holidays(self):
        self.assertHoliday(
            "2010-05-24",
            "2010-10-27",
            "2011-03-25",
            "2011-12-09",
            "2012-02-27",
            "2012-04-30",
            "2012-09-24",
            "2012-12-24",
            "2013-01-31",
            "2013-02-20",
            "2013-04-01",
            "2013-06-21",
            "2014-05-02",
            "2014-12-26",
            "2015-03-23",
            "2015-12-07",
            "2016-07-08",
            "2016-12-09",
            "2018-04-30",
            "2018-12-24",
            "2018-12-31",
            "2019-07-08",
            "2019-08-19",
            "2019-10-14",
            "2020-03-23",
            "2020-07-10",
            "2020-12-07",
            "2021-05-24",
            "2021-10-08",
            "2021-11-22",
            "2022-05-18",
            "2022-10-07",
            "2022-11-21",
            "2022-12-09",
            "2022-12-20",
            "2023-05-26",
            "2023-06-19",
            "2023-10-13",
            "2024-04-01",
            "2024-06-21",
            "2024-10-11",
            "2025-05-02",
            "2025-08-15",
            "2025-11-21",
        )

    def test_special_bank_holidays(self):
        self.assertBankHoliday(
            "2019-12-24",
            "2019-12-31",
            "2020-12-24",
            "2020-12-31",
            "2021-12-24",
            "2021-12-31",
            "2024-12-24",
            "2024-12-31",
        )

    def test_special_subdiv_holidays(self):
        # Buenos Aires.
        self.assertSubdivBHoliday("2018-11-30")

    def test_new_years_day(self):
        self.assertHolidayName("Año Nuevo", (f"{year}-01-01" for year in self.full_range))

    def test_epiphany_day(self):
        name = "Día de Reyes"
        self.assertHolidayName(name, (f"{year}-01-06" for year in range(AR.start_year, 1977)))
        self.assertNoHolidayName(name, range(1977, 2050))

    def test_carnival_monday(self):
        name = "Lunes de Carnaval"
        self.assertHolidayName(
            name,
            "2011-03-07",
            "2016-02-08",
            "2017-02-27",
            "2018-02-12",
            "2019-03-04",
            "2020-02-24",
            "2021-02-15",
            "2022-02-28",
            "2023-02-20",
            "2024-02-12",
            "2025-03-03",
        )
        self.assertHolidayName(name, range(AR.start_year, 1977), range(2011, 2050))
        self.assertNoHolidayName(name, range(1977, 2011))

    def test_carnival_tuesday(self):
        name = "Martes de Carnaval"
        self.assertHolidayName(
            name,
            "2011-03-08",
            "2016-02-09",
            "2017-02-28",
            "2018-02-13",
            "2019-03-05",
            "2020-02-25",
            "2021-02-16",
            "2022-03-01",
            "2023-02-21",
            "2024-02-13",
            "2025-03-04",
        )
        self.assertHolidayName(name, range(AR.start_year, 1977), range(2011, 2050))
        self.assertNoHolidayName(name, range(1977, 2011))

    def test_national_day_of_remembrance(self):
        name = "Día Nacional de la Memoria por la Verdad y la Justicia"
        self.assertHolidayName(name, (f"{year}-03-24" for year in range(2006, 2050)))
        self.assertNoHolidayName(name, range(AR.start_year, 2006))

    def test_malvinas_war_day(self):
        name_1 = "Día del Veterano de Guerra"
        name_2 = "Día del Veterano y de los Caidos en la Guerra de Malvinas"
        self.assertHolidayName(
            name_1,
            "1993-04-05",
            "1994-04-02",
            "1995-04-02",
            "1996-04-01",
            "1997-03-31",
            "1998-04-06",
            "1999-04-05",
            "2000-04-02",
        )
        self.assertHolidayName(
            name_2,
            "2001-04-02",
            "2002-04-01",
            "2003-03-31",
            "2004-04-05",
            "2005-04-02",
            "2006-04-02",
            "2020-03-31",
        )
        self.assertHolidayName(
            name_2, (f"{year}-04-02" for year in (*range(2007, 2020), *range(2021, 2050)))
        )
        self.assertNoHolidayName(name_1, range(AR.start_year, 1993), range(2001, 2050))
        self.assertNoHolidayName(name_2, range(AR.start_year, 2001))

    def test_maundy_thursday(self):
        name = "Jueves Santo"
        self.assertHolidayName(
            name,
            "1976-04-15",
            "2011-04-21",
            "2012-04-05",
            "2013-03-28",
            "2014-04-17",
            "2015-04-02",
            "2016-03-24",
            "2017-04-13",
            "2018-03-29",
            "2019-04-18",
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
        )
        self.assertHolidayName(name, range(AR.start_year, 1977), range(2011, 2050))
        self.assertNoHolidayName(name, range(1977, 2011))

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
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(1977, 2050))
        self.assertNoHolidayName(name, range(AR.start_year, 1977))

    def test_labor_day(self):
        self.assertHolidayName("Día del Trabajo", (f"{year}-05-01" for year in self.full_range))

    def test_may_revolution_day(self):
        self.assertHolidayName(
            "Día de la Revolución de Mayo", (f"{year}-05-25" for year in self.full_range)
        )

    def test_corpus_christi(self):
        name = "Corpus Christi"
        self.assertHolidayName(
            name,
            "1957-06-20",
            "1958-06-05",
            "1959-05-28",
            "1960-06-16",
            "1961-06-01",
            "1962-06-21",
            "1963-06-13",
            "1964-05-28",
            "1965-06-17",
            "1966-06-09",
            "1967-05-25",
            "1968-06-13",
            "1969-06-05",
            "1970-05-28",
            "1971-06-10",
            "1972-06-01",
            "1973-06-21",
            "1974-06-13",
            "1975-05-29",
        )
        self.assertNoHolidayName(name, range(1976, 2050))

    def test_sovereignty_over_malvinas_day(self):
        name = (
            "Día de la Afirmación de los Derechos Argentinos sobre las Malvinas, "
            "Islas y Sector Antártico"
        )
        self.assertHolidayName(
            name,
            "1983-04-02",
            "1984-06-10",
            "1985-06-10",
            "1986-06-10",
            "1987-06-10",
            "1988-06-13",
            "1989-06-10",
            "1990-06-10",
            "1991-06-10",
            "1992-06-08",
            "1993-06-14",
            "1994-06-13",
            "1995-06-10",
            "1996-06-10",
            "1997-06-09",
            "1998-06-08",
            "1999-06-14",
            "2000-06-10",
        )
        self.assertNoHolidayName(name, range(AR.start_year, 1983), range(2001, 2050))

    def test_guemes_day(self):
        name = "Paso a la Inmortalidad del General Don Martín Miguel de Güemes"
        self.assertHolidayName(
            name,
            "2016-06-17",
            "2017-06-17",
            "2018-06-17",
            "2019-06-17",
            "2020-06-15",
            "2021-06-21",
            "2022-06-17",
            "2023-06-17",
            "2024-06-17",
            "2025-06-16",
        )
        self.assertHolidayName(name, range(2016, 2050))
        self.assertNoHolidayName(name, range(AR.start_year, 2016))

    def test_belgrano_day(self):
        name = "Paso a la Inmortalidad del General Don Manuel Belgrano"
        self.assertHolidayName(
            name,
            (
                f"{year}-06-20"
                for year in (*range(AR.start_year, 1988), *range(1992, 1995), *range(2011, 2050))
            ),
        )
        self.assertHolidayName(
            name,
            "1988-06-20",
            "1989-06-19",
            "1990-06-18",
            "1991-06-24",
            "1995-06-19",
            "1996-06-17",
            "1997-06-16",
            "1998-06-15",
            "1999-06-21",
            "2000-06-19",
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
        self.assertHolidayName(
            "Día de la Independencia", (f"{year}-07-09" for year in self.full_range)
        )

    def test_san_martin_day(self):
        name = "Paso a la Inmortalidad del General Don José de San Martín"
        self.assertHolidayName(
            name,
            "2011-08-22",
            "2012-08-20",
            "2013-08-19",
            "2014-08-18",
            "2015-08-17",
            "2016-08-15",
            "2017-08-21",
            "2018-08-20",
            "2019-08-17",
            "2020-08-17",
            "2021-08-16",
            "2022-08-15",
            "2023-08-21",
            "2024-08-17",
            "2025-08-17",
        )
        self.assertHolidayName(name, self.full_range)

    def test_assumption_day(self):
        name = "Día de la Asunción"
        self.assertHolidayName(name, (f"{year}-08-15" for year in range(AR.start_year, 1976)))
        self.assertNoHolidayName(name, range(1976, 2050))

    def test_cultural_diversity_day(self):
        name_1 = "Día de la Raza"
        name_2 = "Día del Respeto a la Diversidad Cultural"
        self.assertHolidayName(
            name_1, (f"{year}-10-12" for year in (*range(AR.start_year, 1976), *range(1982, 1988)))
        )
        self.assertHolidayName(
            name_1,
            "1988-10-10",
            "1989-10-16",
            "1990-10-15",
            "1991-10-12",
            "1992-10-12",
            "1993-10-11",
            "1994-10-10",
            "1995-10-16",
            "1996-10-12",
            "1997-10-12",
            "1998-10-12",
            "1999-10-11",
            "2000-10-16",
            "2001-10-08",
            "2002-10-14",
            "2003-10-12",
            "2004-10-11",
            "2005-10-10",
            "2006-10-16",
            "2007-10-15",
            "2008-10-13",
            "2009-10-12",
        )
        self.assertHolidayName(
            name_2,
            "2010-10-11",
            "2011-10-10",
            "2012-10-08",
            "2013-10-14",
            "2014-10-13",
            "2015-10-12",
            "2016-10-10",
            "2017-10-16",
            "2018-10-15",
            "2019-10-12",
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-16",
            "2024-10-12",
            "2025-10-12",
        )
        self.assertHolidayName(name_2, range(2010, 2050))
        self.assertNoHolidayName(name_1, range(1976, 1982), range(2010, 2050))
        self.assertNoHolidayName(name_2, range(AR.start_year, 2010))

    def test_all_saints_day(self):
        name = "Todos Los Santos"
        self.assertHolidayName(name, (f"{year}-11-01" for year in range(AR.start_year, 1976)))
        self.assertNoHolidayName(name, range(1976, 2050))

    def test_national_sovereignty_day(self):
        name = "Día de la Soberanía Nacional"
        self.assertHolidayName(
            name,
            "2010-11-22",
            "2011-11-28",
            "2012-11-26",
            "2013-11-25",
            "2014-11-24",
            "2015-11-27",
            "2016-11-28",
            "2017-11-20",
            "2018-11-19",
            "2019-11-18",
            "2020-11-23",
            "2021-11-20",
            "2022-11-20",
            "2023-11-20",
            "2024-11-18",
            "2025-11-24",
        )
        self.assertHolidayName(name, range(2010, 2050))
        self.assertNoHolidayName(name, range(1976, 2010))

    def test_immaculate_conception_day(self):
        name = "Inmaculada Concepción de María"
        self.assertHolidayName(
            name, (f"{year}-12-08" for year in (*range(AR.start_year, 1976), *range(1995, 2050)))
        )
        self.assertNoHolidayName(name, range(1976, 1995))

    def test_christmas_day(self):
        self.assertHolidayName("Navidad", (f"{year}-12-25" for year in self.full_range))

    def test_anniversary_of_battle_of_salta(self):
        name = "Aniversario de la Batalla de Salta"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "A":
                self.assertHolidayName(
                    name, holidays, (f"{year}-02-20" for year in range(1977, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 1977))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_memory_of_guemes_salta(self):
        name = (
            "Dia de la memoria del Guerrero de la Independencia y Gobernador "
            "de la Provincia de Salta General Don Martín Miguel de Güemes"
        )
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "A":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-17" for year in range(1977, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 1977))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_feasts_of_lord_and_virgin_of_miracle(self):
        name = "Festividades del Señor y de la Virgen del Milagro"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "A":
                self.assertHolidayName(
                    name,
                    holidays,
                    (f"{year}-09-13" for year in range(1977, 2050)),
                    (f"{year}-09-14" for year in range(1977, 2050)),
                    (f"{year}-09-15" for year in range(1977, 2050)),
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 1977))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_exaltation_of_holy_cross_day(self):
        name = "Día de la Exaltación de la Santa Cruz"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "D":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-03" for year in range(2004, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2004))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_louis_day(self):
        name = "Día de San Luis Rey de Francia"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "D":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-25" for year in range(2004, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2004))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_day_of_remembrance_entre_rios(self):
        name = "Día Provincial de la Memoria por la Verdad y la Justicia"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "E":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-24" for year in range(2018, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2018))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_commemoration_of_battle_of_caseros(self):
        name = "Conmemoración de la Batalla de Caseros"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "E":
                self.assertHolidayName(
                    name, holidays, (f"{year}-02-03" for year in range(1984, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 1984))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_state_workers_day_entre_rios(self):
        name = "Día del Trabajador Estatal"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "E":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-27" for year in range(2004, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2004))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_michael_archangels_day(self):
        name = "San Miguel Arcángel"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "E":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-29" for year in range(1993, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 1993))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_death_of_juan_facundo_quiroga(self):
        name = "Día del fallecimiento de Juan Facundo Quiroga"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "F":
                self.assertHolidayName(
                    name, holidays, (f"{year}-02-16" for year in range(2021, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2021))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_provincial_autonomy_day(self):
        name = "Día de la Autonomía Provincial"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "F":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-01" for year in range(2020, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2020))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_day_of_remembrance_la_rioja(self):
        name = "Día de la Memoria por la Verdad y la Justicia"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "F":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-24" for year in range(2017, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2017))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_malvinas_memorial_day(self):
        name = "Día de los Caídos en Malvinas"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "F":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-02" for year in range(2017, 2021))
                )
                self.assertNoHolidayName(
                    name, holidays, range(AR.start_year, 2017), range(2021, 2050)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_la_rioja_foundation_day(self):
        name = "Día de la fundación de La Rioja"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "F":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-20" for year in range(2000, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2000))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_death_of_enrique_angelelli(self):
        name = "Día del Aniversario del Fallecimiento de Monseñor Enrique Angelelli"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "F":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-04" for year in range(2016, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2016))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_death_of_angel_vicente_penaloza(self):
        name = "Día del Aniversario del Fallecimiento de Ángel Vicente Peñaloza"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "F":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-12" for year in range(2020, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2020))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_tinkunaco_festival(self):
        name = "Día del Tinkunaco Riojano"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "F":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-31" for year in range(2000, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2000))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_teachers_day(self):
        name = "Día del Maestro"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "J":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-11" for year in range(2015, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2015))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_birthday_of_mamerto_esquiu(self):
        name = "Natalicio de Fray Mamerto Esquiú"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "K":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-11" for year in range(1990, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 1990))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_catamarca_autonomy_day(self):
        name = "Autonomía de Catamarca"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "K":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-25" for year in range(1990, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 1990))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_miracle_day(self):
        name = "Día del Milagro"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "K":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-07" for year in range(2018, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2018))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_immaculate_conception_day_catamarka(self):
        name = "Inmaculada Concepción de María"
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "K":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-08" for year in range(1989, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(1976, 1989))
            else:
                self.assertNoHolidayName(name, holidays, range(1976, 1995))

    def test_saint_james_day(self):
        name = "Día del Apóstol Santiago"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "M":
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-25" for year in range(1977, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 1977))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_anniversary_of_battle_of_tucuman(self):
        name = "Aniversario de la Batalla de Tucumán"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "T":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-24" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_plebiscite_1902_trevelin(self):
        name = "Plebiscito 1902 Trevelin"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "U":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-30" for year in range(1984, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 1984))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_anniversary_of_arrival_of_first_welsh_settlers(self):
        name = "Aniversario del arribo de los primeros colonizadores galeses"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "U":
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-28" for year in range(1984, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 1984))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_national_petroleum_day(self):
        name = "Día del Petróleo Nacional"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "U":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-13" for year in range(1984, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 1984))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_tehuelches_and_mapuches_declare_loyalty(self):
        name = "Tehuelches y Mapuches declaran lealtad a la bandera Argentina"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "U":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-03" for year in range(2015, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2015))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_day_of_province_of_tierra_del_fuego(self):
        name = "Día de la Provincia de Tierra del Fuego, Antártida e Islas del Atlántico Sur"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "V":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-01" for year in range(1992, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 1992))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_selknam_genocide_day(self):
        name = "Día del Genocidio Selk'Nam"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "V":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-25" for year in range(2021, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2021))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_anniversary_of_death_of_belgrano_corrientes(self):
        name = (
            "Día del Aniversario del Fallecimiento del General Manuel José Joaquín "
            "del Corazón de Jesús Belgrano"
        )
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "W":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-20" for year in range(2009, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2009))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_anniversary_of_death_of_san_martin_corrientes(self):
        name = "Día del Aniversario del Fallecimiento del General José Francisco de San Martín"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "W":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-17" for year in range(2009, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2009))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_carnival_monday_jujuy(self):
        name = "Lunes de Carnaval"
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "Y":
                self.assertHolidayName(
                    name,
                    holidays,
                    "1984-03-05",
                    "1985-02-18",
                    "1986-02-10",
                    "1987-03-02",
                    "1990-02-26",
                    "1991-02-11",
                    "1992-03-02",
                    "1993-02-22",
                    "1994-02-14",
                    "2005-02-07",
                    "2006-02-27",
                    "2007-02-19",
                    "2008-02-04",
                    "2009-02-23",
                    "2010-02-15",
                )
                self.assertHolidayName(name, holidays, range(1984, 2050))
                self.assertNoHolidayName(name, holidays, range(1977, 1984))
            else:
                self.assertNoHolidayName(name, holidays, range(1977, 2011))

    def test_carnival_tuesday_jujuy(self):
        name = "Martes de Carnaval"
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "Y":
                self.assertHolidayName(
                    name,
                    holidays,
                    "1984-03-06",
                    "1985-02-19",
                    "1986-02-11",
                    "1987-03-03",
                    "1990-02-27",
                    "1991-02-12",
                    "1992-03-03",
                    "1993-02-23",
                    "1994-02-15",
                    "2005-02-08",
                    "2006-02-28",
                    "2007-02-20",
                    "2008-02-05",
                    "2009-02-24",
                    "2010-02-16",
                )
                self.assertHolidayName(name, holidays, range(1984, 2050))
                self.assertNoHolidayName(name, holidays, range(1977, 1984))
            else:
                self.assertNoHolidayName(name, holidays, range(1977, 2011))

    def test_jujuy_exodus_day(self):
        name = "Día del Éxodo Jujeño"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "Y":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-23" for year in range(1984, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 1984))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_jujuy_political_autonomy_day(self):
        name = "Autonomía Política de Jujuy"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "Y":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-18" for year in range(1984, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 1984))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_pachamama_day(self):
        name = "Día de la Pachamama"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "Y":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-01" for year in range(1996, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 1996))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_day_of_virgin_of_rosary_of_rio_blanco_and_paypaya(self):
        name = "Día de la Virgen del Rosario de Río Blanco y Paypaya"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "Y":
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-07" for year in range(1997, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 1997))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_great_day_of_jujuy(self):
        name = "Día Grande de Jujuy"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "Y":
                self.assertHolidayName(
                    name, holidays, (f"{year}-04-27" for year in range(2021, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2021))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_saint_john_boscos_day(self):
        name = "Homenaje al Patrono de la Provincia San Juan Bosco"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "Z":
                self.assertHolidayName(
                    name,
                    holidays,
                    (f"{year}-01-31" for year in range(2007, 2015)),
                    (f"{year}-08-16" for year in range(2015, 2050)),
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2007))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_anniversary_of_death_of_nestor_carlos_kirchner(self):
        name = (
            "Día del Aniversario del Fallecimiento del ex Presidente de la Nación "
            "Doctor Néstor Carlos Kirchner"
        )
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "Z":
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-27" for year in range(2014, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2014))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_commemoration_of_workers_shot_in_patagonian_strikes(self):
        name = "Conmemoración a los obreros fusilados en las Huelgas Patagónicas"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "Z":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-07" for year in range(2019, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(AR.start_year, 2019))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_armenian_holidays(self):
        name = "Día de acción por la tolerancia y el respeto entre los pueblos"
        self.assertNoHolidayName(name)
        self.assertArmenianHolidayName(name, (f"{year}-04-24" for year in range(2007, 2050)))
        self.assertNoArmenianHolidayName(name, range(AR.start_year, 2007))

    def test_bank_holidays(self):
        name = "Día del Bancario"
        self.assertNoHolidayName(name)
        self.assertBankHolidayName(name, (f"{year}-11-06" for year in range(1975, 2050)))
        self.assertNoBankHolidayName(name, range(AR.start_year, 1975))

    def test_government_holidays(self):
        name = "Día del Trabajador del Estado"
        self.assertNoHolidayName(name)
        self.assertGovernmentHolidayName(name, (f"{year}-06-27" for year in range(2014, 2050)))
        self.assertNoGovernmentHolidayName(name, range(AR.start_year, 2014))

    def test_hebrew_holidays(self):
        name = "Año Nuevo Judío (Rosh Hashana)"
        self.assertNoHolidayName(name)
        self.assertHebrewHolidayName(
            name,
            "1996-09-14",
            "1996-09-15",
            "1997-10-02",
            "1997-10-03",
            "2018-09-10",
            "2018-09-11",
            "2019-09-30",
            "2019-10-01",
            "2020-09-19",
            "2020-09-20",
            "2021-09-07",
            "2021-09-08",
            "2022-09-26",
            "2022-09-27",
            "2023-09-16",
            "2023-09-17",
            "2024-10-03",
            "2024-10-04",
            "2025-09-23",
            "2025-09-24",
        )
        self.assertHebrewHolidayName(name, range(1996, 2050))
        self.assertNoHebrewHolidayName(name, range(AR.start_year, 1996))

        name = "Día del Perdón (Iom Kipur)"
        self.assertNoHolidayName(name)
        self.assertHebrewHolidayName(
            name,
            "1996-09-23",
            "1997-10-11",
            "2018-09-19",
            "2019-10-09",
            "2020-09-28",
            "2021-09-16",
            "2022-10-05",
            "2023-09-25",
            "2024-10-12",
            "2025-10-02",
        )
        self.assertHebrewHolidayName(name, range(1996, 2050))
        self.assertNoHebrewHolidayName(name, range(AR.start_year, 1996))

        name = "Pascua Judía (Pésaj)"
        self.assertNoHolidayName(name)
        self.assertHebrewHolidayName(
            name,
            "2007-04-03",
            "2007-04-04",
            "2007-04-09",
            "2007-04-10",
            "2008-04-20",
            "2008-04-21",
            "2008-04-26",
            "2008-04-27",
            "2018-03-31",
            "2018-04-01",
            "2018-04-06",
            "2018-04-07",
            "2019-04-20",
            "2019-04-21",
            "2019-04-26",
            "2019-04-27",
            "2020-04-09",
            "2020-04-10",
            "2020-04-15",
            "2020-04-16",
            "2021-03-28",
            "2021-03-29",
            "2021-04-03",
            "2021-04-04",
            "2022-04-16",
            "2022-04-17",
            "2022-04-22",
            "2022-04-23",
            "2023-04-06",
            "2023-04-07",
            "2023-04-12",
            "2023-04-13",
            "2024-04-23",
            "2024-04-24",
            "2024-04-29",
            "2024-04-30",
            "2025-04-13",
            "2025-04-14",
            "2025-04-19",
            "2025-04-20",
        )
        self.assertHebrewHolidayName(name, range(2007, 2050))
        self.assertNoHebrewHolidayName(name, range(AR.start_year, 2007))

    def test_islamic_holidays(self):
        name = "Año Nuevo Musulmán (Hégira)"
        self.assertNoHolidayName(name)
        self.assertIslamicIslamicNoEstimatedHolidayName(
            name,
            "2019-08-31",
            "2020-08-20",
            "2021-08-08",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-26",
        )
        self.assertIslamicIslamicNoEstimatedHolidayName(name, range(1997, 2050))
        self.assertNoIslamicIslamicNoEstimatedHolidayName(name, range(AR.start_year, 1997))

        name = "Día posterior a la culminación del ayuno (Id Al-Fitr)"
        self.assertNoHolidayName(name)
        self.assertIslamicIslamicNoEstimatedHolidayName(
            name,
            "2019-06-04",
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-31",
        )
        self.assertIslamicIslamicNoEstimatedHolidayName(name, range(1997, 2050))
        self.assertNoIslamicIslamicNoEstimatedHolidayName(name, range(AR.start_year, 1997))

        name = "Día de la Fiesta del Sacrificio (Id Al-Adha)"
        self.assertNoHolidayName(name)
        self.assertIslamicIslamicNoEstimatedHolidayName(
            name,
            "2019-08-11",
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-10",
        )
        self.assertIslamicIslamicNoEstimatedHolidayName(name, range(1997, 2050))
        self.assertNoIslamicIslamicNoEstimatedHolidayName(name, range(AR.start_year, 1997))

    def test_2022(self):
        self.assertHolidays(
            Argentina(years=2022),
            ("2022-01-01", "Año Nuevo"),
            ("2022-02-28", "Lunes de Carnaval"),
            ("2022-03-01", "Martes de Carnaval"),
            ("2022-03-24", "Día Nacional de la Memoria por la Verdad y la Justicia"),
            ("2022-04-02", "Día del Veterano y de los Caidos en la Guerra de Malvinas"),
            ("2022-04-14", "Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-05-18", "Censo Nacional 2022"),
            ("2022-05-25", "Día de la Revolución de Mayo"),
            ("2022-06-17", "Paso a la Inmortalidad del General Don Martín Miguel de Güemes"),
            ("2022-06-20", "Paso a la Inmortalidad del General Don Manuel Belgrano"),
            ("2022-07-09", "Día de la Independencia"),
            ("2022-08-15", "Paso a la Inmortalidad del General Don José de San Martín"),
            ("2022-10-07", "Feriado con fines turísticos"),
            ("2022-10-10", "Día del Respeto a la Diversidad Cultural"),
            ("2022-11-20", "Día de la Soberanía Nacional"),
            ("2022-11-21", "Feriado con fines turísticos"),
            ("2022-12-08", "Inmaculada Concepción de María"),
            ("2022-12-09", "Feriado con fines turísticos"),
            ("2022-12-20", "Día de la Victoria de la Copa Mundial de la FIFA 2022"),
            ("2022-12-25", "Navidad"),
        )

    def test_2023(self):
        self.assertHolidays(
            Argentina(years=2023),
            ("2023-01-01", "Año Nuevo"),
            ("2023-02-20", "Lunes de Carnaval"),
            ("2023-02-21", "Martes de Carnaval"),
            ("2023-03-24", "Día Nacional de la Memoria por la Verdad y la Justicia"),
            ("2023-04-02", "Día del Veterano y de los Caidos en la Guerra de Malvinas"),
            ("2023-04-06", "Jueves Santo"),
            ("2023-04-07", "Viernes Santo"),
            ("2023-05-01", "Día del Trabajo"),
            ("2023-05-25", "Día de la Revolución de Mayo"),
            ("2023-05-26", "Feriado con fines turísticos"),
            ("2023-06-17", "Paso a la Inmortalidad del General Don Martín Miguel de Güemes"),
            ("2023-06-19", "Feriado con fines turísticos"),
            ("2023-06-20", "Paso a la Inmortalidad del General Don Manuel Belgrano"),
            ("2023-07-09", "Día de la Independencia"),
            ("2023-08-21", "Paso a la Inmortalidad del General Don José de San Martín"),
            ("2023-10-13", "Feriado con fines turísticos"),
            ("2023-10-16", "Día del Respeto a la Diversidad Cultural"),
            ("2023-11-20", "Día de la Soberanía Nacional"),
            ("2023-12-08", "Inmaculada Concepción de María"),
            ("2023-12-25", "Navidad"),
        )

    def test_2024(self):
        self.assertHolidays(
            Argentina(years=2024),
            ("2024-01-01", "Año Nuevo"),
            ("2024-02-12", "Lunes de Carnaval"),
            ("2024-02-13", "Martes de Carnaval"),
            ("2024-03-24", "Día Nacional de la Memoria por la Verdad y la Justicia"),
            ("2024-03-28", "Jueves Santo"),
            ("2024-03-29", "Viernes Santo"),
            ("2024-04-01", "Feriado con fines turísticos"),
            ("2024-04-02", "Día del Veterano y de los Caidos en la Guerra de Malvinas"),
            ("2024-05-01", "Día del Trabajo"),
            ("2024-05-25", "Día de la Revolución de Mayo"),
            ("2024-06-17", "Paso a la Inmortalidad del General Don Martín Miguel de Güemes"),
            ("2024-06-20", "Paso a la Inmortalidad del General Don Manuel Belgrano"),
            ("2024-06-21", "Feriado con fines turísticos"),
            ("2024-07-09", "Día de la Independencia"),
            ("2024-08-17", "Paso a la Inmortalidad del General Don José de San Martín"),
            ("2024-10-11", "Feriado con fines turísticos"),
            ("2024-10-12", "Día del Respeto a la Diversidad Cultural"),
            ("2024-11-18", "Día de la Soberanía Nacional"),
            ("2024-12-08", "Inmaculada Concepción de María"),
            ("2024-12-25", "Navidad"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-02-03", "Conmemoración de la Batalla de Caseros"),
            ("2022-02-16", "Día del fallecimiento de Juan Facundo Quiroga"),
            ("2022-02-20", "Aniversario de la Batalla de Salta"),
            ("2022-02-28", "Lunes de Carnaval"),
            ("2022-03-01", "Día de la Autonomía Provincial; Martes de Carnaval"),
            (
                "2022-03-24",
                "Día Nacional de la Memoria por la Verdad y la Justicia; "
                "Día Provincial de la Memoria por la Verdad y la Justicia; "
                "Día de la Memoria por la Verdad y la Justicia",
            ),
            ("2022-04-02", "Día del Veterano y de los Caidos en la Guerra de Malvinas"),
            ("2022-04-14", "Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-04-16", "Pascua Judía (Pésaj)"),
            ("2022-04-17", "Pascua Judía (Pésaj)"),
            ("2022-04-22", "Pascua Judía (Pésaj)"),
            ("2022-04-23", "Pascua Judía (Pésaj)"),
            ("2022-04-24", "Día de acción por la tolerancia y el respeto entre los pueblos"),
            ("2022-04-27", "Día Grande de Jujuy"),
            ("2022-04-30", "Plebiscito 1902 Trevelin"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-05-02", "Día posterior a la culminación del ayuno (Id Al-Fitr)"),
            ("2022-05-03", "Día de la Exaltación de la Santa Cruz"),
            ("2022-05-11", "Natalicio de Fray Mamerto Esquiú"),
            ("2022-05-18", "Censo Nacional 2022"),
            ("2022-05-20", "Día de la fundación de La Rioja"),
            ("2022-05-25", "Día de la Revolución de Mayo"),
            (
                "2022-06-01",
                "Día de la Provincia de Tierra del Fuego, Antártida e Islas del Atlántico Sur",
            ),
            (
                "2022-06-17",
                "Dia de la memoria del Guerrero de la Independencia y Gobernador de la Provincia "
                "de Salta General Don Martín Miguel de Güemes; "
                "Paso a la Inmortalidad del General Don Martín Miguel de Güemes",
            ),
            (
                "2022-06-20",
                "Día del Aniversario del Fallecimiento del General Manuel José Joaquín "
                "del Corazón de Jesús Belgrano; "
                "Paso a la Inmortalidad del General Don Manuel Belgrano",
            ),
            ("2022-06-27", "Día del Trabajador Estatal; Día del Trabajador del Estado"),
            (
                "2022-07-09",
                "Día de la Fiesta del Sacrificio (Id Al-Adha); Día de la Independencia",
            ),
            ("2022-07-25", "Día del Apóstol Santiago"),
            ("2022-07-28", "Aniversario del arribo de los primeros colonizadores galeses"),
            ("2022-07-30", "Año Nuevo Musulmán (Hégira)"),
            ("2022-08-01", "Día de la Pachamama"),
            ("2022-08-04", "Día del Aniversario del Fallecimiento de Monseñor Enrique Angelelli"),
            ("2022-08-15", "Paso a la Inmortalidad del General Don José de San Martín"),
            ("2022-08-16", "Homenaje al Patrono de la Provincia San Juan Bosco"),
            (
                "2022-08-17",
                "Día del Aniversario del Fallecimiento del General José Francisco de San Martín",
            ),
            ("2022-08-23", "Día del Éxodo Jujeño"),
            ("2022-08-25", "Autonomía de Catamarca; Día de San Luis Rey de Francia"),
            ("2022-09-07", "Día del Milagro"),
            ("2022-09-11", "Día del Maestro"),
            ("2022-09-13", "Festividades del Señor y de la Virgen del Milagro"),
            ("2022-09-14", "Festividades del Señor y de la Virgen del Milagro"),
            ("2022-09-15", "Festividades del Señor y de la Virgen del Milagro"),
            ("2022-09-24", "Aniversario de la Batalla de Tucumán"),
            ("2022-09-26", "Año Nuevo Judío (Rosh Hashana)"),
            ("2022-09-27", "Año Nuevo Judío (Rosh Hashana)"),
            ("2022-09-29", "San Miguel Arcángel"),
            ("2022-10-05", "Día del Perdón (Iom Kipur)"),
            (
                "2022-10-07",
                "Día de la Virgen del Rosario de Río Blanco y Paypaya; "
                "Feriado con fines turísticos",
            ),
            ("2022-10-10", "Día del Respeto a la Diversidad Cultural"),
            (
                "2022-10-27",
                "Día del Aniversario del Fallecimiento del ex Presidente de la Nación "
                "Doctor Néstor Carlos Kirchner",
            ),
            ("2022-11-03", "Tehuelches y Mapuches declaran lealtad a la bandera Argentina"),
            ("2022-11-06", "Día del Bancario"),
            ("2022-11-12", "Día del Aniversario del Fallecimiento de Ángel Vicente Peñaloza"),
            ("2022-11-18", "Autonomía Política de Jujuy"),
            ("2022-11-20", "Día de la Soberanía Nacional"),
            ("2022-11-21", "Feriado con fines turísticos"),
            ("2022-11-25", "Día del Genocidio Selk'Nam"),
            ("2022-12-07", "Conmemoración a los obreros fusilados en las Huelgas Patagónicas"),
            ("2022-12-08", "Inmaculada Concepción de María"),
            ("2022-12-09", "Feriado con fines turísticos"),
            ("2022-12-13", "Día del Petróleo Nacional"),
            ("2022-12-20", "Día de la Victoria de la Copa Mundial de la FIFA 2022"),
            ("2022-12-25", "Navidad"),
            ("2022-12-31", "Día del Tinkunaco Riojano"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-02-03", "Commemoration of the Battle of Caseros"),
            ("2022-02-16", "Day of the Death of Juan Facundo Quiroga"),
            ("2022-02-20", "Anniversary of the Battle of Salta"),
            ("2022-02-28", "Carnival Monday"),
            ("2022-03-01", "Carnival Tuesday; Provincial Autonomy Day"),
            (
                "2022-03-24",
                "Day of Remembrance for Truth and Justice; "
                "National Day of Remembrance for Truth and Justice; "
                "Provincial Day of Remembrance for Truth and Justice",
            ),
            ("2022-04-02", "Veteran's Day and the Fallen in the Malvinas War"),
            ("2022-04-14", "Maundy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-16", "Pesach"),
            ("2022-04-17", "Pesach"),
            ("2022-04-22", "Pesach"),
            ("2022-04-23", "Pesach"),
            ("2022-04-24", "Day of Action for Tolerance and Respect among Peoples"),
            ("2022-04-27", "Great Day of Jujuy"),
            ("2022-04-30", "Plebiscite 1902 Trevelin"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-02", "Eid al-Fitr"),
            ("2022-05-03", "Exaltation of the Holy Cross Day"),
            ("2022-05-11", "Birthday of Mamerto Esquiú"),
            ("2022-05-18", "National Census Day 2022"),
            ("2022-05-20", "La Rioja Foundation Day"),
            ("2022-05-25", "May Revolution Day"),
            (
                "2022-06-01",
                "Day of the Province of Tierra del Fuego, Antarctica and the South "
                "Atlantic Islands",
            ),
            (
                "2022-06-17",
                "Day of Memory of General Don Martín Miguel de Güemes; "
                "Pass to the Immortality of General Don Martín Miguel de Güemes",
            ),
            (
                "2022-06-20",
                "Anniversary of the Death of General Manuel Belgrano; "
                "Pass to the Immortality of General Don Manuel Belgrano",
            ),
            ("2022-06-27", "State Worker's Day"),
            ("2022-07-09", "Eid al-Adha; Independence Day"),
            ("2022-07-25", "Saint James' Day"),
            ("2022-07-28", "Anniversary of the arrival of the first Welsh settlers"),
            ("2022-07-30", "Islamic New Year"),
            ("2022-08-01", "Pachamama Day"),
            ("2022-08-04", "Anniversary of the Death of Enrique Angelelli"),
            ("2022-08-15", "Pass to the Immortality of General Don José de San Martín"),
            ("2022-08-16", "Saint John Bosco's Day"),
            ("2022-08-17", "Anniversary of the Death of General José Francisco de San Martín"),
            ("2022-08-23", "Jujuy Exodus Day"),
            ("2022-08-25", "Catamarca Autonomy Day; Saint Louis the King of France's Day"),
            ("2022-09-07", "Miracle Day"),
            ("2022-09-11", "Teacher's Day"),
            ("2022-09-13", "Feasts of the Lord and the Virgin of Miracle"),
            ("2022-09-14", "Feasts of the Lord and the Virgin of Miracle"),
            ("2022-09-15", "Feasts of the Lord and the Virgin of Miracle"),
            ("2022-09-24", "Anniversary of the Battle of Tucumán"),
            ("2022-09-26", "Rosh Hashanah"),
            ("2022-09-27", "Rosh Hashanah"),
            ("2022-09-29", "Saint Michael the Archangel's Day"),
            ("2022-10-05", "Yom Kippur"),
            (
                "2022-10-07",
                "Bridge Public Holiday; Day of the Virgin of the Rosary of Río Blanco and Paypaya",
            ),
            ("2022-10-10", "Respect for Cultural Diversity Day"),
            ("2022-10-27", "Anniversary of the Death of Néstor Carlos Kirchner"),
            ("2022-11-03", "Tehuelches and Mapuches declare loyalty to the Argentine flag"),
            ("2022-11-06", "Bankers' Day"),
            ("2022-11-12", "Anniversary of the Death of Ángel Vicente Peñaloza"),
            ("2022-11-18", "Jujuy Political Autonomy Day"),
            ("2022-11-20", "National Sovereignty Day"),
            ("2022-11-21", "Bridge Public Holiday"),
            ("2022-11-25", "Selk'Nam Genocide Day"),
            ("2022-12-07", "Commemoration of the workers shot in the Patagonian Strikes"),
            ("2022-12-08", "Immaculate Conception"),
            ("2022-12-09", "Bridge Public Holiday"),
            ("2022-12-13", "National Petroleum Day"),
            ("2022-12-20", "FIFA World Cup 2022 Victory Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-31", "Tinkunaco Festival"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-02-03", "День битви під Касеросом"),
            ("2022-02-16", "День смерті Хуана Факундо Кіроги"),
            ("2022-02-20", "Річниця битви при Сальті"),
            ("2022-02-28", "Карнавальний понеділок"),
            ("2022-03-01", "День провінційної автономії; Карнавальний вівторок"),
            (
                "2022-03-24",
                "День памʼяті заради правди та правосуддя; "
                "Національний день памʼяті заради правди та правосуддя; "
                "Провінційний день памʼяті заради правди та правосуддя",
            ),
            ("2022-04-02", "День ветеранів та загиблих на Мальвінській війні"),
            ("2022-04-14", "Великий четвер"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-16", "Песах"),
            ("2022-04-17", "Песах"),
            ("2022-04-22", "Песах"),
            ("2022-04-23", "Песах"),
            ("2022-04-24", "День дій на підтримку толерантності та поваги між народами"),
            ("2022-04-27", "Великий День Хухуя"),
            ("2022-04-30", "Річниця плебісциту 1902 року"),
            ("2022-05-01", "День праці"),
            ("2022-05-02", "Рамазан-байрам"),
            ("2022-05-03", "День Воздвиження Хреста Господнього"),
            ("2022-05-11", "День народження Мамерто Ескуї"),
            ("2022-05-18", "День національного перепису 2022"),
            ("2022-05-20", "День заснування Ла-Ріохи"),
            ("2022-05-25", "День Травневої революції"),
            (
                "2022-06-01",
                "День провінції Вогняна Земля, Антарктиди і Південноатлантичних островів",
            ),
            ("2022-06-17", "День памʼяті генерала Мартіна Мігеля де Гуемеса"),
            (
                "2022-06-20",
                "День памʼяті генерала Мануеля Бельграно; День смерті генерала Мануеля Бельграно",
            ),
            ("2022-06-27", "День державного службовця"),
            ("2022-07-09", "День незалежності; Курбан-байрам"),
            ("2022-07-25", "День Святого Якова"),
            ("2022-07-28", "Річниця прибуття перших валлійських поселенців"),
            ("2022-07-30", "Ісламський Новий рік"),
            ("2022-08-01", "День Пачамами"),
            ("2022-08-04", "День смерті Енріке Анхелельї"),
            ("2022-08-15", "День памʼяті генерала Хосе де Сан-Мартіна"),
            ("2022-08-16", "День Святого Івана Боско"),
            ("2022-08-17", "День смерті генерала Хосе де Сан-Мартіна"),
            ("2022-08-23", "День Виходу Хухуя"),
            ("2022-08-25", "День Святого Людовика; День автономії Катамарки"),
            ("2022-09-07", "День дива"),
            ("2022-09-11", "День учителя"),
            ("2022-09-13", "Свято Господа та Богородиці Чуда"),
            ("2022-09-14", "Свято Господа та Богородиці Чуда"),
            ("2022-09-15", "Свято Господа та Богородиці Чуда"),
            ("2022-09-24", "Річниця битви при Тукумані"),
            ("2022-09-26", "Рош га-Шана"),
            ("2022-09-27", "Рош га-Шана"),
            ("2022-09-29", "День Святого Архангела Михаїла"),
            ("2022-10-05", "Йом Кіпур"),
            ("2022-10-07", "День Богородиці Вервиці Ріо-Бланко і Пайпаї; Додатковий вихідний"),
            ("2022-10-10", "День поваги до культурного різноманіття"),
            ("2022-10-27", "День смерті Нестора Карлоса Кіршнера"),
            ("2022-11-03", "День присяги теуелче та мапуче на вірність аргентинському прапору"),
            ("2022-11-06", "День банківських працівників"),
            ("2022-11-12", "День смерті Анхеля Вісенте Пеньялоса"),
            ("2022-11-18", "День політичної автономії Хухуя"),
            ("2022-11-20", "День національного суверенітету"),
            ("2022-11-21", "Додатковий вихідний"),
            ("2022-11-25", "День геноциду народу селькнам"),
            (
                "2022-12-07",
                "Вшанування пам'яті робітників, розстріляних під час Патагонських страйків",
            ),
            ("2022-12-08", "Непорочне зачаття Діви Марії"),
            ("2022-12-09", "Додатковий вихідний"),
            ("2022-12-13", "Національний день нафти"),
            ("2022-12-20", "День перемоги збірної Аргентини на Чемпіонаті світу з футболу 2022"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-31", "Свято Тінкунако"),
        )
