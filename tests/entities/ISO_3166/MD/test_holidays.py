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

from holidays.entities.ISO_3166.MD import MdHolidays
from tests.common import CommonCountryTests


class TestMdHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MdHolidays)

    def test_no_holidays(self):
        self.assertNoHolidays(MdHolidays(years=1990))

    def test_christmas(self):
        name_old1 = "Nașterea lui Iisus Hristos (Crăciunul)"
        name_old2 = "Nașterea lui Iisus Hristos (Crăciunul pe stil vechi)"
        name_new = "Nașterea lui Iisus Hristos (Crăciunul pe stil nou)"
        self.assertHolidayName(name_old1, (f"{year}-01-07" for year in range(1991, 2014)))
        self.assertNoHolidayName(name_old1, MdHolidays(years=2014))
        self.assertHolidayName(name_old2, (f"{year}-01-07" for year in range(2014, 2031)))
        self.assertNoHolidayName(name_old2, MdHolidays(years=2013))

        self.assertHolidayName(name_new, (f"{year}-12-25" for year in range(2013, 2031)))
        self.assertNoHolidayName(name_new, MdHolidays(years=2012))

    def test_europe_day(self):
        name = "Ziua Europei"
        self.assertHolidayName(name, (f"{year}-05-09" for year in range(2017, 2031)))
        self.assertNoHolidayName(name, MdHolidays(years=2016))

    def test_childrens_day(self):
        name = "Ziua Ocrotirii Copilului"
        self.assertHolidayName(name, (f"{year}-06-01" for year in range(2016, 2031)))
        self.assertNoHolidayName(name, MdHolidays(years=2015))

    def test_2022(self):
        self.assertHolidayDates(
            MdHolidays(years=2022),
            "2022-01-01",
            "2022-01-07",
            "2022-01-08",
            "2022-03-08",
            "2022-04-24",
            "2022-04-25",
            "2022-05-01",
            "2022-05-02",
            "2022-05-09",
            "2022-06-01",
            "2022-08-27",
            "2022-08-31",
            "2022-12-25",
        )

    def test_2023(self):
        self.assertHolidayDates(
            MdHolidays(years=2023),
            "2023-01-01",
            "2023-01-07",
            "2023-01-08",
            "2023-03-08",
            "2023-04-16",
            "2023-04-17",
            "2023-04-24",
            "2023-05-01",
            "2023-05-09",
            "2023-06-01",
            "2023-08-27",
            "2023-08-31",
            "2023-12-25",
        )
