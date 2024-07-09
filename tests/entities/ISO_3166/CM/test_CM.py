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

from holidays.entities.ISO_3166.CM import CmHolidays
from tests.common import CommonCountryTests


class TestCmHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CmHolidays, years=range(1960, 2050))

    def test_no_holidays(self):
        self.assertNoHolidays(CmHolidays(years=1959))

    def test_special_holidays(self):
        self.assertHoliday("2021-05-14", "2021-07-19")

    def test_youth_day(self):
        name = "Youth Day"
        self.assertHolidayName(name, (f"{year}-02-11" for year in range(1966, 2050)))
        self.assertNoHolidayName(name, range(1960, 1966))
        self.assertNoHoliday(f"{year}-02-11" for year in range(1960, 1966))

    def test_national_day(self):
        name = "National Day"
        self.assertHolidayName(name, (f"{year}-05-20" for year in range(1972, 2050)))
        self.assertNoHolidayName(name, range(1960, 1972))
        self.assertNoHoliday(f"{year}-05-20" for year in set(range(1960, 1972)).difference({1971}))

    def test_observed(self):
        dt = (
            # New Year's Day
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
            # Youth Day
            "2018-02-12",
            "2024-02-12",
            # Labour Day
            "2016-05-02",
            "2022-05-03",
            # National Day
            "2012-05-21",
            "2018-05-21",
            # Assumption Day
            "2010-08-16",
            "2021-08-16",
            # Christmas Day
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
            # Eid al-Fitr
            "2012-08-20",
            "2020-05-25",
            # Eid al-Adha
            "2007-01-02",  # special case
            "2014-10-06",
            "2019-08-12",
            # Mawlid
            "2012-02-06",
            "2019-11-11",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_2022(self):
        self.assertHolidays(
            CmHolidays(years=2022),
            ("2022-01-01", "New Year's Day"),
            ("2022-02-11", "Youth Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Eid al-Fitr"),
            ("2022-05-03", "Labour Day (observed)"),
            ("2022-05-20", "National Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-08-15", "Assumption Day"),
            ("2022-10-08", "Mawlid"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )
