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
        super().setUpClass(CnHolidays, language="th")

    def test_th(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "วันปีใหม่สากล"),
            ("2022-01-03", "ชดเชยวันปีใหม่สากล"),
            ("2022-01-31", "วันหยุด (แทน 29/01/2022)"),
            ("2022-02-01", "วันตรุษจีน"),
            ("2022-02-02", "วันตรุษจีน"),
            ("2022-02-03", "วันตรุษจีน"),
            ("2022-02-04", "วันหยุด (แทน 30/01/2022)"),
            ("2022-03-08", "วันสตรีสากล"),
            ("2022-04-04", "วันหยุด (แทน 02/04/2022)"),
            ("2022-04-05", "วันเช็งเม้ง"),
            ("2022-05-01", "วันแรงงาน"),
            ("2022-05-02", "ชดเชยวันแรงงาน"),
            ("2022-05-03", "วันหยุด (แทน 24/04/2022)"),
            ("2022-05-04", "วันหยุด (แทน 07/05/2022); วันเยาวชนห่งชาติจีน"),
            ("2022-06-01", "วันเด็กสากล"),
            ("2022-06-03", "วันไหว้บ๊ะจ่าง"),
            ("2022-08-01", "วันสถาปนากองทัพปลดปล่อยประชาชนจีน"),
            ("2022-09-10", "วันไหว้พระจันทร์"),
            ("2022-09-12", "ชดเชยวันไหว้พระจันทร์"),
            ("2022-10-01", "วันชาติจีน"),
            ("2022-10-02", "วันชาติจีน"),
            ("2022-10-03", "วันชาติจีน"),
            ("2022-10-04", "ชดเชยวันชาติจีน"),
            ("2022-10-05", "ชดเชยวันชาติจีน"),
            ("2022-10-06", "วันหยุด (แทน 08/10/2022)"),
            ("2022-10-07", "วันหยุด (แทน 09/10/2022)"),
        )
