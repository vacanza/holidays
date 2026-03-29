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

from holidays.countries.kuwait import Kuwait
from tests.common import CommonCountryTests


class TestKuwait(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Kuwait)

    def test_new_years_day(self):
        self.assertHolidayName(
            "رأس السنة الميلادية", (f"{year}-01-01" for year in self.full_range)
        )

    def test_national_day(self):
        self.assertHolidayName("اليوم الوطني", (f"{year}-02-25" for year in self.full_range))

    def test_liberation_day(self):
        self.assertHolidayName("يوم التحرير", (f"{year}-02-26" for year in self.full_range))

    def test_islamic_new_year(self):
        name = "رأس السنة الهجرية"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-08-20",
            "2021-08-09",
            "2022-07-30",
            "2023-07-19",
            "2024-07-07",
            "2025-06-26",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_prophets_birthday(self):
        name = "عيد المولد النبوي"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-10-29",
            "2021-10-18",
            "2022-10-08",
            "2023-09-27",
            "2024-09-15",
            "2025-09-04",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_isra_and_miraj(self):
        name = "ليلة المعراج"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-03-22",
            "2021-03-11",
            "2022-02-28",
            "2023-02-18",
            "2024-02-08",
            "2025-01-27",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_fitr(self):
        name = "عيد الفطر"
        name_holiday = f"عطلة {name}"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-05-24",
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

        self.assertIslamicNoEstimatedHolidayName(
            name_holiday,
            "2020-05-25",
            "2020-05-26",
            "2021-05-14",
            "2021-05-15",
            "2022-05-03",
            "2022-05-04",
            "2023-04-22",
            "2023-04-23",
            "2024-04-11",
            "2024-04-12",
            "2025-03-31",
            "2025-04-01",
        )
        self.assertIslamicNoEstimatedHolidayName(name_holiday, self.full_range)

    def test_arafat_day(self):
        name = "يوم عرفة"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-07-30",
            "2021-07-19",
            "2022-07-08",
            "2023-06-27",
            "2024-06-15",
            "2025-06-05",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_adha(self):
        name = "عيد الأضحى"
        name_holiday = f"عطلة {name}"
        self.assertIslamicNoEstimatedHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

        self.assertIslamicNoEstimatedHolidayName(
            name_holiday,
            "2020-08-01",
            "2020-08-02",
            "2021-07-21",
            "2021-07-22",
            "2022-07-10",
            "2022-07-11",
            "2023-06-29",
            "2023-06-30",
            "2024-06-17",
            "2024-06-18",
            "2025-06-07",
            "2025-06-08",
        )
        self.assertIslamicNoEstimatedHolidayName(name_holiday, self.full_range)

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "رأس السنة الميلادية"),
            ("2022-02-25", "اليوم الوطني"),
            ("2022-02-26", "يوم التحرير"),
            ("2022-02-28", "ليلة المعراج (المقدرة)"),
            ("2022-05-02", "عيد الفطر (المقدرة)"),
            ("2022-05-03", "عطلة عيد الفطر (المقدرة)"),
            ("2022-05-04", "عطلة عيد الفطر (المقدرة)"),
            ("2022-07-08", "يوم عرفة (المقدرة)"),
            ("2022-07-09", "عيد الأضحى (المقدرة)"),
            ("2022-07-10", "عطلة عيد الأضحى (المقدرة)"),
            ("2022-07-11", "عطلة عيد الأضحى (المقدرة)"),
            ("2022-07-30", "رأس السنة الهجرية (المقدرة)"),
            ("2022-10-08", "عيد المولد النبوي (المقدرة)"),
        )

    def test_weekend(self):
        for dt in (
            "2007-08-30",  # THU.
            "2007-08-31",  # FRI.
            "2007-09-01",  # SAT.
            "2007-09-07",  # FRI.
            "2007-09-08",  # SAT.
        ):
            self.assertTrue(self.holidays.is_weekend(dt))

        for dt in (
            "2007-08-25",  # SAT.
            "2007-08-26",  # SUN.
            "2007-09-02",  # SUN.
            "2007-09-06",  # THU.
        ):
            self.assertFalse(self.holidays.is_weekend(dt))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2023-01-01", "رأس السنة الميلادية"),
            ("2023-02-18", "ليلة المعراج (المقدرة)"),
            ("2023-02-25", "اليوم الوطني"),
            ("2023-02-26", "يوم التحرير"),
            ("2023-04-21", "عيد الفطر (المقدرة)"),
            ("2023-04-22", "عطلة عيد الفطر (المقدرة)"),
            ("2023-04-23", "عطلة عيد الفطر (المقدرة)"),
            ("2023-06-27", "يوم عرفة (المقدرة)"),
            ("2023-06-28", "عيد الأضحى (المقدرة)"),
            ("2023-06-29", "عطلة عيد الأضحى (المقدرة)"),
            ("2023-06-30", "عطلة عيد الأضحى (المقدرة)"),
            ("2023-07-19", "رأس السنة الهجرية (المقدرة)"),
            ("2023-09-27", "عيد المولد النبوي (المقدرة)"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-02-18", "Isra' and Mi'raj (estimated)"),
            ("2023-02-25", "National Day"),
            ("2023-02-26", "Liberation Day"),
            ("2023-04-21", "Eid al-Fitr (estimated)"),
            ("2023-04-22", "Eid al-Fitr Holiday (estimated)"),
            ("2023-04-23", "Eid al-Fitr Holiday (estimated)"),
            ("2023-06-27", "Arafat Day (estimated)"),
            ("2023-06-28", "Eid al-Adha (estimated)"),
            ("2023-06-29", "Eid al-Adha Holiday (estimated)"),
            ("2023-06-30", "Eid al-Adha Holiday (estimated)"),
            ("2023-07-19", "Islamic New Year (estimated)"),
            ("2023-09-27", "Prophet's Birthday (estimated)"),
        )
