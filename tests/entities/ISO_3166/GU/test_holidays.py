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

from datetime import date
from unittest import TestCase

from holidays.calendars.gregorian import MAR
from holidays.constants import UNOFFICIAL
from holidays.entities.ISO_3166.GU import GuHolidays
from tests.common import CommonCountryTests


class TestGU(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(GuHolidays)

    def test_gu_only(self):
        """Check for a holiday that is not returned by US unless the
        subdivision is specified."""
        self.assertIn("Guam Discovery Day", self.holidays.get_list(date(2016, MAR, 7)))

    def test_unofficial_holidays(self):
        self.assertHolidays(
            GuHolidays(categories=UNOFFICIAL, years=2024),
            ("2024-02-14", "Valentine's Day"),
            ("2024-03-17", "St. Patrick's Day"),
            ("2024-10-31", "Halloween"),
        )
