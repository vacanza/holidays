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

    def test_special(self):
        self.assertHoliday(
            "2020-08-03",
            "2021-05-12",
            "2021-05-16",
            "2021-08-08",
            "2022-05-01",
            "2022-07-12",
            "2022-07-13",
            "2023-04-24",
            "2023-04-25",
            "2023-07-02",
            "2023-07-20",
            "2024-04-09",
            "2025-06-09",
            "2026-03-19",
            "2026-03-23",
            "2026-05-31",
        )

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
        self.assertHolidayName(
            name,
            "2020-08-20",
            "2021-08-09",
            "2022-07-31",
            "2023-07-19",
            "2024-07-07",
            "2025-06-26",
            "2026-06-16",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_prophets_birthday(self):
        name = "عيد المولد النبوي"
        self.assertHolidayName(
            name,
            "2020-10-29",
            "2021-10-21",
            "2022-10-09",
            "2023-09-28",
            "2024-09-15",
            "2025-09-04",
            "2026-08-27",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_isra_and_miraj(self):
        name = "ليلة المعراج"
        self.assertHolidayName(
            name,
            "2023-02-19",
            "2024-02-08",
            "2025-01-30",
            "2026-01-18",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_fitr(self):
        name = "عيد الفطر"
        name_holiday = f"عطلة {name}"
        self.assertHolidayName(
            name,
            "2021-05-13",
            "2022-05-02",
            "2023-04-21",
            "2024-04-10",
            "2025-03-30",
            "2026-03-20",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

        self.assertHolidayName(
            name_holiday,
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
            "2026-03-21",
            "2026-03-22",
        )
        self.assertIslamicNoEstimatedHolidayName(name_holiday, self.full_range)

    def test_arafat_day(self):
        name = "يوم عرفة"
        self.assertHolidayName(
            name,
            "2020-07-30",
            "2021-07-19",
            "2022-07-08",
            "2023-06-27",
            "2024-06-15",
            "2025-06-05",
            "2026-05-26",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

    def test_eid_al_adha(self):
        name = "عيد الأضحى"
        name_holiday = f"عطلة {name}"
        self.assertHolidayName(
            name,
            "2020-07-31",
            "2021-07-20",
            "2022-07-09",
            "2023-06-28",
            "2024-06-16",
            "2025-06-06",
            "2026-05-27",
        )
        self.assertIslamicNoEstimatedHolidayName(name, self.full_range)

        self.assertHolidayName(
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
            "2026-05-28",
            "2026-05-29",
        )
        self.assertIslamicNoEstimatedHolidayName(name_holiday, self.full_range)

    def test_2022(self):
        self.assertHolidaysInYear(
            2022,
            ("2022-01-01", "رأس السنة الميلادية"),
            ("2022-02-25", "اليوم الوطني"),
            ("2022-02-26", "يوم التحرير"),
            ("2022-02-28", "ليلة المعراج (تقديري)"),
            ("2022-05-01", "عطلة عيد الفطر"),
            ("2022-05-02", "عيد الفطر"),
            ("2022-05-03", "عطلة عيد الفطر"),
            ("2022-05-04", "عطلة عيد الفطر"),
            ("2022-07-08", "يوم عرفة"),
            ("2022-07-09", "عيد الأضحى"),
            ("2022-07-10", "عطلة عيد الأضحى"),
            ("2022-07-11", "عطلة عيد الأضحى"),
            ("2022-07-12", "عطلة عيد الأضحى"),
            ("2022-07-13", "عطلة عيد الأضحى"),
            ("2022-07-31", "رأس السنة الهجرية"),
            ("2022-10-09", "عيد المولد النبوي"),
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
            ("2023-02-19", "ليلة المعراج"),
            ("2023-02-25", "اليوم الوطني"),
            ("2023-02-26", "يوم التحرير"),
            ("2023-04-21", "عيد الفطر"),
            ("2023-04-22", "عطلة عيد الفطر"),
            ("2023-04-23", "عطلة عيد الفطر"),
            ("2023-04-24", "عطلة عيد الفطر"),
            ("2023-04-25", "عطلة عيد الفطر"),
            ("2023-06-27", "يوم عرفة"),
            ("2023-06-28", "عيد الأضحى"),
            ("2023-06-29", "عطلة عيد الأضحى"),
            ("2023-06-30", "عطلة عيد الأضحى"),
            ("2023-07-02", "عطلة عيد الأضحى"),
            ("2023-07-19", "رأس السنة الهجرية"),
            ("2023-07-20", "رأس السنة الهجرية"),
            ("2023-09-28", "عيد المولد النبوي"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2023-01-01", "New Year's Day"),
            ("2023-02-19", "Isra' and Mi'raj"),
            ("2023-02-25", "National Day"),
            ("2023-02-26", "Liberation Day"),
            ("2023-04-21", "Eid al-Fitr"),
            ("2023-04-22", "Eid al-Fitr Holiday"),
            ("2023-04-23", "Eid al-Fitr Holiday"),
            ("2023-04-24", "Eid al-Fitr Holiday"),
            ("2023-04-25", "Eid al-Fitr Holiday"),
            ("2023-06-27", "Day of Arafah"),
            ("2023-06-28", "Eid al-Adha"),
            ("2023-06-29", "Eid al-Adha Holiday"),
            ("2023-06-30", "Eid al-Adha Holiday"),
            ("2023-07-02", "Eid al-Adha Holiday"),
            ("2023-07-19", "Islamic New Year"),
            ("2023-07-20", "Islamic New Year"),
            ("2023-09-28", "Prophet's Birthday"),
        )

    def test_l10n_ur_pk(self):
        self.assertLocalizedHolidays(
            "ur_PK",
            ("2023-01-01", "نئے سال کا دن"),
            ("2023-02-19", "شب معراج"),
            ("2023-02-25", "قومی دن"),
            ("2023-02-26", "یوم آزادی"),
            ("2023-04-21", "عید الفطر"),
            ("2023-04-22", "عید الفطر کی تعطیل"),
            ("2023-04-23", "عید الفطر کی تعطیل"),
            ("2023-04-24", "عید الفطر کی تعطیل"),
            ("2023-04-25", "عید الفطر کی تعطیل"),
            ("2023-06-27", "یوم عرفہ"),
            ("2023-06-28", "عید الاضحی"),
            ("2023-06-29", "عید الاضحی کی تعطیل"),
            ("2023-06-30", "عید الاضحی کی تعطیل"),
            ("2023-07-02", "عید الاضحی کی تعطیل"),
            ("2023-07-19", "اسلامی نیا سال"),
            ("2023-07-20", "اسلامی نیا سال"),
            ("2023-09-28", "عید میلاد النبی"),
        )
