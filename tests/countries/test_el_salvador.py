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

from holidays.countries.el_salvador import ElSalvador
from tests.common import CommonCountryTests


class TestElSalvador(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(ElSalvador, years=range(1973, 2050))

    def test_new_years_day(self):
        self.assertHolidayName("Año Nuevo", (f"{year}-01-01" for year in range(1973, 2050)))

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
        self.assertHolidayName(name, range(1973, 2050))

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
        self.assertHolidayName(name, range(1973, 2050))

    def test_holy_saturday(self):
        name = "Sábado Santo"
        self.assertHolidayName(
            name,
            "2016-03-26",
            "2017-04-15",
            "2018-03-31",
            "2019-04-20",
            "2020-04-11",
            "2021-04-03",
            "2022-04-16",
            "2023-04-08",
            "2024-03-30",
        )
        self.assertHolidayName(name, range(1973, 2050))

    def test_labor_day(self):
        self.assertHolidayName("Día del Trabajo", (f"{year}-05-01" for year in range(1973, 2050)))

    def test_mothers_day(self):
        name = "Día de la Madre"
        self.assertHolidayName(name, (f"{year}-05-10" for year in range(2016, 2050)))
        self.assertNoHoliday(f"{year}-05-10" for year in range(1973, 2016))
        self.assertNoHolidayName(name, range(1973, 2016))

    def test_fathers_day(self):
        name = "Día del Padre"
        self.assertHolidayName(name, (f"{year}-06-17" for year in range(2013, 2050)))
        self.assertNoHoliday(f"{year}-06-17" for year in range(1973, 2013))
        self.assertNoHolidayName(name, range(1973, 2013))

    def test_feast_of_san_salvador(self):
        self.assertHolidayName(
            "Celebración del Divino Salvador del Mundo",
            (f"{year}-08-06" for year in range(1973, 2050)),
        )

    def test_independence_day(self):
        self.assertHolidayName(
            "Día de la Independencia", (f"{year}-09-15" for year in range(1973, 2050))
        )

    def test_all_souls_day(self):
        self.assertHolidayName(
            "Día de los Difuntos", (f"{year}-11-02" for year in range(1973, 2050))
        )

    def test_christmas_day(self):
        self.assertHolidayName("Navidad", (f"{year}-12-25" for year in range(1973, 2050)))

    def test_ss_holidays(self):
        name = "Fiesta de San Salvador"
        self.assertNoHolidayName(name)
        self.assertHolidayName(
            name,
            ElSalvador(subdiv="SS", years=range(1973, 2050)),
            (f"{year}-08-03" for year in range(1973, 2050)),
            (f"{year}-08-05" for year in range(1973, 2050)),
        )

    def test_2021(self):
        self.assertHolidaysInYear(
            2021,
            ("2021-01-01", "Año Nuevo"),
            ("2021-04-01", "Jueves Santo"),
            ("2021-04-02", "Viernes Santo"),
            ("2021-04-03", "Sábado Santo"),
            ("2021-05-01", "Día del Trabajo"),
            ("2021-05-10", "Día de la Madre"),
            ("2021-06-17", "Día del Padre"),
            ("2021-08-06", "Celebración del Divino Salvador del Mundo"),
            ("2021-09-15", "Día de la Independencia"),
            ("2021-11-02", "Día de los Difuntos"),
            ("2021-12-25", "Navidad"),
        )

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "Año Nuevo"),
            ("2022-04-14", "Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-04-16", "Sábado Santo"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-05-10", "Día de la Madre"),
            ("2022-06-17", "Día del Padre"),
            ("2022-08-06", "Celebración del Divino Salvador del Mundo"),
            ("2022-09-15", "Día de la Independencia"),
            ("2022-11-02", "Día de los Difuntos"),
            ("2022-12-25", "Navidad"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "Año Nuevo"),
            ("2024-03-28", "Jueves Santo"),
            ("2024-03-29", "Viernes Santo"),
            ("2024-03-30", "Sábado Santo"),
            ("2024-05-01", "Día del Trabajo"),
            ("2024-05-10", "Día de la Madre"),
            ("2024-06-17", "Día del Padre"),
            ("2024-08-03", "Fiesta de San Salvador"),
            ("2024-08-05", "Fiesta de San Salvador"),
            ("2024-08-06", "Celebración del Divino Salvador del Mundo"),
            ("2024-09-15", "Día de la Independencia"),
            ("2024-11-02", "Día de los Difuntos"),
            ("2024-12-25", "Navidad"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-03-28", "Maundy Thursday"),
            ("2024-03-29", "Good Friday"),
            ("2024-03-30", "Holy Saturday"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-10", "Mother's Day"),
            ("2024-06-17", "Father's Day"),
            ("2024-08-03", "Feast of San Salvador"),
            ("2024-08-05", "Feast of San Salvador"),
            ("2024-08-06", "Celebrations of San Salvador"),
            ("2024-09-15", "Independence Day"),
            ("2024-11-02", "All Souls' Day"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2024-01-01", "Новий рік"),
            ("2024-03-28", "Великий четвер"),
            ("2024-03-29", "Страсна пʼятниця"),
            ("2024-03-30", "Велика субота"),
            ("2024-05-01", "День праці"),
            ("2024-05-10", "День матері"),
            ("2024-06-17", "День батька"),
            ("2024-08-03", "Свято Спасителя"),
            ("2024-08-05", "Свято Спасителя"),
            ("2024-08-06", "Свято Божественного Спасителя світу"),
            ("2024-09-15", "День незалежності"),
            ("2024-11-02", "День усіх померлих"),
            ("2024-12-25", "Різдво Христове"),
        )
