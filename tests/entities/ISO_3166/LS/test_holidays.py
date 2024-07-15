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

from holidays.entities.ISO_3166.LS import LsHolidays
from tests.common import CommonCountryTests


class TestLsHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(LsHolidays, years=range(1996, 2040))

    def test_no_holidays(self):
        self.assertNoHolidays(LsHolidays(years=1995))

    def test_special_holidays(self):
        self.assertHoliday("2002-05-25")

    def test_heroes_day(self):
        name = "Heroes Day"
        self.assertHolidayName(name, (f"{year}-04-04" for year in range(1996, 2003)))
        self.assertNoHolidayName(name, range(2003, 2040))
        self.assertNoHoliday(f"{year}-04-04" for year in range(2003, 2040))

    def test_africa_heroes_day(self):
        name = "Africa/Heroes Day"
        self.assertHolidayName(name, (f"{year}-05-25" for year in range(2003, 2040)))
        self.assertNoHolidayName(name, range(1996, 2003))
        self.assertNoHoliday(f"{year}-05-25" for year in range(1996, 2002))

    def test_kings_birthday(self):
        name = "King's Birthday"
        self.assertHolidayName(name, (f"{year}-05-02" for year in range(1996, 1998)))
        self.assertHolidayName(name, (f"{year}-07-17" for year in range(1998, 2040)))
        self.assertNoHoliday(f"{year}-05-02" for year in range(1998, 2040))
        self.assertNoHoliday(f"{year}-07-17" for year in range(1996, 1998))

    def test_2022(self):
        self.assertHolidays(
            LsHolidays(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-03-11", "Moshoeshoe's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Workers' Day"),
            ("2022-05-25", "Africa/Heroes Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-07-17", "King's Birthday"),
            ("2022-10-04", "Independence Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Boxing Day"),
        )
