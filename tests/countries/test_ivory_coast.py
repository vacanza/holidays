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

#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS.md file)

from unittest import TestCase

from holidays.countries import IvoryCoast, CI, CIV
from tests.common import CommonCountryTests


class TestIvoryCoast(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(IvoryCoast)

    def test_country_aliases(self):
        self.assertAliases(IvoryCoast, CI, CIV)

    def test_2025(self):
        self.assertHolidayDates(
            IvoryCoast(years=2025),
            "2025-01-01",
            # todo: uncomment after adding 'Day After Laila tou-Kadr'
            # "2025-03-27",
            "2025-03-30",
            "2025-04-21",
            "2025-05-01",
            "2025-05-29",
            "2025-06-06",
            "2025-06-09",
            "2025-08-07",
            "2025-08-15",
            "2025-09-04",
            "2025-11-01",
            "2025-11-15",
            "2025-12-25",
        )
