#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date

import holidays as hd


class TestIndonesia(unittest.TestCase):
    def setUp(self):
        self.holidays = hd.Indonesia(years=[2020, 2021, 2022])

    def test_holidays(self):
        # Following dates are taken from https://www.officeholidays.com/
        holidays = [
            (2019, 1, 1),
            (2019, 2, 5),
            (2019, 3, 7),
            (2019, 4, 3),
            (2019, 4, 17),
            (2019, 4, 19),
            (2019, 5, 1),
            (2019, 5, 19),
            (2019, 5, 30),
            (2019, 6, 1),
            (2019, 6, 3),  # Joint holiday
            (2019, 6, 4),  # Joint holiday
            (2019, 6, 5),
            (2019, 6, 6),
            (2019, 6, 7),  # Joint holiday
            (2019, 8, 11),
            (2019, 8, 17),
            (2019, 9, 1),
            (2019, 11, 9),
            (2019, 12, 24),  # Joint holiday
            (2019, 12, 25),
            (2020, 1, 1),
            (2020, 1, 25),
            (2020, 3, 22),
            (2020, 3, 25),
            (2020, 4, 10),
            (2020, 5, 1),
            (2020, 5, 7),
            (2020, 5, 21),
            (2020, 5, 22),  # Joint holiday
            (2020, 5, 24),
            (2020, 5, 25),
            (2020, 6, 1),
            (2020, 7, 31),
            (2020, 8, 17),
            (2020, 8, 20),
            (2020, 8, 21),  # Joint holiday
            (2020, 10, 28),  # Joint holiday
            (2020, 10, 29),
            (2020, 10, 30),  # Joint holiday
            (2020, 12, 9),
            (2020, 12, 24),  # Joint holiday
            (2020, 12, 25),
            (2020, 12, 31),  # Joint holiday
            (2021, 1, 1),
            (2021, 2, 12),
            (2021, 3, 11),
            (2021, 3, 14),
            (2021, 4, 2),
            (2021, 5, 1),
            (2021, 5, 12),
            (2021, 5, 13),
            (2021, 5, 14),
            (2021, 5, 26),
            (2021, 6, 1),
            (2021, 7, 20),
            (2021, 8, 11),
            (2021, 8, 17),
            (2021, 10, 20),
            (2021, 12, 25),
            (2022, 1, 1),
            (2022, 2, 1),
            (2022, 2, 28),
            (2022, 3, 3),
            (2022, 4, 15),
            (2022, 4, 29),  # Joint holiday
            (2022, 5, 1),
            (2022, 5, 2),
            (2022, 5, 3),
            (2022, 5, 4),  # Joint holiday
            (2022, 5, 5),  # Joint holiday
            (2022, 5, 6),  # Joint holiday
            (2022, 5, 16),
            (2022, 5, 26),
            (2022, 6, 1),
            (2022, 7, 10),
            (2022, 7, 30),
            (2022, 8, 17),
            (2022, 10, 8),
            (2022, 12, 25),
        ]
        # self.assertEqual(len(holidays), len(self.holidays))
        for dt in holidays:
            self.assertIn(date(*dt), self.holidays)
