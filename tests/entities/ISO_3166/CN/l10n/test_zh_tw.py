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
        super().setUpClass(CnHolidays, language="zh_TW")

    def test_zh_tw(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "元旦"),
            ("2022-01-03", "元旦（觀察日）"),
            ("2022-01-31", "休息日（2022-01-29日起取代）"),
            ("2022-02-01", "春節"),
            ("2022-02-02", "春節"),
            ("2022-02-03", "春節"),
            ("2022-02-04", "休息日（2022-01-30日起取代）"),
            ("2022-03-08", "國際婦女節"),
            ("2022-04-04", "休息日（2022-04-02日起取代）"),
            ("2022-04-05", "清明節"),
            ("2022-05-01", "勞動節"),
            ("2022-05-02", "勞動節（觀察日）"),
            ("2022-05-03", "休息日（2022-04-24日起取代）"),
            ("2022-05-04", "五四青年節; 休息日（2022-05-07日起取代）"),
            ("2022-06-01", "六一兒童節"),
            ("2022-06-03", "端午節"),
            ("2022-08-01", "建軍節"),
            ("2022-09-10", "中秋節"),
            ("2022-09-12", "中秋節（觀察日）"),
            ("2022-10-01", "國慶日"),
            ("2022-10-02", "國慶日"),
            ("2022-10-03", "國慶日"),
            ("2022-10-04", "國慶日（觀察日）"),
            ("2022-10-05", "國慶日（觀察日）"),
            ("2022-10-06", "休息日（2022-10-08日起取代）"),
            ("2022-10-07", "休息日（2022-10-09日起取代）"),
        )
