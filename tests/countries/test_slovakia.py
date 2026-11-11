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

from holidays.constants import PUBLIC, SCHOOL, WORKDAY
from holidays.countries.slovakia import Slovakia
from tests.common import CommonCountryTests


class TestSlovakia(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            Slovakia, with_subdiv_categories=True, years_all_subdivs=range(2014, 2050)
        )

    def test_no_holidays(self):
        super().test_no_holidays()

        self.assertNoHolidays(Slovakia(categories=WORKDAY, years=range(self.start_year, 2021)))

        self.assertNoHolidays(Slovakia(categories=SCHOOL, years=self.full_range))
        for subdiv in Slovakia.subdivisions:
            self.assertNoHolidays(
                Slovakia(subdiv=subdiv, categories=SCHOOL, years=range(self.start_year, 2014))
            )

    def test_special_holidays(self):
        self.assertHoliday(
            "2018-10-30",
        )

    def test_day_of_the_establishment_of_the_slovak_republic(self):
        self.assertHolidayName(
            "Deň vzniku Slovenskej republiky", (f"{year}-01-01" for year in self.full_range)
        )

    def test_epiphany(self):
        self.assertHolidayName(
            "Zjavenie Pána (Traja králi a vianočný sviatok pravoslávnych kresťanov)",
            (f"{year}-01-06" for year in self.full_range),
        )

    def test_good_friday(self):
        name = "Veľký piatok"
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

    def test_easter_monday(self):
        name = "Veľkonočný pondelok"
        self.assertHolidayName(
            name,
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        self.assertHolidayName("Sviatok práce", (f"{year}-05-01" for year in self.full_range))

    def test_day_of_victory_over_fascism(self):
        name = "Deň víťazstva nad fašizmom"
        self.assertHolidayName(
            name, (f"{year}-05-08" for year in (*range(1997, 2026), *range(2027, self.end_year)))
        )
        self.assertNoHolidayName(name, range(self.start_year, 1997), 2026)
        self.assertWorkdayHolidayName(name, "2026-05-08")
        self.assertNoWorkdayHolidayName(
            name, range(self.start_year, 2026), range(2027, self.end_year)
        )

    def test_saints_cyril_and_methodius_day(self):
        self.assertHolidayName(
            "Sviatok svätého Cyrila a svätého Metoda",
            (f"{year}-07-05" for year in self.full_range),
        )

    def test_slovak_national_uprising_anniversary(self):
        self.assertHolidayName(
            "Výročie Slovenského národného povstania",
            (f"{year}-08-29" for year in self.full_range),
        )

    def test_constitution_day(self):
        name = "Deň Ústavy Slovenskej republiky"
        # PUBLIC.
        self.assertHolidayName(name, (f"{year}-09-01" for year in range(self.start_year, 2024)))
        self.assertNoHolidayName(name, range(2024, self.end_year))
        # WORKDAY.
        self.assertWorkdayHolidayName(
            name, (f"{year}-09-01" for year in range(2024, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2024))

    def test_day_of_our_lady_of_the_seven_sorrows(self):
        name = "Sedembolestná Panna Mária"
        self.assertHolidayName(
            name,
            (
                f"{year}-09-15"
                for year in (*range(self.start_year, 2026), *range(2027, self.end_year))
            ),
        )
        self.assertNoHolidayName(name, 2026)
        self.assertWorkdayHolidayName(name, "2026-09-15")
        self.assertNoWorkdayHolidayName(
            name, range(self.start_year, 2026), range(2027, self.end_year)
        )

    def test_day_of_the_establishment_of_the_czech_slovak_state(self):
        name = "Deň vzniku samostatného česko-slovenského štátu"
        self.assertNoHolidayName(name)
        self.assertWorkdayHolidayName(
            name, (f"{year}-10-28" for year in range(2021, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2021))

    def test_all_saints_day(self):
        self.assertHolidayName(
            "Sviatok Všetkých svätých", (f"{year}-11-01" for year in self.full_range)
        )

    def test_struggle_for_freedom_and_democracy_day(self):
        name = "Deň boja za slobodu a demokraciu"
        # PUBLIC.
        self.assertHolidayName(name, (f"{year}-11-17" for year in range(2001, 2025)))
        self.assertNoHolidayName(name, range(self.start_year, 2001), range(2025, self.end_year))
        # WORKDAY.
        self.assertWorkdayHolidayName(
            name, (f"{year}-11-17" for year in range(2025, self.end_year))
        )
        self.assertNoWorkdayHolidayName(name, range(self.start_year, 2025))

    def test_christmas_eve(self):
        self.assertHolidayName("Štedrý deň", (f"{year}-12-24" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName(
            "Prvý sviatok vianočný", (f"{year}-12-25" for year in self.full_range)
        )

    def test_second_day_of_christmas(self):
        self.assertHolidayName(
            "Druhý sviatok vianočný", (f"{year}-12-26" for year in self.full_range)
        )

    def test_2021_public(self):
        self.assertHolidaysInYear(
            2021,
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

    def test_2021_workday(self):
        self.assertWorkdayHolidaysInYear(
            2021,
            ("2021-10-28", "Deň vzniku samostatného česko-slovenského štátu"),
        )

    def test_school_christmas_break(self):
        name = "Vianočné prázdniny"
        self.assertNoHolidayName(name)
        for holidays in self.subdiv_school_holidays.values():
            self.assertHolidayName(
                name,
                holidays,
                "2014-01-01",
                "2014-01-07",
                # Dec 22 is part of the break when Dec 23 falls on a Tuesday.
                "2014-12-22",
                "2014-12-31",
                "2023-12-23",
                "2023-12-31",
                "2025-12-22",
                "2025-12-31",
                "2026-01-01",
                "2026-01-07",
                "2026-12-23",
                "2026-12-31",
            )
            self.assertNoHoliday(
                holidays,
                "2014-01-08",
                "2014-12-21",
                "2023-12-22",
                "2025-12-21",
                "2026-01-08",
                "2026-12-22",
            )
            self.assertHolidayName(name, holidays, range(2014, self.end_year))
            for year in range(2014, self.end_year):
                self.assertHolidayNameCount(
                    name, 17 if year in {2014, 2025, 2031, 2036, 2042} else 16, holidays, year
                )

    def test_school_half_year_break(self):
        name = "Polročné prázdniny"
        self.assertNoHolidayName(name)
        for holidays in self.subdiv_school_holidays.values():
            self.assertHolidayName(
                name,
                holidays,
                "2014-02-03",
                "2015-02-02",
                "2016-02-01",
                "2017-02-03",
                "2018-02-02",
                "2019-02-01",
                "2020-02-03",
                "2021-02-01",
                "2022-02-04",
                "2026-02-02",
                "2027-02-01",
            )
            self.assertHolidayName(name, holidays, range(2014, 2023), range(2026, self.end_year))
            self.assertNoHolidayName(name, holidays, range(2023, 2026))
            self.assertHolidayNameCount(
                name, 1, holidays, range(2014, 2023), range(2026, self.end_year)
            )

    def test_school_spring_break(self):
        name = "Jarné prázdniny"
        self.assertNoHolidayName(name)
        for subdivs, dts, no_dts in (
            (
                # Central Slovakia: Banskobystrický, Trenčiansky, Žilinský kraj.
                ("BC", "TC", "ZI"),
                (
                    "2014-02-17",
                    "2014-02-21",
                    "2015-02-16",
                    "2015-02-20",
                    "2016-02-29",
                    "2016-03-04",
                    "2017-02-27",
                    "2017-03-03",
                    "2018-02-19",
                    "2018-02-23",
                    "2019-03-04",
                    "2019-03-08",
                    "2020-02-24",
                    "2020-02-28",
                    "2021-02-15",
                    "2021-02-19",
                    "2022-03-07",
                    "2022-03-11",
                    "2023-02-27",
                    "2023-03-03",
                    "2024-02-19",
                    "2024-02-23",
                    "2025-03-03",
                    "2025-03-07",
                    "2026-02-23",
                    "2026-02-27",
                    "2027-02-15",
                    "2027-02-19",
                ),
                ("2014-02-16", "2014-02-22", "2026-02-22", "2026-02-28"),
            ),
            (
                # Eastern Slovakia: Košický, Prešovský kraj.
                ("KI", "PV"),
                (
                    "2014-03-03",
                    "2014-03-07",
                    "2015-02-23",
                    "2015-02-27",
                    "2016-02-15",
                    "2016-02-19",
                    "2017-03-06",
                    "2017-03-10",
                    "2018-02-26",
                    "2018-03-02",
                    "2019-02-18",
                    "2019-02-22",
                    "2020-03-02",
                    "2020-03-06",
                    "2021-02-22",
                    "2021-02-26",
                    "2022-02-21",
                    "2022-02-25",
                    "2023-03-06",
                    "2023-03-10",
                    "2024-02-26",
                    "2024-03-01",
                    "2025-02-17",
                    "2025-02-21",
                    "2026-03-02",
                    "2026-03-06",
                    "2027-02-22",
                    "2027-02-26",
                ),
                ("2014-03-02", "2014-03-08", "2026-03-01", "2026-03-07"),
            ),
            (
                # Western Slovakia: Bratislavský, Nitriansky, Trnavský kraj.
                ("BL", "NI", "TA"),
                (
                    "2014-02-24",
                    "2014-02-28",
                    "2015-03-02",
                    "2015-03-06",
                    "2016-02-22",
                    "2016-02-26",
                    "2017-02-20",
                    "2017-02-24",
                    "2018-03-05",
                    "2018-03-09",
                    "2019-02-25",
                    "2019-03-01",
                    "2020-02-17",
                    "2020-02-21",
                    "2021-03-01",
                    "2021-03-05",
                    "2022-02-28",
                    "2022-03-04",
                    "2023-02-20",
                    "2023-02-24",
                    "2024-03-04",
                    "2024-03-08",
                    "2025-02-24",
                    "2025-02-28",
                    "2026-02-16",
                    "2026-02-20",
                    "2027-03-01",
                    "2027-03-05",
                ),
                ("2014-02-23", "2014-03-01", "2026-02-15", "2026-02-21"),
            ),
        ):
            for subdiv in subdivs:
                holidays = self.subdiv_school_holidays[subdiv]
                self.assertHolidayName(name, holidays, *dts)
                self.assertNoHoliday(holidays, *no_dts)
                self.assertHolidayName(name, holidays, range(2014, self.end_year))
                self.assertHolidayNameCount(name, 5, holidays, range(2014, self.end_year))

    def test_school_easter_break(self):
        name = "Veľkonočné prázdniny"
        self.assertNoHolidayName(name)
        for holidays in self.subdiv_school_holidays.values():
            self.assertHolidayName(
                name,
                holidays,
                "2014-04-17",
                "2014-04-22",
                "2024-03-28",
                "2024-04-02",
                "2025-04-17",
                "2025-04-22",
                "2026-04-02",
                "2026-04-07",
                "2027-03-25",
                "2027-03-30",
            )
            self.assertNoHoliday(holidays, "2026-04-01", "2026-04-08")
            self.assertHolidayName(name, holidays, range(2014, self.end_year))
            self.assertHolidayNameCount(name, 6, holidays, range(2014, self.end_year))

    def test_school_summer_break(self):
        name = "Letné prázdniny"
        self.assertNoHolidayName(name)
        for holidays in self.subdiv_school_holidays.values():
            self.assertHolidayName(
                name,
                holidays,
                # Jun 30 is part of the break when it falls on a Monday.
                "2014-06-30",
                "2014-08-31",
                "2024-07-01",
                "2024-08-31",
                "2024-09-01",
                "2025-06-30",
                "2025-08-31",
                "2026-07-01",
                "2026-08-31",
                "2028-07-01",
                "2028-09-01",
            )
            self.assertNoHoliday(
                holidays,
                "2014-06-29",
                "2024-06-30",
                "2024-09-02",
                "2025-06-29",
                "2026-06-30",
                "2028-06-30",
                "2028-09-02",
            )
            self.assertHolidayName(name, holidays, range(2014, self.end_year))
            for year in range(2014, self.end_year):
                self.assertHolidayNameCount(
                    name,
                    63 if year in {2014, 2024, 2025, 2028, 2031, 2036, 2042} else 62,
                    holidays,
                    year,
                )

    def test_school_autumn_break(self):
        name = "Jesenné prázdniny"
        self.assertNoHolidayName(name)
        for holidays in self.subdiv_school_holidays.values():
            self.assertHolidayName(
                name,
                holidays,
                "2014-10-30",
                "2014-10-31",
                "2015-10-29",
                "2015-10-30",
                "2016-10-28",
                "2016-10-31",
                "2017-10-30",
                "2017-10-31",
                "2018-10-31",
                "2018-11-02",
                "2019-10-30",
                "2019-10-31",
                # Ministerial Decision 2020/17949:1-A1810 of Oct 23, 2020.
                "2020-10-30",
                "2020-11-02",
                "2020-11-06",
                "2020-11-09",
                "2021-10-28",
                "2021-10-29",
                "2022-10-28",
                "2022-10-31",
                "2023-10-30",
                "2023-10-31",
                "2024-10-30",
                "2024-10-31",
                "2025-10-30",
                "2025-10-31",
                "2026-10-29",
                "2026-10-30",
                "2027-10-28",
                "2027-10-29",
            )
            self.assertNoHoliday(
                holidays,
                "2014-10-29",
                "2015-10-31",
                "2020-10-29",
                "2021-10-30",
                "2026-10-28",
                "2026-10-31",
            )
            self.assertHolidayName(name, holidays, range(2014, self.end_year))
            for year in range(2014, self.end_year):
                self.assertHolidayNameCount(
                    name,
                    4
                    if year in {2016, 2020, 2022, 2033, 2039, 2044}
                    else 3
                    if year in {2018, 2029, 2035, 2040, 2046}
                    else 2,
                    holidays,
                    year,
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
            categories=(PUBLIC, WORKDAY),
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
            ("2022-07-05", "Saints Cyril and Methodius Day"),
            ("2022-08-29", "Slovak National Uprising Anniversary"),
            ("2022-09-01", "Constitution Day"),
            ("2022-09-15", "Day of Our Lady of the Seven Sorrows"),
            ("2022-10-28", "Day of the Establishment of the Independent Czech-Slovak State"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-17", "Struggle for Freedom and Democracy Day"),
            ("2022-12-24", "Christmas Eve"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
            categories=(PUBLIC, WORKDAY),
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
            categories=(PUBLIC, WORKDAY),
        )

    def _assert_school_l10n(self, language, *expected):
        for subdiv, dt, name in expected:
            self.assertHolidayName(
                name,
                Slovakia(subdiv=subdiv, years=2026, language=language, categories=SCHOOL),
                dt,
            )

    def test_l10n_default_school(self):
        self._assert_school_l10n(
            None,
            ("BL", "2026-01-01", "Vianočné prázdniny"),
            ("BL", "2026-02-02", "Polročné prázdniny"),
            ("BL", "2026-02-16", "Jarné prázdniny"),
            ("BC", "2026-02-23", "Jarné prázdniny"),
            ("KI", "2026-03-02", "Jarné prázdniny"),
            ("BL", "2026-04-02", "Veľkonočné prázdniny"),
            ("BL", "2026-07-01", "Letné prázdniny"),
            ("BL", "2026-10-29", "Jesenné prázdniny"),
        )

    def test_l10n_en_us_school(self):
        self._assert_school_l10n(
            "en_US",
            ("BL", "2026-01-01", "Christmas Break"),
            ("BL", "2026-02-02", "Half-Year Break"),
            ("BL", "2026-02-16", "Spring Break"),
            ("BC", "2026-02-23", "Spring Break"),
            ("KI", "2026-03-02", "Spring Break"),
            ("BL", "2026-04-02", "Easter Break"),
            ("BL", "2026-07-01", "Summer Break"),
            ("BL", "2026-10-29", "Autumn Break"),
        )

    def test_l10n_uk_school(self):
        self._assert_school_l10n(
            "uk",
            ("BL", "2026-01-01", "Різдвяні канікули"),
            ("BL", "2026-02-02", "Піврічні канікули"),
            ("BL", "2026-02-16", "Весняні канікули"),
            ("BC", "2026-02-23", "Весняні канікули"),
            ("KI", "2026-03-02", "Весняні канікули"),
            ("BL", "2026-04-02", "Великодні канікули"),
            ("BL", "2026-07-01", "Літні канікули"),
            ("BL", "2026-10-29", "Осінні канікули"),
        )
