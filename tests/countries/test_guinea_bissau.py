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

from holidays.countries import GuineaBissau, GW, GNB
from tests.common import CommonCountryTests


class TestGuineaBissau(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1975, 2050)
        super().setUpClass(GuineaBissau, years=years, years_non_observed=years)
        cls.no_estimated_holidays = GuineaBissau(years=years, islamic_show_estimated=False)

    def test_country_aliases(self):
        self.assertAliases(GuineaBissau, GW, GNB)

    def test_no_holidays(self):
        self.assertNoHolidays(GuineaBissau(years=1974))

    def test_new_years_day(self):
        self.assertHolidayName("Ano Novo", (f"{year}-01-01" for year in range(1975, 2050)))

    def test_national_heroes_day(self):
        self.assertHolidayName(
            "Dia dos Heróis Nacionais", (f"{year}-01-20" for year in range(1975, 2050))
        )

    def test_international_womens_day(self):
        self.assertHolidayName(
            "Dia Internacional da Mulher", (f"{year}-03-08" for year in range(1975, 2050))
        )

    def test_good_friday(self):
        name = "Sexta-feira Santa"
        self.assertHolidayName(
            name,
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, range(1975, 2050))

    def test_easter_sunday(self):
        name = "Páscoa"
        self.assertHolidayName(
            name,
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
        )
        self.assertHolidayName(name, range(1975, 2050))

    def test_labor_day(self):
        self.assertHolidayName(
            "Dia do Trabalhador", (f"{year}-05-01" for year in range(1975, 2050))
        )

    def test_independence_day(self):
        self.assertHolidayName(
            "Dia da Independência", (f"{year}-09-24" for year in range(1975, 2050))
        )

    def test_all_souls_day(self):
        self.assertHolidayName("Dia dos Finados", (f"{year}-11-02" for year in range(1975, 2050)))

    def test_christmas_eve(self):
        self.assertHolidayName("Véspera de Natal", (f"{year}-12-24" for year in range(1975, 2050)))

    def test_christmas_day(self):
        self.assertHolidayName("Dia de Natal", (f"{year}-12-25" for year in range(1975, 2050)))

    def test_new_years_eve(self):
        self.assertHolidayName(
            "Véspera de Ano Novo", (f"{year}-12-31" for year in range(1975, 2050))
        )

    def test_korite(self):
        name = "Korité"
        self.assertHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-03",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1975, 2050))

    def test_tabaski(self):
        name = "Tabaski"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2021-07-21",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertHolidayName(name, self.no_estimated_holidays, range(1975, 2050))

    def test_2024(self):
        self.assertHolidays(
            GuineaBissau(years=2024),
            ("2024-01-01", "Ano Novo"),
            ("2024-01-20", "Dia dos Heróis Nacionais"),
            ("2024-03-08", "Dia Internacional da Mulher"),
            ("2024-03-29", "Sexta-feira Santa"),
            ("2024-03-31", "Páscoa"),
            ("2024-04-10", "Korité"),
            ("2024-05-01", "Dia do Trabalhador"),
            ("2024-06-16", "Tabaski"),
            ("2024-09-24", "Dia da Independência"),
            ("2024-11-02", "Dia dos Finados"),
            ("2024-12-24", "Véspera de Natal"),
            ("2024-12-25", "Dia de Natal"),
            ("2024-12-31", "Véspera de Ano Novo"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Ano Novo"),
            ("2025-01-20", "Dia dos Heróis Nacionais"),
            ("2025-03-08", "Dia Internacional da Mulher"),
            ("2025-03-30", "Korité"),
            ("2025-04-18", "Sexta-feira Santa"),
            ("2025-04-20", "Páscoa"),
            ("2025-05-01", "Dia do Trabalhador"),
            ("2025-06-06", "Tabaski"),
            ("2025-09-24", "Dia da Independência"),
            ("2025-11-02", "Dia dos Finados"),
            ("2025-12-24", "Véspera de Natal"),
            ("2025-12-25", "Dia de Natal"),
            ("2025-12-31", "Véspera de Ano Novo"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-20", "National Heroes' Day"),
            ("2025-03-08", "International Women's Day"),
            ("2025-03-30", "Eid al-Fitr"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-20", "Easter Sunday"),
            ("2025-05-01", "Labor Day"),
            ("2025-06-06", "Eid al-Adha"),
            ("2025-09-24", "Independence Day"),
            ("2025-11-02", "All Souls' Day"),
            ("2025-12-24", "Christmas Eve"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-31", "New Year's Eve"),
        )
