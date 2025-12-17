#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

from unittest import TestCase

from holidays.countries.iran import Iran
from tests.common import CommonCountryTests


class TestIran(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Iran)

    def test_islamic_revolution_day(self):
        name = "پیروزی انقلاب اسلامی"
        self.assertHolidayName(
            name,
            "2020-02-11",
            "2021-02-10",
            "2022-02-11",
            "2023-02-11",
            "2024-02-11",
            "2025-02-10",
        )
        self.assertHolidayName(name, self.full_range)

    def test_iranian_oil_industry_nationalization_day(self):
        name = "روز ملی شدن صنعت نفت ایران"
        self.assertHolidayName(
            name,
            "2020-03-19",
            "2021-03-19",
            "2022-03-20",
            "2023-03-20",
            "2024-03-19",
            "2025-03-19",
        )
        self.assertHolidayName(name, self.full_range)

    def test_last_day_of_year(self):
        self.assertHolidayName(
            "آخرین روز سال",
            "2005-03-20",
            "2009-03-20",
            "2013-03-20",
            "2017-03-20",
            "2021-03-20",
            "2025-03-20",
        )

    def test_nowruz(self):
        name = "جشن نوروز"
        name_holiday = "عیدنوروز"
        self.assertHolidayName(
            name,
            "2020-03-20",
            "2021-03-21",
            "2022-03-21",
            "2023-03-21",
            "2024-03-20",
            "2025-03-21",
        )
        self.assertHolidayName(name, self.full_range)

        self.assertHolidayName(
            name_holiday,
            "2020-03-21",
            "2020-03-22",
            "2020-03-23",
            "2021-03-22",
            "2021-03-23",
            "2021-03-24",
            "2022-03-22",
            "2022-03-23",
            "2022-03-24",
            "2023-03-22",
            "2023-03-23",
            "2023-03-24",
            "2024-03-21",
            "2024-03-22",
            "2024-03-23",
            "2025-03-22",
            "2025-03-23",
            "2025-03-24",
        )
        self.assertHolidayNameCount(name_holiday, 3, self.full_range)

    def test_islamic_republic_day(self):
        name = "روز جمهوری اسلامی"
        self.assertHolidayName(
            name,
            "2020-03-31",
            "2021-04-01",
            "2022-04-01",
            "2023-04-01",
            "2024-03-31",
            "2025-04-01",
        )
        self.assertHolidayName(name, self.full_range)

    def test_natures_day(self):
        name = "روز طبیعت"
        self.assertHolidayName(
            name,
            "2020-04-01",
            "2021-04-02",
            "2022-04-02",
            "2023-04-02",
            "2024-04-01",
            "2025-04-02",
        )
        self.assertHolidayName(name, self.full_range)

    def test_death_of_imam_khomeini(self):
        name = "رحلت حضرت امام خمینی"
        self.assertHolidayName(
            name,
            "2020-06-03",
            "2021-06-04",
            "2022-06-04",
            "2023-06-04",
            "2024-06-03",
            "2025-06-04",
        )
        self.assertHolidayName(name, self.full_range)

    def test_15_khordad_uprising(self):
        name = "قیام 15 خرداد"
        self.assertHolidayName(
            name,
            "2020-06-04",
            "2021-06-05",
            "2022-06-05",
            "2023-06-05",
            "2024-06-04",
            "2025-06-05",
        )
        self.assertHolidayName(name, self.full_range)

    def test_tasua(self):
        name = "تاسوعای حسینی"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-08-29",
            "2021-08-18",
            "2022-08-07",
            "2023-07-27",
            "2024-07-15",
            "2025-07-05",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_ashura(self):
        name = "عاشورای حسینی"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-08-30",
            "2021-08-19",
            "2022-08-08",
            "2023-07-28",
            "2024-07-16",
            "2025-07-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_arbaeen(self):
        name = "اربعین حسینی"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-10-08",
            "2021-09-27",
            "2022-09-17",
            "2023-09-06",
            "2024-08-25",
            "2025-08-14",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_death_of_prophet_muhammad_and_martyrdom_of_hasan_ibn_ali(self):
        name = "رحلت رسول اکرم؛شهادت امام حسن مجتبی علیه السلام"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-10-16",
            "2021-10-05",
            "2022-09-25",
            "2023-09-14",
            "2024-09-02",
            "2025-08-22",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_matyrdom_of_ali_al_rida(self):
        name = "شهادت امام رضا علیه السلام"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-10-17",
            "2021-10-07",
            "2022-09-27",
            "2023-09-16",
            "2024-09-04",
            "2025-08-24",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_matyrdom_of_hasan_al_askari(self):
        name = "شهادت امام حسن عسکری علیه السلام"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-10-25",
            "2021-10-15",
            "2022-10-05",
            "2023-09-24",
            "2024-09-12",
            "2025-09-01",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_birthday_of_muhammad_and_imam_jafar_al_sadiq(self):
        name = "میلاد رسول اکرم و امام جعفر صادق علیه السلام"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-11-03",
            "2021-10-24",
            "2022-10-14",
            "2023-10-03",
            "2024-09-21",
            "2025-09-10",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_matyrdom_of_fatima(self):
        name = "شهادت حضرت فاطمه زهرا سلام الله علیها"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-01-29",
            "2021-01-17",
            "2022-01-06",
            "2022-12-27",
            "2023-12-17",
            "2024-12-05",
            "2025-11-24",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_birthday_of_imam_ali(self):
        name = "ولادت امام علی علیه السلام و روز پدر"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-03-08",
            "2021-02-25",
            "2022-02-15",
            "2023-02-04",
            "2024-01-25",
            "2025-01-14",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_isra_and_miraj(self):
        name = "مبعث رسول اکرم (ص)"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-03-22",
            "2021-03-11",
            "2022-03-01",
            "2023-02-18",
            "2024-02-08",
            "2025-01-28",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_birthday_of_mahdi(self):
        name = "ولادت حضرت قائم عجل الله تعالی فرجه و جشن نیمه شعبان"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-04-09",
            "2021-03-29",
            "2022-03-18",
            "2023-03-08",
            "2024-02-25",
            "2025-02-14",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_matyrdom_of_imam_ali(self):
        name = "شهادت حضرت علی علیه السلام"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-05-15",
            "2021-05-04",
            "2022-04-23",
            "2023-04-12",
            "2024-04-01",
            "2025-03-22",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_fitr(self):
        name = "عید سعید فطر"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-03",
            "2023-04-22",
            "2024-04-10",
            "2025-03-31",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_fitr_holiday(self):
        name = "تعطیل به مناسبت عید سعید فطر"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-05-25",
            "2021-05-14",
            "2022-05-04",
            "2023-04-23",
            "2024-04-11",
            "2025-04-01",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_matyrdom_of_imam_jafar_al_sadiq(self):
        name = "شهادت امام جعفر صادق علیه السلام"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-06-17",
            "2021-06-06",
            "2022-05-27",
            "2023-05-16",
            "2024-05-04",
            "2025-04-24",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_adha(self):
        name = "عید سعید قربان"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-07-31",
            "2021-07-21",
            "2022-07-10",
            "2023-06-29",
            "2024-06-17",
            "2025-06-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_ghadeer(self):
        name = "عید سعید غدیر خم"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-08-08",
            "2021-07-29",
            "2022-07-18",
            "2023-07-07",
            "2024-06-25",
            "2025-06-14",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_2021(self):
        self.assertHolidaysInYear(
            2021,
            ("2021-01-17", "شهادت حضرت فاطمه زهرا سلام الله علیها"),
            ("2021-02-10", "پیروزی انقلاب اسلامی"),
            ("2021-02-25", "ولادت امام علی علیه السلام و روز پدر"),
            ("2021-03-11", "مبعث رسول اکرم (ص)"),
            ("2021-03-19", "روز ملی شدن صنعت نفت ایران"),
            ("2021-03-20", "آخرین روز سال"),
            ("2021-03-21", "جشن نوروز"),
            ("2021-03-22", "عیدنوروز"),
            ("2021-03-23", "عیدنوروز"),
            ("2021-03-24", "عیدنوروز"),
            ("2021-03-29", "ولادت حضرت قائم عجل الله تعالی فرجه و جشن نیمه شعبان"),
            ("2021-04-01", "روز جمهوری اسلامی"),
            ("2021-04-02", "روز طبیعت"),
            ("2021-05-04", "شهادت حضرت علی علیه السلام"),
            ("2021-05-13", "عید سعید فطر"),
            ("2021-05-14", "تعطیل به مناسبت عید سعید فطر"),
            ("2021-06-04", "رحلت حضرت امام خمینی"),
            ("2021-06-05", "قیام 15 خرداد"),
            ("2021-06-06", "شهادت امام جعفر صادق علیه السلام"),
            ("2021-07-21", "عید سعید قربان"),
            ("2021-07-29", "عید سعید غدیر خم"),
            ("2021-08-18", "تاسوعای حسینی"),
            ("2021-08-19", "عاشورای حسینی"),
            ("2021-09-27", "اربعین حسینی"),
            ("2021-10-05", "رحلت رسول اکرم؛شهادت امام حسن مجتبی علیه السلام"),
            ("2021-10-07", "شهادت امام رضا علیه السلام"),
            ("2021-10-15", "شهادت امام حسن عسکری علیه السلام"),
            ("2021-10-24", "میلاد رسول اکرم و امام جعفر صادق علیه السلام"),
        )

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-06", "شهادت حضرت فاطمه زهرا سلام الله علیها"),
            ("2022-02-11", "پیروزی انقلاب اسلامی"),
            ("2022-02-15", "ولادت امام علی علیه السلام و روز پدر"),
            ("2022-03-01", "مبعث رسول اکرم (ص)"),
            ("2022-03-18", "ولادت حضرت قائم عجل الله تعالی فرجه و جشن نیمه شعبان"),
            ("2022-03-20", "روز ملی شدن صنعت نفت ایران"),
            ("2022-03-21", "جشن نوروز"),
            ("2022-03-22", "عیدنوروز"),
            ("2022-03-23", "عیدنوروز"),
            ("2022-03-24", "عیدنوروز"),
            ("2022-04-01", "روز جمهوری اسلامی"),
            ("2022-04-02", "روز طبیعت"),
            ("2022-04-23", "شهادت حضرت علی علیه السلام"),
            ("2022-05-03", "عید سعید فطر"),
            ("2022-05-04", "تعطیل به مناسبت عید سعید فطر"),
            ("2022-05-27", "شهادت امام جعفر صادق علیه السلام"),
            ("2022-06-04", "رحلت حضرت امام خمینی"),
            ("2022-06-05", "قیام 15 خرداد"),
            ("2022-07-10", "عید سعید قربان"),
            ("2022-07-18", "عید سعید غدیر خم"),
            ("2022-08-07", "تاسوعای حسینی"),
            ("2022-08-08", "عاشورای حسینی"),
            ("2022-09-17", "اربعین حسینی"),
            ("2022-09-25", "رحلت رسول اکرم؛شهادت امام حسن مجتبی علیه السلام"),
            ("2022-09-27", "شهادت امام رضا علیه السلام"),
            ("2022-10-05", "شهادت امام حسن عسکری علیه السلام"),
            ("2022-10-14", "میلاد رسول اکرم و امام جعفر صادق علیه السلام"),
            ("2022-12-27", "شهادت حضرت فاطمه زهرا سلام الله علیها"),
        )

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-02-04", "ولادت امام علی علیه السلام و روز پدر"),
            ("2023-02-11", "پیروزی انقلاب اسلامی"),
            ("2023-02-18", "مبعث رسول اکرم (ص)"),
            ("2023-03-08", "ولادت حضرت قائم عجل الله تعالی فرجه و جشن نیمه شعبان"),
            ("2023-03-20", "روز ملی شدن صنعت نفت ایران"),
            ("2023-03-21", "جشن نوروز"),
            ("2023-03-22", "عیدنوروز"),
            ("2023-03-23", "عیدنوروز"),
            ("2023-03-24", "عیدنوروز"),
            ("2023-04-01", "روز جمهوری اسلامی"),
            ("2023-04-02", "روز طبیعت"),
            ("2023-04-12", "شهادت حضرت علی علیه السلام"),
            ("2023-04-22", "عید سعید فطر"),
            ("2023-04-23", "تعطیل به مناسبت عید سعید فطر"),
            ("2023-05-16", "شهادت امام جعفر صادق علیه السلام"),
            ("2023-06-04", "رحلت حضرت امام خمینی"),
            ("2023-06-05", "قیام 15 خرداد"),
            ("2023-06-29", "عید سعید قربان"),
            ("2023-07-07", "عید سعید غدیر خم"),
            ("2023-07-27", "تاسوعای حسینی"),
            ("2023-07-28", "عاشورای حسینی"),
            ("2023-09-06", "اربعین حسینی"),
            ("2023-09-14", "رحلت رسول اکرم؛شهادت امام حسن مجتبی علیه السلام"),
            ("2023-09-16", "شهادت امام رضا علیه السلام"),
            ("2023-09-24", "شهادت امام حسن عسکری علیه السلام"),
            ("2023-10-03", "میلاد رسول اکرم و امام جعفر صادق علیه السلام"),
            ("2023-12-17", "شهادت حضرت فاطمه زهرا سلام الله علیها"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-02-04", "Birthday of Imam Ali"),
            ("2023-02-11", "Islamic Revolution Day"),
            ("2023-02-18", "Isra' and Mi'raj"),
            ("2023-03-08", "Birthday of Mahdi"),
            ("2023-03-20", "Iranian Oil Industry Nationalization Day"),
            ("2023-03-21", "Nowruz"),
            ("2023-03-22", "Nowruz Holiday"),
            ("2023-03-23", "Nowruz Holiday"),
            ("2023-03-24", "Nowruz Holiday"),
            ("2023-04-01", "Islamic Republic Day"),
            ("2023-04-02", "Nature's Day"),
            ("2023-04-12", "Martyrdom of Imam Ali"),
            ("2023-04-22", "Eid al-Fitr"),
            ("2023-04-23", "Eid al-Fitr Holiday"),
            ("2023-05-16", "Martyrdom of Imam Ja'far al-Sadiq"),
            ("2023-06-04", "Death of Imam Khomeini"),
            ("2023-06-05", "15 Khordad Uprising"),
            ("2023-06-29", "Eid al-Adha"),
            ("2023-07-07", "Eid al-Ghadeer"),
            ("2023-07-27", "Tasua"),
            ("2023-07-28", "Ashura"),
            ("2023-09-06", "Arbaeen"),
            ("2023-09-14", "Death of Prophet Muhammad and Martyrdom of Hasan ibn Ali"),
            ("2023-09-16", "Martyrdom of Ali al-Rida"),
            ("2023-09-24", "Martyrdom of Hasan al-Askari"),
            ("2023-10-03", "Birthday of Muhammad and Imam Ja'far al-Sadiq"),
            ("2023-12-17", "Martyrdom of Fatima"),
        )
