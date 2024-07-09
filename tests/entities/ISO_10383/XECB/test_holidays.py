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

from holidays.entities.ISO_10383.XECB import XecbHolidays
from tests.common import CommonFinancialTests


class TestXECbHolidays(CommonFinancialTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(XecbHolidays, years=range(2000, 2100))

    def test_no_holidays(self):
        self.assertNoHolidays(XecbHolidays(years=1999))

    def test_special_holidays(self):
        self.assertHoliday("2000-12-31")

    def test_new_years(self):
        self.assertHolidayName("New Year's Day", (f"{year}-01-01" for year in range(2000, 2100)))

    def test_good_friday(self):
        dt = (
            "2000-04-21",
            "2010-04-02",
            "2018-03-30",
            "2019-04-19",
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
        )
        self.assertHolidayName("Good Friday", dt)

    def test_easter_monday(self):
        dt = (
            "2000-04-24",
            "2010-04-05",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
        )
        self.assertHolidayName("Easter Monday", dt)

    def test_labour_day(self):
        self.assertHolidayName(
            "1 May (Labour Day)", (f"{year}-05-01" for year in range(2000, 2100))
        )

    def test_christmas_day(self):
        self.assertHolidayName("Christmas Day", (f"{year}-12-25" for year in range(2000, 2100)))

    def test_26_december_day(self):
        self.assertHolidayName("26 December", (f"{year}-12-26" for year in range(2000, 2100)))

    def test_2015(self):
        self.assertHolidays(
            XecbHolidays(years=2015),
            ("2015-01-01", "New Year's Day"),
            ("2015-04-03", "Good Friday"),
            ("2015-04-06", "Easter Monday"),
            ("2015-05-01", "1 May (Labour Day)"),
            ("2015-12-25", "Christmas Day"),
            ("2015-12-26", "26 December"),
        )
