#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.nicaragua import Nicaragua, NI, NIC
from tests.common import CommonCountryTests


class TestNicaragua(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Nicaragua, years=range(1950, 2050))

    def test_country_aliases(self):
        self.assertAliases(Nicaragua, NI, NIC)

    def test_new_years_day(self):
        self.assertHolidayName("Año Nuevo", (f"{year}-01-01" for year in range(1950, 2050)))

    def test_maundy_thursday(self):
        name = "Jueves Santo"
        self.assertHolidayName(
            name,
            "2016-03-24",
            "2017-04-13",
            "2018-03-29",
            "2019-04-18",
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
        )
        self.assertHolidayName(name, range(1950, 2050))

    def test_good_friday(self):
        name = "Viernes Santo"
        self.assertHolidayName(
            name,
            "2016-03-25",
            "2017-04-14",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
        )
        self.assertHolidayName(name, range(1950, 2050))

    def test_labor_day(self):
        self.assertHolidayName("Día del Trabajo", (f"{year}-05-01" for year in range(1950, 2050)))

    def test_mothers_day(self):
        name = "Día de la Madre"
        self.assertHolidayName(name, (f"{year}-05-30" for year in range(2022, 2050)))
        self.assertNoHolidayName(name, range(1950, 2022))

    def test_revolution_day(self):
        name = "Día de la Revolución"
        self.assertHolidayName(name, (f"{year}-07-19" for year in range(1979, 2050)))
        self.assertNoHolidayName(name, range(1950, 1979))

    def test_battle_of_san_jacinto_day(self):
        self.assertHolidayName(
            "Batalla de San Jacinto", (f"{year}-09-14" for year in range(1950, 2050))
        )

    def test_independence_day(self):
        self.assertHolidayName(
            "Día de la Independencia", (f"{year}-09-15" for year in range(1950, 2050))
        )

    def test_virgins_day(self):
        self.assertHolidayName(
            "Concepción de María", (f"{year}-12-08" for year in range(1950, 2050))
        )

    def test_christmas_day(self):
        self.assertHolidayName("Navidad", (f"{year}-12-25" for year in range(1950, 2050)))

    def test_2023(self):
        self.assertHolidays(
            Nicaragua(years=2023),
            ("2023-01-01", "Año Nuevo"),
            ("2023-04-06", "Jueves Santo"),
            ("2023-04-07", "Viernes Santo"),
            ("2023-05-01", "Día del Trabajo"),
            ("2023-05-30", "Día de la Madre"),
            ("2023-07-19", "Día de la Revolución"),
            ("2023-09-14", "Batalla de San Jacinto"),
            ("2023-09-15", "Día de la Independencia"),
            ("2023-12-08", "Concepción de María"),
            ("2023-12-25", "Navidad"),
        )

        for subdiv in Nicaragua.subdivisions:
            if subdiv == "MN":
                self.assertHoliday(
                    Nicaragua(subdiv=subdiv),
                    "2023-08-01",
                    "2023-08-10",
                )
            else:
                self.assertNoHoliday(
                    Nicaragua(subdiv=subdiv),
                    "2023-08-01",
                    "2023-08-10",
                )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-04-14", "Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-05-30", "Día de la Madre"),
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
            ("2022-05-30", "Mother's Day"),
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
            ("2022-05-30", "День матері"),
            ("2022-07-19", "День революції"),
            ("2022-08-01", "Спуск Святого Домініка"),
            ("2022-08-10", "Підйом Святого Домініка"),
            ("2022-09-14", "Річниця битви під Сан-Хасінто"),
            ("2022-09-15", "День незалежності"),
            ("2022-12-08", "Непорочне зачаття Діви Марії"),
            ("2022-12-25", "Різдво Христове"),
        )
