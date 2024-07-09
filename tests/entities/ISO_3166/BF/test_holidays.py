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

from holidays.entities.ISO_3166.BF import BfHolidays
from tests.common import CommonCountryTests


class TestBfHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BfHolidays)

    def test_no_holidays(self):
        self.assertNoHolidays(BfHolidays(years=1960))

    def test_revolution_day(self):
        name = "Revolution Day"
        self.assertHolidayName(name, (f"{year}-01-03" for year in range(1967, 2050)))
        self.assertNoHolidayName(name, BfHolidays(years=range(1961, 1967)))
        self.assertNoHoliday(f"{year}-01-03" for year in range(1961, 1967))

    def test_martyrs_day(self):
        name = "Martyrs' Day"
        self.assertHolidayName(name, (f"{year}-10-31" for year in range(2016, 2050)))
        self.assertNoHolidayName(name, BfHolidays(years=range(1961, 2016)))
        self.assertNoHoliday(f"{year}-10-31" for year in set(range(1961, 2016)).difference({1979}))

    def test_observed(self):
        dt = (
            # New Year's Day
            "2012-01-02",
            "2017-01-02",
            "2023-01-02",
            # Revolution Day
            "2010-01-04",
            "2016-01-04",
            "2021-01-04",
            # International Women's Day
            "2015-03-09",
            "2020-03-09",
            # Labour Day
            "2011-05-02",
            "2016-05-02",
            # Independence Day
            "2012-08-06",
            "2018-08-06",
            # Assumption Day
            "2010-08-16",
            "2021-08-16",
            # All Saints' Day
            "2015-11-02",
            "2020-11-02",
            # Proclamation of Independence Day
            "2011-12-12",
            "2022-12-12",
            # Christmas Day
            "2011-12-26",
            "2016-12-26",
            "2022-12-26",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-01-03", "Revolution Day"),
            ("2022-03-08", "International Women's Day"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-02", "Eid al-Fitr; Labour Day (observed)"),
            ("2022-05-26", "Ascension Day"),
            ("2022-07-09", "Eid al-Adha"),
            ("2022-08-05", "Independence Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-10-09", "Mawlid"),
            ("2022-10-31", "Martyrs' Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-11", "Proclamation of Independence Day"),
            ("2022-12-12", "Proclamation of Independence Day (observed)"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Christmas Day (observed)"),
        )
