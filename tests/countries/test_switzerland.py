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

from holidays.constants import HALF_DAY, OPTIONAL, PUBLIC
from holidays.countries.switzerland import Switzerland, CH, CHE
from tests.common import CommonCountryTests


class TestSwitzerland(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1970, 2050)
        super().setUpClass(Switzerland, years=years)
        cls.prov_hols = {prov: CH(subdiv=prov, years=years) for prov in CH.subdivisions}
        cls.prov_hols_optional = {
            prov: CH(categories=OPTIONAL, subdiv=prov, years=years) for prov in CH.subdivisions
        }

    def test_country_aliases(self):
        self.assertAliases(Switzerland, CH, CHE)

    def test_all_holidays_present(self):
        y_2018 = set()
        for p in CH.subdivisions:
            y_2018.update(
                CH(categories=(HALF_DAY, OPTIONAL, PUBLIC), years=2018, subdiv=p).values()
            )
        all_h = {  # Holidays names in their chronological order.
            "Neujahrestag",
            "Berchtoldstag",
            "Heilige Drei Könige",
            "Jahrestag der Ausrufung der Republik",
            "Josefstag",
            "Näfelser Fahrt",
            "Karfreitag",
            "Ostermontag",
            "Tag der Arbeit",
            "Auffahrt",
            "Pfingstmontag",
            "Fronleichnam",
            "Fest der Unabhängigkeit",
            "Peter und Paul",
            "Nationalfeiertag",
            "Mariä Himmelfahrt",
            "Bettagsmontag",
            "Bruder Klaus",
            "Allerheiligen",
            "Mariä Empfängnis",
            "Genfer Bettag",
            "Weihnachten",
            "Stephanstag",
            "Wiederherstellung der Republik",
        }

        self.assertEqual(
            all_h,
            y_2018,
            f"missing: {all_h - y_2018 if len(all_h - y_2018) > 0 else 'no'},"
            f" extra: {y_2018 - all_h if len(y_2018 - all_h) > 0 else 'no'}",
        )

    def test_fixed_holidays(self):
        # New Year's Day.
        self.assertHolidayName("Neujahrestag", (f"{year}-01-01" for year in range(1970, 2050)))
        # National Day.
        self.assertHolidayName("Nationalfeiertag", (f"{year}-08-01" for year in range(1970, 2050)))
        # Christmas Day.
        self.assertHolidayName("Weihnachten", (f"{year}-12-25" for year in range(1970, 2050)))

    def test_berchtolds_day(self):
        name = "Berchtoldstag"
        provinces_that_have = {"AG", "BE", "JU", "LU", "TG", "VD", "ZH"}
        provinces_optional = {"FR", "GL", "NW", "OW", "SG", "SH", "SO", "VS", "ZG"}

        self.assertNoHolidayName(name)

        for province, holidays in self.prov_hols.items():
            if province in provinces_that_have:
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-02" for year in range(1970, 2050))
                )
            elif province != "NE":
                self.assertNoHoliday(holidays, (f"{year}-01-02" for year in range(1970, 2050)))
                self.assertNoHolidayName(name, holidays)

        for province, holidays in self.prov_hols_optional.items():
            if province in provinces_optional:
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-02" for year in range(1970, 2050))
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-01-02" for year in range(1970, 2050)))
                self.assertNoHolidayName(name, holidays)

        # When holiday present in NE.
        ne_years = {1978, 1984, 1989, 1995, 2006, 2012, 2017, 2023, 2034, 2040, 2045}
        self.assertHolidayName(name, self.prov_hols["NE"], (f"{year}-01-02" for year in ne_years))
        self.assertNoHoliday(
            self.prov_hols["NE"],
            (f"{year}-01-02" for year in set(range(1970, 2050)).difference(ne_years)),
        )

    def test_epiphany(self):
        name = "Heilige Drei Könige"
        provinces_that_have = {"SZ", "TI", "UR"}

        self.assertNoHolidayName(name)

        for province, holidays in self.prov_hols.items():
            if province in provinces_that_have:
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-06" for year in range(1970, 2050))
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-01-06" for year in range(1970, 2050)))
                self.assertNoHolidayName(name, holidays)

    def test_republic_day(self):
        name = "Jahrestag der Ausrufung der Republik"

        self.assertNoHolidayName(name)

        for province, holidays in self.prov_hols.items():
            if province == "NE":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-01" for year in range(1970, 2050))
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-03-01" for year in range(1970, 2050)))
                self.assertNoHolidayName(name, holidays)

    def test_st_josephs_day(self):
        name = "Josefstag"
        provinces_that_have = {"NW", "SZ", "TI", "UR", "VS"}

        self.assertNoHolidayName(name)

        for province, holidays in self.prov_hols.items():
            if province in provinces_that_have:
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-19" for year in range(1970, 2050))
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-03-19" for year in range(1970, 2050)))
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

        for province, holidays in self.prov_hols.items():
            if province == "GL":
                self.assertHolidayName(name, holidays, known_good)
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

        self.assertNoHolidayName(name, CH(subdiv="GL", years=1834))

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
        provinces_that_dont = {"TI", "VS"}
        provinces_optional = {"GR"}
        provinces_that_have = set(CH.subdivisions) - provinces_that_dont - provinces_optional

        self.assertNoHolidayName(name)

        for province, holidays in self.prov_hols.items():
            if province in provinces_that_have:
                self.assertHolidayName(name, holidays, known_good)
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

        for province, holidays in self.prov_hols_optional.items():
            if province in provinces_optional:
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
        provinces_that_dont = {"NE", "SO"}
        provinces_optional = {"FR", "NW", "OW", "VS", "ZG"}
        provinces_that_have = set(CH.subdivisions) - provinces_that_dont - provinces_optional

        self.assertNoHolidayName(name)

        for province, holidays in self.prov_hols.items():
            if province in provinces_that_have:
                self.assertHolidayName(name, holidays, known_good)
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

        for province, holidays in self.prov_hols_optional.items():
            if province in provinces_optional:
                self.assertHolidayName(name, holidays, known_good)
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

    def test_labor_day(self):
        name = "Tag der Arbeit"
        provinces_that_have = {"AG", "BL", "BS", "JU", "NE", "SH", "TG", "TI", "ZH"}

        self.assertNoHolidayName(name)

        for province, holidays in self.prov_hols.items():
            if province in provinces_that_have:
                self.assertHolidayName(
                    name, holidays, (f"{year}-05-01" for year in range(1970, 2050))
                )
            else:
                self.assertNoHolidayName(
                    name, holidays, (f"{year}-05-01" for year in range(1970, 2050))
                )
                self.assertNoHolidayName(name, holidays)

        self.assertHolidayName(
            name,
            CH(categories=HALF_DAY, subdiv="SO", years=range(1970, 2050)),
            (f"{year}-05-01" for year in range(1970, 2050)),
        )

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
        self.assertHolidayName(name, range(1970, 2050))
        for holidays in self.prov_hols.values():
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

        provinces_that_dont = {"NE", "SO"}
        provinces_optional = {"FR", "NW", "OW", "VS", "ZG"}
        provinces_that_have = set(CH.subdivisions) - provinces_that_dont - provinces_optional

        self.assertNoHolidayName(name)

        for province, holidays in self.prov_hols.items():
            if province in provinces_that_have:
                self.assertHolidayName(name, holidays, known_good)
            elif province in provinces_that_dont:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

        for province, holidays in self.prov_hols_optional.items():
            if province in provinces_optional:
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
        provinces_that_have = {
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

        for province, holidays in self.prov_hols.items():
            if province in provinces_that_have:
                self.assertHolidayName(name, holidays, known_good)
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

    def test_independence_day(self):
        name = "Fest der Unabhängigkeit"

        self.assertNoHolidayName(name)

        for province, holidays in self.prov_hols.items():
            if province == "JU":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-23" for year in range(1970, 2050))
                )
            else:
                self.assertNoHolidayName(
                    name, holidays, (f"{year}-06-23" for year in range(1970, 2050))
                )
                self.assertNoHolidayName(name, holidays)

    def test_saints_peter_and_paul(self):
        name = "Peter und Paul"

        self.assertNoHolidayName(name)

        for province, holidays in self.prov_hols.items():
            if province == "TI":
                self.assertHolidayName(
                    name, holidays, (f"{year}-06-29" for year in range(1970, 2050))
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-06-29" for year in range(1970, 2050)))
                self.assertNoHolidayName(name, holidays)

    def test_assumption_day(self):
        name = "Mariä Himmelfahrt"
        provinces_that_have = {
            "AG",
            "AI",
            "JU",
            "LU",
            "NW",
            "OW",
            "SZ",
            "TI",
            "UR",
            "VS",
            "ZG",
        }

        self.assertNoHolidayName(name)

        for province, holidays in self.prov_hols.items():
            if province in provinces_that_have:
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-15" for year in range(1970, 2050))
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-08-15" for year in range(1970, 2050)))
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

        for province, holidays in self.prov_hols.items():
            if province == "VD":
                self.assertHolidayName(name, holidays, known_good)
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

    def test_saint_nicholas(self):
        name = "Bruder Klaus"

        self.assertNoHolidayName(name)

        for province, holidays in self.prov_hols.items():
            if province == "OW":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-25" for year in range(1970, 2050))
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-09-25" for year in range(1970, 2050)))
                self.assertNoHolidayName(name, holidays)

    def test_all_saints_day(self):
        name = "Allerheiligen"
        provinces_that_have = {
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

        for province, holidays in self.prov_hols.items():
            if province in provinces_that_have:
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in range(1970, 2050))
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-11-01" for year in range(1970, 2050)))
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

        for province, holidays in self.prov_hols.items():
            if province == "GE":
                self.assertHolidayName(name, holidays, known_good)
            else:
                self.assertNoHoliday(holidays, known_good)
                self.assertNoHolidayName(name, holidays)

    def test_immaculate_conception(self):
        name = "Mariä Empfängnis"
        provinces_that_have = {
            "AG",
            "AI",
            "LU",
            "NW",
            "OW",
            "SZ",
            "TI",
            "UR",
            "VS",
            "ZG",
        }

        self.assertNoHolidayName(name)

        for province, holidays in self.prov_hols.items():
            if province in provinces_that_have:
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-08" for year in range(1970, 2050))
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-12-08" for year in range(1970, 2050)))
                self.assertNoHolidayName(name, holidays)

    def test_saint_stephens_day(self):
        name = "Stephanstag"
        provinces_that_have = {
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
        provinces_optional = {"FR", "NW", "OW", "VS", "ZG"}
        provinces_that_dont = (
            set(CH.subdivisions)
            - provinces_that_have
            - provinces_optional
            - {"AI", "AR", "NE", "UR"}
        )

        self.assertNoHolidayName(name)

        for province, holidays in self.prov_hols.items():
            if province in provinces_that_have:
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-26" for year in range(1970, 2050))
                )
            elif province in provinces_that_dont:
                self.assertNoHoliday(holidays, (f"{year}-12-26" for year in range(1970, 2050)))
                self.assertNoHolidayName(name, holidays)

        for province, holidays in self.prov_hols_optional.items():
            if province in provinces_optional:
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-26" for year in range(1970, 2050))
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-12-26" for year in range(1970, 2050)))
                self.assertNoHolidayName(name, holidays)

        # When holiday present in NE.
        ne_years_have = {1977, 1983, 1988, 1994, 2005, 2011, 2016, 2022, 2033, 2039, 2044}
        self.assertHolidayName(
            name, self.prov_hols["NE"], (f"{year}-12-26" for year in ne_years_have)
        )
        self.assertNoHoliday(
            self.prov_hols["NE"],
            (f"{year}-12-26" for year in set(range(1970, 2050)).difference(ne_years_have)),
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
        for province in ("AI", "AR", "UR"):
            self.assertHolidayName(
                name,
                self.prov_hols[province],
                set(range(1970, 2050)).difference(ai_ar_ur_years_dont),
            )
            self.assertNoHoliday(
                self.prov_hols[province],
                (f"{year}-12-26" for year in (f"{year}-12-26" for year in ai_ar_ur_years_dont)),
            )

    def test_restoration_day(self):
        name = "Wiederherstellung der Republik"

        self.assertNoHolidayName(name)

        for province, holidays in self.prov_hols.items():
            if province == "GE":
                self.assertHolidayName(
                    name, holidays, (f"{year}-12-31" for year in range(1970, 2050))
                )
            else:
                self.assertNoHoliday(holidays, (f"{year}-12-31" for year in range(1970, 2050)))
                self.assertNoHolidayName(name, holidays)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "Neujahrestag"),
            ("2023-05-18", "Auffahrt"),
            ("2023-08-01", "Nationalfeiertag"),
            ("2023-12-25", "Weihnachten"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-05-18", "Ascension Day"),
            ("2023-08-01", "National Day"),
            ("2023-12-25", "Christmas Day"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2023-01-01", "Nouvel An"),
            ("2023-05-18", "Ascension"),
            ("2023-08-01", "Fête nationale"),
            ("2023-12-25", "Noël"),
        )

    def test_l10n_it(self):
        self.assertLocalizedHolidays(
            "it",
            ("2023-01-01", "Capodanno"),
            ("2023-05-18", "Ascensione di Gesù"),
            ("2023-08-01", "Festa nazionale"),
            ("2023-12-25", "Natale"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2023-01-01", "Новий рік"),
            ("2023-05-18", "Вознесіння Господнє"),
            ("2023-08-01", "Національне свято"),
            ("2023-12-25", "Різдво Христове"),
        )
