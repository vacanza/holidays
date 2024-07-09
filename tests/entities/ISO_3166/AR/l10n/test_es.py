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

from holidays.entities.ISO_3166.AR import ArHolidays
from tests.common import CommonCountryTests


class TestArHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ArHolidays)

    def test_es(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-02-28", "Día de Carnaval"),
            ("2022-03-01", "Día de Carnaval"),
            ("2022-03-24", "Día Nacional de la Memoria por la Verdad y la Justicia"),
            ("2022-04-02", "Día del Veterano y de los Caidos en la Guerra de Malvinas"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-05-18", "Censo nacional 2022"),
            ("2022-05-25", "Día de la Revolución de Mayo"),
            ("2022-06-17", "Paso a la Inmortalidad del General Don Martín Miguel de Güemes"),
            ("2022-06-20", "Paso a la Inmortalidad del General Don Manuel Belgrano"),
            ("2022-07-09", "Día de la Independencia"),
            (
                "2022-08-15",
                "Paso a la Inmortalidad del General Don José de San Martin (observado)",
            ),
            ("2022-10-07", "Feriado con fines turísticos"),
            ("2022-10-10", "Día del Respeto a la Diversidad Cultural (observado)"),
            ("2022-11-20", "Día de la Soberanía Nacional"),
            ("2022-11-21", "Feriado con fines turísticos"),
            ("2022-12-08", "Inmaculada Concepción de María"),
            ("2022-12-09", "Feriado con fines turísticos"),
            ("2022-12-25", "Navidad"),
        )
