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

import unittest

import holidays


class TestIM(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.IsleOfMan()

    def test_some_2018(self):
        self.assertIn("2018-06-01", self.holidays)
        self.assertIn("2018-07-05", self.holidays)

    def test_2022(self):
        self.assertIn("2022-01-01", self.holidays)  # New Year's Day
        self.assertIn("2022-01-03", self.holidays)  # New Year's Day (Observed)
        self.assertIn("2022-04-15", self.holidays)  # Easter Monday
        self.assertIn("2022-04-18", self.holidays)  # Easter Monday
        self.assertIn("2022-05-02", self.holidays)  # May Day
        self.assertIn("2022-06-02", self.holidays)  # Spring Bank Holiday
        self.assertIn("2022-06-03", self.holidays)  # TT Bank Holiday
        self.assertIn("2022-07-05", self.holidays)  # Tynwald Day
        self.assertIn("2022-08-29", self.holidays)  # Late Summer Bank Holiday
        self.assertIn("2022-12-25", self.holidays)  # Christmas Day
        self.assertIn("2022-12-26", self.holidays)  # Boxing Day
        self.assertIn("2022-12-27", self.holidays)  # Boxing Day (Observed)
