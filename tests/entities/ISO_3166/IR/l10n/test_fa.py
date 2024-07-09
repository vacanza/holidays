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

    def test_fa(self):
        self.assertLocalizedHolidays(
            ("2023-02-04", "(تخمین زده) زادروز علی بن ابی‌طالب"),
            ("2023-02-11", "پیروزی انقلاب ۵۷"),
            ("2023-02-18", "(تخمین زده) مبعث"),
            ("2023-03-07", "(تخمین زده) زادروز حجت بن الحسن"),
            ("2023-03-20", "ملی‌شدن صنعت نفت"),
            ("2023-03-21", "نوروز"),
            ("2023-03-22", "نوروز"),
            ("2023-03-23", "نوروز"),
            ("2023-03-24", "نوروز"),
            ("2023-04-01", "روز جمهوری اسلامی"),
            ("2023-04-02", "روز طبیعت"),
            ("2023-04-12", "(تخمین زده) کشته‌شدن علی بن ابی‌طالب"),
            ("2023-04-21", "(تخمین زده) عید فطر"),
            ("2023-04-22", "(تخمین زده) عید فطر"),
            ("2023-05-15", "(تخمین زده) کشته‌شدن جعفر صادق"),
            ("2023-06-04", "درگذشت سید روح‌الله خمینی"),
            ("2023-06-05", "تظاهرات ۱۵ خرداد"),
            ("2023-06-28", "(تخمین زده) عید قربان"),
            ("2023-07-06", "(تخمین زده) عید غدیر"),
            ("2023-07-27", "(تخمین زده) تاسوعا"),
            ("2023-07-28", "(تخمین زده) کشته‌شدن حسین بن علی، عاشورا"),
            ("2023-09-05", "(تخمین زده) چهلم حسین بن علی اربعین"),
            ("2023-09-13", "(تخمین زده) کشته‌شدن حسن مجتبی و درگذشت محمد"),
            ("2023-09-15", "(تخمین زده) کشته‌شدن علی بن موسی الرضا"),
            ("2023-09-23", "(تخمین زده) کشته‌شدن حسن عسکری"),
            ("2023-10-02", "(تخمین زده) زادروز محمد و جعفر صادق"),
            ("2023-12-16", "(تخمین زده) کشته‌شدن فاطمه زهرا"),
        )
