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

from holidays.countries.czechia import Czechia, CZ, CZE
from tests.common import CommonCountryTests


class TestCzechia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Czechia, years=range(1945, 2050))

    def test_country_aliases(self):
        self.assertAliases(Czechia, CZ, CZE)

    def test_new_years_day(self):
        name_1 = "Nový rok"
        name_2 = "Den obnovy samostatného českého státu"
        self.assertHolidayName(name_1, (f"{year}-01-01" for year in range(1945, 2000)))
        self.assertHolidayName(name_2, (f"{year}-01-01" for year in range(2000, 2050)))
        self.assertNoHolidayName(name_1, range(2000, 2050))
        self.assertNoHolidayName(name_2, range(1945, 2000))

    def test_good_friday(self):
        name = "Velký pátek"
        self.assertHolidayName(
            name,
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
        )
        self.assertNoHolidayName(name, range(1952, 2016))

    def test_easter_monday(self):
        self.assertHolidayName(
            "Velikonoční pondělí",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )

    def test_labor_day(self):
        name = "Svátek práce"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1951, 2050)))
        self.assertNoHoliday(f"{year}-05-01" for year in range(1945, 1951))
        self.assertNoHolidayName(name, range(1945, 1951))

    def test_victory_day(self):
        name_1 = "Den vítězství nad hitlerovským fašismem"
        name_2 = "Den vítězství"
        self.assertHolidayName(name_1, (f"{year}-05-09" for year in range(1947, 1992)))
        self.assertHolidayName(name_2, (f"{year}-05-08" for year in range(1992, 2050)))
        self.assertNoHoliday(f"{year}-05-09" for year in range(1945, 1947))
        self.assertNoHoliday(f"{year}-05-09" for year in range(1992, 2050))
        self.assertNoHoliday(f"{year}-05-08" for year in range(1945, 1992))
        self.assertNoHolidayName(name_1, range(1945, 1947), range(1992, 2050))
        self.assertNoHolidayName(name_2, range(1945, 1992))

    def test_cyril_and_methodius_day(self):
        name = "Den slovanských věrozvěstů Cyrila a Metoděje"
        self.assertHolidayName(name, (f"{year}-07-05" for year in range(1951, 2050)))
        self.assertNoHoliday(f"{year}-07-05" for year in range(1945, 1951))
        self.assertNoHolidayName(name, range(1945, 1951))

    def test_jan_hus_day(self):
        name = "Den upálení mistra Jana Husa"
        self.assertHolidayName(name, (f"{year}-07-06" for year in range(1951, 2050)))
        self.assertNoHoliday(f"{year}-07-06" for year in range(1945, 1951))
        self.assertNoHolidayName(name, range(1945, 1951))

    def test_statehood_day(self):
        name = "Den české státnosti"
        self.assertHolidayName(name, (f"{year}-09-28" for year in range(2000, 2050)))
        self.assertNoHoliday(f"{year}-09-28" for year in range(1945, 2000))
        self.assertNoHolidayName(name, range(1945, 2000))

    def test_independent_czechoslovak_state_day(self):
        name = "Den vzniku samostatného československého státu"
        self.assertHolidayName(name, (f"{year}-10-28" for year in range(1951, 2050)))
        self.assertNoHoliday(f"{year}-10-28" for year in range(1945, 1951))
        self.assertNoHolidayName(name, range(1945, 1951))

    def test_struggle_for_freedom_and_democracy_day(self):
        name = "Den boje za svobodu a demokracii"
        self.assertHolidayName(name, (f"{year}-11-17" for year in range(1990, 2050)))
        self.assertNoHoliday(f"{year}-11-17" for year in range(1945, 1990))
        self.assertNoHolidayName(name, range(1945, 1990))

    def test_christmas_eve(self):
        name = "Štědrý den"
        self.assertHolidayName(name, (f"{year}-12-24" for year in range(1990, 2050)))
        self.assertNoHoliday(f"{year}-12-24" for year in range(1945, 1990))
        self.assertNoHolidayName(name, range(1945, 1990))

    def test_christmas_day(self):
        name = "1. svátek vánoční"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1951, 2050)))
        self.assertNoHoliday(f"{year}-12-25" for year in range(1945, 1951))
        self.assertNoHolidayName(name, range(1945, 1951))

    def test_christmas_second_day(self):
        name = "2. svátek vánoční"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1951, 2050)))
        self.assertNoHoliday(f"{year}-12-26" for year in range(1945, 1951))
        self.assertNoHolidayName(name, range(1945, 1951))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Den obnovy samostatného českého státu"),
            ("2022-04-15", "Velký pátek"),
            ("2022-04-18", "Velikonoční pondělí"),
            ("2022-05-01", "Svátek práce"),
            ("2022-05-08", "Den vítězství"),
            ("2022-07-05", "Den slovanských věrozvěstů Cyrila a Metoděje"),
            ("2022-07-06", "Den upálení mistra Jana Husa"),
            ("2022-09-28", "Den české státnosti"),
            ("2022-10-28", "Den vzniku samostatného československého státu"),
            ("2022-11-17", "Den boje za svobodu a demokracii"),
            ("2022-12-24", "Štědrý den"),
            ("2022-12-25", "1. svátek vánoční"),
            ("2022-12-26", "2. svátek vánoční"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "Independent Czech State Restoration Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-08", "Victory Day"),
            ("2022-07-05", "Saints Cyril and Methodius Day"),
            ("2022-07-06", "Jan Hus Day"),
            ("2022-09-28", "Statehood Day"),
            ("2022-10-28", "Independent Czechoslovak State Day"),
            ("2022-11-17", "Struggle for Freedom and Democracy Day"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )

    def test_l10n_sk(self):
        self.assertLocalizedHolidays(
            "sk",
            ("2022-01-01", "Deň obnovy samostatného českého štátu"),
            ("2022-04-15", "Veľký piatok"),
            ("2022-04-18", "Veľkonočný pondelok"),
            ("2022-05-01", "Sviatok práce"),
            ("2022-05-08", "Deň víťazstva"),
            ("2022-07-05", "Deň slovanských vierozvestcov Cyrila a Metoda"),
            ("2022-07-06", "Deň upálenia majstra Jána Husa"),
            ("2022-09-28", "Deň českej štátnosti"),
            ("2022-10-28", "Deň vzniku samostatného československého štátu"),
            ("2022-11-17", "Deň boja za slobodu a demokraciu"),
            ("2022-12-24", "Štedrý deň"),
            ("2022-12-25", "1. sviatok vianočný"),
            ("2022-12-26", "2. sviatok vianočný"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "День відновлення незалежної чеської держави"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-08", "День перемоги"),
            ("2022-07-05", "День Святих Кирила та Мефодія"),
            ("2022-07-06", "День спалення Яна Гуса"),
            ("2022-09-28", "День чеської державності"),
            ("2022-10-28", "День створення незалежної чехословацької держави"),
            ("2022-11-17", "День боротьби за свободу і демократію"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )
