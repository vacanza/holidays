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

from holidays.entities.ISO_3166.BN import BnHolidays
from tests.common import CommonCountryTests


class TestBnHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(BnHolidays, language="th")

    def test_th(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "วันขึ้นปีใหม่"),
            ("2023-01-02", "ชดเชยวันขึ้นปีใหม่"),
            ("2023-01-22", "วันตรุษจีน"),
            ("2023-01-23", "ชดเชยวันตรุษจีน"),
            ("2023-02-18", "วันเมี๊ยะราจ"),
            ("2023-02-23", "วันชาติบรูไน"),
            ("2023-03-23", "วันแรกการถือศีลอด"),
            ("2023-04-08", "วันนูซุลอัลกุรอาน"),
            ("2023-04-22", "วันอีฎิ้ลฟิตริ"),
            ("2023-04-23", "วันอีฎิ้ลฟิตริ"),
            ("2023-04-24", "วันอีฎิ้ลฟิตริ"),
            ("2023-04-25", "ชดเชยวันอีฎิ้ลฟิตริ"),
            ("2023-05-31", "วันกองทัพบรูไน"),
            ("2023-06-29", "วันอีดิ้ลอัฎฮา"),
            ("2023-07-15", "วันเฉลิมพระชนมพรรษาสมเด็จพระราชาธิบดีสุลต่านฮัสซานัล โบลเกียห์"),
            ("2023-07-19", "วันขึ้นปีใหม่อิสลาม"),
            ("2023-09-28", "วันเมาลิดนบี"),
            ("2023-12-25", "วันคริสต์มาส"),
        )
