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

from holidays.entities.ISO_3166.AE import AeHolidays
from tests.common import CommonCountryTests


class TestAeHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(AeHolidays)

    def test_ar(self):
        self.assertLocalizedHolidays(
            ("2018-01-01", "رأس السنة الميلادية"),
            ("2018-04-13", "ليلة المعراج"),
            ("2018-06-14", "عيد الفطر"),
            ("2018-06-15", "عطلة عيد الفطر"),
            ("2018-06-16", "عطلة عيد الفطر"),
            ("2018-08-20", "وقفة عرفة"),
            ("2018-08-21", "عيد الأضحى"),
            ("2018-08-22", "عطلة عيد الأضحى"),
            ("2018-08-23", "عطلة عيد الأضحى"),
            ("2018-09-11", "رأس السنة الهجرية"),
            ("2018-11-19", "عيد المولد النبوي"),
            ("2018-11-30", "يوم الشهيد"),
            ("2018-12-02", "اليوم الوطني"),
            ("2018-12-03", "اليوم الوطني"),
        )
