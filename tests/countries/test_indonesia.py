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

from holidays.countries.indonesia import Indonesia, ID, IDN
from tests.common import TestCase


class TestIndonesia(TestCase):
    def setUp(self):
        self.holidays = Indonesia()

    def test_country_aliases(self):
        self.assertCountryAliases(Indonesia, ID, IDN)

    def test_lunar_new_year(self):
        for year, month, day in (
            (2005, 2, 9),
            (2006, 1, 29),
            (2007, 2, 18),
            (2008, 2, 7),
            (2009, 1, 26),
            (2010, 2, 14),
            (2011, 2, 3),
            (2012, 1, 23),
            (2013, 2, 10),
            (2014, 1, 31),
            (2015, 2, 19),
            (2016, 2, 8),
            (2017, 1, 28),
            (2018, 2, 16),
            (2019, 2, 5),
            (2020, 1, 25),
            (2021, 2, 12),
            (2022, 2, 1),
        ):
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "Tahun Baru Imlek",
            )

    def test_day_of_silence(self):
        for year, month, day in (
            (2009, 3, 26),
            (2014, 3, 31),
            (2018, 3, 17),
            (2020, 3, 25),
            (2021, 3, 14),
            (2022, 3, 3),
        ):
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "Hari Suci Nyepi",
            )

        self.assertFalse(Indonesia(years=1982).get_named("Hari Suci Nyepi"))

    def test_islamic_holidays(self):
        for year, month, day in (
            # Eid al-Fitr
            (2001, 12, 16),
            (2001, 12, 17),
            (2011, 8, 30),
            (2011, 8, 31),
            (2018, 6, 15),
            (2018, 6, 16),
            (1991, 4, 15),
            (1991, 4, 16),
            (1996, 2, 19),
            (1996, 2, 20),
            (1999, 1, 18),
            (1999, 1, 19),
            # Eid al-Adha
            (2001, 3, 6),
            (2011, 11, 6),
            (2018, 8, 22),
            (1991, 6, 22),
            (1996, 4, 27),
            (1999, 3, 27),
            # Islamic New Year
            (2001, 3, 26),
            (2011, 11, 27),
            (2018, 9, 11),
            (1991, 7, 12),
            (1996, 5, 18),
            (1999, 4, 17),
            # The Prophet's Birthday
            (2006, 4, 10),
            (2011, 2, 15),
            (2018, 11, 20),
            (1991, 9, 20),
            (1996, 7, 27),
            (1999, 6, 26),
            # The Prophet's Ascension
            (2001, 10, 15),
            (2011, 6, 29),
            (2018, 4, 14),
            (1991, 2, 11),
            (1996, 12, 8),
            (1999, 11, 5),
        ):
            self.assertIn(date(year, month, day), self.holidays)

    def test_vesak(self):
        for year, month, day in (
            (2007, 6, 1),
            (2011, 5, 17),
            (2018, 5, 29),
            (1991, 5, 28),
            (1996, 5, 31),
            (1999, 5, 29),
        ):
            self.assertIn(date(year, month, day), self.holidays)

    def test_common(self):
        self.assertIn(date(2018, 1, 1), self.holidays)  # New Year's Day

        # Labour Day
        self.assertIn(date(1965, 5, 1), self.holidays)
        self.assertIn(date(1968, 5, 1), self.holidays)
        self.assertIn(date(2014, 5, 1), self.holidays)
        self.assertNotIn(date(1969, 5, 1), self.holidays)
        self.assertNotIn(date(2013, 5, 1), self.holidays)

        # Pancasila Day
        self.assertIn(date(2017, 6, 1), self.holidays)
        self.assertIn(date(2020, 6, 1), self.holidays)
        self.assertNotIn(date(2016, 6, 1), self.holidays)

        self.assertIn(date(2006, 4, 14), self.holidays)  # Good Friday
        self.assertIn(date(2013, 5, 9), self.holidays)  # Ascension Day

        self.assertIn(date(2007, 8, 17), self.holidays)  # National Day
        self.assertIn(date(2014, 12, 25), self.holidays)  # Christmas Day

    def test_special(self):
        self.assertIn(date(2018, 6, 27), self.holidays)
        self.assertIn(date(2019, 4, 17), self.holidays)
        self.assertIn(date(2020, 12, 9), self.holidays)

    def test_2021(self):
        for month, day in (
            (1, 1),
            (2, 12),
            (3, 11),
            (3, 14),
            (4, 2),
            (5, 1),
            (5, 13),
            (5, 14),
            (5, 26),
            (6, 1),
            (7, 20),
            (8, 11),
            (8, 17),
            (10, 19),
            (12, 25),
        ):
            self.assertIn(date(2021, month, day), self.holidays)

    def test_2022(self):
        for month, day in (
            (1, 1),
            (2, 1),
            (2, 28),
            (3, 3),
            (4, 15),
            (5, 1),
            (5, 2),
            (5, 3),
            (5, 16),
            (5, 26),
            (6, 1),
            (7, 10),
            (7, 30),
            (8, 17),
            (10, 8),
            (12, 25),
        ):
            self.assertIn(date(2022, month, day), self.holidays)
