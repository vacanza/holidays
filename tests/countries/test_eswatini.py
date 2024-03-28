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

import warnings
from unittest import TestCase

import holidays
from holidays.countries.eswatini import Eswatini, SZ, SZW
from tests.common import CommonCountryTests


class TestEswatini(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Eswatini, years=range(1939, 2050))

    def test_country_aliases(self):
        self.assertAliases(Eswatini, SZ, SZW)

    def test_no_holidays(self):
        self.assertNoHolidays(Eswatini(years=1938))

    def test_special_holidays(self):
        self.assertHoliday("1999-12-31", "2000-01-03")

    def test_holidays(self):
        for year in range(1939, 2050):
            self.assertHoliday(
                f"{year}-01-01",
                f"{year}-05-01",
                f"{year}-09-06",
                f"{year}-12-25",
                f"{year}-12-26",
            )

    def test_kings_birthday(self):
        self.assertNoHolidayName("King's Birthday", range(1939, 1987))
        self.assertHoliday(f"{year}-04-19" for year in range(1987, 2050))

    def test_national_flag_day(self):
        self.assertNoHoliday(f"{year}-04-25" for year in range(1939, 1969))
        self.assertNoHolidayName("National Flag Day", range(1939, 1969))
        self.assertHoliday(f"{year}-04-25" for year in range(1969, 2050))

    def test_late_king_sobhuza(self):
        self.assertNoHoliday(f"{year}-07-22" for year in range(1939, 1983))
        self.assertNoHolidayName("Birthday of Late King Sobhuza", range(1939, 1983))
        self.assertHoliday(f"{year}-07-22" for year in range(1983, 2050))

    def test_easter(self):
        self.assertHoliday(
            # Good Friday
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            # Easter Monday
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            # Ascension Day
            "2018-05-10",
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
        )

    def test_observed(self):
        dt = (
            # New Year's Day
            "2023-01-02",
            # King's Birthday
            "2026-04-20",
            "2071-04-21",
            "2076-04-21",
            "2082-04-21",
            # National Flag Day
            "2021-04-26",
            "2027-04-26",
            "2038-04-27",
            # Worker's Day
            "2022-05-02",
            # Birthday of Late King Sobhuza
            "2029-07-23",
            # Independence Day
            "2026-09-07",
            # Christmas Day
            "2022-12-27",
            # Boxing Day
            "2021-12-27",
            "2027-12-27",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_swaziland_deprecation_warning(self):
        warnings.simplefilter("default")
        with self.assertWarns(Warning):
            holidays.Swaziland()

        warnings.simplefilter("error")
        with self.assertRaises(Warning):
            holidays.Swaziland()
