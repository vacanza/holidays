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

from datetime import date
from unittest import TestCase

from holidays.calendars.gregorian import _timedelta
from holidays.entities.ISO_3166.PK import PkHolidays
from tests.common import CommonCountryTests


class TestPkHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(PkHolidays, years=range(1948, 2050))

    def test_no_holidays(self):
        self.assertNoHolidays(PkHolidays(years=1947))

    def test_kashmir_day(self):
        name = "Kashmir Solidarity Day"
        self.assertHolidayName(name, (f"{year}-02-05" for year in range(1990, 2050)))
        self.assertNoHolidayName(name, range(1948, 1990))

    def test_pakistan_day(self):
        name = "Pakistan Day"
        self.assertHolidayName(name, (f"{year}-03-23" for year in range(1956, 2050)))
        self.assertNoHolidayName(name, range(1948, 1956))

    def test_labour_day(self):
        name = "Labour Day"
        self.assertHolidayName(name, (f"{year}-05-01" for year in range(1972, 2050)))
        self.assertNoHolidayName(name, range(1948, 1972))

    def test_independence_day(self):
        self.assertHolidayName("Independence Day", (f"{year}-08-14" for year in range(1948, 2050)))

    def test_iqbal_day(self):
        name = "Iqbal Day"
        self.assertHolidayName(name, (f"{year}-11-09" for year in range(1948, 2015)))
        self.assertHolidayName(name, (f"{year}-11-09" for year in range(2022, 2050)))
        self.assertNoHolidayName(name, range(2015, 2022))

    def test_quaid_e_azam_day(self):
        self.assertHolidayName("Quaid-e-Azam Day", (f"{year}-12-25" for year in range(1948, 2050)))

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
            date(2023, 4, 22),
        ):
            self.assertHoliday(dt)
            self.assertHoliday(_timedelta(dt, +1))
            self.assertHoliday(_timedelta(dt, +2))
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
            date(2023, 6, 29),
        ):
            self.assertHoliday(dt)
            self.assertHoliday(_timedelta(dt, +1))
            self.assertHoliday(_timedelta(dt, +2))
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
            self.assertHoliday(_timedelta(dt, -1))
            self.assertIn(name, self.holidays.get(dt))

    def test_2002(self):
        self.assertHolidays(
            PkHolidays(years=2002),
            ("2002-02-05", "Kashmir Solidarity Day"),
            ("2002-02-22", "Eid-ul-Adha (estimated)"),
            ("2002-02-23", "Eid-ul-Adha (estimated)"),
            ("2002-02-24", "Eid-ul-Adha (estimated)"),
            ("2002-03-23", "Ashura (estimated); Pakistan Day"),
            ("2002-03-24", "Ashura (estimated)"),
            ("2002-05-01", "Labour Day"),
            ("2002-05-24", "Eid Milad-un-Nabi (estimated)"),
            ("2002-08-14", "Independence Day"),
            ("2002-11-09", "Iqbal Day"),
            ("2002-12-05", "Eid-ul-Fitr (estimated)"),
            ("2002-12-06", "Eid-ul-Fitr (estimated)"),
            ("2002-12-07", "Eid-ul-Fitr (estimated)"),
            ("2002-12-25", "Quaid-e-Azam Day"),
        )

    def test_2022(self):
        self.assertHolidays(
            PkHolidays(years=2022),
            ("2022-02-05", "Kashmir Solidarity Day"),
            ("2022-03-23", "Pakistan Day"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-03", "Eid-ul-Fitr"),
            ("2022-05-04", "Eid-ul-Fitr"),
            ("2022-05-05", "Eid-ul-Fitr"),
            ("2022-07-10", "Eid-ul-Adha"),
            ("2022-07-11", "Eid-ul-Adha"),
            ("2022-07-12", "Eid-ul-Adha"),
            ("2022-08-08", "Ashura"),
            ("2022-08-09", "Ashura"),
            ("2022-08-14", "Independence Day"),
            ("2022-10-09", "Eid Milad-un-Nabi"),
            ("2022-11-09", "Iqbal Day"),
            ("2022-12-25", "Quaid-e-Azam Day"),
        )
