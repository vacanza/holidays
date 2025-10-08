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

from holidays.constants import HALF_DAY, OPTIONAL, PUBLIC
from holidays.countries.switzerland import Switzerland, CH, CHE
from tests.common import CommonCountryTests


class TestSwitzerland(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full_range = range(1970, 2050)
        super().setUpClass(Switzerland, years=cls.full_range)
        cls.subdiv_holidays = {
            subdiv: Switzerland(subdiv=subdiv, years=cls.full_range)
            for subdiv in Switzerland.subdivisions
        }
        cls.subdiv_half_day_holidays = {
            subdiv: Switzerland(categories=HALF_DAY, subdiv=subdiv, years=cls.full_range)
            for subdiv in Switzerland.subdivisions
        }
        cls.subdiv_optional_holidays = {
            subdiv: Switzerland(categories=OPTIONAL, subdiv=subdiv, years=cls.full_range)
            for subdiv in Switzerland.subdivisions
        }
        cls.subdiv_optional_holidays_non_observed = {
            subdiv: Switzerland(
                categories=OPTIONAL, observed=False, subdiv=subdiv, years=cls.full_range
            )
            for subdiv in Switzerland.subdivisions
        }

    def test_country_aliases(self):
        self.assertAliases(Switzerland, CH, CHE)

    def test_all_holidays_present(self):
        y_2018 = set()
        for p in Switzerland.subdivisions:
            y_2018.update(
                Switzerland(categories=(HALF_DAY, OPTIONAL, PUBLIC), years=2018, subdiv=p).values()
            )
        all_h = {  # Holidays names in their chronological order.
            "Neujahrstag",
            "Berchtoldstag",
            "Heilige Drei Könige",
            "Jahrestag der Ausrufung der Republik",
            "Josefstag",
            "Näfelser Fahrt",
            "Vortag vor Karfreitag",
            "Karfreitag",
            "Ostermontag",
            "Sechseläuten",
            "Tag der Arbeit",
            "Vortag vor Auffahrt",
            "Auffahrt",
            "Brückentag nach Auffahrt",
            "Pfingstmontag",
            "Fronleichnam",
            "Fest der Unabhängigkeit",
            "Peter und Paul",
            "Nationalfeiertag",
            "Mariä Himmelfahrt",
            "Knabenschiessen",
            "Bettagsmontag",
            "Bruder Klaus",
            "Allerheiligen",
            "Mariä Empfängnis",
            "Genfer Bettag",
            "Heiligabend",
            "Weihnachten",
            "Stephanstag",
            "Brückentag",
            "Vortag vor Neujahr",
            "Wiederherstellung der Republik",
        }

        self.assertEqual(
            all_h,
            y_2018,
            f"missing: {all_h - y_2018 or 'no'}, extra: {y_2018 - all_h or 'no'}",
        )

    def test_fixed_holidays(self):
        # New Year's Day.
        self.assertHolidayName("Neujahrstag", (f"{year}-01-01" for year in self.full_range))
        # National Day.
        self.assertHolidayName("Nationalfeiertag", (f"{year}-08-01" for year in self.full_range))
        # Christmas Day.
        self.assertHolidayName("Weihnachten", (f"{year}-12-25" for year in self.full_range))

    def test_berchtolds_day(self):
        name = "Berchtoldstag"
        subdivs_that_have = {"AG", "BE", "JU", "LU", "TG", "VD", "ZH"}
        subdivs_optional = {"FR", "GL", "NW", "OW", "SG", "SH", "SO", "VS", "ZG"}

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in subdivs_that_have:
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-02" for year in self.full_range)
                )
            elif subdiv != "NE":
                self.assertNoHoliday(holidays, (f"{year}-01-02" for year in self.full_range))
                self.assertNoHolidayName(name, holidays)

        for subdiv, holidays in self.subdiv_optional_holidays.items():
            if subdiv in subdivs_optional:
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-02" for year in self.full_range)
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-01-02" for year in self.full_range))
                self.assertNoHolidayName(name, holidays)

        # When holiday present in NE.
        ne_years = {1978, 1984, 1989, 1995, 2006, 2012, 2017, 2023, 2034, 2040, 2045}
        self.assertHolidayName(
            name, self.subdiv_holidays["NE"], (f"{year}-01-02" for year in ne_years)
        )
        self.assertNoHoliday(
            self.subdiv_holidays["NE"],
            (f"{year}-01-02" for year in set(self.full_range).difference(ne_years)),
        )

    def test_epiphany(self):
        name = "Heilige Drei Könige"
        subdivs_that_have = {"SZ", "TI", "UR"}

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in subdivs_that_have:
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-06" for year in self.full_range)
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-01-06" for year in self.full_range))
                self.assertNoHolidayName(name, holidays)

    def test_republic_day(self):
        name = "Jahrestag der Ausrufung der Republik"

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "NE":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-01" for year in self.full_range)
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-03-01" for year in self.full_range))
                self.assertNoHolidayName(name, holidays)

    def test_st_josephs_day(self):
        name = "Josefstag"
        subdivs_that_have = {"NW", "SZ", "TI", "UR", "VS"}

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in subdivs_that_have:
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-19" for year in self.full_range)
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-03-19" for year in self.full_range))
                self.assertNoHolidayName(name, holidays)

    def test_nafels_ride(self):
        name = "Näfelser Fahrt"
        known_good = (
            "2018-04-05",
            "2019-04-04",
            "2020-04-02",
            "2021-04-08",
            "2022-04-07",
            "2023-04-13",
            "2024-04-04",
            "2025-04-03",
            "2026-04-09",
            "2027-04-01",
            "2028-04-06",
            "2029-04-05",
            "2030-04-04",
            "2031-04-03",
            "2032-04-01",
            "2033-04-07",
            "2034-04-13",
            "2035-04-05",
        )

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "GL":
                self.assertHolidayName(name, holidays, known_good)
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

        self.assertNoHolidayName(name, Switzerland(subdiv="GL", years=1834))

    def test_good_friday(self):
        name = "Karfreitag"
        known_good = (
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
            "2026-04-03",
            "2027-03-26",
            "2028-04-14",
            "2029-03-30",
            "2030-04-19",
            "2031-04-11",
            "2032-03-26",
            "2033-04-15",
            "2034-04-07",
            "2035-03-23",
        )
        subdivs_that_dont = {"TI", "VS"}
        subdivs_optional = {"GR"}
        subdivs_that_have = set(Switzerland.subdivisions) - subdivs_that_dont - subdivs_optional

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in subdivs_that_have:
                self.assertHolidayName(name, holidays, known_good)
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

        for subdiv, holidays in self.subdiv_optional_holidays.items():
            if subdiv in subdivs_optional:
                self.assertHolidayName(name, holidays, known_good)
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

    def test_easter_monday(self):
        name = "Ostermontag"
        known_good = (
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
            "2026-04-06",
            "2027-03-29",
            "2028-04-17",
            "2029-04-02",
            "2030-04-22",
            "2031-04-14",
            "2032-03-29",
            "2033-04-18",
            "2034-04-10",
            "2035-03-26",
        )
        subdivs_that_dont = {"NE", "SO"}
        subdivs_optional = {"FR", "NW", "OW", "VS", "ZG"}
        subdivs_that_have = set(Switzerland.subdivisions) - subdivs_that_dont - subdivs_optional

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in subdivs_that_have:
                self.assertHolidayName(name, holidays, known_good)
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

        for subdiv, holidays in self.subdiv_optional_holidays.items():
            if subdiv in subdivs_optional:
                self.assertHolidayName(name, holidays, known_good)
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

    def test_labor_day(self):
        name = "Tag der Arbeit"
        subdivs_that_have = {"AG", "BL", "BS", "JU", "NE", "SH", "TG", "TI", "ZH"}

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in subdivs_that_have:
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(
                    name, holidays, (f"{year}-05-01" for year in self.full_range)
                )
                self.assertNoHolidayName(name, holidays)

        for subdiv, holidays in self.subdiv_half_day_holidays.items():
            if subdiv == "SO":
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(
                    name, holidays, (f"{year}-05-01" for year in self.full_range)
                )
                self.assertNoHolidayName(name, holidays)

    def test_ascension_day(self):
        name = "Auffahrt"
        known_good = (
            "2018-05-10",
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
            "2026-05-14",
            "2027-05-06",
            "2028-05-25",
            "2029-05-10",
            "2030-05-30",
            "2031-05-22",
            "2032-05-06",
            "2033-05-26",
            "2034-05-18",
            "2035-05-03",
        )

        self.assertHolidayName(name, known_good)
        self.assertHolidayName(name, self.full_range)
        for holidays in self.subdiv_holidays.values():
            self.assertHolidayName(name, holidays, known_good)

    def test_whit_monday(self):
        name = "Pfingstmontag"
        known_good = (
            "2018-05-21",
            "2019-06-10",
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
            "2026-05-25",
            "2027-05-17",
            "2028-06-05",
            "2029-05-21",
            "2030-06-10",
            "2031-06-02",
            "2032-05-17",
            "2033-06-06",
            "2034-05-29",
            "2035-05-14",
        )

        subdivs_that_dont = {"NE", "SO"}
        subdivs_optional = {"FR", "NW", "OW", "VS", "ZG"}
        subdivs_that_have = set(Switzerland.subdivisions) - subdivs_that_dont - subdivs_optional

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in subdivs_that_have:
                self.assertHolidayName(name, holidays, known_good)
            elif subdiv in subdivs_that_dont:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

        for subdiv, holidays in self.subdiv_optional_holidays.items():
            if subdiv in subdivs_optional:
                self.assertHolidayName(name, holidays, known_good)
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

    def test_corpus_christi(self):
        name = "Fronleichnam"
        known_good = (
            "2014-06-19",
            "2015-06-04",
            "2016-05-26",
            "2017-06-15",
            "2018-05-31",
            "2019-06-20",
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
        )
        subdivs_that_have = {
            "AG",
            "AI",
            "JU",
            "LU",
            "NE",
            "NW",
            "OW",
            "SZ",
            "TI",
            "UR",
            "VS",
            "ZG",
        }

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in subdivs_that_have:
                self.assertHolidayName(name, holidays, known_good)
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

    def test_independence_day(self):
        name = "Fest der Unabhängigkeit"

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "JU":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-23" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(
                    name, holidays, (f"{year}-06-23" for year in self.full_range)
                )
                self.assertNoHolidayName(name, holidays)

    def test_saints_peter_and_paul(self):
        name = "Peter und Paul"

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "TI":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-29" for year in self.full_range)
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-06-29" for year in self.full_range))
                self.assertNoHolidayName(name, holidays)

    def test_assumption_day(self):
        name = "Mariä Himmelfahrt"
        subdivs_that_have = {"AG", "AI", "JU", "LU", "NW", "OW", "SZ", "TI", "UR", "VS", "ZG"}

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in subdivs_that_have:
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-15" for year in self.full_range)
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-08-15" for year in self.full_range))
                self.assertNoHolidayName(name, holidays)

    def test_prayer_monday(self):
        name = "Bettagsmontag"
        known_good = (
            "2014-09-22",
            "2015-09-21",
            "2016-09-19",
            "2017-09-18",
            "2018-09-17",
            "2019-09-16",
            "2020-09-21",
            "2021-09-20",
            "2022-09-19",
            "2023-09-18",
            "2024-09-16",
        )

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "VD":
                self.assertHolidayName(name, holidays, known_good)
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

    def test_saint_nicholas(self):
        name = "Bruder Klaus"

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "OW":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-25" for year in self.full_range)
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-09-25" for year in self.full_range))
                self.assertNoHolidayName(name, holidays)

    def test_all_saints_day(self):
        name = "Allerheiligen"
        subdivs_that_have = {
            "AG",
            "AI",
            "GL",
            "JU",
            "LU",
            "NW",
            "OW",
            "SG",
            "SZ",
            "TI",
            "UR",
            "VS",
            "ZG",
        }

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in subdivs_that_have:
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-11-01" for year in self.full_range))
                self.assertNoHolidayName(name, holidays)

    def test_genevan_fast(self):
        name = "Genfer Bettag"
        known_good = (
            "2014-09-11",
            "2015-09-10",
            "2016-09-08",
            "2017-09-07",
            "2018-09-06",
            "2019-09-05",
            "2020-09-10",
            "2021-09-09",
            "2022-09-08",
            "2023-09-07",
            "2024-09-05",
            "2025-09-11",
        )

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "GE":
                self.assertHolidayName(name, holidays, known_good)
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

    def test_immaculate_conception(self):
        name = "Mariä Empfängnis"
        subdivs_that_have = {"AG", "AI", "LU", "NW", "OW", "SZ", "TI", "UR", "VS", "ZG"}

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in subdivs_that_have:
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-08" for year in self.full_range)
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-12-08" for year in self.full_range))
                self.assertNoHolidayName(name, holidays)

    def test_saint_stephens_day(self):
        name = "Stephanstag"
        subdivs_that_have = {
            "AG",
            "BL",
            "BS",
            "BE",
            "GL",
            "GR",
            "LU",
            "SG",
            "SH",
            "SZ",
            "TG",
            "TI",
            "ZH",
        }
        subdivs_optional = {"FR", "NW", "OW", "VS", "ZG"}
        subdivs_that_dont = (
            set(Switzerland.subdivisions)
            - subdivs_that_have
            - subdivs_optional
            - {"AI", "AR", "NE", "UR"}
        )

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv in subdivs_that_have:
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-26" for year in self.full_range)
                )
            elif subdiv in subdivs_that_dont:
                self.assertNoHoliday(holidays, (f"{year}-12-26" for year in self.full_range))
                self.assertNoHolidayName(name, holidays)

        for subdiv, holidays in self.subdiv_optional_holidays.items():
            if subdiv in subdivs_optional:
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-26" for year in self.full_range)
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-12-26" for year in self.full_range))
                self.assertNoHolidayName(name, holidays)

        # When holiday present in NE.
        ne_years_have = {1977, 1983, 1988, 1994, 2005, 2011, 2016, 2022, 2033, 2039, 2044}
        self.assertHolidayName(
            name, self.subdiv_holidays["NE"], (f"{year}-12-26" for year in ne_years_have)
        )
        self.assertNoHoliday(
            self.subdiv_holidays["NE"],
            (f"{year}-12-26" for year in set(self.full_range).difference(ne_years_have)),
        )

        # When holiday not present in AI, AR, UR.
        ai_ar_ur_years_dont = {
            1970,
            1972,
            1978,
            1981,
            1987,
            1989,
            1992,
            1995,
            1998,
            2000,
            2006,
            2009,
            2015,
            2017,
            2020,
            2023,
            2026,
            2028,
            2034,
            2037,
            2043,
            2045,
            2048,
        }
        for subdiv in ("AI", "AR", "UR"):
            self.assertHolidayName(
                name,
                self.subdiv_holidays[subdiv],
                set(self.full_range).difference(ai_ar_ur_years_dont),
            )
            self.assertNoHoliday(
                self.subdiv_holidays[subdiv],
                (f"{year}-12-26" for year in (f"{year}-12-26" for year in ai_ar_ur_years_dont)),
            )

    def test_restoration_day(self):
        name = "Wiederherstellung der Republik"

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "GE":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-31" for year in self.full_range)
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-12-31" for year in self.full_range))
                self.assertNoHolidayName(name, holidays)

    def test_knabenschiessen(self):
        name = "Knabenschiessen"

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_holidays.items():
            if subdiv == "ZH":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-09-12",
                    "2020-09-13",
                    "2021-09-11",
                    "2021-09-12",
                    "2022-09-10",
                    "2022-09-11",
                    "2023-09-09",
                    "2023-09-10",
                    "2024-09-07",
                    "2024-09-08",
                    "2025-09-13",
                    "2025-09-14",
                )
                self.assertHolidayNameCount(name, 2, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

        for subdiv, holidays in self.subdiv_half_day_holidays.items():
            if subdiv == "ZH":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-09-14",
                    "2021-09-13",
                    "2022-09-12",
                    "2023-09-11",
                    "2024-09-09",
                    "2025-09-15",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

        for subdiv, holidays in self.subdiv_optional_holidays.items():
            if subdiv == "ZH":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-09-14",
                    "2023-09-11",
                    "2024-09-09",
                    "2025-09-15",
                )
                self.assertNoHolidayName(
                    name,
                    holidays,
                    # Not in years where 4 bridge holidays are given out for Christmas-New Year.
                    "2016-09-12",
                    "2021-09-13",
                    "2022-09-12",
                    "2027-09-13",
                )
            else:
                self.assertNoHolidayName(name, holidays)

        self.assertNoHolidayName(name, Switzerland(subdiv="ZH", years=1898))
        self.assertNoHolidayName(name, Switzerland(categories=HALF_DAY, subdiv="ZH", years=1898))
        self.assertNoHolidayName(name, Switzerland(categories=OPTIONAL, subdiv="ZH", years=1898))

    def test_day_before_good_friday(self):
        name = "Vortag vor Karfreitag"

        self.assertNoHolidayName(name)

        for subdiv, holidays in {
            **self.subdiv_half_day_holidays,
            **self.subdiv_optional_holidays,
        }.items():
            if subdiv == "ZH":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-04-09",
                    "2021-04-01",
                    "2022-04-14",
                    "2023-04-06",
                    "2024-03-28",
                    "2025-04-17",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_sechselauten(self):
        name = "Sechseläuten"

        self.assertNoHolidayName(name)

        for subdiv, holidays in {
            **self.subdiv_half_day_holidays,
            **self.subdiv_optional_holidays,
        }.items():
            if subdiv == "ZH":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-04-20",
                    "2021-04-19",
                    "2022-04-25",
                    "2023-04-17",
                    "2024-04-15",
                    "2025-04-28",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

        subdiv_zh_half_day_holidays = Switzerland(
            categories=HALF_DAY, subdiv="ZH", years=range(1901, 1970)
        )

        self.assertHolidayName(
            name,
            subdiv_zh_half_day_holidays,
            "1902-03-24",
            "1903-03-23",
            "1904-03-21",
            "1949-03-21",
            "1950-03-27",
            "1951-03-26",
            "1952-04-21",
        )
        self.assertHolidayName(name, subdiv_zh_half_day_holidays, range(1902, 1970))
        self.assertNoHolidayName(name, subdiv_zh_half_day_holidays, 1901)

        subdiv_zh_optional_holidays = Switzerland(
            categories=OPTIONAL, subdiv="ZH", years=range(1901, 1970)
        )

        self.assertHolidayName(
            name,
            subdiv_zh_optional_holidays,
            "1902-03-24",
            "1903-03-23",
            "1904-03-21",
            "1949-03-21",
            "1950-03-27",
            "1951-03-26",
            "1952-04-21",
        )
        self.assertHolidayName(name, subdiv_zh_optional_holidays, range(1902, 1970))
        self.assertNoHolidayName(name, subdiv_zh_optional_holidays, 1901)

    def test_day_before_ascension_day(self):
        name = "Vortag vor Auffahrt"

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_half_day_holidays.items():
            if subdiv == "ZH":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-05-20",
                    "2021-05-12",
                    "2022-05-25",
                    "2023-05-17",
                    "2024-05-08",
                    "2025-05-28",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_bridge_holiday_for_ascension_day(self):
        name = "Brückentag nach Auffahrt"

        for subdiv, holidays in self.subdiv_optional_holidays.items():
            if subdiv == "ZH":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2018-05-11",
                    "2019-05-31",
                    "2024-05-10",
                    "2025-05-30",
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_christmas_eve(self):
        name = "Heiligabend"

        self.assertNoHolidayName(name)

        for subdiv, holidays in {
            **self.subdiv_half_day_holidays,
            **self.subdiv_optional_holidays,
        }.items():
            if subdiv == "ZH":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-24" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_bridge_holidays(self):
        name = "Brückentag"

        self.assertNoHolidayName(name)

        for subdiv, holidays in self.subdiv_optional_holidays_non_observed.items():
            if subdiv == "ZH":
                self.assertNonObservedHolidayName(
                    name,
                    holidays,
                    (f"{year}-12-27" for year in self.full_range),
                    (f"{year}-12-28" for year in self.full_range),
                    (f"{year}-12-29" for year in self.full_range),
                    (f"{year}-12-30" for year in self.full_range),
                )
            else:
                self.assertNoNonObservedHolidayName(name, holidays)

        self.assertNoHoliday(
            self.subdiv_optional_holidays["ZH"],
            "2025-12-27",
            "2025-12-28",
            "2026-12-27",
        )

    def test_new_years_eve(self):
        name = "Vortag vor Neujahr"

        self.assertNoHolidayName(name)

        for subdiv, holidays in {
            **self.subdiv_half_day_holidays,
            **self.subdiv_optional_holidays,
        }.items():
            if subdiv == "ZH":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-31" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Neujahrstag"),
            ("2023-01-02", "Berchtoldstag"),
            ("2023-01-06", "Heilige Drei Könige"),
            ("2023-03-01", "Jahrestag der Ausrufung der Republik"),
            ("2023-03-19", "Josefstag"),
            ("2023-04-06", "Vortag vor Karfreitag"),
            ("2023-04-07", "Karfreitag"),
            ("2023-04-10", "Ostermontag"),
            ("2023-04-13", "Näfelser Fahrt"),
            ("2023-04-17", "Sechseläuten"),
            ("2023-05-01", "Tag der Arbeit"),
            ("2023-05-17", "Vortag vor Auffahrt"),
            ("2023-05-18", "Auffahrt"),
            ("2023-05-29", "Pfingstmontag"),
            ("2023-06-08", "Fronleichnam"),
            ("2023-06-23", "Fest der Unabhängigkeit"),
            ("2023-06-29", "Peter und Paul"),
            ("2023-08-01", "Nationalfeiertag"),
            ("2023-08-15", "Mariä Himmelfahrt"),
            ("2023-09-07", "Genfer Bettag"),
            ("2023-09-09", "Knabenschiessen"),
            ("2023-09-10", "Knabenschiessen"),
            ("2023-09-11", "Knabenschiessen"),
            ("2023-09-18", "Bettagsmontag"),
            ("2023-09-25", "Bruder Klaus"),
            ("2023-11-01", "Allerheiligen"),
            ("2023-12-08", "Mariä Empfängnis"),
            ("2023-12-24", "Heiligabend"),
            ("2023-12-25", "Weihnachten"),
            ("2023-12-26", "Stephanstag"),
            ("2023-12-27", "Brückentag"),
            ("2023-12-28", "Brückentag"),
            ("2023-12-29", "Brückentag"),
            ("2023-12-31", "Vortag vor Neujahr; Wiederherstellung der Republik"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-01-02", "Saint Berchtold's Day"),
            ("2023-01-06", "Epiphany"),
            ("2023-03-01", "Republic Day"),
            ("2023-03-19", "Saint Joseph's Day"),
            ("2023-04-06", "Day before Good Friday"),
            ("2023-04-07", "Good Friday"),
            ("2023-04-10", "Easter Monday"),
            ("2023-04-13", "Battle of Naefels Victory Day"),
            ("2023-04-17", "Sechseläuten"),
            ("2023-05-01", "Labor Day"),
            ("2023-05-17", "Day before Ascension Day"),
            ("2023-05-18", "Ascension Day"),
            ("2023-05-29", "Whit Monday"),
            ("2023-06-08", "Corpus Christi"),
            ("2023-06-23", "Independence Day"),
            ("2023-06-29", "Saints Peter and Paul"),
            ("2023-08-01", "National Day"),
            ("2023-08-15", "Assumption Day"),
            ("2023-09-07", "Genevan Fast"),
            ("2023-09-09", "Knabenschiessen"),
            ("2023-09-10", "Knabenschiessen"),
            ("2023-09-11", "Knabenschiessen"),
            ("2023-09-18", "Prayer Monday"),
            ("2023-09-25", "Saint Nicholas of Flüe"),
            ("2023-11-01", "All Saints' Day"),
            ("2023-12-08", "Immaculate Conception"),
            ("2023-12-24", "Christmas Eve"),
            ("2023-12-25", "Christmas Day"),
            ("2023-12-26", "Saint Stephen's Day"),
            ("2023-12-27", "Bridge Holiday"),
            ("2023-12-28", "Bridge Holiday"),
            ("2023-12-29", "Bridge Holiday"),
            ("2023-12-31", "New Year's Eve; Restoration Day"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2023-01-01", "Nouvel An"),
            ("2023-01-02", "Saint-Berchtold"),
            ("2023-01-06", "Épiphanie"),
            ("2023-03-01", "Instauration de la République"),
            ("2023-03-19", "Saint-Joseph"),
            ("2023-04-06", "Veille du Vendredi saint"),
            ("2023-04-07", "Vendredi saint"),
            ("2023-04-10", "Lundi de Pâques"),
            ("2023-04-13", "Fahrtsfest"),
            ("2023-04-17", "Sechseläuten"),
            ("2023-05-01", "Fête du Travail"),
            ("2023-05-17", "Veille de l'Ascension"),
            ("2023-05-18", "Ascension"),
            ("2023-05-29", "Lundi de Pentecôte"),
            ("2023-06-08", "Fête-Dieu"),
            ("2023-06-23", "Commémoration du plébiscite"),
            ("2023-06-29", "Saint-Pierre et Paul"),
            ("2023-08-01", "Fête nationale"),
            ("2023-08-15", "Assomption"),
            ("2023-09-07", "Jeûne genevois"),
            ("2023-09-09", "Knabenschiessen"),
            ("2023-09-10", "Knabenschiessen"),
            ("2023-09-11", "Knabenschiessen"),
            ("2023-09-18", "Lundi du Jeûne fédéral"),
            ("2023-09-25", "Fête de Saint-Nicolas-de-Flüe"),
            ("2023-11-01", "Toussaint"),
            ("2023-12-08", "Immaculée Conception"),
            ("2023-12-24", "Veille de Noël"),
            ("2023-12-25", "Noël"),
            ("2023-12-26", "Saint-Étienne"),
            ("2023-12-27", "Jour pont"),
            ("2023-12-28", "Jour pont"),
            ("2023-12-29", "Jour pont"),
            ("2023-12-31", "Restauration de la République; Réveillon du Nouvel An"),
        )

    def test_l10n_it(self):
        self.assertLocalizedHolidays(
            "it",
            ("2023-01-01", "Capodanno"),
            ("2023-01-02", "Giorno di Bertoldo"),
            ("2023-01-06", "Epifania"),
            ("2023-03-01", "Giorno della Repubblica"),
            ("2023-03-19", "San Giuseppe"),
            ("2023-04-06", "Vigilia del Venerdì Santo"),
            ("2023-04-07", "Venerdì Santo"),
            ("2023-04-10", "Lunedì dell'Angelo"),
            ("2023-04-13", "Battaglia di Näfels"),
            ("2023-04-17", "Sechseläuten"),
            ("2023-05-01", "Festa del lavoro"),
            ("2023-05-17", "Vigilia dell'Ascensione di Gesù"),
            ("2023-05-18", "Ascensione di Gesù"),
            ("2023-05-29", "Lunedì di Pentecoste"),
            ("2023-06-08", "Corpus Domini"),
            ("2023-06-23", "Festa dell'Indipendenza"),
            ("2023-06-29", "Santi Pietro e Paolo"),
            ("2023-08-01", "Festa nazionale"),
            ("2023-08-15", "Assunzione di Maria"),
            ("2023-09-07", "Digiuno ginevrino"),
            ("2023-09-09", "Knabenschiessen"),
            ("2023-09-10", "Knabenschiessen"),
            ("2023-09-11", "Knabenschiessen"),
            ("2023-09-18", "Lunedì del digiuno federal"),
            ("2023-09-25", "San Nicolao della Flue"),
            ("2023-11-01", "Ognissanti"),
            ("2023-12-08", "Immacolata Concezione"),
            ("2023-12-24", "Vigilia di Natale"),
            ("2023-12-25", "Natale"),
            ("2023-12-26", "Giorno di Santo Stefano"),
            ("2023-12-27", "Giorno ponte"),
            ("2023-12-28", "Giorno ponte"),
            ("2023-12-29", "Giorno ponte"),
            ("2023-12-31", "Restaurazione della Repubblica; Vigilia di Capodanno"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2023-01-01", "วันขึ้นปีใหม่"),
            ("2023-01-02", "วันสมโภชนักบุญแบร์กโทลด์"),
            ("2023-01-06", "วันสมโภชพระคริสต์แสดงองค์"),
            ("2023-03-01", "วันครบรอบการสถาปนาสาธารณรัฐนอยชาแตล"),
            ("2023-03-19", "วันสมโภชนักบุญโยเซฟ"),
            ("2023-04-06", "วันก่อนวันศุกร์ประเสริฐ"),
            ("2023-04-07", "วันศุกร์ประเสริฐ"),
            ("2023-04-10", "วันจันทร์อีสเตอร์"),
            ("2023-04-13", "วันรำลึกชัยชนะยุทธการเนเฟลส์"),
            ("2023-04-17", "เซ็กเซ่ะเล๊าเท่น"),
            ("2023-05-01", "วันแรงงาน"),
            ("2023-05-17", "วันก่อนวันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2023-05-18", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2023-05-29", "วันจันทร์หลังวันสมโภชพระจิตเจ้า"),
            ("2023-06-08", "วันสมโภชพระคริสตวรกาย"),
            ("2023-06-23", "วันประกาศเอกราชจูรา"),
            ("2023-06-29", "วันสมโภชนักบุญเปโตรและเปาโล"),
            ("2023-08-01", "วันชาติสวิตเซอร์แลนด์"),
            ("2023-08-15", "วันสมโภชแม่พระรับเกียรติยกขึ้นสวรรค์"),
            ("2023-09-07", "วันถือศีลอดเจนีวา"),
            ("2023-09-09", "คนาเบนชิสเซน"),
            ("2023-09-10", "คนาเบนชิสเซน"),
            ("2023-09-11", "คนาเบนชิสเซน"),
            ("2023-09-18", "วันจันทร์แห่งการอธิษฐาน"),
            ("2023-09-25", "วันสมโภชนักบุญนิโคลัสแห่งฟลือเออ"),
            ("2023-11-01", "วันสมโภชนักบุญทั้งหลาย"),
            ("2023-12-08", "วันสมโภชแม่พระผู้ปฏิสนธินิรมล"),
            ("2023-12-24", "วันคริสต์มาสอีฟ"),
            ("2023-12-25", "วันคริสต์มาส"),
            ("2023-12-26", "วันสมโภชนักบุญสเตเฟน"),
            ("2023-12-27", "วันหยุดเพิ่มเติม"),
            ("2023-12-28", "วันหยุดเพิ่มเติม"),
            ("2023-12-29", "วันหยุดเพิ่มเติม"),
            ("2023-12-31", "วันกอบกู้เอกราชสาธารณรัฐเจนีวา; วันสิ้นปี"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2023-01-01", "Новий рік"),
            ("2023-01-02", "День Святого Бертольда"),
            ("2023-01-06", "Богоявлення"),
            ("2023-03-01", "Річниця проголошення Республіки"),
            ("2023-03-19", "День Святого Йосипа"),
            ("2023-04-06", "Переддень Страсної п’ятниці"),
            ("2023-04-07", "Страсна пʼятниця"),
            ("2023-04-10", "Великодній понеділок"),
            ("2023-04-13", "Свято перемоги під Нефельсом"),
            ("2023-04-17", "Зексельйотен"),
            ("2023-05-01", "День праці"),
            ("2023-05-17", "Переддень Вознесіння Господнього"),
            ("2023-05-18", "Вознесіння Господнє"),
            ("2023-05-29", "День Святого Духа"),
            ("2023-06-08", "Свято Тіла і Крові Христових"),
            ("2023-06-23", "День незалежності"),
            ("2023-06-29", "День Святих Петра і Павла"),
            ("2023-08-01", "Національне свято"),
            ("2023-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2023-09-07", "Женевський піст"),
            ("2023-09-09", "Кнабеншісен"),
            ("2023-09-10", "Кнабеншісен"),
            ("2023-09-11", "Кнабеншісен"),
            ("2023-09-18", "Молитовний понеділок"),
            ("2023-09-25", "День Святого Ніклауса з Флюе"),
            ("2023-11-01", "День усіх святих"),
            ("2023-12-08", "Непорочне зачаття Діви Марії"),
            ("2023-12-24", "Святий вечір"),
            ("2023-12-25", "Різдво Христове"),
            ("2023-12-26", "День Святого Стефана"),
            ("2023-12-27", "Проміжний вихідний"),
            ("2023-12-28", "Проміжний вихідний"),
            ("2023-12-29", "Проміжний вихідний"),
            ("2023-12-31", "День відновлення республіки; Переддень Нового року"),
        )
