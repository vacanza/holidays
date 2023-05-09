#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)


from holidays.countries.slovakia import Slovakia, SK, SVK
from tests.common import TestCase


class TestSlovakia(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Slovakia, years=range(1990, 2023))

    def test_country_aliases(self):
        self.assertCountryAliases(Slovakia, SK, SVK)

    def test_special_holidays(self):
        self.assertHoliday(
            "2018-10-30",
        )

    def test_new_years_day(self):
        self.assertHolidaysName(
            "Deň vzniku Slovenskej republiky",
            (f"{year}-01-01" for year in range(1990, 2023)),
        )

    def test_epiphany(self):
        self.assertHolidaysName(
            "Zjavenie Pána (Traja králi a "
            "vianočnýsviatok pravoslávnych kresťanov)",
            (f"{year}-01-06" for year in range(1990, 2023)),
        )

    def test_good_friday(self):
        self.assertHolidaysName(
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
        self.assertHolidaysName(
            "Sviatok práce",
            (f"{year}-05-01" for year in range(1990, 2023)),
        )

    def test_day_of_victory_over_fascizm(self):
        self.assertHolidaysName(
            "Deň víťazstva nad fašizmom",
            (f"{year}-05-08" for year in range(1997, 2023)),
        )
        self.assertNoHoliday(f"{year}-05-08" for year in range(1950, 1997))

    def test_cyril_and_methodius_day(self):
        self.assertHolidaysName(
            "Sviatok svätého Cyrila a svätého Metoda",
            (f"{year}-07-05" for year in range(1990, 2023)),
        )

    def test_slovak_national_uprising(self):
        self.assertHolidaysName(
            "Výročie Slovenského národného povstania",
            (f"{year}-08-29" for year in range(1990, 2023)),
        )

    def test_constitution_day(self):
        self.assertHolidaysName(
            "Deň Ústavy Slovenskej republiky",
            (f"{year}-09-01" for year in range(1992, 2023)),
        )
        self.assertNoHoliday(f"{year}-09-01" for year in range(1950, 1992))

    def test_Day_of_our_lady_of_the_seven_sorrows(self):
        self.assertHolidaysName(
            "Sedembolestná Panna Mária",
            (f"{year}-09-15" for year in range(1990, 2023)),
        )

    def test_all_saints_day(self):
        self.assertHolidaysName(
            "Sviatok Všetkých svätých",
            (f"{year}-11-01" for year in range(1990, 2023)),
        )

    def test_day_of_freedom_and_democracy(self):
        self.assertHolidaysName(
            "Deň boja za slobodu a demokraciu",
            (f"{year}-11-17" for year in range(2001, 2023)),
        )
        self.assertNoHoliday(f"{year}-11-17" for year in range(1950, 2001))

    def test_christmas_eve(self):
        self.assertHolidaysName(
            "Štedrý deň",
            (f"{year}-12-24" for year in range(1990, 2023)),
        )

    def test_christmas_day(self):
        self.assertHolidaysName(
            "Prvý sviatok vianočný",
            (f"{year}-12-25" for year in range(1990, 2023)),
        )

    def test_stephens_day(self):
        self.assertHolidaysName(
            "Druhý sviatok vianočný",
            (f"{year}-12-26" for year in range(1990, 2023)),
        )

    def test_2022(self):
        self.assertHolidays(
            Slovakia(years=2022),
            ("2022-01-01", "Deň vzniku Slovenskej republiky"),
            (
                "2022-01-06",
                "Zjavenie Pána (Traja králi a "
                "vianočnýsviatok pravoslávnych kresťanov)",
            ),
            ("2022-04-15", "Veľký piatok"),
            ("2022-04-18", "Veľkonočný pondelok"),
            ("2022-05-01", "Sviatok práce"),
            ("2022-05-08", "Deň víťazstva nad fašizmom"),
            ("2022-07-05", "Sviatok svätého Cyrila a svätého Metoda"),
            ("2022-08-29", "Výročie Slovenského národného povstania"),
            ("2022-09-01", "Deň Ústavy Slovenskej republiky"),
            ("2022-09-15", "Sedembolestná Panna Mária"),
            ("2022-11-01", "Sviatok Všetkých svätých"),
            ("2022-11-17", "Deň boja za slobodu a demokraciu"),
            ("2022-12-24", "Štedrý deň"),
            ("2022-12-25", "Prvý sviatok vianočný"),
            ("2022-12-26", "Druhý sviatok vianočný"),
        )
