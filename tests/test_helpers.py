#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

import unittest
from datetime import date, datetime

from holidays.helpers import _convert_to_date


class TestConvertToDate(unittest.TestCase):
    def test_date(self):
        dt = date(2014, 1, 1)
        self.assertEqual(_convert_to_date(dt), dt)

    def test_date_subclass(self):
        class CustomDateType(date):
            pass

        self.assertEqual(CustomDateType(2014, 1, 1), date(2014, 1, 1))

    def test_datetime(self):
        self.assertEqual(_convert_to_date(datetime(2014, 1, 1, 13, 45)), date(2014, 1, 1))

    def test_exception(self):
        self.assertRaises((TypeError, ValueError), lambda: _convert_to_date("invalid string"))
        self.assertRaises((TypeError, ValueError), lambda: _convert_to_date("abc123"))
        self.assertRaises(TypeError, lambda: _convert_to_date({"123"}))
        self.assertRaises((TypeError, ValueError), lambda: _convert_to_date([]))

    def test_string(self):
        self.assertEqual(_convert_to_date("2014-01-03"), date(2014, 1, 3))
        self.assertEqual(_convert_to_date("01/03/2014"), date(2014, 1, 3))

    def test_timestamp(self):
        self.assertEqual(_convert_to_date(1388552400), date(2014, 1, 1))
        self.assertEqual(_convert_to_date(1388552400.01), date(2014, 1, 1))
