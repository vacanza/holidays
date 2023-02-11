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

from holidays.countries.georgia import GE, GEO, Georgia
from tests.common import TestCase


class TestGeorgia(TestCase):
    def setUp(self):
        self.holidays = Georgia()

    def test_country_aliases(self):
        self.assertCountryAliases(Georgia, GE, GEO)

    def test_easter(self):
        self.assertHoliday(
            "2020-04-19",
            "2019-04-28",
            "2018-04-08",
        )

    def test_2020(self):
        # https://en.wikipedia.org/wiki/Public_holidays_in_Georgia_(country)
        self.assertHoliday(
            "2020-01-01",
            "2020-01-02",
            "2020-01-07",
            "2020-01-19",
            "2020-03-03",
            "2020-03-08",
            "2020-04-09",
            "2020-05-09",
            "2020-05-12",
            "2020-05-26",
            "2020-08-28",
            "2020-10-14",
            "2020-11,-23",
        )

    def test_not_holiday(self):
        self.assertNoHoliday(
            "2020-08-16",
            "2008-08-05",
        )
