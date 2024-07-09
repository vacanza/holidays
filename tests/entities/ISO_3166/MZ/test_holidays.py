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

from holidays.entities.ISO_3166.MZ import MzHolidays
from tests.common import CommonCountryTests


class TestMzHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MzHolidays, years=range(1975, 2050))

    def test_no_holidays(self):
        self.assertNoHolidays(MzHolidays(years=1974))

    def test_holidays(self):
        for year in range(1975, 2050):
            self.assertHoliday(
                f"{year}-01-01",
                f"{year}-02-03",
                f"{year}-04-07",
                f"{year}-05-01",
                f"{year}-06-25",
                f"{year}-09-07",
                f"{year}-09-25",
                f"{year}-12-25",
            )

        self.assertNoHoliday(f"{year}-10-04" for year in range(1975, 1993))
        self.assertNoHolidayName("Dia da Paz e Reconciliação", range(1975, 1993))
        self.assertHoliday(f"{year}-10-04" for year in range(1993, 2050))

    def test_observed(self):
        dt = (
            "2011-05-02",
            "2011-09-26",
            "2011-12-26",
            "2012-01-02",
            "2013-02-04",
            "2013-04-08",
            "2014-09-08",
            "2015-10-05",
            "2016-05-02",
            "2016-09-26",
            "2016-12-26",
            "2017-01-02",
            "2017-06-26",
            "2019-02-04",
            "2019-04-08",
            "2020-10-05",
            "2022-05-02",
            "2022-09-26",
            "2022-12-26",
            "2023-01-02",
            "2023-06-26",
        )
        self.assertHoliday(dt)
        self.assertNoNonObservedHoliday(dt)
