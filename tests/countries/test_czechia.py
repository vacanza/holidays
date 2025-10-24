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

from holidays.countries.czechia import Czechia, CZ, CZE
from tests.common import CommonCountryTests


class TestCzechia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Czechia)

    def test_country_aliases(self):
        self.assertAliases(Czechia, CZ, CZE)

    def test_no_holidays(self):
        self.assertNoHolidays(Czechia(years=self.start_year - 1))

    def test_new_years_day(self):
        self.assertHolidayName(
            "Nový rok", (f"{year}-01-01" for year in range(self.start_year, 2000))
        )

    def test_independent_czech_state_day(self):
        name = "Den obnovy samostatného českého státu"
        self.assertHolidayName(name, (f"{year}-01-01" for year in range(2000, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2000))

    def test_good_friday(self):
        name = "Velký pátek"
        self.assertHolidayName(
            name,
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
        )
        self.assertHolidayName(name, range(2016, self.end_year))
        self.assertNoHolidayName(name, range(self.start_year, 2016))

    def test_easter_monday(self):
        name = "Velikonoční pondělí"
        self.assertHolidayName(
            name,
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        self.assertHolidayName("Svátek práce", (f"{year}-05-01" for year in self.full_range))

    def test_victory_day(self):
        name_1952 = "Den osvobození od fašismu"
        name_2001 = "Den osvobození"
        name_2004 = "Den vítězství"
        self.assertHolidayName(
            name_1952,
            (f"{year}-05-09" for year in range(self.start_year, 1992)),
            (f"{year}-05-08" for year in range(1992, 2001)),
        )
        self.assertHolidayName(name_2001, (f"{year}-05-08" for year in range(2001, 2004)))
        self.assertHolidayName(name_2004, (f"{year}-05-08" for year in range(2004, self.end_year)))
        self.assertNoHolidayName(name_1952, range(2001, self.end_year))
        self.assertNoHolidayName(
            name_2001, range(self.start_year, 2001), range(2004, self.end_year)
        )
        self.assertNoHolidayName(name_2004, range(self.start_year, 2004))

    def test_cyril_and_methodius_day(self):
        name = "Den slovanských věrozvěstů Cyrila a Metoděje"
        self.assertHolidayName(name, (f"{year}-07-05" for year in range(1990, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1990))

    def test_jan_hus_day(self):
        name = "Den upálení mistra Jana Husa"
        self.assertHolidayName(name, (f"{year}-07-06" for year in range(1990, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1990))

    def test_statehood_day(self):
        name = "Den české státnosti"
        self.assertHolidayName(name, (f"{year}-09-28" for year in range(2000, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2000))

    def test_independent_czechoslovak_state_day(self):
        self.assertHolidayName(
            "Den vzniku samostatného československého státu",
            (f"{year}-10-28" for year in self.full_range),
        )

    def test_struggle_for_freedom_and_democracy_day(self):
        name_1990 = "Den boje za svobodu a demokracii"
        name_2019 = "Den boje za svobodu a demokracii a Mezinárodní den studentstva"
        self.assertHolidayName(name_1990, (f"{year}-11-17" for year in range(1990, 2019)))
        self.assertHolidayName(name_2019, (f"{year}-11-17" for year in range(2019, self.end_year)))
        self.assertNoHolidayName(
            name_1990, range(self.start_year, 1990), range(2019, self.end_year)
        )
        self.assertNoHolidayName(name_2019, range(self.start_year, 2019))

    def test_christmas_eve(self):
        name = "Štědrý den"
        self.assertHolidayName(name, (f"{year}-12-24" for year in range(1990, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 1990))

    def test_christmas_day(self):
        self.assertHolidayName("1. svátek vánoční", (f"{year}-12-25" for year in self.full_range))

    def test_christmas_second_day(self):
        self.assertHolidayName("2. svátek vánoční", (f"{year}-12-26" for year in self.full_range))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Den obnovy samostatného českého státu; Nový rok"),
            ("2022-04-15", "Velký pátek"),
            ("2022-04-18", "Velikonoční pondělí"),
            ("2022-05-01", "Svátek práce"),
            ("2022-05-08", "Den vítězství"),
            ("2022-07-05", "Den slovanských věrozvěstů Cyrila a Metoděje"),
            ("2022-07-06", "Den upálení mistra Jana Husa"),
            ("2022-09-28", "Den české státnosti"),
            ("2022-10-28", "Den vzniku samostatného československého státu"),
            ("2022-11-17", "Den boje za svobodu a demokracii a Mezinárodní den studentstva"),
            ("2022-12-24", "Štědrý den"),
            ("2022-12-25", "1. svátek vánoční"),
            ("2022-12-26", "2. svátek vánoční"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "Independent Czech State Restoration Day; New Year's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-08", "Victory Day"),
            ("2022-07-05", "Saints Cyril and Methodius Day"),
            ("2022-07-06", "Jan Hus Day"),
            ("2022-09-28", "Statehood Day"),
            ("2022-10-28", "Independent Czechoslovak State Day"),
            (
                "2022-11-17",
                "Struggle for Freedom and Democracy Day and International Students' Day",
            ),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )

    def test_l10n_sk(self):
        self.assertLocalizedHolidays(
            "sk",
            ("2022-01-01", "Deň obnovy samostatného českého štátu; Nový rok"),
            ("2022-04-15", "Veľký piatok"),
            ("2022-04-18", "Veľkonočný pondelok"),
            ("2022-05-01", "Sviatok práce"),
            ("2022-05-08", "Deň víťazstva"),
            ("2022-07-05", "Deň slovanských vierozvestcov Cyrila a Metoda"),
            ("2022-07-06", "Deň upálenia majstra Jána Husa"),
            ("2022-09-28", "Deň českej štátnosti"),
            ("2022-10-28", "Deň vzniku samostatného československého štátu"),
            ("2022-11-17", "Deň boja za slobodu a demokraciu a Medzinárodný deň študentstva"),
            ("2022-12-24", "Štedrý deň"),
            ("2022-12-25", "1. sviatok vianočný"),
            ("2022-12-26", "2. sviatok vianočný"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "День відновлення незалежної чеської держави; Новий рік"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-08", "День Перемоги"),
            ("2022-07-05", "День Святих Кирила та Мефодія"),
            ("2022-07-06", "День спалення Яна Гуса"),
            ("2022-09-28", "День чеської державності"),
            ("2022-10-28", "День створення незалежної чехословацької держави"),
            ("2022-11-17", "День боротьби за свободу і демократію та Міжнародний день студентів"),
            ("2022-12-24", "Святий вечір"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "Другий день Різдва"),
        )
