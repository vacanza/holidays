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

from holidays.entities.ISO_3166.MA import MaHolidays
from tests.common import CommonCountryTests


class TestMAHolicays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(MaHolidays)

    def test_ar(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "رأس السنة الميلادية"),
            ("2023-01-11", "ذكرى تقديم وثيقة الاستقلال"),
            ("2023-04-21", "(تقدير) عيد الفطر"),
            ("2023-04-22", "(تقدير) عيد الفطر"),
            ("2023-05-01", "عيد العمال"),
            ("2023-06-28", "(تقدير) عيد الأضحى"),
            ("2023-06-29", "(تقدير) عيد الأضحى"),
            ("2023-07-19", "(تقدير) رأس السنة الهجرية"),
            ("2023-07-30", "عيد العرش"),
            ("2023-08-14", "ذكرى استرجاع إقليم وادي الذهب"),
            ("2023-08-20", "ذكرى ثورة الملك و الشعب"),
            ("2023-08-21", "عيد الشباب"),
            ("2023-09-27", "(تقدير) عيد المولد النبوي"),
            ("2023-09-28", "(تقدير) عيد المولد النبوي"),
            ("2023-11-06", "ذكرى المسيرة الخضراء"),
            ("2023-11-18", "عيد الإستقلال"),
        )
