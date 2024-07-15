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

from holidays.entities.ISO_3166.KH import KhHolidays
from tests.common import CommonCountryTests


class TestKhHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(KhHolidays, language="th")

    def test_th(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "วันปีใหม่สากล"),
            ("2023-01-07", "วันชัยชนะเหนือระบอบฆ่าล้างเผ่าพันธุ์เขมรแดง"),
            ("2023-03-08", "วันสตรีสากล"),
            ("2023-04-14", "เทศกาลขึ้นปีใหม่ประเพณี"),
            ("2023-04-15", "เทศกาลขึ้นปีใหม่ประเพณี"),
            ("2023-04-16", "เทศกาลขึ้นปีใหม่ประเพณี"),
            ("2023-05-01", "วันแรงงานสากล"),
            ("2023-05-04", "วันวิสาขบูชา"),
            ("2023-05-08", "พระราชพิธีบุญจรดพระนังคัลแรกนาขวัญ"),
            (
                "2023-05-14",
                (
                    "พระราชพิธีเฉลิมพระชนมพรรษา พระบาทสมเด็จพระบรมนาถ นโรดมสีหมุนี "
                    "พระมหากษัตริย์แห่งราชอาณาจักรกัมพูชา"
                ),
            ),
            ("2023-06-18", "พระราชพิธีเฉลิมพระชนมพรรษา สมเด็จพระบรมราชินี นโรดม มนีนาถ สีหนุ"),
            ("2023-09-24", "วันรัฐธรรมนูญ"),
            ("2023-10-13", "เทศกาลงานวันสาร์ทภจุมบิณฑ์เขมร"),
            ("2023-10-14", "เทศกาลงานวันสาร์ทภจุมบิณฑ์เขมร"),
            (
                "2023-10-15",
                (
                    "วันสดุดีพระบาทสมเด็จพระบรมนาถนโรดม สีหนุ พระบิดาแห่งเอกราช "
                    "บูรณภาพแห่งดินแดน และเอกภาพของชาติกัมพูชา; เทศกาลงานวันสาร์ทภจุมบิณฑ์เขมร"
                ),
            ),
            (
                "2023-10-29",
                (
                    "พระราชพิธีเฉลิมฉลองการขึ้นครองราชสมบัติ พระบาทสมเด็จพระบรมนาถ นโรดมสีหมุนี "
                    "พระมหากษัตริย์แห่งราชอาณาจักรกัมพูชา"
                ),
            ),
            ("2023-11-09", "วันประกาศเอกราชจากฝรั่งเศส"),
            ("2023-11-26", "พระราชพิธีบุญแข่งเรือลอยกระทงไฟไหว้พระจันทร์และกินข้าวเม่า"),
            ("2023-11-27", "พระราชพิธีบุญแข่งเรือลอยกระทงไฟไหว้พระจันทร์และกินข้าวเม่า"),
            ("2023-11-28", "พระราชพิธีบุญแข่งเรือลอยกระทงไฟไหว้พระจันทร์และกินข้าวเม่า"),
        )
