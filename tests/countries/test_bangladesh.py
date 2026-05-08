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

from holidays.countries.bangladesh import Bangladesh
from tests.common import CommonCountryTests


class TestBangladesh(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Bangladesh)

    def test_martyrs_day_and_international_mother_language_day(self):
        self.assertHolidayName(
            "শহীদ দিবস ও আন্তর্জাতিক মাতৃভাষা দিবস", (f"{year}-02-21" for year in self.full_range)
        )

    def test_sheikh_mujibur_rahmans_birthday(self):
        name = "জাতির পিতা বঙ্গবন্ধু শেখ মুজিবুর রহমান এর জন্মদিবস"
        self.assertHolidayName(name, (f"{year}-03-17" for year in range(self.start_year, 2025)))
        self.assertNoHolidayName(name, range(2025, self.end_year))

    def test_independence_day(self):
        self.assertHolidayName("স্বাধীনতা দিবস", (f"{year}-03-26" for year in self.full_range))

    def test_bengali_new_years_day(self):
        self.assertHolidayName("পহেলা বৈশাখ", (f"{year}-04-14" for year in self.full_range))

    def test_may_day(self):
        self.assertHolidayName("মে দিবস", (f"{year}-05-01" for year in self.full_range))

    def test_july_mass_uprising_day(self):
        name = "জুলাই গণ-অভ্যুত্থান দিবস"
        self.assertHolidayName(name, (f"{year}-08-05" for year in range(2025, self.end_year)))
        self.assertNoHolidayName(name, range(self.start_year, 2025))

    def test_national_mourning_day(self):
        name = "জাতীয় শোক দিবস"
        self.assertHolidayName(name, (f"{year}-08-15" for year in range(self.start_year, 2025)))
        self.assertNoHolidayName(name, range(2025, self.end_year))

    def test_victory_day(self):
        self.assertHolidayName("বিজয় দিবস", (f"{year}-12-16" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName("বড়দিন", (f"{year}-12-25" for year in self.full_range))

    def test_ashura_day(self):
        name = "আশুরা"
        self.assertHolidayName(
            name,
            "2022-08-09",
            "2023-07-29",
            "2024-07-17",
            "2025-07-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_prophets_birthday(self):
        name = "ঈদে মিলাদুন্নবী"
        self.assertHolidayName(
            name,
            "2022-10-09",
            "2023-09-28",
            "2024-09-16",
            "2025-09-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_mid_shaban(self):
        name = "শবে বরাত"
        self.assertHolidayName(
            name,
            "2022-03-19",
            "2023-03-08",
            "2024-02-26",
            "2025-02-15",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_laylat_al_qadr(self):
        name = "শবে কদর"
        self.assertHolidayName(
            name,
            "2022-04-29",
            "2023-04-19",
            "2024-04-07",
            "2025-03-28",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_jumuatul_wida(self):
        name = "জুমাতুল বিদা"
        self.assertHolidayName(
            name,
            "2022-04-29",
            "2023-04-21",
            "2024-04-05",
            "2025-03-28",
            "2026-03-20",
        )

    def test_eid_al_fitr(self):
        name = "ঈদুল ফিতর"
        self.assertHolidayName(
            name,
            "2023-04-22",
            "2023-04-23",
            "2023-04-24",
            "2022-05-03",
            "2022-05-04",
            "2022-05-05",
            "2024-04-11",
            "2024-04-12",
            "2024-04-10",
            "2025-03-31",
            "2025-04-01",
            "2025-04-02",
        )
        exception_years = {1968, 2000, 2033}
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 3, (year for year in self.full_range if year not in exception_years)
        )

        self.assertIslamicNoEstimatedHolidayNameCount(name, 6, exception_years)

    def test_eid_al_adha(self):
        name = "ঈদুল আজহা"
        self.assertHolidayName(
            name,
            "2022-07-11",
            "2022-07-12",
            "2022-07-10",
            "2023-06-29",
            "2023-06-30",
            "2023-07-01",
            "2024-06-17",
            "2024-06-18",
            "2024-06-19",
            "2025-06-07",
            "2025-06-08",
            "2025-06-09",
        )
        exception_years = {1974, 2006, 2007, 2039}
        self.assertIslamicNoEstimatedHolidayNameCount(
            name, 3, (year for year in self.full_range if year not in exception_years)
        )
        self.assertIslamicNoEstimatedHolidayNameCount(name, 4, 2006)

        self.assertIslamicNoEstimatedHolidayNameCount(name, 5, 2007)

        self.assertIslamicNoEstimatedHolidayNameCount(name, 6, 1974, 2039)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-02-21", "শহীদ দিবস ও আন্তর্জাতিক মাতৃভাষা দিবস"),
            ("2024-02-26", "শবে বরাত"),
            ("2024-03-17", "জাতির পিতা বঙ্গবন্ধু শেখ মুজিবুর রহমান এর জন্মদিবস"),
            ("2024-03-26", "স্বাধীনতা দিবস"),
            ("2024-04-05", "জুমাতুল বিদা"),
            ("2024-04-07", "শবে কদর"),
            ("2024-04-10", "ঈদুল ফিতর"),
            ("2024-04-11", "ঈদুল ফিতর"),
            ("2024-04-12", "ঈদুল ফিতর"),
            ("2024-04-14", "পহেলা বৈশাখ"),
            ("2024-05-01", "মে দিবস"),
            ("2024-06-17", "ঈদুল আজহা"),
            ("2024-06-18", "ঈদুল আজহা"),
            ("2024-06-19", "ঈদুল আজহা"),
            ("2024-07-17", "আশুরা"),
            ("2024-08-15", "জাতীয় শোক দিবস"),
            ("2024-09-16", "ঈদে মিলাদুন্নবী"),
            ("2024-12-16", "বিজয় দিবস"),
            ("2024-12-25", "বড়দিন"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-02-21", "Martyrs' Day and International Mother Language Day"),
            ("2024-02-26", "Mid-Sha'ban"),
            ("2024-03-17", "Sheikh Mujibur Rahman's Birthday"),
            ("2024-03-26", "Independence Day"),
            ("2024-04-05", "Jumu'atul-Wida"),
            ("2024-04-07", "Night of Power"),
            ("2024-04-10", "Eid al-Fitr"),
            ("2024-04-11", "Eid al-Fitr"),
            ("2024-04-12", "Eid al-Fitr"),
            ("2024-04-14", "Bengali New Year's Day"),
            ("2024-05-01", "May Day"),
            ("2024-06-17", "Eid al-Adha"),
            ("2024-06-18", "Eid al-Adha"),
            ("2024-06-19", "Eid al-Adha"),
            ("2024-07-17", "Ashura"),
            ("2024-08-15", "National Mourning Day"),
            ("2024-09-16", "Mawlid"),
            ("2024-12-16", "Victory Day"),
            ("2024-12-25", "Christmas Day"),
        )

    def test_l10n_ar(self):
        self.assertLocalizedHolidays(
            "ar",
            ("2024-02-21", "يوم الشهداء واليوم الدولي للغة الأم"),
            ("2024-02-26", "ليلة النصف من شعبان"),
            ("2024-03-17", "عيد ميلاد الشيخ مجيب الرحمن"),
            ("2024-03-26", "عيد الاستقلال"),
            ("2024-04-05", "جمعة الوداع"),
            ("2024-04-07", "ليلة القدر"),
            ("2024-04-10", "عيد الفطر"),
            ("2024-04-11", "عيد الفطر"),
            ("2024-04-12", "عيد الفطر"),
            ("2024-04-14", "رأس السنة البنغالية"),
            ("2024-05-01", "الأول من مايو"),
            ("2024-06-17", "عيد الأضحى"),
            ("2024-06-18", "عيد الأضحى"),
            ("2024-06-19", "عيد الأضحى"),
            ("2024-07-17", "عاشوراء"),
            ("2024-08-15", "اليوم الوطني للحداد"),
            ("2024-09-16", "المولد النبوي الشريف"),
            ("2024-12-16", "عيد النصر"),
            ("2024-12-25", "عيد الميلاد"),
        )
