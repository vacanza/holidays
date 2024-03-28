#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.mozambique import Mozambique, MZ, MOZ
from tests.common import CommonCountryTests


class TestMozambique(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Mozambique, years=range(1975, 2050))

    def test_country_aliases(self):
        self.assertAliases(Mozambique, MZ, MOZ)

    def test_no_holidays(self):
        self.assertNoHolidays(Mozambique(years=1974))

    def test_holidays(self):
        for year in range(1975, 2050):
            self.assertHoliday(
                f"{year}-01-01",
                f"{year}-02-03",
                f"{year}-04-07",
                f"{year}-05-01",
                f"{year}-06-25",
                f"{year}-09-07",
                f"{year}-09-25",
                f"{year}-12-25",
            )

        self.assertNoHoliday(f"{year}-10-04" for year in range(1975, 1993))
        self.assertNoHolidayName("Dia da Paz e Reconciliação", range(1975, 1993))
        self.assertHoliday(f"{year}-10-04" for year in range(1993, 2050))

    def test_observed(self):
        dt = (
            "2011-05-02",
            "2011-09-26",
            "2011-12-26",
            "2012-01-02",
            "2013-02-04",
            "2013-04-08",
            "2014-09-08",
            "2015-10-05",
            "2016-05-02",
            "2016-09-26",
            "2016-12-26",
            "2017-01-02",
            "2017-06-26",
            "2019-02-04",
            "2019-04-08",
            "2020-10-05",
            "2022-05-02",
            "2022-09-26",
            "2022-12-26",
            "2023-01-02",
            "2023-06-26",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

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
            ("2023-09-07", "День перемоги"),
            ("2023-09-25", "День Збройних сил національного визволення"),
            ("2023-10-04", "День миру та примирення"),
            ("2023-12-25", "День родини"),
        )
