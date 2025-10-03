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

from holidays.countries.canary_islands import HolidaysIC, CanaryIslands, IC
from tests.common import CommonCountryTests


class TestCanaryIslands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HolidaysIC)

    def test_country_aliases(self):
        self.assertAliases(HolidaysIC, CanaryIslands, IC)

    def test_no_holidays(self):
        self.assertNoHolidays(HolidaysIC(years=self.start_year - 1))

    def test_2025(self):
        self.assertHolidays(
            CanaryIslands(years=2025),
            ("2025-01-01", "Año Nuevo"),
            ("2025-01-06", "Epifanía del Señor"),
            ("2025-04-17", "Jueves Santo"),
            ("2025-04-18", "Viernes Santo"),
            ("2025-05-01", "Fiesta del Trabajo"),
            ("2025-05-30", "Día de Canarias"),
            ("2025-08-15", "Asunción de la Virgen"),
            ("2025-11-01", "Todos los Santos"),
            ("2025-12-06", "Día de la Constitución Española"),
            ("2025-12-08", "Inmaculada Concepción"),
            ("2025-12-25", "Natividad del Señor"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("1983-01-01", "Año Nuevo"),
            ("1983-01-06", "Epifanía del Señor"),
            ("1983-03-31", "Jueves Santo"),
            ("1983-04-01", "Viernes Santo"),
            ("1983-05-01", "Fiesta del Trabajo"),
            ("1983-05-30", "Día de Canarias"),
            ("1983-08-15", "Asunción de la Virgen"),
            ("1983-10-12", "Fiesta Nacional de España"),
            ("1983-11-01", "Todos los Santos"),
            ("1983-12-06", "Día de la Constitución Española"),
            ("1983-12-08", "Inmaculada Concepción"),
            ("1983-12-25", "Natividad del Señor"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("1983-01-01", "New Year's Day"),
            ("1983-01-06", "Epiphany"),
            ("1983-03-31", "Maundy Thursday"),
            ("1983-04-01", "Good Friday"),
            ("1983-05-01", "Labor Day"),
            ("1983-05-30", "Day of the Canary Islands"),
            ("1983-08-15", "Assumption Day"),
            ("1983-10-12", "National Day"),
            ("1983-11-01", "All Saints' Day"),
            ("1983-12-06", "Constitution Day"),
            ("1983-12-08", "Immaculate Conception"),
            ("1983-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("1983-01-01", "Новий рік"),
            ("1983-01-06", "Богоявлення"),
            ("1983-03-31", "Великий четвер"),
            ("1983-04-01", "Страсна пʼятниця"),
            ("1983-05-01", "День праці"),
            ("1983-05-30", "День Канарських островів"),
            ("1983-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("1983-10-12", "Національний день Іспанії"),
            ("1983-11-01", "День усіх святих"),
            ("1983-12-06", "День Конституції Іспанії"),
            ("1983-12-08", "Непорочне зачаття Діви Марії"),
            ("1983-12-25", "Різдво Христове"),
        )
