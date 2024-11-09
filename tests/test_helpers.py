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

from holidays.helpers import _normalize_arguments, _normalize_tuple


class TestHelpers(TestCase):
    def test_normalize_arguments(self):
        empty_set = set()
        input_expected_pairs = (
            ((int, []), empty_set),
            ((int, {}), empty_set),
            ((int, None), empty_set),
            ((str, []), empty_set),
            ((str, {}), empty_set),
            ((str, None), empty_set),
            ((int, "1"), {1}),
            ((int, "12"), {12}),
            ((int, "121"), {121}),
            ((int, ["1", "1"]), {1}),
            ((int, ["1", "2"]), {1, 2}),
            ((int, [1, 1]), {1}),
            ((int, [1, 2]), {1, 2}),
            ((int, [1]), {1}),
            ((int, {1}), {1}),
            ((int, 0), {0}),
            ((int, 1.0), {1.0}),
            ((int, 1), {1}),
            ((str, "1"), {"1"}),
            ((str, ("test1", "TEST1")), {"test1", "TEST1"}),
            ((str, ("test1", "test1")), {"test1"}),
            ((str, ("test1", "test2")), {"test1", "test2"}),
            ((str, ["1", "2"]), {"1", "2"}),
            ((str, [1, 2]), {"1", "2"}),
            ((str, [1]), {"1"}),
            ((str, {1: "2"}), {"1"}),
            ((str, {1: 2}), {"1"}),
            ((str, {1}), {"1"}),
            ((str, 1.0), {"1.0"}),
            ((str, 1), {"1"}),
        )

        for input, expected in input_expected_pairs:
            self.assertEqual(_normalize_arguments(*input), expected)

    def test_normalize_tuple(self):
        input_expected_pairs = (
            ((), ()),
            ((1,), ((1,),)),
            ((1, 2), ((1, 2),)),
            (((1, 1), (2, 2)), ((1, 1), (2, 2))),
        )
        for input, expected in input_expected_pairs:
            self.assertEqual(_normalize_tuple(input), expected)
