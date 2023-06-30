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

from holidays.calendars.gregorian import DEC
from holidays.countries.american_samoa import HolidaysAS, AS, ASM
from tests.common import TestCase


class TestAS(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HolidaysAS)

    def test_country_aliases(self):
        self.assertCountryAliases(HolidaysAS, AS, ASM)

    def test_as_only(self):
        """Check for a holiday that is not returned by US unless the
        subdivision is specified."""
        self.assertIn("Christmas Eve (Observed)", self.holidays.get_list(date(2017, DEC, 22)))
