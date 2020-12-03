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

import os
import sys
import unittest
import warnings
from glob import glob
from itertools import product

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta, MO
from flake8.api import legacy as flake8

import holidays


class TestDE(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.DE()
        self.prov_hols = {
            prov: holidays.DE(prov=prov) for prov in holidays.DE.PROVINCES
        }

    def test_no_data_before_1990(self):
        de_1989 = sum(holidays.DE(years=[1989], prov=p) for p in holidays.DE.PROVINCES)
        self.assertEqual(len(de_1989), 0)

    def test_all_holidays_present(self):
        de_2015 = sum(holidays.DE(years=[2015], prov=p) for p in holidays.DE.PROVINCES)
        in_2015 = sum((de_2015.get_list(key) for key in de_2015), [])
        all_de = [
            "Neujahr",
            "Heilige Drei Könige",
            "Karfreitag",
            "Ostersonntag",
            "Ostermontag",
            "Erster Mai",
            "Christi Himmelfahrt",
            "Pfingstsonntag",
            "Pfingstmontag",
            "Fronleichnam",
            "Mariä Himmelfahrt",
            "Tag der Deutschen Einheit",
            "Reformationstag",
            "Allerheiligen",
            "Buß- und Bettag",
            "Erster Weihnachtstag",
            "Zweiter Weihnachtstag",
        ]

        for holiday in all_de:
            self.assertIn(holiday, in_2015, "missing: {}".format(holiday))
        for holiday in in_2015:
            self.assertIn(holiday, all_de, "extra: {}".format(holiday))

    def test_fixed_holidays(self):
        fixed_days_whole_country = (
            (1, 1),  # Neujahr
            (5, 1),  # Maifeiertag
            (10, 3),  # Tag der Deutschen Einheit
            (12, 25),  # Erster Weihnachtstag
            (12, 26),  # Zweiter Weihnachtstag
        )

        for y, (m, d) in product(range(1991, 2050), fixed_days_whole_country):
            self.assertIn(date(y, m, d), self.holidays)

    def test_tag_der_deutschen_einheit_in_1990(self):
        self.assertIn(date(1990, 10, 3), self.holidays)

    def test_heilige_drei_koenige(self):
        provinces_that_have = {"BW", "BY", "BYP", "ST"}
        provinces_that_dont = set(holidays.DE.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1991, 2050)):
            self.assertIn(date(year, 1, 6), self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1991, 2050)):
            self.assertNotIn(date(year, 1, 6), self.prov_hols[province])

    def test_karfreitag(self):
        known_good = [
            (2014, 4, 18),
            (2015, 4, 3),
            (2016, 3, 25),
            (2017, 4, 14),
            (2018, 3, 30),
            (2019, 4, 19),
            (2020, 4, 10),
            (2021, 4, 2),
            (2022, 4, 15),
            (2023, 4, 7),
            (2024, 3, 29),
        ]

        for province, (y, m, d) in product(holidays.DE.PROVINCES, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])

    def test_ostersonntag(self):
        known_good = [
            (2014, 4, 20),
            (2015, 4, 5),
            (2016, 3, 27),
            (2017, 4, 16),
            (2018, 4, 1),
            (2019, 4, 21),
            (2020, 4, 12),
            (2021, 4, 4),
            (2022, 4, 17),
            (2023, 4, 9),
            (2024, 3, 31),
        ]
        provinces_that_have = {"BB"}
        provinces_that_dont = set(holidays.DE.PROVINCES) - provinces_that_have

        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertNotIn(date(y, m, d), self.prov_hols[province])

    def test_ostermontag(self):
        known_good = [
            (2014, 4, 21),
            (2015, 4, 6),
            (2016, 3, 28),
            (2017, 4, 17),
            (2018, 4, 2),
            (2019, 4, 22),
            (2020, 4, 13),
            (2021, 4, 5),
            (2022, 4, 18),
            (2023, 4, 10),
            (2024, 4, 1),
        ]

        for province, (y, m, d) in product(holidays.DE.PROVINCES, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])

    def test_75_jahrestag_beendigung_zweiter_weltkrieg(self):
        known_good = [(2020, 5, 8)]
        provinces_that_have = {"BE"}
        provinces_that_dont = set(holidays.DE.PROVINCES) - provinces_that_have

        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertNotIn(date(y, m, d), self.prov_hols[province])

    def test_christi_himmelfahrt(self):
        known_good = [
            (2014, 5, 29),
            (2015, 5, 14),
            (2016, 5, 5),
            (2017, 5, 25),
            (2018, 5, 10),
            (2019, 5, 30),
            (2020, 5, 21),
            (2021, 5, 13),
            (2022, 5, 26),
            (2023, 5, 18),
            (2024, 5, 9),
        ]

        for province, (y, m, d) in product(holidays.DE.PROVINCES, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])

    def test_weltkindertag(self):
        known_good = [(2019, 9, 20), (2021, 9, 20)]

        provinces_that_have = {"TH"}
        provinces_that_dont = set(holidays.DE.PROVINCES) - provinces_that_have
        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertNotIn(date(y, m, d), self.prov_hols[province])

    def test_frauentag(self):
        known_good = [
            (2019, 3, 8),
        ]

        provinces_that_have = {"BE"}
        provinces_that_dont = set(holidays.DE.PROVINCES) - provinces_that_have
        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertNotIn(date(y, m, d), self.prov_hols[province])

    def test_pfingstsonntag(self):
        known_good = [
            (2014, 6, 8),
            (2015, 5, 24),
            (2016, 5, 15),
            (2017, 6, 4),
            (2018, 5, 20),
            (2019, 6, 9),
            (2020, 5, 31),
            (2021, 5, 23),
            (2022, 6, 5),
            (2023, 5, 28),
            (2024, 5, 19),
        ]
        provinces_that_have = {"BB"}
        provinces_that_dont = set(holidays.DE.PROVINCES) - provinces_that_have

        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertNotIn(date(y, m, d), self.prov_hols[province])

    def test_pfingstmontag(self):
        known_good = [
            (2014, 6, 9),
            (2015, 5, 25),
            (2016, 5, 16),
            (2017, 6, 5),
            (2018, 5, 21),
            (2019, 6, 10),
            (2020, 6, 1),
            (2021, 5, 24),
            (2022, 6, 6),
            (2023, 5, 29),
            (2024, 5, 20),
        ]

        for province, (y, m, d) in product(holidays.DE.PROVINCES, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])

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
        provinces_that_have = {"BW", "BY", "BYP", "HE", "NW", "RP", "SL"}
        provinces_that_dont = set(holidays.DE.PROVINCES) - provinces_that_have

        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertNotIn(date(y, m, d), self.prov_hols[province])

    def test_mariae_himmelfahrt(self):
        provinces_that_have = {"BY", "SL"}
        provinces_that_dont = set(holidays.DE.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1991, 2050)):
            self.assertIn(date(year, 8, 15), self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1991, 2050)):
            self.assertNotIn(date(year, 8, 15), self.prov_hols[province])

    def test_reformationstag(self):
        prov_that_have = {"BB", "MV", "SN", "ST", "TH"}
        prov_yes_since_2018 = prov_that_have.union({"HB", "HH", "NI", "SH"})
        prov_that_dont = set(holidays.DE.PROVINCES) - prov_that_have
        prov_not_since_2018 = set(holidays.DE.PROVINCES) - prov_yes_since_2018

        for province, year in product(prov_that_have, range(1991, 2050)):
            # in 2017 all states got the reformationstag for that year
            if year == 2017:
                continue
            self.assertIn(date(year, 10, 31), self.prov_hols[province])
        # additional provinces got this holiday 2018
        for province, year in product(prov_yes_since_2018, range(2018, 2050)):
            self.assertIn(date(year, 10, 31), self.prov_hols[province])
        for province, year in product(prov_that_dont, range(1991, 2017)):
            self.assertNotIn(date(year, 10, 31), self.prov_hols[province])
        for province, year in product(prov_not_since_2018, range(2018, 2050)):
            self.assertNotIn(date(year, 10, 31), self.prov_hols[province])
        # check the 2017 case where all states have the reformationstag
        for province in holidays.DE.PROVINCES:
            self.assertIn(date(2017, 10, 31), self.prov_hols[province])

    def test_allerheiligen(self):
        provinces_that_have = {"BW", "BY", "BYP", "NW", "RP", "SL"}
        provinces_that_dont = set(holidays.DE.PROVINCES) - provinces_that_have

        for province, year in product(provinces_that_have, range(1991, 2050)):
            self.assertIn(date(year, 11, 1), self.prov_hols[province])
        for province, year in product(provinces_that_dont, range(1991, 2050)):
            self.assertNotIn(date(year, 11, 1), self.prov_hols[province])

    def test_buss_und_bettag(self):
        known_good = [
            (2014, 11, 19),
            (2015, 11, 18),
            (2016, 11, 16),
            (2017, 11, 22),
            (2018, 11, 21),
            (2019, 11, 20),
            (2020, 11, 18),
            (2021, 11, 17),
            (2022, 11, 16),
            (2023, 11, 22),
            (2024, 11, 20),
        ]
        provinces_that_have = {"SN"}
        provinces_that_dont = set(holidays.DE.PROVINCES) - provinces_that_have

        for province, (y, m, d) in product(provinces_that_have, known_good):
            self.assertIn(date(y, m, d), self.prov_hols[province])
        for province, (y, m, d) in product(provinces_that_dont, known_good):
            self.assertNotIn(date(y, m, d), self.prov_hols[province])

    def test_internationaler_frauentag(self):
        prov_that_have = {"BE"}
        prov_that_dont = set(holidays.DE.PROVINCES) - prov_that_have

        for province, year in product(holidays.DE.PROVINCES, range(1991, 2018)):
            self.assertNotIn(date(year, 3, 8), self.prov_hols[province])
        for province, year in product(prov_that_have, range(2019, 2050)):
            self.assertIn(date(year, 3, 8), self.prov_hols[province])
        for province, year in product(prov_that_dont, range(2019, 2050)):
            self.assertNotIn(date(year, 3, 8), self.prov_hols[province])
