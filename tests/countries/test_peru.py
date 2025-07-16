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

from holidays.countries.peru import Peru, PE, PER
from tests.common import CommonCountryTests


class TestPeru(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Peru)

    def test_country_aliases(self):
        self.assertAliases(Peru, PE, PER)

    def test_2019(self):
        self.assertHolidayDates(
            "2019-01-01",
            "2019-04-18",
            "2019-04-19",
            "2019-04-21",
            "2019-05-01",
            "2019-06-29",
            "2019-07-28",
            "2019-07-29",
            "2019-08-30",
            "2019-10-08",
            "2019-11-01",
            "2019-12-08",
            "2019-12-25",
        )

    def test_2025(self):
        self.assertHolidayDates(
            "2025-01-01",
            "2025-04-17",
            "2025-04-18",
            "2025-04-20",
            "2025-05-01",
            "2025-06-07",
            "2025-06-29",
            "2025-07-23",
            "2025-07-28",
            "2025-07-29",
            "2025-08-06",
            "2025-08-30",
            "2025-10-08",
            "2025-11-01",
            "2025-12-08",
            "2025-12-09",
            "2025-12-25",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2025-01-01", "Año Nuevo"),
            ("2025-04-17", "Jueves Santo"),
            ("2025-04-18", "Viernes Santo"),
            ("2025-04-20", "Domingo de Resurrección"),
            ("2025-05-01", "Día del Trabajo"),
            ("2025-06-07", "Batalla de Arica y Día de la Bandera"),
            ("2025-06-29", "San Pedro y San Pablo"),
            ("2025-07-23", "Día de la Fuerza Aérea del Perú"),
            ("2025-07-28", "Día de la Independencia"),
            ("2025-07-29", "Día de la Gran Parada Militar"),
            ("2025-08-06", "Batalla de Junín"),
            ("2025-08-30", "Santa Rosa de Lima"),
            ("2025-10-08", "Combate de Angamos"),
            ("2025-11-01", "Todos Los Santos"),
            ("2025-12-08", "Inmaculada Concepción"),
            ("2025-12-09", "Batalla de Ayacucho"),
            ("2025-12-25", "Navidad del Señor"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2025-01-01", "New Year's Day"),
            ("2025-04-17", "Maundy Thursday"),
            ("2025-04-18", "Good Friday"),
            ("2025-04-20", "Easter Sunday"),
            ("2025-05-01", "Labor Day"),
            ("2025-06-07", "Battle of Arica and National Flag Day"),
            ("2025-06-29", "Saint Peter and Saint Paul's Day"),
            ("2025-07-23", "Peruvian Air Force Day"),
            ("2025-07-28", "Independence Day"),
            ("2025-07-29", "Great Military Parade Day"),
            ("2025-08-06", "Battle of Junín Day"),
            ("2025-08-30", "Rose of Lima Day"),
            ("2025-10-08", "Battle of Angamos Day"),
            ("2025-11-01", "All Saints' Day"),
            ("2025-12-08", "Immaculate Conception"),
            ("2025-12-09", "Battle of Ayacucho Day"),
            ("2025-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2025-01-01", "Новий рік"),
            ("2025-04-17", "Великий четвер"),
            ("2025-04-18", "Страсна пʼятниця"),
            ("2025-04-20", "Великдень"),
            ("2025-05-01", "День праці"),
            ("2025-06-07", "Битва за Аріку та День прапора"),
            ("2025-06-29", "День Святих Петра і Павла"),
            ("2025-07-23", "День Повітряних сил Перу"),
            ("2025-07-28", "День незалежності"),
            ("2025-07-29", "День Великого військового параду"),
            ("2025-08-06", "День битви під Хуніном"),
            ("2025-08-30", "День Святої Рози Лімської"),
            ("2025-10-08", "День битви під Ангамосом"),
            ("2025-11-01", "День усіх святих"),
            ("2025-12-08", "Непорочне зачаття Діви Марії"),
            ("2025-12-09", "День битви при Аякучо"),
            ("2025-12-25", "Різдво Христове"),
        )
