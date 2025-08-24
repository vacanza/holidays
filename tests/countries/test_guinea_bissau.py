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

from holidays.countries.guinea_bissau import GuineaBissau, GW, GNB
from tests.common import CommonCountryTests


class TestGuineaBissau(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(2023, 2050)
        super().setUpClass(GuineaBissau, years=years)
        cls.no_estimated_holidays = GuineaBissau(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(GuineaBissau, GW, GNB)

    def test_no_holidays(self):
        self.assertNoHolidays(GuineaBissau(years=2022))

    def test_new_years_day(self):
        self.assertHolidayName("Ano Novo", (f"{year}-01-01" for year in range(2023, 2050)))

    def test_national_heroes_day(self):
        self.assertHolidayName(
            "Dia dos Heróis Nacionais", (f"{year}-01-20" for year in range(2023, 2050))
        )

    def test_day_of_the_beginning_of_the_armed_struggle(self):
        self.assertHolidayName(
            "Dia do Início da Luta Armada", (f"{year}-01-23" for year in range(2023, 2050))
        )

    def test_womens_day(self):
        self.assertHolidayName(
            "Dia Internacional da Mulher", (f"{year}-03-08" for year in range(2023, 2050))
        )

    def test_easter_sunday(self):
        name = "Páscoa"
        self.assertHolidayName(
            name,
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, range(2023, 2050))

    def test_workers_day(self):
        self.assertHolidayName(
            "Dia do Trabalhador", (f"{year}-05-01" for year in range(2023, 2050))
        )

    def test_pidjiguiti_day(self):
        self.assertHolidayName(
            "Dia de Pidjiguiti", (f"{year}-08-03" for year in range(2023, 2050))
        )

    def test_independence_day(self):
        self.assertHolidayName(
            "Dia da Independência", (f"{year}-09-24" for year in range(2023, 2050))
        )

    def test_christmas_day(self):
        self.assertHolidayName("Dia de Natal", (f"{year}-12-25" for year in range(2023, 2050)))

    def test_korite(self):
        name = "Korité"
        self.assertHolidayName(
            name,
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2023, 2050))

    def test_tabaski(self):
        name = "Tabaski"
        self.assertHolidayName(
            name,
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(2023, 2050))

    def test_2024(self):
        self.assertHolidays(
            GuineaBissau(years=2024),
            ("2024-01-01", "Ano Novo"),
            ("2024-01-20", "Dia dos Heróis Nacionais"),
            ("2024-01-23", "Dia do Início da Luta Armada"),
            ("2024-03-08", "Dia Internacional da Mulher"),
            ("2024-03-31", "Páscoa"),
            ("2024-04-10", "Korité"),
            ("2024-05-01", "Dia do Trabalhador"),
            ("2024-06-16", "Tabaski"),
            ("2024-08-03", "Dia de Pidjiguiti"),
            ("2024-09-24", "Dia da Independência"),
            ("2024-12-25", "Dia de Natal"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Ano Novo"),
            ("2025-01-20", "Dia dos Heróis Nacionais"),
            ("2025-01-23", "Dia do Início da Luta Armada"),
            ("2025-03-08", "Dia Internacional da Mulher"),
            ("2025-03-30", "Korité"),
            ("2025-04-20", "Páscoa"),
            ("2025-05-01", "Dia do Trabalhador"),
            ("2025-06-06", "Tabaski"),
            ("2025-08-03", "Dia de Pidjiguiti"),
            ("2025-09-24", "Dia da Independência"),
            ("2025-12-25", "Dia de Natal"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-20", "National Heroes' Day"),
            ("2025-01-23", "Day of the Beginning of the Armed Struggle"),
            ("2025-03-08", "International Women's Day"),
            ("2025-03-30", "Eid al-Fitr"),
            ("2025-04-20", "Easter Sunday"),
            ("2025-05-01", "Worker's Day"),
            ("2025-06-06", "Eid al-Adha"),
            ("2025-08-03", "Pidjiguiti Day"),
            ("2025-09-24", "Independence Day"),
            ("2025-12-25", "Christmas Day"),
        )
