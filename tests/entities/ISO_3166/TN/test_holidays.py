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

from holidays.entities.ISO_3166.TN import TnHolidays
from tests.common import CommonCountryTests


class TestTnHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(TnHolidays)

    def test_2021(self):
        self.assertHolidayDates(
            "2021-01-01",
            "2021-01-14",
            "2021-03-20",
            "2021-04-09",
            "2021-05-01",
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            "2021-07-19",
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            "2021-07-25",
            "2021-08-09",
            "2021-08-13",
            "2021-10-15",
            "2021-10-18",
        )

    def test_hijri_based(self):
        self.assertHoliday(
            # Eid al-Fitr
            "2021-05-13",
            "2021-05-14",
            "2021-05-15",
            # Eid al-Adha
            "2006-01-10",
            "2006-12-31",
            "2021-07-19",
            "2021-07-20",
            "2021-07-21",
            "2021-07-22",
            # Islamic New Year
            "2008-01-10",
            "2008-12-29",
            "2021-08-09",
            # Prophet Muhammad's Birthday
            "2021-10-18",
        )
