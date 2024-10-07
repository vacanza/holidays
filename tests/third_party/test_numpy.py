#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.cambodia import Cambodia
from holidays.countries.thailand import Thailand
from holidays.countries.ukraine import Ukraine


class TestNumpy(TestCase):
    def test_years_int_conversion(self):
        import numpy as np  # It seems the import causes the error mentioned above.

        years = (1995, 2000)
        years_range = set(range(*years))

        for cls in (Cambodia, Thailand, Ukraine):
            # Test single value.
            for int_x in (np.int16, np.int32, np.int64):
                self.assertEqual(cls(years=int_x(2024)).years, {2024})

            # Test iterable.
            self.assertEqual(cls(years=np.arange(*years)).years, years_range)
