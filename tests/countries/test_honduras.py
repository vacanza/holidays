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

from holidays.countries.honduras import Honduras
from tests.common import CommonCountryTests


class TestHonduras(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Honduras)

    def test_new_years_day(self):
        self.assertHolidayName("Año Nuevo", (f"{year}-01-01" for year in self.full_range))

    def test_maundy_thursday(self):
        name = "Jueves Santo"
        self.assertHolidayName(
            name,
            "2020-04-09",
            "2021-04-01",
            "2022-04-14",
            "2023-04-06",
            "2024-03-28",
            "2025-04-17",
        )
        self.assertHolidayName(name, self.full_range)

    def test_good_friday(self):
        name = "Viernes Santo"
        self.assertHolidayName(
            name,
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

    def test_holy_saturday(self):
        name = "Sábado de Gloria"
        self.assertHolidayName(
            name,
            "2020-04-11",
            "2021-04-03",
            "2022-04-16",
            "2023-04-08",
            "2024-03-30",
            "2025-04-19",
        )
        self.assertHolidayName(name, self.full_range)

    def test_panamerican_day(self):
        self.assertHolidayName(
            "Día de las Américas", (f"{year}-04-14" for year in self.full_range)
        )

    def test_labor_day(self):
        self.assertHolidayName("Día del Trabajo", (f"{year}-05-01" for year in self.full_range))

    def test_independence_day(self):
        self.assertHolidayName(
            "Día de la Independencia", (f"{year}-09-15" for year in self.full_range)
        )

    def test_morazan_day(self):
        name = "Día de Morazán"
        self.assertHolidayName(name, (f"{year}-10-03" for year in range(self.start_year, 2015)))
        self.assertNoHolidayName(name, range(2015, self.end_year))

    def test_columbus_day(self):
        name = "Día de la Raza"
        self.assertHolidayName(name, (f"{year}-10-12" for year in range(self.start_year, 2015)))
        self.assertNoHolidayName(name, range(2015, self.end_year))

    def test_army_day(self):
        name = "Día de las Fuerzas Armadas"
        self.assertHolidayName(name, (f"{year}-10-21" for year in range(self.start_year, 2015)))
        self.assertNoHolidayName(name, range(2015, self.end_year))

    def test_morazan_weekend(self):
        name = "Semana Morazánica"
        self.assertHolidayName(
            name,
            "2020-10-07",
            "2020-10-08",
            "2020-10-09",
            "2021-10-06",
            "2021-10-07",
            "2021-10-08",
            "2022-10-05",
            "2022-10-06",
            "2022-10-07",
            "2023-10-04",
            "2023-10-05",
            "2023-10-06",
            "2024-10-02",
            "2024-10-03",
            "2024-10-04",
            "2025-10-01",
            "2025-10-02",
            "2025-10-03",
        )
        self.assertHolidayNameCount(name, 3, range(2015, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2015))

    def test_christmas_day(self):
        self.assertHolidayName("Navidad", (f"{year}-12-25" for year in self.full_range))

    def test_2016(self):
        # https://www.officeholidays.com/countries/honduras/2016
        self.assertHolidayDatesInYear(
            2016,
            "2016-01-01",
            "2016-03-24",
            "2016-03-25",
            "2016-03-26",
            "2016-04-14",
            "2016-05-01",
            "2016-09-15",
            "2016-10-05",
            "2016-10-06",
            "2016-10-07",
            "2016-12-25",
        )

    def test_2021(self):
        # https://www.officeholidays.com/countries/honduras/2021
        self.assertHolidayDatesInYear(
            2021,
            "2021-01-01",
            "2021-04-01",
            "2021-04-02",
            "2021-04-03",
            "2021-04-14",
            "2021-05-01",
            "2021-09-15",
            "2021-10-06",
            "2021-10-07",
            "2021-10-08",
            "2021-12-25",
        )

    def test_2025(self):
        self.assertHolidayDatesInYear(
            2025,
            "2025-01-01",
            "2025-04-14",
            "2025-04-17",
            "2025-04-18",
            "2025-04-19",
            "2025-05-01",
            "2025-09-15",
            "2025-10-01",
            "2025-10-02",
            "2025-10-03",
            "2025-12-25",
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-04-14", "Día de las Américas; Jueves Santo"),
            ("2022-04-15", "Viernes Santo"),
            ("2022-04-16", "Sábado de Gloria"),
            ("2022-05-01", "Día del Trabajo"),
            ("2022-09-15", "Día de la Independencia"),
            ("2022-10-05", "Semana Morazánica"),
            ("2022-10-06", "Semana Morazánica"),
            ("2022-10-07", "Semana Morazánica"),
            ("2022-12-25", "Navidad"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-04-14", "Maundy Thursday; Panamerican Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-16", "Holy Saturday"),
            ("2022-05-01", "Labor Day"),
            ("2022-09-15", "Independence Day"),
            ("2022-10-05", "Morazan Weekend"),
            ("2022-10-06", "Morazan Weekend"),
            ("2022-10-07", "Morazan Weekend"),
            ("2022-12-25", "Christmas Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-04-14", "Великий четвер; День Америки"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-16", "Велика субота"),
            ("2022-05-01", "День праці"),
            ("2022-09-15", "День незалежності"),
            ("2022-10-05", "Тиждень Морасана"),
            ("2022-10-06", "Тиждень Морасана"),
            ("2022-10-07", "Тиждень Морасана"),
            ("2022-12-25", "Різдво Христове"),
        )
