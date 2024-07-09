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

from holidays.entities.ISO_3166.JO import JoHolidays
from tests.common import CommonCountryTests


class TestJoHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(JoHolidays)

    def test_2024(self):
        self.assertHolidays(
            JoHolidays(years=2024),
            ("2024-01-01", "رأس السنة الميلادية"),
            ("2024-02-08", "(تقدير) ليلة المعراج"),
            ("2024-04-10", "(تقدير) عيد الفطر"),
            ("2024-04-11", "(تقدير) عطلة عيد الفطر"),
            ("2024-04-12", "(تقدير) عطلة عيد الفطر"),
            ("2024-05-01", "عيد العمال"),
            ("2024-05-25", "عيد الإستقلال"),
            ("2024-06-15", "(تقدير) يوم عرفة"),
            ("2024-06-16", "(تقدير) عيد الأضحى"),
            ("2024-06-17", "(تقدير) عطلة عيد الأضحى"),
            ("2024-06-18", "(تقدير) عطلة عيد الأضحى"),
            ("2024-07-07", "(تقدير) رأس السنة الهجرية"),
            ("2024-09-15", "(تقدير) عيد المولد النبوي"),
            ("2024-12-25", "عيد الميلاد المجيد"),
        )
