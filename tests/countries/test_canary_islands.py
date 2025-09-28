from unittest import TestCase

from holidays.constants import PUBLIC, UNOFFICIAL, WORKDAY
from holidays.countries.canary_islands import HolidaysIC, IC, CanaryIslands
from tests.common import CommonCountryTests

class TestCanaryIslands(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HolidaysIC)
    
    def test_country_aliases(self):
        self.assertAliases(CanaryIslands, IC, CanaryIslands)
    
    def test_no_holidays(self):
        self.assertNoHolidays(CanaryIslands(years=1982))
    
    def test_1983(self):
        self.assertHolidays(
        CanaryIslands(years=1983),
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


