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

from holidays.constants import BANK, PUBLIC
from holidays.countries.uruguay import Uruguay, UY, URY
from tests.common import CommonCountryTests


class TestUruguay(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1920, 2050)
        super().setUpClass(Uruguay, years=years)
        cls.bank_holidays = Uruguay(years=years, categories=BANK)

    def test_country_aliases(self):
        self.assertAliases(Uruguay, UY, URY)

    def test_no_holidays(self):
        self.assertNoHolidays(Uruguay(categories=(BANK, PUBLIC), years=1919))

    def test_special_holidays(self):
        self.assertHoliday(
            "1985-03-01",
            "1990-03-01",
            "1995-03-01",
            "2000-03-01",
            "2005-03-01",
            "2010-03-01",
            "2015-03-01",
            "2020-03-01",
        )

    def test_new_years_day(self):
        self.assertHolidayName("Año Nuevo", (f"{year}-01-01" for year in range(1920, 2050)))

    def test_cry_of_asencio(self):
        name = "Grito de Asencio"
        self.assertHolidayName(name, (f"{year}-02-28" for year in range(1920, 1934)))
        self.assertNoHolidayName(name, range(1934, 2050))

    def test_labor_day(self):
        name = "Día de los Trabajadores"
        self.assertHolidayName(
            name, (f"{year}-05-01" for year in set(range(1920, 2050)).difference({1980, 1981}))
        )
        self.assertHolidayName(
            name,
            "1980-05-05",
            "1981-05-04",
        )

    def test_spain_day(self):
        name = "Día de España"
        self.assertHolidayName(name, (f"{year}-05-02" for year in range(1920, 1933)))
        self.assertNoHolidayName(name, range(1933, 2050))

    def test_america_day(self):
        name = "Día de América"
        self.assertHolidayName(name, (f"{year}-05-25" for year in range(1920, 1933)))
        self.assertNoHolidayName(name, range(1933, 2050))

    def test_democracy_day(self):
        name = "Día de la Democracia"
        self.assertHolidayName(name, (f"{year}-07-04" for year in range(1920, 1933)))
        self.assertNoHolidayName(name, range(1933, 2050))

    def test_humanity_day(self):
        name = "Día de la Humanidad"
        self.assertHolidayName(name, (f"{year}-07-14" for year in range(1920, 1933)))
        self.assertNoHolidayName(name, range(1933, 2050))

    def test_constitution_day(self):
        self.assertHolidayName(
            "Jura de la Constitución", (f"{year}-07-18" for year in range(1920, 2050))
        )

    def test_independence_day(self):
        self.assertHolidayName(
            "Declaratoria de la Independencia", (f"{year}-08-25" for year in range(1920, 2050))
        )

    def test_italy_day(self):
        name = "Día de Italia"
        self.assertHolidayName(name, (f"{year}-09-20" for year in range(1920, 1933)))
        self.assertNoHolidayName(name, range(1933, 2050))

    def test_open_town_hall(self):
        name = "Cabildo Abierto"
        self.assertHolidayName(name, (f"{year}-09-21" for year in range(1920, 1933)))
        self.assertNoHolidayName(name, range(1933, 2050))

    def test_beaches_day(self):
        name = "Día de las Playas"
        self.assertHolidayName(name, (f"{year}-12-08" for year in range(1920, 1933)))
        self.assertHolidayName(name, (f"{year}-12-08" for year in range(1936, 1980)))
        self.assertNoHolidayName(name, range(1933, 1936), range(1980, 2050))

    def test_christmas(self):
        self.assertHolidayName(
            "Día de la Familia", (f"{year}-12-25" for year in range(1920, 2050))
        )

    def test_childrens_day(self):
        self.assertHolidayName(
            "Día de los Niños", self.bank_holidays, (f"{year}-01-06" for year in range(1920, 2050))
        )

    def test_carnival(self):
        name = "Carnaval"
        self.assertHolidayName(
            name,
            self.bank_holidays,
            "2018-02-12",
            "2018-02-13",
            "2019-03-04",
            "2019-03-05",
            "2020-02-24",
            "2020-02-25",
            "2021-02-15",
            "2021-02-16",
            "2022-02-28",
            "2022-03-01",
            "2023-02-20",
            "2023-02-21",
        )
        self.assertHolidayName(name, self.bank_holidays, range(1920, 2050))

    def test_landing_of_33_patriots(self):
        name = "Desembarco de los 33 Orientales"
        self.assertHolidayName(
            name, self.bank_holidays, (f"{year}-04-19" for year in range(1920, 1933))
        )
        self.assertHolidayName(
            name,
            self.bank_holidays,
            (f"{year}-04-19" for year in set(range(1949, 1997)).difference({1983})),
        )
        self.assertNoHolidayName(name, self.bank_holidays, range(1934, 1949))
        self.assertHolidayName(
            name,
            self.bank_holidays,
            "1983-04-18",
            "2000-04-17",
            "2018-04-23",
            "2019-04-22",
            "2020-04-19",
            "2021-04-19",
            "2022-04-18",
            "2023-04-17",
        )
        self.assertHolidayName(name, self.bank_holidays, range(1949, 2050))

    def test_tourism_week(self):
        name = "Semana de Turismo"
        self.assertHolidayName(
            name,
            self.bank_holidays,
            "2020-04-06",
            "2020-04-07",
            "2020-04-08",
            "2020-04-09",
            "2020-04-10",
            "2021-03-29",
            "2021-03-30",
            "2021-03-31",
            "2021-04-01",
            "2021-04-02",
            "2022-04-11",
            "2022-04-12",
            "2022-04-13",
            "2022-04-14",
            "2022-04-15",
        )
        self.assertHolidayName(name, self.bank_holidays, range(1920, 2050))

    def test_battle_of_las_piedras(self):
        name = "Batalla de Las Piedras"
        self.assertHolidayName(
            name, self.bank_holidays, (f"{year}-05-18" for year in range(1920, 1933))
        )
        self.assertHolidayName(
            name,
            self.bank_holidays,
            (f"{year}-05-18" for year in set(range(1942, 1997)).difference({1982, 1983})),
        )
        self.assertNoHolidayName(name, self.bank_holidays, range(1933, 1942))
        self.assertHolidayName(
            name,
            self.bank_holidays,
            "1982-05-17",
            "1983-05-16",
            "1999-05-17",
            "2018-05-21",
            "2019-05-18",
            "2020-05-18",
            "2021-05-17",
            "2022-05-16",
            "2023-05-22",
        )
        self.assertHolidayName(name, self.bank_holidays, range(1942, 2050))

    def test_birthday_of_artigas(self):
        name = "Natalicio de Artigas"
        self.assertHolidayName(
            name, self.bank_holidays, (f"{year}-06-19" for year in range(1920, 1933))
        )
        self.assertHolidayName(
            name,
            self.bank_holidays,
            (
                f"{year}-06-19"
                for year in set(range(1940, 2050)).difference({1980, 1981, 1997, 1998, 2001})
            ),
        )
        self.assertNoHolidayName(name, self.bank_holidays, range(1933, 1940))
        self.assertHolidayName(
            name,
            self.bank_holidays,
            "1980-06-23",
            "1981-06-22",
            "1997-06-23",
            "1998-06-22",
            "2001-06-18",
        )
        self.assertHolidayName(name, self.bank_holidays, range(1940, 2050))

    def test_cultural_diversity_day(self):
        name_1 = "Día de la Raza"
        name_2 = "Día de la Diversidad Cultural"
        self.assertHolidayName(
            name_1, self.bank_holidays, (f"{year}-10-12" for year in range(1920, 1933))
        )
        self.assertHolidayName(
            name_1,
            self.bank_holidays,
            (f"{year}-10-12" for year in set(range(1937, 1997)).difference({1982, 1983})),
        )
        self.assertNoHolidayName(name_1, self.bank_holidays, range(1933, 1937))
        self.assertNoHolidayName(name_1, self.bank_holidays, range(2014, 2050))
        self.assertHolidayName(
            name_1,
            self.bank_holidays,
            "1982-10-11",
            "1983-10-10",
            "1999-10-11",
            "2013-10-12",
        )
        self.assertHolidayName(name_1, self.bank_holidays, range(1937, 2014))

        self.assertHolidayName(
            name_2,
            self.bank_holidays,
            "2014-10-12",
            "2018-10-15",
            "2019-10-12",
            "2020-10-12",
            "2021-10-11",
            "2022-10-10",
            "2023-10-16",
        )
        self.assertNoHolidayName(name_2, self.bank_holidays, range(1920, 2014))
        self.assertHolidayName(name_2, self.bank_holidays, range(2014, 2050))

    def test_all_souls_day(self):
        name = "Día de los Difuntos"
        self.assertHolidayName(
            name, self.bank_holidays, (f"{year}-11-02" for year in range(1920, 1933))
        )
        self.assertHolidayName(
            name,
            self.bank_holidays,
            (
                f"{year}-11-02"
                for year in set(range(1938, 2050)).difference({1982, 1983, 1999, 2000, 2001})
            ),
        )
        self.assertNoHolidayName(name, self.bank_holidays, range(1933, 1938))
        self.assertHolidayName(
            name,
            self.bank_holidays,
            "1982-11-01",
            "1983-10-31",
            "1999-11-01",
            "2000-11-06",
            "2001-11-05",
        )
        self.assertHolidayName(name, self.bank_holidays, range(1938, 2050))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Año Nuevo"),
            ("2022-01-06", "Día de los Niños"),
            ("2022-02-28", "Carnaval"),
            ("2022-03-01", "Carnaval"),
            ("2022-04-11", "Semana de Turismo"),
            ("2022-04-12", "Semana de Turismo"),
            ("2022-04-13", "Semana de Turismo"),
            ("2022-04-14", "Semana de Turismo"),
            ("2022-04-15", "Semana de Turismo"),
            ("2022-04-18", "Desembarco de los 33 Orientales"),
            ("2022-05-01", "Día de los Trabajadores"),
            ("2022-05-16", "Batalla de Las Piedras"),
            ("2022-06-19", "Natalicio de Artigas"),
            ("2022-07-18", "Jura de la Constitución"),
            ("2022-08-25", "Declaratoria de la Independencia"),
            ("2022-10-10", "Día de la Diversidad Cultural"),
            ("2022-11-02", "Día de los Difuntos"),
            ("2022-12-25", "Día de la Familia"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Children's Day"),
            ("2022-02-28", "Carnival"),
            ("2022-03-01", "Carnival"),
            ("2022-04-11", "Tourism Week"),
            ("2022-04-12", "Tourism Week"),
            ("2022-04-13", "Tourism Week"),
            ("2022-04-14", "Tourism Week"),
            ("2022-04-15", "Tourism Week"),
            ("2022-04-18", "Landing of the 33 Patriots"),
            ("2022-05-01", "International Workers' Day"),
            ("2022-05-16", "Battle of Las Piedras"),
            ("2022-06-19", "Birthday of Artigas"),
            ("2022-07-18", "Constitution Day"),
            ("2022-08-25", "Independence Day"),
            ("2022-10-10", "Cultural Diversity Day"),
            ("2022-11-02", "All Souls' Day"),
            ("2022-12-25", "Day of the Family"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-06", "День дітей"),
            ("2022-02-28", "Карнавал"),
            ("2022-03-01", "Карнавал"),
            ("2022-04-11", "Тиждень туризму"),
            ("2022-04-12", "Тиждень туризму"),
            ("2022-04-13", "Тиждень туризму"),
            ("2022-04-14", "Тиждень туризму"),
            ("2022-04-15", "Тиждень туризму"),
            ("2022-04-18", "День висадки 33 патріотів"),
            ("2022-05-01", "День трудящих"),
            ("2022-05-16", "День битви при Лас-Пʼєдрас"),
            ("2022-06-19", "Річниця Артігаса"),
            ("2022-07-18", "День присяги Конституції"),
            ("2022-08-25", "День проголошення незалежності"),
            ("2022-10-10", "День культурного різноманіття"),
            ("2022-11-02", "День усіх померлих"),
            ("2022-12-25", "День родини"),
        )
