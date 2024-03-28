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

    def test_2022(self):
        self.assertHolidayDates(
            "2022-01-01",
            "2022-04-14",
            "2022-04-15",
            "2022-04-17",
            "2022-05-01",
            "2022-06-29",
            "2022-07-28",
            "2022-07-29",
            "2022-08-06",
            "2022-08-30",
            "2022-10-08",
            "2022-11-01",
            "2022-12-08",
            "2022-12-09",
            "2022-12-25",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-04-14", "Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-04-17", "Domingo de Resurrección"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-06-29", "San Pedro y San Pablo"),
            ("2022-07-28", "Día de la Independencia"),
            ("2022-07-29", "Día de la Gran Parada Militar"),
            ("2022-08-06", "Batalla de Junín"),
            ("2022-08-30", "Santa Rosa de Lima"),
            ("2022-10-08", "Combate de Angamos"),
            ("2022-11-01", "Todos Los Santos"),
            ("2022-12-08", "Inmaculada Concepción"),
            ("2022-12-09", "Batalla de Ayacucho"),
            ("2022-12-25", "Navidad del Señor"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-14", "Maundy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-05-01", "Labor Day"),
            ("2022-06-29", "Saint Peter and Saint Paul"),
            ("2022-07-28", "Independence Day"),
            ("2022-07-29", "Great Military Parade Day"),
            ("2022-08-06", "Battle of Junín Day"),
            ("2022-08-30", "Rose of Lima Day"),
            ("2022-10-08", "Battle of Angamos Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-08", "Immaculate Conception Day"),
            ("2022-12-09", "Battle of Ayacucho Day"),
            ("2022-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-14", "Великий четвер"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-05-01", "День праці"),
            ("2022-06-29", "День Святих Петра і Павла"),
            ("2022-07-28", "День незалежності"),
            ("2022-07-29", "День Великого військового параду"),
            ("2022-08-06", "День битви під Хуніном"),
            ("2022-08-30", "День Святої Рози Лімської"),
            ("2022-10-08", "День битви під Ангамосом"),
            ("2022-11-01", "День усіх святих"),
            ("2022-12-08", "Непорочне зачаття Діви Марії"),
            ("2022-12-09", "День битви при Аякучо"),
            ("2022-12-25", "Різдво Христове"),
        )
