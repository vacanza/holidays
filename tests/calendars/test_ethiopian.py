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

import unittest

from holidays.calendars.ethiopian import is_ethiopian_leap_year


class TestEthiopianCalendar(unittest.TestCase):
    def test_is_ethiopian_leap_year(self):
        known_ethiopian_leap_years = {
            # Known Cases.
            2022: False,
            2023: True,
            2024: False,
            2025: False,
            # Future Cases.
            2098: False,
            2099: True,
            2100: False,
            2101: False,
            2198: False,
            2199: True,
            2200: False,
            2201: False,
        }
        for year in known_ethiopian_leap_years:
            self.assertEqual(known_ethiopian_leap_years[year], is_ethiopian_leap_year(year))
