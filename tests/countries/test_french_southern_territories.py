#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.french_southern_territories import (
    HolidaysTF,
    FrenchSouthernTerritories,
    TF,
    ATF,
)
from tests.common import CommonCountryTests


class TestTF(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(HolidaysTF)

    def test_country_aliases(self):
        self.assertAliases(HolidaysTF, FrenchSouthernTerritories, TF, ATF)

    def test_2022(self):
        self.assertHolidayDates(
            HolidaysTF(years=2022),
            "2022-01-01",
            "2022-04-18",
            "2022-05-01",
            "2022-05-08",
            "2022-05-26",
            "2022-06-06",
            "2022-07-14",
            "2022-08-15",
            "2022-11-01",
            "2022-11-11",
            "2022-12-25",
        )
