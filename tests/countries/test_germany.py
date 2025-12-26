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

import warnings
from unittest import TestCase

from holidays.constants import CATHOLIC
from holidays.countries.germany import Germany
from tests.common import CommonCountryTests


class TestGermany(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Germany, with_subdiv_categories=True)

    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_subdiv_deprecation(self):
        self.assertDeprecatedSubdivisions("This subdivision is deprecated and will be removed")

    def test_deprecated(self):
        self.assertEqual(
            sorted(Germany(subdiv="BYP", years=2023).keys()),
            sorted(Germany(subdiv="BY", years=2023).keys()),
        )

    def test_no_holidays(self):
        super().test_no_holidays()

        for subdiv in Germany.subdivisions:
            self.assertNoHolidays(Germany(years=self.start_year - 1, subdiv=subdiv))
        for subdiv in ("BY", "SN", "TH"):
            self.assertNoHolidays(
                Germany(subdiv=subdiv, years=self.start_year - 1, categories=CATHOLIC)
            )

    def test_special_holidays(self):
        # 2017's Reformation Day is tested in test_reformation_day.
        be_dts = (
            "2020-05-08",
            "2025-05-08",
            "2028-06-17",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            # Berlin.
            if subdiv == "BE":
                self.assertHoliday(holidays, be_dts)
            else:
                self.assertNoHoliday(holidays, be_dts)

    def test_new_years_day(self):
        self.assertHolidayName("Neujahr", (f"{year}-01-01" for year in self.full_range))

    def test_epiphany(self):
        name = "Heilige Drei Könige"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Bayern, Sachsen, Thüringen, Augsburg.
            if subdiv in {"BW", "BY", "ST", "Augsburg"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-06" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_womens_day(self):
        name = "Frauentag"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Berlin - 2019.
            if subdiv == "BE":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-08" for year in range(2019, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2019))
            # Mecklenburg-Vorpommern - 2023.
            elif subdiv == "MV":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-08" for year in range(2023, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2023))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_good_friday(self):
        name = "Karfreitag"
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

    def test_easter_sunday(self):
        name = "Ostersonntag"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Brandenburg.
            if subdiv == "BB":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-04-12",
                    "2021-04-04",
                    "2022-04-17",
                    "2023-04-09",
                    "2024-03-31",
                    "2025-04-20",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_easter_monday(self):
        name = "Ostermontag"
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

    def test_ascension_day(self):
        name = "Christi Himmelfahrt"
        self.assertHolidayName(
            name,
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, self.full_range)

    def test_labor_day(self):
        self.assertHolidayName("Erster Mai", (f"{year}-05-01" for year in self.full_range))

    def test_whit_sunday(self):
        name = "Pfingstsonntag"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Brandenburg.
            if subdiv == "BB":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-05-31",
                    "2021-05-23",
                    "2022-06-05",
                    "2023-05-28",
                    "2024-05-19",
                    "2025-06-08",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_whit_monday(self):
        name = "Pfingstmontag"
        self.assertHolidayName(
            name,
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.full_range)

    def test_corpus_christi(self):
        name = "Fronleichnam"
        self.assertNoHolidayName(name)
        dts = (
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
            "2025-06-19",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            # Baden-Württemberg, Bayern, Hessen, Nordrhein-Westfalen,
            # Rheinland-Pfalz, Saarland, Augsburg.
            if subdiv in {"BW", "BY", "HE", "NW", "RP", "SL", "Augsburg"}:
                self.assertHolidayName(name, holidays, dts)
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

        # Sachsen, Thüringen.
        self.assertSubdivSnCatholicHolidayName(name, dts)
        self.assertSubdivSnCatholicHolidayName(name, self.full_range)
        self.assertSubdivThCatholicHolidayName(name, dts)
        self.assertSubdivThCatholicHolidayName(name, self.full_range)

    def test_augsburg_peace_festival(self):
        name = "Augsburger Hohes Friedensfest"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Augsburg.
            if subdiv == "Augsburg":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-08" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_assumption_day(self):
        name = "Mariä Himmelfahrt"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Saarland.
            if subdiv == "SL":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-15" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

        # Bayern.
        self.assertSubdivByCatholicHolidayName(name, (f"{year}-08-15" for year in self.full_range))

    def test_world_childrens_day(self):
        name = "Weltkindertag"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Thüringen.
            if subdiv == "TH":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-20" for year in range(2019, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2019))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_german_unity_day(self):
        self.assertHolidayName(
            "Tag der Deutschen Einheit", (f"{year}-10-03" for year in self.full_range)
        )

    def test_reformation_day(self):
        name = "Reformationstag"
        for subdiv, holidays in self.subdiv_holidays.items():
            # Brandenburg, Mecklenburg-Vorpommern, Sachsen, Sachsen-Anhalt, Thüringen.
            if subdiv in {"BB", "MV", "SN", "ST", "TH"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-31" for year in self.full_range)
                )
            # Bremen, Hamburg, Niedersachsen, Schleswig-Holstein.
            elif subdiv in {"HB", "HH", "NI", "SH"}:
                # While these subdivisions started their holiday observance in 2018,
                # this is de facto implemented in 2017's nationwide special observance.
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-31" for year in range(2017, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2017))
            else:
                self.assertHolidayName(name, holidays, "2017-10-31")
                self.assertNoHolidayName(
                    name, holidays, range(self.start_year, 2017), range(2018, self.end_year)
                )
        self.assertHolidayName(name, "2017-10-31")

    def test_all_saints_day(self):
        name = "Allerheiligen"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Baden-Württemberg, Bayern, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Augsburg.
            if subdiv in {"BW", "BY", "NW", "RP", "SL", "Augsburg"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_repentance_and_prayer_day(self):
        name = "Buß- und Bettag"
        dts_pre_1995 = (
            "1991-11-20",
            "1992-11-18",
            "1993-11-17",
            "1994-11-16",
        )
        dts = (
            "2020-11-18",
            "2021-11-17",
            "2022-11-16",
            "2023-11-22",
            "2024-11-20",
            "2025-11-19",
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            # Sachsen.
            if subdiv == "SN":
                self.assertHolidayName(name, holidays, dts, dts_pre_1995)
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertHolidayName(name, holidays, dts_pre_1995)
                self.assertNoHolidayName(name, holidays, range(1995, self.end_year))
        self.assertHolidayName(name, dts_pre_1995)
        self.assertNoHolidayName(name, range(1995, self.end_year))

    def test_christmas_day(self):
        self.assertHolidayName(
            "Erster Weihnachtstag", (f"{year}-12-25" for year in self.full_range)
        )

    def test_second_day_of_christmas(self):
        self.assertHolidayName(
            "Zweiter Weihnachtstag", (f"{year}-12-26" for year in self.full_range)
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Neujahr"),
            ("2022-01-06", "Heilige Drei Könige"),
            ("2022-03-08", "Frauentag"),
            ("2022-04-15", "Karfreitag"),
            ("2022-04-17", "Ostersonntag"),
            ("2022-04-18", "Ostermontag"),
            ("2022-05-01", "Erster Mai"),
            ("2022-05-26", "Christi Himmelfahrt"),
            ("2022-06-05", "Pfingstsonntag"),
            ("2022-06-06", "Pfingstmontag"),
            ("2022-06-16", "Fronleichnam"),
            ("2022-08-08", "Augsburger Hohes Friedensfest"),
            ("2022-08-15", "Mariä Himmelfahrt"),
            ("2022-09-20", "Weltkindertag"),
            ("2022-10-03", "Tag der Deutschen Einheit"),
            ("2022-10-31", "Reformationstag"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-11-16", "Buß- und Bettag"),
            ("2022-12-25", "Erster Weihnachtstag"),
            ("2022-12-26", "Zweiter Weihnachtstag"),
        )


class TestGermanySaarlandSchoolHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Germany, with_subdiv_categories=True)

    def test_christmas_cross_year(self):
        # 2025 Christmas range spans 2025->2026. Ensure per-year population.
        h_2025 = Germany(years=2025, subdiv="SL", categories=("school",))
        self.assertIn("2025-12-22", h_2025)
        self.assertEqual(h_2025["2025-12-22"], "Weihnachtsferien")

        h_2026 = Germany(years=2026, subdiv="SL", categories=("school",))
        self.assertIn("2026-01-01", h_2026)
        self.assertEqual(h_2026["2026-01-01"], "Weihnachtsferien")
        self.assertNotIn("2025-12-22", h_2026)

    def test_key_2026_ranges(self):
        h = Germany(years=2026, subdiv="SL", categories=("school",))
        self.assertIn("2026-02-16", h)
        self.assertEqual(h["2026-02-16"], "Fastnachtsferien")
        self.assertIn("2026-04-07", h)
        self.assertEqual(h["2026-04-07"], "Osterferien")
        self.assertIn("2026-06-29", h)
        self.assertEqual(h["2026-06-29"], "Sommerferien")
        self.assertIn("2026-08-07", h)
        self.assertEqual(h["2026-08-07"], "Sommerferien")
        self.assertIn("2026-10-05", h)
        self.assertEqual(h["2026-10-05"], "Herbstferien")

    def test_2029_and_2030_ranges(self):
        h_2029 = Germany(years=2029, subdiv="SL", categories=("school",))
        self.assertIn("2029-05-22", h_2029)
        self.assertEqual(h_2029["2029-05-22"], "Pfingstferien")
        self.assertIn("2029-07-16", h_2029)
        self.assertEqual(h_2029["2029-07-16"], "Sommerferien")
        self.assertIn("2029-12-21", h_2029)
        self.assertEqual(h_2029["2029-12-21"], "Weihnachtsferien")

        h_2030 = Germany(years=2030, subdiv="SL", categories=("school",))
        self.assertIn("2030-01-01", h_2030)
        self.assertEqual(h_2030["2030-01-01"], "Weihnachtsferien")
        self.assertIn("2030-02-25", h_2030)
        self.assertEqual(h_2030["2030-02-25"], "Fastnachtsferien")
        self.assertIn("2030-07-22", h_2030)
        self.assertEqual(h_2030["2030-07-22"], "Sommerferien")


class TestGermanyThuringiaSchoolHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Germany, with_subdiv_categories=True)

    def test_christmas_cross_year(self):
        # 2025 Christmas range spans 2025->2026. Ensure per-year population.
        h_2025 = Germany(years=2025, subdiv="TH", categories=("school",))
        self.assertIn("2025-12-22", h_2025)
        self.assertEqual(h_2025["2025-12-22"], "Weihnachtsferien")

        h_2026 = Germany(years=2026, subdiv="TH", categories=("school",))
        self.assertIn("2026-01-01", h_2026)
        self.assertEqual(h_2026["2026-01-01"], "Weihnachtsferien")
        self.assertNotIn("2025-12-22", h_2026)

    def test_key_2026_ranges(self):
        h = Germany(years=2026, subdiv="TH", categories=("school",))
        self.assertIn("2026-02-16", h)
        self.assertEqual(h["2026-02-16"], "Winterferien")
        self.assertIn("2026-04-07", h)
        self.assertEqual(h["2026-04-07"], "Osterferien")
        self.assertIn("2026-05-15", h)
        self.assertEqual(h["2026-05-15"], "Schulfreier Tag")
        self.assertIn("2026-07-04", h)
        self.assertEqual(h["2026-07-04"], "Sommerferien")

    def test_2027_and_2030_ranges(self):
        h_2027 = Germany(years=2027, subdiv="TH", categories=("school",))
        self.assertIn("2027-02-01", h_2027)
        self.assertEqual(h_2027["2027-02-01"], "Winterferien")
        self.assertIn("2027-07-10", h_2027)
        self.assertEqual(h_2027["2027-07-10"], "Sommerferien")

        h_2030 = Germany(years=2030, subdiv="TH", categories=("school",))
        self.assertIn("2030-01-01", h_2030)
        self.assertEqual(h_2030["2030-01-01"], "Weihnachtsferien")
        self.assertIn("2030-05-31", h_2030)
        self.assertEqual(h_2030["2030-05-31"], "Schulfreier Tag")


class TestGermanySchleswigHolsteinSchoolHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Germany, with_subdiv_categories=True)

    def test_christmas_cross_year(self):
        h_2025 = Germany(years=2025, subdiv="SH", categories=("school",))
        self.assertIn("2025-12-19", h_2025)
        self.assertEqual(h_2025["2025-12-19"], "Weihnachtsferien")

        h_2026 = Germany(years=2026, subdiv="SH", categories=("school",))
        self.assertIn("2026-01-01", h_2026)
        self.assertEqual(h_2026["2026-01-01"], "Weihnachtsferien")
        self.assertNotIn("2025-12-19", h_2026)

    def test_key_2026_ranges(self):
        h = Germany(years=2026, subdiv="SH", categories=("school",))
        self.assertIn("2026-03-26", h)
        self.assertEqual(h["2026-03-26"], "Osterferien")
        self.assertIn("2026-05-15", h)
        self.assertEqual(h["2026-05-15"], "Himmelfahrt")
        self.assertIn("2026-07-04", h)
        self.assertEqual(h["2026-07-04"], "Sommerferien")

    def test_2028_and_2030_ranges(self):
        h_2028 = Germany(years=2028, subdiv="SH", categories=("school",))
        self.assertIn("2028-06-24", h_2028)
        self.assertEqual(h_2028["2028-06-24"], "Sommerferien")

        h_2030 = Germany(years=2030, subdiv="SH", categories=("school",))
        self.assertIn("2030-07-08", h_2030)
        self.assertEqual(h_2030["2030-07-08"], "Sommerferien")
        self.assertIn("2030-05-31", h_2030)
        self.assertEqual(h_2030["2030-05-31"], "Himmelfahrt")


class TestGermanySaxonySchoolHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Germany, with_subdiv_categories=True)

    def test_christmas_cross_year(self):
        h_2025 = Germany(years=2025, subdiv="SN", categories=("school",))
        self.assertIn("2025-12-22", h_2025)
        self.assertEqual(h_2025["2025-12-22"], "Weihnachtsferien")

        h_2026 = Germany(years=2026, subdiv="SN", categories=("school",))
        self.assertIn("2026-01-01", h_2026)
        self.assertEqual(h_2026["2026-01-01"], "Weihnachtsferien")
        self.assertNotIn("2025-12-22", h_2026)

    def test_key_2026_ranges(self):
        h = Germany(years=2026, subdiv="SN", categories=("school",))
        self.assertIn("2026-02-09", h)
        self.assertEqual(h["2026-02-09"], "Winterferien")
        self.assertIn("2026-04-03", h)
        self.assertEqual(h["2026-04-03"], "Osterferien")
        self.assertIn("2026-07-04", h)
        self.assertEqual(h["2026-07-04"], "Sommerferien")
        self.assertIn("2026-05-15", h)
        self.assertEqual(h["2026-05-15"], "Unterrichtsfreier Tag")

    def test_2027_and_2029_ranges(self):
        h_2027 = Germany(years=2027, subdiv="SN", categories=("school",))
        self.assertIn("2027-05-15", h_2027)
        self.assertEqual(h_2027["2027-05-15"], "Pfingstferien")
        self.assertIn("2027-07-10", h_2027)
        self.assertEqual(h_2027["2027-07-10"], "Sommerferien")

        h_2029 = Germany(years=2029, subdiv="SN", categories=("school",))
        self.assertIn("2029-03-29", h_2029)
        self.assertEqual(h_2029["2029-03-29"], "Osterferien")
        self.assertIn("2029-07-21", h_2029)
        self.assertEqual(h_2029["2029-07-21"], "Sommerferien")


class TestGermanySaxonyAnhaltSchoolHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Germany, with_subdiv_categories=True)

    def test_christmas_cross_year(self):
        h_2025 = Germany(years=2025, subdiv="ST", categories=("school",))
        self.assertIn("2025-12-22", h_2025)
        self.assertEqual(h_2025["2025-12-22"], "Weihnachtsferien")

        h_2026 = Germany(years=2026, subdiv="ST", categories=("school",))
        self.assertIn("2026-01-01", h_2026)
        self.assertEqual(h_2026["2026-01-01"], "Weihnachtsferien")
        self.assertNotIn("2025-12-22", h_2026)

    def test_key_2026_ranges(self):
        h = Germany(years=2026, subdiv="ST", categories=("school",))
        self.assertIn("2026-01-31", h)
        self.assertEqual(h["2026-01-31"], "Winterferien")
        self.assertIn("2026-03-30", h)
        self.assertEqual(h["2026-03-30"], "Osterferien")
        self.assertIn("2026-05-26", h)
        self.assertEqual(h["2026-05-26"], "Pfingstferien")
        self.assertIn("2026-07-04", h)
        self.assertEqual(h["2026-07-04"], "Sommerferien")

    def test_2028_and_2029_ranges(self):
        h_2028 = Germany(years=2028, subdiv="ST", categories=("school",))
        self.assertIn("2028-06-03", h_2028)
        self.assertEqual(h_2028["2028-06-03"], "Pfingstferien")
        self.assertIn("2028-10-02", h_2028)
        self.assertEqual(h_2028["2028-10-02"], "Beweglicher Ferientag")

        h_2029 = Germany(years=2029, subdiv="ST", categories=("school",))
        self.assertIn("2029-04-30", h_2029)
        self.assertEqual(h_2029["2029-04-30"], "Beweglicher Ferientag")
        self.assertIn("2029-05-11", h_2029)
        self.assertEqual(h_2029["2029-05-11"], "Pfingstferien")


class TestGermanyHamburgSchoolHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Germany, with_subdiv_categories=True)

    def test_christmas_cross_year(self):
        # 2025 Christmas range spans 2025->2026. Ensure per-year population.
        h_2025 = Germany(years=2025, subdiv="HH", categories=("school",))
        self.assertIn("2025-12-17", h_2025)
        self.assertEqual(h_2025["2025-12-17"], "Weihnachtsferien")

        h_2026 = Germany(years=2026, subdiv="HH", categories=("school",))
        # 2026 object should include 2026-01-01 but not 2025-12-17
        self.assertIn("2026-01-01", h_2026)
        self.assertEqual(h_2026["2026-01-01"], "Weihnachtsferien")
        self.assertNotIn("2025-12-17", h_2026)

    def test_halfyear_and_spring_2026(self):
        h = Germany(years=2026, subdiv="HH", categories=("school",))
        self.assertIn("2026-01-30", h)
        self.assertEqual(h["2026-01-30"], "Halbjahrespause")
        self.assertIn("2026-03-02", h)
        self.assertEqual(h["2026-03-02"], "Frühjahrsferien")

    def test_himmelfahrt_pfingsten_and_summer_2026(self):
        h = Germany(years=2026, subdiv="HH", categories=("school",))
        self.assertIn("2026-05-11", h)
        self.assertEqual(h["2026-05-11"], "Himmelfahrt/Pfingsten")
        self.assertIn("2026-07-09", h)
        self.assertEqual(h["2026-07-09"], "Sommerferien")
        self.assertIn("2026-08-19", h)
        self.assertEqual(h["2026-08-19"], "Sommerferien")

    def test_default_categories_excludes_school(self):
        # If no categories specified, school category should not be present.
        h = Germany(years=2026, subdiv="HH")
        self.assertNotIn("2026-07-09", h)

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-03-08", "Women's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-06", "Whit Monday"),
            ("2022-06-16", "Corpus Christi"),
            ("2022-08-08", "Augsburg Peace Festival"),
            ("2022-08-15", "Assumption Day"),
            ("2022-09-20", "World Children's Day"),
            ("2022-10-03", "German Unity Day"),
            ("2022-10-31", "Reformation Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-16", "Repentance and Prayer Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-06", "วันสมโภชพระคริสต์แสดงองค์"),
            ("2022-03-08", "วันสตรี"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-17", "วันอาทิตย์อีสเตอร์"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-05-01", "วันแรงงาน"),
            ("2022-05-26", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2022-06-05", "วันสมโภชพระจิตเจ้า"),
            ("2022-06-06", "วันจันทร์หลังวันสมโภชพระจิตเจ้า"),
            ("2022-06-16", "วันสมโภชพระคริสตวรกาย"),
            ("2022-08-08", "วันเทศกาลสันติภาพเอาก์สบวร์ก"),
            ("2022-08-15", "วันสมโภชแม่พระรับเกียรติยกขึ้นสวรรค์"),
            ("2022-09-20", "วันเด็กสากล"),
            ("2022-10-03", "วันรวมชาติเยอรมัน"),
            ("2022-10-31", "วันแห่งการปฏิรูป"),
            ("2022-11-01", "วันสมโภชนักบุญทั้งหลาย"),
            ("2022-11-16", "วันแห่งการอธิษฐานและการกลับใจ"),
            ("2022-12-25", "วันคริสต์มาสวันแรก"),
            ("2022-12-26", "วันคริสต์มาสวันที่สอง"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-06", "Богоявлення"),
            ("2022-03-08", "Жіночий день"),
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-05", "Трійця"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-06-16", "Свято Тіла і Крові Христових"),
            ("2022-08-08", "Аугсбурзьке свято миру"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-09-20", "Всесвітній день дітей"),
            ("2022-10-03", "День німецької єдності"),
            ("2022-10-31", "День Реформації"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-16", "День молитви та покаяння"),
            ("2022-12-25", "Перший день Різдва"),
            ("2022-12-26", "Другий день Різдва"),
        )


class TestGermanyBadenWuerttembergSchoolHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Germany, with_subdiv_categories=True)

    def test_summer_and_christmas_2025(self):
        h = Germany(years=2025, subdiv="BW", categories=("school",))
        self.assertIn("2025-07-31", h)
        self.assertEqual(h["2025-07-31"], "Sommerferien")
        self.assertIn("2025-12-22", h)
        self.assertEqual(h["2025-12-22"], "Weihnachtsferien")

    def test_2026_ranges(self):
        h = Germany(years=2026, subdiv="BW", categories=("school",))
        self.assertIn("2026-03-30", h)
        self.assertEqual(h["2026-03-30"], "Osterferien")
        self.assertIn("2026-05-26", h)
        self.assertEqual(h["2026-05-26"], "Pfingstferien")


class TestGermanyBayernSchoolHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Germany, with_subdiv_categories=True)

    def test_christmas_2025_2026(self):
        h1 = Germany(years=2025, subdiv="BY", categories=("school",))
        self.assertIn("2025-12-22", h1)
        self.assertEqual(h1["2025-12-22"], "Weihnachtsferien")

        h2 = Germany(years=2026, subdiv="BY", categories=("school",))
        self.assertIn("2026-01-05", h2)
        self.assertEqual(h2["2026-01-05"], "Weihnachtsferien")

    def test_spring_and_summer_2026(self):
        h = Germany(years=2026, subdiv="BY", categories=("school",))
        self.assertIn("2026-02-16", h)
        self.assertEqual(h["2026-02-16"], "Frühjahrsferien")
        self.assertIn("2026-08-03", h)
        self.assertEqual(h["2026-08-03"], "Sommerferien")


class TestGermanyBerlinSchoolHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Germany, with_subdiv_categories=True)

    def test_christmas_and_winter_2025_2026(self):
        h = Germany(years=2025, subdiv="BE", categories=("school",))
        self.assertIn("2025-12-22", h)
        self.assertEqual(h["2025-12-22"], "Weihnachtsferien")


class TestGermanyBrandenburgSchoolHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Germany, with_subdiv_categories=True)

    def test_christmas_cross_year_2025_2026(self):
        g25 = Germany(years=2025, subdiv="BB", categories=("school",))
        self.assertIn("2025-12-22", g25)
        self.assertEqual(g25["2025-12-22"], "Weihnachtsferien")

        g26 = Germany(years=2026, subdiv="BB", categories=("school",))
        # 2026 object should include the 2026 portion of Christmas but not 2025-12-22
        self.assertIn("2026-01-01", g26)
        self.assertEqual(g26["2026-01-01"], "Weihnachtsferien")
        self.assertNotIn("2025-12-22", g26)

    def test_spring_and_pfingsten_2026(self):
        g = Germany(years=2026, subdiv="BB", categories=("school",))
        self.assertIn("2026-02-02", g)
        self.assertEqual(g["2026-02-02"], "Winterferien")
        self.assertIn("2026-03-30", g)
        self.assertEqual(g["2026-03-30"], "Osterferien")
        self.assertIn("2026-05-26", g)
        self.assertEqual(g["2026-05-26"], "Pfingsten")
        # Variable days
        self.assertIn("2026-05-13", g)
        self.assertIn("2026-05-15", g)
        self.assertIn("2026-05-18", g)

    def test_summer_and_autumn_2026(self):
        g = Germany(years=2026, subdiv="BB", categories=("school",))
        self.assertIn("2026-07-09", g)
        self.assertEqual(g["2026-07-09"], "Sommerferien")
        self.assertIn("2026-10-19", g)
        self.assertEqual(g["2026-10-19"], "Herbstferien")

    def test_variable_days_2028_2029(self):
        g28 = Germany(years=2028, subdiv="BB", categories=("school",))
        self.assertIn("2028-05-26", g28)
        self.assertIn("2028-10-30", g28)

        g29 = Germany(years=2029, subdiv="BB", categories=("school",))
        self.assertIn("2029-04-30", g29)
        self.assertIn("2029-05-11", g29)
        self.assertIn("2029-05-22", g29)


class TestGermanyBremenSchoolHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Germany, with_subdiv_categories=True)

    def test_christmas_cross_year_2025_2026(self):
        b25 = Germany(years=2025, subdiv="HB", categories=("school",))
        self.assertIn("2025-12-22", b25)
        self.assertEqual(b25["2025-12-22"], "Weihnachtsferien")

        b26 = Germany(years=2026, subdiv="HB", categories=("school",))
        self.assertIn("2026-01-01", b26)
        self.assertEqual(b26["2026-01-01"], "Weihnachtsferien")
        self.assertNotIn("2025-12-22", b26)

    def test_halfyear_and_easter_2026(self):
        b = Germany(years=2026, subdiv="HB", categories=("school",))
        self.assertIn("2026-02-02", b)
        self.assertEqual(b["2026-02-02"], "Halbjahresferien")
        self.assertIn("2026-03-23", b)
        self.assertEqual(b["2026-03-23"], "Osterferien")

    def test_himmelfahrt_pfingsten_and_summer_2026(self):
        b = Germany(years=2026, subdiv="HB", categories=("school",))
        self.assertIn("2026-05-15", b)
        self.assertEqual(b["2026-05-15"], "Tag nach Himmelfahrt")
        self.assertIn("2026-05-26", b)
        self.assertEqual(b["2026-05-26"], "Pfingsten")
        self.assertIn("2026-07-02", b)
        self.assertEqual(b["2026-07-02"], "Sommerferien")

    def test_autumn_and_christmas_2026_2027(self):
        b = Germany(years=2026, subdiv="HB", categories=("school",))
        self.assertIn("2026-10-12", b)
        self.assertEqual(b["2026-10-12"], "Herbstferien")

        b27 = Germany(years=2027, subdiv="HB", categories=("school",))
        self.assertIn("2027-01-01", b27)
        self.assertIn("2027-12-23", b27)

    def test_special_days_2028_2029(self):
        b28 = Germany(years=2028, subdiv="HB", categories=("school",))
        self.assertIn("2028-10-02", b28)
        self.assertEqual(b28["2028-10-02"], "Tag vor dem 03. Oktober")

        b29 = Germany(years=2029, subdiv="HB", categories=("school",))
        self.assertIn("2029-04-30", b29)
        self.assertIn("2029-10-04", b29)

    def test_summer_2030(self):
        b30 = Germany(years=2030, subdiv="HB", categories=("school",))
        self.assertIn("2030-07-11", b30)
        self.assertEqual(b30["2030-07-11"], "Sommerferien")


class TestGermanyHessenSchoolHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Germany, with_subdiv_categories=True)

    def test_christmas_cross_year_2025_2026(self):
        h25 = Germany(years=2025, subdiv="HE", categories=("school",))
        self.assertIn("2025-12-22", h25)
        self.assertEqual(h25["2025-12-22"], "Weihnachtsferien")

        h26 = Germany(years=2026, subdiv="HE", categories=("school",))
        self.assertIn("2026-01-01", h26)
        self.assertEqual(h26["2026-01-01"], "Weihnachtsferien")
        self.assertNotIn("2025-12-22", h26)

    def test_easter_and_summer_2026(self):
        h = Germany(years=2026, subdiv="HE", categories=("school",))
        self.assertIn("2026-03-30", h)
        self.assertEqual(h["2026-03-30"], "Osterferien")
        self.assertIn("2026-06-29", h)
        self.assertEqual(h["2026-06-29"], "Sommerferien")

    def test_autumn_and_christmas_2026_2027(self):
        h = Germany(years=2026, subdiv="HE", categories=("school",))
        self.assertIn("2026-10-05", h)
        self.assertEqual(h["2026-10-05"], "Herbstferien")

        h27 = Germany(years=2027, subdiv="HE", categories=("school",))
        self.assertIn("2027-12-23", h27)
        self.assertEqual(h27["2027-12-23"], "Weihnachtsferien")

    def test_ranges_through_2030(self):
        h28 = Germany(years=2028, subdiv="HE", categories=("school",))
        self.assertIn("2028-07-03", h28)
        self.assertIn("2028-10-09", h28)

        h29 = Germany(years=2029, subdiv="HE", categories=("school",))
        self.assertIn("2029-07-16", h29)
        self.assertIn("2029-10-15", h29)

        h30 = Germany(years=2030, subdiv="HE", categories=("school",))
        self.assertIn("2030-07-22", h30)


class TestGermanyMecklenburgVorpommernSchoolHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Germany, with_subdiv_categories=True)

    def test_christmas_cross_year_2025_2026(self):
        m25 = Germany(years=2025, subdiv="MV", categories=("school",))
        self.assertIn("2025-12-20", m25)
        self.assertEqual(m25["2025-12-20"], "Weihnachtsferien")

        m26 = Germany(years=2026, subdiv="MV", categories=("school",))
        self.assertIn("2026-01-01", m26)
        self.assertEqual(m26["2026-01-01"], "Weihnachtsferien")
        self.assertNotIn("2025-12-20", m26)

    def test_winter_easter_pfingsten_2026(self):
        m = Germany(years=2026, subdiv="MV", categories=("school",))
        self.assertIn("2026-02-09", m)
        self.assertEqual(m["2026-02-09"], "Winterferien")
        self.assertIn("2026-03-30", m)
        self.assertEqual(m["2026-03-30"], "Osterferien")
        self.assertIn("2026-05-22", m)
        self.assertEqual(m["2026-05-22"], "Pfingstferien")
        self.assertIn("2026-05-15", m)

    def test_summer_and_autumn_2026(self):
        m = Germany(years=2026, subdiv="MV", categories=("school",))
        self.assertIn("2026-07-13", m)
        self.assertEqual(m["2026-07-13"], "Sommerferien")
        self.assertIn("2026-10-15", m)
        self.assertEqual(m["2026-10-15"], "Herbstferien")

    def test_variable_and_special_days_2027_2029(self):
        m27 = Germany(years=2027, subdiv="MV", categories=("school",))
        self.assertIn("2027-05-07", m27)
        self.assertIn("2027-07-05", m27)

        m29 = Germany(years=2029, subdiv="MV", categories=("school",))
        self.assertIn("2029-03-09", m29)
        self.assertIn("2029-04-30", m29)
        self.assertIn("2029-05-11", m29)
        self.assertIn("2029-06-18", m29)

    def test_ranges_through_2030(self):
        m30 = Germany(years=2030, subdiv="MV", categories=("school",))
        self.assertIn("2030-04-17", m30)
        self.assertIn("2030-07-01", m30)


class TestGermanyNiedersachsenSchoolHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Germany, with_subdiv_categories=True)

    def test_christmas_cross_year_2025_2026(self):
        n25 = Germany(years=2025, subdiv="NI", categories=("school",))
        self.assertIn("2025-12-22", n25)
        self.assertEqual(n25["2025-12-22"], "Weihnachtsferien")

        n26 = Germany(years=2026, subdiv="NI", categories=("school",))
        self.assertIn("2026-01-01", n26)
        self.assertEqual(n26["2026-01-01"], "Weihnachtsferien")
        self.assertNotIn("2025-12-22", n26)

    def test_halfyear_and_easter_2026(self):
        n = Germany(years=2026, subdiv="NI", categories=("school",))
        self.assertIn("2026-02-02", n)
        self.assertEqual(n["2026-02-02"], "Halbjahresferien")
        self.assertIn("2026-03-23", n)
        self.assertEqual(n["2026-03-23"], "Osterferien")

    def test_may_and_pfingsten_2026(self):
        n = Germany(years=2026, subdiv="NI", categories=("school",))
        self.assertIn("2026-05-15", n)
        self.assertIn("2026-05-26", n)

    def test_summer_and_autumn_2026(self):
        n = Germany(years=2026, subdiv="NI", categories=("school",))
        self.assertIn("2026-07-02", n)
        self.assertIn("2026-10-12", n)

    def test_ranges_through_2030(self):
        n27 = Germany(years=2027, subdiv="NI", categories=("school",))
        self.assertIn("2027-07-08", n27)
        self.assertIn("2027-10-16", n27)

        n29 = Germany(years=2029, subdiv="NI", categories=("school",))
        self.assertIn("2029-07-19", n29)
        self.assertIn("2029-10-04", n29)

        n30 = Germany(years=2030, subdiv="NI", categories=("school",))
        self.assertIn("2030-07-11", n30)


class TestGermanyNordrheinWestfalenSchoolHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Germany, with_subdiv_categories=True)

    def test_christmas_cross_year_2025_2026(self):
        w25 = Germany(years=2025, subdiv="NW", categories=("school",))
        self.assertIn("2025-12-22", w25)
        self.assertEqual(w25["2025-12-22"], "Weihnachtsferien")

        w26 = Germany(years=2026, subdiv="NW", categories=("school",))
        self.assertIn("2026-01-01", w26)
        self.assertEqual(w26["2026-01-01"], "Weihnachtsferien")
        self.assertNotIn("2025-12-22", w26)

    def test_summer_2026(self):
        w = Germany(years=2026, subdiv="NW", categories=("school",))
        self.assertIn("2026-07-20", w)
        self.assertIn("2026-09-01", w)

    def test_autumn_2026(self):
        w = Germany(years=2026, subdiv="NW", categories=("school",))
        self.assertIn("2026-10-17", w)
        self.assertIn("2026-10-31", w)

    def test_oster_and_pfingsten_2027(self):
        w27 = Germany(years=2027, subdiv="NW", categories=("school",))
        self.assertIn("2027-03-22", w27)
        self.assertIn("2027-05-18", w27)

    def test_ranges_through_2030(self):
        w29 = Germany(years=2029, subdiv="NW", categories=("school",))
        self.assertIn("2029-03-26", w29)
        self.assertIn("2029-07-02", w29)
        self.assertIn("2029-10-15", w29)

        w30 = Germany(years=2030, subdiv="NW", categories=("school",))
        self.assertIn("2030-04-15", w30)


class TestGermanyRheinlandPfalzSchoolHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Germany, with_subdiv_categories=True)

    def test_summer_and_christmas_2025(self):
        r25 = Germany(years=2025, subdiv="RP", categories=("school",))
        self.assertIn("2025-07-07", r25)
        self.assertEqual(r25["2025-07-07"], "Sommerferien")
        self.assertIn("2025-12-22", r25)
        self.assertEqual(r25["2025-12-22"], "Weihnachtsferien")

    def test_2026_ranges(self):
        r26 = Germany(years=2026, subdiv="RP", categories=("school",))
        self.assertIn("2026-03-30", r26)
        self.assertEqual(r26["2026-03-30"], "Osterferien")
        self.assertIn("2026-06-29", r26)
        self.assertEqual(r26["2026-06-29"], "Sommerferien")

    def test_cross_year_christmas(self):
        r26 = Germany(years=2026, subdiv="RP", categories=("school",))
        self.assertIn("2026-01-01", r26)
        self.assertEqual(r26["2026-01-01"], "Weihnachtsferien")
        self.assertNotIn("2025-12-22", r26)

    def test_ranges_through_2030(self):
        r29 = Germany(years=2029, subdiv="RP", categories=("school",))
        self.assertIn("2029-07-16", r29)
        self.assertIn("2029-10-22", r29)

        r30 = Germany(years=2030, subdiv="RP", categories=("school",))
        self.assertIn("2030-01-01", r30)
        self.assertIn("2030-04-15", r30)

        h2 = Germany(years=2026, subdiv="BE", categories=("school",))
        self.assertIn("2026-02-02", h2)
        self.assertEqual(h2["2026-02-02"], "Winterferien")

    def test_special_and_summer_2026(self):
        h = Germany(years=2026, subdiv="BE", categories=("school",))
        self.assertIn("2026-05-15", h)
        self.assertEqual(h["2026-05-15"], "Unterrichtsfreier Tag nach AZVO")
        self.assertIn("2026-07-09", h)
        self.assertEqual(h["2026-07-09"], "Sommerferien")
