#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.constants import OPTIONAL, PUBLIC
from holidays.countries import CapeVerde, CV, CAV
from tests.common import CommonCountryTests


class TestCapeVerde(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CapeVerde, years=range(1976, 2050))

    def test_country_aliases(self):
        self.assertAliases(CapeVerde, CV, CAV)

    def test_no_holidays(self):
        self.assertNoHolidays(CapeVerde(categories=(OPTIONAL, PUBLIC), years=1975))

    def test_democracy_and_freedom_day(self):
        name = "Dia da Liberdade e Democracia"
        self.assertHolidayName(name, (f"{year}-01-13" for year in range(1991, 2050)))
        self.assertNoHolidayName(name, range(1976, 1991))

    def test_independence_day(self):
        self.assertHolidayName(
            "Dia da Independência Nacional", (f"{year}-07-05" for year in range(1976, 2050))
        )

    def test_heroes_day(self):
        self.assertHolidayName(
            "Dia da Nacionalidade e dos Heróis Nacionais",
            (f"{year}-01-20" for year in range(1976, 2050)),
        )

    def test_international_childrens_day(self):
        self.assertHolidayName(
            "Dia Mundial da Criança", (f"{year}-06-01" for year in range(1976, 2050))
        )

    def test_2024_public_holidays(self):
        self.assertHolidays(
            CapeVerde(categories=PUBLIC, years=2024),
            ("2024-01-01", "Ano Novo"),
            ("2024-01-13", "Dia da Liberdade e Democracia"),
            ("2024-01-20", "Dia da Nacionalidade e dos Heróis Nacionais"),
            ("2024-02-14", "Quarta-feira de Cinzas"),
            ("2024-03-29", "Sexta-feira Santa"),
            ("2024-03-31", "Páscoa"),
            ("2024-05-01", "Dia do Trabalhador"),
            ("2024-06-01", "Dia Mundial da Criança"),
            ("2024-07-05", "Dia da Independência Nacional"),
            ("2024-08-15", "Dia da Assunção"),
            ("2024-11-01", "Dia de Todos os Santos"),
            ("2024-12-25", "Natal"),
        )

    def test_2024_optional_holidays(self):
        self.assertHolidays(
            CapeVerde(categories=OPTIONAL, years=2024),
            ("2024-03-28", "Quinta-Feira Santa"),
            ("2024-05-12", "Dia das Mães"),
            ("2024-06-16", "Dia dos Pais"),
        )

    def test_2025_public_holidays(self):
        self.assertHolidays(
            CapeVerde(categories=PUBLIC, years=2025),
            ("2025-01-01", "Ano Novo"),
            ("2025-01-13", "Dia da Liberdade e Democracia"),
            ("2025-01-20", "Dia da Nacionalidade e dos Heróis Nacionais"),
            ("2025-03-05", "Quarta-feira de Cinzas"),
            ("2025-04-18", "Sexta-feira Santa"),
            ("2025-04-20", "Páscoa"),
            ("2025-05-01", "Dia do Trabalhador"),
            ("2025-06-01", "Dia Mundial da Criança"),
            ("2025-07-05", "Dia da Independência Nacional"),
            ("2025-08-15", "Dia da Assunção"),
            ("2025-11-01", "Dia de Todos os Santos"),
            ("2025-12-25", "Natal"),
        )

    def test_default_l10n(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Ano Novo"),
            ("2025-01-13", "Dia da Liberdade e Democracia"),
            ("2025-01-20", "Dia da Nacionalidade e dos Heróis Nacionais"),
            ("2025-01-22", "Dia do Município de São Vicente"),
            ("2025-01-31", "Dia do Município de Ribeira Grande de Santiago"),
            ("2025-03-04", "Terça-feira de Carnaval"),
            ("2025-03-05", "Quarta-feira de Cinzas"),
            ("2025-04-17", "Quinta-Feira Santa"),
            ("2025-04-18", "Sexta-feira Santa"),
            ("2025-04-20", "Páscoa"),
            ("2025-04-29", "Dia da Cidade da Praia"),
            ("2025-05-01", "Dia do Trabalhador"),
            ("2025-05-11", "Dia das Mães"),
            ("2025-05-19", "Dia do Município da Praia"),
            ("2025-06-01", "Dia Mundial da Criança"),
            ("2025-06-15", "Dia dos Pais"),
            ("2025-06-24", "Dia do Município da Brava"),
            ("2025-07-04", "Dia do Município"),
            ("2025-07-05", "Dia da Independência Nacional"),
            ("2025-08-02", "Dia do Município do Tarrafal de São Nicolau"),
            ("2025-08-15", "Dia da Assunção"),
            ("2025-09-08", "Dia do Município do Maio"),
            ("2025-09-15", "Dia do Município"),
            ("2025-11-01", "Dia de Todos os Santos"),
            ("2025-12-06", "Dia do Município de Ribeira Brava"),
            ("2025-12-25", "Natal"),
        )

    def test_en_us_l10n(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-13", "Democracy and Freedom Day"),
            ("2025-01-20", "National Heroes Day"),
            ("2025-01-22", "St. Vincent Municipal Day"),
            ("2025-01-31", "Day of the Municipality of Ribeira Grande de Santiago"),
            ("2025-03-04", "Shrove Tuesday"),
            ("2025-03-05", "Ash Wednesday"),
            ("2025-04-17", "Holy Thursday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-20", "Easter Sunday"),
            ("2025-04-29", "Praia City Day"),
            ("2025-05-01", "Worker's Day"),
            ("2025-05-11", "Mother's Day"),
            ("2025-05-19", "Praia Municipal Day"),
            ("2025-06-01", "International Children's Day"),
            ("2025-06-15", "Father's Day"),
            ("2025-06-24", "Day of the Municipality of Brava"),
            ("2025-07-04", "Municipal Day"),
            ("2025-07-05", "Independence Day"),
            ("2025-08-02", "Day of the Municipality of Tarrafal de São Nicolau"),
            ("2025-08-15", "Assumption Day"),
            ("2025-09-08", "May Day"),
            ("2025-09-15", "Municipal Day"),
            ("2025-11-01", "All Saints' Day"),
            ("2025-12-06", "Day of the Municipality of Ribeira Brava"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_municipal_specific_days(self):
        subdiv_holidays = {
            "BR": ("2024-06-24",),
            "BV": ("2024-07-04",),
            "CF": ("2024-05-01",),
            "MA": ("2024-09-08",),
            "PR": ("2024-04-29",),
            "RB": ("2024-12-06",),
            "RS": ("2024-01-31",),
            "SL": ("2024-09-15",),
            "SV": ("2024-01-22",),
            "TS": ("2024-08-02",),
        }
        for subdiv, holidays in subdiv_holidays.items():
            self.assertHoliday(CapeVerde(subdiv=subdiv, years=2024), holidays)
