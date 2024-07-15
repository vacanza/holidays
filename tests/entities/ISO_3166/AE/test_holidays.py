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

from holidays.entities.ISO_3166.AE import AeHolidays
from tests.common import CommonCountryTests


class TestAeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AeHolidays, years=range(2014, 2024))

    def test_2020(self):
        self.assertHolidayDates(
            AeHolidays(years=2020),
            "2020-01-01",
            "2020-05-23",
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            "2020-07-30",
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
            "2020-08-23",
            "2020-10-29",
            "2020-12-01",
            "2020-12-02",
            "2020-12-03",
        )

    def test_commemoration_day(self):
        self.assertNoHoliday("2014-11-30")
        self.assertNoHolidayName("يوم الشهيد", 2014, 2023)
        self.assertHoliday(f"{year}-11-30" for year in range(2015, 2019))
        self.assertNoHoliday("2019-11-30")
        self.assertHoliday(f"{year}-12-01" for year in range(2019, 2023))

    def test_hijri_based(self):
        self.assertHoliday(
            # Eid Al-Fitr
            "2018-06-14",
            "2018-06-15",
            "2018-06-16",
            "2020-05-23",
            "2020-05-24",
            "2020-05-25",
            "2020-05-26",
            # Arafat Day & Eid Al-Adha
            "2020-07-30",
            "2020-07-31",
            "2020-08-01",
            "2020-08-02",
            "2023-06-27",
            "2023-06-28",
            "2023-06-29",
            "2023-06-30",
            # Islamic New Year
            "2008-01-10",
            "2008-12-29",
            "2018-09-11",
            "2019-08-31",
            "2020-08-23",
            "2021-08-12",
            "2022-07-30",
            "2023-07-21",
            # Isra' and Mi'raj
            "2018-04-13",
            # Prophet's Birthday
            "2018-11-19",
            "2019-11-09",
            "2020-10-29",
            "2021-10-21",
            "2022-10-08",
            "2023-09-29",
        )
        self.assertNoHoliday("2018-06-13")  # Eid Al-Fitr Eve
        self.assertNoHolidayName("ليلة المعراج", range(2019, 2024))
