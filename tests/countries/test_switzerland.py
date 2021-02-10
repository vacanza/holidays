# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2020
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from itertools import product

from datetime import date

import holidays


class TestSwitzerland(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.CH()
        self.prov_hols = dict(
            (prov, holidays.CH(prov=prov)) for prov in holidays.CH.PROVINCES
        )

    def test_all_holidays_present(self):
        ch_2018 = sum(
            holidays.CH(years=[2018], prov=p) for p in holidays.CH.PROVINCES
        )
        in_2018 = sum((ch_2018.get_list(key) for key in ch_2018), [])
        all_ch = [
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
            "Lundi du Jeûne",
            "Bruder Klaus",
            "Allerheiligen",
            "Mariä Empfängnis",
            "Escalade de Genève",
            "Weihnachten",
            "Stephanstag",
            "Wiederherstellung der Republik",
        ]

        for holiday in all_ch:
            self.assertTrue(holiday in all_ch, "missing: {}".format(holiday))
        for holiday in in_2018:
            self.assertTrue(holiday in in_2018, "extra: {}".format(holiday))

    def test_fixed_holidays(self):
        fixed_days_whole_country = (
            (1, 1),  # Neujahrestag
            (8, 1),  # Nationalfeiertag
            (12, 25),  # Weihnachten
        )
        for y, (m, d) in product(range(1291, 2050), fixed_days_whole_country):
            self.assertTrue(date(y, m, d) in self.holidays)

    def test_berchtoldstag(self):
        provinces_that_have = {
            "AG",
            "BE",
            "FR",
            "GL",
            "GR",
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
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 1, 2) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 1, 2) not in self.prov_hols[province])

    def test_heilige_drei_koenige(self):
        provinces_that_have = {"SZ", "TI", "UR"}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 1, 6) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 1, 6) not in self.prov_hols[province])

    def test_jahrestag_der_ausrufung_der_republik(self):
        provinces_that_have = {"NE"}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 3, 1) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 3, 1) not in self.prov_hols[province])

    def test_josefstag(self):
        provinces_that_have = {"NW", "SZ", "TI", "UR", "VS"}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 3, 19) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 3, 19) not in self.prov_hols[province])

    def test_naefelser_fahrt(self):
        known_good = [
            (2018, 4, 5),
            (2019, 4, 4),
            (2020, 4, 2),
            (2021, 4, 8),
            (2022, 4, 7),
            (2023, 4, 13),
            (2024, 4, 4),
            (2025, 4, 3),
            (2026, 4, 9),
            (2027, 4, 1),
            (2028, 4, 6),
            (2029, 4, 5),
            (2030, 4, 4),
            (2031, 4, 3),
            (2032, 4, 1),
            (2033, 4, 7),
            (2034, 4, 13),
            (2035, 4, 5),
        ]
        provinces_that_have = {"GL"}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertTrue(date(y, m, d) in self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertTrue(date(y, m, d) not in self.prov_hols[province])

    def test_karfreitag(self):
        known_good = [
            (2018, 3, 30),
            (2019, 4, 19),
            (2020, 4, 10),
            (2021, 4, 2),
            (2022, 4, 15),
            (2023, 4, 7),
            (2024, 3, 29),
            (2025, 4, 18),
            (2026, 4, 3),
            (2027, 3, 26),
            (2028, 4, 14),
            (2029, 3, 30),
            (2030, 4, 19),
            (2031, 4, 11),
            (2032, 3, 26),
            (2033, 4, 15),
            (2034, 4, 7),
            (2035, 3, 23),
        ]
        provinces_that_dont = {"VS"}
        provinces_that_have = set(holidays.CH.PROVINCES) - provinces_that_dont
        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertTrue(date(y, m, d) in self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertTrue(date(y, m, d) not in self.prov_hols[province])

    def test_ostern(self):
        known_good = [
            (2018, 4, 1),
            (2019, 4, 21),
            (2020, 4, 12),
            (2021, 4, 4),
            (2022, 4, 17),
            (2023, 4, 9),
            (2024, 3, 31),
            (2025, 4, 20),
            (2026, 4, 5),
            (2027, 3, 28),
            (2028, 4, 16),
            (2029, 4, 1),
            (2030, 4, 21),
            (2031, 4, 13),
            (2032, 3, 28),
            (2033, 4, 17),
            (2034, 4, 9),
            (2035, 3, 25),
        ]

        for province, (y, m, d) in product(holidays.CH.PROVINCES, known_good):
            self.assertTrue(date(y, m, d) in self.prov_hols[province])

    def test_ostermontag(self):
        known_good = [
            (2018, 4, 2),
            (2019, 4, 22),
            (2020, 4, 13),
            (2021, 4, 5),
            (2022, 4, 18),
            (2023, 4, 10),
            (2024, 4, 1),
            (2025, 4, 21),
            (2026, 4, 6),
            (2027, 3, 29),
            (2028, 4, 17),
            (2029, 4, 2),
            (2030, 4, 22),
            (2031, 4, 14),
            (2032, 3, 29),
            (2033, 4, 18),
            (2034, 4, 10),
            (2035, 3, 26),
        ]
        provinces_that_dont = {"VS"}
        provinces_that_have = set(holidays.CH.PROVINCES) - provinces_that_dont
        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertTrue(date(y, m, d) in self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertTrue(date(y, m, d) not in self.prov_hols[province])

    def test_auffahrt(self):
        known_good = [
            (2018, 5, 10),
            (2019, 5, 30),
            (2020, 5, 21),
            (2021, 5, 13),
            (2022, 5, 26),
            (2023, 5, 18),
            (2024, 5, 9),
            (2025, 5, 29),
            (2026, 5, 14),
            (2027, 5, 6),
            (2028, 5, 25),
            (2029, 5, 10),
            (2030, 5, 30),
            (2031, 5, 22),
            (2032, 5, 6),
            (2033, 5, 26),
            (2034, 5, 18),
            (2035, 5, 3),
        ]

        for province, (y, m, d) in product(holidays.CH.PROVINCES, known_good):
            self.assertTrue(date(y, m, d) in self.prov_hols[province])

    def test_pfingsten(self):
        known_good = [
            (2018, 5, 20),
            (2019, 6, 9),
            (2020, 5, 31),
            (2021, 5, 23),
            (2022, 6, 5),
            (2023, 5, 28),
            (2024, 5, 19),
            (2025, 6, 8),
            (2026, 5, 24),
            (2027, 5, 16),
            (2028, 6, 4),
            (2029, 5, 20),
            (2030, 6, 9),
            (2031, 6, 1),
            (2032, 5, 16),
            (2033, 6, 5),
            (2034, 5, 28),
            (2035, 5, 13),
        ]

        for province, (y, m, d) in product(holidays.CH.PROVINCES, known_good):
            self.assertTrue(date(y, m, d) in self.prov_hols[province])

    def test_pfingstmontag(self):
        known_good = [
            (2018, 5, 21),
            (2019, 6, 10),
            (2020, 6, 1),
            (2021, 5, 24),
            (2022, 6, 6),
            (2023, 5, 29),
            (2024, 5, 20),
            (2025, 6, 9),
            (2026, 5, 25),
            (2027, 5, 17),
            (2028, 6, 5),
            (2029, 5, 21),
            (2030, 6, 10),
            (2031, 6, 2),
            (2032, 5, 17),
            (2033, 6, 6),
            (2034, 5, 29),
            (2035, 5, 14),
        ]

        for province, (y, m, d) in product(holidays.CH.PROVINCES, known_good):
            self.assertTrue(date(y, m, d) in self.prov_hols[province])

    def test_fronleichnam(self):
        known_good = [
            (2014, 6, 19),
            (2015, 6, 4),
            (2016, 5, 26),
            (2017, 6, 15),
            (2018, 5, 31),
            (2019, 6, 20),
            (2020, 6, 11),
            (2021, 6, 3),
            (2022, 6, 16),
            (2023, 6, 8),
            (2024, 5, 30),
        ]
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
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertTrue(date(y, m, d) in self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertTrue(date(y, m, d) not in self.prov_hols[province])

    def test_fest_der_unabhaengikeit(self):
        provinces_that_have = {"JU"}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 6, 23) in self.prov_hols[province])
        # 2011 is "Fronleichnam" on the same date, we don't test this year
        for province, year in product(provinces_that_dont, range(1970, 2010)):
            self.assertTrue(date(year, 6, 23) not in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(2012, 2050)):
            self.assertTrue(date(year, 6, 23) not in self.prov_hols[province])

    def test_peter_und_paul(self):
        provinces_that_have = {"TI"}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 6, 29) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 6, 29) not in self.prov_hols[province])

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
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 8, 15) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 8, 15) not in self.prov_hols[province])

    def test_lundi_du_jeune(self):
        known_good = [
            (2014, 9, 22),
            (2015, 9, 21),
            (2016, 9, 19),
            (2017, 9, 18),
            (2018, 9, 17),
            (2019, 9, 16),
            (2020, 9, 21),
            (2021, 9, 20),
            (2022, 9, 19),
            (2023, 9, 18),
            (2024, 9, 16),
        ]
        provinces_that_have = {"VD"}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertTrue(date(y, m, d) in self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertTrue(date(y, m, d) not in self.prov_hols[province])

    def test_bruder_chlaus(self):
        provinces_that_have = {"OW"}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 9, 25) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 9, 25) not in self.prov_hols[province])

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
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 11, 1) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 11, 1) not in self.prov_hols[province])

    def test_jeune_genevois(self):
        known_good = [
            (2014, 9, 11),
            (2015, 9, 10),
            (2016, 9, 8),
            (2017, 9, 7),
            (2018, 9, 6),
            (2019, 9, 5),
            (2020, 9, 10),
            (2021, 9, 9),
            (2022, 9, 8),
            (2023, 9, 7),
            (2024, 9, 5),
            (2025, 9, 11),
        ]
        provinces_that_have = {"GE"}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertTrue(date(y, m, d) in self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertTrue(date(y, m, d) not in self.prov_hols[province])

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
            "NE",
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
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 12, 26) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 12, 26) not in self.prov_hols[province])

    def test_wiedererstellung_der_republik(self):
        provinces_that_have = {"GE"}
        provinces_that_dont = set(holidays.CH.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1970, 2050)):
            self.assertTrue(date(year, 12, 31) in self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1970, 2050)):
            self.assertTrue(date(year, 12, 31) not in self.prov_hols[province])
