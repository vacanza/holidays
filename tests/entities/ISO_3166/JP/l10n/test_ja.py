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

from holidays.entities.ISO_3166.JP import JpHolidays
from tests.common import CommonCountryTests


class TestJpHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(JpHolidays)

    def test_ja(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "元日"),
            ("2022-01-02", "銀行休業日"),
            ("2022-01-03", "銀行休業日"),
            ("2022-01-10", "成人の日"),
            ("2022-02-11", "建国記念の日"),
            ("2022-02-23", "天皇誕生日"),
            ("2022-03-21", "春分の日"),
            ("2022-04-29", "昭和の日"),
            ("2022-05-03", "憲法記念日"),
            ("2022-05-04", "みどりの日"),
            ("2022-05-05", "こどもの日"),
            ("2022-07-18", "海の日"),
            ("2022-08-11", "山の日"),
            ("2022-09-19", "敬老の日"),
            ("2022-09-23", "秋分の日"),
            ("2022-10-10", "スポーツの日"),
            ("2022-11-03", "文化の日"),
            ("2022-11-23", "勤労感謝の日"),
            ("2022-12-31", "銀行休業日"),
        )
