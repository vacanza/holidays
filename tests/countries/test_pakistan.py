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
from datetime import timedelta as td

from holidays.countries.pakistan import Pakistan, PK, PAK
from tests.common import TestCase


class TestPakistan(TestCase):
    def setUp(self):
        self.holidays = Pakistan()

    def test_country_aliases(self):
        self.assertCountryAliases(Pakistan, PK, PAK)

    def test_no_holidays(self):
        self.assertNoHolidays(Pakistan(years=1947))

    def test_kashmir_day(self):
        name = "Kashmir Solidarity Day"
        for year in range(1990, 2050):
            self.assertIn(name, Pakistan(years=year).get(f"{year}-02-05"))
        for year in range(1948, 1990):
            self.assertEqual(Pakistan(years=year).get_named(name), [])

    def test_pakistan_day(self):
        name = "Pakistan Day"
        for year in range(1956, 2050):
            self.assertIn(name, Pakistan(years=year).get(f"{year}-03-23"))
        for year in range(1948, 1956):
            self.assertEqual(Pakistan(years=year).get_named(name), [])

    def test_labour_day(self):
        name = "Labour Day"
        for year in range(1972, 2050):
            self.assertIn(name, Pakistan(years=year).get(f"{year}-05-01"))
        for year in range(1948, 1972):
            self.assertEqual(Pakistan(years=year).get_named(name), [])

    def test_independence_day(self):
        name = "Independence Day"
        for year in range(1948, 2050):
            self.assertIn(name, Pakistan(years=year).get(f"{year}-08-14"))

    def test_iqbal_day(self):
        name = "Iqbal Day"
        for year in range(1948, 2015):
            self.assertIn(name, Pakistan(years=year).get(f"{year}-11-09"))
        for year in range(2022, 2050):
            self.assertIn(name, Pakistan(years=year).get(f"{year}-11-09"))
        for year in range(2015, 2022):
            self.assertEqual(Pakistan(years=year).get_named(name), [])

    def test_quaid_e_azam_day(self):
        name = "Quaid-e-Azam Day"
        for year in range(1948, 2050):
            self.assertIn(name, Pakistan(years=year).get(f"{year}-12-25"))

    def test_eid_ul_fitr(self):
        name = "Eid-ul-Fitr"
        for dt in (
            date(2000, 1, 8),
            date(2000, 12, 27),
            date(2001, 12, 16),
            date(2002, 12, 5),
            date(2003, 11, 25),
            date(2004, 11, 14),
            date(2005, 11, 4),
            date(2006, 10, 24),
            date(2013, 8, 8),
            date(2019, 6, 5),
            date(2020, 5, 24),
            date(2021, 5, 13),
            date(2022, 5, 3),
            date(2023, 4, 21),
        ):
            self.assertHoliday(dt)
            self.assertHoliday(dt + td(days=+1))
            self.assertHoliday(dt + td(days=+2))
            self.assertIn(name, self.holidays.get(dt))

    def test_eid_ul_adha(self):
        name = "Eid-ul-Adha"
        for dt in (
            date(2000, 3, 16),
            date(2001, 3, 5),
            date(2002, 2, 22),
            date(2003, 2, 11),
            date(2004, 2, 1),
            date(2005, 1, 21),
            date(2006, 1, 10),
            date(2006, 12, 31),
            date(2013, 10, 15),
            date(2019, 8, 12),
            date(2020, 7, 31),
            date(2021, 7, 21),
            date(2022, 7, 10),
            date(2023, 6, 28),
        ):
            self.assertHoliday(dt)
            self.assertHoliday(dt + td(days=+1))
            self.assertHoliday(dt + td(days=+2))
            self.assertIn(name, self.holidays.get(dt))

    def test_eid_milad_un_nabi(self):
        name = "Eid Milad-un-Nabi"
        for dt in (
            date(2000, 6, 14),
            date(2001, 6, 4),
            date(2002, 5, 24),
            date(2003, 5, 13),
            date(2004, 5, 1),
            date(2005, 4, 22),
            date(2006, 4, 11),
            date(2013, 1, 24),
            date(2019, 11, 10),
            date(2020, 10, 30),
            date(2021, 10, 19),
            date(2022, 10, 9),
            date(2023, 9, 27),
        ):
            self.assertHoliday(dt)
            self.assertIn(name, self.holidays.get(dt))

    def test_ashura(self):
        name = "Ashura"
        for dt in (
            date(2000, 4, 15),
            date(2001, 4, 4),
            date(2002, 3, 24),
            date(2003, 3, 13),
            date(2004, 3, 1),
            date(2005, 2, 18),
            date(2006, 2, 8),
            date(2009, 1, 6),
            date(2009, 12, 26),
            date(2013, 11, 13),
            date(2019, 9, 9),
            date(2020, 8, 29),
            date(2021, 8, 18),
            date(2022, 8, 9),
            date(2023, 7, 28),
        ):
            self.assertHoliday(dt)
            self.assertHoliday(dt + td(days=+1))
            self.assertIn(name, self.holidays.get(dt))
