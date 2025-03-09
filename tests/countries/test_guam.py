#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from datetime import date
from unittest import TestCase

from holidays.calendars.gregorian import MAR
from holidays.constants import GOVERNMENT, UNOFFICIAL
from holidays.countries.guam import HolidaysGU, GU, GUM
from tests.common import CommonCountryTests


class TestGU(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HolidaysGU)

    def test_country_aliases(self):
        self.assertAliases(HolidaysGU, GU, GUM)

    def test_gu_only(self):
        """Check for a holiday that is not returned by US unless the
        subdivision is specified."""
        self.assertIn("Guam Discovery Day", self.holidays.get_list(date(2016, MAR, 7)))

    def test_unofficial_holidays(self):
        self.assertHolidays(
            HolidaysGU(categories=UNOFFICIAL, years=2024),
            ("2024-02-14", "Valentine's Day"),
            ("2024-03-17", "Saint Patrick's Day"),
            ("2024-10-31", "Halloween"),
        )

    def test_government_holidays(self):
        self.assertHolidays(
            HolidaysGU(categories=GOVERNMENT, years=2024),
            ("2024-01-01", "New Year's Day"),
            ("2024-01-15", "Birthday of Martin Luther King, Jr."),
            ("2024-02-19", "Washington's Birthday"),
            ("2024-05-27", "Memorial Day"),
            ("2024-06-19", "Juneteenth National Independence Day"),
            ("2024-07-04", "Independence Day"),
            ("2024-09-02", "Labor Day"),
            ("2024-10-14", "Columbus Day"),
            ("2024-11-11", "Veterans Day"),
            ("2024-11-28", "Thanksgiving Day"),
            ("2024-12-25", "Christmas Day"),
        )
