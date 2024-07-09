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

from holidays.entities.ISO_3166.KR import KrHolidays
from tests.common import CommonCountryTests


class TestKrHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(KrHolidays)

    def test_ko(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "신정연휴"),
            ("2022-01-31", "설날 전날"),
            ("2022-02-01", "설날"),
            ("2022-02-02", "설날 다음날"),
            ("2022-03-01", "삼일절"),
            ("2022-03-09", "대통령 선거일"),
            ("2022-05-01", "근로자의날"),
            ("2022-05-05", "어린이날"),
            ("2022-05-08", "부처님오신날"),
            ("2022-06-01", "지방선거일"),
            ("2022-06-06", "현충일"),
            ("2022-08-15", "광복절"),
            ("2022-09-09", "추석 전날"),
            ("2022-09-10", "추석"),
            ("2022-09-11", "추석 다음날"),
            ("2022-09-12", "추석 대체 휴일"),
            ("2022-10-03", "개천절"),
            ("2022-10-09", "한글날"),
            ("2022-10-10", "한글날 대체 휴일"),
            ("2022-12-25", "기독탄신일"),
        )
