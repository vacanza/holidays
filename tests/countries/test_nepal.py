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

from holidays.countries.nepal import Nepal, NP, NPL
from tests.common import CommonCountryTests


class TestNepal(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Nepal)

    def test_country_aliases(self):
        self.assertAliases(Nepal, NP, NPL)
