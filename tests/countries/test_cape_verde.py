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

    def test_democracy_day(self):
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
            ("2024-03-29", "Sexta-feira Santa"),
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
            ("2024-02-14", "Dia das Cinzas"),
            ("2024-03-28", "Quinta-Feira Santa"),
            ("2024-03-31", "Páscoa"),
            ("2024-05-12", "Dia das Mães"),
            ("2024-06-16", "Dia dos Pais"),
        )

    def test_2025_public_holidays(self):
        self.assertHolidays(
            CapeVerde(years=2025),
            ("2025-01-01", "Ano Novo"),
            ("2025-01-13", "Dia da Liberdade e Democracia"),
            ("2025-01-20", "Dia da Nacionalidade e dos Heróis Nacionais"),
            ("2025-04-18", "Sexta-feira Santa"),
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
            ("2025-03-05", "Dia das Cinzas"),
            ("2025-04-17", "Quinta-Feira Santa"),
            ("2025-04-18", "Sexta-feira Santa"),
            ("2025-04-20", "Páscoa"),
            ("2025-05-01", "Dia do Trabalhador"),
            ("2025-05-11", "Dia das Mães"),
            ("2025-06-01", "Dia Mundial da Criança"),
            ("2025-06-15", "Dia dos Pais"),
            ("2025-07-05", "Dia da Independência Nacional"),
            ("2025-08-15", "Dia da Assunção"),
            ("2025-11-01", "Dia de Todos os Santos"),
            ("2025-12-25", "Natal"),
        )

    def test_en_us_l10n(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-13", "Democracy Day"),
            ("2025-01-20", "National Heroes Day"),
            ("2025-03-05", "Ash Wednesday"),
            ("2025-04-17", "Holy Thursday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-20", "Easter Sunday"),
            ("2025-05-01", "Worker's Day"),
            ("2025-05-11", "Mother's Day"),
            ("2025-06-01", "International Children's Day"),
            ("2025-06-15", "Father's Day"),
            ("2025-07-05", "Independence Day"),
            ("2025-08-15", "Assumption Day"),
            ("2025-11-01", "All Saints' Day"),
            ("2025-12-25", "Christmas Day"),
        )
