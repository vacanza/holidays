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

from datetime import date
from unittest import TestCase

from holidays.financial.brasil_bolsa_balcao import BrasilBolsaBalcao
from tests.common import CommonFinancialTests


class TestBrasilBolsaBalcao(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BrasilBolsaBalcao)

    def test_universal_fraternization_day(self):
        name = "Confraternização Universal"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))

    def test_carnival(self):
        name = "Carnaval"
        self.assertHolidayName(
            name,
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
        self.assertHolidayNameCount(name, 2, self.full_range)

    def test_holy_thursday(self):
        name = "Quinta-feira Santa"
        self.assertHolidayName(
            name,
            "1995-04-13",
            "1996-04-04",
            "1997-03-27",
            "1998-04-09",
            "1999-04-01",
        )
        self.assertHolidayName(name, range(self.start_year, 2000))
        self.assertNoHolidayName(name, range(2000, self.end_year))

    def test_good_friday(self):
        name = "Sexta-feira Santa"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
        )
        self.assertHolidayName(name, self.full_range)

    def test_tiradentes_day(self):
        name = "Tiradentes"
        years_absent = {1931, 1932}
        self.assertHolidayName(
            name, (f"{year}-04-21" for year in self.full_range if year not in years_absent)
        )
        self.assertNoHolidayName(name, years_absent)

    def test_workers_day(self):
        name = "Dia do Trabalhador"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1925, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1925))

    def test_corpus_christi_day(self):
        name = "Corpus Christi"
        self.assertHolidayName(
            name,
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
        )
        self.assertHolidayName(name, self.full_range)

    def test_independence_day(self):
        name = "Independência do Brasil"
        self.assertHolidayName(name, (f"{year}-09-07" for year in self.full_range))

    def test_our_lady_of_aparecida(self):
        name = "Nossa Senhora Aparecida"
        self.assertHolidayName(name, (f"{year}-10-12" for year in range(1980, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1980))

    def test_all_souls_day(self):
        name = "Finados"
        self.assertHolidayName(name, (f"{year}-11-02" for year in self.full_range))

    def test_republic_proclamation_day(self):
        name = "Proclamação da República"
        self.assertHolidayName(name, (f"{year}-11-15" for year in self.full_range))

    def test_national_day_of_zumbi_and_black_awareness(self):
        name = "Dia Nacional de Zumbi e da Consciência Negra"
        self.assertHolidayName(name, (f"{year}-11-20" for year in range(2024, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2024))

    def test_christmas_eve(self):
        name = "Véspera de Natal"
        self.assertHolidayName(name, (f"{year}-12-24" for year in range(2019, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2019))

    def test_christmas_day(self):
        name = "Natal"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1922, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1922))

    def test_new_years_eve(self):
        name = "Véspera de Ano-Novo"
        self.assertHolidayName(name, (f"{year}-12-31" for year in range(2019, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2019))

    def test_2022(self):
        self.assertHolidays(
            BrasilBolsaBalcao(years=2022),
            ("2022-01-01", "Confraternização Universal"),
            ("2022-02-28", "Carnaval"),
            ("2022-03-01", "Carnaval"),
            ("2022-04-15", "Sexta-feira Santa"),
            ("2022-04-21", "Tiradentes"),
            ("2022-05-01", "Dia do Trabalhador"),
            ("2022-06-16", "Corpus Christi"),
            ("2022-09-07", "Independência do Brasil"),
            ("2022-10-12", "Nossa Senhora Aparecida"),
            ("2022-11-02", "Finados"),
            ("2022-11-15", "Proclamação da República"),
            ("2022-12-24", "Véspera de Natal"),
            ("2022-12-25", "Natal"),
            ("2022-12-31", "Véspera de Ano-Novo"),
        )

    def test_2026(self):
        # https://www.b3.com.br/pt_br/noticias/calendario-de-negociacao-da-b3-confira-o-funcionamento-da-bolsa-em-2026.htm
        self.assertHolidays(
            BrasilBolsaBalcao(years=2026),
            ("2026-01-01", "Confraternização Universal"),
            ("2026-02-16", "Carnaval"),
            ("2026-02-17", "Carnaval"),
            ("2026-04-03", "Sexta-feira Santa"),
            ("2026-04-21", "Tiradentes"),
            ("2026-05-01", "Dia do Trabalhador"),
            ("2026-06-04", "Corpus Christi"),
            ("2026-09-07", "Independência do Brasil"),
            ("2026-10-12", "Nossa Senhora Aparecida"),
            ("2026-11-02", "Finados"),
            ("2026-11-15", "Proclamação da República"),
            ("2026-11-20", "Dia Nacional de Zumbi e da Consciência Negra"),
            ("2026-12-24", "Véspera de Natal"),
            ("2026-12-25", "Natal"),
            ("2026-12-31", "Véspera de Ano-Novo"),
        )

    def test_working_days_around_new_year(self):
        holidays = BrasilBolsaBalcao(years=2026)
        self.assertEqual(holidays.get_nth_working_day("2026-12-23", 1), date(2026, 12, 28))
        self.assertEqual(holidays.get_working_days_count("2026-12-21", "2026-12-31"), 6)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Confraternização Universal"),
            ("2023-02-20", "Carnaval"),
            ("2023-02-21", "Carnaval"),
            ("2023-04-07", "Sexta-feira Santa"),
            ("2023-04-21", "Tiradentes"),
            ("2023-05-01", "Dia do Trabalhador"),
            ("2023-06-08", "Corpus Christi"),
            ("2023-09-07", "Independência do Brasil"),
            ("2023-10-12", "Nossa Senhora Aparecida"),
            ("2023-11-02", "Finados"),
            ("2023-11-15", "Proclamação da República"),
            ("2023-12-24", "Véspera de Natal"),
            ("2023-12-25", "Natal"),
            ("2023-12-31", "Véspera de Ano-Novo"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "Universal Fraternization Day"),
            ("2023-02-20", "Carnival"),
            ("2023-02-21", "Carnival"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-21", "Tiradentes' Day"),
            ("2023-05-01", "Worker's Day"),
            ("2023-06-08", "Corpus Christi"),
            ("2023-09-07", "Independence Day"),
            ("2023-10-12", "Our Lady of Aparecida"),
            ("2023-11-02", "All Souls' Day"),
            ("2023-11-15", "Republic Proclamation Day"),
            ("2023-12-24", "Christmas Eve"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-31", "New Year's Eve"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2023-01-01", "День всесвітнього братання"),
            ("2023-02-20", "Карнавал"),
            ("2023-02-21", "Карнавал"),
            ("2023-04-07", "Страсна пʼятниця"),
            ("2023-04-21", "День Тирадентіса"),
            ("2023-05-01", "День трудящих"),
            ("2023-06-08", "Свято Тіла і Крові Христових"),
            ("2023-09-07", "День незалежності Бразилії"),
            ("2023-10-12", "День Богоматері Апаресіди"),
            ("2023-11-02", "День усіх померлих"),
            ("2023-11-15", "День проголошення республіки"),
            ("2023-12-24", "Святий вечір"),
            ("2023-12-25", "Різдво Христове"),
            ("2023-12-31", "Переддень Нового року"),
        )
