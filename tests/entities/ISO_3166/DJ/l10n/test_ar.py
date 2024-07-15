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

from holidays.entities.ISO_3166.DJ import DjHolidays
from tests.common import CommonCountryTests


class TestDjHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(DjHolidays, language="ar")

    def test_ar(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "يوم السنة الجديدة"),
            ("2022-02-28", "(تقدير) الإسراء والمعراج"),
            ("2022-05-01", "عيد العمال"),
            ("2022-05-02", "(تقدير) عيد الفطر"),
            ("2022-05-03", "(تقدير) عطلة عيد الفطر"),
            ("2022-06-27", "عيد الإستقلال"),
            ("2022-06-28", "عطلة عيد الاستقلال"),
            ("2022-07-08", "(تقدير) يوم عرفة"),
            ("2022-07-09", "(تقدير) عيد الأضحى"),
            ("2022-07-10", "(تقدير) عطلة عيد الأضحى"),
            ("2022-07-30", "(تقدير) رأس السنة الهجرية"),
            ("2022-10-08", "(تقدير) عيد المولد النبوي"),
            ("2022-12-25", "عيد الميلاد المجيد"),
        )
