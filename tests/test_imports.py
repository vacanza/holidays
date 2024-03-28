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

import holidays


class TestHolidaysImports(TestCase):
    def assertImport(self, name):
        self.assertTrue(hasattr(holidays, name), f"Import error: `from holidays import {name}`")

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
            "country_holidays",
            "CountryHoliday",
            "financial_holidays",
            "list_localized_countries",
            "list_localized_financial",
            "list_supported_countries",
            "list_supported_financial",
        ):
            self.assertImport(name)
