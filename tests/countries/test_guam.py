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

from datetime import date

from holidays.calendars.gregorian import MAR
from holidays.countries.guam import HolidaysGU, GU, GUM
from tests.common import TestCase


class TestGU(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HolidaysGU)

    def test_country_aliases(self):
        self.assertCountryAliases(HolidaysGU, GU, GUM)

    def test_gu_only(self):
        """Check for a holiday that is not returned by US unless the
        subdivision is specified."""
        self.assertIn("Guam Discovery Day", self.holidays.get_list(date(2016, MAR, 7)))
