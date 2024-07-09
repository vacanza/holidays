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

from holidays.entities.ISO_3166.CA import CaHolidays
from tests.common import CommonCountryTests


class TestCaHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(CaHolidays, language="th")

    def test_th(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-03", "ชดเชยวันขึ้นปีใหม่"),
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-05-23", "วันวิคตอเรีย"),
            ("2022-07-01", "วันชาติแคนาดา"),
            ("2022-09-05", "วันแรงงาน"),
            ("2022-09-30", "วันชาติแห่งความจริงและการปรองดอง"),
            ("2022-10-10", "วันขอบคุณพระเจ้า"),
            ("2022-11-11", "วันรำลึก"),
            ("2022-12-25", "วันคริสต์มาส"),
            ("2022-12-26", "ชดเชยวันคริสต์มาส; วันเปิดกล่องของขวัญ"),
            ("2022-12-27", "ชดเชยวันคริสต์มาส"),
        )
