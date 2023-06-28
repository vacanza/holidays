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

from holidays.countries.ireland import Ireland, IE, IRL
from tests.common import TestCase


class TestIreland(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Ireland, years=range(1950, 2050))

    def test_country_aliases(self):
        self.assertCountryAliases(Ireland, IE, IRL)

    def test_special_holidays(self):
        self.assertHoliday("2022-03-18")

    def test_new_years_day(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(1950, 2050)))

    def test_st_brigids_day(self):
        name = "St. Brigid's Day"
        self.assertHolidayName(
            name,
            "2023-02-06",
            "2024-02-05",
            "2025-02-03",
            "2026-02-02",
            "2027-02-01",
            "2028-02-07",
            "2029-02-05",
            "2030-02-01",
            "2031-02-03",
            "2032-02-02",
        )
        self.assertNoHolidayName(name, range(1950, 2023))

    def test_st_patricks_day(self):
        self.assertHolidayName(
            "St. Patrick's Day", (f"{year}-03-17" for year in range(1950, 2050))
        )
        obs_dt = (
            "2001-03-19",
            "2002-03-18",
            "2007-03-19",
            "2012-03-19",
            "2013-03-18",
            "2018-03-19",
            "2019-03-18",
        )
        self.assertHoliday(obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_easter_monday(self):
        self.assertHolidayName(
            "Easter Monday",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
        )

    def test_may_day(self):
        name = "May Day"
        self.assertHolidayName(
            name,
            "1978-05-01",
            "1979-05-07",
            "1980-05-05",
            "1995-05-08",
            "1999-05-03",
            "2000-05-01",
            "2010-05-03",
            "2018-05-07",
            "2019-05-06",
            "2020-05-04",
        )
        self.assertNoHolidayName(name, range(1950, 1978))

    def test_june_bank_holiday(self):
        self.assertHolidayName(
            "June Bank Holiday",
            "2019-06-03",
            "2020-06-01",
            "2021-06-07",
            "2022-06-06",
            "2023-06-05",
        )

    def test_august_bank_holiday(self):
        self.assertHolidayName(
            "August Bank Holiday",
            "2019-08-05",
            "2020-08-03",
            "2021-08-02",
            "2022-08-01",
            "2023-08-07",
        )

    def test_october_bank_holiday(self):
        self.assertHolidayName(
            "October Bank Holiday",
            "2019-10-28",
            "2020-10-26",
            "2021-10-25",
            "2022-10-31",
            "2023-10-30",
        )

    def test_christmas_day(self):
        name = "Christmas Day"
        self.assertHolidayName(name, (f"{year}-12-25" for year in range(1950, 2050)))
        obs_dt = (
            "1993-12-27",
            "1999-12-27",
            "2004-12-27",
            "2010-12-27",
            "2021-12-27",
        )
        self.assertHoliday(obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)
        self.assertHolidayName(
            f"{name} (Observed)",
            "1994-12-26",
            "2005-12-26",
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
        )

    def test_st_stephens_day(self):
        name = "St. Stephen's Day"
        self.assertHolidayName(name, (f"{year}-12-26" for year in range(1950, 2050)))
        obs_dt = (
            "2004-12-28",
            "2009-12-28",
            "2010-12-28",
            "2015-12-28",
            "2020-12-28",
        )
        self.assertHoliday(obs_dt)
        self.assertNoNonObservedHoliday(obs_dt)

    def test_2020(self):
        self.assertHolidays(
            Ireland(years=2020),
            ("2020-01-01", "New Year's Day"),
            ("2020-03-17", "St. Patrick's Day"),
            ("2020-04-13", "Easter Monday"),
            ("2020-05-04", "May Day"),
            ("2020-06-01", "June Bank Holiday"),
            ("2020-08-03", "August Bank Holiday"),
            ("2020-10-26", "October Bank Holiday"),
            ("2020-12-25", "Christmas Day"),
            ("2020-12-26", "St. Stephen's Day"),
            ("2020-12-28", "St. Stephen's Day (Observed)"),
        )

    def test_2022(self):
        self.assertHolidays(
            Ireland(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-03-17", "St. Patrick's Day"),
            ("2022-03-18", "Day of Remembrance and Recognition"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-02", "May Day"),
            ("2022-06-06", "June Bank Holiday"),
            ("2022-08-01", "August Bank Holiday"),
            ("2022-10-31", "October Bank Holiday"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (Observed); St. Stephen's Day"),
        )
