#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.jamaica import Jamaica, JM, JAM
from tests.common import CommonCountryTests


class TestJamaica(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Jamaica, years=range(1950, 2050))

    def test_country_aliases(self):
        self.assertAliases(Jamaica, JM, JAM)

    def test_new_years_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1950, 2050))
        dt = (
            "1995-01-02",
            "2006-01-02",
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_labour_day(self):
        self.assertHoliday(f"{year}-05-23" for year in range(1950, 2050))
        dt = (
            "1998-05-25",
            "1999-05-24",
            "2004-05-24",
            "2009-05-25",
            "2010-05-24",
            "2015-05-25",
            "2020-05-25",
            "2021-05-24",
            "2026-05-25",
            "2027-05-24",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_emancipation_day(self):
        self.assertHoliday(f"{year}-08-01" for year in range(1998, 2050))
        dt = (
            "1999-08-02",
            "2004-08-02",
            "2010-08-02",
            "2021-08-02",
            "2027-08-02",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)
        self.assertNoHolidayName("Emancipation Day", 1997)

    def test_independence_day(self):
        self.assertHoliday(f"{year}-08-06" for year in range(1950, 2050))
        dt = (
            "2000-08-07",
            "2006-08-07",
            "2017-08-07",
            "2023-08-07",
            "2028-08-07",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_national_heroes_day(self):
        self.assertHoliday(
            "2015-10-19",
            "2016-10-17",
            "2017-10-16",
            "2018-10-15",
            "2019-10-21",
            "2020-10-19",
            "2021-10-18",
            "2022-10-17",
            "2023-10-16",
            "2024-10-21",
        )

    def test_christmas_day(self):
        self.assertHoliday(f"{year}-12-25" for year in range(1950, 2050))
        dt = (
            "2005-12-27",
            "2011-12-27",
            "2016-12-27",
            "2022-12-27",
            "2033-12-27",
        )
        self.assertHolidayName("Christmas Day (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_boxing_day(self):
        self.assertHoliday(f"{year}-12-26" for year in range(1950, 2050))
        dt = (
            "2004-12-27",
            "2010-12-27",
            "2021-12-27",
            "2027-12-27",
            "2032-12-27",
        )
        self.assertHolidayName("Boxing Day (observed)", dt)
        self.assertNoNonObservedHoliday(dt)

    def test_ash_wednesday(self):
        self.assertHoliday(
            "2015-02-18",
            "2016-02-10",
            "2017-03-01",
            "2018-02-14",
            "2019-03-06",
            "2020-02-26",
            "2021-02-17",
            "2022-03-02",
            "2023-02-22",
            "2024-02-14",
        )

    def test_good_friday(self):
        self.assertHoliday(
            "2015-04-03",
            "2016-03-25",
            "2017-04-14",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
        )

    def test_easter_monday(self):
        self.assertHoliday(
            "2015-04-06",
            "2016-03-28",
            "2017-04-17",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
        )
