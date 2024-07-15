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

from holidays.entities.ISO_3166.CN import CnHolidays
from tests.common import CommonCountryTests


class TestCnHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CnHolidays)

    def test_zh_cn(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "元旦"),
            ("2022-01-03", "元旦（观察日）"),
            ("2022-01-31", "休息日（2022-01-29日起取代）"),
            ("2022-02-01", "春节"),
            ("2022-02-02", "春节"),
            ("2022-02-03", "春节"),
            ("2022-02-04", "休息日（2022-01-30日起取代）"),
            ("2022-03-08", "国际妇女节"),
            ("2022-04-04", "休息日（2022-04-02日起取代）"),
            ("2022-04-05", "清明节"),
            ("2022-05-01", "劳动节"),
            ("2022-05-02", "劳动节（观察日）"),
            ("2022-05-03", "休息日（2022-04-24日起取代）"),
            ("2022-05-04", "五四青年节; 休息日（2022-05-07日起取代）"),
            ("2022-06-01", "六一儿童节"),
            ("2022-06-03", "端午节"),
            ("2022-08-01", "建军节"),
            ("2022-09-10", "中秋节"),
            ("2022-09-12", "中秋节（观察日）"),
            ("2022-10-01", "国庆节"),
            ("2022-10-02", "国庆节"),
            ("2022-10-03", "国庆节"),
            ("2022-10-04", "国庆节（观察日）"),
            ("2022-10-05", "国庆节（观察日）"),
            ("2022-10-06", "休息日（2022-10-08日起取代）"),
            ("2022-10-07", "休息日（2022-10-09日起取代）"),
        )
