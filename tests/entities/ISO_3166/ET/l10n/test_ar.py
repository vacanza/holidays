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

from holidays.entities.ISO_3166.ET import EtHolidays
from tests.common import CommonCountryTests


class TestEtHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(EtHolidays, language="ar")

    def test_ar(self):
        self.assertLocalizedHolidays(
            ("2022-01-07", "عيد الميلاد"),
            ("2022-01-19", "عيد الغطاس"),
            ("2022-03-02", "العدوة"),
            ("2022-04-22", "جمعة جيدة"),
            ("2022-04-24", "عيد الفصح"),
            ("2022-05-01", "يوم العمال"),
            ("2022-05-02", "عيد الفطر"),
            ("2022-05-05", "يوم الوطنيين"),
            ("2022-05-28", "يوم سقوط ديرج"),
            ("2022-07-09", "عيد الأضحى"),
            ("2022-09-11", "السنة الإثيوبية الجديدة"),
            ("2022-09-27", "مسكل"),
            ("2022-10-08", "عيد المولد النبوي"),
        )
