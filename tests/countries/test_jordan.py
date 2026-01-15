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

from holidays.countries.jordan import Jordan
from tests.common import CommonCountryTests


class TestJordan(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Jordan)

    def test_new_years_day(self):
        self.assertHolidayName(
            "رأس السنة الميلادية", (f"{year}-01-01" for year in self.full_range)
        )

    def test_labor_day(self):
        self.assertHolidayName("عيد العمال", (f"{year}-05-01" for year in self.full_range))

    def test_independence_day(self):
        self.assertHolidayName("عيد الإستقلال", (f"{year}-05-25" for year in self.full_range))

    def test_christmas_day(self):
        self.assertHolidayName("عيد الميلاد المجيد", (f"{year}-12-25" for year in self.full_range))

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

    def test_weekend(self):
        for dt in (
            "1999-12-30",  # THU.
            "1999-12-31",  # FRI.
            "2000-01-07",  # FRI.
            "2000-01-08",  # SAT.
        ):
            self.assertTrue(self.holidays.is_weekend(dt))

        for dt in (
            "2000-01-01",  # SAT.
            "2000-01-02",  # SUN.
            "2000-01-06",  # THU.
            "2000-01-09",  # SUN.
        ):
            self.assertFalse(self.holidays.is_weekend(dt))

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2024-01-01", "رأس السنة الميلادية"),
            ("2024-02-08", "ليلة المعراج (المقدرة)"),
            ("2024-04-10", "عيد الفطر (المقدرة)"),
            ("2024-04-11", "عطلة عيد الفطر (المقدرة)"),
            ("2024-04-12", "عطلة عيد الفطر (المقدرة)"),
            ("2024-05-01", "عيد العمال"),
            ("2024-05-25", "عيد الإستقلال"),
            ("2024-06-15", "يوم عرفة (المقدرة)"),
            ("2024-06-16", "عيد الأضحى (المقدرة)"),
            ("2024-06-17", "عطلة عيد الأضحى (المقدرة)"),
            ("2024-06-18", "عطلة عيد الأضحى (المقدرة)"),
            ("2024-07-07", "رأس السنة الهجرية (المقدرة)"),
            ("2024-09-15", "عيد المولد النبوي (المقدرة)"),
            ("2024-12-25", "عيد الميلاد المجيد"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2024-01-01", "New Year's Day"),
            ("2024-02-08", "Isra' and Mi'raj (estimated)"),
            ("2024-04-10", "Eid al-Fitr (estimated)"),
            ("2024-04-11", "Eid al-Fitr Holiday (estimated)"),
            ("2024-04-12", "Eid al-Fitr Holiday (estimated)"),
            ("2024-05-01", "Labor Day"),
            ("2024-05-25", "Independence Day"),
            ("2024-06-15", "Arafat Day (estimated)"),
            ("2024-06-16", "Eid al-Adha (estimated)"),
            ("2024-06-17", "Eid al-Adha Holiday (estimated)"),
            ("2024-06-18", "Eid al-Adha Holiday (estimated)"),
            ("2024-07-07", "Islamic New Year (estimated)"),
            ("2024-09-15", "Prophet's Birthday (estimated)"),
            ("2024-12-25", "Christmas Day"),
        )
