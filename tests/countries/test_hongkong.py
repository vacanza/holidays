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

from holidays.countries.hongkong import HongKong, HK, HKG
from tests.common import TestCase


class TestHongKong(TestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass(HongKong)

    def test_country_aliases(self):
        self.assertCountryAliases(HongKong, HK, HKG)

    def test_common(self):
        self.assertNonObservedHoliday("2019-01-01")
        self.assertNonObservedHolidaysName(
            "The first day of January",
            "2019-01-01",
        )

        self.assertEqual(
            self.holidays[date(2015, 9, 3)],
            "The 70th anniversary day of the victory of the Chinese "
            "people's war of resistance against Japanese aggression",
        )
        self.assertEqual(len(HongKong(years=1945)), 0)

    def test_first_day_of_january(self):
        exception_years = (2006, 2012, 2017, 2023)
        for year in range(2006, 2024):
            if year in exception_years:
                self.assertEqual(
                    self.holidays[date(year, 1, 2)],
                    "The day following the first day of January",
                )
            else:
                self.assertEqual(
                    self.holidays[date(year, 1, 1)],
                    "The first day of January",
                )

    def test_lunar_new_year(self):
        for year, month, day in [(2006, 1, 28), (2007, 2, 17), (2010, 2, 13)]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The day preceding Lunar New Year's Day",
            )

        for year, month, day in [
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
            (2021, 2, 12),
            (2022, 2, 1),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "Lunar New Year's Day",
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
            (2021, 2, 13),
            (2022, 2, 2),
            (2023, 1, 23),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The second day of Lunar New Year",
            )

        for year, month, day in [
            (2006, 1, 31),
            (2007, 2, 20),
            (2008, 2, 9),
            (2009, 1, 28),
            (2010, 2, 16),
            (2011, 2, 5),
            (2012, 1, 25),
            (2013, 2, 12),
            (2015, 2, 21),
            (2016, 2, 10),
            (2017, 1, 30),
            (2019, 2, 7),
            (2020, 1, 27),
            (2022, 2, 3),
            (2023, 1, 24),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The third day of Lunar New Year",
            )

        for year, month, day in [
            (2013, 2, 13),
            (2014, 2, 3),
            (2017, 1, 31),
            (2018, 2, 19),
            (2020, 1, 28),
            (2021, 2, 15),
            (2023, 1, 25),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The fourth day of Lunar New Year",
            )

    def test_ching_ming_festival(self):
        for year, month, day in [
            (2006, 4, 5),
            (2007, 4, 5),
            (2008, 4, 4),
            (2009, 4, 4),
            (2011, 4, 5),
            (2012, 4, 4),
            (2013, 4, 4),
            (2014, 4, 5),
            (2016, 4, 4),
            (2017, 4, 4),
            (2018, 4, 5),
            (2019, 4, 5),
            (2020, 4, 4),
            (2022, 4, 5),
            (2023, 4, 5),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "Ching Ming Festival",
            )

        for year, month, day in [(2010, 4, 6), (2015, 4, 6), (2021, 4, 5)]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The day following Ching Ming Festival",
            )

    def test_easter(self):
        for year, month, day in [
            (2006, 4, 14),
            (2007, 4, 6),
            (2008, 3, 21),
            (2009, 4, 10),
            (2010, 4, 2),
            (2011, 4, 22),
            (2012, 4, 6),
            (2013, 3, 29),
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
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)], "Good Friday"
            )

        for year, month, day in [
            (2006, 4, 15),
            (2007, 4, 7),
            (2008, 3, 22),
            (2009, 4, 11),
            (2010, 4, 3),
            (2011, 4, 23),
            (2012, 4, 7),
            (2013, 3, 30),
            (2014, 4, 19),
            (2015, 4, 4),
            (2016, 3, 26),
            (2017, 4, 15),
            (2018, 3, 31),
            (2019, 4, 20),
            (2020, 4, 11),
            (2021, 4, 3),
            (2022, 4, 16),
            (2023, 4, 8),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The day following Good Friday",
            )

        for year, month, day in [
            (2006, 4, 17),
            (2007, 4, 9),
            (2008, 3, 24),
            (2009, 4, 13),
            (2010, 4, 5),
            (2011, 4, 25),
            (2012, 4, 9),
            (2013, 4, 1),
            (2014, 4, 21),
            (2016, 3, 28),
            (2017, 4, 17),
            (2018, 4, 2),
            (2019, 4, 22),
            (2020, 4, 13),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)], "Easter Monday"
            )

        for year, month, day in [(2015, 4, 7), (2021, 4, 6)]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The day following Easter Monday",
            )

    def test_birthday_of_buddha(self):
        for year, month, day in [
            (2006, 5, 5),
            (2007, 5, 24),
            (2008, 5, 12),
            (2009, 5, 2),
            (2010, 5, 21),
            (2011, 5, 10),
            (2012, 4, 28),
            (2013, 5, 17),
            (2014, 5, 6),
            (2015, 5, 25),
            (2016, 5, 14),
            (2017, 5, 3),
            (2018, 5, 22),
            (2020, 4, 30),
            (2021, 5, 19),
            (2023, 5, 26),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The Birthday of the Buddha",
            )

        for year, month, day in [
            (2019, 5, 13),
            (2022, 5, 9),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The day following The Birthday of the Buddha",
            )

    def test_labour_day(self):
        for year in [
            1998,
            2006,
            2007,
            2008,
            2009,
            2010,
            2012,
            2013,
            2014,
            2015,
            2017,
            2018,
            2019,
            2020,
            2021,
            2023,
        ]:
            self.assertEqual(self.holidays[date(year, 5, 1)], "Labour Day")

        for year in (2011, 2016, 2022):
            self.assertEqual(
                self.holidays[date(year, 5, 2)],
                "The day following Labour Day",
            )

        self.assertNotIn(date(1997, 5, 1), self.holidays)
        self.assertNotIn(date(1997, 5, 2), self.holidays)

    def test_tuen_ng_festival(self):
        for year, month, day in [
            (2006, 5, 31),
            (2007, 6, 19),
            (2009, 5, 28),
            (2010, 6, 16),
            (2011, 6, 6),
            (2012, 6, 23),
            (2013, 6, 12),
            (2014, 6, 2),
            (2015, 6, 20),
            (2016, 6, 9),
            (2017, 5, 30),
            (2018, 6, 18),
            (2019, 6, 7),
            (2020, 6, 25),
            (2021, 6, 14),
            (2022, 6, 3),
            (2023, 6, 22),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "Tuen Ng Festival",
            )

        self.assertEqual(
            self.holidays[date(2008, 6, 9)],
            "The day following Tuen Ng Festival",
        )

    def test_hksar_day(self):
        for year in [
            1997,
            2006,
            2008,
            2009,
            2010,
            2011,
            2013,
            2014,
            2015,
            2016,
            2017,
            2019,
            2020,
        ]:
            self.assertEqual(
                self.holidays[date(year, 7, 1)],
                "Hong Kong Special Administrative Region Establishment Day",
            )

        for year in (2007, 2012, 2018):
            self.assertEqual(
                self.holidays[date(year, 7, 2)],
                (
                    "The day following Hong Kong Special Administrative "
                    "Region Establishment Day"
                ),
            )

        self.assertNotIn(date(1996, 7, 1), self.holidays)
        self.assertNotIn(date(1996, 7, 2), self.holidays)

    def test_mid_autumn_festival(self):
        for year, month, day in [
            (2003, 9, 12),
            (2004, 9, 29),
            (2005, 9, 19),
            (2006, 10, 7),
            (2007, 9, 26),
            (2008, 9, 15),
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
            (2023, 9, 30),
            (2024, 9, 18),
            (2025, 10, 7),
            (2026, 9, 26),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The day following the Chinese Mid-Autumn Festival",
            )

        for year, month, day in [(2002, 9, 21), (2009, 10, 3)]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "Chinese Mid-Autumn Festival",
            )

        for year, month, day in [(2022, 9, 12)]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The second day of the Chinese Mid-Autumn Festival (Monday)",
            )

    def test_national_day(self):
        for year in [
            2007,
            2008,
            2009,
            2010,
            2011,
            2013,
            2014,
            2015,
            2016,
            2018,
            2019,
            2020,
            2021,
            2022,
        ]:
            self.assertEqual(self.holidays[date(year, 10, 1)], "National Day")

        for year in (2006, 2012, 2017, 2023):
            self.assertEqual(
                self.holidays[date(year, 10, 2)],
                "The day following National Day",
            )

    def test_chung_yeung_festival(self):
        for year, month, day in [
            (2006, 10, 30),
            (2007, 10, 19),
            (2008, 10, 7),
            (2009, 10, 26),
            (2010, 10, 16),
            (2011, 10, 5),
            (2012, 10, 23),
            (2014, 10, 2),
            (2015, 10, 21),
            (2017, 10, 28),
            (2018, 10, 17),
            (2019, 10, 7),
            (2021, 10, 14),
            (2022, 10, 4),
            (2023, 10, 23),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "Chung Yeung Festival",
            )

        for year, month, day in [
            (2013, 10, 14),
            (2016, 10, 10),
            (2020, 10, 26),
        ]:
            self.assertEqual(
                self.holidays[date(year, month, day)],
                "The day following Chung Yeung Festival",
            )

    def test_christmas_day(self):
        for year in [
            2006,
            2007,
            2008,
            2009,
            2010,
            2012,
            2013,
            2014,
            2015,
            2017,
            2018,
            2019,
            2020,
            2021,
            2023,
        ]:
            self.assertEqual(
                self.holidays[date(year, 12, 25)], "Christmas Day"
            )

        for year in (2005, 2011, 2016, 2022):
            self.assertNotIn(date(year, 12, 25), self.holidays)

        name = "The first weekday after Christmas Day"
        for year in range(2006, 2010):
            self.assertEqual(self.holidays[date(year, 12, 26)], name)
        self.assertEqual(self.holidays[date(2010, 12, 27)], name)
        for year in range(2011, 2021):
            self.assertEqual(self.holidays[date(year, 12, 26)], name)
        self.assertEqual(self.holidays[date(2021, 12, 27)], name)
        for year in range(2022, 2024):
            self.assertEqual(self.holidays[date(year, 12, 26)], name)

        name = "The second weekday after Christmas Day"
        self.assertEqual(self.holidays[date(2011, 12, 27)], name)
        self.assertEqual(self.holidays[date(2016, 12, 27)], name)
        self.assertEqual(self.holidays[date(2022, 12, 27)], name)

    def test_old_holidays(self):
        for year, month, day in [
            # Queen's Birthday
            (1952, 6, 9),
            (1987, 6, 8),
            (1990, 6, 11),
            (1997, 6, 9),
            # Anniversary of the liberation of Hong Kong
            # and Anniversary of the victory in the Second Sino-Japanese War
            (1980, 8, 24),
            (1980, 8, 25),
            (1990, 8, 26),
            (1990, 8, 27),
            (1996, 8, 25),
            (1996, 8, 26),
        ]:
            self.assertIn(date(year, month, day), self.holidays)
