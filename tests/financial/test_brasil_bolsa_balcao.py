#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.financial.brasil_bolsa_balcao import BrasilBolsaBalcao, BVMF, B3
from tests.common import CommonFinancialTests


class TestBrasilBolsaBalcao(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BrasilBolsaBalcao, years=range(1890, 2100))

    def test_market_aliases(self):
        self.assertAliases(BrasilBolsaBalcao, BVMF, B3)

    def test_no_holidays(self):
        self.assertNoHolidays(BrasilBolsaBalcao(years=1889))

    def test_universal_fraternization_day(self):
        name = "Confraternização Universal"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1890, 2100)))

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
        self.assertHolidayName(name, range(1890, 2100))

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
        self.assertHolidayName(name, range(1890, 2000))
        self.assertNoHolidayName(name, range(2000, 2100))

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
        self.assertHolidayName(name, range(1890, 2100))

    def test_tiradentes_day(self):
        name = "Tiradentes"
        self.assertHolidayName(
            name, (f"{year}-04-21" for year in set(range(1890, 2100)).difference({1931, 1932}))
        )
        self.assertNoHolidayName(name, {1931, 1932})

    def test_workers_day(self):
        name = "Dia do Trabalhador"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1925, 2100)))
        self.assertNoHolidayName(name, range(1890, 1925))

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
        self.assertHolidayName(name, range(1890, 2100))

    def test_independence_day(self):
        name = "Independência do Brasil"
        self.assertHolidayName(name, (f"{year}-09-07" for year in range(1890, 2100)))

    def test_our_lady_of_aparecida(self):
        name = "Nossa Senhora Aparecida"
        self.assertHolidayName(name, (f"{year}-10-12" for year in range(1980, 2100)))
        self.assertNoHolidayName(name, range(1890, 1980))

    def test_all_souls_day(self):
        name = "Finados"
        self.assertHolidayName(name, (f"{year}-11-02" for year in range(1890, 2100)))

    def test_republic_proclamation_day(self):
        name = "Proclamação da República"
        self.assertHolidayName(name, (f"{year}-11-15" for year in range(1890, 2100)))

    def test_national_day_of_zumbi_and_black_awareness(self):
        name = "Dia Nacional de Zumbi e da Consciência Negra"
        self.assertHolidayName(name, (f"{year}-11-20" for year in range(2024, 2100)))
        self.assertNoHolidayName(name, range(1890, 2024))

    def test_christmas_day(self):
        name = "Natal"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1922, 2100)))
        self.assertNoHolidayName(name, range(1890, 1922))

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
            ("2022-12-25", "Natal"),
        )

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
            ("2023-12-25", "Natal"),
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
            ("2023-12-25", "Christmas Day"),
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
            ("2023-12-25", "Різдво Христове"),
        )
