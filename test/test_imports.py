#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import holidays
from test.common import TestCase


class TestHolidaysImports(TestCase):
    def assertImport(self, name):
        self.assertTrue(
            hasattr(holidays, name),
            f"Import error: `from holidays import {name}`",
        )

    def test_constants(self):
        for name in (
            "MON",
            "TUE",
            "WED",
            "THU",
            "FRI",
            "SAT",
            "SUN",
            "WEEKEND",
        ):
            self.assertImport(name)

    def test_holidays_base(self):
        for name in ("DateLike", "HolidayBase", "HolidaySum"):
            self.assertImport(name)

    def test_utils(self):
        for name in (
            "CountryHoliday",
            "country_holidays",
            "financial_holidays",
            "list_supported_countries",
            "list_supported_financial",
        ):
            self.assertImport(name)
