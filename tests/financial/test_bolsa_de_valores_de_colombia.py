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

from holidays.financial.bolsa_de_valores_de_colombia import BolsaDeValoresDeColombia
from tests.common import CommonFinancialTests


class TestBolsaDeValoresDeColombia(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BolsaDeValoresDeColombia)

    def test_code(self):
        self.assertTrue(hasattr(self.holidays, "market"))
        self.assertIsNone(getattr(self.holidays, "country", None))

    def test_year_end_market_holiday(self):
        name = "Día no bursátil de fin de año"
        self.assertHolidayName(
            name,
            "2008-12-31",
            "2009-12-31",
            "2010-12-31",
            "2011-12-30",
            "2012-12-31",
            "2013-12-31",
            "2014-12-31",
            "2015-12-31",
            "2016-12-30",
            "2017-12-29",
            "2018-12-31",
            "2019-12-31",
            "2020-12-31",
            "2021-12-31",
            "2022-12-30",
            "2023-12-29",
            "2024-12-31",
            "2025-12-31",
            "2026-12-31",
        )
        self.assertHolidayNameCount(name, 1, self.full_range)

    def test_year_end_market_holiday_on_weekend(self):
        # When December 31 falls on a weekend, the preceding Friday is closed instead.
        self.assertNoHoliday("2011-12-29", "2016-12-29", "2017-12-28", "2022-12-29", "2023-12-28")

    def test_half_day(self):
        name = "Nochebuena (el mercado cierra a las 13:00)"
        self.assertHalfDayHolidayName(name, "2019-12-24", "2020-12-24", "2021-12-24", "2025-12-24")
        self.assertNoHalfDayHoliday("2018-12-24", "2024-12-24")
        self.assertNoHoliday("2019-12-24", "2020-12-24", "2021-12-24", "2025-12-24")

    def test_2025(self):
        self.assertHolidaysInYear(
            2025,
            ("2025-01-01", "Año Nuevo"),
            ("2025-01-06", "Día de los Reyes Magos"),
            ("2025-03-24", "Día de San José (observado)"),
            ("2025-04-17", "Jueves Santo"),
            ("2025-04-18", "Viernes Santo"),
            ("2025-05-01", "Día del Trabajo"),
            ("2025-06-02", "Ascensión del señor (observado)"),
            ("2025-06-23", "Corpus Christi (observado)"),
            ("2025-06-30", "Sagrado Corazón (observado); San Pedro y San Pablo (observado)"),
            ("2025-07-20", "Día de la Independencia"),
            ("2025-08-07", "Batalla de Boyacá"),
            ("2025-08-18", "La Asunción (observado)"),
            ("2025-10-13", "Día de la Raza (observado)"),
            ("2025-11-03", "Día de Todos los Santos (observado)"),
            ("2025-11-17", "Independencia de Cartagena (observado)"),
            ("2025-12-08", "La Inmaculada Concepción"),
            ("2025-12-25", "Navidad"),
            ("2025-12-31", "Día no bursátil de fin de año"),
        )

    def test_2026(self):
        self.assertHolidaysInYear(
            2026,
            ("2026-01-01", "Año Nuevo"),
            ("2026-01-12", "Día de los Reyes Magos (observado)"),
            ("2026-03-23", "Día de San José (observado)"),
            ("2026-04-02", "Jueves Santo"),
            ("2026-04-03", "Viernes Santo"),
            ("2026-05-01", "Día del Trabajo"),
            ("2026-05-18", "Ascensión del señor (observado)"),
            ("2026-06-08", "Corpus Christi (observado)"),
            ("2026-06-15", "Sagrado Corazón (observado)"),
            ("2026-06-29", "San Pedro y San Pablo"),
            ("2026-07-13", "Día de Nuestra Señora del Rosario de Chiquinquirá (observado)"),
            ("2026-07-20", "Día de la Independencia"),
            ("2026-08-07", "Batalla de Boyacá"),
            ("2026-08-17", "La Asunción (observado)"),
            ("2026-10-12", "Día de la Raza"),
            ("2026-11-02", "Día de Todos los Santos (observado)"),
            ("2026-11-16", "Independencia de Cartagena (observado)"),
            ("2026-12-08", "La Inmaculada Concepción"),
            ("2026-12-25", "Navidad"),
            ("2026-12-31", "Día no bursátil de fin de año"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Año Nuevo"),
            ("2025-01-06", "Día de los Reyes Magos"),
            ("2025-03-24", "Día de San José (observado)"),
            ("2025-04-17", "Jueves Santo"),
            ("2025-04-18", "Viernes Santo"),
            ("2025-05-01", "Día del Trabajo"),
            ("2025-06-02", "Ascensión del señor (observado)"),
            ("2025-06-23", "Corpus Christi (observado)"),
            ("2025-06-30", "Sagrado Corazón (observado); San Pedro y San Pablo (observado)"),
            ("2025-07-20", "Día de la Independencia"),
            ("2025-08-07", "Batalla de Boyacá"),
            ("2025-08-18", "La Asunción (observado)"),
            ("2025-10-13", "Día de la Raza (observado)"),
            ("2025-11-03", "Día de Todos los Santos (observado)"),
            ("2025-11-17", "Independencia de Cartagena (observado)"),
            ("2025-12-08", "La Inmaculada Concepción"),
            ("2025-12-24", "Nochebuena (el mercado cierra a las 13:00)"),
            ("2025-12-25", "Navidad"),
            ("2025-12-31", "Día no bursátil de fin de año"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-01-06", "Epiphany"),
            ("2025-03-24", "Saint Joseph's Day (observed)"),
            ("2025-04-17", "Maundy Thursday"),
            ("2025-04-18", "Good Friday"),
            ("2025-05-01", "Labor Day"),
            ("2025-06-02", "Ascension Day (observed)"),
            ("2025-06-23", "Corpus Christi (observed)"),
            ("2025-06-30", "Sacred Heart (observed); Saint Peter and Saint Paul's Day (observed)"),
            ("2025-07-20", "Independence Day"),
            ("2025-08-07", "Battle of Boyacá"),
            ("2025-08-18", "Assumption Day (observed)"),
            ("2025-10-13", "Columbus Day (observed)"),
            ("2025-11-03", "All Saints' Day (observed)"),
            ("2025-11-17", "Independence of Cartagena (observed)"),
            ("2025-12-08", "Immaculate Conception"),
            ("2025-12-24", "Christmas Eve (markets close at 1:00pm)"),
            ("2025-12-25", "Christmas Day"),
            ("2025-12-31", "Year-end market holiday"),
        )
