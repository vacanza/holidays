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
        super().setUpClass(TwHolidays, language="th")

    def test_th(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "วันสถาปนาสาธารณรัฐจีน(ไต้หวัน)"),
            ("2022-01-31", "วันก่อนวันตรุษจีน"),
            ("2022-02-01", "วันตรุษจีน"),
            ("2022-02-02", "วันตรุษจีน"),
            ("2022-02-03", "วันตรุษจีน"),
            ("2022-02-04", "วันหยุด (แทน 22/01/2022)"),
            ("2022-02-28", "วันรำลึกสันติภาพ"),
            ("2022-04-04", "วันเด็กแห่งชาติ"),
            ("2022-04-05", "วันเช็งเม้ง"),
            ("2022-06-03", "วันไหว้บ๊ะจ่าง"),
            ("2022-09-09", "ชดเชยวันไหว้พระจันทร์"),
            ("2022-09-10", "วันไหว้พระจันทร์"),
            ("2022-10-10", "วันชาติสาธารณรัฐจีน(ไต้หวัน)"),
        )
