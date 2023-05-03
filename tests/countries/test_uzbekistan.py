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

from holidays.countries.uzbekistan import Uzbekistan, UZ, UZB
from tests.common import TestCase


class TestUzbekistan(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Uzbekistan)

    def test_country_aliases(self):
        self.assertCountryAliases(Uzbekistan, UZ, UZB)

    def test2020(self):
        self.assertHolidays(
            Uzbekistan(years=2022),
            ("2022-01-01", "New Year"),
            ("2022-03-08", "Women's Day"),
            ("2022-03-21", "Nauryz"),
            ("2022-05-02", "Ramadan Khait* (*estimated)"),
            ("2022-05-09", "Memorial Day"),
            ("2022-07-09", "Kurban Khait* (*estimated)"),
            ("2022-09-01", "Independence Day"),
            ("2022-10-01", "Teacher's Day"),
            ("2022-12-08", "Constitution Day"),
        )
