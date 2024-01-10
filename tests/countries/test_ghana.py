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

from holidays.countries.ghana import Ghana, GH, GHA
from tests.common import TestCase


class TestGhana(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Ghana, years=range(1957, 2050))

    def test_country_aliases(self):
        self.assertCountryAliases(Ghana, GH, GHA)

    def test_no_holidays(self):
        self.assertNoHolidays(Ghana(years=1956))

    def test_new_year_day(self):
        self.assertHoliday(f"{year}-01-01" for year in range(1957, 2050))
