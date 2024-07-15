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

from holidays.entities.ISO_3166.UA import UaHolidays
from tests.common import CommonCountryTests


class TestUaHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(UaHolidays, language="ar")

    def test_ar(self):
        self.assertLocalizedHolidays(
            ("2021-01-01", "السنة الجديدة"),
            ("2021-01-07", "عيد الميلاد (حسب التقويم اليولياني)"),
            ("2021-01-08", "يوم عطلة (استبدل من 16/01/2021)"),
            ("2021-03-08", "اليوم العالمي للمرأة"),
            ("2021-05-01", "عيد العمال"),
            ("2021-05-02", "عيد الفصح"),
            ("2021-05-03", "(يوم عطلة) عيد العمال"),
            ("2021-05-04", "(يوم عطلة) عيد الفصح"),
            ("2021-05-09", "يوم النصر على النازية في الحرب العالمية الثانية (يوم النصر)"),
            (
                "2021-05-10",
                "(يوم عطلة) يوم النصر على النازية في الحرب العالمية الثانية (يوم النصر)",
            ),
            ("2021-06-20", "الثالوث"),
            ("2021-06-21", "(يوم عطلة) الثالوث"),
            ("2021-06-28", "يوم الدستور في أوكرانيا"),
            ("2021-08-23", "يوم عطلة (استبدل من 28/08/2021)"),
            ("2021-08-24", "عيد استقلال أوكرانيا"),
            ("2021-10-14", "يوم المدافعين عن أوكرانيا"),
            ("2021-10-15", "يوم عطلة (استبدل من 23/10/2021)"),
            ("2021-12-25", "عيد الميلاد (حسب التقويم الغريغوري)"),
            ("2021-12-27", "(يوم عطلة) عيد الميلاد (حسب التقويم الغريغوري)"),
        )
