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

from holidays.countries.vanuatu import Vanuatu, VU, VTU
from tests.common import TestCase


class TestVanuatu(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Vanuatu)

    def test_country_aliases(self):
        self.assertCountryAliases(Vanuatu, VU, VTU)

    def test_no_holidays(self):
        self.assertNoHolidays(Vanuatu(years=1980))

    def test_fater_lini_day(self):
        name = "Father Lini Day"
        self.assertHolidayName(name, (f"{year}-02-21" for year in range(1991, 2050)))
        self.assertNoHolidayName(name, Vanuatu(years=range(1981, 1991)))
        self.assertNoHoliday(f"{year}-02-21" for year in range(1981, 1991))

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-01", "New Year's Day"),
            ("2022-02-21", "Father Lini Day"),
            ("2022-03-05", "Custom Chief's Day"),
            ("2022-04-15", "Good Friday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labour Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-07-24", "Children's Day"),
            ("2022-07-30", "Independence Day"),
            ("2022-08-15", "Assumption Day"),
            ("2022-10-05", "Constitution Day"),
            ("2022-11-29", "National Unity Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Family Day"),
        )
