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

from holidays.countries.nicaragua import Nicaragua, NI, NIC
from tests.common import CommonCountryTests


class TestNicaragua(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Nicaragua)

    def test_country_aliases(self):
        self.assertAliases(Nicaragua, NI, NIC)

    def test_2020(self):
        self.assertHoliday(
            "2020-01-01",
            "2020-04-09",
            "2020-04-10",
            "2020-05-01",
            "2020-07-19",
            "2020-08-01",
            "2020-08-10",
            "2020-09-14",
            "2020-09-15",
            "2020-12-08",
            "2020-12-25",
        )
        self.assertNoHoliday(
            Nicaragua(subdiv="AN"),
            "2020-08-01",
            "2020-08-10",
        )

    def test_ni_holidays_1979(self):
        self.assertHoliday(
            "1979-01-01",
            "1979-04-12",
            "1979-04-13",
            "1979-05-01",
            "1979-07-19",
            "1979-09-14",
            "1979-09-15",
            "1979-12-08",
            "1979-12-25",
        )

    def test_pre_1979(self):
        self.assertNoHoliday("1978-07-19")

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-04-14", "Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-07-19", "Día de la Revolución"),
            ("2022-08-01", "Bajada de Santo Domingo"),
            ("2022-08-10", "Subida de Santo Domingo"),
            ("2022-09-14", "Batalla de San Jacinto"),
            ("2022-09-15", "Día de la Independencia"),
            ("2022-12-08", "Concepción de María"),
            ("2022-12-25", "Navidad"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-14", "Maundy Thursday"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "Labor Day"),
            ("2022-07-19", "Revolution Day"),
            ("2022-08-01", "Descent of Saint Dominic"),
            ("2022-08-10", "Ascent of Saint Dominic"),
            ("2022-09-14", "Battle of San Jacinto Day"),
            ("2022-09-15", "Independence Day"),
            ("2022-12-08", "Virgin's Day"),
            ("2022-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-14", "Великий четвер"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-05-01", "День праці"),
            ("2022-07-19", "День революції"),
            ("2022-08-01", "Спуск Святого Домініка"),
            ("2022-08-10", "Підйом Святого Домініка"),
            ("2022-09-14", "Річниця битви під Сан-Хасінто"),
            ("2022-09-15", "День незалежності"),
            ("2022-12-08", "Непорочне зачаття Діви Марії"),
            ("2022-12-25", "Різдво Христове"),
        )
