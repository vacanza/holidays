#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date

import holidays


class TestKorea(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.KR()

    def test_common(self):
        holidaysNoObserved = holidays.KR(observed=False)
        self.assertEqual(
            holidaysNoObserved[date(2019, 1, 1)], "New Year's Day"
        )

        self.assertNotIn(date(1582, 10, 2), self.holidays)
        self.assertNotIn(date(1582, 11, 14), self.holidays)

    def test_first_day_of_january(self):
        for year in range(2006, 2021):
            self.assertIn(self.holidays[date(year, 1, 1)], "New Year's Day")

    def test_lunar_new_year(self):
        for year, month, day in [
            (2006, 1, 28),
            (2007, 2, 17),
            (2010, 2, 13),
            (2014, 1, 30),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The day preceding of Lunar New Year's Day",
            )

        for year, month, day in [
            (1916, 2, 4),
            (1944, 1, 26),
            (1954, 2, 4),
            (1958, 2, 19),
            (1966, 1, 22),
            (1988, 2, 18),
            (1997, 2, 8),
            (2008, 2, 7),
            (2009, 1, 26),
            (2011, 2, 3),
            (2012, 1, 23),
            (2014, 1, 31),
            (2015, 2, 19),
            (2016, 2, 8),
            (2017, 1, 28),
            (2018, 2, 16),
            (2019, 2, 5),
            (2020, 1, 25),
            (2027, 2, 7),
            (2028, 1, 27),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)], "Lunar New Year's Day"
            )

        for year, month, day in [
            (2006, 1, 30),
            (2007, 2, 19),
            (2008, 2, 8),
            (2009, 1, 27),
            (2010, 2, 15),
            (2011, 2, 4),
            (2012, 1, 24),
            (2013, 2, 11),
            (2014, 2, 1),
            (2015, 2, 20),
            (2016, 2, 9),
            (2018, 2, 17),
            (2019, 2, 6),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The second day of Lunar New Year's Day",
            )

        for year, month, day in [(2016, 2, 10), (2017, 1, 30), (2020, 1, 27)]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "Alternative holiday of Lunar New Year's Day",
            )

        self.assertNotIn(date(2015, 2, 21), self.holidays)
        self.assertNotIn(date(2015, 2, 7), self.holidays)

    def test_independence_movement_day(self):
        for year, month, day in [
            (2006, 3, 1),
            (2022, 3, 1),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "Independence Movement Day",
            )

        for year, month, day in [(2025, 3, 3)]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "Alternative holiday of Independence Movement Day",
            )

    def test_tree_planting_day(self):
        for year, month, day in [
            (1949, 4, 5),
            (2005, 4, 5),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)], "Tree Planting Day"
            )

        for year, month, day in [
            (1960, 4, 5),
            (2006, 4, 5),
        ]:
            self.assertNotIn(date(year, month, day), self.holidays)

    def test_childrens_day(self):
        for year, month, day in [
            (2015, 5, 5),
            (2018, 5, 5),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)], "Children's Day"
            )

        for year, month, day in [(2018, 5, 7), (2019, 5, 6)]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "Alternative holiday of Children's Day",
            )
        for year, month, day in [(2025, 5, 6), (2044, 5, 6)]:
            self.assertIn(
                "Alternative holiday of Children's Day",
                self.holidays[date(year, month, day)],
            )

    def test_birthday_of_buddha(self):
        name = "Birthday of the Buddha"
        for year, month, day in [
            (1931, 5, 25),
            (1968, 5, 5),
            (2010, 5, 21),
            (2011, 5, 10),
            (2012, 5, 28),
            (2013, 5, 17),
            (2014, 5, 6),
            (2015, 5, 25),
            (2016, 5, 14),
            (2017, 5, 3),
            (2018, 5, 22),
            (2019, 5, 12),
            (2020, 4, 30),
            (2021, 5, 19),
            (2022, 5, 8),
            (2023, 5, 27),
            (2024, 5, 15),
            (2026, 5, 24),
            (2027, 5, 13),
            (2028, 5, 2),
            (2029, 5, 20),
            (2030, 5, 9),
        ]:
            self.assertEqual(self.holidays[date(year, month, day)], name)

        for year, month, day in [(2001, 5, 1)]:
            self.assertIn(
                "Birthday of the Buddha", self.holidays[date(year, month, day)]
            )

    def test_labour_day(self):
        for year in [1948, 1993]:
            self.assertIn("Labour Day", self.holidays[date(year, 3, 10)])

        for year in [1994, 2023]:
            self.assertIn("Labour Day", self.holidays[date(year, 5, 1)])

        self.assertNotIn(date(1993, 5, 1), self.holidays)
        self.assertNotIn(date(1994, 3, 10), self.holidays)

    def test_memorial_day(self):
        for year in [2006, 2022]:
            self.assertEqual(self.holidays[date(year, 6, 6)], "Memorial Day")

    def test_constitution_day(self):
        for year in [1948, 2007]:
            self.assertEqual(
                self.holidays[date(year, 7, 17)], "Constitution Day"
            )
        self.assertNotIn(date(1947, 7, 17), self.holidays)
        self.assertNotIn(date(2008, 7, 17), self.holidays)

    def test_liberation_day(self):
        for year in [1945, 2020]:
            self.assertEqual(
                self.holidays[date(year, 8, 15)], "Liberation Day"
            )
        self.assertEqual(
            self.holidays[date(2021, 8, 16)],
            "Alternative holiday of Liberation Day",
        )

    def test_chuseok(self):
        for year, month, day in [
            (2010, 9, 21),
            (2011, 9, 11),
            (2012, 9, 29),
            (2013, 9, 18),
            (2014, 9, 7),
            (2015, 9, 26),
            (2016, 9, 14),
            (2018, 9, 23),
            (2019, 9, 12),
            (2020, 9, 30),
            (2021, 9, 20),
            (2022, 9, 9),
            (2023, 9, 28),
            (2024, 9, 16),
            (2025, 10, 5),
            (2026, 9, 24),
            (2027, 9, 14),
            (2028, 10, 2),
            (2029, 9, 21),
            (2030, 9, 11),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The day preceding of Chuseok",
            )

        for year, month, day in [(2017, 10, 3)]:
            self.assertIn(
                "The day preceding of Chuseok",
                self.holidays[date(year, month, day)],
            )

        for year, month, day in [
            (1942, 9, 25),
            (1978, 9, 17),
            (2010, 9, 22),
            (2011, 9, 12),
            (2012, 9, 30),
            (2013, 9, 19),
            (2014, 9, 8),
            (2015, 9, 27),
            (2016, 9, 15),
            (2017, 10, 4),
            (2018, 9, 24),
            (2019, 9, 13),
            (2020, 10, 1),
            (2021, 9, 21),
            (2022, 9, 10),
            (2023, 9, 29),
            (2024, 9, 17),
            (2025, 10, 6),
            (2026, 9, 25),
            (2027, 9, 15),
            (2029, 9, 22),
            (2030, 9, 12),
            (2040, 9, 21),
        ]:
            self.assertEqual(self.holidays[date(year, month, day)], "Chuseok")

        for year, month, day in [(2028, 10, 3)]:
            self.assertIn("Chuseok", self.holidays[date(year, month, day)])

        for year, month, day in [
            (2010, 9, 23),
            (2011, 9, 13),
            (2012, 10, 1),
            (2013, 9, 20),
            (2014, 9, 9),
            (2015, 9, 28),
            (2016, 9, 16),
            (2017, 10, 5),
            (2018, 9, 25),
            (2019, 9, 14),
            (2020, 10, 2),
            (2021, 9, 22),
            (2022, 9, 11),
            (2023, 9, 30),
            (2024, 9, 18),
            (2025, 10, 7),
            (2026, 9, 26),
            (2027, 9, 16),
            (2028, 10, 4),
            (2029, 9, 23),
            (2030, 9, 13),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The second day of Chuseok",
            )

        for year, month, day in [
            (2014, 9, 10),
            (2015, 9, 29),
            (2018, 9, 26),
            (2022, 9, 12),
            (2025, 10, 8),
            (2029, 9, 24),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "Alternative holiday of Chuseok",
            )

    def test_national_foundation_day(self):
        for year in [1951, 2049]:
            self.assertIn(
                "National Foundation Day", self.holidays[date(year, 10, 3)]
            )

        for year, month, day in [(2021, 10, 4)]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "Alternative holiday of National Foundation Day",
            )

    def test_hangeul_day(self):
        for year in [1948, 1990]:
            self.assertEqual(self.holidays[date(year, 10, 9)], "Hangeul Day")

        for year in [2013, 2023]:
            self.assertEqual(self.holidays[date(year, 10, 9)], "Hangeul Day")

        for year in [1991, 2012]:
            self.assertNotIn(date(year, 10, 9), self.holidays)

        for year, month, day in [(2021, 10, 11)]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "Alternative holiday of Hangeul Day",
            )

    def test_christmas_day(self):
        for year in [1948, 2050]:
            self.assertEqual(
                self.holidays[date(year, 12, 25)], "Christmas Day"
            )

    def test_years_range(self):
        self.holidays = holidays.KR(years=[2006, 2021])
        for year in [2006, 2021]:
            self.assertIn(self.holidays[date(year, 1, 1)], "New Year's Day")

    def test_special_holidays(self):
        self.assertIn("2020-08-17", self.holidays)
