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

from holidays.countries.british_indian_ocean_territory import BritishIndianOceanTerritory, IO, IOT
from tests.common import CommonCountryTests


class TestBritishIndianOceanTerritory(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full_range = range(1900, 2050)
        super().setUpClass(BritishIndianOceanTerritory, years=cls.full_range)

    def test_country_aliases(self):
        self.assertAliases(BritishIndianOceanTerritory, IO, IOT)

    def test_no_holidays(self):
        self.assertNoHolidays(BritishIndianOceanTerritory(years=self.full_range))
