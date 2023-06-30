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
from holidays.countries.northern_mariana_islands import HolidaysMP, MP, MNP
from tests.common import TestCase


class TestMP(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HolidaysMP)

    def test_country_aliases(self):
        self.assertCountryAliases(HolidaysMP, MP, MNP)

    def test_mp_only(self):
        """Check for a holiday that is not returned by US unless the
        subdivision is specified."""
        self.assertIn("Commonwealth Covenant Day", self.holidays.get_list(date(2022, MAR, 24)))
