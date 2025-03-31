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
        super().setUpClass(CapeVerde, years=range(1973, 2050))

    def test_country_aliases(self):
        self.assertAliases(CapeVerde, CV, CAV)

    def test_no_holidays(self):
        self.assertNoHolidays(CapeVerde(years=1972))

    def test_democracy_day(self):
        name = "Dia da Liberdade e Democracia"
        self.assertHolidayName(name, (f"{year}-01-13" for year in range(1991, 2050)))
        self.assertNoHolidayName(name, CapeVerde(years=(1973, 1990)))

    def test_independence_day(self):
        name = "Dia da Independência Nacional"
        self.assertHolidayName(name, (f"{year}-07-05" for year in range(1975, 2050)))
        self.assertNoHolidayName(name, CapeVerde(years=(1973, 1974)))

    def test_heroes_day(self):
        self.assertHolidayName(
            "Dia da Nacionalidade e dos Heróis Nacionais",
            (f"{year}-01-20" for year in range(1973, 2050)),
        )

    def test_youth_day(self):
        self.assertHolidayName(
            "Dia Mundial da Criança", (f"{year}-06-01" for year in range(1973, 2050))
        )

    def test_2026_public_holidays(self):
        holidays = CapeVerde(categories=PUBLIC, years=2026)
        self.assertHolidayName("Ano Novo", holidays, "2026-01-01")
        self.assertHolidayName("Dia da Liberdade e Democracia", holidays, "2026-01-13")
        self.assertHolidayName(
            "Dia da Nacionalidade e dos Heróis Nacionais", holidays, "2026-01-20"
        )
        self.assertHolidayName("Sexta-feira Santa", holidays, "2026-04-03")
        self.assertHolidayName("Dia do Trabalhador", holidays, "2026-05-01")
        self.assertHolidayName("Dia Mundial da Criança", holidays, "2026-06-01")
        self.assertHolidayName("Dia da Independência Nacional", holidays, "2026-07-05")
        self.assertHolidayName("Dia da Assunção", holidays, "2026-08-15")
        self.assertHolidayName("Dia de Todos os Santos", holidays, "2026-11-01")
        self.assertHolidayName("Natal", holidays, "2026-12-25")

    def test_2026_optional_holidays(self):
        holidays = CapeVerde(categories=OPTIONAL, years=2026)
        self.assertHolidayName("Dia das Cinzas", holidays, "2026-02-18")
        self.assertHolidayName("Quinta-Feira Santa", holidays, "2026-04-02")
        self.assertHolidayName("Páscoa", holidays, "2026-04-05")
        self.assertHolidayName("Dia das Mães", holidays, "2026-05-10")
        self.assertHolidayName("Dia dos Pais", holidays, "2026-06-21")

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
            ("2025-01-20", "Heroes Day"),
            ("2025-03-05", "Ash Wednesday"),
            ("2025-04-17", "Holy Thursday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-20", "Easter Sunday"),
            ("2025-05-01", "Labor Day"),
            ("2025-05-11", "Mother's Day"),
            ("2025-06-01", "Youth Day"),
            ("2025-06-15", "Father's Day"),
            ("2025-07-05", "Independence Day"),
            ("2025-08-15", "Assumption of Mary"),
            ("2025-11-01", "All Saints' Day"),
            ("2025-12-25", "Christmas Day"),
        )
