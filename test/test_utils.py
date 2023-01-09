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

from unittest import mock

from holidays import utils
from test.common import TestCase


class TestUtils(TestCase):
    @mock.patch("importlib.util.find_spec", return_value=None)
    def test_dependency_hijri_converter(self, find_spec):
        self.assertRaises(
            ImportError, lambda: utils._islamic_to_gre(2022, 10, 1)
        )
