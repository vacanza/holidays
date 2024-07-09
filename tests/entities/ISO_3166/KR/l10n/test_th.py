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
        super().setUpClass(KrHolidays, language="th")

    def test_th(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "วันปีใหม่สากล"),
            ("2022-01-31", "วันก่อนเทศกาลซอลลัล"),
            ("2022-02-01", "เทศกาลซอลลัล"),
            ("2022-02-02", "วันหลังเทศกาลซอลลัล"),
            ("2022-03-01", "วันอิสรภาพ"),
            ("2022-03-09", "วันเลือกตั้งประธานาธิบดี"),
            ("2022-05-01", "วันแรงงาน"),
            ("2022-05-05", "วันเด็ก"),
            ("2022-05-08", "วันวิสาขบูชา"),
            ("2022-06-01", "วันเลือกตั้งท้องถิ่น"),
            ("2022-06-06", "วันรำลึกวีรชน"),
            ("2022-08-15", "วันฉลองอิสรภาพ"),
            ("2022-09-09", "วันก่อนเทศกาลชูซอก"),
            ("2022-09-10", "เทศกาลชูซอก"),
            ("2022-09-11", "วันหลังเทศกาลชูซอก"),
            ("2022-09-12", "ชดเชยเทศกาลชูซอก"),
            ("2022-10-03", "วันสถาปนาประเทศ"),
            ("2022-10-09", "วันฮันกึล"),
            ("2022-10-10", "ชดเชยวันฮันกึล"),
            ("2022-12-25", "วันคริสต์มาส"),
        )
