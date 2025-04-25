#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.constants import GOVERNMENT, UNOFFICIAL
from holidays.countries.american_samoa import HolidaysAS, AS, ASM
from tests.common import CommonCountryTests


class TestAS(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HolidaysAS)

    def test_country_aliases(self):
        self.assertAliases(HolidaysAS, AS, ASM)

    def test_as_only(self):
        """Check for a holiday that is not returned by US unless the subdivision is specified."""
        self.assertHolidayName("American Samoa Flag Day", "2024-04-17")
        self.assertHolidayName("Manu'a Islands Cession Day", "2024-07-16")
        self.assertHolidayName("White Sunday", "2024-10-13")

    def test_unofficial_holidays(self):
        self.assertHolidays(
            HolidaysAS(categories=UNOFFICIAL, years=2024),
            ("2024-02-14", "Valentine's Day"),
            ("2024-03-17", "Saint Patrick's Day"),
            ("2024-10-31", "Halloween"),
        )

    def test_government_holidays(self):
        self.assertHolidays(
            HolidaysAS(categories=GOVERNMENT, years=2024),
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
