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

import unittest

from holidays.calendars.tibetan import _TibetanLunisolar


class TestTibetanLunisolar(unittest.TestCase):
    def setUp(self):
        self.tibetan_calendar = _TibetanLunisolar()

    def test_check_calendar(self):
        self.assertIsInstance(self.tibetan_calendar, _TibetanLunisolar)
