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

from holidays.entities.ISO_3166.EG import EgHolidays
from tests.common import CommonCountryTests


class TestEgypt(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(EgHolidays)

    def test_ar(self):
        self.assertLocalizedHolidays(
            ("2019-01-01", "رأس السنة الميلادية"),
            ("2019-01-07", "عيد الميلاد المجيد (تقويم قبطي)"),
            ("2019-01-25", "عيد ثورة 25 يناير"),
            ("2019-04-25", "عيد تحرير سيناء"),
            ("2019-04-28", "عيد الفصح القبطي"),
            ("2019-04-29", "شم النسيم"),
            ("2019-05-01", "عيد العمال"),
            ("2019-06-04", "(تقدير) عيد الفطر"),
            ("2019-06-05", "(تقدير) عطلة عيد الفطر"),
            ("2019-06-06", "(تقدير) عطلة عيد الفطر"),
            ("2019-06-30", "عيد ثورة 30 يونيو"),
            ("2019-07-23", "عيد ثورة 23 يوليو"),
            ("2019-08-10", "(تقدير) يوم عرفة"),
            ("2019-08-11", "(تقدير) عيد الأضحى"),
            ("2019-08-12", "(تقدير) عطلة عيد الأضحى"),
            ("2019-08-13", "(تقدير) عطلة عيد الأضحى"),
            ("2019-08-31", "(تقدير) رأس السنة الهجرية"),
            ("2019-10-06", "عيد القوات المسلحة"),
            ("2019-11-09", "(تقدير) عيد المولد النبوي"),
        )
