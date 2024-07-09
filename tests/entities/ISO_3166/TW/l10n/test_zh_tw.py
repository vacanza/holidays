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

from unittest import TestCase

from holidays.entities.ISO_3166.TW import TwHolidays
from tests.common import CommonCountryTests


class TestTwHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(TwHolidays)

    def test_zh_tw(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "中華民國開國紀念日"),
            ("2022-01-31", "農曆除夕"),
            ("2022-02-01", "春節"),
            ("2022-02-02", "春節"),
            ("2022-02-03", "春節"),
            ("2022-02-04", "休息日（2022-01-22日起取代）"),
            ("2022-02-28", "和平紀念日"),
            ("2022-04-04", "兒童節"),
            ("2022-04-05", "清明節"),
            ("2022-06-03", "端午節"),
            ("2022-09-09", "中秋節（慶祝）"),
            ("2022-09-10", "中秋節"),
            ("2022-10-10", "中華民國國慶日"),
        )
