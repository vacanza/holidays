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

from datetime import date

from holidays.countries.switzerland import Switzerland, CH, CHE
from tests.common import TestCase


class TestSwitzerland(TestCase):
    @classmethod
    def setUpClass(cls):
        years = range(1970, 2050)
        super().setUpClass(Switzerland, years=years)
        cls.prov_hols = {prov: CH(subdiv=prov, years=years) for prov in CH.subdivisions}

    def test_country_aliases(self):
        self.assertCountryAliases(Switzerland, CH, CHE)

    def test_all_holidays_present(self):
        y_2018 = set()
        for p in CH.subdivisions:
            y_2018.update(CH(years=2018, subdiv=p).values())
        all_h = {  # Holidays names in their chronological order.
            "Neujahrestag",
            "Berchtoldstag",
            "Heilige Drei Könige",
            "Jahrestag der Ausrufung der Republik",
            "Josefstag",
            "Näfelser Fahrt",
            "Karfreitag",
            "Ostern",
            "Ostermontag",
            "Tag der Arbeit",
            "Auffahrt",
            "Pfingsten",
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
        # Neujahrestag
        self.assertHoliday(f"{year}-01-01" for year in range(1970, 2050))
        # Nationalfeiertag
        self.assertHoliday(f"{year}-08-01" for year in range(1970, 2050))
        # Weihnachten
        self.assertHoliday(f"{year}-12-25" for year in range(1970, 2050))

    def test_berchtoldstag(self):
        provinces_that_have = {
            "AG",
            "BE",
            "FR",
            "GL",
            "JU",
            "LU",
            "NE",
            "OW",
            "SH",
            "SO",
            "TG",
            "VD",
            "ZG",
            "ZH",
        }
        provinces_that_dont = set(CH.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(
                self.prov_hols[province], (f"{year}-01-02" for year in range(1970, 2050))
            )
        for province in provinces_that_dont:
            self.assertNoHoliday(
                self.prov_hols[province], (f"{year}-01-02" for year in range(1970, 2050))
            )

    def test_heilige_drei_koenige(self):
        provinces_that_have = {"SZ", "TI", "UR"}
        provinces_that_dont = set(CH.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(
                self.prov_hols[province], (f"{year}-01-06" for year in range(1970, 2050))
            )
        for province in provinces_that_dont:
            self.assertNoHoliday(
                self.prov_hols[province], (f"{year}-01-06" for year in range(1970, 2050))
            )

    def test_jahrestag_der_ausrufung_der_republik(self):
        provinces_that_have = {"NE"}
        provinces_that_dont = set(CH.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(
                self.prov_hols[province], (f"{year}-03-01" for year in range(1970, 2050))
            )
        for province in provinces_that_dont:
            self.assertNoHoliday(
                self.prov_hols[province], (f"{year}-03-01" for year in range(1970, 2050))
            )

    def test_josefstag(self):
        provinces_that_have = {"NW", "SZ", "TI", "UR", "VS"}
        provinces_that_dont = set(CH.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(
                self.prov_hols[province], (f"{year}-03-19" for year in range(1970, 2050))
            )
        for province in provinces_that_dont:
            self.assertNoHoliday(
                self.prov_hols[province], (f"{year}-03-19" for year in range(1970, 2050))
            )

    def test_naefelser_fahrt(self):
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
        provinces_that_have = {"GL"}
        provinces_that_dont = set(CH.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(self.prov_hols[province], known_good)
        for province in provinces_that_dont:
            self.assertNoHoliday(self.prov_hols[province], known_good)

        self.assertNoHolidayName("Näfelser Fahrt", CH(subdiv="GL", years=1834))

    def test_karfreitag(self):
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
        provinces_that_dont = {"VS"}
        provinces_that_have = set(CH.subdivisions) - provinces_that_dont

        for province in provinces_that_have:
            self.assertHoliday(self.prov_hols[province], known_good)
        for province in provinces_that_dont:
            self.assertNoHoliday(self.prov_hols[province], known_good)

    def test_ostern(self):
        known_good = (
            "2018-04-01",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
            "2025-04-20",
            "2026-04-05",
            "2027-03-28",
            "2028-04-16",
            "2029-04-01",
            "2030-04-21",
            "2031-04-13",
            "2032-03-28",
            "2033-04-17",
            "2034-04-09",
            "2035-03-25",
        )

        for province in CH.subdivisions:
            self.assertHoliday(self.prov_hols[province], known_good)

    def test_ostermontag(self):
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
        provinces_that_dont = {"VS"}
        provinces_that_have = set(CH.subdivisions) - provinces_that_dont

        for province in provinces_that_have:
            self.assertHoliday(self.prov_hols[province], known_good)
        for province in provinces_that_dont:
            self.assertNoHoliday(self.prov_hols[province], known_good)

    def test_auffahrt(self):
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

        for province in CH.subdivisions:
            self.assertHoliday(self.prov_hols[province], known_good)

    def test_pfingsten(self):
        known_good = (
            "2018-05-20",
            "2019-06-09",
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
            "2025-06-08",
            "2026-05-24",
            "2027-05-16",
            "2028-06-04",
            "2029-05-20",
            "2030-06-09",
            "2031-06-01",
            "2032-05-16",
            "2033-06-05",
            "2034-05-28",
            "2035-05-13",
        )

        for province in CH.subdivisions:
            self.assertHoliday(self.prov_hols[province], known_good)

    def test_pfingstmontag(self):
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

        provinces_that_dont = {"VS"}
        provinces_that_have = set(CH.subdivisions) - provinces_that_dont

        for province in provinces_that_have:
            self.assertHoliday(self.prov_hols[province], known_good)
        for province in provinces_that_dont:
            self.assertNoHoliday(self.prov_hols[province], known_good)

    def test_fronleichnam(self):
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
        provinces_that_dont = set(CH.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(self.prov_hols[province], known_good)
        for province in provinces_that_dont:
            self.assertNoHoliday(self.prov_hols[province], known_good)

    def test_fest_der_unabhaengikeit(self):
        provinces_that_have = {"JU"}
        provinces_that_dont = set(CH.subdivisions) - provinces_that_have

        years = set(range(1970, 2050)).difference({2011})
        # 2011 is "Fronleichnam" on the same date, we don't test this year
        for province in provinces_that_have:
            self.assertHoliday(self.prov_hols[province], (f"{year}-06-23" for year in years))
        for province in provinces_that_dont:
            self.assertNoHoliday(self.prov_hols[province], (f"{year}-06-23" for year in years))

    def test_peter_und_paul(self):
        provinces_that_have = {"TI"}
        provinces_that_dont = set(CH.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(
                self.prov_hols[province], (f"{year}-06-29" for year in range(1970, 2050))
            )
        for province in provinces_that_dont:
            self.assertNoHoliday(
                self.prov_hols[province], (f"{year}-06-29" for year in range(1970, 2050))
            )

    def test_mariae_himmelfahrt(self):
        provinces_that_have = {
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
        provinces_that_dont = set(CH.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(
                self.prov_hols[province], (f"{year}-08-15" for year in range(1970, 2050))
            )
        for province in provinces_that_dont:
            self.assertNoHoliday(
                self.prov_hols[province], (f"{year}-08-15" for year in range(1970, 2050))
            )

    def test_lundi_du_jeune(self):
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
        provinces_that_have = {"VD"}
        provinces_that_dont = set(CH.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(self.prov_hols[province], known_good)
        for province in provinces_that_dont:
            self.assertNoHoliday(self.prov_hols[province], known_good)

    def test_bruder_chlaus(self):
        provinces_that_have = {"OW"}
        provinces_that_dont = set(CH.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(
                self.prov_hols[province], (f"{year}-09-25" for year in range(1970, 2050))
            )
        for province in provinces_that_dont:
            self.assertNoHoliday(
                self.prov_hols[province], (f"{year}-09-25" for year in range(1970, 2050))
            )

    def test_allerheiligen(self):
        provinces_that_have = {
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
        provinces_that_dont = set(CH.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(
                self.prov_hols[province], (f"{year}-11-01" for year in range(1970, 2050))
            )
        for province in provinces_that_dont:
            self.assertNoHoliday(
                self.prov_hols[province], (f"{year}-11-01" for year in range(1970, 2050))
            )

    def test_jeune_genevois(self):
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
        provinces_that_have = {"GE"}
        provinces_that_dont = set(CH.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(self.prov_hols[province], known_good)
        for province in provinces_that_dont:
            self.assertNoHoliday(self.prov_hols[province], known_good)

    def test_stephanstag(self):
        provinces_that_have = {
            "AG",
            "AR",
            "AI",
            "BL",
            "BS",
            "BE",
            "FR",
            "GL",
            "GR",
            "LU",
            "NW",
            "OW",
            "SG",
            "SH",
            "SZ",
            "SO",
            "TG",
            "TI",
            "UR",
            "ZG",
            "ZH",
        }
        provinces_that_dont = set(CH.subdivisions) - provinces_that_have - {"NE"}

        for province in provinces_that_have:
            self.assertHoliday(
                self.prov_hols[province], (f"{year}-12-26" for year in range(1970, 2050))
            )
        for province in provinces_that_dont:
            self.assertNoHoliday(
                self.prov_hols[province], (f"{year}-12-26" for year in range(1970, 2050))
            )
        for year in range(1970, 2050):
            dt = date(year, 12, 26)
            self.assertEqual(dt.weekday() == 0, dt in self.prov_hols["NE"])

    def test_wiedererstellung_der_republik(self):
        provinces_that_have = {"GE"}
        provinces_that_dont = set(CH.subdivisions) - provinces_that_have

        for province in provinces_that_have:
            self.assertHoliday(
                self.prov_hols[province], (f"{year}-12-31" for year in range(1970, 2050))
            )
        for province in provinces_that_dont:
            self.assertNoHoliday(
                self.prov_hols[province], (f"{year}-12-31" for year in range(1970, 2050))
            )

    def test_national_feiertag(self):
        # Before 1291, national fiertag was not celebrated
        self.assertNoHoliday("1290-08-01")

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "Neujahrestag"),
            ("2018-04-01", "Ostern"),
            ("2018-05-10", "Auffahrt"),
            ("2018-05-20", "Pfingsten"),
            ("2018-08-01", "Nationalfeiertag"),
            ("2018-12-25", "Weihnachten"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2018-01-01", "New Year's Day"),
            ("2018-04-01", "Easter Sunday"),
            ("2018-05-10", "Ascension Day"),
            ("2018-05-20", "Whit Sunday"),
            ("2018-08-01", "National Day"),
            ("2018-12-25", "Christmas Day"),
        )

    def test_l10n_fr(self):
        self.assertLocalizedHolidays(
            "fr",
            ("2018-01-01", "Nouvel An"),
            ("2018-04-01", "Pâques"),
            ("2018-05-10", "Ascension"),
            ("2018-05-20", "Pentecôte"),
            ("2018-08-01", "Fête nationale"),
            ("2018-12-25", "Noël"),
        )

    def test_l10n_it(self):
        self.assertLocalizedHolidays(
            "it",
            ("2018-01-01", "Capodanno"),
            ("2018-04-01", "Pasqua"),
            ("2018-05-10", "Ascensione di Gesù"),
            ("2018-05-20", "Pentecoste"),
            ("2018-08-01", "Festa nazionale"),
            ("2018-12-25", "Natale"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2018-01-01", "Новий рік"),
            ("2018-04-01", "Великдень"),
            ("2018-05-10", "Вознесіння Господнє"),
            ("2018-05-20", "Трійця"),
            ("2018-08-01", "Національне свято"),
            ("2018-12-25", "Різдво Христове"),
        )
