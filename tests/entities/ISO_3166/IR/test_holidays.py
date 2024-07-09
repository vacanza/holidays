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

from holidays.entities.ISO_3166.IR import IrHolidays
from tests.common import CommonCountryTests


class TestIrHolidays(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(IrHolidays)

    def test_no_holidays(self):
        self.assertNoHolidays(IrHolidays(years=1979))
        self.assertNoHolidays(IrHolidays(years=2102))

    def test_2022(self):
        self.assertHolidays(
            ("2022-01-06", "(تخمین زده) کشته‌شدن فاطمه زهرا"),
            ("2022-02-11", "پیروزی انقلاب ۵۷"),
            ("2022-02-14", "(تخمین زده) زادروز علی بن ابی‌طالب"),
            ("2022-02-28", "(تخمین زده) مبعث"),
            ("2022-03-18", "(تخمین زده) زادروز حجت بن الحسن"),
            ("2022-03-20", "ملی‌شدن صنعت نفت"),
            ("2022-03-21", "نوروز"),
            ("2022-03-22", "نوروز"),
            ("2022-03-23", "نوروز"),
            ("2022-03-24", "نوروز"),
            ("2022-04-01", "روز جمهوری اسلامی"),
            ("2022-04-02", "روز طبیعت"),
            ("2022-04-22", "(تخمین زده) کشته‌شدن علی بن ابی‌طالب"),
            ("2022-05-02", "(تخمین زده) عید فطر"),
            ("2022-05-03", "(تخمین زده) عید فطر"),
            ("2022-05-26", "(تخمین زده) کشته‌شدن جعفر صادق"),
            ("2022-06-04", "درگذشت سید روح‌الله خمینی"),
            ("2022-06-05", "تظاهرات ۱۵ خرداد"),
            ("2022-07-09", "(تخمین زده) عید قربان"),
            ("2022-07-17", "(تخمین زده) عید غدیر"),
            ("2022-08-07", "(تخمین زده) تاسوعا"),
            ("2022-08-08", "(تخمین زده) کشته‌شدن حسین بن علی، عاشورا"),
            ("2022-09-16", "(تخمین زده) چهلم حسین بن علی اربعین"),
            ("2022-09-24", "(تخمین زده) کشته‌شدن حسن مجتبی و درگذشت محمد"),
            ("2022-09-26", "(تخمین زده) کشته‌شدن علی بن موسی الرضا"),
            ("2022-10-04", "(تخمین زده) کشته‌شدن حسن عسکری"),
            ("2022-10-13", "(تخمین زده) زادروز محمد و جعفر صادق"),
            ("2022-12-27", "(تخمین زده) کشته‌شدن فاطمه زهرا"),
        )
