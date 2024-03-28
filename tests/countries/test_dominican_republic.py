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

from holidays.countries.dominican_republic import DominicanRepublic, DO, DOM
from tests.common import CommonCountryTests


class TestDominicanRepublic(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(DominicanRepublic)

    def test_country_aliases(self):
        self.assertAliases(DominicanRepublic, DO, DOM)

    def test_2020(self):
        self.assertHolidays(
            ("2020-01-01", "Año Nuevo"),
            ("2020-01-06", "Día de los Santos Reyes"),
            ("2020-01-21", "Día de la Altagracia"),
            ("2020-01-26", "Día de Duarte"),
            ("2020-02-27", "Día de Independencia"),
            ("2020-04-10", "Viernes Santo"),
            ("2020-05-04", "Día del Trabajo"),
            ("2020-06-11", "Corpus Christi"),
            ("2020-08-16", "Día de la Restauración"),
            ("2020-09-24", "Día de las Mercedes"),
            ("2020-11-09", "Día de la Constitución"),
            ("2020-12-25", "Día de Navidad"),
        )

    def test_2021(self):
        self.assertHolidays(
            ("2021-01-01", "Año Nuevo"),
            ("2021-01-04", "Día de los Santos Reyes"),
            ("2021-01-21", "Día de la Altagracia"),
            ("2021-01-25", "Día de Duarte"),
            ("2021-02-27", "Día de Independencia"),
            ("2021-04-02", "Viernes Santo"),
            ("2021-05-01", "Día del Trabajo"),
            ("2021-06-03", "Corpus Christi"),
            ("2021-08-16", "Día de la Restauración"),
            ("2021-09-24", "Día de las Mercedes"),
            ("2021-11-06", "Día de la Constitución"),
            ("2021-12-25", "Día de Navidad"),
        )

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-01-10", "Día de los Santos Reyes"),
            ("2022-01-21", "Día de la Altagracia"),
            ("2022-01-24", "Día de Duarte"),
            ("2022-02-27", "Día de Independencia"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-02", "Día del Trabajo"),
            ("2022-06-16", "Corpus Christi"),
            ("2022-08-15", "Día de la Restauración"),
            ("2022-09-24", "Día de las Mercedes"),
            ("2022-11-06", "Día de la Constitución"),
            ("2022-12-25", "Día de Navidad"),
        )

    def test_movable(self):
        self.assertHoliday(
            "1996-01-06",
            "1997-01-06",
            "1998-01-05",
            "1998-01-26",
            "1999-01-25",
            "1996-05-01",
            "1998-05-04",
            "1996-11-06",
            "1997-11-10",
            "2000-08-16",
            "2001-08-20",
        )

        self.assertNoHoliday(
            "1998-01-06",
            "1999-01-26",
            "1998-05-01",
            "1997-11-06",
            "2001-08-16",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-01-10", "Día de los Santos Reyes"),
            ("2022-01-21", "Día de la Altagracia"),
            ("2022-01-24", "Día de Duarte"),
            ("2022-02-27", "Día de Independencia"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-02", "Día del Trabajo"),
            ("2022-06-16", "Corpus Christi"),
            ("2022-08-15", "Día de la Restauración"),
            ("2022-09-24", "Día de las Mercedes"),
            ("2022-11-06", "Día de la Constitución"),
            ("2022-12-25", "Día de Navidad"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-10", "Epiphany"),
            ("2022-01-21", "Lady of Altagracia"),
            ("2022-01-24", "Juan Pablo Duarte Day"),
            ("2022-02-27", "Independence Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-02", "Labor Day"),
            ("2022-06-16", "Corpus Christi"),
            ("2022-08-15", "Restoration Day"),
            ("2022-09-24", "Our Lady of Mercedes Day"),
            ("2022-11-06", "Constitution Day"),
            ("2022-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-10", "Богоявлення"),
            ("2022-01-21", "День Богоматері Альтаграсія"),
            ("2022-01-24", "День Дуарте"),
            ("2022-02-27", "День незалежності"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-05-02", "День праці"),
            ("2022-06-16", "Свято Тіла і Крові Христових"),
            ("2022-08-15", "День реставрації"),
            ("2022-09-24", "День Богоматері Милосердя"),
            ("2022-11-06", "День Конституції"),
            ("2022-12-25", "Різдво Христове"),
        )
