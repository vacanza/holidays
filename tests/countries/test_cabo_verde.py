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
from holidays.countries.cabo_verde import CaboVerde, CV, CPV
from tests.common import CommonCountryTests


class TestCapeVerde(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CaboVerde)

    def test_country_aliases(self):
        self.assertAliases(CaboVerde, CV, CPV)

    def test_no_holidays(self):
        self.assertNoHolidays(
            CaboVerde(categories=CaboVerde.supported_categories, years=CV.start_year - 1)
        )

    def test_new_years_day(self):
        self.assertHolidayName("Ano Novo", (f"{year}-01-01" for year in self.full_range))

    def test_democracy_and_freedom_day(self):
        name = "Dia da Liberdade e da Democracia"
        self.assertHolidayName(name, (f"{year}-01-13" for year in range(2000, 2050)))
        self.assertNoHolidayName(name, range(CV.start_year, 2000))

    def test_heroes_day(self):
        self.assertHolidayName(
            "Dia da Nacionalidade e dos Heróis Nacionais",
            (f"{year}-01-20" for year in self.full_range),
        )

    def test_ash_wednesday(self):
        name = "Quarta-feira de Cinzas"
        self.assertHolidayName(
            name,
            "2020-02-26",
            "2021-02-17",
            "2022-03-02",
            "2023-02-22",
            "2024-02-14",
            "2025-03-05",
        )
        self.assertHolidayName(name, self.full_range)

    def test_good_friday(self):
        name = "Sexta-feira Santa"
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

    def test_easter_sunday(self):
        name = "Páscoa"
        self.assertHolidayName(
            name,
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, self.full_range)

    def test_workers_day(self):
        self.assertHolidayName("Dia do Trabalhador", (f"{year}-05-01" for year in self.full_range))

    def test_international_childrens_day(self):
        name = "Dia Mundial da Criança"
        self.assertHolidayName(name, (f"{year}-06-01" for year in range(2005, 2050)))
        self.assertNoHolidayName(name, range(CV.start_year, 2005))

    def test_independence_day(self):
        self.assertHolidayName(
            "Dia da Independência Nacional", (f"{year}-07-05" for year in self.full_range)
        )

    def test_assumption_day(self):
        self.assertHolidayName("Dia da Assunção", (f"{year}-08-15" for year in self.full_range))

    def test_all_saints_day(self):
        self.assertHolidayName(
            "Dia de Todos os Santos", (f"{year}-11-01" for year in self.full_range)
        )

    def test_christmas_day(self):
        self.assertHolidayName("Dia do Natal", (f"{year}-12-25" for year in self.full_range))

    def test_holy_thursday(self):
        name = "Quinta-Feira Santa"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
        )
        self.assertOptionalHolidayName(name, self.full_range)

    def test_mothers_day(self):
        name = "Dia das Mães"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2020-05-10",
            "2021-05-09",
            "2022-05-08",
            "2023-05-14",
            "2024-05-12",
            "2025-05-11",
        )
        self.assertOptionalHolidayName(name, self.full_range)

    def test_fathers_day(self):
        name = "Dia dos Pais"
        self.assertNoHolidayName(name)
        self.assertOptionalHolidayName(
            name,
            "2020-06-21",
            "2021-06-20",
            "2022-06-19",
            "2023-06-18",
            "2024-06-16",
            "2025-06-15",
        )
        self.assertOptionalHolidayName(name, self.full_range)

    def test_brava_municipality_day(self):
        name = "Dia do Município da Brava"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BR":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-24" for year in range(1983, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 1983))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_boa_vista_municipality_day(self):
        name = "Dia do Município da Boa Vista"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "BV":
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-04" for year in range(1983, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 1983))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_santa_catarina_de_santiago_municipality_day(self):
        name = "Dia do Município de Santa Catarina de Santiago"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "CA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-25" for year in range(1982, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 1982))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_santa_catarina_do_fogo_municipality_day(self):
        name = "Dia do Município de Santa Catarina do Fogo"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "CF":
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-25" for year in range(2005, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 2005))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_santa_cruz_municipality_day(self):
        name = "Dia do Município de Santa Cruz"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "CR":
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-25" for year in range(1983, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 1983))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_maio_municipality_day(self):
        name = "Dia do Município do Maio"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "MA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-08" for year in range(1983, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 1983))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_mosteiros_municipality_day(self):
        name = "Dia do Município dos Mosteiros"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "MO":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-15" for year in range(1992, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 1992))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_santo_antao_island_day(self):
        name = "Dia da Ilha de Santo Antão"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in {"PA", "PN", "RG"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-17" for year in range(1983, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 1983))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_paul_municipality_day(self):
        name = "Dia do Município do Paúl"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-13" for year in range(1983, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 1983))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_porto_novo_municipality_day(self):
        name = "Dia do Município do Porto Novo"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PN":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-02" for year in range(1983, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 1983))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_praia_municipality_day(self):
        name = "Dia do Município da Praia"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "PR":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-19" for year in range(1983, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 1983))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_ribeira_brava_municipality_day(self):
        name = "Dia do Município de Ribeira Brava"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "RB":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-06" for year in range(2005, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 2005))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_ribeira_grande_municipality_day(self):
        name = "Dia do Município de Ribeira Grande"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "RG":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-07" for year in range(1983, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 1983))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_ribeira_grande_de_santiago_municipality_day(self):
        name = "Dia do Município de Ribeira Grande de Santiago"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "RS":
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-31" for year in range(2006, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 2006))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_sao_domingos_municipality_day(self):
        name = "Dia do Município de São Domingos"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SD":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-13" for year in range(1994, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 1994))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_sao_filipe_municipality_day(self):
        name = "Dia do Município de São Filipe"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SF":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-01" for year in range(1992, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 1992))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_sal_municipality_day(self):
        name = "Dia do Município do Sal"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SL":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-15" for year in range(1983, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 1983))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_sao_miguel_municipality_day(self):
        name = "Dia do Município de São Miguel"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SM":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-29" for year in range(1997, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 1997))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_sao_lourenco_dos_orgaos_municipality_day(self):
        name = "Dia do Município de São Lourenço dos Órgãos"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SO":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-09" for year in range(2005, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 2005))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_sao_salvador_do_mundo_municipality_day(self):
        name = "Dia do Município de São Salvador do Mundo"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SS":
                self.assertHolidayName(
                    name, holidays, (f"{year}-07-19" for year in range(2005, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 2005))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_sao_vicente_municipality_day(self):
        name = "Dia do Município de São Vicente"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SV":
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-22" for year in range(1983, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 1983))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_carnival_tuesday(self):
        name = "Terça-feira de Carnaval"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "SV":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-02-25",
                    "2021-02-16",
                    "2022-03-01",
                    "2023-02-21",
                    "2024-02-13",
                    "2025-03-04",
                )
                self.assertHolidayName(name, holidays, range(1983, 2050))
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 1983))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_tarrafal_de_santiago_municipality_day(self):
        name = "Dia do Município do Tarrafal de Santiago"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TA":
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-15" for year in range(1983, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 1983))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_tarrafal_de_sao_nicolau_municipality_day(self):
        name = "Dia do Município do Tarrafal de São Nicolau"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TS":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-02" for year in range(2005, 2050))
                )
                self.assertNoHolidayName(name, holidays, range(CV.start_year, 2005))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_2024_public_holidays(self):
        self.assertHolidays(
            CaboVerde(years=2024),
            ("2024-01-01", "Ano Novo"),
            ("2024-01-13", "Dia da Liberdade e da Democracia"),
            ("2024-01-20", "Dia da Nacionalidade e dos Heróis Nacionais"),
            ("2024-02-14", "Quarta-feira de Cinzas"),
            ("2024-03-29", "Sexta-feira Santa"),
            ("2024-03-31", "Páscoa"),
            ("2024-05-01", "Dia do Trabalhador"),
            ("2024-06-01", "Dia Mundial da Criança"),
            ("2024-07-05", "Dia da Independência Nacional"),
            ("2024-08-15", "Dia da Assunção"),
            ("2024-11-01", "Dia de Todos os Santos"),
            ("2024-12-25", "Dia do Natal"),
        )

    def test_2024_optional_holidays(self):
        self.assertHolidays(
            CaboVerde(categories=OPTIONAL, years=2024),
            ("2024-03-28", "Quinta-Feira Santa"),
            ("2024-05-12", "Dia das Mães"),
            ("2024-06-16", "Dia dos Pais"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Ano Novo"),
            ("2025-01-13", "Dia da Liberdade e da Democracia"),
            ("2025-01-15", "Dia do Município do Tarrafal de Santiago"),
            ("2025-01-17", "Dia da Ilha de Santo Antão"),
            ("2025-01-20", "Dia da Nacionalidade e dos Heróis Nacionais"),
            ("2025-01-22", "Dia do Município de São Vicente"),
            ("2025-01-31", "Dia do Município de Ribeira Grande de Santiago"),
            ("2025-03-04", "Terça-feira de Carnaval"),
            ("2025-03-05", "Quarta-feira de Cinzas"),
            ("2025-03-13", "Dia do Município de São Domingos"),
            ("2025-04-17", "Quinta-Feira Santa"),
            ("2025-04-18", "Sexta-feira Santa"),
            ("2025-04-20", "Páscoa"),
            ("2025-05-01", "Dia do Município de São Filipe; Dia do Trabalhador"),
            ("2025-05-07", "Dia do Município de Ribeira Grande"),
            ("2025-05-09", "Dia do Município de São Lourenço dos Órgãos"),
            ("2025-05-11", "Dia das Mães"),
            ("2025-05-19", "Dia do Município da Praia"),
            ("2025-06-01", "Dia Mundial da Criança"),
            ("2025-06-13", "Dia do Município do Paúl"),
            ("2025-06-15", "Dia dos Pais"),
            ("2025-06-24", "Dia do Município da Brava"),
            ("2025-07-04", "Dia do Município da Boa Vista"),
            ("2025-07-05", "Dia da Independência Nacional"),
            ("2025-07-19", "Dia do Município de São Salvador do Mundo"),
            ("2025-07-25", "Dia do Município de Santa Cruz"),
            ("2025-08-02", "Dia do Município do Tarrafal de São Nicolau"),
            ("2025-08-15", "Dia da Assunção; Dia do Município dos Mosteiros"),
            ("2025-09-02", "Dia do Município do Porto Novo"),
            ("2025-09-08", "Dia do Município do Maio"),
            ("2025-09-15", "Dia do Município do Sal"),
            ("2025-09-29", "Dia do Município de São Miguel"),
            ("2025-11-01", "Dia de Todos os Santos"),
            (
                "2025-11-25",
                "Dia do Município de Santa Catarina de Santiago; "
                "Dia do Município de Santa Catarina do Fogo",
            ),
            ("2025-12-06", "Dia do Município de Ribeira Brava"),
            ("2025-12-25", "Dia do Natal"),
        )

    def test_l10n_de(self):
        self.assertLocalizedHolidays(
            "de",
            ("2025-01-01", "Neujahr"),
            ("2025-01-13", "Tag der Demokratie und Freiheit"),
            ("2025-01-15", "Tag der Gemeinde Tarrafal de Santiago"),
            ("2025-01-17", "Tag der Insel Santo Antão"),
            ("2025-01-20", "Tag der Nationalhelden"),
            ("2025-01-22", "Tag der Gemeinde São Vicente"),
            ("2025-01-31", "Tag der Gemeinde Ribeira Grande de Santiago"),
            ("2025-03-04", "Faschingsdienstag"),
            ("2025-03-05", "Aschermittwoch"),
            ("2025-03-13", "Tag der Gemeinde São Domingos"),
            ("2025-04-17", "Gründonnerstag"),
            ("2025-04-18", "Karfreitag"),
            ("2025-04-20", "Ostersonntag"),
            ("2025-05-01", "Tag der Arbeit; Tag der Gemeinde São Filipe"),
            ("2025-05-07", "Tag der Gemeinde Ribeira Grande"),
            ("2025-05-09", "Tag der Gemeinde São Lourenço dos Órgãos"),
            ("2025-05-11", "Muttertag"),
            ("2025-05-19", "Tag der Gemeinde Praia"),
            ("2025-06-01", "Weltkindertag"),
            ("2025-06-13", "Tag der Gemeinde Paúl"),
            ("2025-06-15", "Vatertag"),
            ("2025-06-24", "Tag der Gemeinde Brava"),
            ("2025-07-04", "Tag der Gemeinde Boa Vista"),
            ("2025-07-05", "Unabhängigkeitstag"),
            ("2025-07-19", "Tag der Gemeinde São Salvador do Mundo"),
            ("2025-07-25", "Tag der Gemeinde Santa Cruz"),
            ("2025-08-02", "Tag der Gemeinde Tarrafal de São Nicolau"),
            ("2025-08-15", "Mariä Himmelfahrt; Tag der Gemeinde Mosteiros"),
            ("2025-09-02", "Tag der Gemeinde Porto Novo"),
            ("2025-09-08", "Tag der Gemeinde Maio"),
            ("2025-09-15", "Tag der Gemeinde Sal"),
            ("2025-09-29", "Tag der Gemeinde São Miguel"),
            ("2025-11-01", "Allerheiligen"),
            (
                "2025-11-25",
                "Tag der Gemeinde Santa Catarina de Santiago; "
                "Tag der Gemeinde Santa Catarina do Fogo",
            ),
            ("2025-12-06", "Tag der Gemeinde Ribeira Brava"),
            ("2025-12-25", "Weihnachten"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-13", "Democracy and Freedom Day"),
            ("2025-01-15", "Tarrafal de Santiago Municipality Day"),
            ("2025-01-17", "Santo Antão Island Day"),
            ("2025-01-20", "National Heroes Day"),
            ("2025-01-22", "São Vicente Municipality Day"),
            ("2025-01-31", "Ribeira Grande de Santiago Municipality Day"),
            ("2025-03-04", "Carnival Tuesday"),
            ("2025-03-05", "Ash Wednesday"),
            ("2025-03-13", "São Domingos Municipality Day"),
            ("2025-04-17", "Holy Thursday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-20", "Easter Sunday"),
            ("2025-05-01", "São Filipe Municipality Day; Worker's Day"),
            ("2025-05-07", "Ribeira Grande Municipality Day"),
            ("2025-05-09", "São Lourenço dos Órgãos Municipality Day"),
            ("2025-05-11", "Mother's Day"),
            ("2025-05-19", "Praia Municipality Day"),
            ("2025-06-01", "International Children's Day"),
            ("2025-06-13", "Paúl Municipality Day"),
            ("2025-06-15", "Father's Day"),
            ("2025-06-24", "Brava Municipality Day"),
            ("2025-07-04", "Boa Vista Municipality Day"),
            ("2025-07-05", "Independence Day"),
            ("2025-07-19", "São Salvador do Mundo Municipality Day"),
            ("2025-07-25", "Santa Cruz Municipality Day"),
            ("2025-08-02", "Tarrafal de São Nicolau Municipality Day"),
            ("2025-08-15", "Assumption Day; Mosteiros Municipality Day"),
            ("2025-09-02", "Porto Novo Municipality Day"),
            ("2025-09-08", "Maio Municipality Day"),
            ("2025-09-15", "Sal Municipality Day"),
            ("2025-09-29", "São Miguel Municipality Day"),
            ("2025-11-01", "All Saints' Day"),
            (
                "2025-11-25",
                "Santa Catarina de Santiago Municipality Day; "
                "Santa Catarina do Fogo Municipality Day",
            ),
            ("2025-12-06", "Ribeira Brava Municipality Day"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_l10n_es(self):
        self.assertLocalizedHolidays(
            "es",
            ("2025-01-01", "Año Nuevo"),
            ("2025-01-13", "Día de la Libertad y la Democracia"),
            ("2025-01-15", "Día del Municipio de Tarrafal de Santiago"),
            ("2025-01-17", "Día de la Isla de Santo Antão"),
            ("2025-01-20", "Día de la Nacionalidad y de los Héroes Nacionales"),
            ("2025-01-22", "Día del Municipio de São Vicente"),
            ("2025-01-31", "Día del Municipio de Ribeira Grande de Santiago"),
            ("2025-03-04", "Martes de Carnaval"),
            ("2025-03-05", "Miércoles de Ceniza"),
            ("2025-03-13", "Día del Municipio de São Domingos"),
            ("2025-04-17", "Jueves Santo"),
            ("2025-04-18", "Viernes Santo"),
            ("2025-04-20", "Domingo de Pascua"),
            ("2025-05-01", "Día del Municipio de São Filipe; Día del Trabajador"),
            ("2025-05-07", "Día del Municipio de Ribeira Grande"),
            ("2025-05-09", "Día del Municipio de São Lourenço dos Órgãos"),
            ("2025-05-11", "Día de la Madre"),
            ("2025-05-19", "Día del Municipio de Praia"),
            ("2025-06-01", "Día Mundial de la Infancia"),
            ("2025-06-13", "Día del Municipio de Paúl"),
            ("2025-06-15", "Día del Padre"),
            ("2025-06-24", "Día del Municipio de Brava"),
            ("2025-07-04", "Día del Municipio de Boa Vista"),
            ("2025-07-05", "Día de la Independencia Nacional"),
            ("2025-07-19", "Día del Municipio de São Salvador do Mundo"),
            ("2025-07-25", "Día del Municipio de Santa Cruz"),
            ("2025-08-02", "Día del Municipio de Tarrafal de São Nicolau"),
            ("2025-08-15", "Asunción de Nuestra Señora; Día del Municipio de Mosteiros"),
            ("2025-09-02", "Día del Municipio de Porto Novo"),
            ("2025-09-08", "Día del Municipio de Maio"),
            ("2025-09-15", "Día del Municipio de Sal"),
            ("2025-09-29", "Día del Municipio de São Miguel"),
            ("2025-11-01", "Día de Todos los Santos"),
            (
                "2025-11-25",
                "Día del Municipio de Santa Catarina de Santiago; "
                "Día del Municipio de Santa Catarina do Fogo",
            ),
            ("2025-12-06", "Día del Municipio de Ribeira Brava"),
            ("2025-12-25", "Navidad"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2025-01-01", "Nouvel An"),
            ("2025-01-13", "Journée de la liberté et de la démocratie"),
            ("2025-01-15", "Journée de la municipalité de Tarrafal de Santiago"),
            ("2025-01-17", "Journée de l'île de Santo Antão"),
            ("2025-01-20", "Journée de la nationalité et des héros nationaux"),
            ("2025-01-22", "Journée de la municipalité de São Vicente"),
            ("2025-01-31", "Journée de la municipalité de Ribeira Grande de Santiago"),
            ("2025-03-04", "Mardi du Carnaval"),
            ("2025-03-05", "Mercredi des Cendres"),
            ("2025-03-13", "Journée de la municipalité de São Domingos"),
            ("2025-04-17", "Jeudi Saint"),
            ("2025-04-18", "Vendredi Saint"),
            ("2025-04-20", "Dimanche de Pâques"),
            ("2025-05-01", "Fête du travail; Journée de la municipalité de São Filipe"),
            ("2025-05-07", "Journée de la municipalité de Ribeira Grande"),
            ("2025-05-09", "Journée de la municipalité de São Lourenço dos Órgãos"),
            ("2025-05-11", "Fête des Mères"),
            ("2025-05-19", "Journée de la municipalité de Praia"),
            ("2025-06-01", "Journée mondiale de l'enfance"),
            ("2025-06-13", "Journée de la municipalité de Paúl"),
            ("2025-06-15", "Fête des Pères"),
            ("2025-06-24", "Journée de la municipalité de Brava"),
            ("2025-07-04", "Journée de la municipalité de Boa Vista"),
            ("2025-07-05", "Fête de l'Indépendance Nationale"),
            ("2025-07-19", "Journée de la municipalité de São Salvador do Mundo"),
            ("2025-07-25", "Journée de la municipalité de Santa Cruz"),
            ("2025-08-02", "Journée de la municipalité de Tarrafal de São Nicolau"),
            ("2025-08-15", "Assomption de Notre-Dame; Journée de la municipalité des Mosteiros"),
            ("2025-09-02", "Journée de la municipalité de Porto Novo"),
            ("2025-09-08", "Journée de la municipalité de Maio"),
            ("2025-09-15", "Journée de la municipalité de Sal"),
            ("2025-09-29", "Journée de la municipalité de São Miguel"),
            ("2025-11-01", "Toussaint"),
            (
                "2025-11-25",
                "Journée de la municipalité de Santa Catarina de Santiago; "
                "Journée de la municipalité de Santa Catarina do Fogo",
            ),
            ("2025-12-06", "Journée de la municipalité de Ribeira Brava"),
            ("2025-12-25", "Noël"),
        )
