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
        super().setUpClass(JpHolidays, language="th")

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-02", "วันหยุดธนาคาร"),
            ("2022-01-03", "วันหยุดธนาคาร"),
            ("2022-01-10", "วันฉลองบรรลุนิติภาวะ"),
            ("2022-02-11", "วันชาติญี่ปุ่น"),
            ("2022-02-23", "วันคล้ายวันพระราชสมภพ สมเด็จพระจักรพรรดินารุฮิโตะ"),
            ("2022-03-21", "วันวสันตวิษุวัต"),
            ("2022-04-29", "วันโชวะ"),
            ("2022-05-03", "วันรัฐธรรมนูญ"),
            ("2022-05-04", "วันพฤกษชาติ"),
            ("2022-05-05", "วันเด็กแห่งชาติ"),
            ("2022-07-18", "วันแห่งทะเล"),
            ("2022-08-11", "วันแห่งภูเขา"),
            ("2022-09-19", "วันเคารพผู้สูงอายุ"),
            ("2022-09-23", "วันศารทวิษุวัต"),
            ("2022-10-10", "วันกีฬาแห่งชาติ"),
            ("2022-11-03", "วันวัฒนธรรม"),
            ("2022-11-23", "วันขอบคุณแรงงาน"),
            ("2022-12-31", "วันหยุดธนาคาร"),
        )
