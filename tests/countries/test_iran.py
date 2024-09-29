#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.iran import Iran, IR, IRN
from tests.common import CommonCountryTests


class TestIran(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Iran)

    def test_country_aliases(self):
        self.assertAliases(Iran, IR, IRN)

    def test_no_holidays(self):
        self.assertNoHolidays(Iran(years=1979))
        self.assertNoHolidays(Iran(years=2102))

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

    def test_l10n_default(self):
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

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-02-04", "Birthday of Ali (estimated)"),
            ("2023-02-11", "Islamic Revolution Day"),
            ("2023-02-18", "Isra' and Mi'raj (estimated)"),
            ("2023-03-07", "Birthday of Mahdi (estimated)"),
            ("2023-03-20", "Iranian Oil Industry Nationalization Day"),
            ("2023-03-21", "Persian New Year"),
            ("2023-03-22", "Persian New Year"),
            ("2023-03-23", "Persian New Year"),
            ("2023-03-24", "Persian New Year"),
            ("2023-04-01", "Islamic Republic Day"),
            ("2023-04-02", "Nature's Day"),
            ("2023-04-12", "Martyrdom of Ali (estimated)"),
            ("2023-04-21", "Eid al-Fitr (estimated)"),
            ("2023-04-22", "Eid al-Fitr (estimated)"),
            ("2023-05-15", "Martyrdom of Ja'far al-Sadiq (estimated)"),
            ("2023-06-04", "Death of Khomeini"),
            ("2023-06-05", "Khordad National Uprising"),
            ("2023-06-28", "Eid al-Adha (estimated)"),
            ("2023-07-06", "Eid al-Ghadeer (estimated)"),
            ("2023-07-27", "Tasua (estimated)"),
            ("2023-07-28", "Ashura (estimated)"),
            ("2023-09-05", "Arbaeen (estimated)"),
            ("2023-09-13", "Demise of Prophet Muhammad and Hasan ibn Ali (estimated)"),
            ("2023-09-15", "Martyrdom of Ali al-Rida (estimated)"),
            ("2023-09-23", "Martyrdom of Hasan al-Askari (estimated)"),
            ("2023-10-02", "Birthday of Muhammad and Ja'far al-Sadiq (estimated)"),
            ("2023-12-16", "Martyrdom of Fatima (estimated)"),
        )
