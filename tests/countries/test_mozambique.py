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

from holidays.countries.mozambique import Mozambique
from tests.common import CommonCountryTests


class TestMozambique(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Mozambique)

    def test_new_years_day(self):
        name = "Dia da Fraternidade universal"
        self.assertHolidayName(name, (f"{year}-01-01" for year in self.full_range))
        obs_dts = (
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_heroes_day(self):
        name = "Dia dos Heróis Moçambicanos"
        self.assertHolidayName(
            name,
            (f"{year}-02-03" for year in self.full_range),
        )
        obs_dts = (
            "2013-02-04",
            "2019-02-04",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_womens_day(self):
        name = "Dia da Mulher Moçambicana"
        self.assertHolidayName(
            name,
            (f"{year}-04-07" for year in self.full_range),
        )
        obs_dts = (
            "2013-04-08",
            "2019-04-08",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_workers_day(self):
        name = "Dia Internacional dos Trabalhadores"
        self.assertHolidayName(
            name,
            (f"{year}-05-01" for year in self.full_range),
        )
        obs_dts = (
            "2011-05-02",
            "2016-05-02",
            "2022-05-02",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_independence_day(self):
        name = "Dia da Independência Nacional"
        self.assertHolidayName(
            name,
            (f"{year}-06-25" for year in self.full_range),
        )
        obs_dts = (
            "2017-06-26",
            "2023-06-26",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_victory_day(self):
        name = "Dia da Vitória"
        self.assertHolidayName(
            name,
            (f"{year}-09-07" for year in self.full_range),
        )
        obs_dts = (
            "2014-09-08",
            "2025-09-08",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_armed_forces_day(self):
        name = "Dia das Forças Armadas de Libertação Nacional"
        self.assertHolidayName(
            name,
            (f"{year}-09-25" for year in self.full_range),
        )
        obs_dts = (
            "2011-09-26",
            "2016-09-26",
            "2022-09-26",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_peace_and_reconciliation_day(self):
        name = "Dia da Paz e Reconciliação"
        self.assertHolidayName(
            name,
            (f"{year}-10-04" for year in range(1993, self.end_year)),
        )
        self.assertNoHolidayName(name, range(self.start_year, 1993))
        obs_dts = (
            "2015-10-05",
            "2020-10-05",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_family_day(self):
        name = "Dia da Família"
        self.assertHolidayName(
            name,
            (f"{year}-12-25" for year in self.full_range),
        )
        obs_dts = (
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
        )
        self.assertHolidayName(f"{name} (ponte)", obs_dts)
        self.assertNoNonObservedHoliday(obs_dts)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Dia da Fraternidade universal"),
            ("2023-01-02", "Dia da Fraternidade universal (ponte)"),
            ("2023-02-03", "Dia dos Heróis Moçambicanos"),
            ("2023-04-07", "Dia da Mulher Moçambicana"),
            ("2023-05-01", "Dia Internacional dos Trabalhadores"),
            ("2023-06-25", "Dia da Independência Nacional"),
            ("2023-06-26", "Dia da Independência Nacional (ponte)"),
            ("2023-09-07", "Dia da Vitória"),
            ("2023-09-25", "Dia das Forças Armadas de Libertação Nacional"),
            ("2023-10-04", "Dia da Paz e Reconciliação"),
            ("2023-12-25", "Dia da Família"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "International Fraternalism Day"),
            ("2023-01-02", "International Fraternalism Day (observed)"),
            ("2023-02-03", "Heroes' Day"),
            ("2023-04-07", "Women's Day"),
            ("2023-05-01", "International Workers' Day"),
            ("2023-06-25", "Independence Day"),
            ("2023-06-26", "Independence Day (observed)"),
            ("2023-09-07", "Victory Day"),
            ("2023-09-25", "Armed Forces Day"),
            ("2023-10-04", "Peace and Reconciliation Day"),
            ("2023-12-25", "Family Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2023-01-01", "День всесвітнього братерства"),
            ("2023-01-02", "День всесвітнього братерства (вихідний)"),
            ("2023-02-03", "День героїв Мозамбіку"),
            ("2023-04-07", "День жінок Мозамбіку"),
            ("2023-05-01", "Міжнародний день трудящих"),
            ("2023-06-25", "День національної незалежності"),
            ("2023-06-26", "День національної незалежності (вихідний)"),
            ("2023-09-07", "День Перемоги"),
            ("2023-09-25", "День Збройних сил національного визволення"),
            ("2023-10-04", "День миру та примирення"),
            ("2023-12-25", "День родини"),
        )
