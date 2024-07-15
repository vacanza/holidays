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

from holidays.constants import WORKDAY
from holidays.entities.ISO_3166.SK import SkHolidays
from tests.common import CommonCountryTests


class TestSkHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SkHolidays, years=range(1993, 2050))

    def test_no_holidays(self):
        self.assertNoHolidays(SkHolidays(years=1992))

    def test_special_holidays(self):
        self.assertHoliday(
            "2018-10-30",
        )

    def test_new_years_day(self):
        self.assertHolidayName(
            "Deň vzniku Slovenskej republiky", (f"{year}-01-01" for year in range(1993, 2050))
        )

    def test_epiphany(self):
        self.assertHolidayName(
            "Zjavenie Pána (Traja králi a vianočný sviatok pravoslávnych kresťanov)",
            (f"{year}-01-06" for year in range(1993, 2050)),
        )

    def test_good_friday(self):
        self.assertHolidayName(
            "Veľký piatok",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )

    def test_easter_monday(self):
        self.assertHolidayName(
            "Veľkonočný pondelok",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )

    def test_labor_day(self):
        self.assertHolidayName("Sviatok práce", (f"{year}-05-01" for year in range(1993, 2050)))

    def test_day_of_victory_over_fascizm(self):
        name = "Deň víťazstva nad fašizmom"
        self.assertHolidayName(name, (f"{year}-05-08" for year in range(1997, 2050)))
        self.assertNoHoliday(f"{year}-05-08" for year in range(1993, 1997))
        self.assertNoHolidayName(name, range(1993, 1997))

    def test_cyril_and_methodius_day(self):
        self.assertHolidayName(
            "Sviatok svätého Cyrila a svätého Metoda",
            (f"{year}-07-05" for year in range(1993, 2050)),
        )

    def test_slovak_national_uprising(self):
        self.assertHolidayName(
            "Výročie Slovenského národného povstania",
            (f"{year}-08-29" for year in range(1993, 2050)),
        )

    def test_constitution_day(self):
        self.assertHolidayName(
            "Deň Ústavy Slovenskej republiky", (f"{year}-09-01" for year in range(1993, 2050))
        )

    def test_day_of_our_lady_of_the_seven_sorrows(self):
        self.assertHolidayName(
            "Sedembolestná Panna Mária", (f"{year}-09-15" for year in range(1993, 2050))
        )

    def test_all_saints_day(self):
        self.assertHolidayName(
            "Sviatok Všetkých svätých", (f"{year}-11-01" for year in range(1993, 2050))
        )

    def test_day_of_freedom_and_democracy(self):
        name = "Deň boja za slobodu a demokraciu"
        self.assertHolidayName(name, (f"{year}-11-17" for year in range(2001, 2050)))
        self.assertNoHoliday(f"{year}-11-17" for year in range(1993, 2001))
        self.assertNoHolidayName(name, range(1993, 2001))

    def test_christmas_eve(self):
        self.assertHolidayName("Štedrý deň", (f"{year}-12-24" for year in range(1993, 2050)))

    def test_christmas_day(self):
        self.assertHolidayName(
            "Prvý sviatok vianočný", (f"{year}-12-25" for year in range(1993, 2050))
        )

    def test_stephens_day(self):
        self.assertHolidayName(
            "Druhý sviatok vianočný", (f"{year}-12-26" for year in range(1993, 2050))
        )

    def test_establishment_state_day(self):
        name = "Deň vzniku samostatného česko-slovenského štátu"
        holidays = SkHolidays(categories=WORKDAY, years=range(1993, 2050))
        self.assertHolidayName(name, holidays, (f"{year}-10-28" for year in range(2021, 2050)))
        self.assertNoHoliday(holidays, (f"{year}-10-28" for year in range(1993, 2021)))
        self.assertNoHolidayName(name, holidays, range(1993, 2021))

    def test_2021(self):
        self.assertHolidays(
            SkHolidays(years=2021),
            ("2021-01-01", "Deň vzniku Slovenskej republiky"),
            (
                "2021-01-06",
                "Zjavenie Pána (Traja králi a vianočný sviatok pravoslávnych kresťanov)",
            ),
            ("2021-04-02", "Veľký piatok"),
            ("2021-04-05", "Veľkonočný pondelok"),
            ("2021-05-01", "Sviatok práce"),
            ("2021-05-08", "Deň víťazstva nad fašizmom"),
            ("2021-07-05", "Sviatok svätého Cyrila a svätého Metoda"),
            ("2021-08-29", "Výročie Slovenského národného povstania"),
            ("2021-09-01", "Deň Ústavy Slovenskej republiky"),
            ("2021-09-15", "Sedembolestná Panna Mária"),
            ("2021-11-01", "Sviatok Všetkých svätých"),
            ("2021-11-17", "Deň boja za slobodu a demokraciu"),
            ("2021-12-24", "Štedrý deň"),
            ("2021-12-25", "Prvý sviatok vianočný"),
            ("2021-12-26", "Druhý sviatok vianočný"),
        )

    def test_workday_2021(self):
        self.assertHolidays(
            SkHolidays(categories=WORKDAY, years=2021),
            ("2021-10-28", "Deň vzniku samostatného česko-slovenského štátu"),
        )
