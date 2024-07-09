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
        super().setUpClass(CaHolidays, language="ar")

    def test_ar(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "يوم السنة الجديدة"),
            ("2022-01-03", "(تمت ملاحظته) يوم السنة الجديدة"),
            ("2022-04-15", "جمعة جيدة"),
            ("2022-05-23", "يوم فيكتوريا"),
            ("2022-07-01", "يوم كندا"),
            ("2022-09-05", "عيد العمال"),
            ("2022-09-30", "اليوم الوطني للحقيقة والمصالحة"),
            ("2022-10-10", "عيد الشكر"),
            ("2022-11-11", "يوم الذكرى"),
            ("2022-12-25", "عيد الميلاد"),
            ("2022-12-26", "(تمت ملاحظته) عيد الميلاد; يوم الملاكمة"),
            ("2022-12-27", "(تمت ملاحظته) عيد الميلاد"),
        )
