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

from holidays.countries.angola import Angola, AO, AGO
from tests.common import CommonCountryTests


class TestAngola(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Angola, years=range(1975, 2050), years_non_observed=range(2000, 2030))

    def test_country_aliases(self):
        self.assertAliases(Angola, AO, AGO)

    def test_no_holidays(self):
        self.assertNoHolidays(Angola(years=1974))

    def test_special_holidays(self):
        self.assertHoliday("2017-08-23")

    def test_new_years_day(self):
        name = "Dia do Ano Novo"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(1975, 2050)))
        obs_dt = (
            "2006-01-02",
            "2018-12-31",
            "2026-01-02",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_martyrs_of_colonial_repression_day(self):
        name = "Dia dos Mártires da Repressão Colonial"
        self.assertHolidayName(name, (f"{year}-01-04" for year in range(1997, 2012)))
        self.assertNoHoliday(f"{year}-01-04" for year in range(1975, 1997))
        self.assertNoHoliday(f"{year}-01-04" for year in range(2012, 2050))
        self.assertNoHolidayName(name, range(1975, 1997), range(2012, 2050))
        obs_dt = (
            "2004-01-05",
            "2009-01-05",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_armed_struggle_day(self):
        name_1 = "Dia do Início da Luta Armada"
        name_2 = "Dia do Início da Luta Armada de Libertação Nacional"
        self.assertHolidayName(name_1, (f"{year}-02-04" for year in range(1975, 2012)))
        self.assertHolidayName(name_2, (f"{year}-02-04" for year in range(2012, 2050)))
        self.assertNoHolidayName(name_1, range(2012, 2050))
        self.assertNoHolidayName(name_2, range(1975, 2012))
        obs_dt = (
            "2001-02-05",
            "2007-02-05",
        )
        self.assertHolidayName(f"{name_1} (ponte)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        obs_dt = (
            "2018-02-05",
            "2020-02-03",
            "2021-02-05",
            "2025-02-03",
        )
        self.assertHolidayName(f"{name_2} (ponte)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_carnival_day(self):
        name = "Dia do Carnaval"
        self.assertHolidayName(
            name,
            "1997-02-11",
            "2000-03-07",
            "2010-02-16",
            "2018-02-13",
            "2019-03-05",
            "2020-02-25",
            "2021-02-16",
            "2022-03-01",
            "2023-02-21",
        )
        self.assertHolidayName(name, range(1997, 2050))
        self.assertNoHolidayName(name, range(1975, 1997))

        obs_dt = (
            "2019-03-04",
            "2020-02-24",
            "2021-02-15",
            "2022-02-28",
            "2023-02-20",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_international_womens_day(self):
        name = "Dia Internacional da Mulher"
        self.assertHolidayName(name, (f"{year}-03-08" for year in range(1997, 2050)))
        self.assertNoHoliday(f"{year}-03-08" for year in range(1975, 1997))
        self.assertNoHolidayName(name, range(1975, 1997))
        obs_dt = (
            "2009-03-09",
            "2015-03-09",
            "2022-03-07",
            "2029-03-09",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_southern_africa_liberation_day(self):
        name = "Dia da Libertação da África Austral"
        self.assertHolidayName(name, (f"{year}-03-23" for year in range(2019, 2050)))
        self.assertNoHoliday(f"{year}-03-23" for year in range(1975, 2019))
        self.assertNoHolidayName(name, range(1975, 2019))
        obs_dt = (
            "2021-03-22",
            "2023-03-24",
            "2027-03-22",
            "2028-03-24",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_peace_and_national_reconciliation_day(self):
        name = "Dia da Paz e Reconciliação Nacional"
        self.assertHolidayName(name, (f"{year}-04-04" for year in range(2003, 2050)))
        self.assertNoHoliday(f"{year}-04-04" for year in range(1975, 2003))
        self.assertNoHolidayName(name, range(1975, 2003))
        obs_dt = (
            "2004-04-05",
            "2010-04-05",
            "2019-04-05",
            "2023-04-03",
            "2024-04-05",
            "2028-04-03",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_good_friday(self):
        name = "Sexta-Feira Santa"
        self.assertHolidayName(
            name,
            "1997-03-28",
            "2000-04-21",
            "2010-04-02",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )
        self.assertHolidayName(name, range(1997, 2050))
        self.assertNoHolidayName(name, range(1975, 1997))

    def test_international_workers_day(self):
        name = "Dia Internacional do Trabalhador"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1975, 2050)))
        obs_dt = (
            "2005-05-02",
            "2011-05-02",
            "2016-05-02",
            "2025-05-02",
            "2029-04-30",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_africa_day(self):
        name = "Dia da África"
        self.assertHolidayName(name, (f"{year}-05-25" for year in range(2001, 2011)))
        self.assertNoHoliday(f"{year}-05-25" for year in range(1975, 2001))
        self.assertNoHoliday(f"{year}-05-25" for year in range(2011, 2050))
        self.assertNoHolidayName(name, range(1975, 2001), range(2011, 2050))
        obs_dt = (
            "2003-05-26",
            "2008-05-26",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_international_childrens_day(self):
        name = "Dia Internacional da Criança"
        self.assertHolidayName(name, (f"{year}-06-01" for year in range(1997, 2011)))
        self.assertNoHoliday(f"{year}-06-01" for year in range(1975, 1997))
        self.assertNoHoliday(f"{year}-06-01" for year in range(2011, 2050))
        self.assertNoHolidayName(name, range(1975, 1997), range(2011, 2050))
        obs_dt = (
            "2003-06-02",
            "2008-06-02",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_national_heroes_day(self):
        name = "Dia do Fundador da Nação e do Herói Nacional"
        self.assertHolidayName(name, (f"{year}-09-17" for year in range(1980, 2050)))
        self.assertNoHoliday(f"{year}-09-17" for year in range(1975, 1980))
        self.assertNoHolidayName(name, range(1975, 1980))
        obs_dt = (
            "2000-09-18",
            "2006-09-18",
            "2017-09-18",
            "2019-09-16",
            "2020-09-18",
            "2024-09-16",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_all_souls_day(self):
        name = "Dia dos Finados"
        self.assertHolidayName(name, (f"{year}-11-02" for year in range(1975, 2050)))
        obs_dt = (
            "2003-11-03",
            "2008-11-03",
            "2021-11-01",
            "2023-11-03",
            "2027-11-01",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_national_independence_day(self):
        name_1 = "Dia da Independência"
        name_2 = "Dia da Independência Nacional"
        self.assertHolidayName(name_1, (f"{year}-11-11" for year in range(1975, 1996)))
        self.assertHolidayName(name_2, (f"{year}-11-11" for year in range(1996, 2050)))
        self.assertNoHolidayName(name_1, range(1996, 2050))
        self.assertNoHolidayName(name_2, range(1975, 1996))
        obs_dt = (
            "2001-11-12",
            "2007-11-12",
            "2012-11-12",
            "2021-11-12",
            "2025-11-10",
        )
        self.assertHolidayName(f"{name_2} (ponte)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_date_of_founding_of_mpla(self):
        name = "Data da Fundacao do MPLA - Partido do Trabalho"
        self.assertHolidayName(name, (f"{year}-12-10" for year in range(1975, 1992)))
        self.assertNoHoliday(f"{year}-12-10" for year in range(1992, 2050))
        self.assertNoHolidayName(name, range(1992, 2050))

    def test_christmas_and_family_day(self):
        name_1 = "Dia da Família"
        name_2 = "Dia do Natal"
        name_3 = "Dia de Natal e da Família"
        self.assertHolidayName(name_1, (f"{year}-12-25" for year in range(1975, 1996)))
        self.assertHolidayName(name_2, (f"{year}-12-25" for year in range(1996, 2011)))
        self.assertHolidayName(name_3, (f"{year}-12-25" for year in range(2011, 2050)))
        self.assertNoHolidayName(name_1, range(1996, 2050))
        self.assertNoHolidayName(name_2, range(1975, 1996), range(2011, 2050))
        self.assertNoHolidayName(name_3, range(1996, 2011))

        obs_dt = ("2005-12-26",)
        self.assertHolidayName(f"{name_2} (ponte)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        obs_dt = (
            "2018-12-24",
            "2025-12-26",
            "2029-12-24",
        )
        self.assertHolidayName(f"{name_3} (ponte)", obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_2022(self):
        self.assertHolidays(
            Angola(years=2022),
            ("2022-01-01", "Dia do Ano Novo"),
            ("2022-02-04", "Dia do Início da Luta Armada de Libertação Nacional"),
            ("2022-02-28", "Dia do Carnaval (ponte)"),
            ("2022-03-01", "Dia do Carnaval"),
            ("2022-03-07", "Dia Internacional da Mulher (ponte)"),
            ("2022-03-08", "Dia Internacional da Mulher"),
            ("2022-03-23", "Dia da Libertação da África Austral"),
            ("2022-04-04", "Dia da Paz e Reconciliação Nacional"),
            ("2022-04-15", "Sexta-Feira Santa"),
            ("2022-05-01", "Dia Internacional do Trabalhador"),
            ("2022-09-17", "Dia do Fundador da Nação e do Herói Nacional"),
            ("2022-11-02", "Dia dos Finados"),
            ("2022-11-11", "Dia da Independência Nacional"),
            ("2022-12-25", "Dia de Natal e da Família"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Dia do Ano Novo"),
            ("2023-02-04", "Dia do Início da Luta Armada de Libertação Nacional"),
            ("2023-02-20", "Dia do Carnaval (ponte)"),
            ("2023-02-21", "Dia do Carnaval"),
            ("2023-03-08", "Dia Internacional da Mulher"),
            ("2023-03-23", "Dia da Libertação da África Austral"),
            ("2023-03-24", "Dia da Libertação da África Austral (ponte)"),
            ("2023-04-03", "Dia da Paz e Reconciliação Nacional (ponte)"),
            ("2023-04-04", "Dia da Paz e Reconciliação Nacional"),
            ("2023-04-07", "Sexta-Feira Santa"),
            ("2023-05-01", "Dia Internacional do Trabalhador"),
            ("2023-09-17", "Dia do Fundador da Nação e do Herói Nacional"),
            ("2023-11-02", "Dia dos Finados"),
            ("2023-11-03", "Dia dos Finados (ponte)"),
            ("2023-11-11", "Dia da Independência Nacional"),
            ("2023-12-25", "Dia de Natal e da Família"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-02-04", "Liberation Movement Day"),
            ("2023-02-20", "Day off for Carnival Day"),
            ("2023-02-21", "Carnival Day"),
            ("2023-03-08", "International Women's Day"),
            ("2023-03-23", "Southern Africa Liberation Day"),
            ("2023-03-24", "Day off for Southern Africa Liberation Day"),
            ("2023-04-03", "Day off for Peace and National Reconciliation Day"),
            ("2023-04-04", "Peace and National Reconciliation Day"),
            ("2023-04-07", "Good Friday"),
            ("2023-05-01", "International Worker's Day"),
            ("2023-09-17", "National Heroes' Day"),
            ("2023-11-02", "All Souls' Day"),
            ("2023-11-03", "Day off for All Souls' Day"),
            ("2023-11-11", "National Independence Day"),
            ("2023-12-25", "Christmas and Family Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2023-01-01", "Новий рік"),
            ("2023-02-04", "День початку збройної боротьби за національне визволення"),
            ("2023-02-20", "Вихідний за Карнавал"),
            ("2023-02-21", "Карнавал"),
            ("2023-03-08", "Міжнародний жіночий день"),
            ("2023-03-23", "День визволення південної Африки"),
            ("2023-03-24", "Вихідний за День визволення південної Африки"),
            ("2023-04-03", "Вихідний за День миру та національного примирення"),
            ("2023-04-04", "День миру та національного примирення"),
            ("2023-04-07", "Страсна пʼятниця"),
            ("2023-05-01", "Міжнародний день трудящих"),
            ("2023-09-17", "День засновника нації та національного героя"),
            ("2023-11-02", "День усіх померлих"),
            ("2023-11-03", "Вихідний за День усіх померлих"),
            ("2023-11-11", "День національної незалежності"),
            ("2023-12-25", "Різдво Христове та День родини"),
        )
