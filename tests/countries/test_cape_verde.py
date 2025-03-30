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

#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2026-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2026
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

    def test_2025_holidays(self):
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

    def test_democracy_day(self):
        name = "Dia da Liberdade e Democracia"
        self.assertNoHolidayName(name, CapeVerde(years=1990))
        self.assertHolidayName(
            name,
            (f"{year}-01-13" for year in range(1991, 2050)),
        )
        self.assertNoHolidayName(name, range(1980, 1990))

    def test_no_democracy_day_before_1991(self):
        self.assertNoHolidayName("Dia da Liberdade e Democracia", CapeVerde(years=1990))

    def test_independence_day(self):
        name = "Dia da Independência Nacional"
        self.assertNoHolidayName(name, CapeVerde(years=1974))
        self.assertHolidayName(
            name,
            (f"{year}-07-05" for year in range(1975, 2050)),
        )

    def test_heroes_day(self):
        name = "Dia da Nacionalidade e dos Heróis Nacionais"
        self.assertNoHolidayName(name, CapeVerde(years=1972))
        self.assertHolidayName(
            name,
            (f"{year}-01-20" for year in range(1973, 2050)),
        )

    def test_youth_day(self):
        name = "Dia Mundial da Criança"
        self.assertHolidayName(
            name,
            (f"{year}-06-01" for year in range(1973, 2050)),
        )

    def test_public_holidays(self):
        holidays = CapeVerde(categories=PUBLIC, years=2026)
        self.assertHoliday(
            holidays,
            "2026-01-01",
            "2026-01-13",
            "2026-01-20",
            "2026-04-03",
            "2026-05-01",
            "2026-06-01",
            "2026-07-05",
            "2026-08-15",
            "2026-11-01",
            "2026-12-25",
        )

    def test_optional_holidays(self):
        holidays = CapeVerde(categories=OPTIONAL, years=2026)
        self.assertHoliday(
            holidays,
            "2026-02-18",
            "2026-03-20",
            "2026-04-02",
            "2026-04-05",
            "2026-05-10",
            "2026-06-21",
            "2026-09-22",
            "2026-12-21",
        )
