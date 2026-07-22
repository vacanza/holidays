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

from holidays.financial.bolsas_y_mercados_argentinos import BolsasYMercadosArgentinos
from tests.common import CommonFinancialTests


class TestBolsasYMercadosArgentinos(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BolsasYMercadosArgentinos)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_restricted_settlement(self):
        self.assertRestrictedSettlementHolidaysInYear(
            2026,
            ("2026-01-19", "Sin liquidación cable"),
            ("2026-03-23", "Sin liquidación local"),
            ("2026-06-19", "Sin liquidación cable"),
            ("2026-07-10", "Sin liquidación local"),
            ("2026-09-07", "Sin liquidación cable"),
            ("2026-11-11", "Sin liquidación cable"),
            ("2026-11-26", "Sin liquidación cable"),
            ("2026-12-07", "Sin liquidación local"),
            ("2026-12-24", "Sin liquidación local"),
        )

    def test_half_day(self):
        self.assertHalfDayHolidaysInYear(
            2026,
            ("2026-12-24", "Nochebuena (el mercado cierra a las 15:00)"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2026-01-01", "Año Nuevo"),
            ("2026-01-19", "Sin liquidación cable"),
            ("2026-02-16", "Lunes de Carnaval"),
            ("2026-02-17", "Martes de Carnaval"),
            ("2026-03-23", "Sin liquidación local"),
            ("2026-03-24", "Día Nacional de la Memoria por la Verdad y la Justicia"),
            (
                "2026-04-02",
                "Día del Veterano y de los Caidos en la Guerra de Malvinas; Jueves Santo",
            ),
            ("2026-04-03", "Viernes Santo"),
            ("2026-05-01", "Día del Trabajo"),
            ("2026-05-25", "Día de la Revolución de Mayo"),
            ("2026-06-15", "Paso a la Inmortalidad del General Don Martín Miguel de Güemes"),
            ("2026-06-19", "Sin liquidación cable"),
            ("2026-06-20", "Paso a la Inmortalidad del General Don Manuel Belgrano"),
            ("2026-07-09", "Día de la Independencia"),
            ("2026-07-10", "Sin liquidación local"),
            ("2026-08-17", "Paso a la Inmortalidad del General Don José de San Martín"),
            ("2026-09-07", "Sin liquidación cable"),
            ("2026-10-12", "Día del Respeto a la Diversidad Cultural"),
            ("2026-11-06", "Día del Bancario"),
            ("2026-11-11", "Sin liquidación cable"),
            ("2026-11-23", "Día de la Soberanía Nacional"),
            ("2026-11-26", "Sin liquidación cable"),
            ("2026-12-07", "Sin liquidación local"),
            ("2026-12-08", "Inmaculada Concepción de María"),
            ("2026-12-24", "Nochebuena (el mercado cierra a las 15:00); Sin liquidación local"),
            ("2026-12-25", "Navidad"),
            ("2026-12-31", "Feriado bursátil de fin de año"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2026-01-01", "New Year's Day"),
            ("2026-01-19", "No cable settlement"),
            ("2026-02-16", "Carnival Monday"),
            ("2026-02-17", "Carnival Tuesday"),
            ("2026-03-23", "No local settlement"),
            ("2026-03-24", "National Day of Remembrance for Truth and Justice"),
            ("2026-04-02", "Maundy Thursday; Veteran's Day and the Fallen in the Malvinas War"),
            ("2026-04-03", "Good Friday"),
            ("2026-05-01", "Labor Day"),
            ("2026-05-25", "May Revolution Day"),
            ("2026-06-15", "Pass to the Immortality of General Don Martín Miguel de Güemes"),
            ("2026-06-19", "No cable settlement"),
            ("2026-06-20", "Pass to the Immortality of General Don Manuel Belgrano"),
            ("2026-07-09", "Independence Day"),
            ("2026-07-10", "No local settlement"),
            ("2026-08-17", "Pass to the Immortality of General Don José de San Martín"),
            ("2026-09-07", "No cable settlement"),
            ("2026-10-12", "Respect for Cultural Diversity Day"),
            ("2026-11-06", "Bankers' Day"),
            ("2026-11-11", "No cable settlement"),
            ("2026-11-23", "National Sovereignty Day"),
            ("2026-11-26", "No cable settlement"),
            ("2026-12-07", "No local settlement"),
            ("2026-12-08", "Immaculate Conception"),
            ("2026-12-24", "Christmas Eve (markets close at 3:00pm); No local settlement"),
            ("2026-12-25", "Christmas Day"),
            ("2026-12-31", "Year-end market holiday"),
        )
