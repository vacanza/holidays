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
        super().setUpClass(TwHolidays, language="zh_CN")

    def test_zh_cn(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "中华民国开国纪念日"),
            ("2022-01-31", "农历除夕"),
            ("2022-02-01", "春节"),
            ("2022-02-02", "春节"),
            ("2022-02-03", "春节"),
            ("2022-02-04", "休息日（2022-01-22日起取代）"),
            ("2022-02-28", "和平纪念日"),
            ("2022-04-04", "儿童节"),
            ("2022-04-05", "清明节"),
            ("2022-06-03", "端午节"),
            ("2022-09-09", "中秋节（庆祝）"),
            ("2022-09-10", "中秋节"),
            ("2022-10-10", "中华民国国庆日"),
        )
