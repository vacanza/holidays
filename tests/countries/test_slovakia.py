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
from holidays.countries.slovakia import Slovakia, SK, SVK
from tests.common import CommonCountryTests


class TestSlovakia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Slovakia, years=range(1993, 2050))

    def test_country_aliases(self):
        self.assertAliases(Slovakia, SK, SVK)

    def test_no_holidays(self):
        self.assertNoHolidays(Slovakia(years=1992))

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
        holidays = Slovakia(categories=WORKDAY, years=range(1993, 2050))
        self.assertHolidayName(name, holidays, (f"{year}-10-28" for year in range(2021, 2050)))
        self.assertNoHoliday(holidays, (f"{year}-10-28" for year in range(1993, 2021)))
        self.assertNoHolidayName(name, holidays, range(1993, 2021))

    def test_2021(self):
        self.assertHolidays(
            Slovakia(years=2021),
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
            Slovakia(categories=WORKDAY, years=2021),
            ("2021-10-28", "Deň vzniku samostatného česko-slovenského štátu"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Deň vzniku Slovenskej republiky"),
            (
                "2022-01-06",
                "Zjavenie Pána (Traja králi a vianočný sviatok pravoslávnych kresťanov)",
            ),
            ("2022-04-15", "Veľký piatok"),
            ("2022-04-18", "Veľkonočný pondelok"),
            ("2022-05-01", "Sviatok práce"),
            ("2022-05-08", "Deň víťazstva nad fašizmom"),
            ("2022-07-05", "Sviatok svätého Cyrila a svätého Metoda"),
            ("2022-08-29", "Výročie Slovenského národného povstania"),
            ("2022-09-01", "Deň Ústavy Slovenskej republiky"),
            ("2022-09-15", "Sedembolestná Panna Mária"),
            ("2022-10-28", "Deň vzniku samostatného česko-slovenského štátu"),
            ("2022-11-01", "Sviatok Všetkých svätých"),
            ("2022-11-17", "Deň boja za slobodu a demokraciu"),
            ("2022-12-24", "Štedrý deň"),
            ("2022-12-25", "Prvý sviatok vianočný"),
            ("2022-12-26", "Druhý sviatok vianočný"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "Day of the Establishment of the Slovak Republic"),
            ("2022-01-06", "Epiphany (Three Kings' Day and Orthodox Christmas)"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-08", "Day of Victory over Fascism"),
            ("2022-07-05", "St. Cyril and Methodius Day"),
            ("2022-08-29", "Slovak National Uprising Anniversary"),
            ("2022-09-01", "Constitution Day"),
            ("2022-09-15", "Day of Our Lady of the Seven Sorrows"),
            ("2022-10-28", "Day of the Establishment of the Independent Czech-Slovak State"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-17", "Struggle for Freedom and Democracy Day"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "День утворення Словацької Республіки"),
            ("2022-01-06", "Богоявлення (Три царі і православне Різдво Христове)"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-08", "День перемоги над фашизмом"),
            ("2022-07-05", "День Святих Кирила та Мефодія"),
            ("2022-08-29", "Річниця Словацького національного повстання"),
            ("2022-09-01", "День конституції Словацької Республіки"),
            ("2022-09-15", "День Божої Матері семи скорбот"),
            ("2022-10-28", "День створення незалежної чесько-словацької держави"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-17", "День боротьби за свободу та демократію"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )
