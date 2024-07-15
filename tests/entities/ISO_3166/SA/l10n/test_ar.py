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

from holidays.entities.ISO_3166.SA import SaHolidays
from tests.common import CommonCountryTests


class TestSaHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(SaHolidays)

    def test_ar(self):
        self.assertLocalizedHolidays(
            ("2023-02-22", "يوم التأسيسي"),
            ("2023-04-21", "(تقدير) عطلة عيد الفطر"),
            ("2023-04-22", "(تقدير) عطلة عيد الفطر"),
            ("2023-04-23", "(تقدير) عطلة عيد الفطر"),
            ("2023-04-24", "(تقدير) عطلة عيد الفطر"),
            ("2023-04-25", "(تقدير ملاحظة) عطلة عيد الفطر"),
            ("2023-04-26", "(تقدير ملاحظة) عطلة عيد الفطر"),
            ("2023-06-27", "(تقدير) يوم عرفة"),
            ("2023-06-28", "(تقدير) عطلة عيد الأضحى"),
            ("2023-06-29", "(تقدير) عطلة عيد الأضحى"),
            ("2023-06-30", "(تقدير) عطلة عيد الأضحى"),
            ("2023-07-02", "(تقدير ملاحظة) عطلة عيد الأضحى"),
            ("2023-09-23", "اليوم الوطني"),
            ("2023-09-24", "(ملاحظة) اليوم الوطني"),
        )
