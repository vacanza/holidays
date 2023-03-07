#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.countries.dominican_republic import DominicanRepublic, DO, DOM
from tests.common import TestCase


class TestDominicanRepublic(TestCase):
    def setUp(self):
        self.holidays = DominicanRepublic()

    def test_country_aliases(self):
        self.assertCountryAliases(DominicanRepublic, DO, DOM)

    def test_2020(self):
        self.assertHolidays(
            ("2020-01-01", "Año Nuevo [New Year's Day]"),
            ("2020-01-06", "Día de los Santos Reyes [Epiphany]"),
            ("2020-01-21", "Día de la Altagracia [Lady of Altagracia]"),
            ("2020-01-26", "Día de Duarte [Juan Pablo Duarte Day]"),
            ("2020-02-27", "Día de Independencia [Independence Day]"),
            ("2020-04-10", "Viernes Santo [Good Friday]"),
            ("2020-05-04", "Día del Trabajo [Labor Day]"),
            ("2020-06-11", "Corpus Christi [Feast of Corpus Christi]"),
            ("2020-08-16", "Día de la Restauración [Restoration Day]"),
            ("2020-09-24", "Día de las Mercedes [Our Lady of Mercedes Day]"),
            ("2020-11-09", "Día de la Constitución [Constitution Day]"),
            ("2020-12-25", "Día de Navidad [Christmas Day]"),
        )

    def test_2021(self):
        self.assertHolidays(
            ("2021-01-01", "Año Nuevo [New Year's Day]"),
            ("2021-01-04", "Día de los Santos Reyes [Epiphany]"),
            ("2021-01-21", "Día de la Altagracia [Lady of Altagracia]"),
            ("2021-01-25", "Día de Duarte [Juan Pablo Duarte Day]"),
            ("2021-02-27", "Día de Independencia [Independence Day]"),
            ("2021-04-02", "Viernes Santo [Good Friday]"),
            ("2021-05-01", "Día del Trabajo [Labor Day]"),
            ("2021-06-03", "Corpus Christi [Feast of Corpus Christi]"),
            ("2021-08-16", "Día de la Restauración [Restoration Day]"),
            ("2021-09-24", "Día de las Mercedes [Our Lady of Mercedes Day]"),
            ("2021-11-06", "Día de la Constitución [Constitution Day]"),
            ("2021-12-25", "Día de Navidad [Christmas Day]"),
        )

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "Año Nuevo [New Year's Day]"),
            ("2022-01-10", "Día de los Santos Reyes [Epiphany]"),
            ("2022-01-21", "Día de la Altagracia [Lady of Altagracia]"),
            ("2022-01-24", "Día de Duarte [Juan Pablo Duarte Day]"),
            ("2022-02-27", "Día de Independencia [Independence Day]"),
            ("2022-04-15", "Viernes Santo [Good Friday]"),
            ("2022-05-02", "Día del Trabajo [Labor Day]"),
            ("2022-06-16", "Corpus Christi [Feast of Corpus Christi]"),
            ("2022-08-15", "Día de la Restauración [Restoration Day]"),
            ("2022-09-24", "Día de las Mercedes [Our Lady of Mercedes Day]"),
            ("2022-11-06", "Día de la Constitución [Constitution Day]"),
            ("2022-12-25", "Día de Navidad [Christmas Day]"),
        )

    def test_change_day_by_law(self):
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
